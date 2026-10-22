# How I Use Web Scraping to Find Products That Sell for 20x the Price

- **Video:** [CKRglRCeVDM](https://www.youtube.com/watch?v=CKRglRCeVDM) · **Channel:** The Koerner Office · **Uploaded:** 2026-03-10 · **Length:** 35 min · **Transcript:** transcribeyoutube
- **Speakers:** Chris Koerner (host) · **Format:** tutorial_howto
- **Evidence quality:** C — The method is demonstrated live with real scraped data, but the profit figures are rough estimates, not results from the host's own Amazon business; no first-hand FBA performance numbers are given. The video is partly promotional. · Promotional conflict: Sponsored by Oxylabs (the host promotes an affiliate link and promo code); also links to his other videos and free spreadsheet.
- **Extraction:** claude-sonnet-5-5 · quotes verified 23/23

## Summary

Chris Koerner demonstrates how to use the Oxylabs web scraper API (his sponsor) to scrape Amazon best-seller lists in three categories (pet accessories, household/health, children's education books), then analyse them in Google Sheets and Claude to find products with strong sales rank but low review counts. He then finds near-identical products on Alibaba via image search and works through landed-cost and Amazon fee maths (about 30% net margin claimed on a cat feeder). He adds extra screening tactics: one-star test, fee-tier size shrinking, variations, rating distribution, Google Trends, Amazon Choice badges. Key takeaway: pick Amazon products by data (rank vs review mismatch) rather than personal interest, but the margin maths is rough and the evidence is promotional.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Amazon FBA product arbitrage using scraped best-seller data (Alibaba sourcing)** — Scrape Amazon best-seller lists, find products with high sales rank but few reviews, source a near-identical item from Alibaba and sell it via FBA. | ecommerce_physical | deep | 3/4/1/5/4 | 4 |
| I2 | **Imported children's books and workbooks sold on Amazon** — Source generic kids' workbooks and books cheaply from Alibaba and sell them on Amazon using proven title structures. | ecommerce_physical | moderate | 3/4/1/5/4 | 3 |
| I3 | **Printables on Etsy and Amazon using title structure insights** — Use best-selling book title patterns to sell printables such as word searches, posters and coloring pages on Etsy. | digital_products | mention | 3/5/5/5/4 | 5 |

### I1. Amazon FBA product arbitrage using scraped best-seller data (Alibaba sourcing)

- **Customer:** Amazon shoppers in the chosen marketplace (US .com in the demo)
- **Problem:** Most Amazon sellers pick products by personal interest rather than data, so they enter saturated or low-margin niches.
- **Offer:** A copy or slightly improved version of an under-reviewed best-selling product (e.g. a bundled gravity-fed cat feeder and water dispenser), differentiated by colour, material or size.
- **Business model:** One-off product sales on Amazon; margin between Alibaba landed cost and Amazon price less FBA fees
- **Pricing:** Match competitor price on Amazon, or slightly under. Cat feeder Amazon price (competitor) USD 29.99 per unit; Suggested price for smaller version USD 28 per unit; Stainless paper towel holder Amazon price USD 5 per unit Leave extra margin for Amazon ads
- **Acquisition:** marketplace_platform: Amazon search ranking; seller aims to take the position of a product with few reviews. First listing image is stressed as critical; use lifestyle photos not Alibaba stock photos. Fewer returns boost ranking. Amazon ads suggested.
- **Delivery:** Order about 100 units from an Alibaba supplier and ship directly to an Amazon warehouse; Amazon FBA handles storage, fulfilment and shipping to the consumer.
- **Unit economics (claims):** Cat feeder: Alibaba about $1.50-2 per unit, shipping and tariffs about $5, landed about $7; Amazon fees $10-15 (large bulky); total cost $16-21; net profit about $9 per unit at $30, about 30% margin; Shrinking the product to drop a fee tier could save about $3 per unit; Paper towel holder sources at $0.40-1.77 and sells for $5
- **Tools:** Oxylabs Web Scraper API, Claude, Google Sheets, Alibaba (image search), Amazon FBA, Google Trends, Amazon Ads
- **Startup cost:** About $155 for a first 100-unit order of the cat feeder (excluding shipping, tariffs, FBA fees and ads)
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Amazon.co.uk and FBA UK exist, and the scraper supports other domains. Differences: UK VAT, import duties and customs, UKCA/CE product safety rules, different FBA fee tiers, and the tariff figure quoted is US-specific.
- **Risks:** Trademark and copyright infringement, especially on branded books from China; Low margins could be wiped out by fees, ads and returns; New unvetted Alibaba suppliers and quality control issues; Review-rate maths is a rough estimate; Scraping may breach Amazon terms of service; Competitors may copy again; tariffs may change
- **Automation [E]:** acquisition 3/5 (Amazon marketplace search and ads are inbound and automatable; listing creation, images and ad tuning can be agent-assisted but need checks.); onboarding 4/5 (No customer onboarding; Amazon handles the buyer relationship.); delivery 1/5 (Physical goods: sourcing, samples, supplier negotiation, QC and freight need a human, though FBA handles last-mile fulfilment. Research and scraping can be agent-run.); billing 5/5 (Amazon collects payment and pays out automatically.); support 4/5 (Amazon handles most customer service and returns; the seller occasionally handles reviews, Q&A and supplier issues.)
> "This is the single most valuable signal that most people miss." — Chris Koerner (~5:18)
> "high BSR plus low review count equals a land grab is still in progress." — Chris Koerner (~5:54)
> "Buy with data, sell with emotion." — Chris Koerner (~16:57)

### I2. Imported children's books and workbooks sold on Amazon

- **Customer:** Parents of young children buying education and learning books
- **Problem:** Demand for learning books is steady, and books are cheap to ship because they are small and light.
- **Offer:** Generic kindergarten workbooks, coloring books and similar titles with 'what it is, what it does, who it's for' titles.
- **Business model:** One-off product sales on Amazon
- **Pricing:** Match Amazon market price. Kindergarten workbook Amazon price USD 7 per unit; Alibaba cost of workbook USD 0.8 per unit A 33-book Oxford Reading Tree set shown at $167 on Amazon vs $12 on Alibaba, but trademark risk
- **Acquisition:** marketplace_platform: Amazon search; titles follow 'what it is, what it does, who it's for', lead with quantity, age-gate, and use 'learn to' prefixes.
- **Delivery:** Import from Alibaba and ship to FBA.
- **Unit economics (claims):** Workbook about $0.80 on Alibaba vs about $7 on Amazon
- **Tools:** Oxylabs, Alibaba, Claude, Google Trends
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 3/5 — Works via Amazon.co.uk, but books have no import VAT issues like other goods, though copyright and children's product safety rules apply. UK import duty/VAT apply to books differently.
- **Risks:** Counterfeit or copyright-infringing books; Quality of printing; Low price may mean thin margins
- **Automation [E]:** acquisition 3/5 (Amazon listing optimisation and ads are mostly automatable.); onboarding 4/5 (None needed.); delivery 1/5 (Physical import and freight.); billing 5/5 (Handled by Amazon.); support 4/5 (Amazon handles most support.)
> "we're not trying to violate any trademarks or copyrights. China is not exactly known for caring about trademarks or copyrights." — Chris Koerner (~31:21)

## Revenue and metric claims (unverified claims)

- **Cat feeder net profit about $9 per unit at $30 price, about 30% net margin** (margin, second-hand, hypothetical, claimant: Chris Koerner)
  > "leaving you a net profit of $9 per unit if you sell it at the same price as these other guys, which is a 30% net profit margin" — Chris Koerner (~16:25)
- **Amazon fees $10-15 per unit for large bulky item** (cost, second-hand, hypothetical, claimant: Chris Koerner)
  > "you're going to pay between $10 and $15 in Amazon fees." — Chris Koerner (~16:10)
- **Alibaba cat feeder price for 100 pieces** (cost, second-hand, hypothetical, claimant: Chris Koerner)
  > "If you order a 100 pieces, in case you're not doing the math, that's only $150 worth of product." — Chris Koerner (~14:49)
- **Product sold on Amazon at $30 sourced at about $3** (price, second-hand, claimant: Chris Koerner)
  > "I mean, this is a $3 product that's selling for $30 on Amazon." — Chris Koerner (~14:45)
- **Estimated 440,000 units sold for top cat feeder, multi-million dollar revenue (estimated from review rate)** (revenue, second-hand, hypothetical, claimant: Chris Koerner)
  > "we would have to multiply that 8,800 by 50 and we get about 440,000" — Chris Koerner (~7:28)
- **Reviewers are 1-5% of buyers** (conversion_rate, second-hand, claimant: Chris Koerner)
  > "the percentage of people that actually leave a rating or review on an Amazon product can vary between 1 and 5%." — Chris Koerner (~7:04)
- **Paper towel holder Alibaba cost $0.40-$1.77** (cost, second-hand, claimant: Chris Koerner)
  > "40 cents to $1.77 for the same item." — Chris Koerner (~22:38)
- **Shrinking the product to a lower fee tier saves about $3 per unit** (cost, second-hand, hypothetical, claimant: Chris Koerner)
  > "that could be the difference between $13 in Amazon fees and $10 in Amazon fees." — Chris Koerner (~25:50)
- **Host has ordered millions of dollars of goods from Alibaba/AliExpress over 17 years** (other, first-hand, claimant: Chris Koerner)
  > "someone that's been ordering millions of dollars worth of electronics and other items from Alibaba and AliExpress for the last 17 years." — Chris Koerner (~15:00)
- **Kids' book 33 for $12 on Alibaba vs $167 on Amazon** (price, second-hand, claimant: Chris Koerner)
  > "33 books for $12. Brand new." — Chris Koerner (~31:07)
- **Free trial gives up to 2,000 scraped results; 20% discount** (other, second-hand, claimant: Chris Koerner)
  > "you can get up to 2,000 scraped results for free." — Chris Koerner (~35:09)

## Tactics and playbook steps

**Rank vs review-count mismatch screen** (product)
1. Scrape Amazon best sellers for a category using its browse node ID (Claude can supply the IDs)
2. Export JSON, convert to CSV with Claude, paste into Google Sheets
3. Add a column dividing ratings count by best-seller rank and sort
4. Apply conditional formatting colour scale to the rating count to find outliers near the top ranks
5. Ignore items with high rank and thousands of reviews (saturated); target high rank with under about 300 reviews
> "If a product has a very good or highseller rank, but a low review count of like under 300" — Chris Koerner (~5:21)

**Use Claude to analyse screenshots of top candidates** (product)
1. Screenshot the listings and the sheet
2. Run two separate prompts: one with your hypothesis and one unbiased
3. Compare what features differentiate (bundle, simplicity, price)
4. Ask for improvement angles like better materials

**Alibaba image search sourcing and landed cost** (operations)
1. Save the Amazon product image and run Alibaba image search
2. Or scrape Alibaba with Oxylabs using a search term and sort by price and MOQ
3. Compare MOQ, supplier years in business
4. Estimate sea freight and tariffs about $4-5 per unit
5. Ship directly to Amazon warehouse
6. Check FBA fees and size tier

**Tangential category piggybacking** (product)
1. If a category is dominated by big brands, scrape an adjacent accessory category (e.g. paper towel holders)
2. Apply the same rank/review screen
3. Source the accessory from Alibaba

**One-star test and variation mining** (product)
1. Count one-star reviews by complaint type
2. If about 40% cite the same problem, fix it and sell at the same price
3. Scrape Q&A and reviews for phrases like 'I wish'
4. Ask supplier for colours, sizes or bundles requested
> "about 40% is the magic number." — Chris Koerner (~23:41)

**Fee-tier size optimisation** (pricing)
1. Check Amazon size and weight thresholds
2. Shrink product slightly to fall into a lower fee tier
3. Optionally lower price to lift conversion

**Trend and badge checks** (product)
1. Check Google Trends for the keyword over 5 years
2. Accept seasonal products if trend is up
3. Look for categories with multiple Amazon Choice badges as sign of no category leader
4. Check rating distribution shape: mostly 5-star plus few 1-star suggests fixable defect

## Lessons

- *niche_selection*: Choose products by data (demand versus competition signals) rather than personal interest.
- *niche_selection*: A saturated-looking category can still have gaps; look at demand vs supply signals and adjacent categories.
- *offer_design*: Small physical tweaks (size, weight, bundle, colour) can improve margin or conversion without a new product.
- *offer_design*: Simple products with fewer features tend to have fewer returns, which Amazon's algorithm rewards.
- *automation_ai*: Use AI to speed up analysis and spot things the operator overlooks, but test with both biased and unbiased prompts.
- *finance_unit_economics*: Seasonal businesses can still be very profitable if planned for.
- *finance_unit_economics*: Do the landed-cost and fee maths before ordering stock; margins decide viability.
- *customer_acquisition*: Listing quality (first image, real-life photos) differentiates copy products from lazy stock-photo sellers.
- *validation_testing*: Test suppliers and demand with a small first order (about 100 units) before scaling.

## Warnings and mistakes

- Avoid trademark and copyright violations when importing branded goods, especially books from China; stick to generic items.
- Check margins before importing: fees and shipping could erase profit.
- Don't rely on ratings with very small sample sizes (e.g. 6 reviews).
- Many Amazon FBA course sellers went out of business and some went to jail.
- Brand new Alibaba suppliers are unvetted; test before committing.

## Tools mentioned

Oxylabs Web Scraper API (Scrape Amazon best sellers and Alibaba results; Free trial up to 2,000 results; 20% off with code Chris (sponsor)), Claude (Find browse node IDs, convert JSON to CSV, analyse screenshots), Google Sheets (Analysis with conditional formatting), Alibaba (Supplier sourcing and image search), Amazon FBA (Fulfilment and selling), Google Trends (Trend and seasonality check), Amazon Ads (Promote products), Etsy (Marketplace for printables)
