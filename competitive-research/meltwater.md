# Meltwater — Competitor Deep Dive

> Source: "Media Monitoring Product Landscape" report

---

## Company Profile

| Field | Detail |
|---|---|
| Founded | 20+ years ago (early 2000s), Norwegian origin |
| HQ | San Francisco, USA |
| Global presence | Offices in 55 countries, customers in 125+ countries |
| Customers | 27,000+ organizations globally |
| Scale | 500M+ new content pieces ingested daily, 2PB+ data stored, 200B+ documents indexed |
| Positioning | Breadth of coverage, real-time intelligence, integrated analytics |

---

## Product: Media Monitoring

### Core Capabilities
- Track keywords for brand, competitors, and topics across **all channels** in one unified system
- Real-time updates whenever keywords appear in news or social
- **Media channels**: Online news (270K+ sources), social media (15+ platforms incl. X firehose), forums, blogs, print (via partners), broadcast TV/radio (regional), podcasts (25K+)
- Advanced **Boolean searches** for precise filtering
- **Historical archives**: news back to ~2009, social up to 15 months

### Analytics Suite
- **Volume of mentions** tracking
- **Share of voice** across channels
- **Audience reach** estimation
- **Sentiment analysis** (positive/negative/neutral + emotion tagging)
- **Trending themes** associated with brand
- **Top publications, geographies, and influential journalists** identification
- **Competitive benchmarking** in real time (mention counts, sentiment, geographic spread side-by-side)
- **Image/logo recognition** in social posts (vision ML)

### Dashboards & Reporting
- **Unified Dashboards** (2025): combine paid, owned, and earned media in one view
- Configurable widgets: sentiment, share of voice, heatmaps, trending themes
- Interactive — drill down and explore
- Auto-refreshed, shareable with stakeholders via live links
- **Export API**: JSON feeds for Tableau, PowerBI, Google Data Studio
- Scheduled email reports, CSV exports, PDF reports
- Can build custom "command center" displays outside the app
- Learning curve noted for advanced tools

### Alerts & Delivery
- Real-time alerts via email and mobile push notifications
- **Mobile app** (iOS/Android) for on-the-go monitoring
- Configurable alert frequency
- Alerts piped into **Microsoft Teams**
- API/webhooks for custom integration

### AI & Advanced Features
- **GenAI Lens**: Monitors how brands are discussed by LLMs (ChatGPT, Gemini, Claude). Tracks which sources AI cites and brand's Share of Voice in AI-generated answers
- **MIRA**: AI writing assistant for social content
- Automated insights (explains "why" behind trends)
- Predictive analytics (virality prediction, potential impressions)
- Advanced sentiment beyond pos/neg — emotion tagging
- Topic modeling and entity extraction
- Image/logo recognition in social posts

### Media Database & Outreach
- Includes media contacts database (journalists/influencers)
- Press release distribution module
- Can identify top authors and integrate with email pitching
- Historically smaller database than Cision's

---

## Technology & Operations

### Infrastructure
- Runs entirely on **AWS**
- Large-scale **Kubernetes** deployment: hundreds of nodes, 10,000+ pods across multiple clusters
- Uses **Cilium** (advanced CNI) for network performance and security
- **2 petabytes+ of data** stored
- **200+ billion documents** indexed
- **200 million searches/week** executed
- Microservices architecture for crawling, NLP, indexing, analytics
- Real-time streaming pipeline (for alerts) + batch processing (for historical analytics)
- CDNs and geo-distributed clusters for low-latency globally
- "Foundation" engineering team for internal developer platform
- CI/CD via Harness (1,200 pipelines/day)

### Data Sourcing

| Source Type | Method |
|---|---|
| Online news/blogs | Proprietary web crawlers + RSS feeds (270K+ sources). NLP applied: language detection, entity tagging, topic classification |
| Social media | Official Twitter data reseller (X firehose). Platform APIs for FB, IG, YT, TikTok (via authorized data partners). Engagement counts + ML-inferred demographics |
| Print media | Partner network: regional monitoring firms that scan/OCR print publications |
| Paywalled/premium content | **Factiva (Dow Jones) partnership** — snippets/full text from WSJ, FT, etc. |
| Broadcast TV/Radio | Regional vendor integrations (possibly TVEyes in some markets, local agencies in others) |
| Podcasts | In-house transcription (25K+ podcasts) using speech-to-text (likely AWS Transcribe) |
| AI/LLM outputs | GenAI Lens queries ChatGPT, Gemini, Claude via APIs, parses and analyzes responses |

### Key Partnerships
- **Factiva (Dow Jones)** — licensed paywalled news content access
- **Twitter/X** — official data reseller (full firehose access)
- Platform APIs (Facebook, Instagram, YouTube, TikTok) — via authorized partners
- Regional print monitoring firms globally
- Regional broadcast monitoring vendors
- Possibly **GlobeNewswire** for press release distribution in some markets
- Partnership model: licensing fees (annual) or revenue-sharing

### Acquisitions that Bolstered Tech
- **Sysomos** — social analytics (historical social data)
- **Infomart** — media monitoring
- **AI research labs** — Silicon Valley + Norway, in-house NLP/ML innovation

---

## Pricing & Go-to-Market

### Pricing
- **Annual or multi-year licenses** with custom pricing
- No public pricing — consultative sales process (demo → tailored quote)
- Suite of modules: monitoring, social listening, consumer insights, press distribution
- Tiered by: number of users, volume of data/mentions, modules selected
- **Estimated range**: ~$10K/year (small business, basic monitoring) to six figures (global enterprise, multi-module)
- Known for price increases at renewal

### Go-to-Market Strategy
- **Global-local approach**: offices/reps in many countries, localized selling
- Aggressive salesforce targeting all company sizes (SME to enterprise)
- Content marketing: blog, webinars, guides for lead generation
- Land-and-expand: start with core monitoring, upsell analytics/historical/social modules
- Sales segmentation: SMEs via inside sales, large accounts via field sales
- Geography-specific pitches (e.g., local language coverage in Europe, global reach in APAC)

### Customer Segmentation
- **Mid-market and enterprise** primary targets, but also accessible to smaller businesses
- Strong in: North America, Europe (especially Scandinavia, DACH), Asia-Pacific (offices in India's metros)
- In India: services Indian conglomerates and agencies, emphasizes global + social coverage advantage over local players

---

## Notable Clients
- **Google** — 25% increase in target-region coverage within 6 months
- **The Economist** — global communications insight
- **H&M** — retail media monitoring
- **Swarovski**
- **The Hughes Agency** — PR agency, credits mobile app for preventing client from being blindsided
- **Aranca** (India) — tracks trends across Europe, Gulf, and US
- **CARE** (NGO)
- PR agencies: BCW, Weber Shandwick offices
- Tech: Facebook, Toyota
- Financial/services sector

---

## Strengths
- Broadest content ingestion (500M+ pieces/day)
- Most mature global infrastructure (125+ countries, 55 offices)
- Strong API and BI tool integration
- GenAI Lens — unique LLM monitoring capability
- #1 on G2 Crowd for media monitoring
- Flexible "build your suite" approach

## Weaknesses
- Learning curve for advanced features
- Can feel complex for new users
- Price increases at renewal (user complaint)
- Print/broadcast coverage dependent on regional partners (quality may vary)
