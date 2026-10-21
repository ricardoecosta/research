# Playbook: Build-first websites for local businesses on a monthly subscription

**Source:** The Koerner Office — *No Money? Start This AI Website Side Hustle* (`_aGMxMmJJj4`) and *I Told an AI Agent to Make Me Money. It Did.* (`1PwTrINNzOA`). Transcripts: `../transcripts/raw/_aGMxMmJJj4.txt`, `../transcripts/raw/1PwTrINNzOA.txt`
**Ranking:** #1 of 227, weighted 4.20 (E4 V4 S4 Sc5 R4 A5 F4) — `../analysis/all_ideas_ranked.json`
**Template:** the outline in `../analysis/opportunity-shortlist.md` ("What to ask the playbook for"), the same structure as the other playbooks here. The original ClarityRelay manual was not found in the repo, on the box or in Google Drive. This playbook adds §11, the automation stack and the automated proving-phase workflow, because it is one of the three ideas picked for full automation.

> **Evidence status.** All figures are the presenter's or guest's claims. The strongest evidence is the agent experiment in `1PwTrINNzOA`: an AI agent found 350 Utah businesses, built 350 sites and made the postcards, and the experiment produced "a little over 8K a month in MRR". **A human made the closing calls in that experiment**, and the buyers paid for a marketing package of "three to 700 bucks a month" with the site included free. Whether a no-call, fully automated close works is the main thing the proving phase must test.

---

## 1. ICP and buyer

- **Who:** owner-operated local service businesses. `_aGMxMmJJj4` uses handymen ("150,000" in the US, owner's cell often on Google Maps). The `1PwTrINNzOA` agent mostly found landscaping, HVAC, plumbing, electrical and roofing businesses.
- **Buyer:** the owner. The presenter picks trades where the owner is the decision-maker, not dentists ("maybe 5% chance" of reaching them) or lawyers.
- **With or without a website?** The two sources disagree. `_aGMxMmJJj4`: "you need to find people that have a website because they realize the value of a website." `1PwTrINNzOA` targeted both ("some of which who had websites but were bad"). Treat this as a split test (§6).

## 2. Offer and pricing

| Item | Figure (claim) |
|---|---|
| Offer | A ready-made site built before contact, hosted and maintained, with booking/CRM integration |
| Price | "pay me 75 bucks a month"; operators charge "50 to 100 bucks a month" (`_aGMxMmJJj4`) |
| Alternative | Site free with the cheapest marketing package, "three to 700 bucks a month" (`1PwTrINNzOA`) |
| Build cost | "a handful of cents" per site in tokens using low-cost models (`1PwTrINNzOA`) |
| Platform cost | GoHighLevel sub-accounts; on a higher tier, unlimited sub-accounts, so each customer is "virtually pure profit" (`_aGMxMmJJj4`, GHL sponsors the video) |

**UK note (not from the video):** set the price in pounds yourself; the video gives no UK pricing. A starting point to test is £49–79/month with no setup fee.

## 3. Niche-selection scorecard

Score each trade and town from 1 to 5:

| Criterion | What to check | Video basis |
|---|---|---|
| Owner reachable | Owner's own contact on the listing | Handymen chosen for owner cell numbers |
| Budget for £50–75/month | Established, has reviews | "a business that has a budget presumably for $50 to $75 a month" |
| Search demand | "[trade] near me" trend not falling | Google Trends check in `_aGMxMmJJj4` |
| Many small operators | Single operators, not chains | Skipped a 1,500-review handyman as "too many for a single operator" |
| Template reuse | One master prompt works across the trade | "Swap out the name of the business and the location and you are good to go" |

## 4. First 30 prospects

`1PwTrINNzOA`: the agent "scraped Google business across Utah", pulling name, company, email and phone from the Google profile. For the first 30:
1. Pull one trade in one town from Google Maps (Google Places API or an Apify/Outscraper actor).
2. Keep business name, phone, website (or none), email, review count and rating.
3. **UK (not from the video):** look the business up on Companies House. Limited companies and LLPs are "corporate subscribers" under PECR and can get a cold B2B email with an opt-out; sole traders and partnerships need consent for marketing email, so reach them by post instead.
4. Keep 15 with a weak site and 15 with no site for the split test.

## 5. Outreach scripts

**What the videos did:**
- `_aGMxMmJJj4`: a personal text with a screenshot of the finished site, the owner's name and the presenter's own town "so it just adds a little more legitimacy". The presenter avoids scraping and mass texting: "there's a lot of regulations around that stuff".
- `1PwTrINNzOA`: a **postcard with a QR code** to the prospect's new site, sent through Lob's direct-mail API at "a little more than a dollar each". 341 of 350 were delivered and "like 20%" scanned. The presenter notes that mass texting "is not compliant. You will get sued".

**Postcard copy (adapted):**
> "[Business name], we built you a new website. Scan to see it. If you like it, it's yours for £[X]/month: hosting, edits and booking included. If not, ignore this and it will be deleted in 30 days."

**Email to a limited company (UK, not from the video):**
> Subject: I built [Business name] a new website
> "Hi [first name], I made this for [Business name] last week: [preview link]. It's live on a test address now. If you want it on your domain, it's £[X]/month with hosting and edits included, and you can start from the page. If not, reply 'no' and I'll take it down. [Your name, company, address, opt-out line]"

## 6. Demo / validation workflow

The demo is the prospect's own site. Each preview page carries a banner: "Built for [Business]. Claim this site for £[X]/month" with a Stripe Checkout button and a "request a change" form.

**Split tests to run:** weak site vs no site (the two videos disagree), and postcard vs email (limited companies only).

## 7. Delivery SOP

1. On payment, move the site from the preview subdomain to a live plan.
2. Send an onboarding form: domain (theirs or a new one), logo, photos, services, hours and service area.
3. Connect the domain (registrar/DNS API) and the booking calendar.
4. Apply edits from the form and send the owner a "you're live" email with the URL and how to request changes.
5. Monthly: uptime check, one content refresh and a short report (visits, form fills, bookings).

## 8. QA / acceptance gate (before a preview goes out)

- [ ] Business name, phone, town and services match the Google listing.
- [ ] No invented reviews, awards, licences, prices or years in business.
- [ ] Phone link and contact form work; the booking widget, if shown, is connected.
- [ ] The page passes a mobile layout and speed check.
- [ ] The preview banner, price and "delete in 30 days" note are visible.

## 9. 21-day launch plan

| Days | Action |
|---|---|
| 1–2 | Pick a trade and town (§3). Set up the stack (§11). Write the master prompt and one template. |
| 3–4 | Pull 100 prospects (§4) and check company status. Generate and QA 10 sites by hand to tune the template. |
| 5–7 | Generate and QA the remaining previews. Build the claim page and Stripe Checkout. |
| 8 | Send wave 1: 50 postcards (all types) and 30 emails (limited companies only). |
| 9–14 | Automated follow-ups (§11). Track scans, visits, replies and checkouts. |
| 15–18 | Onboard any buyers. Send wave 2 with the better-performing message and segment. |
| 19–21 | Review the metrics (§10). Decide whether to scale, change the offer or stop. |

## 10. Metrics and kill criteria

**Track:** previews built · postcards delivered · QR scans/visits · emails sent/opened/replied · claim-page visits · checkouts · cost per site · cost per paying customer · churn.

**Kill or rethink if** _(proposed thresholds, not from the video; set your own)_:
- after 100 previews, fewer than 10% are ever visited (the video saw ~20% scan postcards);
- after 200 previews, no one buys without a call. Then add a call step for warm visitors (as the video did) and treat the idea as semi-automated;
- the cost to acquire one paying customer is more than 4 months of revenue.

## 11. Automation stack and automated proving-phase workflow

**Why this idea qualifies:** every step except the final close was already done by an agent in `1PwTrINNzOA` (finding businesses, pulling contacts, building 350 sites, making postcards). The close can run through a self-serve claim page with Stripe. The work that is left is low-volume: approving batches and answering edge-case replies.

**Stack** (tool choices are proposals, not from the video unless marked):

| Job | Tool |
|---|---|
| Prospect data | Google Places API or an Apify/Outscraper Google Maps actor (video: Google profile data) |
| Company check (UK) | Companies House public API: company status and type, to decide email vs post |
| Site generation | A low-cost LLM filling one master template per trade (video: "Chinese models", "a handful of cents" per site) |
| Hosting | Static hosting with one preview subdomain per prospect (e.g. Cloudflare Pages or Netlify); move to GoHighLevel later if you want CRM and booking upsells |
| Direct mail | A print-and-post API (video: Lob in the US; in the UK, a UK print-and-post API such as Stannp) |
| Email | A cold-email sender with a separate domain, warm-up and opt-out handling, only for limited companies |
| Payments | Stripe Checkout and Billing (monthly subscription), Stripe webhooks |
| Onboarding and edits | A form, then an agent that applies edits and redeploys |
| Reply handling | An agent reading the outreach inbox: answers FAQs, removes opt-outs, escalates anything unusual |
| Orchestration | n8n or a small scheduled script; a Google Sheet or database as the pipeline record |

**Automated proving-phase workflow:**
1. **Find:** a scheduled job pulls N businesses for one trade and town and writes them to the pipeline table.
2. **Qualify:** an agent drops chains and businesses with very good sites, checks Companies House status, and tags each one "email" or "post".
3. **Build:** for each prospect, the LLM fills the template from the listing data. The site deploys to a preview subdomain with the claim banner.
4. **QA:** an automatic check against §8 (name/phone/town match, no invented claims, links work, mobile check). Failures are rebuilt or dropped.
5. **Approve (human, ~10 minutes a batch):** you review a sample of previews and the outgoing batch before anything is sent. This is the one deliberate manual gate.
6. **Reach:** postcards with QR codes go through the mail API; limited companies also get the §5 email.
7. **Follow up:** visits trigger one follow-up email (limited companies) on day 3 and day 7; post-only prospects get a second postcard on day 10 if they scanned but didn't buy.
8. **Close:** the owner pays on the claim page. A webhook marks the deal won and sends the onboarding form.
9. **Deliver:** the agent applies the form inputs, connects the domain and sends the "you're live" email.
10. **Clean up:** previews that were never claimed are deleted after 30 days, as promised on the card.
11. **Report:** a daily summary of funnel numbers against §10.

**Manual work that remains:** batch approval, replies the agent escalates, and DNS changes when an owner can't follow the instructions.

**Compliance (not from the video; check ICO PECR guidance before sending):** no cold texts or calls. Email only to corporate subscribers, with your identity and an opt-out. Post to sole traders. Keep a suppression list. Never put fake reviews or claims on a preview.

## Risks (from the card)

- Cold texting is restricted under UK/EU rules (PECR/GDPR); use post or compliant email.
- Commoditised offer with high churn.
- GoHighLevel lock-in (GHL sponsors `_aGMxMmJJj4`).
- Many other people copy this playbook.
- The proven close in `1PwTrINNzOA` was a human phone call; a fully automated close is unproven.
