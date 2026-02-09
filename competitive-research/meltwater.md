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

---

## Product & Feature Analysis (Screenshot Walkthroughs)

> Source: Meltwater product screenshots from live demo/product pages. Analyzed for feature depth, user flow, and ICP relevance.

### Screenshot 1: Home Dashboard + Onboarding Modal

**What this screen shows:** The main landing page after login — the "home base" of Meltwater's product.

**Key elements observed:**

#### Left Sidebar Navigation (Primary Product Modules)
The sidebar reveals Meltwater's full product architecture — 8 top-level modules:
1. **Home** — dashboard/landing
2. **Explore** — search & discover brand/competitor/industry mentions across all sources
3. **Monitor** — personalized feeds of relevant media coverage
4. **Analyze** — analytics and reporting on coverage data
5. **Media Relations** — journalist database, media lists, pitching
6. **Newsletters** — curated newsletter creation/distribution
7. **Report** — formal report generation and management
8. **Alerts** — real-time notifications for new mentions
9. **Content** — configuration hub (searches, tags, labels, RSS feeds, manually added URLs)
10. **Account** — user/org settings

Media Relations, Report, and Content have expandable sub-menus (chevron icons), suggesting deeper feature sets within each.

#### Welcome Onboarding Modal
- Branded as **"Meltwater Media Intelligence"**
- Key claim: **"Powered by 1.3B+ data sources"** (up from 500M+ pieces/day mentioned elsewhere — likely cumulative indexed sources)
- Positions "Explore" as the primary entry point for new users
- Multi-step onboarding wizard (pagination dots visible — at least 7 steps)
- Tone: accessible, guided — acknowledges the product has a learning curve

#### "Pick Up Where You Left Off" Section
- Shows **recent activity cards** across different modules — user was working on:
  - "Automotive - Industry" (Explore, 4 days ago)
  - "Hospitality - Hotels" (Dashboards, 5 days ago)
  - "Electric Vehicles" (Dashboards, 5 days ago)
  - "Monitor" (Monitor, 5 days ago)
- **ICP relevance:** PR/comms teams track multiple brands, industries, and competitors simultaneously. This "recents" feature reduces friction for multi-topic workflows. Critical for users juggling 5-10 active monitoring searches.

#### Product Overview Cards (Behind Modal)
Each card represents a core workflow with a description + two CTAs ("Go to [Module]" + "Start training"):
1. **Explore insights and trends** — "Create and manage searches to monitor brand, competitor, and industry media coverage"
2. **Monitor media coverage** — "Personalize your monitoring experience to easily view, organize, and share relevant media coverage"
3. **Find and engage with journalists** — "Conduct media research, manage media lists, and pitch relevant story ideas to contacts"
4. **Report** — "Access and manage all of your reports"
5. **Manage your content** — "Manage all of your content configurations like searches, tags, labels, RSS feeds, and any manually added URLs"

The "Start training" CTA on every card confirms the product requires guided onboarding — a known weakness from reviews.

#### Right Sidebar — Alerts Panel
- **179 unread alerts** — shows this is a high-volume notification system
- Alert cards show:
  - **"Top Reach"** badge — alerts are prioritized/tagged by reach/importance
  - Time: "5h ago"
  - Example: *"Automotive - Industry - EV Charging Speed: MSN.com (122M) just wrote about fast charging, electric vehicle, electric cars"*
  - Includes **outlet reach number** (122M) inline — immediate context on impact
- **ICP relevance:** PR teams need to know immediately when a high-reach outlet covers their topic. The "Top Reach" prioritization and inline reach numbers let them triage fast — "is this MSN.com (122M reach) or a niche blog (5K reach)?"

#### Right Sidebar — Promotional Carousel
- "Explore Social & News Media" promo card — upsell/feature discovery within the product
- Suggests Meltwater uses the home screen for internal marketing of underused features

#### Other UI Elements
- **Platform Assistant** button (top right) — likely AI-powered help/search assistant
- **99+ notifications** badge — heavy notification system
- **Universal search bar** ("Find") — search across the entire platform
- **"BOOK A MEETING"** CTA + chat widget — sales/support always accessible, even inside the product
- **"The next generation of search has arrived — Go to Explore"** banner — they're actively pushing users toward their newer Explore module (suggests Monitor may be legacy)

#### User Flow Insights
- **Home → Explore** is the promoted primary path (onboarding modal, banner, first product card all point to Explore)
- The product appears to have evolved: "Monitor" seems like the older workflow, "Explore" is the newer, more powerful version
- Users can jump into any module from the sidebar, but the home page guides new users through a structured path
- The "Pick up where you left off" pattern suggests power users skip the home page and go directly to their active searches

#### ICP Value Summary for This Screen
| Element | ICP Value |
|---|---|
| Multi-module sidebar | Comms teams need monitoring + journalist outreach + reporting in one platform — reduces tool sprawl |
| Recent activity cards | PR teams track multiple brands/topics — quick resume reduces daily friction |
| Alert panel with reach scores | Immediate triage: "which coverage matters most right now?" |
| Training links on every module | Acknowledges complexity — but also signals a steep learning curve (weakness) |
| Universal search | Large teams with many saved searches need fast navigation |

---

### Screenshot 2: Explore Module — Search Creation & Management

**What this screen shows:** The "Explore" module — the foundation of Meltwater's product. This is where users create, manage, and organize their monitoring searches. Searches are the **core building blocks** that feed into every other module (dashboards, alerts, reports, monitors).

**Key elements observed:**

#### AI Search Assistant (Top Banner — Heavily Promoted)
- Prominent banner: **"Create and refine searches with AI Search Assistant"**
- Natural language input: *"Ask me to create a search for your desired brand or industry"*
- This is Meltwater's push to lower the Boolean search barrier — users can describe what they want in plain English and AI generates the query
- Positioned as the first thing users see in Explore — signals this is a key differentiator they're investing in

#### Three Search Creation Methods
Presented as equal-weight cards, but AI is visually highlighted (purple/brand color):

1. **Keyword Search** — "Use keywords to get results quickly and easily"
   - Simplest method — type a brand name, get results
   - Entry-level for new users or simple monitoring needs

2. **Advanced Search** — "Use Boolean queries for powerful and precise searches"
   - Boolean operators (AND, OR, NOT, proximity, etc.)
   - For power users who need precise filtering (e.g., "Tesla AND (battery OR charging) NOT stock")
   - Most saved searches in the list use this type — confirms power users prefer Boolean

3. **AI Search Assistant** — "Create and refine searches using AI"
   - Highlighted in brand purple — this is the feature they're pushing
   - Bridges the gap between simple keyword and complex Boolean
   - **ICP relevance:** PR teams often struggle with Boolean syntax. AI-assisted search creation removes a major friction point and reduces dependency on trained power users.

#### Onboarding Tooltip
- Guided wizard step: "Start by creating a search using: 1) Keywords, 2) Boolean queries, 3) AI Search assistant"
- Confirms structured onboarding flow continues into the Explore module

#### Saved Searches Table
Columns: **Name | Used in | Type | Created by | Last edited**

Visible searches:
| Search Name | Used In | Type | Created By | Last Edited |
|---|---|---|---|---|
| alert-electric-vehicles-battery-life | 0 places | Keyword | Maia Clinch | Oct 15, 2024 |
| Automotive - Industry - EV | 2 places | Advanced | Unknown | Mar 26, 2024 |
| Automotive - Industry - EV & Acceleration | 3 places | Advanced | Unknown | Jan 4, 2024 |
| Automotive - Industry - EV Autonomous Driving | 3 places | Advanced | Unknown | Feb 20, 2024 |
| Automotive - Industry - EV Battery Life | 3 places | Advanced | Unknown | Feb 20, 2024 |
| Automotive - Industry - EV Charging Speed | 3 places | Advanced | Unknown | Feb 20, 2024 |
| Automotive - Industry - EV Driving Range | 3 places | Advanced | Unknown | Feb 20, 2024 |
| Vegan | 0 places | Advanced | Maia Clinch | Oct 10, 2024 |

**Critical design insight — Searches are reusable building blocks:**
- The **"Used in" column** shows how many dashboards, monitors, or alerts each search feeds into
- A single search (e.g., "Automotive - Industry - EV") can be reused across 2-3 places — dashboards, alerts, reports all reference the same underlying search
- This means editing a search automatically updates everywhere it's used — powerful for consistency
- Searches persist for months (Jan 2024 → Oct 2024) — these are long-running, persistent monitoring queries, not one-off searches

**Naming convention insight:**
- Hierarchical naming: `Industry → Sub-industry → Topic` (e.g., "Automotive - Industry - EV Charging Speed")
- Suggests users create a **matrix of searches** — one parent topic broken into sub-topic searches for granular tracking
- A single brand/industry monitoring setup may require 5-10+ individual searches

**Team collaboration:**
- "Created by" shows different team members (Maia Clinch, Unknown) — searches are shared across the team
- Checkbox column suggests bulk operations (delete, move, assign)

#### Tabs (Partially Visible)
Below the search creation cards: `...sets` | `Author lists` | `Custom categories`
- "...sets" likely = "Presets" or "Datasets" — pre-built search templates
- **Author lists** — curated lists of journalists/authors to track (ties into Media Relations)
- **Custom categories** — user-defined taxonomies for organizing coverage (e.g., "Product launches", "Crisis", "Competitor moves")

#### ICP Value Summary for This Screen
| Element | ICP Value |
|---|---|
| AI Search Assistant | Removes Boolean barrier — junior team members can create searches without training |
| Three search tiers | Accommodates all skill levels — from intern doing keyword search to senior analyst doing Boolean |
| Reusable search building blocks | One search feeds dashboards + alerts + reports — consistency across workflows, edit once/update everywhere |
| Hierarchical search organization | PR teams monitoring 5+ topics per brand need structured organization |
| Team-shared searches | Multiple team members can create/manage searches — collaborative workflow |
| Persistent long-running searches | Media monitoring is continuous, not one-off — searches run for months/years |

---

### Screenshot 3 (5 images): Explore Module — Full Tabs, Labels & AI Search Assistant Flow

**What these screens show:** The complete user journey from the Explore search list → opening the AI Search Assistant → generating a Boolean query via natural language → previewing live results with analytics breakdown. This is the core "search creation" workflow.

#### 3a: Explore Module — Full Tab Bar & Label Organization

**New elements visible (not in Screenshot 2):**

**Full tab bar revealed:**
- **Searches** — saved search queries (currently selected)
- **Comparisons** — side-by-side comparison setups (likely brand vs. competitor)
- **Filter sets** — reusable filter combinations
- **Author lists** — curated journalist/author lists for tracking
- **Custom categories** — user-defined taxonomies

**Left sidebar — Label system:**
- "All searches: 8" — total search count
- **Labels section** with "Manage" link:
  - `Automotive` (6 searches)
  - `Walnut.io` (7 searches)
- Labels function as **folders/tags** for organizing searches by brand, client, or industry
- **ICP relevance:** PR agencies managing multiple clients need to separate searches by client. In-house teams need to separate by brand/product line. Labels solve this organization problem.

#### 3b: AI Search Assistant — Chat Interface (Empty State)

The AI Search Assistant opens as a **full-page chat interface** — a ChatGPT-style conversational UI inside Meltwater.

**Personalized greeting:** "Welcome, Jacob. I am your AI Search Assistant. I will help you create and refine searches."

**Two primary action cards:**
1. **Create brand search** — "Discover mentions and insights about your brand or products."
2. **Create industry search** — "Understand market trends, consumer behavior, and industry news."

This distinction is important — Meltwater recognizes that monitoring falls into two fundamental categories:
- **Brand monitoring:** "What is being said about us/our competitors?"
- **Industry monitoring:** "What trends are happening in our market?"

**Four secondary actions (refine existing searches):**
1. **Expand my current search** — broaden to catch more results
2. **Narrow down my current search** — reduce noise/false positives
3. **Review and repair my current search** — debug/fix a search that's not performing well
4. **Translate my current search** — convert a search to work in another language

**Bottom elements:**
- Chat input: "Message AI Search Assistant"
- File upload icon — can attach context
- Disclaimer: *"The AI Search Assistant can make mistakes. Please let us know when it does. Provide feedback"*

**ICP relevance:** The "expand/narrow/review/translate" actions address the exact pain points PR teams face with Boolean searches:
- Searches that are too broad (noise) → "Narrow down"
- Searches that miss coverage (gaps) → "Expand"
- Searches that suddenly stop working well → "Review and repair"
- Need to monitor a brand in French/German/Hindi → "Translate"

#### 3c: AI Search Assistant — Guided Example

Onboarding tooltip shows a pre-filled example prompt:
> *"Please create a search on conversations about electric vehicles and their cost?"*

This demonstrates Meltwater's onboarding strategy — show users concrete examples of natural language queries they can make. Reduces the blank-page problem.

#### 3d & 3e: AI Search Assistant — Query Generation + Live Results Preview

**The core AI workflow in action:**

**User prompt:** "Please create a search on conversations about electric vehicles and their cost?"

**AI Response — Keyword Expansion:**
The AI suggests synonyms for "price" and "cost":
- "value", "expense", "fee", "rate", "charge", "tariff"

**AI-Generated Boolean Query:**
```
(EV OR EVs OR "Electric vehicle") AND (price OR cost OR value OR expense OR fee OR rate OR charge OR tariff)
```
- Named: **"EV Cost and Price Expansion v2"**
- The AI automatically handles: synonym expansion, Boolean syntax, proper quoting, OR/AND logic
- Query box has three actions: **Preview | Save | ⋮** (more options)

**This is the key value proposition of AI Search Assistant:** A user typed one natural language sentence and got a properly structured Boolean query with synonym expansion that would take a trained analyst 10-15 minutes to build manually.

**Right Panel — Live Results Preview (178K results, Nov 11-18, 2024):**

The results panel shows an instant preview of what the search captures:

**1. Volume trend line** — mention count over time (line chart, ~1 week view)

**2. Source Type breakdown (bar chart):**
| Source | Count |
|---|---|
| News | 88.1k |
| X (Twitter) | 65k |
| Reddit | 11.8k |
| Social Message Boards | 2.32k |
| Podcasts | 1.07k |
| Social Comments | 691 |

**3. Country breakdown (bar chart):**
| Country | Count |
|---|---|
| United States | 65.1k |
| Unknown Location | 56.3k |
| Canada | 10.1k |
| India | 8.39k |
| Australia | 7.58k |

**4. Language breakdown:**
| Language | Count |
|---|---|
| English | 171k |
| French | 731 |
| (others) | 592, 485, 474 |

**5. Individual article results — rich metadata per article:**
Each result shows:
- **Source + Author:** MSN.com, Juliette Portala
- **Metadata tags:** `News | English | United States | Positive | today 20:02`
- **Headline:** "California unveils its first-ever 24/7 EV charging center..."
- **Snippet:** Article excerpt with **keyword highlighting** (EV, EVs highlighted in the text)
- **Entity tags:** EV, electric vehicle, EVs, cost
- **Reach:** 125.6M reach
- **Sentiment tag:** Positive / Neutral / Negative — shown inline per article

Multiple articles visible with different sentiment ratings:
- MSN.com, Juliette Portala — **Positive**
- MSN.com, Matt Oliver — **Neutral** (UK's biggest electric car charging network)
- MSN.com, Rick Kazmer — **Neutral** (Researchers develop revolutionary smart-charging)
- MSN.com, Matt Oliver — **Negative** (The campaign to debunk electric car 'myths' as sales falter)

**Critical design observations:**

1. **Two-panel layout:** Left = AI chat conversation, Right = live results. The user refines the query conversationally while seeing results update in real time. This is a powerful iterative workflow.

2. **Sentiment is per-article, not aggregated** — users can see at a glance which coverage is positive vs. negative. This is table-stakes for brand monitoring.

3. **Reach numbers are prominent** (125.6M) — tells PR teams the potential audience exposure immediately.

4. **Source type distribution** answers: "Where is this conversation happening?" — critical for knowing whether to focus on news response, social media response, or both.

5. **Country distribution** answers: "Where geographically is this being discussed?" — critical for global brands with regional PR teams.

6. **"Save" button** (top right, prominent teal) — one click to save this AI-generated search as a persistent, reusable search that feeds into dashboards, alerts, and reports.

#### ICP Value Summary for AI Search Assistant Flow
| Element | ICP Value |
|---|---|
| Natural language → Boolean query | Eliminates the #1 barrier to advanced monitoring — junior team members can create complex queries |
| Synonym expansion | Catches mentions that simple keyword searches miss (e.g., "tariff" for cost-related EV coverage) |
| Live results preview | Immediate validation — "does this search capture what I want?" before saving |
| Source type breakdown | Tells PR teams where the conversation is happening (news vs. social vs. Reddit) |
| Country breakdown | Global brands need geographic segmentation of coverage |
| Per-article sentiment | Instant triage — which coverage needs a response? |
| Reach per article | Prioritize by impact — a 125M-reach outlet matters more than a 5K-reach blog |
| Expand/narrow/translate actions | Address the full lifecycle of search maintenance, not just creation |
| Label organization | Agencies can separate searches by client; in-house teams by brand/product |

---

### Screenshot 4 (5 images): Explore — Search Library, Results View, Filters & AI Insights

**What these screens show:** Continuing the Explore flow — from search library management to opening a saved search, viewing results with rich filtering, AI-powered insights, mentions trend analytics, and per-article reach data.

#### 4a: Search Library Tooltip

Onboarding tooltip reveals a key selling point:
> *"This is your search library. Build unlimited adhoc searches with unlimited mentions. Save and tag to monitor over time."*

**"Unlimited" is notable** — some competitors (Brand24, Mention) limit searches by pricing tier. Meltwater positions "unlimited searches with unlimited mentions" as a feature — likely because they charge enough to absorb it.

#### 4b: Search Library — Label Filtering + Search Within Searches

**New interactions visible:**
- **"Automotive" label selected** (highlighted teal) — filters the list from 8 to 6 searches under that label
- **Search box with "Battery" typed** — further filters to 1 result: "Automotive - Industry - EV Battery Life"
- Tooltip: *"Manage your new and existing searches with Edit, Copy, and Delete."*
- Pagination: "1-1 of 1"

**Design insight:** Two-level filtering (label → text search) lets users with dozens or hundreds of saved searches find what they need quickly. This matters at scale — enterprise accounts may have 50-200+ saved searches.

#### 4c: Explore Results View — The Core Analysis Screen (Volume Tab)

This is the **most feature-dense screen in Meltwater**. It's where users spend most of their time. **The "Volume" tab is selected** — all analytics shown in this screenshot and the following ones (4d, 4e, 5a-5d) are Volume-specific views.

**Top Bar:**
- Search name: "Automotive - Industry - EV Battery Life" (dropdown to switch searches)
- Save button
- Date range: "Last 7 days" (dropdown)
- "Ignore case" toggle
- "Entity analysis" toggle
- "Actions" button (red/prominent)

**Full Boolean query visible:**
```
("electric vehicles" OR "electric cars" OR electricvehicles OR electriccars OR "electric vehicle" OR "electric car" OR electricvehicle OR electriccar)
```
- "AI Search Assistant" button — can jump back to AI chat to refine this query
- "Supported operators" link — documentation for Boolean syntax

**Filter Bar (7 filter dimensions):**
`Filter set | Source type | Language | Location | Keyword | Sentiment | Author | Custom categories`

Each filter is a dropdown with multi-select. This is the core filtering power of the platform.

**Analysis Tabs (4 views of the same data):**
- **Volume** (selected) — mention count trends
- **Narrative** — what's being said (topic/theme analysis)
- **Sentiment** — positive/negative/neutral breakdown
- **Engagement** — social engagement metrics (likes, shares, comments)

These four tabs are the primary analytical lenses within every Explore search. Each tab has its own set of analytics widgets and sub-views on the right panel, while the left panel (article feed) and the top filter bar (Filter set | Source type | Language | Location | Keyword | Sentiment | Author | Custom categories) persist across all tabs. **All screenshots from 4c onward through 5d are under the Volume tab.**

**Left Panel — Article Results Feed:**
- **1.08k Results** count with **"AI Tags"** toggle
- Sorted by: Date (with direction toggle)
- Action icons: download, list view, copy, eye/preview
- Search within results (magnifying glass)
- **First article is RADIO content:**
  - Source: SEN WA (Radio | AU | today · 12:00 AM) — Australian radio station
  - **Embedded video/audio player** — broadcast content is playable directly in Meltwater
  - Keyword highlighting in snippet (electric vehicle, battery life)
  - Entity tags: "electric vehicle, battery life"
  - Custom category tag: "Battery Life" (user-defined)
  - Sentiment: Neutral
- Second article: Greatest Hits Gloucestershire (Radio | GB) — UK radio

**This confirms Meltwater monitors broadcast radio** and includes playable audio/video content — not just text articles.

**Right Panel — Analytics Dashboard:**

**1. AI-Powered Insight (auto-generated summary):**
> *"The topic of the posts is primarily about elect... discuss the issues surrounding electric vehicl... The posts also mention the impact of misinfo..."*
- Thumbs up/down feedback buttons, regenerate, copy
- This is an **LLM-generated summary** of the entire result set — tells the user "here's what's happening in this topic right now" without reading individual articles

**2. Mentions Trend:**
- Total Mentions: **985** (↓16% vs. previous period 1.17k)
- Line chart: Oct 16 - Oct 22 (daily resolution)
- Period-over-period comparison built in

**3. Date Range Dropdown (10 presets + custom):**
Today | This week | Last 7 days | Last 14 days | This month | Last 30 days | This quarter | Last 90 days | This year | Last year | Custom...

**Onboarding tooltip reveals data depth:**
> *"Choose a time frame. You get access to 10 years+ of historical news data and 15 months of historical social data."*

**10+ years of news archives is a massive moat.** AlmaLabs cannot replicate this without licensing (LexisNexis, Factiva).

#### 4d: Location Filter — Country-Level Multi-Select with Counts (Volume Tab)

**Location filter dropdown showing:**
| Country | Mention Count | Selected? |
|---|---|---|
| United States | 7.53k | No |
| Unknown | 713 | No |
| India | 614 | No |
| United Kingdom | 514 | Yes ✓ |
| Australia | 390 | Yes ✓ |
| Canada | 249 | Yes ✓ |
| Germany | 182 | No |
| Ireland | 93 | No |
| Jordan | 79 | No |
| China | 49 | No |
| Singapore | 42 | No |

- **3 countries selected** — filter bar shows "Location (3)"
- Each country shows mention count + a trend arrow icon
- "Select all" and "Clear" options
- Search box to find specific countries
- Total results: 11.6k (broader date range: Sep 1 - Oct 22)

**Right panel with filters applied:**
- AI-Powered Insight: different text about battery life prediction and LQMs (Large Quantitative Models) by SandboxAQ
- Daily Average: **213** (↑2%, previous period 210)
- Mentions trend chart: Sep 1 - Oct 22 with spike dots highlighted on peaks

**Onboarding tooltip:** *"Apply filters to fine-tune your search. Select multiple locations and languages."*

**ICP relevance:** Global brands need to see coverage by country. A PR team in London wants to see UK/AU/CA coverage separately from US coverage. Regional PR leads need their geographic slice.

#### 4e: Filtered Results — AI Insight + Reach Per Article (Volume Tab)

**With filters applied (3 locations, 1 custom category), 1.15k results:**

**AI-Powered Insight (contextual, changes with filters):**
> *"The increase in volume is due to Battery X Metals' portfolio company LIBRT engaging a leading patent law firm to file patents for innovative EV battery diagnostic and rebalancing software and hardware. This news has generated significant interest and discussion in the EV industry and among investors."*

**This is genuinely useful** — the AI doesn't just summarize topics, it explains **why volume changed**. It identified a specific company (LIBRT) and a specific event (patent filing) as the driver of a spike. This is the kind of insight that saves a PR analyst 30-60 minutes of manual reading.

- Thumbs up/down, regenerate, copy buttons — feedback loop for AI quality

**Mentions Trend:**
- Total Mentions: **1.15k** (↓21%, previous period 1.46k)
- Daily Average: **22** (↓21%, previous period 28)
- Line chart with a visible spike around Sep 21 — clickable spike point matches the AI-explained event

**Article results:**
- Radio content with audio player, entity tags, sentiment
- "The UK Charging Infrastructure Symposium · Mankirat Kaur" (News | GB)

**Onboarding tooltip:** *"See search results with reach highlighted for each article."*
- Shows **"260 Reach"** at the bottom of an article card — every article has reach displayed

#### ICP Value Summary for This Screen Sequence
| Element | ICP Value |
|---|---|
| AI-Powered Insight (auto-generated) | Saves 30-60 min — explains "why" behind volume changes, identifies specific events driving coverage |
| 10 years+ historical news data | Deep historical analysis, trend comparison, crisis lookback — a major competitive moat |
| 7-dimension filter bar | Lets PR teams slice data by source, language, location, sentiment, author — answers any coverage question |
| Country-level filtering with counts | Global brands need geographic segmentation for regional PR teams |
| Volume/Narrative/Sentiment/Engagement tabs | Four analytical lenses on the same data — comprehensive coverage analysis |
| Broadcast radio content with playback | Full media monitoring — not just text articles, actual audio/video content |
| Period-over-period comparison | "Is coverage increasing or decreasing?" — the first question any PR team asks |
| Per-article reach | Immediate impact assessment — prioritize high-reach coverage |
| Custom categories | User-defined taxonomies — PR teams tag coverage by campaign, product line, issue area |
| Unlimited searches + unlimited mentions | No artificial limits — scales with the user's needs (at enterprise pricing) |

---

### Screenshot 5 (4 images): Explore — Article Detail, AI Spike Analysis & Analytics Dashboard (All Under Volume Tab)

**What these screens show:** Still within the **Volume tab** of Explore. Drilling deeper into individual articles (entity extraction, reach, sentiment, sharing actions), AI-powered spike analysis on the trend chart, and the Volume tab's analytics widgets (top locations at city level, top editorial sources, source type breakdown).

#### 5a: Content Analysis Panel — Per-Article Deep Dive

Clicking on an article opens a **"Content analysis"** side panel with rich metadata:

**Article info:**
- Source: The UK Charging Infrastructure Symposium (News | GB | yesterday · 6:58 PM)
- Headline: "Vector Informatik GmbH's Peter Guse explores MCS a..."
- Snippet with keyword highlighting ("electric vehicles")
- Entity tags: "electric vehicles, battery li..." with "Show more"
- Custom category: "Battery Life"
- Thumbnail image

**Actions menu (6 actions per article):**
1. **Open in a new tab** — read the full article on the publisher's site
2. **Tag** — apply labels/categories to the article
3. **Share** — share internally
4. **Post to X** — publish directly to Twitter/X
5. **Post to Facebook** — publish directly to Facebook
6. **Post to LinkedIn** — publish directly to LinkedIn

**The social posting actions are significant** — a PR team can find relevant coverage and amplify it on their brand's social channels directly from Meltwater, without leaving the platform. This is an earned-to-owned media workflow.

**Right side — Article-level analytics:**

**Sentiment:** Neutral (with emoji-style face icon)

**Potential reach (donut chart):**
| Channel | Share | Count |
|---|---|---|
| Mobile | 47% | 123 |
| Web | 53% | 137 |

Reach is broken down by mobile vs. web — tells PR teams how the audience consumed this content.

**Top Entities (NER + per-entity sentiment):**
| Entity | Type | Sentiment |
|---|---|---|
| Lee Guse | Person 👤 | Neutral |
| Vector | Company 🏢 | Positive |
| megawatt | Company 🏢 | Positive |
| guse | Company 🏢 | Not Rated |
| germany | Location 📍 | Positive |

**This is entity-level sentiment analysis** — not just "is the article positive/negative" but "how is each entity mentioned in the article portrayed?" This is exactly what brand monitoring needs: "Our brand was mentioned in a negative article, but the sentiment about *us specifically* was positive."

**ICP relevance:** When a PR Director asks "how was our brand portrayed in this article?", entity-level sentiment answers directly — even if the article overall is negative about the industry, the brand might be mentioned positively.

#### 5b: AI-Powered Insights Tooltip

Onboarding tooltip:
> *"AI-Powered Insights highlight key brand performance drivers and trends for quick brand insights."*

Confirms the AI insight feature is positioned as a "quick brand intelligence" tool — skip the 100-article reading and get the summary instantly.

"Regenerate" button visible — user can ask for a fresh AI analysis if the first one isn't useful.

#### 5c: Spike Analysis — AI-Powered Spike Drill-Down (Most Impressive Feature)

**Clicking on a spike point in the mentions trend chart opens a detailed spike analysis popup:**

**Header:** "110 Mentions · Oct 2" / "Mentions spiked 4x higher than average"
**Badge:** "News Spike"

**Structured spike breakdown (6 dimensions):**

1. **Volume context:** "Mentions spiked to **110** on Oct 02, compared to a daily average of **25** in the previous period."

2. **Source type driver:** "**Top Source Types: News** was up **6x** from an average of **15** mentions to **101**."

3. **Topic driver:** "**Top Terms: ev adoption** appeared in **92** mentions, exceeding the average."

4. **Sentiment analysis:** "**Sentiment: 98%** of non-neutral mentions were **positive**, **5x** higher than average."

5. **Geographic driver:** "**Top Location: 92** mentions were from **Australia**, **13x** higher than average."

6. **Top content by reach:** "The following content had the highest reach: **7NEWS** (Licensed by Copyright Agency) · News | AU | Oct 2 · 8:35 AM"
   - Note: *"Content from this publisher is not available in yo..."* — **even Meltwater has content licensing restrictions** on some publishers (7NEWS via Copyright Agency in Australia)

**"View more insights" link** — drill deeper

**Onboarding tooltip:** *"AI Spike Summary quickly analyzes sources and keywords driving spikes."*

**This is arguably Meltwater's most impressive analytical feature.** It answers the question every PR team asks when they see a spike: "What happened? Why did mentions jump? Is it good or bad? Where is it coming from?" All answered automatically in one click.

**For AlmaLabs:** This spike analysis is a feature that would be relatively straightforward to build with LLMs — analyze the day's articles vs. the baseline, identify top drivers by source/topic/location/sentiment. High-impact, moderate build effort.

#### 5d: Analytics Dashboard — Top Locations (City-Level) + Top Editorial Sources (Volume Tab, Scrolled Down)

**Scrolling down in the Volume tab's right-side analytics panel reveals deeper breakdowns. These widgets are specific to the Volume tab:**

**Source Type Breakdown (colored bar chart at top):**
| Source Type | Count |
|---|---|
| Broadcast | 275 |
| X (Twitter) | 91 |
| Forums | 15 |
| Blogs | 1 |
| Comments | 1 |

**Top Locations — City-Level Granularity:**
Dropdown: "City" (can switch to Country, State/Region)
| City | Mentions |
|---|---|
| London | 192 |
| Toronto | 50 |
| Vancouver | 47 |
| Subiaco | 30 |
| Mount Macedon | 25 |
| Québec | 19 |
| Kew East | 19 |
| Eveleigh | 18 |
| Stanmore | 18 |
| Sydney Central Business District | 15 |
Pagination: "1-10 of 35 Locations"

**City-level location data is a premium feature** — most budget tools only offer country-level. This lets PR teams understand coverage at a hyper-local level.

**Top Editorial Sources (ranked by mention count):**
| Rank | Publication | Mentions |
|---|---|---|
| 1 | Yahoo! Canada | 25 |
| 2 | WhaTech | 25 |
| 3 | Insider Tracking | 20 |
| 4 | Le Lézard | 19 |
| 5 | Kelowna Daily Courier - FinancialContent | 17 |
| 6 | Canadian... | (partially visible) |
| 7 | Theweek... | (partially visible) |
Pagination: "1-7 of 30 Editorial Sources"

**ICP relevance:** PR teams need to know which outlets are covering them the most. This ranked list directly answers "which publications should I build relationships with?" and "which outlets are driving our coverage?"

**Onboarding tooltip:** *"View live, real-time analytics"*

#### Volume Tab — Complete Widget Inventory (Screenshots 4c-5d Combined)

The Volume tab's right-side analytics panel contains these widgets (top to bottom):
1. **AI-Powered Insight** — LLM-generated summary of what's driving the results
2. **Mentions Trend** — total mentions + daily average + period-over-period % change + line chart (with clickable spike points)
3. **Source Type Breakdown** — bar chart (News, X/Twitter, Reddit, Broadcast, Forums, Blogs, Podcasts, Social Comments)
4. **Top Locations** — bar chart with city/state/country toggle (e.g., London 192, Toronto 50)
5. **Top Editorial Sources** — ranked publication list with mention counts (e.g., Yahoo! Canada 25, WhaTech 25)

The left panel (article feed) persists across all tabs and shows: article cards with source, author, timestamp, snippet with keyword highlighting, entity tags, custom category tags, sentiment label, and reach number.

#### ICP Value Summary for This Screen Sequence
| Element | ICP Value |
|---|---|
| Per-article entity extraction + entity-level sentiment | "How is *our brand specifically* portrayed?" — even in mixed/negative articles |
| Social posting (X, Facebook, LinkedIn) from article view | Earned → owned media amplification without leaving the platform |
| AI Spike Analysis (6-dimension breakdown) | Instantly answers "what happened and why?" — saves 30-60 min of manual analysis |
| City-level location data | Hyper-local coverage analysis for regional PR strategies |
| Top Editorial Sources ranking | "Which outlets cover us most?" — informs media relationship strategy |
| Reach breakdown (mobile vs. web) | Audience consumption channel insight |
| Content licensing limitations visible | Even Meltwater can't show all content — 7NEWS restricted by licensing |

---

### Screenshot 6: Explore — Narrative Tab

**What this screen shows:** The **Narrative tab** within Explore results for the same search ("Automotive - Industry - EV Battery Life", Sep 1 - Oct 22, 1.15k results, same filters applied). The Narrative tab answers: **"What are the main stories and themes being discussed?"**

**Persistent elements (same across all tabs):**
- Boolean query, filter bar (Filter set | Source type | Language | Location (3) | Keyword | Sentiment | Author | Custom categories (1)), left-side article feed — all unchanged from Volume tab

**Narrative tab-specific right panel widgets:**

#### 1. AI-Powered Insight (Narrative-Specific)
> *"Many of the posts are about the rise of electr... hydrogen-powered electric cars. Some posts... There is a mention of a specific company, Ce..."*

The AI insight here is **different from the Volume tab's** — it focuses on narrative themes rather than volume drivers. Mentions hydrogen-powered cars and a specific company as key themes.

Onboarding tooltip: *"AI highlights sub-themes and narratives within your time-frame."*

#### 2. AI-Powered Clusters (The Core Narrative Feature)

A table showing **AI-generated topic clusters** — the system automatically groups 1.15k articles into thematic clusters:

| # | Cluster (Representative Summary) | Mentions |
|---|---|---|
| 1 | The Cathode Materials Market is expected to grow at a CAGR of 5% from January 2021 to January 2022. | 17 |
| 2 | Global Electric Scooter Battery Market projected to grow at a CAGR of 21.6% from 2021 to 2030. Increasing fuel prices are the driving factors. | 16 |
| 3 | West Shore RCMP officers have been piloting a Tesla Model Y since early 2023, and this week are getting behind the wheels of a Ford F-150 Lightning pickup truck. | 15 |
| 4 | Autoimmune Disease Testing Market by Product Type (Instruments and Consumables and kits), Disease Type (Rheumatoid Arthritis, Systemic Lupus Erythematous, Scleroderma, Vasculitis, Inflammatory Bowel Disease and Others) | 13 |
| 5 | The new SMU family provides designers of automotive battery management systems with a single solution for the needs of FHEV, PHEV and BEV technologies | 11 |
| 6 | In this article, we will look at where EnerSys ranks among the best battery stocks to buy according to analysts. | 10 |
| 7 | CNT-coated aluminum foil (CCAF) is designed to meet the rising demand for faster charging and sodium-ion batteries | (partially visible) |

Pagination: **"1-7 of 30 Clusters"**

**Table/Chart toggle** visible (currently in Table view) + download icon — suggests an alternative visual view (likely a bubble chart or treemap).

**Key observations about Narrative Clusters:**

1. **Automatic topic discovery** — the system groups 1.15k articles into 30 distinct narrative clusters without any user input. This answers "what are the top stories in my topic right now?"

2. **Each cluster is described by a representative sentence** — not just a keyword but a full contextual summary. This gives much more meaning than a simple word cloud.

3. **Mention counts per cluster** — shows relative weight of each narrative thread. PR teams can see which stories are dominating the conversation (Cathode Materials Market = 17 mentions, biggest cluster).

4. **Noise is visible** — Cluster 4 (Autoimmune Disease Testing) appears to be a false positive/irrelevant result caught by the broad Boolean query. This is a real-world accuracy issue that demonstrates the importance of search refinement. Also shows Meltwater's clustering isn't perfect.

5. **30 clusters from 1.15k results** — roughly 1 cluster per ~38 articles on average, though distribution is uneven (top clusters have 10-17 mentions, long tail likely has fewer).

**ICP relevance:**
| Element | ICP Value |
|---|---|
| AI-Powered Clusters | Answers "what are the main stories about my brand/topic?" without reading hundreds of articles |
| Narrative-specific AI Insight | Different from Volume's — focuses on themes and sub-themes, not volume drivers |
| Cluster mention counts | Prioritize which narratives to respond to — biggest clusters = dominant stories |
| 30 clusters from 1.15k articles | Granular topic decomposition — far beyond what keyword-only tools offer |
| Table + chart toggle | Flexible presentation for different use cases (analysis vs. reporting) |
| Noise/false positives visible | Real-world limitation — Boolean queries catch irrelevant results; search refinement matters |

---

### Screenshot 7 (4 images): Explore — Sentiment Tab

**What these screens show:** The **Sentiment tab** within Explore results for the same search ("Automotive - Industry - EV Battery Life", Sep 1 - Oct 22, 1.15k results). The Sentiment tab answers: **"Is coverage positive or negative, how is sentiment trending, and what's driving each sentiment?"**

**Persistent elements (same across all tabs):** Boolean query, filter bar, left-side article feed — unchanged.

#### 7a: Sentiment Tab Overview

**Sentiment tab-specific right panel widgets:**

**1. AI-Powered Insight (Sentiment-Specific — Structured as Positive vs. Negative)**

Unlike Volume (which explains volume drivers) and Narrative (which highlights themes), the Sentiment tab's AI Insight is **explicitly split into positive and negative**:

> **Positive mentions:** "Several posts discuss the rise of electric car sales, which is attributed to manufacturers limiting the production of petrol models. Center Parcs receives a top award, and the director expresses their commitment to the company. The best long-range electric cars of 2024 are highlighted, showcasing the top 10 models with impressive range capabilities."

> **Negative mentions:** "The decrease in the number of people willing to buy an electric vehicle is a concern for the EV market. The issue of battery life and range is still a significant concern for potential buyers of electric cars. There is a lack of understanding among petrol drivers about electric vehicle charging and battery life. Research suggests that petrol drivers often have misconceptions about electric car ownership, including charging and battery life."

**This structured positive/negative summary is exactly what a PR team needs** — "what are people saying good about us, and what are the concerns?"

Thumbs up/down, regenerate, copy buttons for feedback.

Onboarding tooltip: *"AI summarizes sentiment across 240+ languages."*

**2. Sentiment Distribution (Donut Chart)**
| Sentiment | Percentage | Count |
|---|---|---|
| Positive | 31.7% | 366 |
| Not Rated | 0% | 0 |
| Neutral | 61.1% | 705 |
| Negative | 7.1% | 82 |

The donut provides instant visual — majority neutral (61%), significant positive (32%), small negative slice (7%).

**3. Sentiment Trend (Multi-Line Chart)**
- Time series: Sep 1 - Oct 22
- Separate colored lines for Positive (green), Negative (red), Neutral (gray)
- Shows how sentiment fluctuates over time
- Hoverable data points with tooltip

#### 7b: Sentiment Trend — Interactive Hover + Spike Detection

Hovering over a data point in the Sentiment Trend chart reveals:
- **Source:** Positive
- **Date:** 10-01-2024
- **Time:** 07:00 PM
- **Count:** 52

Onboarding tooltip: *"Spike detection & analysis: Interact with analytics. Understand what's driving shift in sentiment."*

**Confirms that the spike analysis feature from Volume tab also works in Sentiment tab** — clicking a sentiment spike would show what drove the sentiment shift. This is critical for crisis detection: "Why did negative sentiment spike on Tuesday?"

#### 7c: Sentiment Tab Scrolled Down — Sentiment By Source + Filtered Mentions Drill-Down

**New widgets visible when scrolled:**

**4. Sentiment By Source (Stacked Bar Chart)**
- X-axis: All | Blogs | Broadcast | Comments | Forums (more columns likely hidden)
- Y-axis: 0-100%
- Color stacks: Positive (green), Not Rated, Neutral, Negative (red)
- **Visual insight:** Broadcast content is overwhelmingly neutral, Blogs skew more positive, Forums show some negative. Each source type has a different sentiment profile.

**ICP relevance:** Tells PR teams "where is the negative sentiment coming from?" — if negative coverage is concentrated in forums but news is positive, the response strategy differs completely from negative news coverage.

**5. Top Keyword Sentiment** — section header visible at bottom (content cut off), likely shows sentiment breakdown per keyword/entity.

**Filtered Mentions Slide-Out Panel (clicking a chart segment):**

Clicking on a segment (e.g., "News + Positive") opens a **"Filtered Mentions"** right-side panel:
- Tabs: **Mentions** | **Analytics**
- Active filter: "Viewing: News (Source), Positive (sentiment)"
- "Add filter" button for further refinement
- **Total Mentions: 347** (↑ <1%)
- Mini trend chart
- **AI-Powered Insight (context-specific to the filter):**
  > "Several posts discuss electric car sales and the impact of rationing petrol models on electric car sales. There are multiple posts featuring different companies in the battery industry, such as Enovix Corporation, Apple Inc., Plug Power Inc., Sigma Lithium Corporation, and Albemarle Corporation. The posts also mention the rise of electric vehicle companies and their potential to outperform..."
  + "Show more" link
- **347 article results** sorted by Date
- Article: just-auto.com (News | GB) — "Valeo and TotalEnergies expand partnership to enhance EV batteries" — Positive sentiment, "Battery Life" category tag

Onboarding tooltip: *"Dive into content driving positive spikes. Results are from unsampled data."*

**This drill-down is powerful** — a user can click on "Positive News" in the chart and immediately see all 347 positive news articles with their own AI summary. Same for "Negative Blogs" or "Neutral Broadcast." Every chart segment is clickable and explorable.

#### 7d: Platform Assistant — AI-Powered Alert Creation (Sentiment Shift)

The **Platform Assistant** (top-right "Beta" feature) is opened, showing a conversational AI that can **take actions inside the platform**, not just answer questions.

**User prompt:** "create an alert for change in sentiment for electric vehicles battery life"

**AI Assistant response:**
> "Hot Topic Alerts — Yes, I can create a Smart Alert for you. Alerts automatically send key insights about your brand, competitors, or industry trends. Please enter the details below:"

**Alert configuration form (AI-generated):**
- **Alert Type:** Sentiment Shift
- **Saved Searches:** "alert-electric-vehicles-b..." (auto-populated from user's saved searches)
- **Delivery Method:** Email | Meltwater web (toggle options)
- Submit button

**AI confirmation:** "Your alert has been created, you can check it out on the Alerts page."

Onboarding tooltip: *"Send alerts to email, Meltwater web, Meltwater mobile app, Slack, and Microsoft Teams!"*

Beta disclaimer: "I'm still in beta and can make mistakes."

**This is a significant capability** — the Platform Assistant goes beyond the AI Search Assistant (which only creates searches). It can:
- Understand a natural language request ("alert me when sentiment changes")
- Map it to the right alert type ("Sentiment Shift")
- Auto-populate the relevant saved search
- Offer delivery options (email, web, mobile, Slack, Teams)
- Create the alert in one step

**ICP relevance:** A PR Director can say "alert me if sentiment about our brand turns negative" and have it configured in 30 seconds vs. navigating multiple settings screens. This is a genuine AI workflow improvement, not just a gimmick.

#### Sentiment Tab — Complete Widget Inventory

The Sentiment tab's right panel contains (top to bottom):
1. **AI-Powered Insight** — structured as Positive mentions / Negative mentions summaries
2. **Sentiment Distribution** — donut chart (Positive / Neutral / Negative / Not Rated with counts)
3. **Sentiment Trend** — multi-line time series (one line per sentiment, with spike detection)
4. **Sentiment By Source** — stacked bar chart showing sentiment composition per source type
5. **Top Keyword Sentiment** — (partially visible) sentiment breakdown per keyword/entity

Every chart segment is clickable → opens a **Filtered Mentions** drill-down panel with its own AI Insight + article list.

#### ICP Value Summary for Sentiment Tab
| Element | ICP Value |
|---|---|
| Positive/Negative AI summary split | Directly answers "what's being said good/bad about us?" — the #1 PR question |
| Sentiment donut with counts | Instant visual: "what % of coverage is negative?" — key metric for exec reporting |
| Sentiment trend over time | "Is sentiment improving or deteriorating?" — tracks effectiveness of PR campaigns |
| Sentiment By Source | "Where is the negativity coming from?" — different response strategies for news vs. forums |
| Clickable chart → Filtered Mentions | Every data point is explorable — zero-click to see the actual articles behind any metric |
| Platform Assistant: Sentiment Shift alerts | Conversational AI creates alerts in 30 seconds — "tell me if sentiment changes" |
| Alert delivery: Email, Web, Mobile, Slack, Teams | Meets PR teams where they work — no need to log into Meltwater to get alerted |
| 240+ language sentiment analysis | Global brands need sentiment across all markets, not just English |

---

### Screenshot 8 (2 images): Analyze Module + Report (Insight Reports)

#### 8a: Analyze Module — Topic Share of Voice Dashboard

**What this screen shows:** The **Analyze module** — a separate module from Explore. This is a **pre-built, multi-search comparison dashboard** that visualizes Share of Voice across multiple saved searches side by side.

**Module:** Analyze (selected in sidebar)
**Dashboard:** "Electric Vehicles" (with settings gear + "Saved" indicator)
**Tabs:** `Electric Vehicles` (selected, dropdown) | `Brand Analysis` | `+` (add new)
**Top right controls:** Select a date | Edit inputs | Add insight | Share

**5 dashboard widgets visible:**

**1. Share of Voice by Mentions (Last 90 days)**
| Topic (Saved Search) | Mentions |
|---|---|
| Automotive - Industry - EV & Acceleration | 23.4k |
| Automotive - Industry - EV Autonomous Driving | 58.3k |
| Automotive - Industry - EV Battery Life | 18.6k |
| Automotive - Industry - EV Charging Speed | 55.9k |
| Automotive - Industry - EV Driving Range | 49.3k |

Horizontal bar chart — instant visual comparison of which sub-topics get the most discussion.

**2. Share of Voice by Engagement (Last 90 days)**
| Topic | Engagement |
|---|---|
| EV & Acceleration | 106k |
| EV Autonomous Driving | 186k |
| EV Battery Life | 52.9k |
| EV Charging Speed | 163k |
| EV Driving Range | 230k |

Engagement (likes, shares, comments) tells a different story than mentions — EV Driving Range has the most engagement (230k) despite not being the most mentioned.

**3. Share of Voice by Editorial Reach (Last 90 days)**
| Topic | Editorial Reach |
|---|---|
| EV & Acceleration | 52.2B |
| EV Autonomous Driving | 94.7B |
| EV Battery Life | 19.1B |
| EV Charging Speed | 83.9B |
| EV Driving Range | 102B |

Reach is in **billions** — aggregate potential audience across all articles. EV Autonomous Driving has the highest reach (94.7B).

**4. Share of Voice by Source Type (Last 7 days)**
- Stacked bar chart
- X-axis source types: **News, X, Broadcast, Reddit, Podcasts, Forums, Blogs, WeChat, Comments, Sina Weibo, Pinterest**
- Each bar segmented by the 5 sub-topics (color-coded)
- Shows where each topic's conversation is concentrated
- Notable: **WeChat and Sina Weibo** are included — confirms Meltwater covers Chinese social platforms

**5. Top Organizations and Share of Voice (Last 7 days)**
- Horizontal stacked bar chart
- Organizations ranked by total mentions:
  - **Tesla** (~2k, dominant)
  - EIN Presswire, NEO Battery Materials, U.S. Securities and Exchange Commission, Hyundai, PR Newswire, Dido, Tether, SERES, Allied Market Research
- Each bar segmented by which sub-topic the mentions relate to

**Key design insights:**

1. **Analyze is a dashboard builder, not a search tool.** It takes multiple saved searches from Explore and compares them visually. The searches are the building blocks; Analyze is the reporting layer.

2. **"Edit inputs" button** — users can swap which saved searches feed the dashboard. This means one dashboard template can be reused for different brands/topics by changing the inputs.

3. **"Add insight" button** — likely adds AI-generated insight widgets alongside the charts.

4. **"Brand Analysis" tab** — suggests a second dashboard view for competitive benchmarking (our brand vs. competitors), confirming the Analyze module supports multiple analysis templates.

5. **Three metrics for Share of Voice:** Mentions (volume), Engagement (social interaction), and Editorial Reach (potential audience). These three dimensions give a complete picture — a topic might have low mention volume but massive reach if covered by a tier-1 outlet.

6. **Source types include WeChat, Sina Weibo, Pinterest** — broader than just Western platforms. Global brands monitoring in China need this.

Onboarding tooltip: *"Visualize brand analytics with share of voice and custom timeframes."*

**ICP relevance:** Share of Voice is one of the most commonly requested PR metrics. "Are we being talked about more than our competitors?" / "Which sub-topics dominate the conversation?" This dashboard answers both instantly.

---

#### 8b: Report Module — Insight Reports

**What this screen shows:** The **Report module** with its **Insight Reports** sub-section. This is where users create, manage, and schedule executive-ready reports.

**Report module sub-sections (sidebar expanded):**
1. **Digest reports** — likely automated daily/weekly digests
2. **Dashboard reports** — export Analyze dashboards as reports
3. **Insight reports** (selected) — AI-powered executive summary reports

**Page:** "Create an Insight Report or revisit a saved report"
**"Create report" button** (top right, prominent)
**Banner:** "Click here to access your reports in the previous version" — suggests recent redesign

**Recently edited reports (visual cards with cover images):**
| Report | Date |
|---|---|
| Electric Vehicle Topics - Q3 2024 | Oct 10, 2024 |
| Insight Report - Jun 2024 | Jul 10, 2024 |
| Insight Report - Q1 2024 | May 28, 2024 |

Reports have **cover images** (EV charging station photos) — designed to be presentation-ready and visually professional for executive sharing.

**All Insight Reports table:**
| Name | Created by | Date created | Last edited | Schedule |
|---|---|---|---|---|
| Electric Vehicle Topics - Q3 2024 | Maia Clinch | Oct 10, 2024 | Oct 15, 2024 | -- |
| Insight Report - Jun 2024 | Ayesha Wallia | Jul 10, 2024 | Sep 13, 2024 | -- |
| Insight Report - Q1 2024 | Ella Soares | May 28, 2024 | Sep 13, 2024 | -- |

**Key observations:**

1. **Three report types** serve different cadences: Digests (daily/weekly automated), Dashboard (data-heavy), Insight (AI-generated executive summaries).

2. **Multiple team members creating reports** (Maia Clinch, Ayesha Wallia, Ella Soares) — collaborative, team-based workflow.

3. **Quarterly cadence** visible (Q1 → Jun → Q3) — aligns with standard PR reporting rhythms (quarterly board reports, monthly reviews).

4. **"Schedule" column** (all "--") — reports can be set to auto-generate on a schedule. None are scheduled here, but the capability exists for automated recurring reports.

5. **Cover images make reports shareable** — these are meant to be sent to CMOs and executives, not just internal analysis. Visual polish matters.

Onboarding tooltip: *"Share executive summaries with AI analysis by creating Insight Reports."*

**ICP relevance:**
| Element | ICP Value |
|---|---|
| Share of Voice (3 metrics) | The #1 PR metric — "are we being talked about more than competitors?" |
| Multi-search comparison dashboards | Compare sub-topics, brands, or competitors side by side |
| Mentions vs. Engagement vs. Reach | Three dimensions give a complete picture — volume alone is misleading |
| Top Organizations widget | "Which companies dominate this topic?" — competitive intelligence |
| Source type comparison (incl. WeChat, Sina Weibo) | Global coverage including Chinese platforms |
| Three report types (Digest, Dashboard, Insight) | Different formats for different audiences — daily ops vs. quarterly exec review |
| AI-powered Insight Reports | Executive summaries generated by AI — saves hours of manual report writing |
| Scheduled reports | Automated recurring delivery — set once, executives get it every Monday |
| Cover images on reports | Presentation-ready — designed to be shared up the chain |

---

# Deep Research: Comprehensive Meltwater Product Analysis

> Generated from 7 parallel research agents analyzing: module architecture, pricing, reporting internals, gap analysis, user journeys, feature prioritization, and executive synthesis.
> Date: 2026-02-08

---

## Section 1: Complete Module Architecture

Meltwater has **10 top-level modules** accessible from the left sidebar. The screenshot walkthroughs above covered Explore (Volume, Narrative, Sentiment tabs), Analyze, and Report in detail. This section documents the remaining modules.

### 1.1 Monitor Module — Daily Consumption Feed

**What it is:** A personalized, curated feed of articles matching saved searches. Think "Google Reader for media monitoring." While Explore is for deep analysis, Monitor is for daily reading and triage.

**Key capabilities:**
- Chronological feed of matched articles with sentiment badges, source/author, reach, and entity tags
- Per-article actions: tag, share internally, add to newsletter, add to report, post to social (X, Facebook, LinkedIn)
- Email digest delivery: automated daily/weekly summaries sent to team members or stakeholders without Meltwater login
- Filter by saved search, sentiment, source type, date range
- "Quick newsletter" — select articles from feed, one-click create newsletter

**ICP value:** The daily workhorse for PR teams. Monitor is where 60-70% of daily time is spent — scanning, triaging, tagging articles, and sharing relevant coverage with stakeholders.

### 1.2 Media Relations Module — Journalist Database & Outreach

**What it is:** A full journalist/influencer database with 800,000+ contacts, integrated with email pitching and tracking.

**Key capabilities:**
- **Contact database:** 800K+ journalists and influencers with beat, outlet, contact info, social profiles, recent articles
- **Media lists:** Static (manually curated) and dynamic (auto-updating based on criteria like "journalists who cover EV in the US")
- **Author lists:** Track specific journalists across all their publications (reusable in Explore filters)
- **Email pitching:** Compose, personalize, and send pitches directly from the platform
- **Pitch tracking:** Open rates, click rates, reply rates per pitch and per journalist
- **Journalist profiles:** Activity history, coverage patterns, social engagement metrics

**Competitive context:** Smaller than Cision's database (their primary moat) but integrated with monitoring. Muck Rack's journalist self-updated profiles are considered higher quality.

### 1.3 Newsletters Module — Media Briefing Distribution

**What it is:** Curated newsletter creation and distribution for stakeholder briefings.

**Key capabilities:**
- **Two modes:** Manual curation (drag-and-drop article selection) and dynamic auto-population from saved searches
- **Branded templates:** Company logo, colors, header/footer customization, section-based layout
- **Distribution:** Email to managed recipient lists, web link (shareable URL, no login needed), PDF export
- **Scheduling:** Daily/weekly/monthly automated delivery
- **Analytics:** Open rate, click rate, per-article click tracking, per-recipient engagement
- **Audience management:** Internal + external recipients, subscriber management, unsubscribe handling

**ICP value:** The #1 use case: "Send our CEO a daily media briefing." Agencies use branded newsletters for client-facing briefings. Auto-populated newsletters from saved searches save hours per week.

### 1.4 Alerts Module — 6+ Alert Types with AI-Powered Smart Alerts

**Alert types:**

| Type | Trigger | Example |
|---|---|---|
| **Mention Alert** | New article matches a saved search | "Brand mentioned in Reuters" |
| **Top Reach Alert** | High-reach outlet publishes matching content | "Only alert if outlet reach > 1M" |
| **Sentiment Shift Alert** (Smart) | AI detects significant sentiment change vs. baseline | "Negative sentiment increased 20% vs. 30-day average" |
| **Volume Spike Alert** (Smart) | AI detects statistically significant mention spike | "Mentions exceeded 3x the 30-day average" |
| **Journalist/Author Alert** | Specific journalist publishes new article | "WSJ reporter covering our industry published" |
| **Competitive Alert** | Competitor's metrics exceed yours | "Competitor X mention volume exceeded ours for 3 days" |

**Delivery channels:** Email, Meltwater web (in-app bell), mobile push (iOS/Android), Slack, Microsoft Teams, Webhooks/API

**Smart Alerts are the differentiator.** They analyze rolling baselines (7/30/90 day) and include AI-generated explanations: "Mentions spiked 4x due to [event] covered by [outlets] in [region]."

### 1.5 Content Module — Configuration Hub

**What it is:** The administrative backbone managing content ingestion. Not a content creation tool — it's source and taxonomy configuration.

**Key components:**
- **Search management:** View/edit all saved searches, see which modules each search feeds
- **Tags:** User-defined labels on articles (e.g., "Crisis", "Product Launch"). Support auto-tagging rules
- **Labels:** Organizational folders for grouping searches (e.g., "Client A > Brand > Sub-brand")
- **Custom categories:** User-defined classification taxonomies visible as filter dimensions across Explore
- **RSS feeds:** Add custom RSS sources not in Meltwater's default library
- **Manual URLs:** Paste article URLs to manually add missed content to the index
- **Source lists:** Create groups of publications (e.g., "Tier 1 Sources") usable as filters everywhere

### 1.6 Explore — Engagement Tab (4th Analysis Tab)

The Engagement tab answers: "How much interaction is coverage generating? What's going viral?"

**Core widgets:**
- Total Engagement metric (likes + shares + comments aggregate)
- Engagement trend over time (with spike detection)
- Engagement by source type (X vs. Facebook vs. Reddit vs. News shares)
- Top engaging content (ranked by total interaction — surfaces viral content)
- Engagement by sentiment (negative content often generates disproportionate engagement)
- Top authors by engagement (influential voices, not just prolific ones)
- Engagement-to-reach ratio (normalized impact: small outlet with high engagement > large outlet with low engagement)

### Cross-Module Architecture Map

```
Content (Configuration Layer)
  ├── Searches (Boolean queries) ──────→ FEEDS INTO EVERYTHING
  ├── Tags, Labels, Custom Categories ──→ Classification system used everywhere
  ├── RSS Feeds, Manual URLs ──────────→ Augments content ingestion
  └── Source Lists ────────────────────→ Filter dimension in Explore/Monitor

Explore (Analysis Layer)
  ├── Volume Tab ──────→ Mention trends, source breakdown, locations
  ├── Narrative Tab ───→ AI topic clusters, theme discovery
  ├── Sentiment Tab ───→ Pos/neg distribution, sentiment by source
  └── Engagement Tab ──→ Social interaction metrics, viral content

Monitor (Consumption Layer) ──→ Daily reading/triage + email digests
Media Relations (Outreach) ───→ 800K+ contacts + pitching + tracking
Newsletters (Distribution) ──→ Curated briefings + auto-newsletters
Alerts (Notification) ────────→ 6+ alert types + Smart AI alerts
Analyze (Comparison) ─────────→ Share of Voice dashboards
Report (Output) ──────────────→ Digest / Dashboard / Insight Reports
```

---

## Section 2: Pricing Deep Dive

### Meltwater's Pricing Structure

Meltwater has **no public pricing**. All pricing requires consultative sales (demo → tailored quote). The structure is **module-based, not strictly tiered**.

### Inferred Tier Structure

| Tier | Annual Price Range | Target Buyer | What's Included |
|---|---|---|---|
| **Basic / Essentials** | ~$8K-$15K/yr | Small business, single team | Core monitoring (Explore + Monitor + Alerts), basic analytics, 1-3 users |
| **Professional / Suite** | ~$15K-$40K/yr | Mid-market PR teams | Full monitoring + Analyze + Report + Media Relations, 3-10 users, AI Search Assistant |
| **Enterprise / Full Suite** | ~$40K-$100K+/yr | Large enterprises | All modules + Social Listening + Consumer Insights + API + GenAI Lens, 10+ users, dedicated CSM |
| **Global Enterprise** | ~$100K-$250K+/yr | Fortune 500, multi-market | Full suite, multiple regions, custom SLAs, highest data volumes |

**Average Revenue Per Customer:** ~$18,500/year (derived from Oslo Stock Exchange filings: ~$500M revenue / 27K customers)

### User-Reported Price Data

| Source | Price Mentioned | Context |
|---|---|---|
| Reddit r/PublicRelations | "$24,000/year" | "Google Alerts with a nicer UI" |
| Reddit r/PublicRelations | "$4,000/month" ($48K/yr) | Compared to $1,500/month for Brand24 + Muck Rack combo |
| G2 Review (Enterprise) | "$50K+/year" | Criticizing support quality vs. price |
| Reddit user | -- | "I wish someone would build a monitoring tool that costs $200-500/month" |

### Feature Gating Matrix

| Feature | Basic ($8-15K) | Professional ($15-40K) | Enterprise ($40-100K+) |
|---|---|---|---|
| Core Monitoring (Explore/Monitor) | Yes | Yes | Yes |
| AI Search Assistant | Yes | Yes | Yes |
| Alerts (email) | Yes | Yes | Yes |
| Sentiment Analysis | Basic | Full | Full |
| Narrative Clustering | No | Yes | Yes |
| Spike Analysis (AI) | Limited | Yes | Yes |
| Insight Reports (AI) | No | Yes (limited) | Yes (unlimited) |
| Media Relations Module | No | Yes | Yes |
| Social Listening (Deep) | No | Add-on | Yes |
| API/Data Export (JSON) | No | No | Yes |
| GenAI Lens | No | No | Yes/Add-on |
| Number of Users | 1-3 | 3-10 | 10+ |

### Contract Structure

- **Annual contracts mandatory** — no monthly option
- **Multi-year deals pushed aggressively** (2-year contracts for 15-30% discounts)
- **Auto-renewal clauses** with 30-60 day cancellation windows (buried in contracts)
- **Price increases at renewal: 5-15% standard, 20-50% reported** — the #1 customer complaint (65% of negative reviews)

### Competitor Price Comparison

| Vendor | Entry Price | Mid-Range | Pricing Model |
|---|---|---|---|
| **Meltwater** | ~$8K-$15K/yr | ~$15K-$40K/yr | Opaque, annual |
| **Cision** | ~$6K-$12K/yr | ~$20K-$50K/yr | Opaque, annual |
| **Muck Rack** | ~$5K/yr | ~$9K-$15K/yr | Quote-based, annual |
| **Brand24** | $948/yr ($79/mo) | $2,388/yr ($199/mo) | **Public, monthly option** |
| **Mention** | $588/yr ($49/mo) | $2,148/yr ($179/mo) | Semi-public, monthly |

**Key insight for AlmaLabs:** Transparent pricing at $49-$199/month directly addresses the #1 industry frustration. Every buyer researching alternatives after a Meltwater renewal shock is a conversion opportunity.

---

## Section 3: Reporting Internals

### Three Report Types

**1. Digest Reports** — Automated daily/weekly/monthly email summaries
- Mention counts with period-over-period comparison
- Top articles by reach with source, headline, sentiment
- AI-generated insight summary ("what happened")
- Source type and sentiment breakdowns
- Configurable cadence and delivery

**2. Dashboard Reports** — Exports of Analyze module dashboards
- Share of Voice widgets (Mentions, Engagement, Editorial Reach)
- Source type breakdown, Top Organizations
- PDF, CSV, JSON/API export formats
- Live shareable links (interactive, auto-refreshed)

**3. Insight Reports** — AI-powered executive summaries
- Cover images (presentation-ready for C-suite)
- AI-generated narrative sections (volume drivers, sentiment themes)
- Data visualizations pulled from Analyze widgets
- Multi-author collaboration (team-based creation)
- Schedulable for automated recurring delivery
- Quarterly cadence aligns with PR reporting rhythms

### Distribution Channels

Email (scheduled + real-time) | Live shareable links | PDF download | CSV export | API/JSON (Tableau, PowerBI) | Mobile push | Slack + Microsoft Teams | Social posting per-article

### Known Reporting Weaknesses (from 1,100+ reviews)

- **~30% of negative reviews cite reporting limitations** across ALL platforms
- *"CSV exports are poorly formatted and PDF reports look like they're from 2010"* — G2
- *"We can't customize reports the way our C-suite wants. We rebuild in PowerPoint."* — Capterra
- *"I spend 4 hours every Friday rebuilding Meltwater data into PowerPoint. That's criminal for a $50K/year tool."* — G2
- Non-licensed stakeholder access restricted (seat-based licensing limits who sees reports)

**Opportunity for AlmaLabs:** Auto-generated, truly C-suite-ready reports that don't require PowerPoint rebuilding would be a significant differentiator at every price tier.

---

## Section 4: AlmaLabs vs. Meltwater — Feature Gap Analysis

### 33 features across 14 categories. Severity rated Critical / High / Medium / Low.

### Critical Gaps (Must close for MVP)

| # | Gap | Meltwater Has | AlmaLabs Has | Build Effort |
|---|---|---|---|---|
| 1 | **NER Pipeline** | Full entity extraction (persons, companies, locations) | String matching only (~50-60% accuracy) | 8-10 weeks (spaCy) |
| 2 | **Article-Level Sentiment** | 3-class with 240+ language support | None | 4-8 weeks (RoBERTa) |
| 3 | **Deduplication** | Story clustering for syndicated content | None (1 AP story = 50 separate alerts) | 3-4 weeks (SimHash) |
| 4 | **User-Facing Search** | Keyword + Boolean + AI Search Assistant | No user-facing search creation | 7-10 weeks |
| 5 | **Dashboard** | Configurable widgets, interactive drill-down | None — alerts as posts only | 8-12 weeks (React) |
| 6 | **Content Licensing** | Factiva, 270K+ sources, X firehose | 20K-50K scraped sources, no licenses | 4-6 weeks integration + $138K-$355K/yr |

**Total Critical MVP Build:** ~37-54 engineering weeks (4-6 months with 4-5 engineers)

### High-Priority Gaps (Competitive tier — Months 7-18)

| # | Gap | Build Effort |
|---|---|---|
| 7 | Entity-Level Sentiment | 4-6 weeks |
| 8 | AI-Powered Insights (LLM summaries) | 4-6 weeks |
| 9 | Spike Detection & Analysis | 6-8 weeks |
| 10 | Share of Voice Analytics | 4-6 weeks |
| 11 | Per-Article Reach Data | 3-4 weeks |
| 12 | Team Collaboration | 4-6 weeks |
| 13 | Report Generation (Digest + PDF) | 6-8 weeks |
| 14 | Alert Rule Engine (sentiment shift, spike) | 3-4 weeks |
| 15 | Country-Level Location Filtering | 3-4 weeks |
| 16 | AI Search Assistant | 4-6 weeks |
| 17 | Twitter/X Integration | 8-12 weeks + $60K/yr API |
| 18 | Historical Archives (via licensing) | 6-8 weeks + licensing |
| 19 | Competitive Benchmarking Dashboards | 4-6 weeks |

### Medium/Low Gaps (Enterprise tier — Month 18+)

Broadcast monitoring (Partner TVEyes) | Narrative clusters | Platform Assistant | Social posting | Mobile app | Podcast monitoring | GenAI Lens | Image/Logo recognition | Print media | Predictive analytics | Media contact database (Defer — separate product)

### Key Strategic Takeaway

> "The 50% reuse claim is accurate but misleading. AlmaLabs has crawling infrastructure and a delivery pipeline, but the entire intelligence layer (NER, sentiment, dedup, analytics, dashboards) must be built from scratch. The '50% we already have' covers plumbing; the '50% we need' covers the entire product experience."

---

## Section 5: ICP User Journey Maps (5 Journeys)

### Journey 1: Morning Media Briefing (Daily, 15-30 min)

**Persona:** Priya, Communications Analyst (daily user)

| Step | Module | Action |
|---|---|---|
| 1 | Home | Check alert count (179 unread), scan Top Reach alerts |
| 2 | Alerts Panel | Triage by reach — MSN.com (122M) first, local blogs last |
| 3 | Explore > Volume | Check mentions trend, period-over-period comparison |
| 4 | Explore > Sentiment | Quick sentiment check — any negative shift? |
| 5 | Monitor | Scan curated feed, tag relevant articles |
| 6 | Newsletters | Add articles to automated daily briefing for CEO |

**Key friction:** Alert overload (179 unread = noise). No single "morning briefing" screen — requires navigating 3-4 modules.

### Journey 2: Crisis Response (Ad-hoc, 1-4 hours)

**Persona:** Sarah, PR Director + David, VP Communications

| Step | Module | Action |
|---|---|---|
| 1 | Alerts | Sentiment Shift or Volume Spike smart alert fires |
| 2 | Explore > Volume | Spike Analysis: what happened, why, where, who |
| 3 | Explore > Sentiment | AI summary of positive vs. negative drivers |
| 4 | Explore > Narrative | AI clusters: what are the story angles? |
| 5 | Media Relations | Find journalists covering the crisis for proactive outreach |
| 6 | Alerts | Set additional sentiment shift alerts for early warning |

**Key friction:** No unified "crisis mode" view. Must navigate 4 separate analysis tabs. Media Relations is a separate module from Explore (no inline journalist info).

### Journey 3: Monthly/Quarterly Reporting (2-4 hours)

**Persona:** Priya builds; Sarah reviews; CMO receives

| Step | Module | Action |
|---|---|---|
| 1 | Analyze | Open competitive dashboard, set date range |
| 2 | Analyze | Review Share of Voice (Mentions, Engagement, Reach) |
| 3 | Explore > Sentiment | Pull per-search sentiment trends |
| 4 | Explore > Narrative | Capture top theme clusters |
| 5 | Explore > Volume | Top Locations + Top Editorial Sources |
| 6 | Report | Create Insight Report (AI-generated executive summary) |
| 7 | Report | Customize, add cover image, schedule delivery |
| 8 | **Manual** | **Rebuild key charts in PowerPoint** (common pain point) |

**Key friction:** Analyze and Explore are separate modules with different views. PowerPoint rebuild step costs 15-30+ minutes per report.

### Journey 4: New Brand/Topic Setup (30-60 min, one-time)

**Steps:** AI Search Assistant → save search → label organization → create sub-topic searches → configure alerts (real-time + sentiment shift + digest) → add to Analyze dashboard → configure Content module (RSS feeds, custom categories)

**Key friction:** Creating 5-10 searches for one brand is tedious (no batch create). Alert, dashboard, and content configuration span 3 separate modules with no guided setup wizard.

### Journey 5: Competitive Benchmarking (Weekly 30 min, Quarterly 1-2 hours)

**Steps:** Analyze dashboard (SoV by Mentions/Engagement/Reach/Source Type) → Per-competitor Explore deep-dives (Sentiment, Narrative, Top Sources) → Comparisons tab → Build competitive Insight Report

**Key friction:** Per-competitor deep dives require sequential Explore sessions (4 competitors × 3 tabs = 12 separate views). No competitive sentiment comparison widget on one screen. SoV can be inflated by wire/syndication sources.

### Cross-Journey Module Usage

| Module | Morning | Crisis | Reporting | Setup | Competitive |
|---|---|---|---|---|---|
| Home | Entry | — | — | — | — |
| Explore | Primary | Primary | Data gathering | Primary | Deep-dive |
| Monitor | Optional | — | — | — | — |
| Analyze | — | — | Primary | Dashboard setup | Primary |
| Media Relations | — | Journalist lookup | — | — | — |
| Report | — | — | Report building | — | Report building |
| Alerts | Triage | Create/monitor | — | Configuration | — |
| Content | — | — | — | RSS/URL config | — |

**Architectural observation:** Every journey except the simplest requires navigating **3-5 separate modules**. Power comes from depth within each module; friction comes from fragmentation across modules.

---

## Section 6: Feature Prioritization Matrix (4-Tier Build Order)

### Tier 1: Table Stakes — Beat Google Alerts (Months 1-6, $49-$199/mo)

| # | Feature | Build Effort | Why Table Stakes |
|---|---|---|---|
| 1.1 | Keyword Search + Saved Searches | 7-10 weeks | Core product — type brand name, see mentions |
| 1.2 | Sentiment Analysis (article-level, 3-class) | 4-8 weeks | 31.7% of users' first question: "is coverage positive or negative?" |
| 1.3 | Mentions Volume Trend + Spike Detection | 4-6 weeks | The first chart every buyer expects |
| 1.4 | NER-Based Entity Matching | 8-10 weeks | Replaces string matching, eliminates false positives |
| 1.5 | Deduplication (SimHash) | 3-4 weeks | Without this, 1 story = 50 alerts. Destroys trust |
| 1.6 | Real-Time Email Alerts (with reach context) | 3-4 weeks | PR teams need immediate notification |
| 1.7 | Per-Article Reach Estimation | 2-3 weeks | Triage by impact — 125M-reach outlet vs. 5K-reach blog |
| 1.8 | Fixed Dashboard (5 widgets) | 4-6 weeks | Volume trend, sentiment donut, top sources, locations, recent mentions |
| 1.9 | CSV/PDF Export | 1-2 weeks | Share results with bosses — non-negotiable |
| 1.10 | Source/Country Breakdown | 2-3 weeks | "Where is the conversation happening?" |

**Total Tier 1:** ~30-42 engineering weeks | **Price point enabled:** $49-$199/month

### Tier 2: Differentiators — Beat Brand24/Mention (Months 3-9)

| # | Feature | Build Effort | Why Differentiator |
|---|---|---|---|
| 2.1 | LLM-Powered Result Validation | 3-4 weeks | Every result verified for relevance — eliminates noise problem |
| 2.2 | AI-Generated Daily Briefing | 3-4 weeks | Auto-generated 3-paragraph briefing at 8 AM — no login needed |
| 2.3 | Spike Alerts with AI Explanation | 4-6 weeks | Alert itself contains the insight — no click-through for triage |
| 2.4 | Natural Language Search (no Boolean ever) | 4-6 weeks | 5-minute setup vs. weeks of Boolean training |
| 2.5 | Hindi NLP (MuRIL/IndicBERT) | 4-6 weeks | India-first differentiation — Meltwater is weak on Indian languages |
| 2.6 | Customizable Dashboard | 5-6 weeks | Widget selection, date range, drill-down |
| 2.7 | Slack/Teams Alerts | 2-3 weeks | Meet PR teams in their workflow tools |
| 2.8 | Share of Voice (Mentions) | 4-6 weeks | The #1 PR metric — "are we talked about more than competitors?" |
| 2.9 | Branded Report Generation (PDF) | 4-6 weeks | C-suite-ready reports without PowerPoint rebuild |
| 2.10 | Multi-User Seats (3-5) | 3-4 weeks | Team-based monitoring with shared searches |

**Total Tier 2:** ~34-43 engineering weeks | **Price point enabled:** $100-$199/month

### Tier 3: Competitive Parity — Match Lower Meltwater (Year 2)

Key features: Full social listening (FB, IG, YT, TikTok) | Entity-level sentiment | Broadcast monitoring (TVEyes partner) | Podcast monitoring | Advanced dashboard + share links | Paywalled content (LexisNexis partner) | Multi-language support (5-10 languages) | API access | Sentiment trend + sentiment by source

**Total Tier 3:** ~53-70 engineering weeks | **Price point enabled:** $200-$500/month

### Tier 4: Enterprise Only (Year 3+)

Key features: 10+ year historical archives (Factiva partner) | GenAI Lens | Image/logo recognition | Press release distribution (partner) | SSO/SAML | SOC2 Type II | Print media (partner) | CRM integration | Full agency workspace + white-label | Earned/owned/paid unified dashboards

**Total Tier 4:** Partner-heavy, ~60-90 engineering weeks | **Price point enabled:** $500+/month

### Summary

| Tier | Focus | Timeline | Total Build | Key Evidence |
|---|---|---|---|---|
| **Tier 1** | Beat Google Alerts | Months 1-6 | ~30-42 weeks | Top 5 Google Alerts upgrade triggers |
| **Tier 2** | Beat Brand24/Mention | Months 3-9 | ~34-43 weeks | "AI that actually works" demand signal |
| **Tier 3** | Match lower Meltwater | Year 2 | ~53-70 weeks | RFP Tier 2 requirements |
| **Tier 4** | Match full Meltwater | Year 3+ | ~60-90 weeks | Enterprise procurement gates |

---

## Section 7: Executive Strategic Synthesis

### Meltwater's 5 Most Defensible Features (Hardest to Replicate)

**1. Data Scale & Historical Archives (10+ years news, 15 months social)**
- 200B+ documents indexed, 500M+ new pieces daily, 270K+ sources
- **Cannot be replicated.** License what you can (PTI, NewsAPI), build forward, position as "accuracy over volume"

**2. Twitter/X Full Firehose Access (Official Data Reseller)**
- Post-Musk: $504K-$1.2M+/year for Enterprise API, and that's still not firehose
- **Defer to Phase 2.** Use Reddit + forums + news as social proxies at launch

**3. Global Source Network (55 offices, 125+ countries)**
- Regional print/broadcast via partners, 25K+ podcast transcriptions, Chinese social platforms
- **Do not attempt global coverage at launch.** India-first with 20K-50K digital news sources

**4. Entity-Level Sentiment (Per-Entity, Per-Article, 240+ Languages)**
- "How was *our brand* portrayed in this article?" — not just article positive/negative
- **Leapfrog opportunity.** LLM-powered entity sentiment at 85-92% accuracy achievable within 6 months for English + Hindi

**5. Factiva/Dow Jones Licensed Paywalled Content**
- WSJ, FT, and premium outlets that free tools cannot access
- **Pursue LexisNexis DaaS in Phase 2** after 80+ customers demonstrate traction

### Meltwater's 3 Biggest Exploitable Weaknesses

**1. Complexity and Learning Curve — "The Onboarding Tax"**
- Every module has "Start training" CTA. 7+ onboarding wizard steps. 10 top-level modules. Boolean syntax training required.
- 45% of negative reviews cite UX/interface problems
- **Exploit:** Build product where first brand monitor is set up in <5 minutes with zero training. "You don't need a training program to monitor your brand."

**2. Pricing Opacity and Contract Lock-In — "The Trust Deficit"**
- No public pricing. Annual lock-in. Auto-renewal traps. 20-50% price hikes at renewal.
- 65% of negative reviews cite pricing/contract issues
- **Exploit:** Publish pricing. Monthly contracts. No auto-renewal. Price-lock guarantee.

**3. Noise and False Positives — "The Accuracy Gap"**
- Screenshot evidence: Narrative clusters include irrelevant "Autoimmune Disease Testing" in an EV search
- 55% of negative reviews cite data accuracy issues
- **Exploit:** LLM-validate every result for relevance post-retrieval. $0.001-$0.01/article. "Every result is verified. No noise."

### Minimum Feature Set for First 100 Customers

| Feature | Why Required | Build Effort |
|---|---|---|
| Keyword/brand search with instant results | Core product | 4-6 weeks |
| Sentiment analysis (article-level) | Table stakes question #1 | 4-8 weeks |
| Mentions volume trend | First chart every buyer expects | 2-3 weeks |
| Source and country breakdown | Basic segmentation | 2-3 weeks |
| Real-time email alerts with reach context | Immediate notification of high-impact coverage | 3-4 weeks |
| Per-article reach estimation | Triage by impact | 2-3 weeks |
| Deduplication | Without this, volume metrics are garbage | 3-4 weeks |
| NER-based brand matching | Eliminates false positives | 8-12 weeks |
| Simple dashboard (5 widgets) | Visual analytics | 4-6 weeks |
| CSV/PDF export | Share results with bosses | 1-2 weeks |

**Total:** 5-6 months with 3 engineers (product), 1 (NLP), 1 (infrastructure)

**Deliberately excluded from MVP:** Social media, broadcast/print, Boolean builder, journalist database, newsletters, SoV dashboards, mobile app, Slack/Teams

### What AlmaLabs Should Never Build

1. **Media contact database / journalist pitching** — Partner with CRM/outreach tools (HubSpot, Prowly). Cision's moat; negative ROI to replicate.
2. **Press release distribution** — Dominated by PR Newswire/GlobeNewswire. Shrinking market. Distraction.
3. **Broadcast TV/Radio monitoring (in-house)** — Partner with TVEyes when enterprise customers demand it.
4. **GenAI Lens** — Novel but niche. Monitor market traction before investing.
5. **240+ language sentiment** — Build high-accuracy for English + Hindi. Add languages only when entering those markets.

### The AI Advantage — Where AlmaLabs Can Leapfrog

**Opportunity 1: AI-First Result Validation (The Noise Killer)**
Run every matched article through an LLM relevance check. Meltwater can't retrofit this at 500M+ pieces/day. AlmaLabs at 50K-500K/day can afford $0.001-$0.01/article.

**Opportunity 2: Natural Language Everything (No Boolean, Ever)**
Eliminate Boolean entirely. User types plain English; AI handles query construction. Fundamentally different architecture vs. legacy Boolean + AI helper overlay.

**Opportunity 3: Automated Daily Briefing (The Report That Writes Itself)**
Auto-generated 3-paragraph briefing delivered at 8 AM: "Here's what happened yesterday with [brand]. Coverage up 15%. Dominant story: [X]. Sentiment: 72% positive. One negative article from [outlet] warrants attention." No login required.

**Opportunity 4: Spike Alerts with Full Explanation**
Not "you have 179 unread alerts" — instead: "Coverage spiked 4x in last 3 hours. Driven by [event]. 87% positive. Highest-reach article from [outlet] (12M reach). Here's the 2-sentence summary." The alert IS the insight.

### The Positioning Framework

Per CEO directive: position as "Media Monitoring," not "AI Media Intelligence." But build every AI advantage into the product. Users experience AI-powered accuracy, AI-generated briefings, AI-explained spikes — but marketing says "Media Monitoring that actually works." The AI is invisible infrastructure, not the brand promise.

### Bottom Line

> Meltwater's real moats are data scale, licensed content, and global partnerships — not technology. Their AI features are competent but not exceptional. AlmaLabs' path is to build a product that is **10x simpler, 5x cheaper**, and uses LLMs to deliver accuracy that Meltwater's legacy NLP stack cannot match — starting in India where Meltwater's advantages are weakest and AlmaLabs' advantages (local knowledge, existing client base, cost structure) are strongest. The first 100 customers will not be won on features; they will be won on **simplicity, transparency, and accuracy**.
