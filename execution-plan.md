# Execution Plan: Competitive Intelligence Deep Dive

> Prepared by: Claude (acting as Senior McKinsey Consultant)
> Client: AlmaLabs
> Date: 2026-01-30
> Status: PENDING APPROVAL

---

## Scope

9 research workstreams to fill critical intelligence gaps before a go/no-go decision on entering the brand media monitoring market. Point 5 (hands-on demos) excluded — requires physical execution by the team.

---

## Workstream 1: Market Sizing

### Objective
Determine Total Addressable Market (TAM), Serviceable Addressable Market (SAM), and Serviceable Obtainable Market (SOM) for brand media monitoring. Understand market growth trajectory.

### Approach

**Step 1.1 — Meltwater Financial Analysis**
Meltwater is publicly traded on Oslo Stock Exchange (ticker: MLTW). I will:
- Pull Meltwater's latest annual report / investor presentation (2025) via web search
- Extract: total revenue, revenue by segment, growth rate, customer count, ARPU (average revenue per user), gross margin
- This gives us a direct data point on what a market leader earns

**Step 1.2 — Cision/Brandwatch Revenue Estimates**
Cision is private (owned by Platinum Equity). I will:
- Search for the last known revenue figures (pre-acquisition or leaked estimates)
- Look at SEC filings from when Cision was public (pre-2019 take-private)
- Search for analyst estimates, press coverage of the Platinum Equity deal valuation
- Brandwatch had known revenue pre-acquisition — search for those figures

**Step 1.3 — Industry Analyst Reports**
Search for publicly available data from:
- Grand View Research, Mordor Intelligence, MarketsandMarkets — they publish media monitoring market size reports
- Gartner/Forrester reports on PR technology or media intelligence
- Extract: global market size (2024-2025), CAGR projections, segmentation by type (news vs social vs broadcast)

**Step 1.4 — Bottom-Up Estimation**
Cross-validate by estimating:
- Number of potential buyers (PR teams, comms departments globally)
- Average deal value per segment (SMB, mid-market, enterprise)
- Penetration rate assumptions

**Step 1.5 — SAM/SOM for AlmaLabs**
Define realistic scope:
- Which geographies? (Start India + US? Global?)
- Which segments? (Enterprise only? Mid-market?)
- What share is realistic in year 1, 3, 5?

### Tools
- WebSearch for Meltwater financials, Cision revenue, analyst reports
- WebFetch for specific financial pages, investor presentations

### Output
- File: `competitive-research/market-sizing.md`
- Contents: TAM/SAM/SOM estimates with sources, Meltwater financials summary, market growth data

---

## Workstream 2: Missing Competitors (3-5 Additional Players)

### Objective
Complete the competitive map with smaller/mid-tier players that are more relevant to AlmaLabs' entry point.

### Target Competitors

| Competitor | Why They Matter |
|---|---|
| **Onclusive** | Acquired Critical Mention (broadcast monitoring leader). Analytics-focused. Relevant because they also pivoted from legacy to modern |
| **Signal AI** | AI-native media intelligence platform. Relevant because they're the "AI-first" player — directly tests Swapnil's "no AI positioning" constraint |
| **Brand24** | Affordable, self-serve ($79/mo starting). Relevant because this is the LOW END of market — where AlmaLabs might enter |
| **Mention** | Mid-market monitoring ($41/mo starting). Simple, accessible. Another entry-point benchmark |
| **Talkwalker** (now Hootsuite) | Social + media monitoring. Acquired by Hootsuite. Shows consolidation trend |

### Approach

For each competitor, I will:

**Step 2.1 — Company Profile**
- WebSearch for company overview, founding, funding, customer count, recent news
- Identify their positioning and target segment

**Step 2.2 — Product Feature Extraction**
- WebFetch their product/features pages
- Document: channels covered, alert types, analytics, dashboards, API, integrations
- Compare against our existing feature matrix

**Step 2.3 — Pricing Research**
- WebSearch for pricing pages (Brand24 and Mention have public pricing)
- Search G2/Capterra for pricing info on others
- Document tier structure and entry points

**Step 2.4 — Tech & Data Sourcing**
- WebSearch for engineering blog posts, job listings (reveal tech stack), partnership announcements
- Identify their data sourcing strategy

**Step 2.5 — Competitive Position**
- Where do they sit relative to Meltwater/Cision/Muck Rack?
- What's their unique angle?

### Tools
- WebSearch (primary) — multiple searches per competitor
- WebFetch — for product pages, pricing pages, blog posts

### Output
- Files: `competitive-research/onclusive.md`, `competitive-research/signal-ai.md`, `competitive-research/brand24.md`, `competitive-research/mention.md`, `competitive-research/talkwalker.md`
- Update: `competitive-research/landscape-overview.md` with expanded comparison matrix
- Each file follows the same structure as existing competitor files

---

## Workstream 3: Customer Voice & Win-Loss Analysis

### Objective
Understand WHY customers choose, switch, or leave these platforms. Identify unmet needs and pain points that could be AlmaLabs' wedge.

### Approach

**Step 3.1 — G2 Review Mining**
For each of the 3 main competitors + new ones:
- WebSearch for "[Competitor] G2 reviews"
- WebFetch G2 pages to extract:
  - Top positive themes (what do users love?)
  - Top negative themes (what do users hate?)
  - "Switched from" patterns (who are they replacing?)
  - Star ratings and trend

**Step 3.2 — Capterra/TrustRadius Mining**
- Same approach for Capterra and TrustRadius
- These often have different user demographics (Capterra skews mid-market)

**Step 3.3 — Reddit r/PublicRelations Mining**
- WebSearch for Reddit discussions on:
  - "Meltwater vs Cision vs Muck Rack"
  - "media monitoring tool recommendation"
  - "switching from Cision"
  - "Meltwater alternative"
  - "best media monitoring 2025 2026"
- Extract: real user opinions, switching stories, price complaints, feature wishes

**Step 3.4 — LinkedIn/Twitter Sentiment**
- WebSearch for public discussions about these tools on LinkedIn and Twitter
- Look for common frustrations or praise

**Step 3.5 — Synthesis**
- Categorize complaints: Price, Accuracy, UX, Support, Coverage Gaps, Contract Issues
- Identify the #1 reason people switch
- Identify unmet needs (things nobody does well)

### Tools
- WebSearch — multiple targeted queries
- WebFetch — for review pages

### Output
- File: `competitive-research/customer-voice.md`
- Contents: Complaint taxonomy, switching patterns, unmet needs, competitive opportunity areas

---

## Workstream 4: Buyer Decision Framework

### Objective
Map how brands and PR teams evaluate, select, and buy media monitoring tools. Understand the purchase process, decision criteria, and key stakeholders.

### Approach

**Step 4.1 — Buying Guide Research**
- WebSearch for: "how to choose media monitoring tool", "media monitoring RFP template", "media monitoring buyer's guide"
- WebFetch relevant guides (Meltwater, Cision, and third parties all publish these)
- Extract the evaluation criteria they recommend

**Step 4.2 — RFP Criteria Analysis**
- WebSearch for: "media monitoring RFP requirements", "PR technology evaluation criteria"
- Look for actual RFP templates or procurement documents
- Identify standard evaluation dimensions

**Step 4.3 — Buyer Persona Mapping**
- WebSearch for: "who buys media monitoring", "PR tech buyer persona"
- Determine: typical buyer title, budget owner, decision process, typical budget range
- Map: influencer vs decision-maker vs user

**Step 4.4 — Sales Cycle Research**
- Search G2/Capterra reviews for mentions of sales process
- Search Reddit for discussions about buying/negotiating with these vendors
- Identify: typical sales cycle length, negotiation patterns, common objections

**Step 4.5 — Synthesis: Ranked Decision Criteria**
Build the ranked list:
1. Coverage breadth? 2. Speed? 3. Price? 4. UX? 5. Accuracy? 6. Integrations?
Backed by evidence from Steps 4.1-4.4.

### Tools
- WebSearch — buyer guides, RFP templates
- WebFetch — for specific guide content

### Output
- File: `competitive-research/buyer-framework.md`
- Contents: Decision criteria ranked, buyer personas, typical sales cycle, budget benchmarks, RFP criteria checklist

---

## Workstream 6: Content Licensing Economics

### Objective
Understand the actual economics of content partnerships — what it costs, what terms look like, and what barriers exist for a new entrant like AlmaLabs.

### Approach

**Step 6.1 — Factiva / Dow Jones Licensing**
- WebSearch for: "Factiva data licensing pricing", "Dow Jones API pricing", "Factiva partnership media monitoring"
- Look for: developer documentation, API pricing pages, partnership program info
- Search for: case studies or blog posts from companies that integrated Factiva

**Step 6.2 — LexisNexis Licensing**
- WebSearch for: "LexisNexis data licensing", "LexisNexis API for media monitoring", "LexisNexis Nexis Solutions API pricing"
- Look for: their data-as-a-service offerings, partnership programs
- Check: LexisNexis Developer Portal for API documentation and pricing tiers

**Step 6.3 — TVEyes Broadcast Monitoring**
- WebSearch for: "TVEyes partnership pricing", "TVEyes API access", "broadcast monitoring licensing cost"
- Check if TVEyes has a partner program or reseller model documentation

**Step 6.4 — News Agency Licensing (AP, Reuters, AFP)**
- WebSearch for: "AP news API pricing", "Reuters content licensing", "AFP licensing for media monitoring"
- Look for: AP's "AP News API" pricing, Reuters Connect platform pricing
- These agencies have content licensing programs — find the entry points

**Step 6.5 — Social Media API Costs**
- WebSearch for: "Twitter X API pricing 2026", "Facebook Graph API limits", "social media API costs for monitoring"
- Document current X/Twitter API tiers (Basic, Pro, Enterprise) and costs
- Document: what level of access is needed for real-time brand monitoring

**Step 6.6 — Indian Media Licensing**
Since AlmaLabs is India-based:
- WebSearch for: "Indian news agency licensing", "PTI news licensing", "Indian newspaper digital licensing"
- Look for: Press Trust of India (PTI), IANS, Asian News International (ANI) licensing programs
- Identify Indian media houses with digital licensing programs

**Step 6.7 — Cost Estimation Table**
Compile estimated costs for each partnership type:
- Annual licensing fee ranges
- Per-query or per-article costs
- Minimum commitments
- Barriers to entry (minimum revenue, customer count requirements)

### Tools
- WebSearch — extensive, multiple queries per source type
- WebFetch — for API documentation pages, pricing pages, partnership program info

### Output
- File: `competitive-research/content-licensing-economics.md`
- Contents: Per-source cost estimates, partnership models, barriers to entry, recommended approach for AlmaLabs

---

## Workstream 7: Technical Cost Model

### Objective
Estimate what it would cost AlmaLabs to build or augment infrastructure for brand media monitoring — from crawling to NLP to delivery.

### Approach

**Step 7.1 — Infrastructure Cost Benchmarking**
- WebSearch for: "media monitoring infrastructure cost", "news crawling infrastructure AWS cost", "Elasticsearch cluster cost at scale"
- Look for engineering blog posts from similar-scale companies about their cloud costs

**Step 7.2 — AWS Service Pricing Research**
Research current pricing for key services AlmaLabs would need:
- EC2/EKS (compute for crawlers, NLP pipeline)
- S3 (article storage)
- OpenSearch/Elasticsearch (search index)
- SES (email alerts)
- Comprehend or Bedrock (NLP/sentiment)
- Lambda (serverless event processing)
- Use WebFetch on AWS pricing pages for current numbers

**Step 7.3 — Social Media API Cost Analysis**
- Twitter/X Enterprise API: what does real-time brand monitoring cost?
- Facebook/Instagram API: limits and costs
- Reddit API: current commercial terms
- YouTube Data API: quota limits

**Step 7.4 — NLP/ML Pipeline Costs**
- Cost of running sentiment analysis at scale (per article)
- Options: AWS Comprehend vs open-source models (Hugging Face) vs fine-tuned LLMs
- Cost comparison at different volume tiers (10K, 100K, 1M articles/day)

**Step 7.5 — Content Partnership Costs (from Workstream 6)**
- Integrate licensing cost estimates from Workstream 6

**Step 7.6 — Build vs Buy vs Partner Analysis**
For each capability layer, estimate:
- Build in-house: team size + timeline + ongoing cost
- Buy/license: annual cost + integration effort
- Partner: revenue share model + dependency risk

**Step 7.7 — Total Cost Model**
Build three scenarios:
- **MVP** (minimum to enter market): stripped-down version, key partnerships only
- **Competitive** (match Muck Rack): full feature set, all major partnerships
- **Enterprise** (match Meltwater/Cision): global coverage, all channels, premium analytics

### Tools
- WebSearch — AWS pricing, API pricing, engineering cost benchmarks
- WebFetch — AWS pricing calculator pages, API documentation

### Output
- File: `competitive-research/technical-cost-model.md`
- Contents: Cost breakdown by component, three scenario models (MVP/Competitive/Enterprise), build vs buy analysis

---

## Workstream 8: Adjacent & Free Alternative Analysis

### Objective
Map what brands use BEFORE buying enterprise monitoring tools. Understand the low end of the market and the upgrade trigger.

### Approach

**Step 8.1 — Google Alerts Analysis**
- WebSearch for: "Google Alerts vs paid media monitoring", "Google Alerts limitations for PR"
- Document: what Google Alerts does, what it doesn't do, why people upgrade
- Identify the "upgrade trigger" — the pain point that makes free insufficient

**Step 8.2 — Budget Tools Research**
For Brand24 and Mention (both have public pricing):
- WebFetch their pricing pages — exact tier structure and features per tier
- WebFetch feature pages — what's included at each level
- Compare against enterprise tools — where's the gap?

**Step 8.3 — Social Media Native Tools**
- WebSearch for: "social media monitoring free tools", "Twitter brand monitoring free"
- Document: what's available natively on each social platform
- Identify limitations that drive users to paid tools

**Step 8.4 — DIY/Manual Monitoring**
- WebSearch for: "manual media monitoring process", "media monitoring without tools"
- Understand: what does a PR team do when they have NO tool? (Google searches, RSS readers, intern checking news sites)
- Identify the pain points that drive purchase

**Step 8.5 — The Upgrade Journey Map**
Synthesize: What's the typical journey from free → budget → enterprise?
- Stage 1: Google Alerts + manual
- Stage 2: Brand24/Mention ($50-$200/mo)
- Stage 3: Muck Rack ($5K-$15K/year)
- Stage 4: Meltwater/Cision ($10K-$100K+/year)

What triggers each upgrade? Where should AlmaLabs insert itself?

### Tools
- WebSearch — pricing research, comparison articles
- WebFetch — pricing pages, feature pages

### Output
- File: `competitive-research/adjacent-alternatives.md`
- Contents: Tool-by-tool analysis, upgrade journey map, entry point recommendation for AlmaLabs

---

## Workstream 9: Legal & Compliance Landscape

### Objective
Map the legal risks and compliance requirements for operating a media monitoring service — especially relevant since AlmaLabs currently scrapes "by any means."

### Approach

**Step 9.1 — Web Scraping Legality**
- WebSearch for: "web scraping legality 2025 2026", "news scraping legal risks", "hiQ vs LinkedIn ruling impact"
- Research key cases: hiQ Labs v. LinkedIn (US), Ryanair v. PR Aviation (EU)
- Document: what's legal, what's gray area, what's clearly illegal

**Step 9.2 — Copyright & Fair Use for News Content**
- WebSearch for: "news aggregation copyright law", "fair use news monitoring", "snippet length copyright"
- Research: how much of an article can you display? Full text? Headline + snippet? Link only?
- Look at: AP vs Meltwater settlement (2013) — directly relevant precedent
- Document: safe practices for displaying news content

**Step 9.3 — GDPR & Data Privacy**
- WebSearch for: "GDPR media monitoring", "personal data monitoring compliance", "GDPR brand monitoring"
- Document: requirements for monitoring personal names, storing personal data, EU data subjects
- Relevance: especially important since current AlmaConnect News monitors individual NAMES (alumni/prospects)

**Step 9.4 — Terms of Service Risks**
- WebSearch for: "news website terms of service scraping", "social media scraping legal"
- Document: common ToS restrictions that news sites and social platforms impose
- Identify: which sources explicitly prohibit automated access without partnership

**Step 9.5 — India-Specific Legal Considerations**
- WebSearch for: "India web scraping law", "India copyright news aggregation", "India data protection act media monitoring"
- Research: India's Digital Personal Data Protection Act (2023) implications
- Document: India-specific requirements

**Step 9.6 — How Competitors Handle Compliance**
- WebSearch for: "Meltwater copyright lawsuit", "Cision data compliance", "media monitoring legal compliance"
- Research: AP vs Meltwater (2013), any other lawsuits in this space
- Document: how incumbents navigated legal challenges and what safeguards they built

**Step 9.7 — Risk Assessment**
Categorize AlmaLabs' current practices by risk level:
- RED: Practices that must stop immediately
- YELLOW: Practices that need legal review
- GREEN: Practices that are safe to continue

### Tools
- WebSearch — legal precedents, compliance frameworks, regulations
- WebFetch — for specific legal analysis articles, regulatory documents

### Output
- File: `competitive-research/legal-compliance.md`
- Contents: Scraping legality summary, copyright rules, GDPR requirements, India-specific rules, risk assessment for AlmaLabs, recommended compliance framework

---

## Workstream 10: Sentiment/NLP Quality & Data Freshness Benchmarks

### Objective
Understand what "good" looks like for NLP accuracy and alert speed in media monitoring. Set benchmarks AlmaLabs must hit.

### Approach

**Step 10.1 — Sentiment Analysis Accuracy Benchmarks**
- WebSearch for: "sentiment analysis accuracy media monitoring", "NLP sentiment benchmark news articles"
- Research: what accuracy do industry tools achieve? (typically 70-85%)
- Document: state of the art vs good enough vs table stakes

**Step 10.2 — Entity Extraction / NER Benchmarks**
- WebSearch for: "named entity recognition accuracy benchmark 2025", "NER news articles performance"
- Document: what models achieve (spaCy, Hugging Face, AWS Comprehend, GPT-based)
- Identify: performance on non-English text (especially Indian languages)

**Step 10.3 — Alert Latency Benchmarks**
- WebSearch for: "media monitoring alert speed comparison", "real-time news monitoring latency"
- Look at: what Muck Rack, Meltwater claim for speed
- Search G2/user reviews for real-world speed reports
- Document: expected SLA (minutes? hours? same-day?)

**Step 10.4 — Duplicate Detection & Syndication Handling**
- WebSearch for: "news article deduplication techniques", "syndication detection media monitoring"
- Document: standard approaches (fingerprinting, simhash, MinHash)
- Benchmark: what false positive / false negative rates are acceptable

**Step 10.5 — Multi-Language NLP**
- WebSearch for: "multilingual sentiment analysis accuracy", "NLP non-English news monitoring"
- Document: which languages are well-served by current models vs poorly served
- Relevance: AlmaLabs serving Indian clients needs Hindi, regional language capability

**Step 10.6 — What AlmaLabs Needs to Hit**
Define three tiers:
- **Table stakes**: minimum NLP quality to not embarrass yourself
- **Competitive**: match Muck Rack level
- **Best-in-class**: match Meltwater/Cision level

### Tools
- WebSearch — NLP benchmarks, accuracy studies, speed comparisons
- WebFetch — for specific benchmark reports, technical blog posts

### Output
- File: `competitive-research/nlp-benchmarks.md`
- Contents: Sentiment accuracy benchmarks, NER benchmarks, latency benchmarks, dedup standards, multi-language assessment, target thresholds for AlmaLabs

---

## Execution Sequence

I recommend executing in this order to maximize information flow between workstreams:

```
Phase A (parallel — no dependencies):
├── Workstream 1: Market Sizing
├── Workstream 2: Missing Competitors
├── Workstream 3: Customer Voice
├── Workstream 9: Legal/Compliance
└── Workstream 10: NLP/Latency Benchmarks

Phase B (depends on Phase A outputs):
├── Workstream 4: Buyer Decision Framework (benefits from customer voice data)
├── Workstream 6: Content Licensing Economics
└── Workstream 8: Adjacent Alternatives (benefits from competitor data)

Phase C (depends on all above):
└── Workstream 7: Technical Cost Model (integrates licensing costs, NLP costs, infra costs)
```

Phase A workstreams can all run in parallel since they don't depend on each other.
Phase B benefits from Phase A findings.
Phase C is the synthesis — needs all inputs.

---

## Deliverables Summary

| Workstream | Output File | Key Question Answered |
|---|---|---|
| 1. Market Sizing | `market-sizing.md` | How big is this opportunity? |
| 2. Missing Competitors | `onclusive.md`, `signal-ai.md`, `brand24.md`, `mention.md`, `talkwalker.md` | Who else is in this market? |
| 3. Customer Voice | `customer-voice.md` | Why do people switch? What's broken? |
| 4. Buyer Framework | `buyer-framework.md` | How do buyers choose? |
| 6. Licensing Economics | `content-licensing-economics.md` | What do partnerships cost? |
| 7. Cost Model | `technical-cost-model.md` | What will it cost us to compete? |
| 8. Adjacent Alternatives | `adjacent-alternatives.md` | What do people use before enterprise tools? |
| 9. Legal/Compliance | `legal-compliance.md` | What are the legal risks? |
| 10. NLP Benchmarks | `nlp-benchmarks.md` | What quality bar must we hit? |

All files go in: `competitive-research/`

---

## Post-Execution

After all 9 workstreams are complete, I will:
1. Update `action-log.json` with all actions, findings, and decisions
2. Update `context.md` with new insights that change the strategic picture
3. Produce a **synthesis document** that answers Swapnil's core question: "Can we compete, and what will it take?"
