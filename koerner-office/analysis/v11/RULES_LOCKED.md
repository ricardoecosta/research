# v11 rules (REBUILT and locked 23 Oct 2026, 23:20 BST, before harvesting)

These rules can't change mid-run. Market scope is **any country**. Ricardo is a UK-based founder, so every channel must be lawful both where he is and where the recipient is.

## Hard constraints (failing any one = kill)
1. **Run by AI agents:** at least 50% of all work automated, and at most 5 h/week of Ricardo's time. For a bought business, that's the hours after the 90-day handover.
2. **No selling to local businesses.**
3. **No face or personal brand** needed, including a brand that depends on the seller.
4. **No cold or unlawful outreach.**
5. **Software, digital or data product** that interests Ricardo.

## Track E: evidence first (build)
1. **Harvest** (no LLM). Sources:
   - HN Algolia comments and stories
   - Reddit search RSS
   - 1–2★ reviews of paid tools: Shopify App Store paid apps, WordPress.org freemium plugins, Apple App Store paid or subscription apps

   Pull everything within the **last 6 months** (since 23 Apr 2026), using fixed pain-phrase queries (`scripts/v11/harvest_evidence.py`). Store the author, date, URL and text.
2. **Label** (Codex low, batches). For each snippet, record:
   - `is_pain` (a real complaint or need)
   - `pain` (≤12 words, generic, product-agnostic)
   - `pays` (the author pays or would pay, a paid tool is named, or it's a review of a paid tool)
3. **Cluster** (Codex medium, one call). Merge pain labels into clusters. **Count without the LLM:** distinct authors per cluster within 6 months, and paying-proof snippets.
4. **Bar:** at least **30 distinct complainers in 6 months** and **at least 1 paying proof**.
   - If fewer than 5 clusters reach 30, the documented lower bar is **≥10 distinct complainers plus ≥1 paying proof**, with the actual counts reported.
   - No more than the top 40 clusters by count go to the kill-check.
5. **Kill-check** (one Codex xhigh pass with live web; a URL for every kill):
   - **K0 time-to-moat:** kill if any part fails. (a) Agents can build the asset within 3 months. (b) A rival needs at least 3 months to copy it. (c) Nobody already owns it.
   - **K1:** hard rules.
   - **K2:** a dated search for competing launches since 23 Apr 2026. Two or more is a kill.
   - **K3:** the platform owner or an official partner already serves it.
   - **K4:** 5 or more maintained incumbents at the price floor, with no wedge.
   - **K6:** the demand is dead.

## Track B: buy (main track)
1. **Harvest** (no LLM). Flippa public search for SaaS, apps and plugins priced $20k–$150k, parsed from the cards and then the listing pages (`scripts/v11/harvest_listings.py`). Dedupe against `SEEN.csv`.
2. **Checklist** (Codex medium, no web, from listing text only). This produces a table where each row is **stated / missing / looks off**. Rows:
   - **C1** verified revenue (a Flippa verification badge, Stripe connection or P&L verification)
   - **C2** revenue of at least $1k/month and profit above 0
   - **C3** price between $20k and $150k, and at most 5× annual profit
   - **C4** traffic and acquisition mostly organic, app store or marketplace, not owner outreach
   - **C5** the owner's current hours and tasks
   - **C6** no customer concentration (no customer above 20% of revenue)
   - **C7** transferability, with no seller face or brand
   - **C8** durability: no decline above 30%, no platform-ban risk
   - **C9** a plausible 90-day handover to agents ending at ≤5 h/week

   The checklist also writes **5 follow-up questions for the seller**.
3. **Pass rule (mechanical):**
   - **Hard fails:** C1, C2, C3, C7 or C9 marked "looks off", or C1 or C2 "missing".
   - **Pass:** no hard fail and at most 3 rows "missing".

   The LLM does **not** rank or pick.

## Validation (METHOD step 10)
- **Who:** E-track kill-check survivors and B-track checklist passes, at most 8 in total, with at least 4 from B if available. Claude Opus high with live web; the fallbacks are Codex xhigh, then pi, then Grok Bot.
- **Verdicts:** pursue, maybe or kill, with confidence and URLs.
- **Pursue at medium or higher requires** live, dated paid-demand evidence and a lawful channel. Track B also requires verified revenue confirmed on the listing and a credible handover plan. Track E also requires time-to-moat confirmed and copy-speed passing.
- **Every pursue or maybe gets a ≤£50 test plan:** a pre-sale page, small ad test or listing-fee page, with a channel, spend, duration and success threshold. For Track B, the plan is the first due-diligence step plus a low-cost verification. **Compounding assets are favoured**, such as curated directories or data sites where vendors pay to be listed. **Nothing is spent and nobody is contacted.**

## Shadow check
10 random kills (seed 11) are re-judged on Claude.

## Budget
- ≤4 h wall-clock (until about 03:15 BST)
- ≤100 clusters or listings into the kill-check or checklist
- Codex ≤250 calls, Claude ≤30, box ≤50, Grok Bot web checks ≤40
