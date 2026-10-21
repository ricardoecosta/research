# Playbook: API arbitrage — Apify actor wrapper, launched as a niche Google Maps lead scraper

**Source:** The Koerner Office — *Forget Big Apps. These Tiny Tools Are Making Millions* (`50iWtrj9Mkw`). Transcript: `../transcripts/raw/50iWtrj9Mkw.txt`
**Ranking:** two ideas from the same video, picked together so they aren't counted twice:
- *API arbitrage / Apify actor wrapper*: #2 of 227, weighted 4.15 (E4 V4 S4 Sc5 R4 A5 F3).
- *Niche Google Maps lead scraper*: #3 of 227, weighted 4.15 (E5 V3 S5 Sc4 R4 A5 F3).

Both are in `../analysis/all_ideas_ranked.json`. The Maps scraper is used as the first actor to wrap.
**Template:** the outline in `../analysis/opportunity-shortlist.md` ("What to ask the playbook for"), the same structure as the other playbooks here. The original ClarityRelay manual was not found. This playbook adds §11, the automation stack and the automated proving-phase workflow, because it is one of the three ideas picked for full automation.

> **Evidence status.** One case, as told by the presenter: Nico, a former pasta cook with "no tech experience", wrapped a Google Maps scraper ("gyms in Texas") in a vibe-coded site with Stripe, charges "35 bucks a month" convertible into credits, and after "like 7 months" does "3500 bucks in monthly recurring revenue". "His costs are almost zero. His customer support is basically zero." Growth was word of mouth, "never done paid ads". These are not audited figures.

---

## 1. ICP and buyer

- **Who buys lead lists (from the video):** "B2B sales teams, cold callers, SDRs, marketing agencies, anyone who needs to build a list of local businesses."
- **Buyer:** the person doing outreach, often paying with their own card, so self-serve checkout fits.
- **Why they pay:** Apify has "over 30,000 actors", but "the customer doesn't know that Apify exists. If they do know it exists, it might be a little too technical for them."

## 2. Offer and pricing

| Item | Figure (claim) |
|---|---|
| Product | "Type in gyms in Texas, and then you have a spreadsheet of every gym in Texas" |
| Price | $35/month, convertible into credits that don't expire, so people "could still come back 9 months later and use the rest of their credits" |
| Alternative pricing | Per-result pricing ("1 cent per follower pulled"), "$5 per scrape in credits" |
| Margin | "like 95% profit margin" |

**UK note (not from the video):** price in pounds, e.g. £29/month or credit packs. Show the price per 100 leads, because buyers compare it with list brokers.

## 3. Niche-selection scorecard

"Nothing is too niche. The more niche you are, the better you can target your ads." Score candidates from 1 to 5:

| Criterion | What to check |
|---|---|
| Buyer is obvious | A clear group sells to this vertical (e.g. software for dentists, suppliers to roofers) |
| Data quality on Maps | Most listings have a phone, a website and reviews |
| Search intent | People search "list of [trade] in [region]" or "[trade] leads" |
| Enrichment value | You can add something cheap, e.g. email from the website or UK company status |
| Low legal risk | Business contact data only; no sensitive categories |

Video examples: dentist, roofer, gym, lawyer scrapers; also Yelp-style lists ("every roofer in Phoenix… phone, email, owner name, review count").

## 4. First 30 customers

The video's channel was LinkedIn and friends: "Post about on LinkedIn to your 452 followers. You don't need to be an influencer." For an automated launch, use paid search and a free sample instead (§11). Keep the first 30 buyers' feedback in one sheet: vertical, region, what they did with the list, and what was missing.

## 5. Outreach scripts (landing and ad copy)

- **Headline:** "Every [trade] in [region], in a spreadsheet, in 2 minutes."
- **Sub-head:** "Name, phone, website, rating and review count. £[X] for [N] leads, or £[Y]/month. Credits never expire."
- **Free sample:** "Get the first 25 free, no card." The sample is the demo.
- **Search ad:** "[Trade] Leads UK — Download a Clean List | Phone, Website, Reviews | Credits Never Expire".

## 6. Demo / validation workflow

The presenter's validation method: "Why not build five of these ideas? Test all five with a hundred bucks in ad spend each and then just run with the one that has the lowest cost per acquisition." Apply it to five verticals (or five actors) at once with the same site template.

## 7. Delivery SOP

1. User enters vertical + region and sees a count and a 10-row preview.
2. Checkout (Stripe) buys credits or a subscription.
3. The back end runs the actor, cleans and de-duplicates the rows, and writes a CSV.
4. The user downloads the CSV and gets an email link. Credits are deducted for rows actually delivered.
5. Failed or empty runs refund credits automatically.

## 8. QA / acceptance gate (per run)

- [ ] Row count matches the preview count within an agreed tolerance.
- [ ] No duplicates; phone numbers are well formed; closed businesses are removed.
- [ ] Only business contact fields are included (see compliance in §11).
- [ ] The download link works and expires as stated.

## 9. 21-day launch plan

| Days | Action |
|---|---|
| 1–2 | Pick five verticals (§3). Test the actor on each; check data quality. |
| 3–6 | Build one site template with search, preview, Stripe credits and CSV export (§11). |
| 7 | Run the QA gate on 20 test runs. Write the privacy notice and terms. |
| 8–14 | £100 (≈$100) of search ads per vertical. Free 25-lead sample on every page. |
| 15–18 | Compare cost per paying customer. Pause the worst three verticals. |
| 19–21 | Add one enrichment (e.g. UK company status) to the winner. Decide whether to continue (§10). |

## 10. Metrics and kill criteria

**Track:** visits · free samples · sample → paid conversion · cost per paying customer per vertical · credits used per customer · refunds · support emails.

**Kill or rethink if** _(proposed thresholds, not from the video; set your own)_:
- after £500 of ad spend across five verticals, there are fewer than 5 paying customers;
- the best vertical's cost per paying customer is above 3 months of revenue;
- refunds or data complaints exceed 10% of orders.

## 11. Automation stack and automated proving-phase workflow

**Why this idea qualifies:** in the source case the product is "a self-served product" with support "basically zero". Discovery can be paid search, the sale is self-serve checkout, and delivery is an API call. There is nothing to deliver by hand.

**Stack** (proposals unless marked):

| Job | Tool |
|---|---|
| Data | Apify Google Maps actor (video: "an Apify actor, an API on the back end") |
| Site | Vibe-coded web app (video: "vibecoded it into a nice, clean little website with a Stripe integration"), e.g. Next.js on Vercel |
| Accounts and credits | Supabase or similar (auth, credit ledger, run history) |
| Payments | Stripe Checkout for credit packs and subscriptions; webhooks add credits |
| Jobs | A queue or worker that calls the Apify API, polls for completion and cleans rows |
| Email | A transactional email service for receipts, download links and run alerts |
| Ads | Google Ads (search) for the five-vertical test; landing page per vertical |
| SEO pages | Generated pages per vertical × region ("Plumbers in Leeds: download the list") with real counts |
| Support | An agent on the support inbox that answers FAQs, refunds failed runs within a set limit, and escalates the rest |
| Monitoring | Daily checks of actor cost per row, error rate and margin |

**Automated proving-phase workflow:**
1. **Set up five verticals:** an agent generates a landing page per vertical from one template, with the actor configuration and a sample count.
2. **Launch ads:** search campaigns at a fixed daily budget per vertical (the video's "$100 each").
3. **Free sample:** visitors get 25 rows with no card. The run is automatic and capped by IP/email to limit abuse.
4. **Convert:** an automatic email two hours later shows how many more rows exist and links to checkout.
5. **Deliver:** paid runs go through the queue, QA (§8) and CSV export. Failed QA refunds credits.
6. **Support:** the agent handles routine questions and refunds within limits.
7. **Decide:** a daily report ranks verticals by cost per paying customer. After the test window, budgets move to the winner automatically, within a cap you set.
8. **Expand:** the same template can wrap a second actor (the video's other ideas: Instagram micro-influencer finder, Upwork freelancer finder, Yelp lists, TikTok hashtag trend report).

**Manual work that remains:** choosing verticals, setting ad caps, reviewing the daily report, and handling escalated complaints.

**Compliance (not from the video):** business listings for sole traders are personal data under UK GDPR. Sell business contact fields only, publish a privacy notice and legitimate-interest assessment, honour removal requests with a suppression list, and remind buyers that PECR still applies to how they contact the leads. Check Google Maps and Apify actor terms. If you use the Google Places API instead of scraping, check its caching and display terms.

## Risks (from the cards)

- Easy to copy; crowded; commoditised.
- Platform/API dependency (Apify actor changes, Google blocking).
- Scraping and terms risk; data accuracy.
- Low willingness to pay; support and refunds.
