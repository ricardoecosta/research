# Playbook: Amazon review intelligence tool

**Source:** The Koerner Office — *Forget Big Apps. These Tiny Tools Are Making Millions* (`50iWtrj9Mkw`), idea 3. The report method also uses the "one-star test" from *How I Use Web Scraping to Find Products That Sell for 20x the Price* (`CKRglRCeVDM`). Transcripts: `../transcripts/raw/50iWtrj9Mkw.txt`, `../transcripts/raw/CKRglRCeVDM.txt`
**Ranking:** #7 of 227, weighted 4.00 (E4 V4 S4 Sc4 R4 A5 F3) — `../analysis/all_ideas_ranked.json`
**Template:** the outline in `../analysis/opportunity-shortlist.md` ("What to ask the playbook for"), the same structure as the other playbooks here. The original ClarityRelay manual was not found. This playbook adds §11, the automation stack and the automated proving-phase workflow, because it is one of the three ideas picked for full automation.

> **Evidence status.** This is a **suggested idea, not a case study.** The presenter describes the product and prices it but shows no customer or revenue. Its realism comes from the same video's working pattern (Nico's $3,500 MRR wrapper on a different actor). The one-star method comes from the presenter's own product research in `CKRglRCeVDM`, which is sponsored by Oxylabs.

---

## 1. ICP and buyer

- **Who (from the video):** "Every Shopify brand or Amazon seller… They all want to know what their competitors are doing. What are they complaining about? What do they love? What features are missing? What words are reviewers using?"
- **Market size (claim):** "three or four million Shopify brands" and "a few million Amazon independent sellers".
- **Pain:** "the only way to figure that out for most people is to manually read hundreds of reviews or to manually screenshot and copy and paste".
- **Buyer:** the founder or product/marketing lead. Self-serve.

## 2. Offer and pricing

| Item | Figure (claim) |
|---|---|
| Product | "Paste in a competitor's Amazon URL, your tool can scrape the last 500 reviews, run them through ChatGPT, and spit out a one-page report" |
| Report contents | "top compliments, top complaints, common phrases, suggested product improvements" |
| Price | "$19 for a one-off report", or "50 bucks a month, 100 bucks a month" |
| Cost | "pennies per report" (Apify actor + OpenAI API key) |

**UK note (not from the video):** support amazon.co.uk and the EU marketplaces from day one. Price at £15 per report and £39/month for tracked products as a starting test.

## 3. Niche-selection scorecard

The tool is general, but the ads and landing pages should target one seller segment at a time. Score each from 1 to 5:

| Criterion | What to check |
|---|---|
| Review volume | Typical top products have hundreds of reviews to analyse |
| Defect-driven complaints | Complaints cluster on fixable issues (the one-star test, §6) |
| Active private label | Many small brands launch look-alike products |
| Reachable buyers | Search terms and communities exist for the segment |

Start with a segment such as pet products, kitchen gadgets or fitness accessories.

## 4. First 30 customers

Paid search and free sample reports (§11), not cold outreach. Record for the first 30: marketplace, category, what they used the report for, and what they wanted added.

## 5. Outreach scripts (landing and ad copy)

- **Headline:** "Paste a competitor's Amazon link. Get what 500 customers love and hate about it in one page."
- **Proof block:** a free sample report on a well-known product in the segment.
- **Search ad:** "Amazon Review Analysis — Top Complaints & Fixes in 2 Min | £15 Report".
- **Hook from `CKRglRCeVDM` (presenter's method):** "If 40% of one-star reviews name the same problem, that's your product improvement."

## 6. Demo / validation workflow

- The free sample report is the demo.
- Build the **one-star test** into every report. The presenter counts negative reviews by type: "in my experience, about 40% is the magic number. If 40% of one-star reviews are mentioning the same quality control problem…" A mostly five-star product with a few one-stars is "probably a manufacturing defect, which is somewhat fixable."
- Validation test: run the five-segment, fixed-budget ad test from the same video ("test all five with a hundred bucks in ad spend each").

## 7. Delivery SOP

1. The buyer pastes a URL and pays (Stripe).
2. The back end fetches up to 500 recent reviews through the actor.
3. The LLM groups the reviews into themes, counts them (one-star test), pulls representative quotes and writes improvements.
4. A PDF/HTML report is generated and emailed, with a link to the web version.
5. Subscribers get the same report monthly per tracked product, with changes since last month.

## 8. QA / acceptance gate (per report)

- [ ] At least the minimum review count was fetched (else refund or a "thin data" warning before payment).
- [ ] Every theme has a count and at least one real quote; no invented quotes.
- [ ] Theme percentages add up and match the counts.
- [ ] Product title, ASIN and marketplace are correct on the cover.

## 9. 21-day launch plan

| Days | Action |
|---|---|
| 1–2 | Test the reviews actor on 20 products across UK/US marketplaces; check how many reviews it can return. |
| 3–6 | Build the paste-URL page, Stripe checkout, report pipeline and email delivery (§11). |
| 7 | Run the QA gate on 20 reports. Publish 5 sample reports. |
| 8–14 | Search ads at a fixed budget for five segments. One free report per email address. |
| 15–18 | Compare cost per paying customer. Keep the best two segments. |
| 19–21 | Add the monthly tracking plan if repeat buyers appear. Decide (§10). |

## 10. Metrics and kill criteria

**Track:** visits · free reports · free → paid · paid reports · subscribers · cost per paying customer · cost per report · refunds.

**Kill or rethink if** _(proposed thresholds, not from the video; set your own)_:
- after £500 of ad spend, fewer than 10 paid reports;
- the actor can't reliably fetch enough reviews on the main marketplaces;
- refunds exceed 10% of paid reports.

## 11. Automation stack and automated proving-phase workflow

**Why this idea qualifies:** the product is a pipeline: URL in, report out. The presenter's design is fully self-serve ("The backend is all handled by an API key on Apify. You're also using an OpenAI API key"). Marketing can be paid search plus sample reports, and delivery takes minutes with no human.

**Stack** (proposals unless marked):

| Job | Tool |
|---|---|
| Review data | An Apify Amazon reviews actor (video) |
| Analysis | OpenAI API (video) or another LLM, with a fixed JSON schema for themes, counts and quotes |
| Report | HTML template rendered to PDF |
| Site and payments | Vibe-coded web app with Stripe Checkout (one-off) and Billing (monthly) |
| Jobs | A worker queue that runs the actor, the LLM step and QA |
| Email | Transactional email for the report and receipts |
| Ads and SEO | Google Ads per segment; public sample-report pages for search |
| Support | An agent on the support inbox that resends reports and refunds thin-data runs within limits |

**Automated proving-phase workflow:**
1. **Seed:** an agent generates five segment landing pages, each with two sample reports on popular products.
2. **Acquire:** search campaigns run at a fixed daily cap per segment.
3. **Free report:** one free report per verified email, capped at 100 reviews.
4. **Upsell:** the free report shows the full 500-review version behind a £15 checkout.
5. **Deliver:** paid runs go through the actor, LLM, QA (§8) and email. Failed QA refunds automatically.
6. **Retain:** a follow-up email after 14 days offers monthly tracking.
7. **Decide:** a daily report ranks segments by cost per paying customer and moves budget within your cap.

**Manual work that remains:** choosing segments, setting ad caps, a spot-check of 1 in 20 reports in week one, and escalated support.

**Compliance (not from the video):** Amazon restricts automated access to its site, and actor reliability can change. Analyse and quote only short excerpts. Don't store reviewer names. State that the report is AI-generated analysis.

## Risks (from the card)

- Amazon scraping / terms of service.
- Competition.
- Report quality.
- API costs.
- No revenue shown for this exact product; it is a presenter suggestion.
