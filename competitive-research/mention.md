# Mention — Competitor Deep Dive

> Source: AlmaLabs competitive landscape research

---

## Company Profile

| Field | Detail |
|---|---|
| Founded | 2012 |
| HQ | Paris, France (with presence in New York) |
| Founders | Matthieu Vaxelaire (original CEO) |
| Funding | ~$2.2M total raised (lean startup, bootstrapped growth after initial seed) |
| Ownership | Acquired by **Mynewsdesk** (2022), which is owned by **NHST Media Group** (Norwegian media company). Part of a broader PR/media tech portfolio alongside Mynewsdesk |
| Employees | ~50-80 (estimated) |
| Customers | 750,000+ users have tried the platform (claimed); ~4,000-5,000 active paying customers (estimated) |
| Positioning | **Mid-market media monitoring and social listening** — simple, accessible, well-designed |
| Free trial | **14-day free trial** available |
| Tagline | "Stay on top of your online presence" / "Media monitoring made simple" |

---

## Product: Media Monitoring & Social Listening

### Core Capabilities
- **Real-time media monitoring** across web and social channels
- **Social listening**: Track brand mentions, competitor activity, and industry keywords across social platforms
- **Alert system**: Configurable real-time notifications
- **Feed-based interface**: Chronological stream of mentions with filters
- **Boolean query support**: Advanced search operators for precise monitoring
- **Collaboration tools**: Assign mentions to team members, tag/categorize, internal notes
- Designed to be **simple enough for a marketing intern but powerful enough for a CMO**

### Coverage Breadth
- **Social media**: Twitter/X, Facebook (public pages/posts), Instagram, YouTube, Reddit, Pinterest, TikTok
- **Online news**: Web news crawling (broad global coverage)
- **Blogs**: Major blog platforms and independent blogs
- **Forums**: Discussion boards and community sites
- **Review sites**: Some coverage (less comprehensive than Brand24)
- **NOT covered well**: Paywalled/premium news (no LexisNexis/Factiva), print media, broadcast TV/radio, podcasts (very limited)

### Analytics Suite
- **Sentiment analysis**: Automatic positive/negative/neutral classification
- **Volume trends**: Mention count over time with interactive charts
- **Reach estimation**: Estimated audience reach of mentions
- **Top sources**: Ranking of sources by volume and influence
- **Influencer identification**: Identifies key voices/authors driving conversations
- **Geographic distribution**: Where mentions are coming from
- **Language breakdown**: Mentions by language
- **Competitive analysis**: Compare brand vs. competitors side-by-side
- **Share of voice**: Percentage comparison across tracked terms
- **Tag-based analysis**: Custom tags for categorizing mentions, then analyze by tag
- Analytics are **functional but not deep** — sufficient for mid-market, insufficient for enterprise

### Dashboards & Reporting
- **Clean, modern dashboard** with real-time data
- Pre-built views: overview, feed, analytics, influencers
- Customizable date ranges and filters
- **Automated reports**: Scheduled email reports (daily/weekly/monthly)
- **Export**: CSV and Excel export
- **No PowerPoint/PDF generation** (limitation vs Meltwater/Cision)
- Dashboard design is clean and praised in reviews
- **Publish feature**: Create branded, shareable report pages (web link)
- Limited data visualization options compared to enterprise tools

### Alerts & Delivery
- **Real-time email alerts**: Instant notification when new mentions match criteria
- Configurable alert frequency (real-time, hourly, daily digest)
- **Slack integration**: Route alerts to Slack channels
- **Zapier integration**: Connect Mention to 5,000+ apps (including MS Teams, Trello, HubSpot, etc.)
- **In-app notifications**
- **Mobile app** (iOS and Android)
- Filter alerts by sentiment, source, language
- Spike detection available (alerts on unusual volume)

### Social Publishing (Added Feature)
- **Social media publishing**: Schedule and publish posts to social platforms directly from Mention
- Content calendar view
- Multi-platform posting (Facebook, Twitter/X, Instagram, LinkedIn)
- **This is unique** — Mention bundles monitoring + publishing, unlike most monitoring-only tools
- Competes with Hootsuite/Buffer on the publishing side
- Useful for small teams that want one tool for both listening and publishing

### API
- **REST API** available on Company and Enterprise plans
- Access to mentions, analytics data, alerts
- Used for integration with CRM, BI tools, custom dashboards
- Rate-limited based on plan
- Public API documentation available
- Webhook support for real-time data push

---

## Technology & Operations

### Infrastructure
- Cloud-based SaaS (likely AWS based on Paris tech ecosystem)
- Modern web application (React-based frontend, estimated from job listings)
- Real-time data processing pipeline
- NLP for sentiment analysis (likely combination of proprietary + open-source models)
- After Mynewsdesk acquisition, some infrastructure consolidation likely

### Data Sourcing

| Source Type | Method |
|---|---|
| Social media | **Platform APIs**: Twitter/X (standard API), Facebook Graph API, Instagram API, YouTube Data API, Reddit API, Pinterest, TikTok |
| Online news | **Proprietary web crawlers** + RSS feeds (broad but not as deep as Meltwater's 270K sources) |
| Blogs | **Web crawlers** scanning major blog platforms |
| Forums | **Crawlers** for popular forums and discussion boards |
| Review sites | Limited crawling of some review platforms |
| Paywalled/premium news | **NOT covered** — no content licensing partnerships |
| Print media | **NOT covered** |
| Broadcast TV/Radio | **NOT covered** |
| Podcasts | **Minimal** — some coverage via RSS/crawling of podcast show notes, not transcription |

### Post-Acquisition Synergies (Mynewsdesk)
- **Mynewsdesk** brings: press release distribution capability, media contacts database (Nordic/European focus), newsroom hosting
- Potential for bundled offering: monitoring (Mention) + distribution (Mynewsdesk) + newsroom (Mynewsdesk)
- Integration depth unclear as of last assessment
- NHST Media Group ownership provides media industry connections in Nordics

---

## Pricing & Go-to-Market

### Pricing (PUBLIC — from mention.com/en/pricing)

| Plan | Monthly Price (billed annually) | Monthly Price (billed monthly) | Key Features |
|---|---|---|---|
| **Solo** | $41/mo | $49/mo | 2 alerts (tracked terms), 5K mentions/mo, 1 user, basic monitoring, no social publishing |
| **Pro** | $83/mo | $99/mo | 5 alerts, 10K mentions/mo, 10 users, sentiment analysis, Boolean queries, competitive reports |
| **ProPlus** | $149/mo | $179/mo | 7 alerts, 20K mentions/mo, unlimited users, advanced analytics, social publishing, API access, Slack integration |
| **Company** | Custom pricing | Custom pricing | Unlimited alerts and mentions, custom integrations, dedicated account manager, API, priority support, custom onboarding |

- **14-day free trial** on all self-serve plans
- **Annual billing saves ~15-20%**
- All plans include: mention feed, alerts, basic analytics, mobile app
- **Social publishing** only on ProPlus and above
- **API access** on ProPlus and Company plans
- **Boolean queries** on Pro and above

### Pricing Analysis
- Entry point ($41/mo = ~$490/year) is even lower than Brand24 ($79/mo)
- Mid-range ($83-$149/mo) is competitive with Brand24
- Company plan bridges to enterprise with custom pricing
- Dramatically cheaper than Meltwater (~$10K+), Cision (~$6K+), Muck Rack (~$5K+)
- **Social publishing bundled** at no extra cost is unique value at this price point
- Mention limits (5K-20K) are lower than Brand24's limits at comparable prices

### Go-to-Market Strategy
- **Product-led growth**: Free trial drives adoption, self-serve purchase
- **Content marketing**: Strong blog with SEO-optimized content (ranks for monitoring/listening keywords)
- **Freemium adjacent**: Free trial is the main acquisition channel
- **Review sites**: Active presence on G2, Capterra, TrustRadius
- **Webinars and educational content**: How-to guides for social listening
- **Partner ecosystem**: Zapier integrations extend reach
- **Mynewsdesk cross-sell**: Potential to bundle with Mynewsdesk for European clients
- **Localized**: French origin gives European language/market advantage
- **No aggressive enterprise sales team** — limited ability to close six-figure deals
- **Agency partner program**: Some agencies resell or recommend Mention

### Customer Segmentation
- **Primary**: Small-to-mid businesses (10-500 employees), marketing teams, digital agencies
- **Secondary**: Freelancers, social media managers, PR practitioners, startup founders
- **Industries**: Marketing agencies, SaaS companies, e-commerce, hospitality, education
- **Geography**: Strong in Europe (France, DACH, Nordics via Mynewsdesk), growing in North America
- **NOT targeting**: Large enterprises, government, Fortune 500 (too limited for their needs)
- **Buyer persona**: Marketing manager, social media manager, digital marketing director, small agency owner

---

## Notable Clients
- **Microsoft** — project-level monitoring
- **Asos** — fashion/e-commerce brand monitoring
- **Airbus** — selective monitoring use cases
- **Le Monde** — media company monitoring
- **Deliveroo** — brand/reputation tracking
- **Intercom** — SaaS brand monitoring
- **WPP agencies** — some agency offices use Mention
- **Trello** — (before Atlassian acquisition)
- Many European mid-market companies
- Primarily mid-market and startup references

---

## Strengths
- **Very affordable entry point** ($41/mo) — accessible to solo practitioners and tiny teams
- **Clean, intuitive UX** — praised in reviews for simplicity and ease of use; one of the best-designed tools in the category
- **Social media publishing bundled** — unique at this price point; small teams can monitor and publish from one tool
- **Strong European presence** — French origin + Mynewsdesk (Nordic) gives European language and market advantage
- **Zapier integration** — connects to 5,000+ apps, compensating for limited native integrations
- **Mobile app** (iOS/Android) — real-time monitoring on the go
- **Boolean query support** — more precise than simple keyword matching
- **Good collaboration features** — assign mentions, tag, categorize — useful for team workflows
- **Mention feed UX** — clean, readable, easy to triage mentions
- **No sales call required** — transparent pricing and self-serve onboarding
- **Mynewsdesk synergies** — potential for integrated monitoring + distribution offering

## Weaknesses
- **No paywalled/premium news** — cannot monitor WSJ, FT, NYT, Reuters, or other premium publications
- **No print media monitoring**
- **No broadcast TV/radio monitoring**
- **Very limited podcast coverage**
- **Low mention volume caps** — 5K-20K/month on self-serve plans is restrictive for any brand with significant media presence
- **Low alert limits** — 2-7 tracked terms on self-serve plans; enterprise brands need dozens or hundreds
- **No media database or journalist outreach** — not a PR workflow tool
- **No press release distribution** (though Mynewsdesk parent offers this)
- **Basic analytics** — sentiment and volume are adequate but lack depth of Meltwater/Cision (no attribution, no React Score equivalent)
- **Limited historical data** — not competitive with enterprise tools' deep archives
- **Smaller data footprint** — crawlers cover fewer sources than enterprise competitors
- **Standard Twitter/X API** — not firehose, missing significant tweet volume
- **Export limitations** — no native PowerPoint/PDF report generation
- **Post-acquisition uncertainty** — Mynewsdesk acquisition may lead to product direction changes or reduced investment in standalone Mention product
- **Small engineering team** — slower feature development compared to well-funded competitors

---

## Comparison to Meltwater / Cision / Muck Rack

| Dimension | Mention | vs. Incumbents |
|---|---|---|
| **Pricing** | $41-$149/mo (public, self-serve) | 10-50x cheaper than enterprise tools |
| **Content breadth** | Social + online news + blogs/forums | Missing: paywalled news, print, broadcast, podcasts |
| **Social listening** | Adequate — major platforms covered | Behind Cision (Brandwatch) and Meltwater; comparable to Muck Rack's partial social |
| **Social publishing** | Included (schedule + publish) | Unique — none of the three offer publishing |
| **Analytics depth** | Basic (sentiment, volume, reach) | Far behind Meltwater and Cision |
| **PR workflow** | None — no database, pitching | Cannot replace any of the three as PR tool |
| **UX** | Clean, simple, well-designed | On par with Muck Rack; simpler than Meltwater/Cision (but also less powerful) |
| **Onboarding** | Minutes (self-serve, free trial) | Far faster than all three |
| **Scale** | Capped (5K-20K mentions/mo on self-serve) | Cannot match enterprise-scale needs |
| **Mobile** | iOS/Android app | On par with Meltwater/Cision; ahead of Muck Rack |
| **Collaboration** | Good (assign, tag, notes) | Adequate but less sophisticated than enterprise tools |
| **Global reach** | European strength, growing globally | Behind Meltwater (global); ahead in continental Europe vs Muck Rack (English-focused) |

### Strategic Position
Mention occupies the **lower-mid segment** of the media monitoring market, overlapping with Brand24 but differentiated by its social publishing capability and European heritage. Post-acquisition by Mynewsdesk, there is potential for a more integrated offering (monitoring + distribution + newsroom) that could move upmarket. However, standalone Mention lacks the data depth, premium content access, and PR workflow tools needed to compete with Meltwater/Cision/Muck Rack for enterprise deals. For AlmaLabs, Mention demonstrates that **simple, well-designed monitoring at low price points** can attract a large user base, and that bundling monitoring with adjacent capabilities (publishing, distribution) is a viable differentiation strategy for the mid-market.

---

## Sources
- https://mention.com/en/ — Company website
- https://mention.com/en/pricing/ — Public pricing page
- https://mention.com/en/blog/ — Product updates and content
- https://www.g2.com/products/mention/reviews — G2 user reviews
- https://www.capterra.com/p/134333/Mention/ — Capterra reviews
- https://www.crunchbase.com/organization/mention — Company and funding data
- https://mention.com/en/api/ — API documentation
- https://www.mynewsdesk.com/ — Parent company (Mynewsdesk)
- https://www.nhst.no/ — Ultimate parent (NHST Media Group)
- Industry analyst reports and competitive intelligence databases
