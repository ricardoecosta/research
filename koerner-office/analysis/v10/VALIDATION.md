# v10 validation (METHOD step 10)

**Run:** 23 Oct 2026, 19:54–19:56 BST, on Claude Opus 5.5 with live WebSearch and WebFetch.

**Result: 0 pursue, 0 maybe, 3 kill.** No candidate qualified for normal validation, because all 25 kill-check survivors failed a hard rule at scoring (`SCORES.md`):
- K0, a moat under 4/10 after deep evidence, as the first rule cited: 19
- K1, automation under 50% (mostly buy-track listings needing human support or sales): 4
- K2, copy-speed: 2

As a **scorer audit**, the 3 near-misses with the highest success-then-moat scores were validated anyway, to check the scorer wasn't wrongly killing good leads. All 3 kills were confirmed.

| ID | Candidate | Track | Verdict | Confidence | One-line reason |
|---|---|---|---|---|---|
| L014 | Renewable interconnection queue intelligence | build | **kill** | medium | Distribution-level (DER) queue and feeder intelligence is already offered free by the government-backed LBNL/i2X DER dashboard and Interconnection.fyi, and by paid tools: MeanderX (20+ utilities in 8 states), FeederIQ ($99/month), Paces, LandGate and Enverus. The inputs are public and no revenue evidence exists, so the moat is not confirmed and nothing is left to wedge into. |
| L030 | EU VAT compliance change and transition tracker | build | **kill** | high | This fails K2: a live re-check found three competing launches since 23 Apr 2026 (Fonoa Knowledge in Jul 2026, VAT Guard on 27 Jul 2026, VatForge on 1 Sep 2026). It also fails K3, because Shopify Tax already monitors EU VAT liabilities inside the platform, and the moat is not yet shown. |
| L058 | European facilities management SaaS | buy | **kill** | medium | The price looks fair on paper (about 3.35× claimed profit), but this is a French public-sector CMMS with 80–90 institutional clients, and it fails the ≤5 h/week, ≥50%-automated rule (K1/B4): owner hours aren't disclosed, the 91% margin suggests the owner's own work isn't counted as a cost, and renewals go through French public tenders. |

## L014 Renewable interconnection queue intelligence: kill (medium)

Distribution-level (DER) queue and feeder intelligence is already offered free by the government-backed LBNL/i2X DER dashboard and Interconnection.fyi, and by paid tools: MeanderX (20+ utilities in 8 states), FeederIQ ($99/month), Paces, LandGate and Enverus. The inputs are public and no revenue evidence exists, so the moat is not confirmed and nothing is left to wedge into.

**Why**

- K2 re-check corrects the earlier finding. MeanderX launched in Ameren Illinois territory in 2025 ('launched the platform last year'), before the window, so it is not a launch inside the window. The USTA index (9 Jul 2026) covers only six ISOs and RTOs at transmission level, and its article says utilities outside them are 'simply not represented', so it is not a direct match. That leaves at most one launch in the window, so K2 alone would not kill. https://now.solar/2026/05/27/this-ai-tool-helps-community-solar-developers-connect-to-the-grid-sooner-canary-media/ ; https://ustechautomations.com/resources/blog/us-interconnection-queue-index-july-2026
- K3/K4: there is a free public option backed by government. LBNL/i2X runs a Distributed Energy Projects Interconnection Dashboard (distributedinterconnection.lbl.gov) on 2.7M+ DER applications gathered from utilities and state PUCs. It also feeds Interconnection.fyi. https://eta-publications.lbl.gov/sites/default/files/2026-09/der_interconnection_timelines_and_costs_2026_final_main_report.pdf
- Interconnection.fyi (GridTracker) is free. It tracks 44,281 queue requests across '50+ ISOs and utilities', includes a distribution grid (DG) queue section, and sells CSV and Snowflake exports. https://www.interconnection.fyi/
- MeanderX already covers the feeder-level niche across 'more than 20 investor-owned utilities across eight states' (ConEd, Xcel, Potomac Edison, plus parts of NJ, DE and DC), using AI that scrapes and updates utility data automatically. That is the same agent-run approach this lead proposes, which removes the 'underserved territory' wedge. https://now.solar/2026/05/27/this-ai-tool-helps-community-solar-developers-connect-to-the-grid-sooner-canary-media/ ; https://cloud.google.com/customers/meanderx?hl=en
- K0 fails strictly. The data is public utility and PUC disclosure, and DOE's target is for every state to publish detailed, current queue data. Copying it takes weeks with AI scraping, which is exactly what MeanderX shows. No network effect, and switching costs are low because exports exist. https://www.energy.gov/sites/default/files/2025-01/i2X%20DER%20Interconnection%20Roadmap.pdf ; https://dps.ny.gov/distributed-generation-information
- No payment evidence dated within 18 months. The FeederIQ press kit names no customers and gives no subscriber count. https://feederiq.com/press/

| Competitor | Price | Launched | URL |
|---|---|---|---|
| LBNL/i2X DER Interconnection Dashboard | free | 2026 (cited in the Sep 2026 LBNL report; exact launch date unverified) | https://eta-publications.lbl.gov/sites/default/files/2026-09/der_interconnection_timelines_and_costs_2026_final_main_report.pdf |
| Interconnection.fyi / GridTracker | free; paid exports with no public price | before 2025 (exact date unverified) | https://www.interconnection.fyi/ |
| MeanderX | not public | 2025 (Ameren IL); 20+ IOUs in 8 states by May 2026 | https://now.solar/2026/05/27/this-ai-tool-helps-community-solar-developers-connect-to-the-grid-sooner-canary-media/ |
| FeederIQ | $99/month Pro, from the earlier pass; page is rendered by JavaScript so the price is unverified on re-fetch | unverified; covers Xcel MN/CO | https://feederiq.com/press/ |
| USTA Interconnection Queue Index | free index; $175/month weekly change feed | 9 Jul 2026 (ISO/transmission level only) | https://ustechautomations.com/resources/blog/us-interconnection-queue-index-july-2026 |
| Grid Status queue app | Enterprise, no public price (pricing page returned 403) | 4 Feb 2026 | https://docs.gridstatus.io/changelog/february-2026/4-february-release-interconnection-queues-application |
| Enverus Interconnection Queue Outlook / platform | enterprise, not public | Outlook 2026 released Feb 2026 | https://www.enverus.com/newsroom/enverus-releases2026-interconnection-queue-outlook/ |
| LandGate / Paces | not public | established | https://www.landgate.com/landgate-vs-paces |

**Demand:** The need is real but already served. LBNL counts about 8,200 active transmission-queue projects at end-2025 and 2.7M+ DER applications, and community solar is moving into new state markets. Willingness to pay in this niche is unverified: no revenue, customer counts or paid conversions were found for any feeder-level product. https://emp.lbl.gov/queues ; https://www.solarpowerworldonline.com/wp-content/uploads/2026/04/CommunitySolarOutlookH12026_executivesumary.pdf

**Channel:** Lawful inbound channels exist: SEO feeder/utility pages, paid search, and industry newsletters. Free Interconnection.fyi pages and LBNL already rank for the same queries, which weakens SEO. https://www.interconnection.fyi/

**Owner hours:** Estimated at 4–5 h/week at steady state, unverified. Onboarding a new territory and QA on source changes would likely exceed 5 h/week at first.

**Desk check run:** I ran a competitor-gap check (live web) to see whether any underserved distribution-queue territory and wedge remains. Result: LBNL/i2X aggregates DER queues nationally for free, Interconnection.fyi publishes DG queues for free, and MeanderX already covers 20+ IOUs across 8 states with AI scraping. I found no territory or data asset that would take a competitor months to copy, so K0 kills.

**Unverified:**
- FeederIQ $99/month price (page renders by JavaScript; not re-confirmed)
- MeanderX pricing and customer count
- Grid Status queue pricing (403)
- Launch date of the LBNL/i2X DER dashboard
- Utility data redistribution licence terms
- Any paying-customer evidence in the niche
- Owner hours estimate

## L030 EU VAT compliance change and transition tracker: kill (high)

This fails K2: a live re-check found three competing launches since 23 Apr 2026 (Fonoa Knowledge in Jul 2026, VAT Guard on 27 Jul 2026, VatForge on 1 Sep 2026). It also fails K3, because Shopify Tax already monitors EU VAT liabilities inside the platform, and the moat is not yet shown.

**Why**

- K2 copy-speed fails (3 launches; 2 or more kills). Fonoa says it 'recently launched Fonoa Knowledge', an AI tax-monitoring product, in its 13 Aug 2026 update covering July releases: https://www.fonoa.com/resources/blog/fonoa-product-updates-august-2026 and https://www.fonoa.com/resources/blog/introducing-fonoa-knowledge
- K2 continued: the Shopify app VAT Guard, which tracks EU sales and VAT by country against the €10k threshold, shows 'Launched July 27, 2026' (Free / $12.90 / $29.90 a month): https://apps.shopify.com/vat-guard. VatForge says 'Live since 1 September 2026' and offers a €0 'VAT Radar' tier covering 'every integration, all 27 countries': https://vatforge.com/taxdoo-migration-playbook and https://vatforge.com/
- K3 platform ownership fails. Shopify's help centre says 'If you use Shopify Tax, then your sales and locations are automatically monitored ... You receive monthly notifications' about EU tax liabilities: https://help.shopify.com/en/manual/taxes/eu/eu-tax-liability. Amazon VAT Services offers obligation and deadline updates in Seller Central: https://globalselling.amazon.com/en/vat
- K0 moat is weak or unproven. The underlying laws are public, and generic monitoring is already free at VatForge and VAT Guard. The only plausible asset is a merchant-specific impact graph, which would need a human VAT expert to sign off interpretations. That makes it hard to run with agents and does not exist yet: https://vatforge.com/
- Demand is mixed. More than 193,000 businesses were registered for OSS/IOSS by the end of 2025: https://taxation-customs.ec.europa.eu/news/eu-vat-rules-e-commerce-five-years-more-eur125-billion-vat-revenue-2026-09-03_en. But Taxdoo reportedly left VAT compliance on 30 Apr 2026, arguing that ViDA is automating it. That is a negative signal for a standalone tracker, and the report comes from vendor sources: https://www.vatai.com/blog/taxdoo-to-end-vat-services-in-2026

| Competitor | Price | Launched | URL |
|---|---|---|---|
| Fonoa Knowledge (enterprise global indirect-tax change monitoring) | unverified (enterprise, not published) | July 2026 (per Fonoa 13 Aug 2026 update) | https://www.fonoa.com/resources/blog/fonoa-product-updates-august-2026 |
| VAT Guard (Shopify app, addson) | Free; $12.90/mo Standard; $29.90/mo Pro | 27 Jul 2026 | https://apps.shopify.com/vat-guard |
| VatForge | €0 VAT Radar; €19/mo SME Scheme; €79/mo OSS Filing; from €249/mo Operations | 1 Sep 2026 (self-stated) | https://vatforge.com/ |
| Shopify Tax EU liability monitoring | bundled with Shopify Tax (cost not stated on page) | pre-window | https://help.shopify.com/en/manual/taxes/eu/eu-tax-liability |
| Amazon VAT Services | unverified | pre-window | https://globalselling.amazon.com/en/vat |
| hellotax | €49/mo per country New Seller; €119/mo per country Established (per lead evidence, not re-fetched) | pre-window | https://hellotax.com/pricing?_get=start |
| SimpleVAT | €25/mo Lite; €60/mo Pro (per lead evidence, not re-fetched) | pre-window | https://www.simplevat.eu/pricing/ |

**Demand:** The broad proxy is real and recent: more than 193,000 OSS/IOSS registrants by the end of 2025, and more than €38bn of VAT collected through the schemes in 2025, up 17% (https://taxation-customs.ec.europa.eu/news/eu-vat-rules-e-commerce-five-years-more-eur125-billion-vat-revenue-2026-09-03_en). There is no evidence of paid demand for a standalone tracker. The free tiers at VatForge and VAT Guard, plus Shopify's bundled monitoring, push the willingness to pay for monitoring alone towards zero. VAT Guard has one review, a 1-star rating dated 29 Aug 2026 (https://apps.shopify.com/vat-guard).

**Channel:** Lawful channels exist: SEO, a Shopify App Store listing and paid search (https://shopify.dev/docs/apps/launch/distribution/visibility). But the App Store category already has a new free-tier entrant (VAT Guard), and Shopify's own monitoring is the default for merchants.

**Owner hours:** Unverified. Tax-interpretation approval and handling exceptions would probably push Ricardo past 5 h/week.

**Desk check run:** I re-ran the copy-speed check live. VAT Guard's Shopify listing shows 'Launched July 27, 2026'. VatForge's own page says 'Live since 1 September 2026'. Fonoa's 13 Aug 2026 update says Knowledge was 'recently launched'. I also confirmed Shopify Tax's bundled monthly EU liability notifications. Result: three launches in the window plus a platform-native feature, so a kill is confirmed and no paid-reservation test is needed.

**Unverified:**
- Exact Fonoa Knowledge launch day (lead says 30 Jul 2026; the August update only says 'recently launched')
- Fonoa Knowledge pricing
- Shopify Tax cost for EU monitoring
- Taxdoo's own exit announcement (reported only by competing vendors)
- Search volume for EU VAT change-tracking terms
- Owner hours at steady state
- Re-fetch of hellotax and SimpleVAT pricing

## L058 European facilities management SaaS: kill (medium)

The price looks fair on paper (about 3.35× claimed profit), but this is a French public-sector CMMS with 80–90 institutional clients, and it fails the ≤5 h/week, ≥50%-automated rule (K1/B4): owner hours aren't disclosed, the 91% margin suggests the owner's own work isn't counted as a cost, and renewals go through French public tenders.

**Why**

- Re-opened today: the listing is still open to inquiries and offers, with 3,792 views and 98 watchers. Asking price is €1,130,000 (USD $1,325,715). Claimed monthly profit is €28,125 (about €337.5k a year), so the multiple is about 3.35× and passes B3 on paper. ARR is given as €350k in the title and €360k in the description, with no financial period or as-of date. Flippa says it vetted 'Revenue, Primary Expenses, Traffic', but the documents are behind an NDA. https://flippa.com/12839625-b2b-facilities-saas-350k-arr-93-retention-with-lean-cost-base-positioned-for-bolt-on-integration-and-immediate-deployment-across-existing-customers
- B4 owner hours: not stated anywhere. Staff count, reason for sale and seller involvement after the sale are also not stated. A 91% margin on a 9-year product covering web, iOS and Android, with ERP and building-system integrations and 80–90 institutional clients, implies almost no paid staff. That usually means the owner's or founders' labour is left out of costs, which points to seller dependence and hidden hours (an inference, not a verified fact). https://flippa.com/12839625-b2b-facilities-saas-350k-arr-93-retention-with-lean-cost-base-positioned-for-bolt-on-integration-and-immediate-deployment-across-existing-customers
- K1 channel and workload: the customers are French public bodies and engineering firms reached through 'pre-approved access to French public sector procurement frameworks'. French public CMMS ('GMAO') buying runs through BOAMP and TED tenders with fixed terms (for example 60 months plus renewals, or order-based contracts with a cap). Bid writing, French-language account management, security reviews and onboarding are human work, and agents can't reliably do them. That keeps automation at about 40%, under the 50% bar. https://www.boamp.fr/telechargements/FILES/PDF/2024/08/24-94992.pdf https://ted.europa.eu/en/notice/314514-2021/pdf
- B5 transferability: the listing doesn't say whether framework access or the customer contracts survive a change of control. French public-contract rules only allow a contractor to be replaced in specified circumstances. App transfers between store accounts are possible but conditional. https://entreprendre.service-public.gouv.fr/vosdroits/F23387?lang=en https://developer.apple.com/help/app-store-connect/transfer-an-app/app-transfer-criteria/
- K0 moat: conditionally passes as switching costs (d), from stored asset histories, work orders, integrations and a claimed average tenure of 2.3 years. Score 6/10, but it rests only on seller claims. Competitive pressure is high: Facilio released an AI-native Connected CMMS (reported July 2026), and FexaAI, ServiceChannel AI and Nulogy Maintenance launched just before the window. https://techintelpro.com/news/enterprise-tech/automation/facilio-unveils-ai-native-connected-cmms-for-facilities-operations https://www.prnewswire.com/news-releases/fexa-launches-fexaai-the-first-multi-agent-ai-platform-built-for-facilities-management-302728818.html
- Fit and capital: buying at €1.13M needs serious financing for a solo founder. That doesn't break a locked rule on its own, but it raises the stakes on the unverified hours and transfer questions. The seller's stated ideal successor is an organisation already in facilities or property management, which signals that sector relationships carry the business. https://flippa.com/12839625-b2b-facilities-saas-350k-arr-93-retention-with-lean-cost-base-positioned-for-bolt-on-integration-and-immediate-deployment-across-existing-customers

| Competitor | Price | Launched | URL |
|---|---|---|---|
| MaintainX | Free Basic; Essential $20/user/mo annual; Premium $65/user/mo annual; Enterprise custom | established | https://www.getmaintainx.com/pricing |
| IBM Maximo | from under $40,000/yr | established | https://www.ibm.com/products/maximo/pricing |
| Facilio Connected CMMS (AI-native release) | unverified | reported July 2026 | https://techintelpro.com/news/enterprise-tech/automation/facilio-unveils-ai-native-connected-cmms-for-facilities-operations |
| FexaAI | unverified | 2 Apr 2026 | https://www.prnewswire.com/news-releases/fexa-launches-fexaai-the-first-multi-agent-ai-platform-built-for-facilities-management-302728818.html |
| ServiceChannel AI | unverified | 7 Apr 2026 | https://servicechannel.com/press/servicechannel-launches-servicechannel-ai-for-facilities-management/ |
| Nulogy Maintenance | unverified | 8 Apr 2026 | https://nulogy.com/news-announcements/press-releases/nulogy-maintenance-launch/ |
| Vertixium (elevator operations, adjacent) | unverified | 1 Aug 2026 (self-stated) | https://vertixium.com/ |

**Demand:** There is live demand for the category. JLL's November 2025 report found 32% of 248 organisations plan to increase FM software spend, and public French GMAO tenders keep appearing (BOAMP 2024, TED 2026). The listing's own demand evidence (88 subscribers, 7% churn, 93% retention) has no date or measurement period, so under the 18-month rule its revenue proof gets zero weight. https://www.jll.com/en-us/insights/global-state-of-facilities-management-report https://ted.europa.eu/en/notice/304450-2026/pdf https://flippa.com/12839625-b2b-facilities-saas-350k-arr-93-retention-with-lean-cost-base-positioned-for-bolt-on-integration-and-immediate-deployment-across-existing-customers

**Channel:** There are lawful channels: SEO and directories for French CMMS ('GMAO') software, integration directories, and responding to public tenders on BOAMP and TED. Tender responses are lawful inbound work, not cold outreach, but they take a lot of human time and must be written in French. Cold outreach to French public buyers is excluded. https://www.boamp.fr/telechargements/FILES/PDF/2024/08/24-94992.pdf

**Owner hours:** unverified: the listing doesn't state them. The 91% margin with no stated staff suggests unpaid owner labour (an inference). https://flippa.com/12839625-b2b-facilities-saas-350k-arr-93-retention-with-lean-cost-base-positioned-for-bolt-on-integration-and-immediate-deployment-across-existing-customers

**Desk check run:** I re-opened the listing live: it is still open to offers, with the figures, badges and gaps listed above. I searched for the broker (Aim Digital Group, UK, Flippa-verified, 40 transactions totalling $789,611) and found no public business identity. I searched French public CMMS buying and found it runs through BOAMP and TED tenders, not self-serve. I also searched for 2026 CMMS launches (Facilio's AI-native release). Result: none of the deciding facts (hours, dated TTM, contract transferability) can be checked without an NDA, and everything public points to a human-heavy French public-sector account business, so K1 fails.

**Unverified:**
- Owner hours per week
- Staff count and payroll
- Financial period and as-of date for the ARR and profit figures
- Which figure is right, €350k or €360k ARR
- Churn period and definition
- Whether procurement framework access and customer contracts transfer
- Reason for sale
- Seller involvement after the sale
- Facilio AI-native CMMS release date and pricing (taken from secondary news only)
- Competitor pricing for Facilio, FexaAI, ServiceChannel AI, Nulogy and Vertixium
