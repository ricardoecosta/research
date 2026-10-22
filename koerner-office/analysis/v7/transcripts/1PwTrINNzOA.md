# I Told an AI Agent to Make Me Money. It Did.

- **Video:** [1PwTrINNzOA](https://www.youtube.com/watch?v=1PwTrINNzOA) · **Channel:** The Koerner Office · **Uploaded:** 2026-05-30 · **Length:** 41 min · **Transcript:** ok_freetranscriptapi
- **Speakers:** Chris Koerner (host), Brandon Doyle (guest) · **Format:** operator_interview
- **Evidence quality:** B — First-hand operator with specific figures, but self-reported, unverified, a single month, and with attribution gaps (customer count ranges 17-20, closes partly from calls). The $8K MRR comes from selling the operator's own existing agency services. · Promotional conflict: Brandon sells AI services via David AI (getdavid.ai) and uses this as a showcase; Koerner promotes Beehiiv (sponsor) and his TKO community.
- **Extraction:** claude-sonnet-5-5 · quotes verified 22/22

## Summary

Chris Koerner interviews Brandon Doyle (David AI), who used his OpenClaw AI agent ("Zach Morris", reached via iMessage) to launch three experiments over a month. A custom bedtime-story email subscription (Dreamtales) reached about $300 MRR from ~33 customers on roughly $400 of ads. An agent-built website plus postcard plus cold-call funnel for 350 Utah home-service businesses produced a claimed ~$8K MRR from about 17-20 marketing clients. A Facebook Marketplace/eBay flipping idea was dropped. The key takeaway is that agents did the build and outreach prep, while hard-to-ignore physical postcards and human closing calls drove the results.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Free agent-built websites + postcard + call funnel selling AI marketing packages** — An agent scraped 350 Utah home-service businesses, built a site for each, mailed QR-code postcards via Lob, and a human salesperson called to sell marketing packages. | agency | deep | 2/2/3/4/2 | 4 |
| I2 | **Dreamtales custom bedtime story email subscription** — A daily personalised bedtime story emailed to parents at 7pm, built and marketed largely by an AI agent. | digital_products | deep | 3/5/5/5/4 | 4 |
| I3 | **Agent-run Facebook Marketplace/eBay arbitrage** — Agent scans Marketplace for underpriced items, reserves them, and relists on eBay. | arbitrage_reselling | moderate | 4/5/1/4/3 | 4 |

### I1. Free agent-built websites + postcard + call funnel selling AI marketing packages

- **Customer:** Small local home-service businesses (landscaping, HVAC, plumbing, electrical, roofing) in Utah with no or poor websites
- **Problem:** Local service businesses have no or bad websites and are flooded with low-effort marketing pitches
- **Offer:** A free pre-built website (business info, reviews, click-to-call) if they sign up for AI-powered marketing services
- **Business model:** Monthly marketing retainers; website given free with the cheapest package
- **Pricing:** Monthly retainer packages; free website bundled with the cheapest tier. Marketing packages range (stated as $300-700) USD 300-700 per month; Biggest customers USD 1200 per month Most customers take the cheapest package (a few hundred dollars a month); average about $400/month across ~17-20 customers.
- **Acquisition:** direct_mail_postcards: Lob API postcards with a QR code to the customer's own free site; ~$1+ each, 341 of 350 delivered, claimed ~20% scanned.; cold_call: Part-time salesperson called all 350, prioritising people who scanned the QR code, pitching the cheapest package with the free site.; google_business_profile_maps: Leads (names, phones, emails, business info) scraped from Google Business/Maps listings across Utah.
- **Delivery:** Agent built the sites cheaply with Chinese models on test URLs; marketing services are delivered by David AI (AI-powered marketing); a human closes the deals.
- **Unit economics (claims):** ~$8K MRR from ~17-20 customers; Postcards ~$400 total, tokens ~$10-20; ~14 of 68 scanners closed; ~90% of closes were scanners
- **Tools:** OpenClaw, Mac Mini, Chinese LLMs, Lob, Google Maps/Business Profile, iMessage
- **Startup cost:** About $400 postcards plus $10-20 tokens plus sales rep time
- **Time to first revenue:** Within the one-month experiment
- **UK applicability [E]:** 4/5 — Postcards are legal in the UK (PECR does not cover addressed post, but UK GDPR legitimate interest and Royal Mail rules apply); sole-trader data and cold calls need TPS/CTPS screening; Lob has UK equivalents (e.g. Royal Mail-based APIs). Companies House and Google Maps data are available.
- **Risks:** Conversion data on sites vs no-site wasn't tracked; Some closes may have come from the call alone, not the postcard; Scaling risks quality of client work; Heavy reliance on human cold-calling; Single experiment, small sample
- **Automation [E]:** acquisition 2/5 (Lead scraping, site generation and postcard sending via Lob API are automated, but closing relies on human cold calls; calls to limited companies need TPS/CTPS screening.); onboarding 2/5 (Service onboarding for marketing clients likely needs human setup; not described.); delivery 3/5 (AI-powered marketing services are delivered by AI with routine checks; details not stated.); billing 4/5 (Recurring subscription billing can be automated; not described.); support 2/5 (Client communication for marketing retainers needs human involvement.)
> "it found 350 local businesses in Utah. Some of which who had websites but were bad. Some of which who had who didn't have websites." — Brandon Doyle (~27:35)
> "it worked and we have like a little over 8K a month in MR from from this experiment." — Brandon Doyle (~0:20)

### I2. Dreamtales custom bedtime story email subscription

- **Customer:** Parents (mostly moms) of young children
- **Problem:** Parents find it hard to keep inventing new bedtime stories every night
- **Offer:** Personalised story with child's name and preferences delivered to inbox daily
- **Business model:** Monthly subscription with 7-day free trial
- **Pricing:** Monthly subscription by number of kids. Starter, one kid USD 9 per month; Up to three kid profiles (planned to change to $19 for up to 4-6 kids) USD 24 per month Considering a physical book option via waitlist.
- **Acquisition:** paid_social: Facebook/Instagram ads with Meta targeting; founder's 15-20 second talking-to-camera video ad plus AI-generated image ads; ~$400 spend. The founder's own ad performed best.
- **Delivery:** AI generates stories and emails them nightly; website and system built by OpenClaw.
- **Unit economics (claims):** ~$300 MRR from ~33-34 customers; ~$400 ad spend, roughly break-even
- **Tools:** OpenClaw, Facebook/Instagram Ads, HeyGen (mentioned for avatar ads), Email delivery
- **Startup cost:** Low; domain plus about $400 ads
- **Time to first revenue:** Within about a month
- **UK applicability [E]:** 4/5 — Works in the UK; need UK GDPR/children's data care (collecting kids' names/preferences), ICO registration, and VAT on digital services.
- **Risks:** Churn as kids age out; Break-even on ads so far; Children's data/privacy; Generic AI stories may lack differentiation; Low price needs cheap CAC
- **Automation [E]:** acquisition 3/5 (Paid ads with AI creative; human-made ad performed best.); onboarding 5/5 (Self-serve signup and child profile form.); delivery 5/5 (Stories generated and emailed automatically on schedule.); billing 5/5 (Standard subscription billing.); support 4/5 (Mostly self-serve; AI can handle basic queries.)
> "we charge nine bucks a month if you have one kid" — Brandon Doyle (~23:03)
> "we have like a little over $300 in MR right now." — Brandon Doyle (~24:40)

### I3. Agent-run Facebook Marketplace/eBay arbitrage

- **Customer:** eBay/Marketplace buyers
- **Problem:** Price gaps between marketplaces
- **Offer:** Flip items such as sneakers
- **Business model:** Buy low, resell higher
- **Pricing:** Resale margin. Hypothetical buy price USD 78 per unit; Hypothetical net after eBay fees USD 103 per unit Hypothetical example by Koerner.
- **Acquisition:** marketplace_platform: Sell on eBay; source from Facebook Marketplace.
- **Delivery:** Needs a human to physically pick up and ship items.
- **Unit economics (claims):** Hypothetical $78 buy, ~$128 sale, ~$103 net
- **Tools:** OpenClaw, Facebook Marketplace, eBay, Venmo
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Facebook Marketplace and eBay exist in the UK; consumer rules and platform ToS on automation apply.
- **Risks:** Abandoned after little effort; untested; Platform ToS on bots; Physical logistics
- **Automation [E]:** acquisition 4/5 (Listing scanning and relisting can be automated.); onboarding 5/5 (No onboarding.); delivery 1/5 (Physical pickup and shipping needed.); billing 4/5 (Marketplace payments.); support 3/5 (Buyer messages handled by agent with checks.)
> "I kind of started doing it. I canned it, but I think it has potential for sure." — Brandon Doyle (~21:58)

## Revenue and metric claims (unverified claims)

- **About $8K MRR from the website/postcard experiment** (mrr, first-hand, claimant: Brandon Doyle)
  > "we have like a little over 8K a month in MR from from this experiment" — Brandon Doyle (~0:21)
- **About $300 MRR from ~33-34 bedtime-story customers** (mrr, first-hand, claimant: Brandon Doyle)
  > "we have like a little over $300 in MR right now." — Brandon Doyle (~24:40)
- **About $400 spent on ads for Dreamtales** (cost, first-hand, claimant: Brandon Doyle)
  > "we probably spent like $400 in ads" — Brandon Doyle (~24:48)
- **Roughly 20% of postcards scanned** (conversion_rate, first-hand, claimant: Brandon Doyle)
  > "I want to say it was like 20% of them scanned." — Brandon Doyle (~31:16)
- **Postcards cost a little over a dollar each** (cost, first-hand, claimant: Brandon Doyle)
  > "It was like a little more than a dollar each." — Brandon Doyle (~35:46)
- **Website token cost was a handful of cents each; total tokens about $10-20** (cost, first-hand, claimant: Brandon Doyle)
  > "Oh, like a handful of cents." — Brandon Doyle (~29:12)
- **About 17-20 unique customers behind the $8K MRR** (customers, first-hand, claimant: Brandon Doyle)
  > "Yeah, probably like 20." — Brandon Doyle (~32:54)
- **About 90% of closes came from people who scanned** (conversion_rate, first-hand, claimant: Brandon Doyle)
  > "it was like 90% scanners, 10% non-scanners." — Brandon Doyle (~32:37)
- **Marketing packages range from $300 to $700 per month** (price, first-hand, claimant: Brandon Doyle)
  > "we have packages that range from like three to 700 bucks a month on the marketing side" — Brandon Doyle (~17:53)
- **Same pitch by email would maybe close one; postcards got 17-20** (conversion_rate, second-hand, hypothetical, claimant: Chris Koerner)
  > "had you done the same pitch with the same copy to the same 350 people over email, you maybe close one, maybe." — Chris Koerner (~36:47)

## Tactics and playbook steps

**Pre-built free site + QR postcard + warm call** (acquisition)
1. Scrape Google Maps/Business listings for local service businesses
2. Have the agent build a cheap site per business from public data (use low-cost models)
3. Mail a postcard via Lob API with a QR code to their site and your contact info
4. Track scans and have a salesperson call scanners first
5. Offer the site free with the cheapest marketing package
> "as soon as we hear that they scanned for sure call on those like super hard" — Brandon Doyle (~31:31)

**Stack friction-heavy touches to stand out** (sales)
1. Combine several hard-to-fake touches (custom site, physical mail, phone calls)
2. Avoid mass email/DM that looks like bot spam
3. Consider a fourth touch such as hand delivery
> "if you compound your difficult things, compound your frictionful things, then you compound your wins" — Chris Koerner (~38:14)

**Deliver product inside existing channels (email/iMessage) instead of an app** (product)
1. Use email or messaging as the delivery vehicle
2. Avoid building another app people won't install

**Founder-led video ad on Meta with open targeting** (acquisition)
1. Record a 15-20 second talking-to-camera ad as a parent with the same problem
2. Let Meta choose targeting
3. Test AI-generated image ads alongside

**Cut token costs for bulk generation** (operations)
1. Tell the agent to keep token cost low
2. Use cheaper Chinese models
3. Host on test URLs rather than custom domains initially

## Lessons

- *offer_design*: Put the product where users already are (email, iMessage) rather than building another app.
- *automation_ai*: Agents are best at building and prep; humans still close deals and drive conversion.
- *customer_acquisition*: Doing the hard, costly thing (physical mail, personalised assets, calls) differentiates when everyone else spams email.
- *automation_ai*: Giving the agent explicit cost constraints (cheap models) made 350 sites cost cents each.
- *finance_unit_economics*: A $9/month product that breaks even on ads in month one can be fine since the revenue recurs.
- *validation_testing*: Run experiments with a clear tracking plan; missing attribution limited learning.
- *mindset_execution*: Drop low-priority experiments when others work (opportunity cost).
- *customer_acquisition*: Founder-led, human-faced creative beat AI avatar ads.
- *scaling*: Repeating experiments monthly and refining (e.g. SEO angle for sites that rank poorly) compounds learning.

## Warnings and mistakes

- Didn't track whether closes came from businesses with or without websites, so the split test was lost.
- Mass texting is non-compliant and can lead to lawsuits and fines.
- Hosting hundreds of live sites on Replit would get costly.
- Some closes may have come from calls alone, so postcard attribution is uncertain.

## Tools mentioned

OpenClaw (Agent that runs tasks and connects to models, Gmail, Drive, iMessage), Mac Mini (Always-on host for the agent), Lob (Direct mail postcard API with delivery analytics; ~$1+ per postcard), Replit (Hosting/building websites; $20/month for ~7-10 live sites), Lovable (Website builder mentioned), Facebook/Instagram Ads (Paid acquisition for bedtime stories; ~$400), HeyGen (AI avatar ads), Outscraper (Lead scraping for cold email (not used)), Beehiiv (Newsletter platform (sponsor); 30% off for 30 days), Claude, Gemini, ChatGPT, Deepseek, Qwen, Kimi (Models OpenClaw can use)
