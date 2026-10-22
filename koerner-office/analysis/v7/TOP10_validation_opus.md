# TOP10 validation (Claude Opus 5.5, low effort)

**Method and limits.** I read TOP10.md, TOP10_redteam.md and the top 35 rows of ideas_scored.csv. Because this was a low-effort pass, I did **not** run web searches, so this document has no URLs. The legal and platform points below come from my own knowledge (cutoff June 2026) and are marked "verify" where commencement dates or current rules matter. All revenue figures are creator self-reports from the transcripts.

**Scores.** S = chance of success for a solo part-timer in 12 months (1-10). A = realistic automation, as a % of all work including acquisition. F = fit for Ricardo (1-10).

---

## 1. ASO-first single-feature app portfolio — VALIDATED WITH CAVEATS
**S 5 · A 70% · F 8**

**For**
- It has the clearest unit-economics claims in the set: "12% of the people starting a free trial", "35,000 MRR", and "$2600 a month" for one app (`t9yFAJzsOkE`).
- Apple acts as merchant of record, so payments, VAT and refunds are off Ricardo's plate. The judge's onboarding, delivery and billing sub-scores are 5/5/5 (C0263).
- No outbound marketing is involved, so it carries no PECR risk.

**Against**
- Almost all of the evidence comes from one studio in one video (S=3, n_channels=2).
- Guideline 4.3 (spam) targets exactly the "many similar apps from one account" strategy.
- The keyword gaps are being mined by many AI app studios (red team; C0116 has M=1).

**Wrong or overstated in TOP10**
- "Apple handles ... refunds" is correct, but Apple's refund decisions are outside Ricardo's control.
- On the DMCC Act 2024 subscription rules, the commencement date is not settled. Verify it rather than assume.
- The 90% automation figure ignores App Review back-and-forth and creative judgment on paywalls. About 70% is more realistic.
- "Keep ~40% that earn" comes from one creator's "launch 10 to get 4 right". It is not a base rate.

**Cheapest test this week**
- Agents mine 50 search terms.
- Ship one app to App Review.
- **Pass:** the app is approved, and there are ≥3 terms where the top-5 results have fewer than 500 reviews.
- **Fail:** rejected twice, or no qualifying terms.

## 2. Niche add-ons for platform marketplaces — VALIDATED WITH CAVEATS
**S 4 · A 60% · F 9**

**For**
- It has the strongest revenue trail in the corpus: $30k launch month, then ~$90k/month, then a $2.7M exit (`eVldld15cXo`). There is also an independent second founder: "1,500 a month to 30 grand a month ... just me" (`4IETgMZy1o0`).
- Each directory is a built-in acquisition channel, and real engineering filters out low-effort competitors (C0266 M=3, the highest in the list).
- It is the best match for Ricardo's technical interest.

**Against**
- Link Whisper launched to an existing list of 10,000 people (`eVldld15cXo`), and Ricardo has no audience.
- C0106 is one channel with M=2. C0266's "200 customers ... six figures" (`vB08-7RzgOs`) is hypothetical.
- Support is 3/5 for both clusters. A bad release breaks customer sites, so releases need human sign-off.

**Wrong or overstated in TOP10**
- The automation claim of 75% is optimistic once compatibility support is counted. 60% is more realistic.
- "GPL means you sell updates and support" applies to WordPress only. Shopify and Chrome apps are not GPL-bound.
- Shopify's revenue-share terms changed recently. Verify the current threshold before modelling.

**Cheapest test this week**
- Run the review-mining test as written in TOP10.md.
- **Pass:** one unmet request appears in ≥20 one- or two-star reviews across ≥3 competitors, and Ricardo can build it in ≤2 weekends.
- **Fail:** nothing passes that bar.

## 3. UK data-led SEO directories plus an email list — VALIDATED WITH CAVEATS
**S 4 · A 75% · F 6**

**For**
- C0066 scores 77.2 and C0050 scores 77.0. Across the merged directory and content clusters there are 15 videos.
- The realistic anchor is "most of make just 1K" (`SiRlIMtZygI`).
- Data refresh is genuinely agent work.

**Against**
- C0066 is one channel, and every directory cluster has M=2.
- The model depends entirely on Google, which is hostile to scaled AI content.
- Featured-listing sales mean selling to the listed businesses, which edges towards the local-business work Ricardo ruled out.

**Wrong or overstated in TOP10**
- The pass bar of "≥50% of 200 pages indexed in 7-10 days" is unrealistic for a new domain. A slow result proves nothing, so the test generates false fails. Use an impressions-at-4-weeks bar instead.
- "Cookie consent before analytics cookies" may now be overstated. The Data (Use and Access) Act 2025 adds exemptions for some low-risk analytics cookies. Verify commencement. Ad cookies still need consent.
- PECR reg 22 also allows a "soft opt-in". That does not change the advice, which is still opt-in only.

**Cheapest test this week**
- Build one 50-100 page site from an OGL dataset.
- **Pass (at week 4):** ≥1,000 Search Console impressions and ≥20 digest signups.
- **Pass (this week):** the dataset is confirmed licensable and ≥3 search results for target queries are visibly thinner than the dataset.

## 4. UK calculator and utility portfolio — VALIDATED WITH CAVEATS (as a feeder, not stand-alone)
**S 3 · A 85% · F 6**

**For**
- Automation is genuinely high (judge 4/5/5/5/4).
- Startup cost is near zero (`Wl0NMNbYRDk`).
- There is cross-linking evidence: "half of them come from one tool to the other" (`SiRlIMtZygI`).

**Against**
- E=2.5 and M=2, and the only revenue claims come from a single founder.
- GOV.UK, banks and comparison sites own the UK head terms (stamp duty, take-home pay).
- AI Overviews answer simple sums inline.

**Wrong or overstated in TOP10**
- The examples in the concept are mostly the head-term calculators the red team said to avoid, and the "EV charging cost" and "energy-tariff comparison" examples bring in Ofgem and price-comparison issues. The pick should be long-tail only.
- A 90% automation figure with a "human signs off tax rates" step is internally inconsistent. 85% is more honest.
- This substantially overlaps with #3 (same channel, same founder).

**Cheapest test this week**
- Run the test as written in TOP10.md (5 tools).
- **Pass:** all 5 indexed and impressions on ≥2 within 14 days, not 7.
- Recommendation: run it on the #3 domain rather than as a separate business.

## 5. UK open-data alerts and APIs — VALIDATED WITH CAVEATS
**S 4 · A 80% · F 9**

**For**
- The legal path is clean: OGL data and official APIs.
- The work is highly technical and enjoyable for Ricardo.
- Delivery is fully automatable.

**Against**
- All five clusters are single-video. Three are prelim-only, with no judge score (rank 257+).
- The only real revenue story (`IywUW2RjXis`, "over 5K in eight months") is a US social-posting API. It is not UK open data.
- Tussell, Stotles and the free Contracts Finder and Find a Tender alerts already exist.

**Wrong or overstated in TOP10**
- Merging C1119 (a social-media posting API) into a "UK open-data" pick borrows its score (69.5, E=5) for something it is not evidence for.
- The combined score shown (70.8) is C0438's **prelim** score. It should not be presented alongside judge scores.
- The pass bar of "15 trials from £50 of ads" is not grounded. B2B tender keywords may cost several pounds per click (unknown), which would mean roughly 10-25 clicks for £50.

**Cheapest test this week**
- Pick one under-served niche dataset (for example FSA hygiene-rating changes, or EPC register changes for a trade).
- Agents build a working alert.
- Post it in 3 relevant communities.
- **Pass:** ≥30 email signups, ≥5 replies, and ≥1 person saying they would pay £10/month or more.

## 6. Niche job board (employer-paid) — NOT VALIDATED
**S 2 · A 60% · F 5**

**For**
- C0160 is rank 4, with E=5 across 3 channels.
- Ingestion and alerts automate well.

**Against**
- The only proven model in the evidence is seeker-paid (`xEoLsAQFnOY`), and it is unsafe to copy in the UK.
- The employer-paid version has zero first-hand evidence. Selling featured posts is B2B sales, and acquisition scores 3/5.
- Even the US model has 31% churn.

**Wrong or overstated in TOP10**
- On the 2003 Conduct Regulations: "generally prohibit seeker fees" is broadly right. Whether a passive job-listing site counts as an "employment agency" at all is a definitional question, and it is not settled in the inputs. Take legal advice before relying on either reading.
- An email open rate of ≥40% is an unreliable metric because Apple Mail Privacy Protection inflates opens. Use clicks instead.
- Many ATS feeds (Greenhouse, Lever) are public but have terms on reuse. Check the terms for each feed.

**Cheapest test this week**
- Email 20 UK employers in the niche (limited companies only, with an opt-out). Offer a £49 featured post.
- **Pass:** ≥2 employers pay.
- **Fail:** 0 pay, which means drop the idea.

## 7. Technical templates and AI skill packs — VALIDATED WITH CAVEATS (low ceiling)
**S 4 · A 75% · F 7**

**For**
- Build cost is close to zero, and a merchant of record handles VAT.
- There is a revenue claim: "$3,000 just passively" in 30-45 days at $99 (`quYKZushRPo`).
- UK-specific workflows (MTD, Xero, Companies House) give Ricardo a technical edge.

**Against**
- The $3k came from a creator who already had an audience.
- These products are trivially copied, and vendors give equivalents away free. The support sub-score is 2/5 for C0188.
- Products go stale every time a vendor API changes.

**Wrong or overstated in TOP10**
- The "n8n creator hub" as a paid sales channel is unknown and not verified. Confirm that paid templates are permitted there.
- On Consumer Contracts, the waiver-on-download point is correct.

**Cheapest test this week**
- Run the test as written in TOP10.md.
- **Pass:** ≥100 free downloads or ≥1 paid sale in 7 days. That bar is reasonable.

## 8. Website/GEO audit and monitoring SaaS — NOT VALIDATED
**S 2 · A 70% · F 5**

**For**
- It is very cheap to run: "five bucks a month" (`KtAGjnWViMQ`).
- It is self-serve.

**Against**
- There are no first-hand revenue claims in any of its clusters.
- The market is saturated (Ahrefs, Semrush and free GEO checkers), with M=2.
- Buyers can build their own version with agents.

**Wrong or overstated in TOP10**
- The pass bar of 3 paid conversions from 30 audits in 7 days implies a 10% conversion rate from cold traffic, with no source behind it.
- "C0129 is the only b2b_cold_email_ok pick" is wrong: C0080 in the CSV also carries that flag. It was excluded for other reasons.

**Cheapest test this week**
- Launch the free check for Shopify stores.
- **Pass:** ≥30 audits run and ≥1 paid conversion in 14 days.

## 9. UK-vertical micro-SaaS — VALIDATED WITH CAVEATS (slow)
**S 3 · A 50% · F 8**

**For**
- It has the broadest evidence base: 8 videos across 3 channels, S=5.
- Platform risk is low.
- UK-specific compliance (for example landlord certificates) is a real wedge against US tools.

**Against**
- Acquisition scores 2/5, and the source itself calls this the slowest route ("22 out of 25 ... lower is better", `yC0S7eYvOIc`).
- The judge says vibe-coded clones have flooded every niche.
- Automation is the lowest in the list, because Ricardo becomes a processor of business-critical data.

**Wrong or overstated in TOP10**
- The 66% automation figure is generous. About 50% is more realistic once support and security are counted.
- The landlord example will face existing UK landlord-software incumbents (their names and pricing were not verified in this pass). The Renters' Rights Act changes may be a tailwind; verify.

**Cheapest test this week**
- Run the test as written in TOP10.md.
- **Pass:** ≥25 waitlist signups or ≥2 pre-orders from £100 of ads.

## 10. Personalised children's story subscription — NOT VALIDATED
**S 2 · A 70% · F 6**

**For**
- Ricardo is the target customer.
- Delivery is easy to automate.

**Against**
- The digital version is one video at break-even: about $300 MRR after about $400 of ads (`1PwTrINNzOA`).
- The print version cost $1,000-1,500 for 10 customers (`a8qQzY3a1us`), and its delivery automation is only 2/5.
- Parents can prompt ChatGPT for free, and AI story apps are already crowded.

**Wrong or overstated in TOP10**
- On the Age Appropriate Design Code, keeping the product "parent-facing" helps. But if stories are read by or to children, the code's "likely to be accessed by children" test may still bite. Verify.
- The ICO data protection fee is right.

**Cheapest test this week**
- Run £100 of Meta ads to a landing page with a pre-order price. No product build needed.
- **Pass:** cost per signup under £5 and ≥3 pre-orders.

---

## Re-ranking

| New # | Idea | Old # |
|---|---|---|
| 1 | Platform add-ons/plugins | 2 |
| 2 | ASO app portfolio | 1 |
| 3 | UK open-data alerts/APIs | 5 |
| 4 | Data-led directories (with #4 calculators merged in as page types) | 3 + 4 |
| 5 | Technical templates/skill packs | 7 |
| 6 | UK-vertical micro-SaaS | 9 |
| 7 | Bedtime stories (wildcard) | 10 |
| 8 | Job board (employer-paid) | 6 |
| 9 | Audit/monitoring SaaS | 8 |

## Swaps
- **Drop #8 (audit/monitoring).** It has no revenue evidence and the market is saturated.
- **Merge #4 into #3.** They share a channel and a founder.
- **Candidate fill: C1094 (encrypted on-device iOS file vault, 68.0, E=5, single video).** It is a concrete, privacy-first #1-style app that needs no server data, and it is a good first app for the portfolio. It is not really a new category, though.
- **C0433 (digital waivers SaaS, 67.9) was considered and rejected.** Its buyers are local businesses.
- Nothing else in the top ~35 clears Ricardo's filters better than what is already on the list. A 9-item list is more honest than padding it to 10.

## Bottom line
Start with **plugins/add-ons (#2)**, with **UK open-data alerts (#5)** as a parallel, cheaper experiment. Plugins have the only multi-founder revenue trail, a built-in directory channel, and the most technical work. Open-data alerts are the cleanest legally and fit Ricardo's interests, and agents can build one in a weekend. Both rely on inbound acquisition, so neither has PECR exposure. Run the review-mining test and one live alert this week. Pick up the app portfolio (#1) only if one of these fails its pass bar, because App Review and 4.3 make it more of a platform gamble than its score suggests. Expect a realistic 12-month outcome in the low hundreds of pounds per month, not the creators' headline numbers: no pick has audited or UK-specific revenue evidence.
