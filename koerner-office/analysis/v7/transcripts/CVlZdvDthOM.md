# How AI Makes Facebook Marketplace a Gold Mine

- **Video:** [CVlZdvDthOM](https://www.youtube.com/watch?v=CVlZdvDthOM) · **Channel:** The Koerner Office · **Uploaded:** 2026-03-26 · **Length:** 19 min · **Transcript:** transcribeyoutube
- **Speakers:** Chris Koerner (host) · **Format:** listicle_roundup
- **Evidence quality:** C — Mostly a brainstormed listicle of hypothetical ideas with a real demo of the scraper; the only big number ($600k) is second-hand. Demo is first-hand and concrete. · Promotional conflict: Says it is not sponsored by Oxylabs, but links a schema in the description and promotes Oxylabs heavily; also includes a Beehive sponsor read (ignored as an idea).
- **Extraction:** claude-sonnet-5-5 · quotes verified 30/30

## Summary

Chris Koerner pitches many ways to make money from Facebook Marketplace, then demos no-code scraping of listings with Oxylabs' AI Scraper (prompting a JSON schema, exporting CSV to Google Sheets, scheduling via Zapier). Ideas include an arbitrage sniper, deal feeds and alert tools for resellers, lead generation for local businesses, a 'gone wild' media account and niche 'radar' micro-SaaS. He also shares a second-hand story of a friend flipping sheds for $600k/yr net. Key takeaway: scrape public Marketplace data to be first on underpriced deals or sell the data/alerts to resellers and local businesses.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Facebook Marketplace arbitrage sniper** — Scrape Marketplace for underpriced or free items with terms like 'must go', 'free', 'cheap', message sellers first and resell. | arbitrage_reselling | moderate | 3/4/0/2/2 | 4 |
| I2 | **Deal feed for local resellers** — Sell resellers a daily/weekly spreadsheet or app of scraped underpriced Marketplace listings. | data_leads | moderate | 1/4/5/5/3 | 4 |
| I3 | **Cold outreach to local businesses using Marketplace** — Scrape local retail and service businesses active on Marketplace and sell them scraping/alert services via cold outreach. | b2b_service | mention | 3/3/4/5/3 | 3 |
| I4 | **Custom Marketplace alert software** — Build granular alerts Facebook lacks: notify on specific sellers, auto-message, or notify on 'wanted' posts. | saas_software | moderate | 3/4/5/5/3 | 4 |
| I5 | **Wanted-post lead generation for local service businesses** — Monitor Marketplace for 'wanted tree removal' posts and send alerts/leads to local businesses, or sell the leads. | data_leads | moderate | 3/4/5/4/3 | 3 |
| I6 | **Real estate underpriced-listing lead alerts** — Alert real estate flippers when underpriced homes matching specific criteria appear on Marketplace. | data_leads | mention | 2/4/5/4/3 | 2 |
| I7 | **Facebook Marketplace Gone Wild media account** — Scrape odd Marketplace listings and post them as a social media/media brand, like Zillow Gone Wild. | content_media | mention | 4/5/4/3/4 | 4 |
| I8 | **Niche 'radar' micro-SaaS alert sites** — Cheap per-niche alert tools (appliance radar, couch radar) pinging resellers on new listings, cloned across niches. | saas_software | moderate | 4/5/5/5/4 | 4 |
| I9 | **Used shed flipping with flatbed truck** — Friend takes unwanted sheds free from Marketplace and resells with delivery at about 4x. | arbitrage_reselling | deep | 3/3/0/2/2 | 2 |
| I10 | **Marketplace scraping tutorial with Oxylabs AI Scraper** — No-code walkthrough: scrape Marketplace search results into CSV with Oxylabs, schedule via Zapier, build an app via API. | ai_automation | deep | 3/4/5/4/3 | 4 |

### I1. Facebook Marketplace arbitrage sniper

- **Customer:** Local buyers on Facebook Marketplace
- **Problem:** Underpriced listings are snapped up quickly; manual refreshing is tedious
- **Offer:** Be first to underpriced items via scraping every 1-60 minutes, then resell, sometimes before even picking up
- **Business model:** Buy underpriced items and resell for the margin
- **Pricing:** Resale margin.  Items given free worth hundreds or thousands of dollars
- **Acquisition:** marketplace_platform: Sell on Facebook Marketplace; message sellers with a standout message ('I'm 5 minutes from you, I can come get this right now. What's your address?')
- **Delivery:** Owner scrapes, messages sellers, physically collects and resells items
- **Unit economics (claims):** People give away stuff worth hundreds or thousands of dollars daily
- **Tools:** Oxylabs AI Scraper, Facebook Marketplace
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Facebook Marketplace is used in the UK; check Meta terms of service on scraping and UK GDPR for personal data
- **Risks:** Facebook ToS on scraping; Scraping may be blocked; Competition from other flippers
- **Automation [E]:** acquisition 3/5 (Scraping and alerts are automatable; sourcing and resale listings still need a human); onboarding 4/5 (No customer onboarding; buyers are ad hoc); delivery 0/5 (Physical pickup, storage and handover of goods); billing 2/5 (Cash or bank transfers on handover, human-handled); support 2/5 (Buyer and seller chat needs a human or heavy tooling)
> "You can scrape all the results from these listings every 1 minute, 60 minute, 30 minutes, whatever you want. This will ensure you are the first buyer for underpriced stuff." — Chris Koerner (~1:44)

### I2. Deal feed for local resellers

- **Customer:** Local resellers, flippers and liquidation sellers, especially high-ticket sellers
- **Problem:** Tedious refreshing and searching to find deals
- **Offer:** Spreadsheet emailed daily/weekly or a software tool surfacing deals
- **Business model:** Subscription (spreadsheet service or software)
- **Pricing:** Monthly subscription. High-ticket seller willingness to pay USD 30-150 per month; Example tool price USD 29.99 per month Avoid low-ticket sellers (e.g. t-shirt sellers making ~$30/week)
- **Acquisition:** marketplace_platform: Find high-volume sellers on Marketplace by opening listings and seller profiles; save URLs in a Google Sheet, then reach out; facebook_groups_communities: Join reseller/flipper/liquidation Facebook groups (local or not); post about the tool you built and ask what features they'd change instead of pitching directly
- **Delivery:** Scrape with Oxylabs, deliver via Google Sheet or email, or build an app with vibe coding tools
- **Unit economics (claims):** Seller doing multiple $300 treadmills a week might pay $30-$150/month
- **Tools:** Oxylabs AI Scraper, Google Sheets, Zapier, Replit, Lovable, Lindy
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — UK has reseller communities; prices in GBP; check ToS and GDPR on scraped seller data
- **Risks:** Facebook ToS; Scraper breakage; Customers churn if deals are poor; Unsolicited DMs to sole traders limited by PECR
- **Automation [E]:** acquisition 1/5 (Finding sellers is manual; outreach to individuals or sole traders via DMs is restricted under UK PECR; Facebook group posting is manual); onboarding 4/5 (Self-serve signup or emailing a sheet); delivery 5/5 (Scheduled scraping and emailed sheets run unattended once built); billing 5/5 (Stripe subscriptions); support 3/5 (AI support with occasional human fixes when scrapers break)
> "a lot of people prefer working with data in a Google sheet or a spreadsheet. and they'd rather just be in their inbox and see that come every morning" — Chris Koerner (~2:57)

### I4. Custom Marketplace alert software

- **Customer:** Resellers and local businesses
- **Problem:** Facebook's notify-me settings only cover location, price and search term
- **Offer:** Granular alerts (high-volume sellers, filters, auto-messaging)
- **Business model:** Software subscription for business owners
- **Pricing:** Subscription.  not stated
- **Acquisition:** facebook_groups_communities: Share the tool in communities
- **Delivery:** Scheduled scrapes feeding email/SMS alerts
- **Unit economics (claims):** 
- **Tools:** Oxylabs, Zapier
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Works the same technically; auto-messaging may violate Meta rules
- **Risks:** Facebook ToS; Auto-messaging account bans
- **Automation [E]:** acquisition 3/5 (Content and community posts); onboarding 4/5 (Self-serve); delivery 5/5 (Scheduled automated alerts); billing 5/5 (Subscription); support 3/5 (Agents with human escalation)
> "What if I don't want to be notified every time something that matches my search terms are listed, but I want to automatically reach out to them" — Chris Koerner (~7:38)

### I5. Wanted-post lead generation for local service businesses

- **Customer:** Local service businesses such as tree trimmers
- **Problem:** Missing inbound requests posted on Marketplace
- **Offer:** Email/text alerts with poster contact details, or sold leads
- **Business model:** Lead sales or alert software subscription
- **Pricing:** Software fee or per lead.  not stated
- **Acquisition:** cold_email: Pitch local businesses; not specified
- **Delivery:** Automated scrape and alert by email/text
- **Unit economics (claims):** Real estate leads sell for significantly more than tree trimming leads
- **Tools:** Oxylabs, Zapier
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 3/5 — Passing on personal contact details of posters raises UK GDPR concerns
- **Risks:** Low lead volume; GDPR issues; Facebook ToS
- **Automation [E]:** acquisition 3/5 (Cold email to limited companies; calls need TPS screening); onboarding 4/5 (Configure keywords); delivery 5/5 (Automated alerts); billing 4/5 (Subscription or per-lead invoicing); support 3/5 (Agent with human check)
> "Basically, you get an email or a text that says, "Hey, Mary just posted a Facebook Marketplace wanted tree removal. Call her at this number."" — Chris Koerner (~8:13)

### I8. Niche 'radar' micro-SaaS alert sites

- **Customer:** Flippers in specific niches (appliances, exercise equipment, furniture)
- **Problem:** Manually checking Marketplace for niche deals
- **Offer:** Ping when a listing matches search term and price
- **Business model:** Low-price monthly subscription
- **Pricing:** Monthly subscription. Example tool price USD 5 per month Clone site per niche
- **Acquisition:** seo_organic_search: Niche domain names (appliance radar etc.) implied; facebook_groups_communities: Reseller groups
- **Delivery:** Automated scrape and alerts
- **Unit economics (claims):** A dozen tools each paying hundreds to thousands per month
- **Tools:** Oxylabs, Replit, Lovable
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Works in UK with local niches; check ToS
- **Risks:** Facebook ToS; Scraper breakage; Low price needs many subscribers
- **Automation [E]:** acquisition 4/5 (SEO and community content); onboarding 5/5 (Self-serve); delivery 5/5 (Scheduled scrapes); billing 5/5 (Stripe); support 4/5 (AI support)
> "it's just like a $5 a month tool that just pings people anytime something is listed in their market that fits a certain search term" — Chris Koerner (~10:55)

### I9. Used shed flipping with flatbed truck

- **Customer:** Homeowners who want a shed delivered and set up
- **Problem:** Sellers can't move heavy sheds; buyers lack flatbed trucks
- **Offer:** Free removal for sellers; delivered shed for buyers
- **Business model:** Buy for free or cheap, resell delivered
- **Pricing:** Resale. Typical shed listing (pickup) USD 500 one-off; Resale with free delivery USD 2000 one-off 
- **Acquisition:** marketplace_platform: Message sellers on day one or return weeks later; list delivered sheds on Marketplace
- **Delivery:** Flatbed truck with mini forklift; batched pickups into a route; drop at lot or deliver to pre-sold buyer
- **Unit economics (claims):** Friend nets $600,000/year
- **Tools:** Facebook Marketplace, Flatbed truck, Oxylabs AI Scraper
- **Startup cost:** Truck rental first 1-2 years, then bought truck
- **Time to first revenue:** not stated
- **UK applicability [E]:** 2/5 — Sheds are less common and smaller in UK; need waste carrier/transport licensing and a suitable vehicle; heavy-goods logistics
- **Risks:** Heavy physical labour; Vehicle costs; Second-hand claim unverified
- **Automation [E]:** acquisition 3/5 (Scraping finds listings; messaging needs a human); onboarding 3/5 (Little onboarding); delivery 0/5 (Physical moving, trucking and setup); billing 2/5 (Payment on delivery); support 2/5 (Buyer questions)
> "I have a friend in North Carolina that makes, I'm not exaggerating, $600,000 a year net profit flipping sheds" — Chris Koerner (~13:29)
> "Hey, here's that same shed for $2,000, but I'll deliver it to you for free." — Chris Koerner (~15:38)

### I10. Marketplace scraping tutorial with Oxylabs AI Scraper

- **Customer:** Non-technical entrepreneurs
- **Problem:** Manual refreshing of listings
- **Offer:** Scraper output to Google Sheet
- **Business model:** Enabling tool for other ideas; scraping-as-a-service
- **Pricing:** not stated.  
- **Acquisition:** youtube: The tutorial is content on the host's channel
- **Delivery:** Scrape in about 7 seconds, 24 listings in the demo, exported to CSV
- **Unit economics (claims):** 
- **Tools:** Oxylabs AI Studio, Zapier, Google Sheets, Replit, Lovable, Lindy
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Tools are available in the UK; ToS and GDPR checks apply
- **Risks:** Facebook ToS; Anti-bot measures
- **Automation [E]:** acquisition 3/5 (Content-driven); onboarding 4/5 (Self-serve); delivery 5/5 (Scheduled by Zapier); billing 4/5 (Subscription); support 3/5 (Agent support)
> "We're going to click scrape and parse. And wait. All right. Beautiful. That took about 7 seconds, give or take." — Chris Koerner (~17:33)

## Revenue and metric claims (unverified claims)

- **Friend nets $600,000/year flipping sheds** (profit, second-hand, claimant: Chris Koerner)
  > "makes, I'm not exaggerating, $600,000 a year net profit flipping sheds" — Chris Koerner (~13:31)
- **Shed listed ~$500 vs resold delivered at $2,000** (price, second-hand, claimant: Chris Koerner)
  > "here's that same shed for $2,000, but I'll deliver it to you for free" — Chris Koerner (~15:38)
- **Reseller selling high-ticket items might pay $30-$150/month** (price, second-hand, hypothetical, claimant: Chris Koerner)
  > "he'll probably pay $30 to $150 a month for a little tool that helps him find more deals or better deals" — Chris Koerner (~5:22)
- **Example tool price $29.99/month** (price, second-hand, hypothetical, claimant: Chris Koerner)
  > "It's only $29.99 per month. Here's what it does." — Chris Koerner (~6:16)
- **Radar tool priced at $5/month** (price, second-hand, hypothetical, claimant: Chris Koerner)
  > "it's just like a $5 a month tool" — Chris Koerner (~10:55)
- **A dozen radar tools could each pay hundreds to thousands a month** (revenue, second-hand, hypothetical, claimant: Chris Koerner)
  > "you've got a dozen tools, each paying you hundreds to thousands of dollars a month" — Chris Koerner (~11:13)
- **Side-hustle t-shirt seller makes ~$30 a week** (revenue, second-hand, hypothetical, claimant: Chris Koerner)
  > "you might be making $30 a week and you're not willing to pay $30 a month for software" — Chris Koerner (~5:08)
- **Scrape of ~7 seconds returned 24 listings** (other, first-hand, claimant: Chris Koerner)
  > "So it looks like it scraped 24 listings for me." — Chris Koerner (~18:14)
- **Oxylabs has almost 200 million residential IPs** (other, second-hand, claimant: Chris Koerner)
  > "I think they have like almost 200 million residential IP addresses that you can use." — Chris Koerner (~12:33)

## Tactics and playbook steps

**Find high-volume Marketplace sellers as customers** (acquisition)
1. Search several terms at once with commas (e.g. must go, free, cheap) within a wide radius
2. Open listings in new tabs and click each seller profile
3. Treat AI-generated-looking listings as a sign of a high-volume seller
4. Save seller URLs in a Google Sheet
5. Prioritise niches with items worth hundreds or thousands
> "start pulling up random listings in new tabs" — Chris Koerner (~3:46)

**Sell the story in Facebook reseller groups** (sales)
1. Join local or remote reseller/flipper groups
2. Post that you built a tool for yourself and explain how it works
3. Ask what they'd add or remove
4. Reply to inbound requests for access with the price
> "I just vibe coded this tool that helps me find underpriced listings on Facebook Marketplace." — Chris Koerner (~5:38)

**Stand-out first message to sellers** (sales)
1. Avoid 'Is this still available?'
2. State your distance and ability to collect now
3. Ask for the address

**Shed flip route** (operations)
1. Message sellers of free or cheap sheds on day one, or follow up weeks later
2. Offer free removal
3. Batch pickups into one route on a rented truck
4. Pre-sell at ~4x with free delivery before pickup

**No-code Oxylabs Marketplace scrape** (operations)
1. Search the term within 80 miles and copy the URL
2. Paste into Oxylabs AI Scraper, set rendering to always and format JSON
3. Define schema: listings array with title, price, location, URL, image
4. Click scrape and parse; switch to CSV and paste into Google Sheets
5. For timestamps, scrape the individual listing URL with a timestamp property
6. Schedule with Zapier 'Schedule' trigger

## Lessons

- *validation_testing*: Start small on a platform where demand and supply are visible; Marketplace provides both products and customers.
- *niche_selection*: Target customers whose margins make a $30-150/month tool a no-brainer; high-ticket sellers pay, low-ticket ones don't.
- *customer_acquisition*: Selling your story and soliciting feedback beats a direct pitch in communities.
- *offer_design*: Many customers prefer a daily emailed spreadsheet over another app login; start manual before building software.
- *niche_selection*: Platform gaps (granular alerts Facebook lacks) are product opportunities.
- *scaling*: Clone one working micro-tool across many niches to scale passive income.
- *automation_ai*: A non-coder can build with AI chat and no-code scrapers; momentum matters more than perfection.
- *mindset_execution*: Stand-out speed and outreach wins the underpriced deal when many people ping the same seller.

## Warnings and mistakes

- Check whether scraping is acceptable under Facebook's terms of service, and scrape without logging in using public data.
- Don't pitch your product directly in groups; it gets blocked or muted.
- Don't target low-ticket sellers, who can't afford software subscriptions.

## Tools mentioned

Oxylabs AI Studio (AI Scraper, Browser Agent, AI Crawler, AI Search, AI Map) (No-code scraping with built-in proxies; not stated), Facebook Marketplace (Marketplace to buy, sell and find leads), Google Sheets (View and share scraped CSV data), Zapier (Schedule scrapes and trigger notifications), Replit (Vibe coding platform to build app on Oxylabs API), Lovable (Vibe coding platform), Lindy (Vibe coding/agent platform), ChatGPT (Advice on scraper settings), Beehive (Newsletter platform (sponsor); 30% off for 30 days with code chris30)
