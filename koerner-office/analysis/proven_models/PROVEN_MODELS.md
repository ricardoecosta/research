# Proven, repeatable business models in the mined transcripts

23 Oct 2026 (UK time). A re-analysis of the v8 mining output. **Nothing was re-mined.**

**The new lens:** is this a proven, repeatable business **model** that an AI-agent team can copy and run? Many people succeeding at the same model counts *for* it. A crowded market isn't held against it. v8 asked the opposite question: is there a unique gap nobody has copied yet?

**Inputs:**
- `analysis/v8/ideas_flat.jsonl`: 4,334 mined records from 434 videos, each with line-cited claims.
- The v8 clusters (`clusters/membership.json`) and scores (`ideas_scored.csv`).
- The v1–v7 playbooks and plans, recovered from `1e03f1b^`.

**How the records were grouped:**
1. **Labelling.** One cheap labelling pass (Codex, low effort) put each of the 1,865 non-physical records into one of 23 business models.
2. **Physical and local records.** These were grouped by rules on their v8 category.
3. **Counts.** Every count below is computed by `scripts/proven_models/group.py` with no model involved.
4. **Evidence summaries.** One Codex call at medium effort per model wrote the summary from that model's cited claims only.

**Caveats:**
- Every revenue figure is a speaker's **unaudited claim**.
- "When" is the date given in the claim. If the claim gives no date, it's the video's publish date.
- Items marked [E] are my judgement.

## Why v8 missed these models

1. **It clustered by gap, not by model.**
   - v8 made 2,491 clusters, mostly single-video.
   - Consumer apps, for example, were split across **95 clusters, 87 of them single-video**. Each cluster then scored low on "success" because it only had one source.
   - Micro-SaaS was split into 172 clusters, digital products into 31 and directories into 21.
   - Counted as models, they have 52, 50 and 19 videos behind them.
2. **The hours>5 hard rule measured the creator's own hours, not owner hours with agents doing the work.** It was the *only* failing rule for:
   - 29 app clusters
   - 22 micro-SaaS clusters
   - 10 directory clusters
   - 9 API-wrapper clusters
   - 7 plugin clusters
   - 5 faceless-page clusters
3. **Rounds v9–v11 then killed whatever survived as "copied quickly" or "crowded".** For a proven model, that's the expected state, not a defect.

Source: `v8_fragmentation.json`.

## Top 10 models (ranked on proven × fit for Ricardo)

**Column key:**
- **Videos (deep):** videos with any record of this model, and in brackets those with a deep, medium or brief record rather than a mention.
- **Operators:** videos where a real operator of this model reports their own revenue or sales, not a hypothetical.
- **Fit**, against the owner constraints:
  - L = no selling to local businesses
  - F = no face or personal brand
  - C = no unlawful cold outreach
  - H = ≤5 h/week of owner time with agents doing the work
  - ✓ = ok, ~ = risk, ✗ = fails

| # | Model | Videos (deep) | Operators | Revenue claims (video, when) | Startup cost | Time to first revenue | Repeatable? | Agents | Fit L/F/C/H | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Niche consumer apps and simple games** (paywall utilities, trackers, daily web/mobile games) | 52 (23) | 13 | Geosports ~$40k/mo, ~$1.2k/day ads (`s9aLA4IOSZE`, Sep 2026). Harpeggia ~$13k/mo, $150 in month 1 → $1.5k in month 2 (`axH1e2cZSrw`, Sep 2026). Voltaire vault $2–3k/day, $66 in month 1 (`NuYO7DWzlaM`, Oct 2026). AbMax ~$55k/mo, $7k in month 1 (`RypUD_Fuaqw`, Oct 2026). Wrestle AI $8k in week 1, then $15–40k/mo (`oaXnY1YExjE`, Jul 2026). Paraphrase app ~$2.6k/mo; frequency app $1k → $8–10k after a paywall change (`t9yFAJzsOkE`, Jun 2026) | ~$35–100 (Supabase $20/mo + Claude Code, `aLidq3_FwW0`) + Apple dev £79/yr [E] | Days to weeks for first $; $1k+/mo after 1–3 months in several cases | High: 13 operators, many clones of the same app types | ~70% | ✓/✓/✓/~ | **Best evidence + fit** |
| 2 | **Niche / programmatic SEO directories** (ads, featured listings, digital add-ons) | 19 (7) | 5 | 3 sites $2.3–3k/mo, untouched for 6 months; thrift directory $2–2.5k/mo for 2 years (`1fTGX4sLVqA`, May 2025). DudeRanch.com ~$50k/yr from 60 advertisers; winery directory $1–2k/mo, $10k purchase paid back in 6 months (`LZ_bjRV6xx0`, Sep 2025). "Most make ~$1k/mo, some $10k" (`SiRlIMtZygI`, Oct 2025) | <$100 build + domain (`abeY8nBzqzo`); $900–18k for premium domains | Months (SEO); not stated | High: template is identical across operators | ~75% | ~/✓/~/✓ (ads route ✓; paid listings need inbound only) | **Strong, low-cost** |
| 3 | **Faceless social video pages** (FB, YT, IG; creator payouts, ads, affiliate) | 36 (10) | 5 | Koerner's FB content $10–35k/mo profit at ~3 h/wk (`IPnafDDgj6o`, Jan 2026). 1.5M-follower FB page ~$35k/mo (`Qv-dw57pFNA`, Mar 2026). FB bonus page $3–5k/mo (`si8FhslNofc`, Apr 2025). Chloe vs History est. $8k/mo after 17M views in 3 months (`AdMZ3eW4WsA`, Jul 2026, second-hand) | AI video credits; one tester spent $1.2k (`RWmEE6ra--g`) | Not stated (weeks to months to hit payout thresholds) [E] | High: many pages, templated formats | ~65% | ✓/✓/✓/~ | **Proven, platform risk** |
| 4 | **Digital products / templates** (Etsy, Gumroad, TPT, skill bundles, playbooks) | 50 (17) | 8 | Claude Code skill bundle >$3k in 30–45 days at $99 (`quYKZushRPo`, May 2026). AI profile pictures ~$10k in 2 months (`22Jpzt683jw`, Oct 2026). Etsy printables first $1k month after 4 months; TPT store ~$2k/mo (`DG4yP9MACWk`, Oct 2026, second-hand). Drive playbook $120k in 30–45 days (`tVbN7XSPnM0`, May 2026, audience-led) | ~£0–20 [E] | Hours (with an audience) to ~4 months (Etsy) | High, but best results lean on an audience | ~75% | ✓/✓/✓/~ | Good fit, weaker without audience |
| 5 | **Self-serve micro-SaaS** (non-local subset) | 120 (61) | 6+ | CareerHound $25k last month, 8k subscribers (`xEoLsAQFnOY`, Sep 2026). Vugola/Vogola $5k in 30 days → ~$11.2k MRR (`JHz6mikOPWw` Apr, `QXxESN94Y6s` Oct 2026). Docspot ~$10k MRR within 3 months (`22Jpzt683jw`, Oct 2026). SEO bot ~$110k/mo (`SiRlIMtZygI`, Oct 2025). Post For Me $500 → $5k MRR in 8 months (`IywUW2RjXis`, Jun 2026) | $11 domain to ~$500/mo credits (`uQKVxCQJPoA`, `JHz6mikOPWw`) | Weeks to 3 months | High as a model; 31% of records sell to local businesses (excluded) | ~65% | ~/~/✓/✗ as reported | Proven, but distribution often founder-led |
| 6 | **SEO free-tool / calculator sites** | 17 (9) | 0 first-hand (5 second-hand portfolios) | Omni Calculator est. $500k+/mo, 17M visits (`Wl0NMNbYRDk`, Apr 2026). Word-unscrambler portfolio est. $5–6M/yr; a fasting calculator $400/mo (`Wvwt9CB6uKI`, Sep 2026). Thumbnail-downloader est. >$4k/mo (`GVSiAvjADBk`, May 2025). JPEG-to-PDF app ~$500/mo (`t9yFAJzsOkE`) | Domain + hosting, ~£10 [E] | Months (SEO) | High pattern, but evidence is third-party estimates | ~90% | ✓/✓/✓/✓ | Best fit, thinner proof |
| 7 | **Niche content / affiliate sites** | 18 (7) | 3 | Goat-care site $3k/mo ads, then $1k, then ~$2k (`yBj1SM4MrIQ`, Sep 2026). Recipe copycat site ~$700–800/mo (`abeY8nBzqzo`, Sep 2025). Host's niche sites $10–20k/mo by 2011 (`si8FhslNofc`) | ~$50/mo tools (`abeY8nBzqzo`) | Months | Proven historically; Google updates hit the model hard | ~70% | ✓/✓/✓/~ | Proven but decaying |
| 8 | **Online DTC / e-com / print-on-demand** (sold online, fulfilled by 3PL or POD) | 180 (72) + POD 13 (6) | 6 DTC + 1 POD | Campour Nation $40k → $120k/mo sales (`Je0NxaeOYFI`, Sep 2026). Printer Pet POD ~$1M in year 1 from a ~$40 start (`3GmZHYBX75s`, Jul 2026; 2020 events). Photo magnets $1.63M in year 1 (`N0NceZbY2_4`, Mar 2026). True Classic $100M in 2 years (`D5iCSoOL-4E`) | ~$40 (POD) to thousands (inventory) | First month (Printer Pet ~$1k, mostly friends and family) | The most proven model in the corpus (54 videos with revenue), but ops-heavy | ~55% | ✓/✓/~/✗ | Proven, poor hours fit |
| 9 | **Plugins / extensions / marketplace apps** (WordPress, Shopify, Chrome) | 18 (10) | 1 (Link Whisper, 3 videos) | Link Whisper $30k in launch month, $5–7k/mo in months 2–3, ~$90k/mo at sale, sold for $2.7M (`eVldld15cXo`, Sep 2026; `czzv3o0PCmI`, Jun 2025) | "A few thousand" for an offshore MVP (`czzv3o0PCmI`) | Month 1 (launched to an existing audience) | Pattern is common; in-corpus proof is one operator | ~70% | ✓/✓/✓/~ | Promising, single-source |
| 10 | **API / scraper wrappers** (Apify actors, niche data storefronts) | 17 (6) | 1 | Google Maps lead scraper $3.5k MRR after ~7 months at $35/mo (`50iWtrj9Mkw`, May 2026) | Near £0 (pay-per-use actors) [E] | Not stated | Templated; one operator in corpus | ~80% | ✓/✓/✓/~ | Cheap to try, thin proof |

**Below the cut:**
- **Self-publishing / KDP** (15 videos): 3 operators, but only 1 self-published and with small royalties.
- **Newsletters** (33 videos): no first-hand, dated revenue.
- **Buying a small online business** (43 videos): **0 in-corpus operators** with their own revenue. The only evidence for it is the forum research.
- **B2B data products** (29 videos): mostly proposals.
- Local, physical, agency, coaching and personal-brand models fail the constraints regardless of proof.

## Top 3 in more detail

### 1. Niche consumer apps and simple games
- **Why it's proven:** 13 different operators report their own revenue across 52 videos. The types repeat: paywalled utilities (PDF, paraphrase, frequency, vault), fitness trackers, and daily geography or sports games. Several started from $66–$150 in month 1 and reached $10k+/mo. Copying a proven app type is the stated tactic in the corpus ("clone a proven app"; a paywall change took one app from $1k to $8–10k).
- **How agents would run it:**
  - Agents mine App Store top-grossing charts and keyword data for proven app types with weak incumbents, then build in Swift or React Native or as a web game.
  - They write the store listing and do ASO, A/B-test the paywall, generate faceless short-video creatives, read analytics and ship weekly fixes.
  - Ricardo picks the app type, approves releases, and owns the developer account and any ad spend.
- **Main risk:** distribution. Most big wins rode virality, paid ads or creator networks. Organic ASO alone may stall at under $500/mo [E]. App review and privacy duties also apply.
- **≤£50 first test (plan only, spend nothing yet):**
  - Agents pick one proven utility type, for example a hard-paywall PDF or scan tool.
  - They build a **web version** with a Stripe-test paywall and a landing page.
  - Run £40 of Reddit or Meta ads (faceless creatives) over 7 days. Spend £0 on an Apple account until the test passes.
  - **Pass** if the cost per trial-start click is under £0.80 and at least 3% of visitors reach checkout. **Kill** if fewer than 1% do.

### 2. Niche / programmatic SEO directories
- **Why it's proven:** 5 operators, the same template every time: a narrow search niche, structured listings plus guides, then display ads, featured listings or a $19 PDF. Results land in the $1k–3k/mo range per site, and several sites kept earning for months to years untouched. Startup cost can be under $100.
- **How agents would run it:**
  - Agents find niches with search demand and thin incumbents, then assemble listings from public or open data with sources.
  - They generate pages and guides, and run Search Console, internal linking and refreshes.
  - Ricardo approves the niche and reviews data accuracy. Paid listings come **inbound only**, with no cold outreach, so that PECR is safe.
- **Main risk:** SEO time-to-traffic (months) and Google or AI-Overview volatility. One record already notes info sites being hit by AI snippets.
- **≤£50 first test (plan only):**
  - Buy a £10 domain and host free on Cloudflare Pages.
  - Agents build a 200–300-page directory in one niche from public data, plus one ~£40 niche backlink or listing (mirroring the $50 backlink in `1fTGX4sLVqA`).
  - **Pass** if at least 70% of pages are indexed by week 4 and there are at least 300 organic clicks/month by week 10. **Kill** if there are under 50 by week 12.

### 3. Faceless social video pages
- **Why it's proven:** 5 operators report payouts, from $3–5k/mo up to $35k/mo. Koerner reports $10–35k/mo at about 3 h/week. Formats are templated (history, explainers, "adding value" to clips, AI characters) and spread across FB, YouTube and IG.
- **How agents would run it:**
  - Agents research formats that already earn, script **original** content, and generate AI voice and visuals.
  - They post on a schedule, track retention, and double down on winners.
  - Ricardo owns the accounts and payouts, and does an editorial and IP check.
- **Main risk:** platform policy and payout changes. One page was removed over alleged IP infringement (`Qv-dw57pFNA`), and reused or AI-spam content gets demonetised. Monetisation thresholds take weeks to months.
- **≤£50 first test (plan only):**
  - Spend about £20 on AI video credits for 30 original shorts in one proven format, posted to a new FB page and YouTube channel over 3 weeks.
  - **Pass** if at least 1 post gets over 50k views and followers are growing toward the payout threshold. **Kill** if no post gets over 5k views after 30 posts.

## Were the v1–v7 playbooks and plans reviewed against this lens?

No. Recovered from `1e03f1b^`, v1–v7 produced:
- **The ranking:** 344 ideas, ranked per *specific idea* on a generic rubric (ease, value, speed, scale, realism, async fit, founder fit).
- **6 playbooks:**
  - build-first websites for local businesses
  - Apify actor wrapper + Google Maps lead scraper
  - Amazon review intelligence tool
  - AI missed-call text-back for trades
  - snail-mail story subscription
  - photo magnets at weddings and markets
- **3 plans:**
  - Bromley build-first websites
  - trades missed-call AI
  - a UK "trades tools hub" run by an agent team

Four of the six playbooks and all three plans targeted local businesses or in-person work. The later no-local and no-cold-outreach constraints ruled those out. They were never re-grouped by business model, and v8 re-mined from scratch rather than reusing them. Two of them, the Apify wrapper and the Amazon review tool, belong to model #10 here. The snail-mail subscription and photo magnets belong to #8.

## Runs and cost

| Runner | Calls | Used for |
|---|---|---|
| Codex gpt-6-luna, low effort | 8 | Labelling 1,865 records (7 batches + 1 collision fix) |
| Codex gpt-6-luna, medium effort | 15 | Per-model evidence summaries |
| Claude, pi, box | 0 | Fallbacks (Codex → Claude → pi) were wired but not needed |

**Files:**
- `models.json`: deterministic counts and claims per model
- `labels.json`
- `evidence.json`
- `v8_fragmentation.json`
- `calls.json`
- scripts in `scripts/proven_models/`
