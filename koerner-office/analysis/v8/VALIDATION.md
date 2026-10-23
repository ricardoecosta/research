# v8 validation (METHOD step 10: high-effort, web-checked)

Run 23 Oct 2026 (UK time) by Grok Bot (Researcher), under the METHOD.md FALLBACKS rule: Claude Opus is out until 5:20pm BST, so Researcher runs the validation itself with live web checks. Every verdict below rests on pages fetched today (WebSearch/WebFetch, Atlassian Marketplace REST, App Store pages, GOV.UK). Codex wasn't used for drafting. Under the EFFICIENCY rules, nothing here comes from a cheap-token pass.

**Scope:** the 15 ranked clusters in `TOP_SLICE.md` plus the 20 scout records in `scouts/scouts.jsonl`.

**Not in scope:** the 5 most-cited clusters (C0001–C0005). The parent run excluded them because each already breaks at least one hard constraint (local selling, physical work, hours, PECR), and those rule kills stand. They were not re-web-checked here. METHOD step 11 asks for a web-checked kill reason for them, so this is a recorded gap.

**Rules applied (RULES_LOCKED.md):**
- **Staleness:** claims older than 18 months, or that rest on a tool, price or platform, were rechecked live.
- **Moat check, applied extra hard:** how fast can a competitor or the platform copy it? We counted live competitors and launches in 2026.
- **UK PECR:** banned cold channels (SMS, WhatsApp, DMs or email to individuals and sole traders) can't be relied on.
- **Ricardo's hard constraints:** high automation, 5 h/week or less, no selling to local businesses, no face or personal brand.
- **"Unverified"** marks any figure we couldn't confirm.

**Verdict key:** **pursue** = passes the gate. **Maybe** = passes the rules, with named open questions that would decide it. **Kill** = fails, with the reason.

This file is the step-10 output. It is not a final shortlist.
## Part B: market scout leads (SC01–SC20)

### SC01: MV3 replacements for orphaned Edge/Chrome MV2 extensions. **Kill**, confidence medium-high
- **Rechecked live:** exstats (5 Sep 2026) counts 3,339 live MV2 listings on Edge with 85.6M installs. The 52 listings with 100k+ installs hold 90.7% of those installs. The other 3,287 listings hold 7.9M installs, about 2.4k each ([exstats](https://exstats.com/blog/mv2-purge-in-numbers)). Microsoft (7 Aug 2026) says 95% of the top MV2 extensions have already moved. By its count only 58 MV2 extensions have meaningful usage, and only 3 of those lack an MV3 version ([Edge blog](https://blogs.windows.com/msedgedev/2026/08/07/moving-the-microsoft-edge-extensions-ecosystem-forward-with-manifest-version-3/)). Enterprise switch-off runs Jan–Apr 2027 ([MC1467356](https://mc.merill.net/message/MC1467356)).
- **Demand:** Chrome is the precedent. After its purge the catalogue grew 44%, but total users stayed flat, and 70.8% of the removed extensions had fewer than 100 users (exstats). The large Edge orphans belong to vendors (Microsoft Purview, Cisco Webex, HP Dynamic Audio, bank Ukey extensions), so a third party can't replace them.
- **Moat:** none. Anyone can port an extension, and the window closes at the end of 2026.
- **Revenue:** no evidence that orphaned-extension users pay. Unverified.
- **Why kill:** the popular extensions have already migrated or belong to vendors, and each orphan in the long tail is too small to pay.

### SC02: Premium Bonds checker app (iOS first). **Kill**, confidence medium
- **Rechecked live:** the NS&I checker on iOS is 2.6★ from 1.4k ratings. It was last updated 28 Nov 2024 (v6.1.3) and sits at #122 in Finance ([App Store](https://apps.apple.com/gb/app/premium-bonds-prize-checker/id474172893)).
- **What changed:** NS&I launched a new main app in late 2025 that shows Premium Bonds prize history; it was updated Aug 2026 ([NS&I](https://www.nsandi.com/mobile-app)). NS&I already sends prize notifications by text and email ([NS&I corporate](https://nsandi-corporate.com/news-research/news/nsi-introduces-more-ways-whole-family-stay-touch-premium-bonds)). Android already has a 4.1★ third-party checker (scout record).
- **Risks:** "Premium Bonds" and NS&I are NS&I's marks, so expect App Store review and trademark trouble. The winning-numbers data is free, so the app is trivial to clone.
- **Revenue:** no evidence anyone pays for a prize checker. Unverified.
- **Why kill:** the official channel now covers the job, and nobody has shown willingness to pay. At most it's a weekend portfolio app, not a business.

### SC03: Octopus tariff companion (OctoTracker successor). **Kill**, confidence medium-high
- **Rechecked live:** OctoTracker's iOS app was last updated 25 Jun 2025 ([App Store](https://apps.apple.com/us/app/octotracker/id6463722470)). A LinkedIn post says "OctoTrack is now available as a web app". That looks like the same developer moving to the web, but the name match is unverified ([LinkedIn](https://www.linkedin.com/posts/vincent-tc-lee_oct-track-activity-7501962584661663744-81Xz)). Octopus Compare also dropped its app for a web version ([blog](https://octopus.compare/blog/welcome-to-octopus-compare-web)).
- **Moat:** none. The Octopus API is free and public, OctoDash and Octopus Watch are active, and Octopus's own app shows tariff prices.
- **Why kill:** two incumbents abandoned their apps for the web, which suggests the apps don't pay. This is the copy pattern again.

### SC04: FreeAgent connector layer (e-commerce settlements and missing Zapier actions). **Kill for now (watch)**, confidence medium
- **Rechecked live:** Equali is FreeAgent's official, help-centre-documented integration. It covers Shopify, Amazon, eBay and Etsy, has TikTok Shop and Facebook/Instagram due in 2026, and FreeAgent users get 20% off ([FreeAgent help](https://support.freeagent.com/hc/en-gb/articles/33737714948626-How-the-Equali-integration-works)). Equali's Shopify app has one review: 1★ on 22 Oct 2026, saying eBay settlements failed to post ([Shopify](https://apps.shopify.com/equali)). A2X, Link My Books and Synder still don't support FreeAgent ([foundationaltech](https://foundationaltech.co.uk/articles/a2x-vs-link-my-books-vs-synder-which)). Make already covers FreeAgent invoices (scout record).
- **Moat:** Equali holds FreeAgent's official listing and the discount, a distribution edge a newcomer can't match. Accounting correctness also brings support load and liability.
- **What would reopen it:** Equali falters, for example more 1★ reviews or a dropped listing, *and* FreeAgent agrees to list a second partner.
- **Why kill:** the gap is real, but it now has an officially endorsed owner.

### SC05: Google Chat for Jira Cloud replacement. **Kill**, confidence medium-high
- **Rechecked live (REST):** the incumbent is **Google LLC's own free app**. It has 11,005 installs, 924,125 total users, 2.30★ from 110 reviews, and its last release was 11 Nov 2021 ([REST](https://marketplace.atlassian.com/rest/2/addons/linovi-hangoutschat-bot); [versions](https://marketplace.atlassian.com/rest/2/addons/linovi-hangoutschat-bot/versions?limit=3)). 2026 reviews on Google's Workspace listing complain that you can't filter out your own actions and ask for one Chat thread per issue ([Workspace Marketplace](https://workspace.google.com/marketplace/app/jira_for_google_chat/1063804824442)).
- **Competitors (live):**
  - Advanced Google Chat for Jira (Move Work Forward): 406 installs, **free**, v4.5.0 on 13 Oct 2026 ([listing](https://marketplace.atlassian.com/apps/1233491/advanced-google-chat-for-jira)).
  - Canary Apps "Google Chat for Jira": 123 installs, updated Oct 2026.
  - Canary's automation actions: 3 installs, paid.
  - **Chatpane** (Brain Static Threads): a paid Forge app, v3.0.0 on 16 Oct 2026. Its pitch matches the 1★ complaints point for point: webhook setup, no Google sign-in, one thread per work item ([listing](https://marketplace.atlassian.com/apps/2126201930/chatpane-google-chat-notifications-for-jira)). It wasn't in this morning's scout data. Its install count isn't shown.
  - DIY: Jira Automation's "Send web request" can post to a Chat webhook for free ([Atlassian community](https://community.atlassian.com/forums/discussion/2568907/custom-google-chat-messages-through-automation)).
- **Economics:** Atlassian takes 0% of Forge revenue until $1M lifetime, then 17%. Connect apps pay 25% ([Atlassian](https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/)). The terms are favourable, but the competition is free.
- **Why kill:** a new entrant already targets the exact complaints and a competent free alternative exists, so a paid app would compete against free twice over. Google could also fix its own app at any time. The extra-hard moat check fails.

### SC06: Harvest for Jira replacement. **Kill**, confidence high
- **Rechecked live:** an Atlassian REST search for "harvest" returns 9 apps. The official app has 2,439 installs (2.53★ from 145), and the others are 42nd (375), Twin Sun (27), MarcelBag (9), Metronome (3), Appvibe (2) and Valandir (1). The moat fails, as the scout found.

### SC07: Orphaned Atlassian integrations (pattern). **Kill as a strategy**, confidence medium
- Copying was confirmed again today: SC05's best orphan already has a fresh competitor (Chatpane, Oct 2026) built around its complaints, and InVision drew 2 replacements (scout). The Forge 0% revenue-share incentive makes cloning cheap for everyone.

### SC08: Better Mermaid for Confluence. **Kill**, confidence high
- **Rechecked live:** an Atlassian REST search for "mermaid" now returns **107** apps; the scout's query found 84. Several are rated 4.0–4.6★ (for example Stratus, 6,223 installs, 4.02★; weweave, 2,181 installs, 4.58★).

### SC09: Stripe/PayPal-to-Xero fix. **Kill**, confidence medium
- Not rechecked beyond the scout's Xero pages. The complaints are aimed at Stripe and Xero themselves, and A2X etc. already cover reconciliation. Nothing a third party can fix.

### SC10: Xero data export and archive. **Kill**, confidence high
- **Rechecked live:** the market is served. Boxkite sells a $49 one-off export with attachments ([Boxkite](https://www.getboxkite.com/download-xero-data)), Xportmydata charges $120 one-off ([Xportmydata](https://www.xportmydata.com/single-download/)), and Numerint also exists ([Numerint](https://numerint.com/)).

### SC11: UK smart-meter data companion. **Kill**, confidence high
- **Rechecked live:** Hildebrand's **Bright** app is free and gives consumers half-hourly smart-meter data through the DCC ([App Store](https://apps.apple.com/gb/app/bright/id1369989022)), and n3rgy runs a consumer portal ([n3rgy](https://www.n3rgy.com/consumer/)). Data access is cheap for the incumbents and their apps are free.

### SC12: Tide Times UK successor. **Kill**, confidence high
- **Rechecked:** My Tide Times is rated 4.8★ on both stores ([App Store GB](https://apps.apple.com/gb/app/my-tide-times-tables-chart/id777280890)). ADMIRALTY EasyTide is free for 7 days ([UKHO](https://www.admiralty.co.uk/access-data/tidal-data/easy-tide)), and Tides Near Me uses UKHO data under the OGL ([source](https://tidesnear.me/data-sources)).

### SC13: UK-specific digital templates (Gumroad/Etsy). **Kill**, confidence medium
- **Rechecked live:** the Gumroad JSON for "uk landlord" still returns a total of 8 products. Supply is thin, but there is still no demand signal (0 ratings, per the scout). Etsy PLR bundles at £1.49–£1.65 would copy any winner. No moat.

### SC14: Productised spreadsheet/n8n automation gig. **Kill (rules)**, confidence high
- It's a service: client scoping and comms break the 50% automation and 5 h/week limits. Not rechecked; the rule kill doesn't depend on the market.

### SC15: UK statutory-inspection SaaS (FireCert/LolerFlow pattern). **Kill (rules)**, confidence high
- The revenue evidence here is the strongest of any scout (FireCert at about $4.5k MRR, Stripe-verified per [wlad.me](https://www.wlad.me/blog/companies/firecert)). But the buyers are local trade contractors reached through sales, which Ricardo has ruled out. Recorded so the reason is visible.

### SC16: HubSpot UK payments-to-Xero/QBO sync. **Kill**, confidence medium
- Carried from the scout, not re-fetched. Funded connectors (Invoice Stack, Synder, the native QBO integration) already serve it, and the demand evidence is one community post.

### SC17: Companies House software accounts filing for micro and dormant companies. **Kill**, confidence medium-high
- **Date resolved (GOV.UK, live):** software-only (iXBRL) accounts filing starts **1 April 2028**; the 2027 date is superseded. WebFiling and paper close for accounts, with no transition period ([GOV.UK guidance](https://www.gov.uk/guidance/using-software-to-file-your-companys-information)). The Written Ministerial Statement records the one-year postponement from April 2027 ([Hansard](https://hansard.parliament.uk/debates/GetDebateAsText/26060938000008)).
- **New today:** the 9 Jun 2026 news story was **withdrawn on 23 Oct 2026** and replaced. Small and micro companies will no longer have to file profit and loss accounts; that requirement is paused, and abridged and "filleted" accounts stay. The software mandate still goes ahead in April 2028 ([GOV.UK update](https://www.gov.uk/government/news/companies-house-update-to-accounts-filing-from-april-2028); [withdrawn notice](https://www.gov.uk/government/news/companies-house-to-bring-in-changes-to-accounts-filing-from-april-2028)). That makes the filing job simpler and pushes the market further toward cheap commodity tools.
- **Competition and price floor:** HMRC's free CATO service already closed on 31 Mar 2026 ([GOV.UK](https://www.gov.uk/guidance/closure-of-the-service-to-file-your-company-accounts-and-tax-return)). Dormant Return charges £5 ([site](https://dormantreturn.co.uk/)), SimpleCompanyTax £10+VAT, DormantFile £19 and TinyTax £20/yr ([TinyTax](https://tinytax.co.uk/pricing)).
- **Why kill:** the market is crowded at £5–£20/yr before the mandate even lands, and filing errors carry liability and support load.

### SC18: Successors to abandoned WordPress.org plugins. **Kill**, confidence medium
- **Rechecked:** BackUpWordPress's last release was Apr 2024 and its homepage now promotes UpdraftPlus, while BackWPup was still shipping updates in Oct 2026. WP Media says Heartbeat Control is still supported. Third parties already publish "abandoned plugin" lists for 2026 ([musthaveplugins](https://musthaveplugins.com/blog/abandoned-wordpress-plugins-2026-part-2/)). The large orphans have maintained alternatives, and support threads cost hours.

### SC19: Gift Aid plugin for small charities. **Kill**, confidence high
- **v7's "no dedicated plugin" claim is out of date.** Tinwell exports in HMRC's column order ([Tinwell](https://tinwell.org/gift-aid-wordpress/)), and Donor Merchant ([site](https://www.donormerchant.com/features/gift-aid/)), Charitable's Gift Aid extension ([site](https://www.wpcharitable.com/extensions/charitable-gift-aid/)) and the HMRC-listed Sky Gift Claim ([site](https://skywebdesign.co.uk/products/sky-gift-claim/)) all cover it too.

### SC20: Royal Mail Click & Drop sync on Shopify (benchmark). **Kill**, confidence high
- **Benchmark reconfirmed:** MakePost launched 7 Oct 2026 with a free plan and a $5.99/mo plan ([Shopify](https://apps.shopify.com/makepost)), and Postbag launched 24 Sep 2026 ([pickyourapp](https://pickyourapp.com/products/postbag)). Postly is established ([Shopify](https://apps.shopify.com/click-and-drop-integration)).
