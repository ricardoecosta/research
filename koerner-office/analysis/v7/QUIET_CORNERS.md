# Quiet corners: opportunities beyond the v7 list

Run on 23 Oct 2026 by Grok Bot, kept short to save credits. Every number below links to its source URL, and anything not checked is marked **unverified**. The raw scan data is in `qc/`: `ios.txt` and `ios.json` (iTunes Search API, GB store, 66 UK-niche terms), `wp.json` (WordPress.org searches on 30 UK terms) and `wpstale.json` (the 2,500 most popular WordPress.org plugins with their last-update dates).

This list leaves out everything already in `IDEAS_WORTH_PURSUING.md`. That covers the Shopify add-on (the Shopify scan is paused, and its 40 search terms, including EPR, GPSR, Gift Aid on Shopify and Royal Mail, are left alone here), the iOS app, the vault app, the UK directory, Find a Tender alerts, AI implementation, the call agent and templates.

## Headline finding

The obvious UK "new rule = new micro-SaaS" corners filled up within months. Search no longer turns up quiet ones. The quiet corners that remain are **installed bases that have been left behind**: apps nobody maintains, plugins and extensions nobody updates, and official apps with bad ratings. There is also room on **smaller stores**, such as Edge Add-ons, which is about one-eighth the size of the Chrome Web Store. The evidence for the crowding:

- MTD bridging software: 88 of the 173 products HMRC recognises are bridging tools ([mtdradar](https://mtdradar.co.uk/mtd-bridging-software)).
- CT600 filing: about 50 suppliers are on HMRC's list ([GOV.UK](https://www.gov.uk/government/publications/corporation-tax-commercial-software-suppliers/corporation-tax-commercial-software-suppliers)), and dormant filing costs £5 ([dormantreturn](https://dormantreturn.co.uk/), [clientsassistant](https://www.clientsassistant.com/hmrc-ct600-service-closed.html)).
- Renters' Rights Act landlord compliance: at least 5 tools ([complywithme](https://complywithme.co/), [rentdocs](https://rentdocs.co.uk/), [propready](https://propready.co.uk/), [landlordcomply](https://landlordcomply.uk/), [datestone](https://www.datestone.io/landlord-software/renters-rights-act)).
- Delay Repay automation: at least 4 tools ([Railed!](https://apps.apple.com/gb/app/railed-train-delay-repay/id6766553406), [Railhop](https://railhop.app/), [Train Badger](https://trainbadger.app/), [RailClaim](https://railclaim.co.uk/)).
- Private parking appeal letters: at least 4 tools ([pcnappealletter](https://pcnappealletter.co.uk/), [appealiq](https://appealiq.app/), [parkappeal](https://parkappeal.co.uk/private-operators/), [beatmypcn](https://beatmypcn.co.uk/)).
- Companies House data in Sheets: [UK Company Details](https://workspace.google.com/marketplace/app/uk_company_details/666560558891) and CompanyStack. In Chrome: Company Check's extension ([extops](https://extops.dev/extensions/gbmnpcdcjldifkooekeadfenfbopjhoi)) and [Leadistry](https://leadistry.co.uk/product/chrome-extension).
- The Chrome Web Store grew 44% in 11 months, to 254,652 listings, while total users stayed flat ([exstats](https://exstats.com/blog/mv2-purge-in-numbers)).

## Summary ranking

Each idea gets two scores out of 10: how interesting it is to you and how likely it is to work.

| # | Opportunity | Where | Automation | Hours/week | Breaks a rule? | Interest | Odds |
|---|---|---|---|---|---|---|---|
| 1 | Replacements for Edge extensions being switched off (Edge's MV2 phase-out) | Microsoft Edge Add-ons | ~75% | 3–5 | No | 7 | 4 |
| 2 | A better iOS Premium Bonds companion than the 2.6★ and 1.6★ official apps | Apple App Store (GB) | ~85% | 1–2 | No | 7 | 4 |
| 3 | "Zombie app" takeovers: rebuild a well-loved UK app that has stopped updating (start with an Octopus smart-tariff companion) | Apple App Store (GB) | ~75% | 2–4 | No | 8 | 3 |
| 4 | Maintained successors to abandoned WordPress.org plugins | WordPress.org | ~70% | 3–5 | Borderline on hours (support load) | 6 | 3 |
| 5 | Software-only Companies House accounts filing for dormant and micro companies (from 1 Apr 2028) | GOV.UK / Companies House | ~70% | 3–6 | Possibly hours; liability | 6 | 3 |
| 6 | Gift Aid declarations and HMRC claim export for small charities on WordPress | WordPress.org, HMRC Charities Online | ~70% | 2–4 | Borderline: customers are charities, not local businesses, and they arrive through the directory | 5 | 3 |
| 7 | One national bin-day reminder app built on council data | Apple App Store / Google Play | ~60% | 4–8 | **Yes**: hours (scrapers break) and probably automation | 4 | 2 |
| 8 | Heat-pump owner performance companion | Apple App Store (GB) | ~60% | 4–6 | **Possibly**: hardware APIs make it hard to automate | 6 | 2 |

**Recommendation:** #1 and #2 are cheap tests of under 2 weeks each that need no sales. #3 is really a niche-finding method for your existing iOS idea, so run it inside that idea's keyword gate rather than as a separate project.

---

## 1. Replacements for Edge extensions being switched off

- **Where found:** [exstats, "MV2 Purge in Numbers"](https://exstats.com/blog/mv2-purge-in-numbers) (5 Sep 2026); the [Chrome MV2 timeline](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline).
- **Background:** Manifest V2 (MV2) is the old format for browser extensions. Chrome and now Edge are switching it off, so MV2 extensions stop working.
- **Why it's underserved:**
  - Edge Add-ons has 32,478 listings, against 254,652 on Chrome.
  - 3,339 Edge listings are still MV2, with 85.6M active installs. Microsoft says the consumer switch-off will finish by the end of 2026.
  - Outside the top ~52 extensions, **3,287 listings with 7.9M installs** are unlikely to get MV3 successors, in exstats' words "no MV3 successor and no announcement naming them".
  - On Chrome, 84.4% of developers whose extensions were removed are no longer visible in the store.
- **The idea:** pick 2–3 orphaned *utility* extensions with 10k–100k installs whose names aren't trademarks. Ship clean MV3 replacements on Edge (and Chrome) with an "alternative to X" listing, and make money through a small Pro tier.
- **Automation:** ~75%, since agents can write and port an extension. **Hours:** 3–5 a week for the first month, then about 1. **Rule breaks:** none.
- **Risks:** many orphaned extensions are trivial or free-by-nature, so it may be hard to charge. The list of Edge MV2 extensions has to be built by hand or bought from exstats (**unverified** whether that's possible). Don't copy code without a licence check, and never reuse names.
- **First test (≤2 weeks):** scrape Edge Add-ons for MV2 listings with ≥10k installs, last updated in 2022 or earlier, and no successor. Shortlist 10, build 1, publish on Edge and Chrome, and track installs for 14 days. **Pass:** ≥300 installs by day 14.
- **Interest 7, Odds 4.**

## 2. A better iOS Premium Bonds companion

- **Where found:** iTunes Search API, GB store ([raw data in qc/ios.txt](qc/ios.txt)); [NS&I's official checker on the App Store](https://apps.apple.com/gb/app/premium-bonds-prize-checker/id474172893); [NS&I's page of winning-bond downloads](https://www.nsandi.com/get-to-know-us/winning-bonds-downloads).
- **Why it's underserved:**
  - NS&I's own "Premium Bonds prize checker" is rated **2.6★ from 1,357 ratings** and was last updated 28 Nov 2024. The main NS&I app is rated **1.6★ from 306 ratings**.
  - The only third-party iOS app the search turned up, "Numo – Premium Bonds & Savings", has **0 ratings**.
  - The web has competitors ([premiumbondsresults.com](https://premiumbondsresults.com/), [pbprizes.com](https://pbprizes.com/)), and Android has "Premium Bonds Prize Checker +" ([Play](https://play.google.com/store/apps/details?hl=en&id=com.steveh.pbcp)). A Reddit builder added email alerts that arrive "days earlier than the official email" ([r/premiumbonds](https://www.reddit.com/r/premiumbonds/comments/1v7txwp/added_email_alerts_to_my_premium_bonds_checker_to/)), which is a sign people want this.
  - The data is free. NS&I publishes full winning-number lists for the last 6 months, and an FOI release covers 2000 to May 2026 ([WhatDoTheyKnow](https://www.whatdotheyknow.com/request/historic_premium_bonds_results)).
- **The idea:** a private, on-device app that stores your bond ranges, checks them automatically every month, sends a push alert, shows effective-rate and odds stats, and flags unclaimed prizes. One-off £2.99, or £0.99 a month.
- **Automation:** ~85%; a monthly cron job just reads the published file. **Hours:** 1–2 a week. **Rule breaks:** none. It's sold to consumers through the App Store, so PECR doesn't apply.
- **Risks:** "Premium Bonds" and "NS&I" are trademarks, so avoid implying the app is official (Apple guideline 4.1/5.2 risk). The number of holders is **unverified**. Revenue per user is small.
- **First test:** check ASO volume for "premium bonds" in the iOS keyword tool (it's already part of the iOS gate in week 2). Build a TestFlight MVP in about 1 week and launch it. **Pass:** ≥20 organic installs a day by day 14.
- **Interest 7, Odds 4.**

## 3. "Zombie app" takeovers: Octopus smart-tariff companion first

- **Where found:** iTunes Search API, GB store ([qc/ios.txt](qc/ios.txt)).
- **Why it's underserved:** popular UK apps that have stopped updating:
  - **OctoTracker:** 1,173 ratings at 4.8★, last updated 25 Jun 2025. Its neighbours are Octo Aid (1,955 ratings) and Octopus Watch (£1.99, 619 ratings).
  - **Tide Times UK:** 6,046 ratings, last updated 6 Mar 2021. Licensing UKHO tide data is a barrier (**unverified** cost).
  - **"Food Hygiene":** 113 ratings, last updated 2018. The FSA rating data is open.
- **The idea:** Octopus has a public customer API (**unverified**, from memory: developer.octopus.energy). A companion app that shows Agile and Tracker prices, home-screen widgets, cheapest-slot alerts and the bill compared with the price cap can take over OctoTracker's abandoned users.
- **Automation:** ~75%. **Hours:** 2–4 a week. **Rule breaks:** none.
- **Risks:** Octopus's own app keeps getting better (266,557 ratings). The app depends on Octopus not closing its API.
- **First test:** put "octopus agile" and "octopus tracker" into the iOS keyword gate. Ship widget-first in 10 days. **Pass:** ≥15 installs a day.
- **Interest 8, Odds 3.**

## 4. Maintained successors to abandoned WordPress.org plugins

- **Where found:** the WordPress.org plugins API, top 2,500 most popular ([qc/wpstale.json](qc/wpstale.json)).
- **Why it's underserved:** **71 plugins with ≥20k installs haven't been updated in more than 2 years.** Examples:
  - BackUpWordPress: 80k installs, 1,373 ratings, last updated 24 Apr 2024.
  - Enhanced Media Library: 60k installs, last updated 15 Jul 2024.
  - Heartbeat Control: 70k installs, last updated 31 Aug 2023.
  - Add From Server: 60k installs, last updated 11 Dec 2020.
  - Display Posts: 80k installs, last updated 14 Oct 2024.

  Many already have successors: Limit Login Attempts (300k, stale) has Reloaded (1M, current), and Search & Replace has Better Search Replace (1M). So filter for **stale with no maintained successor**.
- **The idea:** a successor plugin that imports the old plugin's settings with one click, plus a Pro add-on, with "alternative to X" pages for SEO. Plugin authors can also put plugins up for adoption on WordPress.org (**unverified** for these particular plugins).
- **Automation:** ~70%. **Hours:** 3–5 a week, mostly support threads. **Rule breaks:** borderline on hours. The buyers are site owners, mostly businesses, who find the plugin themselves through the directory; there's no outreach.
- **First test:** for the 71, check whether a maintained alternative exists and how many open support threads ask "is this abandoned?". Pick 1 and ship it. **Pass:** ≥500 active installs in 30 days.
- **Interest 6, Odds 3.**

## 5. Software-only accounts filing at Companies House (1 Apr 2028)

- **Where found:** [GOV.UK news](https://www.gov.uk/government/news/companies-house-to-bring-in-changes-to-accounts-filing-from-april-2028); [Using software to file](https://www.gov.uk/guidance/using-software-to-file-your-companys-information).
- **Why it's underserved:**
  - From 1 April 2028, Companies House closes web and paper filing of accounts with "no transition period". Every self-filing dormant and micro company must use iXBRL software.
  - Micro companies must also file a profit and loss account from then.
  - Companies House accounts-only filing for dormant companies, which often don't need a CT600, looks thinner than CT600 filing, but the size of the Companies House software list is **unverified**.
  - The CT600 market shows how quickly this will fill up: about 50 HMRC-listed suppliers, with dormant filing at £5.
- **The idea:** a £5–£10 a year "dormant and micro accounts to Companies House" filer, with deadline reminders built from Companies House data.
- **Automation:** ~70%. **Hours:** 3–6 a week. **Rule breaks:** possibly hours. Companies House software credentials and accuracy liability are real. Customers are limited companies that come inbound, so PECR doesn't apply.
- **First test:** count the providers on the Companies House software list that file dormant or micro accounts, and their prices. Apply for test filing credentials (**unverified** lead time). **Pass:** ≤10 self-filer products under £20 a year.
- **Interest 6, Odds 3** (it's a timed wave and will be crowded by 2028).

## 6. Gift Aid for small charities on WordPress

- **Where found:** WordPress.org search for "gift aid": 15 results, and the top ones are general donation plugins ([qc/wp.json](qc/wp.json)). Off the directory: [UK Gift Aid for WooCommerce, $50, CSV only](https://power-plugins.com/plugin/uk-gift-aid-for-woocommerce/); [Swft, free CSV](https://docs.swft.co.uk/modules/swft-donations/); [Sky Gift Claim, direct to HMRC, no price shown](https://skywebdesign.co.uk/products/sky-gift-claim/).
- **Why it's underserved:** there's no dedicated free Gift Aid plugin on WordPress.org that captures declarations and produces HMRC's Charities Online file. Direct claiming is only available from a small number of vendors who don't show prices.
- **The idea:** a free plugin for declarations and the Charities Online export, with a paid tier that submits claims directly. Direct submission needs HMRC recognition (**unverified** process).
- **Automation:** ~70%. **Hours:** 2–4 a week. **Rule breaks:** borderline. Charities aren't "local businesses", but many are small and local, so treat this as inbound-only through the directory.
- **First test:** publish the free plugin. **Pass:** ≥100 installs in 30 days, or ≥5 requests for direct submission.
- **Interest 5, Odds 3.**

## 7. National bin-day reminder app (breaks rules)

- **Where found:** iTunes Search API ([qc/ios.txt](qc/ios.txt)).
- **Evidence:**
  - SCAMBS Bin Collections, covering one area, has 1,392 ratings.
  - BinDays, a national app, has 348.
  - Council apps are poorly rated: Tameside 2.6★, last updated Jun 2024; East Riding 3.2★, Apr 2024.
- **Why it's underserved:** demand is local and spread across councils, and there are about 300 councils (**unverified**). An open-source scraper project exists (**unverified**, from memory: "UKBinCollectionData" on GitHub).
- **Automation:** ~60%. **Hours:** 4–8 a week. **Rule breaks:** **hours and automation**, because council sites change. Money is weak: ads or a £1.99 unlock.
- **First test:** cover the 20 biggest councils with an off-the-shelf scraper and track installs. **Pass:** ≥30 a day.
- **Interest 4, Odds 2.**

## 8. Heat-pump owner companion (may break rules)

- **Where found:** iTunes Search API: "heat pump" returned 25 apps with **180 ratings in total** ([qc/ios.txt](qc/ios.txt)). Heat Geek Loop has 25 ratings and Havenwise 22.
- **Why it's underserved:** supply is thin. Demand on the App Store isn't proven either, and forum demand is **unverified**.
- **The idea:** an app that reads smart-meter and heat-pump data and shows efficiency (COP) and running cost per day.
- **Automation:** ~60%. **Hours:** 4–6 a week. **Rule breaks:** **possibly automation**, because each manufacturer's API is different.
- **First test:** a waitlist page plus one Reddit/forum post (inbound, so PECR is fine). **Pass:** ≥100 signups in 2 weeks.
- **Interest 6, Odds 2.**

---

## Checked and crowded (don't pursue)

These are the MTD bridging, Renters' Rights Act landlord compliance, dormant CT600, Delay Repay, PCN appeal and Companies House-in-Sheets/Chrome corners listed under the headline finding.

Two more:

- **Companies House identity verification reminders:** the transition ends on 18 Nov 2026 and the check is free through One Login ([GOV.UK](https://www.gov.uk/government/news/companies-house-confirms-identity-verification-rollout-from-18-november-2025)).
- **WordPress UK shipping (Royal Mail, Evri, Parcelforce):** covered by big plugins (flexible-shipping 100k, advanced-shipment-tracking 70k; [qc/wp.json](qc/wp.json)).

## Not covered this run (budget)

- **Etsy (digital), Gumroad, Fiverr, Upwork job posts:** these sites block automated fetches, so checking them would need a browser session.
- **Not scanned:** Product Hunt, Indie Hackers, Google Play (only one entry, from search), the Xero, QuickBooks, HubSpot, Atlassian and Zapier marketplaces, and the MoneySavingExpert and LandlordZone forums.
- **Next cheapest step:** run the same stale-or-badly-rated scan over the Xero App Store and the Atlassian Marketplace, both of which have public listings.
