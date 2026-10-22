# v7 TOP10: agent-run side-hustle ideas for a UK operator

**Inputs.** This list uses `ideas_scored.json` and `ideas_scored.csv`: 1,154 clusters drawn from the v7 transcript corpus. Each cluster has a combined score built from success and automation. Clusters ranked 1-256 have a judge result; the rest only have a preliminary score.

**How the ten were chosen.** The ranking was treated as a guide, not a verdict. Picks were filtered on four things:
1. a realistic chance of success;
2. near-100% agent automation of acquisition, onboarding, delivery, billing and support;
3. UK legality, meaning PECR, TPS/CTPS, UK GDPR and licensing;
4. fit for Ricardo: technical, no "websites for local businesses", enjoyable, and minimal personal involvement.

**Merging and counts.**
- Near-duplicate clusters are merged. "n_videos (merged)" counts distinct videos across the merged clusters.
- "Score" means the primary cluster's combined / success / automation_pct.
- acq/onb/del/bill/sup are the judge's 1-5 automation sub-scores.

**Evidence rules.**
- Quotes are verbatim from `ideas_scored.json` claims. They are creators' own claims and have not been verified by us.
- Startup cost and time to first revenue are given only where a source states them. Otherwise they are "unknown".
- Revenue figures are mostly in USD because the sources are mostly US.

**Revision status.** This is the post-red-team version. The critique is in `TOP10_redteam.md`, and the changes from the first draft are listed at the bottom.

## The ten at a glance

| # | Idea | Primary cluster | Score (comb/succ/auto) | n_videos (merged) |
|---|---|---|---|---|
| 1 | ASO-first single-feature app portfolio | C0263 (+C0116) | 81.8 / 75 / 90 | 3 (7) |
| 2 | Niche software add-ons for platform marketplaces (WordPress/Shopify/Chrome) | C0106 + C0266 (+C1099, C0482) | 71.7 / 69 / 75 | 5 (9) |
| 3 | UK data-led SEO directories with an owned email list | C0066 (+C0084, C0050, C0114, C0404, newsletter C0063/C0059 as a layer) | 77.2 / 75 / 80 | 6 (15 directory/content; newsletter videos not counted) |
| 4 | UK calculator and utility tool portfolio | C0111 + C0310 | 69.7 / 53 / 90 | 4 (6) |
| 5 | UK open-data alert and API products | C0691, C0438, C1119, C0441, C0681 | 70.8 / 55 / 90 (C0438, prelim) | 1 each (4) |
| 6 | Niche job board, employer- and sponsor-paid | C0160 | 73.3 / 72 / 75 | 4 |
| 7 | Technical templates and AI skill packs | C0188 + C0187 (+C0186; C0051 Etsy demoted) | 68.8 / 62 / 77 | 3 (14 incl. Etsy cluster) |
| 8 | Automated website/GEO audit and change-monitoring SaaS | C0265 + C0129 (+C0431) | 66.5 / 62 / 72 | 3 (9) |
| 9 | UK-vertical micro-SaaS ("cheaper, narrower incumbent") | C0044 + C0122 | 66.5 / 67 / 66 | 8 (12) |
| 10 | Personalised children's story subscription (wildcard) | C0703 + C0108 | 68.6 / 60 / 79 | 1 (5) |

---

## 1. ASO-first single-feature app portfolio

**Concept.** Build a series of small iOS (and later Android) apps that each do one job. Each targets an App Store search term with real volume and weak competitors, and charges through a free trial into a subscription. You ship many, keep the ~40% that earn, and drop the rest. This is AI-heavy work: agents do keyword research, code, screenshots, metadata, paywall A/B tests and review replies.

**Why it ranks.**
- C0263 is #1 overall: combined 81.8, success 75, automation 90, E 4.5, R 4, M 3. acq/onb/del/bill/sup are 4/5/5/5/4.
- It has 3 videos, 2 with first-hand claims, across 2 channels.
- C0116 (single-purpose consumer AI image apps, 66.4, 4 videos) is merged as a sub-genre.

**Evidence.**
- `t9yFAJzsOkE`: "I have paraphrase, which is one of our apps that's making about $2600 a month"
- `t9yFAJzsOkE`: "one of our apps that's doing about 35,000 MRR, we get 12% of the people starting a free trial"
- `t9yFAJzsOkE`: "I need to launch 10 to get 4 right to generate money"
- `t9yFAJzsOkE`: "that's when it went up to 6,000 the next three months"
- `22Jpzt683jw` (C0116): "We made like 10 grand in like two months"

**How agents run it.**
- **Acquisition:** ASO keyword mining, metadata and screenshot generation, and localisation into multiple storefronts. Optional Apple Search Ads within a capped budget.
- **Onboarding and billing:** StoreKit or RevenueCat paywalls. Apple handles payments, VAT and refunds.
- **Delivery:** the app itself, with a coding agent producing a weekly release cycle.
- **Support:** an agent replies to reviews and to a support inbox.
- **Human touchpoints:**
  - holding the Apple/Google developer accounts and passing identity checks;
  - approving ad spend;
  - escalating App Review rejections.

**UK legal notes.**
- No outbound contact, so PECR and TPS do not apply.
- UK GDPR applies: a privacy policy, minimal analytics, and App Privacy labels that match reality.
- Consumer Contracts Regulations: Apple's terms cover the 14-day cancellation right.
- Subscriptions need clear renewal terms. Watch the DMCC Act 2024 subscription-contract rules as they commence.
- If distributed in the EU, the DSA trader-status disclosure publishes your address. Use a business address.

**Startup cost and time to first revenue.**
- Cost per source: "Not stated beyond the Apple developer account; ad spend optional ($10-20/day)."
- Time to first revenue is unknown. The source's revenue jump came "the next three months" after a paywall change on an existing app.

**Key risks.**
- App Store guideline 4.3 (spam/duplicate apps) can block a portfolio.
- Hard-paywall and weekly-subscription scrutiny.
- Cloning by other AI builders.
- Built-in OS or ChatGPT features replacing single-purpose apps.
- Evidence is concentrated in one creator.

**First-week validation test.**
1. Agents mine 50 App Store search terms in two niches that Ricardo finds fun, such as developer utilities or parent tools.
2. Score each on popularity, competitor review counts and last-update date.
3. Build and submit one app to TestFlight and App Review.
4. Pass bar: at least 3 terms where the top-5 results have fewer than 500 reviews or haven't been updated in 12 months, and one app approved.

## 2. Niche software add-ons for platform marketplaces

**Concept.** Build a paid plugin, extension or app that solves a narrow, painful problem inside a platform with a built-in marketplace: WordPress.org, the Shopify App Store, the Chrome Web Store, or Microsoft AppSource. Use a free tier in the directory as the funnel and a paid tier or licence, billed by a merchant of record. Ricardo is technical, so this is the most "enjoyable engineering" option on the list.

**Why it ranks.**
- C0106 (Link Whisper / niche WordPress SEO software): 71.7 / 69 / 75, 5 videos, 5 with first-hand claims, but only 1 channel. E 4.5.
- C0266 (add-on apps for platform marketplaces): 71.4 / 66 / 78, R 4, M 3, acq 4.
- Merged with C1099 (an AI image WordPress plugin) and C0482 (acquire and grow small plugins), for 9 distinct videos.

**Evidence.**
- `eVldld15cXo`: "it actually did $30,000 during the launch period, during the very first month."
- `eVldld15cXo`: "It actually did about $5,000 to $7,000 in the second and third month."
- `eVldld15cXo`: "about $90,000 in revenue, on average, each and every month, by the time I sold the company five years later."
- `eVldld15cXo`: "in early January 2025, I was wired $2.7 million and the deal on Link Whisper was done."
- `eVldld15cXo`: "WordPress.org ended up having 30 to 40,000 free downloads."
- `4IETgMZy1o0` (C0482): "I grew it from 1,500 a month to 30 grand a month and it was just me."
- `vB08-7RzgOs` (C0266) is a hypothetical, not a result: "Sell for 300 bucks one time or 47 bucks a month, undercut them on price, 200 customers and you're making six figures a year."

**How agents run it.**
- **Acquisition:** the directory listing and its SEO, docs and comparison pages, plus an affiliate programme that agents administer.
- **Onboarding:** in-product setup wizards.
- **Delivery:** coding agents handle fixes and compatibility updates for new platform versions.
- **Billing:** Freemius, Paddle, Lemon Squeezy or Shopify Billing, which also handle VAT.
- **Support:** an agent triages tickets and forum threads from the documentation.
- **Human touchpoints:**
  - final approval of releases, since a bad update breaks customer sites;
  - platform review appeals;
  - refunds outside policy.

**UK legal notes.**
- Inbound only, so no PECR exposure.
- If the plugin processes end-user data you are a processor and need a DPA template. Prefer designs that store nothing.
- A merchant of record removes the UK/EU VAT burden.
- GPL licensing applies to WordPress plugins: anyone can redistribute your code, so you sell updates and support, not exclusivity.

**Startup cost and time to first revenue.**
- Cost: unknown, not stated.
- Link Whisper's first month was $30k, but at launch it had an existing audience ("I could email 10,000 people that were on my email list that were not customers", `eVldld15cXo`).
- Without an audience, time to first revenue is unknown.

**Key risks.**
- The platform owner ships the feature natively.
- Directory ranking changes.
- Support load grows with installs.
- The flagship evidence is one founder with a pre-existing audience.

**First-week validation test.**
1. Agents scrape public directory data (allowed) for 3 platforms and list plugins with high installs, ratings under 4.0, or no update in 12+ months.
2. Mine their 1-2 star reviews for repeated unmet requests.
3. Pass bar: one problem cited in at least 20 reviews across at least 3 competitors, which Ricardo could build an MVP for in under 2 weekends.

## 3. UK data-led SEO directories with an owned email list

**Concept.** Build directories whose value is a structured dataset that agents assemble and keep fresh, rather than AI-written articles. Examples are UK-specific listings of things (places, products, providers, tools), with filters, comparison pages and programmatic long-tail pages. They earn from display ads, affiliate links, featured listings and sponsorship. Every site captures emails into a niche digest: the newsletter clusters are merged in here as a layer, not a stand-alone pick.

**Why it ranks.**
- C0066 (niche SEO directory sites): 77.2 / 75 / 80, rank 2, E 4.5, S 4, R 4, all sub-scores 4. It has 6 videos but only 1 channel.
- C0050 (niche content sites): 77.0, 7 videos, 3 channels.
- C0084 (hobby/info directory): 68.6, 5 videos.
- Also merged: C0114 (provider finder) and C0404 (developer/AI tool directory).
- Distinct videos across the directory and content clusters: 15.
- Newsletter layer: C0063 (70.3, 6 videos, 4 channels) and C0059 (66.0, 7 videos).

**Evidence.**
- `SiRlIMtZygI`: "Like most of my directories are making 1K a month. Some make 10K, but most of make just 1K."
- `1fTGX4sLVqA`: "completely passively it's probably around like 2300 to $3,000 a month"
- `1fTGX4sLVqA`: "it ranges from like probably 70 to like 90,000 monthly visitors"
- `1fTGX4sLVqA` (C0114): "It gets around 6,000 monthly visitors but that one's interesting too"
- Newsletter layer:
  - `IPnafDDgj6o`: "Spark Loop will pay you between 50 cents and $5 for every single email"
  - `4AWlBGVQ8nA`: "Boost is probably in like the 10 to 25K um when I'm like active using Boost."

**How agents run it.**
- **Acquisition:** keyword and gap research, programmatic page generation from the dataset, internal linking, and submission to relevant communities. Email capture uses explicit opt-in.
- **Onboarding:** self-serve "claim or feature your listing" with Stripe checkout.
- **Delivery:** scheduled agents refresh the data, check broken links and send the weekly digest.
- **Billing:** ad networks, affiliates, Stripe and Beehiiv Boosts / SparkLoop.
- **Support:** an agent handles listing corrections and takedown requests.
- **Human touchpoints:**
  - choosing niches;
  - approving data sources (licence check);
  - responding to legal or takedown complaints.

**UK legal notes.**
- PECR reg 6 requires cookie consent before ad and analytics cookies, so use a CMP.
- PECR reg 22: newsletter emails only to people who opted in. No list buying.
- Affiliate links and paid placements must be labelled under the CAP Code and the DMCC Act 2024 rules on fake or incentivised reviews.
- Listings that name individuals (for example sole-trader providers) are personal data under UK GDPR: legitimate-interests assessment, accuracy, and an objection route.
- User reviews or comments bring Online Safety Act duties, so start without user-generated content.
- Avoid regulated niches such as health claims or financial promotion.

**Startup cost and time to first revenue.**
- Cost: unknown ("not stated" in all directory sources; one buys an expired domain at about $7,000, `abeY8nBzqzo`, which is not needed).
- Time to first revenue: unknown. Sources describe stacking sites and waiting months for SEO.

**Key risks.**
- Google core and helpful-content updates.
- AI Overviews and answer engines taking the click.
- Mass AI-built directories.
- The directory evidence comes from one channel.
- Ad revenue needs traffic thresholds.

**First-week validation test.**
1. Agents shortlist 10 UK niches where a structured dataset exists or can be legally compiled, and where search results show thin or outdated competitors.
2. Build one 200-page site with a digest signup.
3. Submit to Search Console.
4. Pass bar: at least 50% of pages indexed within 7-10 days, and at least one competitor result that is clearly worse than the data you hold.

## 4. UK calculator and utility tool portfolio

**Concept.** A portfolio of fast, accurate single-purpose web tools that agents build and maintain. Examples include UK-specific calculators (stamp duty, take-home pay, student loan repayment, EV charging cost, energy-tariff comparison) and developer or AI utilities (token cost calculators, format converters). They are monetised by ads, affiliate links and premium tiers, and cross-link to each other so traffic compounds.

**Why it ranks.**
- C0111 (ad-supported calculator and utility tool sites): 69.7 / 53 / 90. acq/onb/del/bill/sup are 4/5/5/5/4. 4 videos across 3 channels, but E is only 2.5.
- C0310 (portfolio of thin AI tools with cross-selling): 68.4, E 4, 2 videos.
- 6 distinct videos merged.

**Evidence.**
- `Wl0NMNbYRDk`: "It's been a total of 6 minutes and we have what we're looking for. An AI token cost calculator."
- `SiRlIMtZygI`: "I have some tools that are making like 1K a month, like very small tools"
- `SiRlIMtZygI`: "For the new users, half of them come from one tool to the other."
- `SiRlIMtZygI`: "Yeah. Like three products do most of the revenue and then everything else brings the rest."

**How agents run it.**
- **Acquisition:** SEO and AI-search optimisation, plus tool directories.
- **Onboarding, delivery and billing:** none needed for free tools. Stripe handles premium tiers.
- **Maintenance:** a scheduled agent re-checks formulas each April against GOV.UK and HMRC rate changes and runs regression tests.
- **Human touchpoints:**
  - signing off on rate and formula changes for tax calculators;
  - choosing niches.

**UK legal notes.**
- Cookie consent (PECR reg 6) for ads.
- Tax, pay and mortgage calculators must carry "guidance only, not advice" disclaimers.
- Do not recommend specific credit or investment products without FCA permission or an authorised partner (financial promotion rules).
- Use GOV.UK content under the Open Government Licence (OGL) with attribution.

**Startup cost and time to first revenue.**
- Cost per source: "Hostinger starter plan, 12-month, 10% off with code; the domain is about a cent for year one or a free .cloud domain" (`Wl0NMNbYRDk`), so near zero.
- Time to first revenue: unknown.

**Key risks.**
- AI Overviews answer simple calculations inline. Accuracy liability on tax figures.
- Low ad RPM without volume.
- The "6 minutes" build claim means anyone can clone you.

**First-week validation test.**
1. Agents build 5 UK calculators, each with a correctness test-suite checked against GOV.UK worked examples.
2. Publish them on one domain and submit to Search Console.
3. Pass bar: all 5 indexed, plus Search Console impressions on at least 2 of them within 7 days.

## 5. UK open-data alert and API products

**Concept.** Wrap official UK open data in alerts or developer APIs that save buyers hours: Contracts Finder and Find a Tender, Companies House, Land Registry Price Paid, EPC register, planning portals where licensed, and Food Standards Agency ratings. Examples:
- a "new tenders matching your keywords" daily email for SMEs;
- a clean JSON API over a messy government dataset;
- a weekly trend digest.

Charge a monthly subscription.

**Why it ranks.**
- These are five single-video clusters with the same shape, each scoring 90 on automation (prelim or judge):
  - C0438 unbundled scraper data SaaS: 70.8, prelim, rank 257;
  - C1119 social-media posting API for developers: 69.5, rank 10, E 5;
  - C0681 weekly trend report: 69.1;
  - C0691 government contract finder: 67.5;
  - C0441 marketplace listing alerts: 64.9.
- They come from 4 distinct videos.

**Evidence.**
- `IywUW2RjXis`: "at 10 bucks a month. I was like, almost 50 people want to use something that I built"
- `IywUW2RjXis`: "grew it to over 5K in eight months"
- `IywUW2RjXis`: "we were seeing anywhere between 500 to $1,000 in monthly recurring being added week over week"
- `HIYiSVvN3RA` (C0691): "Okay, that took about 4 minutes" and "I'm going to spend 12 bucks, buy the domain name"

**How agents run it.**
- **Acquisition:** SEO on long-tail searches like "[sector] tenders UK", developer docs that answer engines can pick up, and build-in-public posts. Cold email is allowed only to limited companies (corporate subscribers) with an opt-out, and is off by default.
- **Onboarding:** self-serve keyword setup.
- **Delivery:** scheduled ingestion, matching and email or API serving.
- **Billing:** Stripe.
- **Support:** an agent works from the docs.
- **Human touchpoints:**
  - checking the licence on each dataset;
  - incident response when an upstream API changes.

**UK legal notes.**
- Use official APIs and OGL datasets, not scraping of sites with restrictive terms.
- Companies House officer data and Land Registry data include personal data, so UK GDPR still applies. You need a legitimate-interests assessment, a privacy notice, and purpose limits such as no profiling of individuals.
- If you ever do cold email, it can go only to corporate subscribers, needs an opt-out in every email, and must never go to sole traders or partnerships (PECR reg 22).
- No phone outreach, so TPS/CTPS is not engaged.

**Startup cost and time to first revenue.**
- Cost: "$12 domain plus Replit subscription" (`HIYiSVvN3RA`) and "Almost zero" (`50iWtrj9Mkw`).
- Time to first revenue: the developer API grew to "over 5K in eight months" (`IywUW2RjXis`). UK-specific timing is unknown.

**Key risks.**
- Every cluster is single-source, and the API case is about a US social-platform API.
- Upstream API changes.
- Incumbents already exist: Tussell, Stotles and Contracts Finder's own alerts for tenders.
- Free government alerts may be "good enough".

**First-week validation test.**
1. Agents pull 30 days of Contracts Finder and Find a Tender data and build keyword alerts for 3 SME sectors.
2. Publish a landing page with a free 14-day trial and a priced tier.
3. Run £50 of search ads.
4. Pass bar: at least 15 trial signups and at least 2 people replying with feedback on match quality.

## 6. Niche job board, employer- and sponsor-paid

**Concept.** A job board for one tight niche (for example remote UK developer contracts, climate-tech roles, or visa-sponsoring employers). Agents aggregate jobs from employers' public ATS feeds and careers pages where terms allow, enrich and tag them, and send daily alerts. **Under UK rules the board charges employers (featured posts), sponsors or advertisers, not job seekers.**

**Why it ranks.**
- C0160 is rank 4: 73.3 / 72 / 75, E 5. acq/onb/del/bill/sup are 3/5/4/5/3.
- It has 4 videos, 3 with first-hand claims, across 3 channels.

**Evidence.**
- `xEoLsAQFnOY`: "My name is Roman. I run a job board called CareerHound that made 25K last month. I'm non-technical, I launched it two years ago."
- `xEoLsAQFnOY`: "So I'm a strong believer in a hard paywall, so no free plans. Our users pay $7 a week, 20 a month, or 50 a year." (This is a seeker-paid model, which is not the UK model.)
- `xEoLsAQFnOY`: "The turn is high because we're selling a job search product, so it's 31%."
- `xEoLsAQFnOY`: "Last month, we did $28,000 in total, and right now our MRR is 12K."

**How agents run it.**
- **Acquisition:** SEO on role and location pages, Google for Jobs structured data, and an organic social feed.
- **Onboarding:** employers self-serve a paid "featured post" through Stripe.
- **Delivery:** ingestion and de-duplication, expiry checks, and alert emails.
- **Support:** an agent answers employer questions.
- **Human touchpoints:**
  - checking the source terms on each new feed;
  - legal sign-off on the revenue model;
  - complaints from employers who were listed without consent.

**UK legal notes.**
- **The Conduct of Employment Agencies and Employment Businesses Regulations 2003 generally prohibit charging work-seekers fees for work-finding services.** CareerHound's seeker subscription is therefore unsafe to copy. Charge employers or sponsors, and get advice before offering any paid seeker extras.
- Alert emails go only to people who opted in (PECR).
- Applicant CVs are personal data under UK GDPR. Don't store them: link out to the employer.
- Ads must not discriminate (Equality Act 2010). Filter postings.

**Startup cost and time to first revenue.**
- Cost: unknown.
- CareerHound was "launched two years ago" before reaching its current figures. UK employer-paid timing is unknown.

**Key risks.**
- The UK fee rules remove the proven seeker-paid model.
- Employers won't pay for a new board until it has traffic.
- Aggregators like Indeed and LinkedIn, plus Google for Jobs.
- ATS feed terms.
- The first-hand evidence is mostly one founder.

**First-week validation test.**
1. Agents identify 2 niches with at least 300 live UK roles per month available from public ATS feeds whose terms allow it.
2. Build the board and the alert signup.
3. Pass bar: 300 or more fresh roles indexed, and an alert-email open rate of at least 40% on the first 50 opt-in subscribers from organic posts.

## 7. Technical templates and AI skill packs

**Concept.** Sell tested, niche-specific digital products to technical buyers, through your own site, the n8n creator hub and Gumroad or Lemon Squeezy. Examples:
- n8n or Make workflows for UK tools (Xero, HMRC Making Tax Digital, Companies House);
- Claude or Cursor skill packs;
- starter kits and boilerplates.

Agents build, test, document and refresh them.

**Why it ranks.**
- C0188 (automation and software templates): 68.8 / 62 / 77, R 4, 3 videos.
- C0187 (AI skill and prompt packs): 67.8, 3 videos, 1 with first-hand claims.
- C0186 (sell existing templates): 63.5, 3 videos.
- C0051 (Etsy printables): 70.7, 7 videos, but M 1 and E 2.5. It is noted but not recommended; see the revisions.

**Evidence.**
- `quYKZushRPo`: "I launched this about 30 to 45 days ago, somewhere in that ballpark. It's made over $3,000 just passively as a digital product."
- `quYKZushRPo`: "I sell mine for $99, but there's about 20 to 25 skills in there."
- `DG4yP9MACWk` (C0051, second-hand): "he started a new Etsy store from scratch, and it took all of four months to reach his first $1,000 months"

**How agents run it.**
- **Acquisition:** marketplace listings, SEO landing pages, demo videos and free sample templates. All inbound.
- **Onboarding and delivery:** instant download with setup docs.
- **Billing:** a merchant of record (Lemon Squeezy, Paddle or Gumroad) handles VAT.
- **Support:** an agent answers from the docs, and a scheduled agent re-tests workflows against API changes.
- **Human touchpoints:**
  - picking niches;
  - spot-checking quality on new packs.

**UK legal notes.**
- Digital content: under the Consumer Contracts Regulations, get express consent and an acknowledgement that the 14-day cancellation right is lost on download.
- Don't copy others' designs (IP).
- No finance or investing "skills" that could be a financial promotion (FCA).
- Selling through a merchant of record covers VAT.

**Startup cost and time to first revenue.**
- Cost: not stated, "beyond existing Claude subscription and time" (`quYKZushRPo`).
- The $3k in 30-45 days came with an existing audience. Without one, it is unknown.

**Key risks.**
- Trivially copied.
- Vendors ship free skills and templates.
- Products go stale as fast as the tools change.
- Small revenue per product.

**First-week validation test.**
1. Agents build 3 UK-specific n8n workflows (for example Xero to MTD VAT summary, or Companies House filing alerts).
2. List them with a free lite version.
3. Pass bar: at least 100 free downloads or 1 paid sale in 7 days.

## 8. Automated website/GEO audit and change-monitoring SaaS

**Concept.** Self-serve SaaS that audits a site for technical SEO and "GEO" (visibility in AI answer engines), or watches competitors' pages, prices and ads and emails a weekly diff. The free one-off audit is the lead magnet, and the monitoring subscription is the product. Aim it at e-commerce stores and SaaS marketers, not local trades (Ricardo has ruled those out).

**Why it ranks.**
- C0265 (SEO/website audit tools): 66.5 / 62 / 72, R 4, 3 videos across 3 channels.
- C0129 (competitor monitoring reports): 61.5, 4 videos. This is the only pick whose judge flag is b2b_cold_email_ok.
- C0431 (listing/review intelligence): 55.2.
- 9 distinct videos merged.

**Evidence.**
- `KtAGjnWViMQ`: "What does this cost you through Hostinger VPS? About five bucks a month."
- `KtAGjnWViMQ`: "Takes about 30 minutes. It costs about five bucks a month and it will run forever."
- `lG5U30gKCaY`: "I recorded this video for like six hours because I had to build an app while recording this video."

**How agents run it.**
- **Acquisition:** a free audit tool (SEO and AI-search inbound), a Shopify app listing, and comparison content. Optional cold email to limited-company e-commerce brands only, off by default.
- **Onboarding:** enter a URL.
- **Delivery:** scheduled crawls and LLM-written diffs.
- **Billing:** Stripe.
- **Support:** an agent.
- **Human touchpoints:**
  - approving any outbound campaign;
  - handling disputes over crawling.

**UK legal notes.**
- Crawl politely and respect robots.txt and site terms.
- For ad monitoring, use the Meta Ad Library API, not scraping.
- Cold email goes only to corporate subscribers, with an opt-out and screening against sole traders. Never SMS, WhatsApp or DMs.
- No phone, so no TPS/CTPS.
- Customer data is minimal, so UK GDPR handling is routine.

**Startup cost and time to first revenue.**
- Cost: "About $5/month for VPS hosting; about 30 minutes of setup" (`KtAGjnWViMQ`).
- Time to first revenue: unknown.

**Key risks.**
- Extremely crowded (Ahrefs, Semrush, Similarweb and free checkers).
- Buyers can build it themselves with agents.
- Little moat.

**First-week validation test.**
1. Launch a free "AI-search visibility check" for Shopify stores, with an email-gated full report.
2. Pass bar: at least 30 audits run and at least 3 paid conversions to a £19/month monitoring tier in 7 days, with traffic from 2 inbound posts and one tool-directory listing.

## 9. UK-vertical micro-SaaS ("cheaper, narrower incumbent")

**Concept.** Use coding agents to build a focused, cheaper alternative to an over-featured incumbent, for one UK-specific workflow. An example is a compliance tracker for small landlords (gas safety, EICR and EPC renewal reminders), where UK rules make US tools a poor fit. Customers are inbound through "X alternative" pages and comparison content.

**Why it ranks.**
- C0044 (AI-built micro SaaS products): 66.5 / 67 / 66, S 5 (8 videos across 3 channels), E 4.5.
- C0122 (cheaper clone of incumbent software): 62.2, M 3.
- 12 distinct videos merged. This is the broadest evidence base of any pick, but the thinnest on first-hand results.

**Evidence.**
- `yC0S7eYvOIc`: "I scored this at 22 out of 25. Remember, lower is better." The source rates micro-SaaS as the slowest and hardest of its options.
- `M3mUNpWD4ow` (C0122, second-hand): "You go to builtwith builtwith.com.450 bucks a month. Don't spend that."

**How agents run it.**
- **Acquisition:** comparison and "alternative" SEO pages, plus directories such as G2 and AppSumo.
- **Onboarding:** in-app.
- **Delivery and support:** coding agents ship features, and a support agent answers from the docs.
- **Billing:** Stripe.
- **Human touchpoints:** this pick has the most:
  - product judgment;
  - security review;
  - incident handling for business-critical data.

**UK legal notes.**
- B2B SaaS that holds customer data makes you a processor. You need DPAs, security and breach procedures (UK GDPR).
- Some verticals are regulated: lettings, property and finance tools may touch the CMA's material-information rules, AML (anti-money-laundering) rules or FCA rules. Pick unregulated workflows.

**Startup cost and time to first revenue.**
- Both unknown. The source scores cost 4 out of 5 (higher than other options) and flags a "Long runway before first revenue".

**Key risks.**
- Distribution, not building, is the constraint.
- Vibe-coded clones flood every niche.
- Support for critical workflows.

**First-week validation test.**
1. Agents find 3 UK workflows where incumbents have 2-3 star reviews that complain about price or US-centricity.
2. Ship a landing page with a waitlist and a priced pre-order for each.
3. Pass bar: at least 25 waitlist signups or 2 pre-orders on one niche from £100 of search ads.

## 10. Personalised children's story subscription (wildcard)

**Concept.** Parents enter their child's first name, age and interests. Agents write and illustrate a short personalised bedtime story each day or week and deliver it by email. A premium tier prints and posts a monthly storybook or letter through a UK print-and-post API. Ricardo is the target customer, which helps with taste and with founder-led ads.

**Why it ranks.**
- C0703 (daily personalised bedtime story email): 68.6 / 60 / 79, R 4. It is a single video.
- C0108 (snail-mail story/letter subscription): 67.2 / 69 / 65, M 3, 4 videos, 3 with first-hand claims.
- 5 distinct videos merged.

**Evidence.**
- `1PwTrINNzOA`: "we have like a little over $300 in MR right now." and "we probably spent like $400 in ads"
- `a8qQzY3a1us`: "So for the bundle our margins are about what was it 80 75 to 80%." and "I think we spent a,000 or 1,500 bucks, and that's how we got 10 customers"
- `t_y8SelBm_s`: "12 a month. So, right now you can do prepaid for $100."

**How agents run it.**
- **Acquisition:** Meta and Pinterest ads to parents within an approved budget, plus gifting SEO.
- **Onboarding:** a web form.
- **Delivery:** generation, a safety filter and the email or print API.
- **Billing:** Stripe subscriptions.
- **Support:** an agent.
- **Human touchpoints:**
  - approving ad spend;
  - spot-checking the content-safety review;
  - handling complaints about child-facing content.

**UK legal notes.**
- Collecting children's names and interests is personal data under UK GDPR. Keep it to the minimum, collect it from the parent, and pay the ICO data protection fee.
- If the product is likely to be used by children directly, the ICO Age Appropriate Design Code applies, so keep it parent-facing.
- Content-safety review.
- Consumer Contracts Regulations for subscriptions.
- VAT through a merchant of record.

**Startup cost and time to first revenue.**
- Cost: "Low; domain plus about $400 ads" (`1PwTrINNzOA`). The physical-letter version spent $1,000-1,500 on Meta ads for 10 customers.
- Time to first revenue: unknown.

**Key risks.**
- Unit economics were only break-even in the source.
- Many AI story apps exist, and parents can prompt ChatGPT themselves.
- Churn as children age.
- Reputational risk from any unsafe output.

**First-week validation test.**
1. Agents build the signup form and generator, and run £100 of Meta ads with a 7-day free trial.
2. Pass bar: cost per trial under £5 and at least 20% of trial users opening 5 or more stories.

---

## Notable exclusions
- **Niche newsletters as a stand-alone business** (C0063 70.3, C0345, C0663, C0059). Folded into #3 as an owned-list layer. As a stand-alone business, sponsor sales need people, the scale bar is 5-10k engaged readers (judge estimate), AI newsletters are saturated, and UK flight deals already have entrenched incumbents.
- **Etsy printables** (C0051 70.7, rank 7). Market headroom M is 1. The judge describes a flood of AI listings and an Etsy crackdown on low-effort AI listings. Per-product earnings are small. Only the technical-template variant is kept, in #7.
- **Voice licensing** (C0359). Low success score.
- **Creator courses and personal-brand plays** (C0018, C0074, C0124). These need Ricardo's face and audience.
- **Local newsletter** (C0020). Automation 59, and it is local.
- **Local directories and rank-and-rent** (C0080, C0088). These are local-business websites by another name, which Ricardo rejected, and they rely on B2B outreach.
- **AI receptionists for local businesses** (C0004). These are local-business services, need human setup and sales, and phone outreach would need TPS/CTPS screening.
- **Freelance automation services** (C0033). Service-heavy and not near-100% automated.
- **Amazon FBA and physical products** (C0008). Inventory and logistics.
- **General affiliate sites** (C0016). Subsumed in #3, and the generic version is saturated.
- **Single-purpose AI image apps** (C0116). Kept only as a sub-genre inside #1, because M is 1 (fad risk).
- **Buying an existing content site** (C0050 sub-case, asking $10-22k) and **acquiring plugins** (C0482). Capital needed beyond a test budget. Noted inside #3 and #2.

## Revisions after red team
The first draft (pre-critique) order was:
1. Apps
2. Directories
3. Job board
4. Plugins
5. Newsletter
6. Templates (Etsy-led)
7. Calculators
8. Data/API wrappers
9. Bedtime stories
10. Audit/monitoring

The changes, driven by `TOP10_redteam.md`:
1. **Newsletter removed as a stand-alone pick.** It is merged into #3 as the owned-audience layer. Sponsorship sales are a human touchpoint, the source's acquisition sub-score is only 3/5, and AI-newsletter saturation is severe.
2. **Plugins moved up from 4 to 2.** This has the strongest first-hand revenue trail in the set (launch, growth and a $2.7M exit) and fits Ricardo's technical interest best. The "single founder, had an audience" caveat is stated explicitly.
3. **Directories moved from 2 to 3 and redefined as data-led.** AI-written content sites are deprioritised because of AI Overviews and the mass-AI-content risk. The one-channel concentration of C0066 is flagged.
4. **Job board moved from 3 to 6, with the revenue model changed.** The proven seeker-paid model (CareerHound) is not safely legal in the UK under the 2003 Conduct Regulations, so the pick is now employer- and sponsor-paid, which is unproven in the inputs.
5. **Templates refocused from Etsy printables to technical templates and skill packs** (C0188/C0187). Etsy has M 1, an AI flood and IP takedown risk.
6. **Data/API wrappers moved from 8 to 5 and narrowed to official UK open data with OGL or official APIs**, rather than scraping. They are labelled single-source, the evidence is US-centric, and UK GDPR limits on Companies House and Land Registry personal data are added.
7. **New #9, UK-vertical micro-SaaS (C0044/C0122).** It fills the newsletter's slot because it has the broadest multi-channel evidence (12 videos), though thin first-hand evidence and the longest runway are stated.
8. **Bedtime stories moved from 9 to 10 and labelled a wildcard.** It is single-source on the digital side and break-even on ads. Children's-data obligations are added.
9. **Audit/monitoring repositioned away from local trades and cold outreach.** It now targets e-commerce and SaaS buyers through inbound channels, and cold email is limited to limited companies and off by default.
10. **Every pick now states its evidence concentration** (single creator or channel), and startup cost and time to revenue are set to "unknown" wherever the inputs are silent.
