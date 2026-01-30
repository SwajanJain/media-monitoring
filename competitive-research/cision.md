# Cision — Competitor Deep Dive

> Source: "Media Monitoring Product Landscape" report

---

## Company Profile

| Field | Detail |
|---|---|
| Founded | Decades-long legacy in PR software |
| HQ | Chicago, USA |
| Global presence | 170 countries |
| Customers | 100,000+ clients globally |
| Platform | CisionOne (Cision Communications Cloud) |
| Positioning | Industry standard for communications teams — all-in-one PR workflow |
| Reputation | "The Bloomberg for PR professionals" |

---

## Product: Media Monitoring

### Core Capabilities
- **Mention Streams**: Custom real-time feeds for brand, competitors, spokespeople, or any topic
- Multiple streams side-by-side for comparison
- Each mention includes: headline, source, sentiment, engagement metrics, impact scores, audience reach
- **All-in-one solution**: monitoring + analytics + influencer engagement + press distribution

### Coverage Breadth
- Hundreds of thousands of news sources
- **10,000+ premium print/online titles** (including paywalled publications)
- **3,000+ TV and radio stations**
- **60,000+ podcasts** (speech-to-text transcription, multiple languages)
- All major **social media platforms** (via Brandwatch acquisition)
- Twitter/X, Facebook, Instagram, forums, review sites
- **Human-curated print clipping** in UK (#1 print monitoring service)

### Analytics & AI
- **React Score**: Proprietary algorithmic metric that flags potentially harmful or high-impact content
  - Breaks down: controversy level, emotional language, likelihood of spreading
  - Crisis early warning system — unique to Cision
- **Sentiment analysis** built-in
- **Engagement data** ("social echo")
- **Audience reach** figures
- Trending topic identification
- **Cision Influencer Graph**: tracks journalist output, topics, frequency, social influence
- Via Brandwatch: image analysis, consumer sentiment analysis using ML
- Factmata AI: identifies fake news / spam content (feeds into React Score)

### Dashboards & Reporting
- Comprehensive dashboards: mention streams, charts for coverage over time, sentiment, competitive comparisons
- **One-click interactive reports** from dashboards
- Shareable via simple URL — executive-ready
- Slice data by: date range, share of voice, geographic spread
- Unlimited clipping and searches in many packages
- **Cision Insights** (add-on): human analysts deliver curated reports and executive briefs

### Alerts & Delivery
- **Instant alerts and notifications** to entire teams including executives
- **Mobile app** (iOS/Android)
- Email digests
- **Slack and Microsoft Teams** integration
- Crucial for reputation management — real-time capability

### Media Database & PR Workflow
- **Largest media database in industry** (hundreds of thousands of journalist/influencer contacts)
- Integrated directly for outreach: journalist email pitches
- **PR Newswire** integration: press release sending + tracking media pickups of releases
- Closed-loop: send release via PR Newswire → auto-track all media pickups in monitoring
- One-stop hub: find journalists → pitch → monitor coverage → report results

---

## Technology & Operations

### Infrastructure
- Evolved from on-premise to unified **cloud-based architecture** (CisionOne)
- Likely **AWS** (AWS Marketplace listings exist) with possible multi-cloud elements
- **Microservices architecture**: separate engines for news search, social search, media contacts DB
- Search indices likely **Elasticsearch/OpenSearch** (from TrendKite acquisition)
- Multi-tenant with strict data partitioning per client
- GDPR-compliant, multi-language monitoring (40+ languages including non-Latin scripts)

### Data Sourcing

| Source Type | Method |
|---|---|
| Online news/blogs | In-house crawlers + news agency feeds (AP, Reuters, AFP) + possibly LexisNexis feeds |
| Paywalled/premium content | 10K+ premium titles — likely via Factiva/Nexis licensing |
| Social media | **Brandwatch** data pipeline (acquired 2021): distributed crawling, X firehose, FB/IG official APIs, forums, review sites. Billions of social conversations indexed |
| Print media | **In-house print monitoring teams** (UK — human-reviewed), local partners globally, possibly Burrelles (US), regional firms in Asia |
| Broadcast TV/Radio | TVEyes partnership + possibly direct recording in key markets (3K+ stations) |
| Podcasts | 20K+ podcasts via speech-to-text (possibly TrendKite tech or Amazon Transcribe) |
| Press releases | **PR Newswire** (owned) — cross-linked with monitoring for pickup tracking |

### Key Acquisitions
- **TrendKite (2019)** — Modern cloud monitoring tech (Elasticsearch + AWS). Became foundation of "Next Generation" monitoring
- **Brandwatch (2021)** — Powerful social media data engine. Massive historical database. AI for image analysis
- **Factmata** — AI startup for fake news / spam detection → feeds React Score
- **Gorkana** — UK monitoring arm, media database

### Key Partnerships
- **News agencies**: AP, AFP, Reuters (long-term wire agreements)
- **Factiva (Dow Jones) / LexisNexis** — licensed content for paywalled sources
- **TVEyes** — broadcast monitoring
- **Twitter/X** — official data partner (via Brandwatch)
- **Facebook** — official data partner (via Brandwatch)
- **IBM Watson** — Brandwatch historically used for AI/image recognition
- **Slack, Microsoft Teams** — workflow integrations
- Regional print monitoring firms globally

### Operational Complexity
- PR Newswire handling huge volume of press releases
- Cross-linking releases with media monitoring (matching quotes/text to coverage)
- Cision Insights: human analysts work directly with backend tools for custom client reports
- Support and analyst services division is significant
- Print monitoring teams in UK physically review newspapers/magazines

---

## Pricing & Go-to-Market

### Pricing
- **Enterprise SaaS model** with custom quotes
- Often **bundles services**: monitoring + PR Newswire distributions + media database access
- **Estimated range**:
  - Small teams: ~$6K–$12K/year (basic "Cision PR Edition")
  - Large enterprises: $50K–$100K/year (full CisionOne + social + database + distribution)
- PR Newswire distribution often transactional (per release or packages) — used as foot-in-the-door
- **Cision Insights** (analyst service): separate cost for premium clients
- **Known for price increases on renewal** (frequent user complaint)

### Tiers
- **Basic**: Media monitoring + limited newswire access
- **Plus**: Adds social listening, analytics dashboards
- **Premium/CisionOne**: Full suite + analyst support
- **Cision PR Edition**: Smaller teams, entry-level

### Go-to-Market Strategy
- **Strong direct sales approach**: targeting PR departments of large companies + top PR agencies
- Sales teams organized by region and industry (government, corporate, etc.)
- PR Newswire as lead generation funnel → upsell to monitoring suite
- Content marketing: annual "State of the Media" report, "Inside PR" report
- Long-standing reputation — many comms veterans default to Cision
- In India/APAC: sells via partners or lighter local presence (PR Newswire offices in India, China promote Cision software)

### Customer Segmentation
- **Fortune 500 companies**, government, PR agencies of all sizes
- Strong in: North America (dominant), Europe (UK, France via Gorkana/Cision UK)
- Asia/India: multinationals use it, some local firms via PR Newswire network
- Government and public sector communications teams

---

## Notable Clients
- **Fortune 500**: Coca-Cola, Amazon, Pfizer
- **PR agencies**: Edelman, FleishmanHillard (longtime users)
- **MMGY Grifco** — returned to Cision after trying alternatives, citing "immediate uptick in coverage captured"
- Government organizations
- UK PR agencies (via Gorkana media database legacy)

---

## Strengths
- **Largest media database** in the industry
- **React Score** — unique crisis/risk detection (no competitor replicates this)
- **PR Newswire** integration — closed-loop from release to pickup tracking
- "Best Media Monitoring Solution" award 2025
- Most complete media dataset claim (10K+ premium/paywalled sources)
- Human-curated print monitoring (high accuracy in UK)
- Cision Insights adds qualitative analyst layer

## Weaknesses
- Interface historically felt clunky (improved with CisionOne but still complex)
- Integration of multiple acquisitions creates tech debt
- Price increases at renewal (frequent complaint)
- Can be overwhelming — too many functions for simple use cases
- Legacy reputation can feel "old school" vs modern alternatives
