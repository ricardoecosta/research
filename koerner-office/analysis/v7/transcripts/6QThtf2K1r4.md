# Forget Dropshipping. This Side Hustle Is 10x Easier (and Smarter)

- **Video:** [6QThtf2K1r4](https://www.youtube.com/watch?v=6QThtf2K1r4) · **Channel:** The Koerner Office · **Uploaded:** 2025-08-17 · **Length:** 35 min · **Transcript:** ok
- **Speakers:** Chris Koerner (host), Cody Schneider (guest) · **Format:** operator_interview
- **Evidence quality:** C — Cody describes a method and past Etsy experience but gives no concrete revenue or results for the AI version; income figures are hypothetical and the creator-merch idea is brainstormed live. Little verification of Etsy policy on mass AI listings. · Promotional conflict: Chris promotes his TKOwners paid community and newsletter/podcast; Cody has a friend who owns Everbe, which he recommends.
- **Extraction:** claude-sonnet-5-5 · quotes verified 36/36

## Summary

Chris Koerner interviews Cody Schneider about AI-powered Etsy print-on-demand: use Everbe to find best-selling Etsy products, generate similar vector graphics with the ChatGPT image API, automate the pipeline with n8n (workflow JSON written by Claude/Perplexity), push to Printify and publish to Etsy for a volume game of thousands of listings. They also cover Google Shopping ads arbitrage, a comparison with dropshipping, other POD/digital product categories, and a pitch to build merch stores for creators on a 5% revenue share via cold email. Key takeaway: AI image generation removes the design bottleneck, but results are unproven and the numbers are speculative.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **AI-generated Etsy print-on-demand at scale** — Find best-selling Etsy products, generate similar AI graphics, and auto-publish thousands of print-on-demand listings via Printify to Etsy. | ecommerce_physical | deep | 4/5/4/5/3 | 4 |
| I2 | **Offensive greeting cards niche Etsy shop** — Build a shop around a trending niche such as offensive get-well-soon cards using AI graphics and print-on-demand cards. | ecommerce_physical | mention | 4/5/4/5/3 | 4 |
| I3 | **Trend discovery via Etsy market pages** — Use a Google site:etsy.com/market search filtered to past 24 hours to spot newly emerging product categories before saturation. | data_leads | moderate | 3/5/4/5/5 | 5 |
| I4 | **Google Shopping ads for proven Etsy winners** — Copy a winning Etsy product onto a Shopify store and run Google Shopping ads at a thin ROAS margin, optionally stacking card points. | ecommerce_physical | moderate | 4/5/4/5/3 | 3 |
| I5 | **Merch store builder for creators on revenue share** — Cold email creators with 'I built you a merch store', build it if they say yes, and take 5% of revenue. | agency | deep | 3/3/4/4/3 | 3 |
| I6 | **Custom personalised print and embroidery products** — Sell personalised items (laser engraving, embroidered denim jackets for bridal parties) via on-demand custom suppliers. | ecommerce_physical | mention | 3/2/3/5/2 | 4 |
| I7 | **Digital assets and printables** — Sell digital products like kids' coloring books, Excel templates and Procreate colour palettes. | digital_products | mention | 4/5/5/5/4 | 5 |
| I8 | **Selling n8n templates and POD businesses** — Automation templates and print-on-demand stores with IP and cash flow can be sold. | digital_products | mention | 3/5/5/5/3 | 5 |

### I1. AI-generated Etsy print-on-demand at scale

- **Customer:** Etsy shoppers searching for niche graphic apparel and gifts (e.g. horse sweatshirts).
- **Problem:** Creating large catalogues of designs used to need design skills or offshore illustrators; finding what sells is guesswork.
- **Offer:** Graphic apparel and merchandise (shirts, sweatshirts, mugs, stickers) with designs modelled on proven best sellers.
- **Business model:** One-off product sales via Etsy marketplace; print-on-demand supplier fulfils; margin is sale price minus production cost, Etsy fees and listing fees.
- **Pricing:** Copy the pricing structure of the winning listings.  Exact prices not stated; Etsy listing fee mentioned as roughly 20 or 30 cents.
- **Acquisition:** marketplace_platform: Rank in Etsy internal search using the same keywords in title and description as the winning listings; Etsy supplies the traffic and trust ('parasite SEO').; seo_organic_search: Etsy category pages rank on Google for generic keywords, so listings benefit from that traffic.
- **Delivery:** Printify prints and ships from its factories; pipeline: scrape winners, generate image via ChatGPT image API, remove background, upload to Printify, bulk publish to Etsy. Research and final publish are the only manual steps, though even those could be automated.
- **Unit economics (claims):** Costs are Everbe subscription, image generation cost and Etsy listing fee; Roughly 20% of products make 80% of revenue; Could make another 100k a year (hypothetical)
- **Tools:** Everbe, ChatGPT image API, n8n, Make.com, Perplexity Pro, Claude 4, Google Drive, Printify, Printful, Etsy, Apify, ScrapingBee
- **Startup cost:** Basically zero; a weekend of about 8 hours to learn
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Etsy, Printify and Printful all operate in the UK, with UK production options; need to handle VAT, UK trademark and IP rules, and Etsy policies on AI and copying listings.
- **Risks:** Copying best-selling listings invites IP and copyright complaints; Trademark takedowns on phrases can lead to shop suspension after about three strikes; Etsy may restrict mass AI-generated listings; Most listings will not sell and results are unproven; Market saturation as more people copy the method
- **Automation [E]:** acquisition 4/5 (Inbound marketplace search; agents can generate and optimise listings, with occasional human review.); onboarding 5/5 (No customer onboarding; buyers check out on Etsy.); delivery 4/5 (Printify handles production and shipping; the image pipeline is automatable, with human checks for trademark and quality.); billing 5/5 (Etsy handles payments and payouts.); support 3/5 (Order issues and messages could be agent-handled, but refunds and disputes need a human sometimes.)
> "it's basically it's doing Etsy print on demand, but using AI generated graphics" — Cody Schneider (~2:17)
> "it's just a volume game. Like you're trying to get 10,000 listings up" — Cody Schneider (~10:18)

### I3. Trend discovery via Etsy market pages

- **Customer:** Print-on-demand sellers
- **Problem:** Knowing which categories are just starting to trend
- **Offer:** A repeatable trend-spotting technique
- **Business model:** Research method feeding product choices rather than a standalone business
- **Pricing:** not applicable.  
- **Acquisition:** 
- **Delivery:** Run the Google search, review newly generated Etsy market pages, and pick categories with growing demand.
- **Unit economics (claims):** 
- **Tools:** Google Search tools, Etsy
- **Startup cost:** Free
- **Time to first revenue:** not stated
- **UK applicability [E]:** 5/5 — Works with Etsy UK pages.
- **Risks:** Some generated pages make no sense; Scraping Google at scale may breach terms
- **Automation [E]:** acquisition 3/5 (Not a business itself; could be scraped on a schedule.); onboarding 5/5 (N/A); delivery 4/5 (Agents can run the search and summarise new pages.); billing 5/5 (N/A); support 5/5 (N/A)
> "site colon etsy.commarket. You select tools on Google and then I can say show me in the past 24 hours." — Cody Schneider (~13:23)

### I4. Google Shopping ads for proven Etsy winners

- **Customer:** Google shoppers searching for the proven product keyword
- **Problem:** Organic Etsy rankings are limited; ads can scale proven winners
- **Offer:** Same print-on-demand products sold on own Shopify store
- **Business model:** Product sales via a Shopify store with paid ads; margin after ad spend
- **Pricing:** Same as Etsy winners.  Example: $1 ad spend returns $2 revenue at about 20% margin.
- **Acquisition:** paid_search: Connect Shopify to Google Shopping and bid on the winning keyword for that product.
- **Delivery:** Print-on-demand fulfilment via Printify or similar.
- **Unit economics (claims):** $1 of ads returns $2 of revenue; about 20% margin on revenue; Amex gives 4x and Chase Sapphire 3x points on ad spend
- **Tools:** Shopify, Google Shopping, Google Ads, Amex, Chase Sapphire
- **Startup cost:** Ad budget; amount not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 3/5 — Google Shopping works in the UK; Amex and Chase Sapphire points hack differs by UK card; thin margins are risky.
- **Risks:** Margins may go negative after ads; Capital at risk with ad spend; Points arbitrage is US-specific
- **Automation [E]:** acquisition 4/5 (Ad management can be largely automated with periodic human review.); onboarding 5/5 (None.); delivery 4/5 (POD supplier ships.); billing 5/5 (Shopify payments.); support 3/5 (Agents handle routine queries.)
> "it's a rorowaz game, right? So it's like I put a dollar in and maybe $2 comes out." — Cody Schneider (~21:18)

### I5. Merch store builder for creators on revenue share

- **Customer:** Content creators, especially long-form YouTubers and podcasters with large audiences who do not yet sell merch
- **Problem:** Most creators do not sell merch because of the hassle of design, store setup and logistics
- **Offer:** A fully built, managed merch store with designs based on the creator's catchphrases, run on Fourthwall or similar
- **Business model:** Revenue share of 5% of merch sales, no upfront fee
- **Pricing:** Revenue share. Revenue share  5 percent of revenue Nothing upfront
- **Acquisition:** cold_email: Scrape creator emails with Apify YouTube email scraper, validate with MillionVerifier, send via Instantly with subject line 'I built you a merch store'. If they reply yes, build and send the store.; cold_sms_dm: DM creators on Instagram as an alternative.
- **Delivery:** Analyse transcripts for recurring catchphrases, design merch around them, set up a store on Fourthwall or Shopify with a cheap domain, and manage designs and logistics. Print-on-demand partner handles production and shipping.
- **Unit economics (claims):** $15 profit per shirt example; Possible $2,000 a month per creator; Ten creators could reach about a quarter million a year (hypothetical)
- **Tools:** Fourthwall, Apify, MillionVerifier, Instantly, Shopify, Perplexity
- **Startup cost:** About $10 domain and Shopify free trial for 30 days
- **Time to first revenue:** not stated
- **UK applicability [E]:** 3/5 — Cold email to sole-trader creators breaches PECR without consent; limited-company creators are fine. Instagram DMs are also restricted. Fourthwall operates in the UK.
- **Risks:** Projections often fall far short; Creators may not respond or may build their own; PECR compliance for cold outreach; Dependency on creator's audience engagement
- **Automation [E]:** acquisition 3/5 (Cold email to creators can be automated, but many are individuals or sole traders, so UK PECR consent rules limit this.); onboarding 3/5 (Agents can build store drafts and contracts; a human approves.); delivery 4/5 (Agents analyse transcripts, generate designs and list products; print partner ships.); billing 4/5 (Platform handles payouts; revenue share reconciliation needs checks.); support 3/5 (Creator relationship needs occasional human contact.)
> "I will make a fully a fully functional store for you and all I charge is 5% of revenue. Pay me nothing upfront." — Chris Koerner (~28:06)
> "you take the transcripts of all the things that they published. You identify those phrases that are recurring" — Cody Schneider (~29:04)

## Revenue and metric claims (unverified claims)

- **Could make another 100k a year with the Etsy AI POD strategy** (revenue, second-hand, hypothetical, claimant: Cody Schneider)
  > "realistically like you could you could make another 100 grand a year doing this strategy" — Cody Schneider (~15:59)
- **Target of 10,000 Etsy listings** (other, second-hand, hypothetical, claimant: Cody Schneider)
  > "how can I get 10,000 listings on Etsy live that's you know that's what you're trying to do here" — Cody Schneider (~6:14)
- **Etsy has created about 19 million category pages** (other, second-hand, claimant: Cody Schneider)
  > "So Etsy has created 19 million of those and we have the opportunity basically to go and build products for all 19 million" — Cody Schneider (~12:40)
- **Etsy listing fee of 20 or 30 cents** (cost, first-hand, claimant: Cody Schneider)
  > "I think a Etsy listing now, I don't know if it's 20 or 30 cents, I can't remember." — Cody Schneider (~17:11)
- **20% of products make 80% of revenue** (other, second-hand, claimant: Cody Schneider)
  > "20% of your products are going to make 80% of your revenue" — Cody Schneider (~10:31)
- **Used to run 10 offshore illustrators in the Philippines producing one design a day each** (other, first-hand, claimant: Cody Schneider)
  > "So I got 10 of them working in the Philippines doing one a day." — Cody Schneider (~10:50)
- **Google Shopping example: $1 ad spend returns $2 revenue at 20% margin** (margin, second-hand, hypothetical, claimant: Cody Schneider)
  > "for every dollar I spend in ads, I get like, you know, $2 back in revenue." — Cody Schneider (~21:26)
- **Merch store example: 5% of revenue with $15 profit per shirt** (price, second-hand, hypothetical, claimant: Chris Koerner)
  > "I just need 1% one $15 profit per shirt. I get 5% of that" — Chris Koerner (~33:59)
- **A creator store might make about $2,000 a month in practice versus projections** (revenue, second-hand, hypothetical, claimant: Chris Koerner)
  > "I'm making $2,000 a month like from a cold email just from my time" — Chris Koerner (~34:10)
- **Setting up a merch store needs about a $10 domain and a 30-day free Shopify trial** (cost, second-hand, claimant: Cody Schneider)
  > "it's a $10 domain Shopify's free trial for 30 days like you don't need to spend hardly any money to do this" — Cody Schneider (~30:56)
- **Perplexity Pro costs $20 a month** (cost, second-hand, claimant: Chris Koerner)
  > "if you pay 20 bucks a month for Perplexity Pro" — Chris Koerner (~8:06)
- **Chris has 3.5 million followers** (customers, first-hand, claimant: Chris Koerner)
  > "I have three and a half million followers." — Chris Koerner (~30:32)

## Tactics and playbook steps

**Etsy winner cloning pipeline** (product)
1. Search an Etsy keyword and use Everbe to see estimated search volume, sales and revenue
2. Export top 10 winners as CSV
3. Copy their title keywords, description and pricing
4. Screenshot or scrape the image and generate a new version with the ChatGPT image API
5. Prefer simple black and white vector style to reduce errors
6. Remove the background to make a PNG
7. Upload to Printify across shirts, sweatshirts, mugs
8. Bulk select and publish to Etsy
> "We'll take those top 10 winners and then we'll go and generate, you know, graphics based off of those top 10 winners." — Cody Schneider (~5:15)

**Use an LLM to write n8n workflow JSON** (operations)
1. Prompt Perplexity Pro (Claude 4) to make an n8n JSON flow for the described workflow
2. Copy the JSON and paste it into your n8n instance
3. Adjust credentials and nodes
4. Extend the flow to Printify upload
> "I can just go and tell AI to make an NADN JSON file for the the flow that I'm trying to create." — Cody Schneider (~7:04)

**Avoid text and phrases in designs** (legal)
1. Stick to generic graphics rather than slogans
2. Check phrases for trademarks before using
3. Avoid mass takedown risk that can close the shop
> "I would stay away from words and like phrases as much as you can." — Cody Schneider (~5:25)

**Spot emerging trends via Google site search** (acquisition)
1. Search site:etsy.com/market
2. Use Tools to filter to the past 24 hours
3. Review newly created pages to find rising categories
4. Build a shop around the trend, e.g. offensive get-well cards

**Show, don't tell merch pitch to creators** (sales)
1. Analyse creator transcripts for recurring catchphrases
2. Create mockups such as a dad hat with the phrase
3. Cold email with the subject 'I built you a merch store'
4. Ask for a yes reply, then send the live store link and a revenue-share proposal
> "I think that is the going to be the differentiator is coming to them with examples." — Cody Schneider (~30:39)

**Cold email at scale stack** (acquisition)
1. Scrape creator emails with Apify YouTube email scraper
2. Validate with MillionVerifier to protect sender reputation
3. Send campaign via Instantly with the same message to all
> "you would validate that email with something called million verifier" — Cody Schneider (~32:25)

**Target long-form creators** (sales)
1. Prefer creators with long-form video or podcasts
2. Their audiences have a stronger parasocial bond and buy more merch
> "I would focus on creators that are long form too." — Cody Schneider (~34:43)

## Lessons

- *customer_acquisition*: Piggyback on marketplaces that already have traffic and trust rather than building audience from scratch.
- *validation_testing*: Use data tools to find proven demand rather than guessing, then copy the pattern.
- *scaling*: Volume strategies expect a power-law outcome: a small share of listings drive most revenue, so surface area matters.
- *automation_ai*: AI removes the human labour bottleneck in creative production, which was previously the moat.
- *automation_ai*: LLMs can write automation workflow files, making complex tools like n8n usable by non-coders.
- *finance_unit_economics*: Print-on-demand carries no inventory or sunk cost, which makes it a better business model than dropshipping and possible to sell.
- *offer_design*: Pitch with finished examples, such as a built store, rather than abstract proposals; it makes the offer easy to say yes to.
- *mindset_execution*: A first business is mostly for acquiring skills; downside is small and the learning compounds into the next venture.
- *niche_selection*: Do not get stuck on one product type; stickers, mugs, notebooks and digital goods can have better margins than apparel.
- *finance_unit_economics*: Thin-margin ad arbitrage can be amplified by credit-card rewards on ad spend, but only if volume is large.

## Warnings and mistakes

- Trademarked phrases can lead to takedown requests; around three strikes can get an Etsy shop shut down and social accounts flagged.
- Sending cold email to invalid addresses ruins sender reputation and deliverability, so validate lists first.
- Your first business statistically will probably not work; the aim is to build skills.
- Projections for creator merch deals often fall far short of expectations.
- Dropshipping from China has slow shipping, poor quality, chargebacks and heavy reliance on paid ads, and cannot be sold.

## Tools mentioned

Everbe (Etsy product research (Jungle Scout for Etsy), Chrome extension and web app; not stated), ChatGPT image API (Generate print designs; not stated), n8n (Workflow automation; not stated), Make.com (No-code automation alternative; not stated), Zapier (Original automation platform; not stated), Perplexity Pro (Generates n8n JSON using Claude 4; also lists POD companies; $20 a month), Printify (Print-on-demand fulfilment and Etsy publishing; not stated), Printful (Print-on-demand alternative; not stated), Gelato (On-demand printed cards; not stated), Fourthwall (Print-on-demand merch for creators; not stated), Apify (Scraping, including YouTube channel email scraper; not stated), ScrapingBee (Scraping images from Etsy; not stated), MillionVerifier (Email validation; not stated), Instantly (Cold email campaigns; not stated), Shopify (Store for Google Shopping ads or merch; 30-day free trial), Google Shopping / Google Ads (Paid ads for proven winners; not stated), Canva (Design graphics; not stated), Amazon Merch (Alternative marketplace for the same graphics; not stated)
