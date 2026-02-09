#!/usr/bin/env python3
"""
Fetch last-12-month submissions from r/PublicRelations and synthesize media-monitoring gaps.

Design goals:
- Scan EVERY post in the time window (title/selftext metadata).
- Pull comments only for posts likely related to media monitoring (to keep runtime sane).
- No third-party dependencies; standard library only.

Outputs:
- analysis/reddit_publicrelations_<start>_to_<end>_posts.jsonl
- analysis/reddit_publicrelations_<start>_to_<end>_threads.jsonl (only monitoring-related, includes sampled comments)
- analysis/reddit_publicrelations_<start>_to_<end>_report.md
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, Iterable, List, Optional, Tuple


USER_AGENT = "media-monitoring-gap-analysis/1.0 (contact: internal-research)"
BASE = "https://www.reddit.com"


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def iso_date(d: dt.datetime) -> str:
    return d.date().isoformat()


def http_get_json(url: str, timeout_s: int = 30) -> Any:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        raw = resp.read()
    return json.loads(raw.decode("utf-8", errors="replace"))


def sleep_backoff(attempt: int) -> None:
    # Simple exponential backoff with cap (seconds).
    time.sleep(min(30.0, 1.5 ** attempt))


def safe_write_jsonl(path: str, rows: Iterable[Dict[str, Any]]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False))
            f.write("\n")


def append_jsonl(path: str, row: Dict[str, Any]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False))
        f.write("\n")


def to_permalink_url(permalink: str) -> str:
    # permalink already begins with /r/...
    return f"{BASE}{permalink}"


def submission_listing_url(subreddit: str, after: Optional[str] = None, limit: int = 100) -> str:
    # Use /new.json and stop once we go beyond the start window.
    q = {"limit": str(limit), "raw_json": "1"}
    if after:
        q["after"] = after
    return f"{BASE}/r/{urllib.parse.quote(subreddit)}/new.json?{urllib.parse.urlencode(q)}"


def thread_json_url(permalink: str, limit: int = 500) -> str:
    # Reddit thread JSON is a list of [postListing, commentListing]
    q = {"raw_json": "1", "limit": str(limit)}
    return f"{to_permalink_url(permalink)}.json?{urllib.parse.urlencode(q)}"


@dataclasses.dataclass(frozen=True)
class Submission:
    id: str
    fullname: str
    created_utc: int
    title: str
    selftext: str
    permalink: str
    url: str
    author: str
    score: int
    num_comments: int
    flair: str

    @property
    def created_dt(self) -> dt.datetime:
        return dt.datetime.fromtimestamp(self.created_utc, tz=dt.timezone.utc)


def parse_submission(child: Dict[str, Any]) -> Submission:
    d = child.get("data", {})
    return Submission(
        id=str(d.get("id", "")),
        fullname=str(d.get("name", "")),
        created_utc=int(d.get("created_utc", 0)),
        title=str(d.get("title", "") or ""),
        selftext=str(d.get("selftext", "") or ""),
        permalink=str(d.get("permalink", "") or ""),
        url=str(d.get("url", "") or ""),
        author=str(d.get("author", "") or ""),
        score=int(d.get("score", 0) or 0),
        num_comments=int(d.get("num_comments", 0) or 0),
        flair=str(d.get("link_flair_text", "") or ""),
    )


VENDORS = {
    # Primary competitors (user request).
    "meltwater": [r"\bmeltwater\b"],
    "cision": [r"\bcision\b", r"\bcisionone\b", r"\bpr\s*newswire\b", r"\bbrandwatch\b"],
    "muck_rack": [r"\bmuck\s*rack\b", r"\bmuckrack\b"],
    "brand24": [r"\bbrand\s*24\b", r"\bbrand24\b"],
    # Adjacent tools sometimes co-mentioned in monitoring threads.
    "talkwalker": [r"\btalkwalker\b"],
    "google_alerts": [r"\bgoogle\s*alerts\b"],
    # Avoid false positives on the English verb "mention".
    "mention_tool": [r"\bmention\.com\b", r"\bmentionlytics\b", r"\bmention\s+tool\b"],
}


PAIN_CATEGORIES: Dict[str, List[str]] = {
    "pricing_contracts": [
        "price", "pricing", "renew", "renewal", "contract", "annual", "auto-renew", "autorenew",
        "upsell", "quote", "negotiat", "nda", "cancel", "termination",
    ],
    "support_cs": ["support", "customer service", "account manager", "am ", "cs m", "csm", "unresponsive", "ghost"],
    "coverage_recall": ["miss", "missing", "coverage", "clip", "clipping", "catch", "recall", "index", "sources"],
    "paywalls_licensing": ["paywall", "paywalled", "licensed", "licensing", "full text", "full-text", "copyright"],
    "ux_workflow": ["clunky", "ui", "ux", "workflow", "hard to use", "confusing", "learning curve", "training"],
    "boolean_search": ["boolean", "query", "queries", "near/", "proximity", "syntax", "operators"],
    "reporting_export": ["report", "reporting", "export", "pdf", "ppt", "powerpoint", "csv", "dashboard"],
    "sentiment_accuracy": ["sentiment", "false positive", "false negative", "accuracy", "relevance", "noise"],
    "social_channels": ["social", "linkedin", "instagram", "facebook", "tiktok", "twitter", "x ", "youtube", "reddit"],
    "alerts_latency": ["alert", "alerts", "real-time", "realtime", "delay", "latency", "digest"],
    "integrations": ["slack", "teams", "api", "webhook", "crm", "salesforce", "hubspot", "integration"],
}


def normalize_text(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip().lower()


def detect_vendors(text: str) -> List[str]:
    t = normalize_text(text)
    found: List[str] = []
    for vendor, needles in VENDORS.items():
        for n in needles:
            if re.search(n, t):
                found.append(vendor)
                break
    return found


def detect_pains(text: str) -> List[str]:
    t = normalize_text(text)
    found: List[str] = []
    for cat, needles in PAIN_CATEGORIES.items():
        for n in needles:
            if n in t:
                found.append(cat)
                break
    return found


MONITORING_KEYWORDS = [
    r"\bmedia\s+monitoring\b",
    r"\bsocial\s+listening\b",
    r"\bmonitoring\s+(tool|platform|software|service)\b",
    r"\bpress\s+clippings?\b",
    r"\bnews\s+clippings?\b",
    r"\bcoverage\s+report(s)?\b",
    r"\bshare\s+of\s+voice\b",
    r"\bsov\b",
    r"\bboolean\s+search\b",
]

MONITORING_CONTEXT = [
    r"\balternatives?\b",
    r"\brecommend(ation)?s?\b",
    r"\bpricing\b",
    r"\bcontract(s)?\b",
    r"\brenew(al)?\b",
    r"\bdemo\b",
    r"\bsubscription\b",
]


def is_monitoring_related(sub: Submission) -> bool:
    blob = normalize_text(f"{sub.title}\n{sub.selftext}")
    if detect_vendors(blob):
        return True
    if any(re.search(k, blob) for k in MONITORING_KEYWORDS) and any(re.search(c, blob) for c in MONITORING_CONTEXT):
        return True
    return False


def is_monitoring_related_text(text: str) -> bool:
    t = normalize_text(text)
    if detect_vendors(t):
        return True
    # If it looks like a "tool choice / monitoring workflow" thread.
    if any(re.search(k, t) for k in MONITORING_KEYWORDS) and any(re.search(c, t) for c in MONITORING_CONTEXT):
        return True
    return False


def extract_comments(comment_listing: Dict[str, Any], max_comments: int) -> List[Dict[str, Any]]:
    # Flatten only top-level comments; keep high-signal fields.
    out: List[Dict[str, Any]] = []
    children = comment_listing.get("data", {}).get("children", [])
    for ch in children:
        kind = ch.get("kind")
        data = ch.get("data", {})
        if kind != "t1":
            continue
        body = data.get("body")
        if not body:
            continue
        out.append(
            {
                "id": str(data.get("id", "")),
                "author": str(data.get("author", "")),
                "score": int(data.get("score", 0) or 0),
                "created_utc": int(data.get("created_utc", 0) or 0),
                "body": str(body),
            }
        )
        if len(out) >= max_comments:
            break
    return out


def crawl_submissions(
    subreddit: str,
    start_utc: int,
    end_utc: int,
    per_page: int,
    min_delay_s: float,
    max_pages: Optional[int],
) -> List[Submission]:
    subs: List[Submission] = []
    after: Optional[str] = None
    pages = 0

    while True:
        if max_pages is not None and pages >= max_pages:
            break
        url = submission_listing_url(subreddit=subreddit, after=after, limit=per_page)
        attempt = 0
        while True:
            try:
                payload = http_get_json(url)
                break
            except urllib.error.HTTPError as e:
                attempt += 1
                if e.code in (429, 500, 502, 503, 504) and attempt <= 6:
                    sleep_backoff(attempt)
                    continue
                raise
            except urllib.error.URLError:
                attempt += 1
                if attempt <= 6:
                    sleep_backoff(attempt)
                    continue
                raise

        data = payload.get("data", {})
        children = data.get("children", [])
        if not children:
            break

        pages += 1
        after = data.get("after")

        oldest_seen = None
        for ch in children:
            sub = parse_submission(ch)
            if not sub.id or not sub.permalink:
                continue
            if sub.created_utc > end_utc:
                continue
            if sub.created_utc < start_utc:
                oldest_seen = sub.created_utc if oldest_seen is None else min(oldest_seen, sub.created_utc)
                continue
            subs.append(sub)
            oldest_seen = sub.created_utc if oldest_seen is None else min(oldest_seen, sub.created_utc)

        # Stop once listing has gone beyond our start window.
        if oldest_seen is not None and oldest_seen < start_utc:
            break

        if not after:
            break

        time.sleep(min_delay_s)

    return subs


def fetch_thread_details(permalink: str, max_comments: int, min_delay_s: float) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    url = thread_json_url(permalink, limit=max(100, max_comments))
    attempt = 0
    while True:
        try:
            payload = http_get_json(url)
            break
        except urllib.error.HTTPError as e:
            attempt += 1
            if e.code in (429, 500, 502, 503, 504) and attempt <= 6:
                sleep_backoff(attempt)
                continue
            raise
        except urllib.error.URLError:
            attempt += 1
            if attempt <= 6:
                sleep_backoff(attempt)
                continue
            raise

    # payload is [post_listing, comment_listing]
    post_listing = payload[0] if isinstance(payload, list) and payload else {}
    comment_listing = payload[1] if isinstance(payload, list) and len(payload) > 1 else {}

    # Extract basic post data to avoid surprises.
    post_children = post_listing.get("data", {}).get("children", [])
    post = post_children[0].get("data", {}) if post_children else {}

    comments = extract_comments(comment_listing, max_comments=max_comments)
    time.sleep(min_delay_s)
    return post, comments


def build_report(
    subreddit: str,
    start_dt: dt.datetime,
    end_dt: dt.datetime,
    submissions: List[Submission],
    threads: List[Dict[str, Any]],
) -> str:
    start_s = iso_date(start_dt)
    end_s = iso_date(end_dt)

    total_posts = len(submissions)
    monitoring_posts = len(threads)

    # Aggregate pains/vendors based on combined (post+comments) text.
    pain_counts: Dict[str, int] = {k: 0 for k in PAIN_CATEGORIES}
    vendor_counts: Dict[str, int] = {k: 0 for k in VENDORS}
    vendor_pain_counts: Dict[Tuple[str, str], int] = {}

    for th in threads:
        blob = normalize_text(th.get("analysis_text", ""))
        pains = detect_pains(blob)
        vendors = detect_vendors(blob)
        for p in pains:
            pain_counts[p] += 1
        for v in vendors:
            vendor_counts[v] += 1
        for v in vendors:
            for p in pains:
                vendor_pain_counts[(v, p)] = vendor_pain_counts.get((v, p), 0) + 1

    def top_items(d: Dict[str, int], n: int = 8) -> List[Tuple[str, int]]:
        return sorted(d.items(), key=lambda kv: kv[1], reverse=True)[:n]

    top_pains = top_items(pain_counts, n=10)
    top_vendors = top_items(vendor_counts, n=10)

    # Heuristic: "gap" pains are those frequently mentioned across >=2 major vendors.
    major_vendors = ["meltwater", "cision", "muck_rack", "brand24"]
    gap_pains: List[str] = []
    for p in PAIN_CATEGORIES.keys():
        v_hit = sum(1 for v in major_vendors if vendor_pain_counts.get((v, p), 0) > 0)
        if v_hit >= 2 and pain_counts.get(p, 0) > 0:
            gap_pains.append(p)

    def pain_label(p: str) -> str:
        return {
            "pricing_contracts": "Pricing + contracts",
            "support_cs": "Support + account mgmt",
            "coverage_recall": "Coverage + recall (missed clips)",
            "paywalls_licensing": "Paywalls + licensing",
            "ux_workflow": "UX + workflow friction",
            "boolean_search": "Boolean/search complexity",
            "reporting_export": "Reporting + export",
            "sentiment_accuracy": "Accuracy + sentiment",
            "social_channels": "Social channel gaps",
            "alerts_latency": "Alerts + latency",
            "integrations": "Integrations + API",
        }.get(p, p)

    # Mermaid gap diagram (compact).
    mermaid_lines = [
        "```mermaid",
        "flowchart TB",
        f'  A["r/{subreddit} (last 12 months)\\nPosts scanned: {total_posts}\\nMonitoring-related threads: {monitoring_posts}"]',
        '  A --> JTBD["JTBD: Detect mentions -> Prioritize -> Explain -> Report/Prove impact"]',
    ]
    for p in gap_pains[:10]:
        mermaid_lines.append(f'  JTBD --> P_{p}["Pain: {pain_label(p)}"]')
    mermaid_lines.append('  JTBD --> W["White space: Trust + Signal + Self-serve\\n(with credible coverage + licensing)"]')
    mermaid_lines.append("```")

    # Build vendor x pain table.
    header = ["Pain"] + [v for v in major_vendors]
    table_lines = ["| " + " | ".join(header) + " |", "| " + " | ".join(["---"] * len(header)) + " |"]
    for p in PAIN_CATEGORIES.keys():
        row = [pain_label(p)]
        for v in major_vendors:
            row.append(str(vendor_pain_counts.get((v, p), 0)))
        table_lines.append("| " + " | ".join(row) + " |")

    # Representative threads: pick top by comment count, then score.
    reps = sorted(threads, key=lambda t: (t.get("num_comments", 0), t.get("score", 0)), reverse=True)[:25]
    rep_lines = ["| Date (UTC) | Title | Vendors | Pains |", "| --- | --- | --- | --- |"]
    for t in reps:
        title = t.get("title", "").replace("|", "\\|")
        permalink = t.get("permalink", "")
        url = to_permalink_url(permalink) if permalink else t.get("url", "")
        vendors = ", ".join(t.get("vendors", []))
        pains = ", ".join([pain_label(p) for p in t.get("pains", [])])
        created = t.get("created_utc", 0)
        created_s = dt.datetime.fromtimestamp(int(created), tz=dt.timezone.utc).date().isoformat() if created else ""
        rep_lines.append(f"| {created_s} | [{title}]({url}) | {vendors} | {pains} |")

    lines: List[str] = []
    lines.append(f"# r/{subreddit} — Media Monitoring Gap Analysis ({start_s} to {end_s})")
    lines.append("")
    lines.append("## Dataset")
    lines.append(f"- Posts scanned (all): **{total_posts}**")
    lines.append(f"- Monitoring-related threads (deep analyzed): **{monitoring_posts}**")
    lines.append("")
    lines.append("## Top Pain Themes (by thread mentions)")
    for k, v in top_pains:
        lines.append(f"- {pain_label(k)}: **{v}**")
    lines.append("")
    lines.append("## Top Vendors Mentioned (by thread mentions)")
    for k, v in top_vendors:
        lines.append(f"- {k}: **{v}**")
    lines.append("")
    lines.append("## Visual Gap Map")
    lines.extend(mermaid_lines)
    lines.append("")
    lines.append("## Vendor vs Pain Heatmap (counts by thread)")
    lines.extend(table_lines)
    lines.append("")
    lines.append("## Representative Threads (highest engagement)")
    lines.extend(rep_lines)
    lines.append("")
    lines.append("## Consultant Synthesis: Current Market Gaps")
    lines.append("- Trust wedge: transparent pricing, cancellation, and renewal policies (anti-trap) are still a core differentiator.")
    lines.append("- Signal wedge: teams still want 'what matters and why' rather than more mentions; prioritization + narrative clarity remains underserved.")
    lines.append("- Coverage wedge: measurable recall/coverage quality and credible paywall/licensing strategy remain persistent gaps.")
    lines.append("- Workflow wedge: reporting/export and day-to-day UX still cause teams to stitch together tools and manual work.")
    lines.append("")
    lines.append("## Notes")
    lines.append("- This report is based on rule-based topic detection; it is designed to be explainable and auditable against the thread index.")
    return "\n".join(lines)


def load_jsonl(path: str) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    if not os.path.exists(path):
        return out
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except Exception:
                continue
    return out


def load_threads_index(threads_path: str) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, Dict[str, Any]]]:
    """
    Returns (ok_by_fullname, error_by_fullname).
    We treat rows with a non-empty 'error' as retryable.
    """
    ok: Dict[str, Dict[str, Any]] = {}
    err: Dict[str, Dict[str, Any]] = {}
    for row in load_jsonl(threads_path):
        fn = str(row.get("fullname", "") or "")
        if not fn:
            continue
        if row.get("error"):
            err[fn] = row
        else:
            ok[fn] = row
    return ok, err


def build_report_from_files(subreddit: str, posts_path: str, threads_path: str, report_path: str, start_dt: dt.datetime, end_dt: dt.datetime) -> None:
    submissions: List[Submission] = []
    for row in load_jsonl(posts_path):
        try:
            submissions.append(
                Submission(
                    id=str(row.get("id", "")),
                    fullname=str(row.get("fullname", "")),
                    created_utc=int(row.get("created_utc", 0)),
                    title=str(row.get("title", "") or ""),
                    selftext=str(row.get("selftext", "") or ""),
                    permalink=str(row.get("permalink", "") or ""),
                    url=str(row.get("url", "") or ""),
                    author=str(row.get("author", "") or ""),
                    score=int(row.get("score", 0) or 0),
                    num_comments=int(row.get("num_comments", 0) or 0),
                    flair=str(row.get("flair", "") or ""),
                )
            )
        except Exception:
            continue

    # De-dupe threads by fullname: prefer rows without errors, then richer comment sample.
    raw_threads = load_jsonl(threads_path)
    best_by_fullname: Dict[str, Dict[str, Any]] = {}
    for r in raw_threads:
        fn = str(r.get("fullname", "") or "")
        if not fn:
            continue
        cur = best_by_fullname.get(fn)
        if cur is None:
            best_by_fullname[fn] = r
            continue
        cur_err = bool(cur.get("error"))
        r_err = bool(r.get("error"))
        if cur_err and not r_err:
            best_by_fullname[fn] = r
            continue
        if cur_err == r_err:
            if len(r.get("comments_sample", []) or []) > len(cur.get("comments_sample", []) or []):
                best_by_fullname[fn] = r

    threads_all = list(best_by_fullname.values())
    # Filter to monitoring-related based on full text (post+comments) when available.
    threads: List[Dict[str, Any]] = []
    for t in threads_all:
        analysis_text = t.get("analysis_text")
        if not analysis_text:
            analysis_text = f"{t.get('title','')}\n{t.get('selftext','')}"
            t["analysis_text"] = analysis_text

        if not is_monitoring_related_text(analysis_text):
            continue

        # Recompute tags from text so report stays consistent even if the JSONL was created by older logic.
        t["vendors"] = sorted(set(detect_vendors(analysis_text)))
        t["pains"] = sorted(set(detect_pains(analysis_text)))
        threads.append(t)
    report_md = build_report(
        subreddit=subreddit,
        start_dt=start_dt,
        end_dt=end_dt,
        submissions=submissions,
        threads=threads,
    )
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_md)
        f.write("\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--subreddit", default="PublicRelations")
    ap.add_argument("--days", type=int, default=365, help="Lookback window in days from now (UTC).")
    ap.add_argument("--per-page", type=int, default=100)
    ap.add_argument("--max-pages", type=int, default=0, help="0 means unlimited.")
    ap.add_argument("--min-delay-s", type=float, default=1.2, help="Minimum delay between HTTP requests.")
    ap.add_argument("--max-comments", type=int, default=80, help="Max top-level comments to sample per relevant thread.")
    ap.add_argument("--max-relevant", type=int, default=0, help="0 means fetch all relevant threads; otherwise cap per run.")
    ap.add_argument("--resume", action="store_true", help="Resume from existing JSONL outputs if present.")
    ap.add_argument("--build-report-only", action="store_true", help="Only (re)build the markdown report from existing JSONL files.")
    args = ap.parse_args()

    end_dt = utc_now()
    start_dt = end_dt - dt.timedelta(days=int(args.days))
    start_utc = int(start_dt.timestamp())
    end_utc = int(end_dt.timestamp())

    max_pages = None if args.max_pages == 0 else int(args.max_pages)

    print(f"[crawl] subreddit=r/{args.subreddit} start={start_dt.isoformat()} end={end_dt.isoformat()}", file=sys.stderr)
    submissions = crawl_submissions(
        subreddit=args.subreddit,
        start_utc=start_utc,
        end_utc=end_utc,
        per_page=int(args.per_page),
        min_delay_s=float(args.min_delay_s),
        max_pages=max_pages,
    )
    submissions.sort(key=lambda s: s.created_utc, reverse=True)
    print(f"[crawl] submissions_in_window={len(submissions)}", file=sys.stderr)

    start_s = iso_date(start_dt)
    end_s = iso_date(end_dt)
    posts_path = os.path.join("analysis", f"reddit_publicrelations_{start_s}_to_{end_s}_posts.jsonl")
    threads_path = os.path.join("analysis", f"reddit_publicrelations_{start_s}_to_{end_s}_threads.jsonl")
    report_path = os.path.join("analysis", f"reddit_publicrelations_{start_s}_to_{end_s}_report.md")

    if args.build_report_only:
        if not os.path.exists(posts_path) or not os.path.exists(threads_path):
            raise SystemExit(f"Missing inputs: need {posts_path} and {threads_path} to build report.")
        build_report_from_files(
            subreddit=args.subreddit,
            posts_path=posts_path,
            threads_path=threads_path,
            report_path=report_path,
            start_dt=start_dt,
            end_dt=end_dt,
        )
        print(f"[out] {report_path}", file=sys.stderr)
        return 0

    # Write submissions JSONL (every post scanned).
    if not (args.resume and os.path.exists(posts_path)):
        os.makedirs(os.path.dirname(posts_path), exist_ok=True)
        with open(posts_path, "w", encoding="utf-8") as f:
            for s in submissions:
                f.write(
                    json.dumps(
                        {
                            "id": s.id,
                            "fullname": s.fullname,
                            "created_utc": s.created_utc,
                            "created_iso": s.created_dt.isoformat(),
                            "title": s.title,
                            "selftext": s.selftext,
                            "permalink": s.permalink,
                            "url": s.url,
                            "author": s.author,
                            "score": s.score,
                            "num_comments": s.num_comments,
                            "flair": s.flair,
                        },
                        ensure_ascii=False,
                    )
                )
                f.write("\n")

    # Fetch details for monitoring-related threads (post + sampled comments) and build analysis rows.
    ok_by_fullname: Dict[str, Dict[str, Any]] = {}
    err_by_fullname: Dict[str, Dict[str, Any]] = {}
    if args.resume and os.path.exists(threads_path):
        ok_by_fullname, err_by_fullname = load_threads_index(threads_path)
        threads: List[Dict[str, Any]] = list(ok_by_fullname.values()) + list(err_by_fullname.values())
    else:
        if os.path.exists(threads_path):
            os.remove(threads_path)
        threads = []

    relevant = [s for s in submissions if is_monitoring_related(s)]
    print(f"[crawl] monitoring_related={len(relevant)}", file=sys.stderr)

    # Resume: skip successfully fetched threads; retry error rows.
    pending = []
    for s in relevant:
        if s.fullname in ok_by_fullname:
            continue
        pending.append(s)
    if args.max_relevant and args.max_relevant > 0:
        pending = pending[: int(args.max_relevant)]

    if ok_by_fullname:
        print(f"[resume] ok={len(ok_by_fullname)} retryable_errors={len(err_by_fullname)} pending={len(pending)}", file=sys.stderr)

    for idx, s in enumerate(pending, start=1):
        try:
            post_data, comments = fetch_thread_details(
                permalink=s.permalink,
                max_comments=int(args.max_comments),
                min_delay_s=float(args.min_delay_s),
            )
        except Exception as e:
            # Keep going; log errors as partial rows.
            post_data, comments = {}, []
            err = f"{type(e).__name__}: {e}"
        else:
            err = ""

        # Text blob for rule-based detection.
        comment_text = "\n".join([c.get("body", "") for c in comments])
        analysis_text = f"{s.title}\n{s.selftext}\n{comment_text}"
        vendors = sorted(set(detect_vendors(analysis_text)))
        pains = sorted(set(detect_pains(analysis_text)))

        row = {
            "id": s.id,
            "fullname": s.fullname,
            "created_utc": s.created_utc,
            "created_iso": s.created_dt.isoformat(),
            "title": s.title,
            "selftext": s.selftext,
            "permalink": s.permalink,
            "url": s.url,
            "author": s.author,
            "score": s.score,
            "num_comments": s.num_comments,
            "flair": s.flair,
            "vendors": vendors,
            "pains": pains,
            "comments_sample": comments,
            "error": err,
            "analysis_text": analysis_text,
        }
        append_jsonl(threads_path, row)
        threads.append(row)
        if idx % 25 == 0:
            print(f"[threads] fetched {idx}/{len(pending)} (this run)", file=sys.stderr)

    # Build report (can be re-run later with --build-report-only).
    build_report_from_files(
        subreddit=args.subreddit,
        posts_path=posts_path,
        threads_path=threads_path,
        report_path=report_path,
        start_dt=start_dt,
        end_dt=end_dt,
    )

    print(f"[out] {posts_path}", file=sys.stderr)
    print(f"[out] {threads_path}", file=sys.stderr)
    print(f"[out] {report_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
