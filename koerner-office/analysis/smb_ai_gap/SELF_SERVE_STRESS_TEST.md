# Backlog 10: stress test of the free self-serve "AI support readiness" audit

24 Oct 2026 (UK time). Desk research only. Nobody contacted, nothing spent. Sources were opened 24 Oct 2026 unless a date is given.
**The idea under test:** a doc-heavy B2B firm (manufacturer, distributor or exporter with manuals, spec sheets, FAQs and a support team) pastes its URL. It gets a free report on how much an AI support agent would help.

## Verdict in one line

**As a standalone free audit for end firms: kill (medium confidence).** The market is saturated, there's no one to charge, and the traffic would take 6–12 months of SEO to build.
**What survives:** sell the *audit engine* to the people who already use audits to win clients. AI-support agencies and consultants would get a white-label, embeddable audit. This is the proven MySiteAuditor and SEOptimer model, ported to AI support (Version B below). **Maybe, leaning pursue (low-medium confidence)** until a £50 test shows agencies will pay.

---

## 1. Stress test

### 1.1 Competitors and substitutes: saturated

**Questionnaire-style readiness graders and ROI calculators.** All free, all built by chatbot vendors as lead magnets:
- Chatsy has an ROI calculator, readiness assessment and cost calculator, with no signup ([chatsy.app/tools](https://chatsy.app/tools)).
- VoxBolt has a 6-question AI readiness assessment ([voxbolt.ai](https://voxbolt.ai/tools/ai-readiness-assessment/)).
- Canary has an "AI Chatbot Readiness Grader" with 10 questions, a score out of 100 and savings in $ ([canarychat.app](https://canarychat.app/tools/chatbot-readiness-grader)).
- Wiredesk ([wiredesk.ai](https://wiredesk.ai/tools/support-roi-calculator)) and Mixdesk ([mixdesk.com](https://mixdesk.com/free-tools/ai-customer-service-roi-calculator), examples reviewed 23 Sep 2026) have ROI calculators.

**Paste-your-URL instant bot demos.** These are a stronger substitute than a report, because the firm *sees its own bot answer* within 60 seconds:
- Conferbot ([conferbot.com](https://www.conferbot.com/tools/website-chatbot-preview))
- Corner, up to 20 pages ([getcorner.ai/try](https://getcorner.ai/try))
- SpideyChat ([spideychat.com/try](https://spideychat.com/try))
- Chatonbo ([chatonbo.com/try-it](https://chatonbo.com/try-it))
- Scale2Sales ([scale2sales.com](https://scale2sales.com/tools/chatbot-tester))

**Manufacturer-specific vendors already own the niche pages.** Help Genie ([helpgenie.ai](https://helpgenie.ai/ai-support-for-manufacturers)), Graybeard ([askgraybeard.com](https://askgraybeard.com/manufacturers)), Wonderchat ([wonderchat.io](https://wonderchat.io/uses/ai-customer-service-manufacturing)) and Miquido ([miquido.com](https://www.miquido.com/custom-ai-solutions/manufacturing-customer-service/)).

**AI consultants already sell audit-first.** Paid AI readiness audits run from $297 to $50k ([appliedagencyai.com](https://www.appliedagencyai.com/insights/how-much-does-an-ai-readiness-audit-cost)). ConsultKit pitches an "audit-first sales model" to AI consultants ([consultkit.ai](https://www.consultkit.ai/blog/the-audit-first-sales-model-why-it-beats-traditional-discovery-calls-for-ai-consultants-1774464789415)). This is a likely direct competitor to Version B. I haven't checked its product depth.

**What they miss.** These are gaps, not a moat.
- Almost all are self-reported questionnaires (ticket volume, % repetitive). None *measures* the site: PDF manual count, spec-sheet depth, FAQ coverage, languages, chat present or absent, support-hiring signals.
- None benchmarks a firm against its own sector or country ("you're in the bottom 20% of Portuguese ceramics exporters").
- Instant demos show a bot but not *why* or *how much*, and they are vendor-locked.
- Nothing I found is sector-specific *and* multilingual (PT/ES).

### 1.2 Who pays, and how much (sourced terms)

| Mechanism | Real terms | What it means here |
|---|---|---|
| **Vendor affiliate fees** | DocsBot: 25% recurring for 12 months, 60-day cookie, PayPal, 45-day hold. Plans $49/$149/$499 a month ([docsbot.ai/affiliates](https://docsbot.ai/affiliates); plan prices via [affiliationlist.com](https://affiliationlist.com/product/docsbot/)). DocsBot agency Partner: 30% first year, *requires you to build client bots* ([docsbot.ai/partners](https://docsbot.ai/partners)), which is agency work. Chatbase: up to 30% for 1 year, $100 minimum ([terms](https://www.chatbase.co/affiliates/terms), [Dub](https://partners.dub.co/chatbase)). Tidio: 20% for 2 years, or 25% at $25k+ new ARR a year ([help.tidio.com](https://help.tidio.com/hc/en-us/articles/5444003167388-Affiliate-Program)). Zendesk: 15% of first-year sales ([zendesk.com](https://www.zendesk.com/programs/affiliate-program/)). Intercom: no public affiliate rate; a solution-partner programme for agencies plus $250 customer-referral credits ([intercom.com](https://www.intercom.com/legal/terms-and-policies/referral-program)). | Per referral, first year: DocsBot Standard $149 × 12 × 25% ≈ **$447**, Personal ≈ $147. Chatbase/Tidio are similar or lower. Earning $1k a month needs roughly 2–3 new paying referrals a month, every month. |
| **Paid deep report** | No direct comparable found. SEO-audit resellers charge about $5 per report (MySiteAuditor case study, [mysiteauditor.com](https://mysiteauditor.com/blog/how-one-of-our-customers-generated-12000-leads-with-mysiteauditor/)). Paid AI audits from consultants run $297+, but those include a human. | Low willingness to pay for an automated PDF when free graders exist. Weak. |
| **Selling qualified leads to AI-support agencies** | No public price list found (uncertain). The value per lead is anchored by the agency's deal: the host's $2–3k setup + $500–1k a month (NOTES.md; unverified, from a DocsBot-biased source). | Lead resale needs consent to pass on contact details (UK GDPR / LGPD), plus a sales motion to agencies. Possible, but fiddly. |
| **White-label audit widget for agencies (SaaS)** | SEOptimer embeddable audit: $59 a month, or $44.25 a month billed annually ([seoptimer.com](https://www.seoptimer.com/embeddable-audit-tool/)). MySiteAuditor: $49 a month Starter, $79 a month Pro with embeds ([mysiteauditor.com/pricing](https://mysiteauditor.com/pricing)). SiteGuru grew from $400 to $14k MRR in a crowded SEO-tool market ([Indie Hackers](https://www.indiehackers.com/post/tech/building-an-seo-product-to-14k-mrr-in-a-crowded-market-gU4DE1l094cpj1GjNHwu); [Starter Story](https://www.starterstory.com/seo-audit-tool)). | **The best-proven model.** Many small companies make money selling audit-as-lead-magnet tools *to agencies*. |
| **Done-for-you upsell** | $2–3k setup + $500–1k a month | ❌ Agency work. Breaks his rules. |
| **Monitoring subscription for end firms** | No evidence that firms pay to re-grade their AI readiness. | Weak. |

**Evidence that graders work as lead magnets.**
- HubSpot's Website Grader (launched 2006/07) graded 1M URLs by mid-2009, 2M by early 2010 and 4M+ by Dec 2011.
- It brought in about 20k visitors a month and about 1,500 leads a month for HubSpot.
- Sources: [HubSpot blog 1M](https://www.hubspot.com/blog/bid/4834/website-grader-evaluates-over-1-million-urls), [2M](https://www.hubspot.com/blog/bid/5539/website-grader-analyzes-over-2-million-sites), [PR Newswire, 6 Dec 2011](https://www.prnewswire.com/news-releases/hubspot-launches-comprehensive-free-marketing-grader-tool-after-grading-4-million-websites-135091323.html), [Social Fresh case study](https://socialfresh.com/hubspot-website-grader-case-study/).

**Caveat:** it worked because HubSpot *had a $ product behind it*. The grader monetised through the vendor's own subscription, not by itself. Lesson: the money is with whoever owns the downstream product or the client relationship.

### 1.3 Distribution without cold outreach

- **Search demand is real but contested.** "AI customer support" gets about 8.1k US and about 22k global searches a month (Aug 2026, via [thepayday.ai](https://thepayday.ai/trends/ai-customer-support); secondary, unverified). Manufacturer-specific queries are long-tail and already targeted by the vendors in 1.1. I didn't get volumes for "AI chatbot for manufacturers"; it's likely tens to low hundreds a month (estimate). New-domain SEO takes 6–12 months.
- **Benchmark reports per sector/country** ("State of AI support in Portuguese ceramics exporters, 2026"). This is the most defensible inbound hook: it gets press and trade-association links, and agents can produce it from the scanner. Unproven.
- **Agency channels (for Version B).**
  - The AI Automation (A–Z) Skool community lists 164.6k members ([skool.com/freegroup](https://www.skool.com/freegroup)), and there's also the AI Automation Society ([skool.com](https://www.skool.com/ai-automation-society)).
  - A UK directory lists 276 AI/automation agencies, 156 of them offering AI strategy or audits ([trustedaiagencies.com, Oct 2026](https://trustedaiagencies.com/guides/uk-ai-automation-agency-prices-2026/)).
  - Vendor partner directories (DocsBot/Chatbase Experts).
  - Posting in communities counts as posting and needs Ricardo's OK. Without a face, it can be done as a product account.
- **Lawful opt-out email** (see COUNTRIES.md). One labelled email per *agency* in the US is lawful under CAN-SPAM. Selling to agencies is also cleaner than selling to SMBs.

### 1.4 Will doc-heavy SMBs actually paste a URL?

- **The adoption gap is real.**
  - US Census BTOS: about 18% of firms used AI in some business function in Nov 2025–Jan 2026, and about 18% of firms with fewer than 20 staff ([Census CES-WP-26-25](https://www2.census.gov/library/working-papers/2026/adrm/ces/CES-WP-26-25.pdf)).
  - Manufacturing was about 12% in the April 2026 supplement ([Minneapolis Fed, 2026](https://www.minneapolisfed.org/article/2026/ai-adoption-in-business-grows-steadily-but-unevenly)) and about 20.8% by Sep 2026 (secondary tracker, [vester.si](https://vester.si/ai-impact/census-btos/)).
  - Among adopters, the top uses are sales/marketing (52%), strategy (45%) and IT (41%). Customer service wasn't in the top three.
- **But a gap is not intent.** I found no evidence of manufacturers *searching for an AI readiness grader*. The people who search for and use these tools are vendors' prospects and consultants. That matches the manual's "hiring a support person" buying trigger: intent shows up as job ads, not grader visits.
- **Conclusion:** end-firm pull is unproven and probably weak. Agency pull for "tools that help me win clients" is proven by SEOptimer, MySiteAuditor and ConsultKit.

### 1.5 Defensibility (what stops a weekend copycat?)

- **Nothing about the grader itself.** Vendors ship these as free side tools, and any LLM can build one in a day.
- **Partial moats:**
  1. a crawled benchmark dataset across thousands of sector sites in EN/PT/ES, refreshed monthly (time plus data compound)
  2. sector and language depth (Portuguese/Spanish manuals, ES/PT/LATAM exporters)
  3. vendor-neutral positioning, which vendors can't credibly copy
  4. for Version B, switching costs once an agency embeds the widget and its leads flow through it.
- None of these is strong. The benchmark dataset is the only one that gets harder to copy over time.

### 1.6 Automation, ops and cost

- **End to end by agents: yes.** Crawl (the scanner already exists, `tools/smb_ai_gap_scan.py`), score, LLM-written report, email delivery, Stripe billing. Ricardo's time is about 1–2 h a week for review and approvals.
- **Cost per audit (estimate, not measured):** crawl 20–50 pages plus about 30–80k LLM tokens on a cheap model is roughly **$0.01–0.10**. Hosting: free to $20 a month (Cloudflare/Vercel plus a small worker). Chat-widget detection needs a headless browser, about $0.005 per site in compute (estimate).
- **Legal (UK, not legal advice):**
  - Storing submitted URLs and emails makes him a UK GDPR controller. He needs a privacy notice, a retention limit and processor terms (LLM, email provider).
  - The ICO data protection fee is probably due (tier 1, about £52 a year; check the exemptions).
  - Marketing follow-ups to people who submitted need consent or soft opt-in under PECR. Make it a tick box.
  - Auditing a third party's public website is fine. Don't present scores of *named* firms publicly in a defamatory way; aggregate benchmarks are safer.
  - Respect robots.txt and terms of service when crawling.

### 1.7 Strongest kill reasons (honest)

1. **No one to charge at the end-firm level.** The free graders are vendor lead magnets subsidised by a $49–499 a month product. A neutral grader without a product only earns affiliate scraps.
2. **Saturated and commoditised.** At least 5 free readiness/ROI graders and at least 5 paste-your-URL instant demos already exist. The instant demo beats a report on "wow".
3. **Wrong buyer psychology.** Owners of doc-heavy SMBs don't search for "AI readiness". Their intent shows up when they hire support staff or have backlog pain, and they buy from vendors or integrators.
4. **Affiliate maths is thin.** About $150–450 per referral for one year. You'd need a steady 2–3+ paid referrals a month to reach $1k a month, which means thousands of qualified audits a month. HubSpot needed about 20k visitors a month for 1.5k leads.
5. **Slow distribution.** SEO on a new domain takes 6–12 months, and the vendors already target the manufacturer keywords.
6. **The agency-facing version has its own risks.** AI agencies churn fast (many are hobbyists from Skool courses), ConsultKit-style tools already exist, and agencies can vibe-code their own.

---

## 2. Refined versions

### Version A: "Sector benchmark + neutral audit", monetised by vendor affiliates
- **Customer:** doc-heavy B2B firms (EN/PT/ES) and their ops or support leads.
- **Value:** "How does your support content compare to 500 peers in your sector/country, and what would an AI agent answer from it today?" A measured audit, not a questionnaire, plus vendor-neutral tool picks.
- **Revenue:** affiliate links (DocsBot 25% for 12 months, Chatbase up to 30% for 1 year, Tidio 20% for 2 years, Zendesk 15% first year).
  - Realistic: 500 audits a month → 1–3% start a paid plan → 5–15 referrals a month × $150–450 in the first year ≈ **$750–6,750 per monthly cohort**, recognised over 12 months.
  - The 1–3% conversion is an estimate, not sourced.
  - Year-1 realistic run-rate: **$0–1.5k a month**.
- **Distribution:** benchmark reports (PR, trade associations, LinkedIn page without a face) plus SEO pages per sector × country.
- **Moat:** benchmark dataset plus multilingual depth.
- **Time to first £:** 3–9 months.
- **Workload:** agents do everything. Ricardo about 1 h a week.
- **£50 test (needs approval to publish or spend):** publish one free benchmark ("AI support readiness of 300 UK lighting manufacturers") on a landing page with the audit form, and push £50 of LinkedIn/Reddit ads to ops/support titles in manufacturing.
  - **Pass:** at least 40 audits run and at least 3 affiliate click-throughs to a vendor trial within 21 days.
  - **Kill:** fewer than 15 audits.
- **Verdict: Maybe → lean kill (confidence: medium).**

### Version B: White-label "AI Support Readiness Audit" widget for AI-support agencies and consultants (MySiteAuditor model)
- **Customer:** AI automation and support agencies and freelancers. Hundreds in the UK alone (276 listed, 156 offering audits), and tens of thousands in Skool communities worldwide. They sell to SMBs; Ricardo sells to them. That's software, not agency work.
- **Value:** agencies embed our audit on their own site. A prospect pastes a URL and gets a branded report: doc count, FAQ coverage, chat present or absent, languages, sector benchmark, estimated deflection. The lead lands in the agency's CRM. It's measured, not a questionnaire, and multilingual EN/PT/ES out of the box.
- **Revenue:** $49–99 a month per agency, matching SEOptimer ($59) and MySiteAuditor ($49/$79).
  - 20 agencies ≈ $1–2k MRR; 100 ≈ $5–10k MRR.
  - SiteGuru shows $400 → $14k MRR is achievable in a crowded audit-tool niche.
  - Optional add-on: affiliate links on reports where the agency opts in.
- **Distribution:**
  - SEO for "AI audit tool for agencies" and "white label AI readiness report"
  - listings in agency tool directories
  - a free tier (5 audits a month)
  - Skool and Reddit posts as a product account (needs Ricardo's approval each time)
  - lawful one-off CAN-SPAM email to US agencies (with approval)
- **Moat:** embedded widget plus CRM integrations (switching cost), the benchmark dataset that makes reports richer than a vibe-coded clone, and multilingual reports.
- **Time to first £:** 4–8 weeks after the MVP.
- **Workload:** agents build and run it (crawler exists, plus report generator, embed script and Stripe). Ricardo about 1–2 h a week for approvals and support escalations.
- **£50 test (no spend or contact until approved):**
  1. Agents build a landing page plus a working demo audit for 3 sample firms (free).
  2. Add a "$49 a month founding price, waitlist / $1 card-verified pre-order" button.
  3. Spend up to £50 on Reddit/Skool-adjacent ads or a single sponsored post, *or* post free in 2 communities as a product account.
  - **Pass:** at least 15 agency waitlist signups and at least 2 paid pre-orders within 14 days.
  - **Kill:** fewer than 5 signups and 0 pre-orders. Also kill if a desk check first shows ConsultKit or similar already sells exactly this under $50 with traction.
- **Verdict: Maybe, leaning pursue (confidence: low-medium).** It's the only version that matches a proven, repeatable money model (audit widgets sold to agencies).

### Version C: Multilingual (PT/ES/LATAM) benchmark data + qualified-lead feed for agencies and vendors
- **Customer:** AI-support vendors and agencies entering Iberia and LATAM (Brazil, Mexico, Colombia, Spain, Portugal).
- **Value:** a monthly feed of firms scored by doc-heaviness and AI gap, plus sector benchmark reports in PT/ES.
- **Revenue:** $200–1,000 a month per subscriber (estimate, no comparable found), or a per-lead fee.
- **Legal friction:**
  - Selling lists of companies is mostly fine for generic company data.
  - Named contacts trigger UK GDPR (as controller), LGPD and Mexico's LFPDPPP.
  - Spain and Portugal are hostile (see COUNTRIES.md).
- **Distribution:** direct to roughly 50–200 vendors and agencies, which needs outreach (lawful opt-out only for US/BR/MX recipients).
- **Moat:** dataset plus languages.
- **Time to first £:** 1–3 months if anyone buys.
- **Workload:** agents crawl and refresh. Ricardo about 1–2 h a week, but sales to vendors is relationship-driven.
- **£50 test:** produce one free PT/ES sample report (Portuguese ceramics/cork exporters) and a pricing page. With approval, send one CAN-SPAM-compliant email to 30 US-based AI-support vendors expanding into LATAM.
  - **Pass:** at least 3 replies asking for the paid feed or a call.
  - **Kill:** 0–1 replies.
- **Verdict: Kill for now (confidence: medium).** It's data-broker territory, relationship sales, and there's no proven comparable at this scale. Keep the benchmark dataset as a by-product of A/B.

---

## 3. Verdicts

| Version | Verdict | Confidence | Main reason |
|---|---|---|---|
| Original (free audit for end firms, no monetisation) | **Kill** | Medium | Saturated vendor lead magnet with no payer |
| A: Benchmark + neutral audit + affiliates | **Maybe (lean kill)** | Medium | Thin affiliate maths, slow SEO |
| B: White-label audit widget for AI agencies | **Maybe (lean pursue)** | Low-medium | Proven model (SEOptimer, MySiteAuditor); a clear buyer that pays $49–99 a month; fully automatable |
| C: PT/ES data and lead feed for vendors/agencies | **Kill (park)** | Medium | Data-broker legal friction plus relationship sales |

**Recommended test:** Version B. First a free desk check of ConsultKit and similar "audit for AI consultants" tools (pricing, traction). Then the landing page, demo and pre-order test (≤£50, nothing spent or posted without Ricardo's approval). It counts toward the "pursue at medium+" target only if it reaches at least 2 paid pre-orders.

## Uncertain or unverified
- Search volumes for manufacturer-specific queries; the 8.1k/22k figures are from a secondary source.
- ConsultKit's actual product and pricing.
- Lead-resale prices for AI agencies.
- The 1–3% audit-to-paid conversion and the per-audit cost (estimates).
- DocsBot plan prices come from a third-party affiliate directory, not docsbot.ai/pricing.
