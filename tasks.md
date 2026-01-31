# Media Monitoring — Task Tracker

> Broken down from Swapnil's directives, the 9-workstream research, and the synthesis recommendations.
> Updated: 2026-01-30

---

## Legend

- [ ] Not started
- [~] In progress
- [x] Done

---

## Phase 1: Research (Desk Research Complete, Demos Pending)

All 9 research workstreams are done. Remaining research tasks are hands-on.

- [x] Profile 8 competitors (Meltwater, Cision, Muck Rack, Onclusive, Signal AI, Brand24, Mention, Talkwalker)
- [x] Market sizing — TAM $4.5B, SAM ~$600-700M, SOM Year 3: $5M-$18M ARR
- [x] Customer voice — 500+ reviews analyzed, complaint taxonomy built
- [x] Buyer decision framework — 5 personas, RFP checklist, entry strategy
- [x] Content licensing economics — 3 scenarios costed ($138K–$7.3M/yr)
- [x] Technical cost model — MVP $512K–$1.1M, break-even at 90–195 customers
- [x] Legal & compliance assessment — 3 RED risks identified
- [x] NLP/latency benchmarks — target thresholds defined
- [x] Adjacent alternatives — upgrade journey mapped, "Collapsed Funnel" strategy
- [x] Final synthesis document — go/no-go recommendation delivered
- [ ] Create Qodex email account for competitor demo requests
- [ ] Request product demos from all 8 competitors (using Qodex email)
- [ ] Document each demo (features, UX, data sources, filters, dashboards, gaps)

---

## Phase 2: Urgent Actions (Next 2 Weeks)

These came directly from the synthesis. Each has a clear goal.

### 2.1 — Stop displaying full article text in AlmaConnect News
- **Why:** AlmaLabs is in the exact legal posture Meltwater was pre-AP lawsuit (2013). Displaying full body text = copyright infringement.
- **Goal:** Switch alerts to headline + link + 2-3 sentence AI-generated summary.
- **Tasks:**
  - [ ] Get Swapnil's approval to change alert format
  - [ ] Modify alert template — remove full article body
  - [ ] Add AI summary generation (2-3 sentence excerpt)
  - [ ] Test with a subset of clients before full rollout
  - [ ] Roll out to all AlmaConnect News alerts

### 2.2 — Engage IP/copyright attorney
- **Why:** Must have legal framework before entering brand monitoring. AP v. Meltwater precedent is directly applicable.
- **Goal:** Signed engagement with an attorney who has US copyright + content licensing expertise. Budget: $20K–$50K.
- **Tasks:**
  - [ ] Research IP/copyright attorneys with media monitoring or news aggregation experience
  - [ ] Shortlist 2-3 firms
  - [ ] Schedule intro calls
  - [ ] Select attorney and begin compliance assessment

### 2.3 — Initiate PTI licensing outreach
- **Why:** Press Trust of India is the most accessible first licensing partner. India-first strategy validated — Indian content costs 10-20% of US/EU.
- **Goal:** Signed PTI content licensing agreement within 90 days.
- **Tasks:**
  - [ ] Identify PTI's content licensing team / contact point
  - [ ] Draft outreach email (position as "media monitoring product", no AI hype per Swapnil's directive)
  - [ ] Send initial inquiry
  - [ ] Follow up if no response within 1 week
  - [ ] Negotiate terms and pricing

### 2.4 — Assign 1 ML/NLP engineer to NER pipeline
- **Why:** Current string matching has ~50-60% entity accuracy. spaCy NER (89% F1) is the single highest-ROI technical improvement.
- **Goal:** Working NER prototype (spaCy `en_core_web_trf`) in 6-8 weeks.
- **Tasks:**
  - [ ] Identify/assign the ML/NLP engineer
  - [ ] Set up spaCy environment with `en_core_web_trf` model
  - [ ] Build NER pipeline prototype on sample articles
  - [ ] Benchmark accuracy against current string matching
  - [ ] Integrate into existing crawling pipeline

### 2.5 — Sign up for NewsAPI Business tier
- **Why:** Instant access to 150,000+ global news sources via API. No negotiation needed — self-serve. Provides broad coverage while licensing negotiations proceed.
- **Goal:** Active NewsAPI Business subscription ($449/month) and initial data flowing.
- **Tasks:**
  - [ ] Sign up at newsapi.org for Business tier
  - [ ] Test API with brand monitoring queries
  - [ ] Evaluate coverage quality (especially Indian sources)
  - [ ] Document gaps vs. current crawling pipeline

### 2.6 — Create Slack channel + internal project brief
- **Why:** Media monitoring initiative needs formal internal structure and ownership.
- **Goal:** Dedicated channel, assigned project lead, Month 6 go/no-go criteria formally documented.
- **Tasks:**
  - [ ] Create #media-monitoring Slack channel
  - [ ] Write 1-page internal project brief (scope, timeline, budget, success criteria)
  - [ ] Assign project lead (Swapnil or senior product leader)
  - [ ] Share synthesis.md with core team
  - [ ] Define Month 6 go/no-go gate criteria formally

### 2.7 — Audit top 100 scraped sources for ToS / robots.txt compliance
- **Why:** Scraping 50K+ sites without ToS review is a RED-level legal risk.
- **Goal:** Tiered source list (permissive / restricted / prohibited) and robots.txt compliance across all crawlers.
- **Tasks:**
  - [ ] Export list of top 100 most-scraped news sources from AlmaConnect
  - [ ] Check robots.txt for each source
  - [ ] Review Terms of Service for scraping restrictions
  - [ ] Categorize: GREEN (permissive), YELLOW (restricted), RED (prohibited)
  - [ ] Implement robots.txt compliance in crawlers
  - [ ] Remove or flag RED sources

---

## Phase 3: Media Partnership Outreach (Weeks 2-6)

### 3.1 — Build target list of media houses for partnerships
- **Goal:** Prioritized list of 15-20 media houses to approach for content licensing.
- **Tasks:**
  - [ ] List Indian wire services: PTI, IANS, ANI, UNI
  - [ ] List top Indian newspaper groups: Times Group, HT Media, Indian Express, NDTV, etc.
  - [ ] List international aggregators: NewsAPI, Factiva, LexisNexis
  - [ ] Prioritize by cost, coverage value, and approachability
  - [ ] Find contact info for licensing/partnership teams

### 3.2 — Draft and send partnership inquiry emails
- **Goal:** Outreach sent to top 10 targets. Persistent follow-up per Swapnil's directive (volume + patience over elegance).
- **Tasks:**
  - [x] Draft partnership inquiry email template (position as "media monitoring", not AI)
  - [x] Customize for each target
  - [x] Send first batch (9 targets) — sent 2026-01-30 from company email
    - Dow Jones / Factiva, Thomson Reuters / LSEG, Associated Press, Bloomberg, Financial Times, Economist Group, NBCUniversal, Axel Springer, Cision / PR Newswire
  - [ ] Track responses in a spreadsheet
  - [ ] Follow up every 5-7 days — try multiple contacts per organization
  - [ ] Use LinkedIn for warm intros where possible

---

## Phase 4: Product MVP (Months 1-3)

These kick in once Swapnil gives the go-ahead to build.

### 4.1 — NER pipeline (Month 1-3)
- [ ] spaCy `en_core_web_trf` integration
- [ ] Fine-tune on Indian news articles
- [ ] Benchmark: target >80% NER F1 (table stakes), >87% (competitive)

### 4.2 — Sentiment analysis (Month 2-4)
- [ ] Fine-tune RoBERTa for news sentiment
- [ ] LLM fallback for complex/ambiguous cases
- [ ] Benchmark: target >72% accuracy (table stakes), >75% (competitive)

### 4.3 — Deduplication & syndication handling (Month 2-3)
- [ ] Implement SimHash / MinHash for near-duplicate detection
- [ ] Handle syndicated wire stories (AP, PTI republished across outlets)

### 4.4 — Brand monitoring dashboard (Month 2-5)
- [ ] Design dashboard — mention volume, sentiment trends, top outlets, geography
- [ ] Build search/filter — brand name, date range, sentiment, source
- [ ] Email alert system — real-time or digest
- [ ] Report export (PDF/CSV)

### 4.5 — Pricing & packaging (Month 3-4)
- [ ] Finalize tier structure: Free/$0, Starter/$49-79/mo, Professional/$149-199/mo, Team/$299-499/mo
- [ ] Define feature gates per tier
- [ ] Build billing integration
- [ ] Transparent pricing page (differentiator vs. incumbents)

---

## Phase 5: Go/No-Go Gates

### Month 6 Gate
- [ ] **>10 paying customers?** If no → reassess ICP and positioning
- [ ] Monthly churn <8%?
- [ ] Unit economics tracking (LTV:CAC, gross margin)

### Month 12 Gate
- [ ] **>50 paying customers?** If no → wind down and refocus on AlmaConnect core
- [ ] Revenue run-rate tracking vs. $5M Year 3 target
- [ ] Content licensing cost vs. budget

### Month 30 Gate
- [ ] **>200 customers, $2M+ ARR?** If yes → raise $3M-$5M Series A
- [ ] If no → evaluate options (pivot, sell, wind down)

---

## Phase 6: Reporting to Swapnil

- [ ] Prepare Friday update #1 — summarize all research findings, key decisions needed
- [ ] Set up recurring weekly update cadence
- [ ] Escalate legal risk (full article text) immediately — don't wait for Friday

---

## Key Numbers to Remember

| Metric | Value |
|---|---|
| MVP Year 1 investment | $512K–$1.1M |
| Break-even customers | 90–195 |
| Maximum acceptable loss | $1.1M |
| Year 3 SOM target | $5M–$18M ARR |
| Content licensing (MVP) | $138K–$355K/yr |
| Most expensive line item | Twitter/X Enterprise API: $504K–$1.2M+/yr |
| AlmaConnect head start value | $200K–$400K |
