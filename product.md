# AlmaConnect News — Product Overview

## Company: AlmaLabs

AlmaLabs offers an alumni engagement platform with three products:

1. **AlmaConnect News** (Media Monitoring / News Product)
2. **Alumni Network for Institutions** (Universities, Schools, Colleges)
3. **Alumni Network for Corporates** (Companies engaging former employees)

This document focuses on **AlmaConnect News** — the product being evaluated for expansion into brand media monitoring.

---

## What AlmaConnect News Is Today

AlmaConnect News is a **prospect and alumni intelligence product** built for university advancement teams — specifically gift officers and prospect research teams.

**How it works:**
- Clients (large educational and institutional organizations) upload prospect/alumni lists ranging from **10,000 to 200,000 prospects**
- The system continuously monitors public news sources and delivers alerts when a prospect or alumni is mentioned in a news article

**Core value proposition:** "Whenever your alumni make news, we alert you."

---

## Current Technical Pipeline

The system operates as a three-step pipeline:

### 1. Ingest
- Scrape/fetch articles daily from **20,000 to 50,000 news websites**
- Two ingestion methods:
  - **RSS feeds** fetched directly from the web
  - **Direct scraping** via plugin-based scraping
- No media partnerships or licensed content — all sources are scraped independently

### 2. Match
- Compare the **full article body text** against prospect name lists
- This is essentially **string matching** — if a prospect's name appears in an article body, it's flagged as a match
- No identity resolution, confidence scoring, or disambiguation layer exists today

### 3. Deliver
- Matched articles are surfaced as **posts or alerts** to the client

---

## Current Capabilities (the ~50% we already have)

| Capability | Status | Notes |
|---|---|---|
| Large-scale news ingestion | Yes | 20K–50K sources daily |
| RSS feed parsing | Yes | Primary ingestion method |
| Web scraping | Yes | Plugin-based scraping |
| Prospect list management | Yes | Handles 10K–200K prospect lists per client |
| Name-to-article matching | Yes | String matching against article body |
| Alert/post delivery | Yes | Alerts delivered to clients |
| Existing client base | Yes | Large institutional clients already using the product |
| Infrastructure for scale | Yes | Already processing high volume daily |

---

## Current Limitations (what's missing)

| Gap | Details |
|---|---|
| Identity resolution | No disambiguation — common names will produce false positives |
| Confidence scoring | No match confidence (high/medium/low) on alerts |
| Entity extraction (NER) | No structured extraction of people, companies, roles, events |
| Sentiment analysis | No positive/negative/neutral classification |
| Topic/category classification | No tagging (wealth signal, relationship trigger, stewardship, etc.) |
| Relevance scoring | No prioritization — all matches treated equally |
| Deduplication | No clustering of syndicated copies of the same story |
| Workflow/assignment | No team-based assignment, status tracking, or feedback loop |
| Premium/paywalled content | No access — scraping only public sources |
| Social media monitoring | No social media coverage (news only) |
| SEC/filing monitoring | No structured financial filing data |
| Media partnerships | None — fully reliant on scraping |
| Reporting/analytics | No dashboards on alert quality, action rates, coverage |

---

## Current ICP and Personas

### Primary: University Advancement Teams
- **Gift Officers / Major Gifts Officers** — Need actionable triggers for outreach
- **Prospect Research / Prospect Development** — Need accurate monitoring and wealth signals
- **Advancement Ops / CRM Admins** — Need data hygiene, integrations, compliance

### Use Cases Served Today
- Alumni news tracking for engagement
- Prospect identification for fundraising
- News-based outreach triggers (promotions, awards, mentions)

---

## Scale and Proof Points

- **500+ organizations** globally (universities, schools, corporates)
- **Millions of alumni** across thousands of communities
- **300,000+ news sources** claimed in marketing (20K–50K actively scraped daily)
- **~60% monthly active user engagement** across AlmaConnect-powered networks
- Clients include: Bryant University, BITS Pilani, IIT Delhi, IIM Udaipur, Marquette University, Bryn Mawr College, Intel, Britannia Industries, Comviva, Syneos Health
