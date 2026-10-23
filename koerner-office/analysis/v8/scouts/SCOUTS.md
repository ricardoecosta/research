# v8 market scouts

Run 23 Oct 2026 (UK time) by Grok Bot, following METHOD.md (MARKET SCOUTS, EFFICIENCY). This was a lean pass with no long verification loops. These are **scout records for scoring and validation, not a shortlist.**

- `scouts.jsonl`: 20 records. Fields: `id, idea, platform, source_urls, evidence, stated_problem, publish_date, observed_date, stale, stale_reason, moat_note, success_12m, agent_runnability, fit, automation_pct, rule_flags, coverage`.
- The scores are a rough first pass from the scout. They feed into step 8 scoring and the high-effort validation gate, and are not final.
- Raw data is in `raw/`:
  - Atlassian Marketplace REST dump of all 6,832 cloud apps (`atlassian_cloud.json.gz`)
  - 435 Xero UK app pages parsed from the sitemap (`xero_apps.json`)
  - Google Play GB search results for 30 UK terms, top 10 each (`gplay.json`)
  - the scripts that produced them

## Coverage

| Source | Coverage | How |
|---|---|---|
| Atlassian Marketplace | **Full** (cloud) | Public REST API: installs, rating, review count and last release for all 6,832 cloud apps, plus recent reviews for the key apps |
| Xero App Store (UK) | **Partial** | The sitemap lists 464 apps, of which 435 parsed. Search is client-rendered, so apps outside the sitemap (including some big ones) were missed |
| Google Play (GB) | **Partial** | Top 10 results for each of 30 UK terms, with rating, downloads and last-updated date |
| Gumroad | **Partial** | Search JSON for 6 UK terms |
| Product Hunt | **Partial** | WebSearch and hunted.space only |
| Indie Hackers | **Partial** | WebSearch only, plus wlad.me's verified-revenue "Boring SaaS" pages |
| Etsy, Fiverr, Upwork | **Partial** | WebSearch only. These sites block automated fetches, so no counts per keyword |
| HubSpot Marketplace, Zapier | **Partial** | WebSearch plus one community thread each |
| Shopify App Store | Carried from v7 | `SHOPIFY_GAP_SCAN.md`, 40 terms, not re-run |
| Apple App Store, Edge Add-ons / Chrome Web Store, WordPress.org | Carried from v7 | `QUIET_CORNERS.md`. Apple was cross-checked against Google Play today |
| QuickBooks App Store | **None** | Skipped to save budget. Only touched indirectly through HubSpot connector search |

## Staleness and moat rules applied

- **Staleness:** under the method, every scout record is flagged stale, because every one makes tool, price or platform-specific claims. `stale_reason` separates age-based staleness (evidence older than 18 months: SC06 Harvest, SC10 XportMyData) from platform-specific staleness, which means recheck before any decision.
- **Moat (extra-hard):** each record counts the competitors and recent launches it could see. This scan confirmed the copy pattern twice more on Atlassian:
  - Harvest for Jira: 3 apps with first releases in Sep–Oct 2026 (launch dates not confirmed).
  - InVision: after InVision shut down, 2 replacement apps were released on 22 Oct 2026.
  - These add to the v7 benchmark on Shopify, where Royal Mail Click & Drop sync drew 4 apps in about 5 weeks.

## Headline observations

1. **Orphaned installed bases are still the only quiet corners, but they get copied fast.** The pattern held on a second marketplace. On Atlassian, 18 cloud apps with at least 1,000 installs haven't shipped a release since before Oct 2024. The best orphan with no strong successor is **Google Chat for Jira Cloud**: 11,008 installs, 2.3★ from 109 reviews, last release Nov 2021, and 1★ reviews in 2026 that say it doesn't work. The three alternatives each have 406 installs or fewer.
2. **FreeAgent users keep getting left behind.** In April 2025 FreeAgent closed its Shopify integration. In Feb 2026 its staff said there is "no capacity" to add Zapier actions. Paid entrants (Equali and Bridging Ledger) are now arriving, and FreeAgent officially lists Equali, which gives Equali a distribution edge. The gap is real, but the window is narrowing.
3. **Xero's weakest big apps belong to the platforms themselves** (Stripe 2.47★ from 383, Hubdoc, PayPal). A third party can't fix those complaints, so Xero gave no quiet corner.
4. **Google Play adds demand size to the Premium Bonds idea but weakens it on Android.** NS&I's own checker has 1m+ downloads, is rated 3.6★ and was last updated in Nov 2024. Android already has a 4.1★ indie checker, so iOS-first still holds. OctoTracker is stale on both stores, but a new rival (OctoDash) is already active.
5. **UK digital templates on Gumroad have almost no supply and no ratings.** There's no evidence of demand either, and Etsy floods any winner with cheap bundles.
6. **The UK compliance launches on Product Hunt got 6 upvotes each** (AbraTax, Bridgly). Product Hunt isn't a demand channel for UK compliance.
7. **Profitable "boring" UK vertical SaaS exists:** FireCert makes about $4.5k a month from 39 subscriptions, and LolerFlow has 5 customers at £250 a month. But it sells to local trade contractors, which breaks Ricardo's rules. It's recorded with that flag.

## Records (rough scout scores, not ranked for decision)

| ID | Idea | Platform | Succ/10 | Agent/10 | Fit/10 | Auto % | Moat verdict | Rule flags |
|---|---|---|---|---|---|---|---|---|
| SC01 | MV3 replacements for orphaned Edge/Chrome MV2 extensions | Edge/Chrome | 4 | 8 | 7 | 75 | Weak; time-boxed window | — |
| SC02 | Premium Bonds checker app (iOS-first) | App Store/Play | 4 | 9 | 8 | 85 | Low; Android already served | — |
| SC03 | Octopus tariff companion (OctoTracker successor) | App Store/Play | 3 | 8 | 8 | 75 | Copying under way (OctoDash) | — |
| SC04 | FreeAgent connector layer (e-com settlements, missing actions) | Shopify/Zapier/FreeAgent | 4 | 6 | 7 | 60 | 2 entrants in ~12 months; Equali has official listing | hours (support) |
| SC05 | Google Chat for Jira Cloud replacement | Atlassian | 4 | 8 | 7 | 75 | 3 small alternatives; incumbent inertia | — |
| SC06 | Harvest for Jira replacement | Atlassian | 2 | 8 | 6 | 75 | **Fails**: 3 new in Sep–Oct 2026 | — |
| SC07 | Orphaned Atlassian integrations (pattern) | Atlassian | 3 | 8 | 7 | 75 | Fast copying (InVision) | — |
| SC08 | Better Mermaid for Confluence | Atlassian | 2 | 8 | 5 | 75 | **Fails**: 84 apps | — |
| SC09 | Stripe/PayPal→Xero fix | Xero | 2 | 6 | 5 | 60 | Not addressable | — |
| SC10 | Xero data export/archive | Xero | 2 | 8 | 6 | 80 | Unknown; thin evidence | — |
| SC11 | UK smart-meter data companion | Google Play | 3 | 6 | 7 | 65 | Data access is the barrier | automation risk |
| SC12 | Tide Times UK successor | Play/App Store | 1 | 7 | 5 | 80 | **Fails**: well served | — |
| SC13 | UK-specific digital templates | Gumroad/Etsy | 3 | 8 | 6 | 80 | None | — |
| SC14 | Productised spreadsheet/n8n automation gig | Upwork/Fiverr | 5 | 4 | 4 | 50 | Crowded | automation, hours, service |
| SC15 | UK statutory inspection/certificate SaaS | IH/wlad.me/LinkedIn | 5 | 4 | 3 | 50 | Moderate | **local trades, sales** |
| SC16 | HubSpot UK payments→Xero/QBO sync | HubSpot | 2 | 5 | 5 | 60 | **Fails**: crowded | — |
| SC17 | Companies House software accounts filing | Product Hunt/GOV.UK | 3 | 6 | 6 | 70 | Crowding pre-mandate; £5 floor | hours/liability; **date conflict 2027 vs 2028** |
| SC18 | WordPress abandoned-plugin successors (carried) | WordPress.org | 3 | 6 | 6 | 70 | Not checked | hours |
| SC19 | Gift Aid plugin for small charities (carried) | WordPress.org | 3 | 6 | 5 | 70 | Thin both ways | borderline local |
| SC20 | Royal Mail Click & Drop sync (carried benchmark) | Shopify | 2 | 7 | 6 | 70 | **Fails**: 4 in ~5 weeks | — |

## Open items for validation (do not treat as done)

- **SC05:** Check Atlassian's revenue share and Forge pricing. Read the 1★ reviews in full. Confirm Google Chat's webhook/app API terms.
- **SC04:** Check FreeAgent's API partner terms, and Equali's and Bridging Ledger's traction. The v7 recommendation of a one-day desk check still stands.
- **SC17:** Resolve whether software-only accounts filing starts in April 2027 or April 2028, using GOV.UK.
- **SC02:** The Google Play link is a search URL, because the NS&I checker's package id wasn't confirmed.
- Not counted: Etsy, Fiverr and Upwork competitor numbers (they need the browser), the QuickBooks App Store, and Xero apps missing from the sitemap.
