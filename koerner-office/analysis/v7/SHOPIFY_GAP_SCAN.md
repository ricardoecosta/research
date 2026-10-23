# Shopify App Store gap scan: UK and B2B terms (v7, idea #1)

**Date:** 23 October 2026 (UK time). **Run by:** Grok Bot.

**Method:**
- Searched 40 UK and B2B terms plus 5 cross-check terms on apps.shopify.com with curl.
- Took page 1 of each search (up to 24 organic results, ads excluded). Counted an app as relevant when its name or card text matched the term.
- For each weak incumbent and its close rivals, fetched the app page: launch date, rating, review count and plan prices.
- Pulled all 1–2★ reviews and clustered them by keyword.
- Data is in `shopify_gap_scan.csv`. Raw JSON and scripts are in `shop/`.

**Gaps in the data:**
- The Shopify App Store doesn't show an app's last-update date, so the "not updated in 12+ months" test couldn't be applied. The newest 1–2★ review date is the best available proxy.
- Relevant-app counts come from page 1 only, so they are approximate.
- Every number below was fetched today. Nothing is estimated.

## Summary

**Verdict: idea #1 fails its first test as written.** None of the 40 terms meets all the pass rules:
- incumbent ≤3.8★ with ≥30 reviews;
- ≤8 relevant apps;
- ≤1 launch in the last 6 months;
- a paid tier at ≥$7.99/month;
- one complaint theme in ≥10 reviews;
- an MVP that takes ≤2 weekends.

The plan says to rerun once on WordPress.org and then drop the idea. I haven't started that rerun.

**The most important finding is that other builders are filling the gaps quickly.** The best gap by far, Royal Mail Click & Drop sync, has had four new apps in five weeks: Shipping King (17 Sep), Postbag (24 Sep), Makepost (7 Oct) and Cleatly (19 Oct 2026). Likewise, UK packaging EPR got at least three new apps between June and July 2026. One developer, New craft, shipped three UK niche apps in 2026: an EORI checker, a B2B portal and OnBuy Sync. When a gap shows up in the reviews, someone else clones it within weeks, so review mining alone no longer gives an edge.

### Top gaps worth a look (all fail at least one rule)

1. **Shopify to FreeAgent bookkeeping (strongest gap; breaks the "weak incumbent with ≥30 reviews" rule).**
   - FreeAgent shut down its own Shopify integration on 30 April 2025. Its help page now tells merchants to split bank transactions by hand (support.freeagent.com).
   - Only one app in the Shopify store serves this: Equali. It launched on 3 April 2026, costs $23–47/month and is rated 1.0 from 1 review. That review, from 22 October 2026, reports HTTP 502 errors posting settlements and no support reply for 2 days.
   - Off the store, Bridging Ledger sells this through founder calls. Its site says no third-party tool had filled the gap, and that Link My Books and A2X don't support FreeAgent.
   - So there is evidence merchants pay (about $23/month or more), supply is thin, and the cohort was orphaned by the platform's exit. That's the "painkiller for a neglected segment" pattern the plan asked for.
   - Risks:
     - accounting correctness and support load, so the MVP is likely more than 2 weekends of work;
     - the FreeAgent API partner terms haven't been checked;
     - the number of Shopify merchants using FreeAgent isn't known.
2. **Royal Mail Click & Drop order sync (most demand, but now crowded).**
   - Royal Mail's own app is rated 1.6 from 89 reviews, 75 of them 1–2★.
   - 46 of those 75 say orders stop syncing or importing, and 19 say support is slow or absent. The newest is from 13 September 2026, so the problem is current.
   - Merchants pay for the fix: Postly is $9.99–24.99/month and rated 5.0 from 19 reviews.
   - Royal Mail's public Click & Drop API makes the MVP feasible in about 2 weekends. But the API can't return labels for OLP (pay-as-you-go) accounts.
   - This fails the launches rule (4 in 6 months). Since 26 August 2025, Shopify has also sold Royal Mail labels natively, for domestic tracked services only.
   - The only differentiated corner left is international (CN22/CN23), GB to Northern Ireland under the Windsor Framework, untracked and Large Letter services, and multi-location stores (3 reviews complain that orders from every location are pulled).
3. **Low-cost Trustpilot invitations and widget (near miss).**
   - Trustpilot's own app is rated 3.4 from 35 reviews. It launched 18 February 2026, so there have been 0 launches in the last 6 months.
   - There are only 3 relevant apps, and the cheap ones cost $8.99 (Trustio) and $9.99 (Trustview).
   - A review from 30 September 2026 says Trustpilot needs a tier "between free and $1k+/year".
   - It fails because there are only 13 low reviews, and no theme reaches 10.
   - Using the Trustpilot API or its review content on a third-party app needs a ToS check.
4. **Sage Business Cloud sync (watch).**
   - Only 2 relevant apps. The Combidesk connector is rated 4.2 from 10 reviews, and 6 of those are 1★. Its newest low review is from 4 March 2025, and it costs $18/month.
   - The sample is too small to prove demand.
5. **Xero sync for price-sensitive merchants (crowded).**
   - Bold Xero Sync is rated 2.5 from 153 reviews ($19.99/month or more). Of its 91 low reviews, 46 mention price or billing and 36 mention support.
   - But there are 17 relevant apps, and A2X (4.9 from 360) and Xero Bridge (4.9 from 309) dominate. Not recommended.

### Zero-supply terms (no relevant apps, so demand is unproven)
- Companies House
- Gift Aid
- GoCardless direct debit
- HMRC MTD
- VAT number validation (only tax-exemption, 4.9 from 47)
- CN22, EORI and Brexit customs (only new apps with 0 reviews)
- WEEE and UKCA
- Royal Mail returns labels
- Parcelforce and Yodel (Parcel2Go apps with 0–1 reviews)

An empty term is not a gap unless there's evidence of payment. Only FreeAgent has that evidence (Equali and Bridging Ledger charging).

## Pass/fail by term

| Term | Relevant (p1) | Weak incumbent (≤3.8★, ≥30 rev) | Launches <6 mo | Verdict and reason |
|---|---|---|---|---|
| royal mail | 5 (8 incl. cross-checks) | Click & Drop 1.6/89 | 4 | FAIL (near miss): crowding, plus native Shopify Royal Mail labels |
| evri | 2 | none (Evri 1.0/13) | 0 | FAIL: too few reviews; native Shopify Evri labels |
| dpd uk | 4 | none (leader 4.9/113) | 0 | FAIL |
| parcelforce | 1 | none | n/c | FAIL: no demand signal |
| yodel | 1 | none | n/c | FAIL: no demand signal |
| inpost uk lockers | 3 | none | 0 | FAIL: InPost UK 1.0/1; native labels |
| uk vat invoice | 5 | none | n/c | FAIL: leaders 4.9–5.0 |
| hmrc mtd | 0 | none | n/a | FAIL: MTD lives in accounting software |
| uk vat ioss | 13 | none | n/c | FAIL |
| eori customs | 0 (+2 new) | none | 1 (Origo, Jun 2026) | FAIL: 0-review apps, no paid demand |
| cn22 customs declaration | 0 | none | n/a | FAIL |
| uk eu shipping brexit | 0 | none | n/a | FAIL |
| ddp duties uk | 8 | none (iGlobal 4.4/159) | n/c | FAIL |
| xero | 17 | Bold Xero Sync 2.5/153 | n/c | FAIL: 17 apps |
| sage accounting | 2 | none (4.2/10) | 0 | FAIL (watch) |
| freeagent | 0 (+Equali) | none | 0 (Equali 3 Apr 2026) | FAIL by rule (notable gap) |
| quickbooks uk | 16 | none | n/c | FAIL |
| b2b wholesale trade pricing | 24 | none | n/c | FAIL |
| trade account approval | 2 | none | 2 (B2B Portal May 2026, TradeAccount Jun 2026) | FAIL |
| net 30 payment terms | 2 | none | n/c | FAIL: 0-review apps |
| companies house | 0 | none | n/a | FAIL |
| business credit check | 2 | none (5.0/23) | 0 | FAIL |
| vat number validation | 0 | none | n/a | FAIL |
| gift aid | 0 | none | n/a | FAIL |
| charity donation uk | 14 | none | n/c | FAIL |
| uk returns portal | 16 | none | n/c | FAIL |
| royal mail returns label | 0 | none | n/a | FAIL |
| uk postcode address lookup | 13 | none | n/c | FAIL |
| ukca weee compliance | 0 | none | n/a | FAIL |
| EPR packaging | 0 (+5 via cross-check) | none (EAS 3.9/76) | 3 | FAIL: crowding fast |
| gpsr product safety | 10 | none | n/c | FAIL: many new 0-review apps |
| age verification uk | 20 | none | n/c | FAIL |
| klarna clearpay uk | 3 | Klarna 2.4/113 | n/c | FAIL: only Klarna can fix its own app; no paid third-party tier |
| gocardless direct debit | 0 | none | n/a | FAIL |
| amazon uk sync | 17 | none | n/c | FAIL |
| ebay uk sync | 13 | none | n/c | FAIL |
| onbuy marketplace | 2 | none (CedCommerce 4.6/78) | 1 (OnBuy Sync, Jun 2026) | FAIL |
| tiktok shop uk | 10 | none | n/c | FAIL |
| subscription cancellation (DMCC) | 21 | none | n/c | FAIL |
| trustpilot reviews uk | 3 | Trustpilot 3.4/35 | 0 | FAIL (near miss): only 13 low reviews |

Key: n/c = not checked, because the term had already failed an earlier rule. n/a = no relevant apps.

## Clusters of 1–2★ reviews (weak incumbents)

| App | Low reviews | Top complaint themes (counted by keyword) |
|---|---|---|
| Royal Mail Click & Drop | 75 | Orders stop syncing or importing: 46 · support slow or absent: 19 · not working: 15 · tracking not sent back to Shopify: 7 · pulls orders from all locations: 3 |
| Bold Xero Sync | 91 | Price or billing: 46 · support: 36 · sync failures: 25 · not working: 17 · tax errors: 7 |
| Klarna On-site Messaging | 61 | Support: 32 · not working: 20 · price: 12 |
| Trustpilot | 13 | Blank screen or install fails: ~4 · no German or Spanish invites: ~3 · too expensive: ~2 |
| Evri (Parcel2Go) | 13 | Sync: 5 · prices higher than Shopify Shipping: 4 · "just a link to the Evri website" |
| Crossborderit Duty Calculator | 15 | Price: 11 · wrong tax or duty: 6 |

## Recommendation
- Follow the plan's rule: run the WordPress.org/WooCommerce rerun once, or stop idea #1.
- If Ricardo will accept breaking the incumbent rule, the one gap worth a 1-day desk check is **Shopify to FreeAgent**. Check:
  - FreeAgent API partner terms;
  - roughly how many UK Shopify merchants use FreeAgent;
  - Equali's and Bridging Ledger's traction.

  It is a higher-effort MVP, more than 2 weekends, and comes with ongoing accounting-support load.
- Don't enter Royal Mail Click & Drop sync unless there's a clear wedge. Four clones arrived in five weeks.
