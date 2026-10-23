# v11 Track B: listing checklists

**Run:** 23 Oct 2026, 23:27–23:30 BST. 177 Flippa SaaS and app listings were harvested from the public search without the LLM (`harvest_listings.py`). Code filters left 100 in scope: the $20k–$150k asking-price band, with content, affiliate, ecommerce and agency listings excluded, capped at 100. Codex medium turned each into a checklist from the listing text only; it did not rank them.

**Mechanical pass rule** (`RULES_LOCKED.md`):
- A hard fail is C1, C2, C3, C7 or C9 marked "looks off", or C1 or C2 marked "missing".
- A listing passes if it has no hard fail and 3 or fewer rows marked "missing".
- Note: Flippa hides detailed financials, traffic and seller notes behind a login. C1 therefore relies on Flippa's "Verified / Vetted / Data Verified" badges and the summary metrics on the public page.

**Result: 5 of 100 pass.**

| Pass | Listing | Price (USD) | Rev/mo | Profit/mo | Verification | Hard fails | Missing |
|---|---|---|---|---|---|---|---|
| **PASS** | [COPA: Football Predictions](https://flippa.com/12822051-new-ai-powered-football-prediction-app-with-recurring-revenue-large-user-base-proven-growth-potential-ready-to-scale-or-monetize-further) | 30000 | 8910 | 629 | “Verified Listing”; listing says Flippa’s vetting team reviewed and verified rev | – | 2 |
| **PASS** | [Subscription SaaS for Amazon Self-Published Authors / 450+ P](https://flippa.com/14387997-subscription-saas-for-amazon-self-published-authors-450-paying-members-70-adjusted-margin-va-run-5-hrs-week) | 118167 |  |  | Flippa says “Vetted + Data Verified Listing” and that its team reviewed and veri | – | 3 |
| **PASS** | [Kliptok](https://flippa.com/12255808-kliptok-cutting-edge-ai-video-saas-sora-2-veo-3-kling-2-6-71-profit-margin-premium-tech-100-organic-mrr) | 22877 | 4950 | 4160 | “Vetted + Data Verified Listing”; Flippa says it verified Revenue, Primary Expen | – | 3 |
| **PASS** | [AI customer service chatbot platform for SMBs](https://flippa.com/14142133-ai-customer-service-chatbot-platform-for-smbs-model-agnostic-80-languages-4-7k-mrr-90-active-clients-zero-owner-hours-declined-from-no-marketing) | 45000 | 6900 | 985 | Revenue, primary expenses, and traffic reviewed by Flippa team or broker; listin | – | 3 |
| **PASS** | [Internet Web Browser for Google TV](https://flippa.com/12008497-internet-web-browser-for-google-tv-4-9k-mrr-2-400-active-subs-2-5m-installs-100-organic-99-margin) | 117782 | 5470 | 5420 | Vetted Listing; Flippa says its team reviewed and verified revenue, primary expe | – | 3 |
| fail | [AI motion graphics SaaS: text prompts to animated charts and](https://flippa.com/14367152-ai-motion-graphics-saas-text-prompts-to-animated-charts-and-kinetic-type-121k-users-315-paying-customers-15k-ttm-revenue-profitable) | 30000 | 1270 | 781 | The listing says “Verified Listing” and “Vetted Listing”; Flippa says its team r | C9 | 1 |
| fail | [Established multichannel messaging and automation SaaS with ](https://flippa.com/13935859-established-multichannel-messaging-and-automation-saas-with-8-250-users-200-300-monthly-inbound-leads-organic-seo-growth-and-recurring-revenue) | 39900 | 1432 | 1121 | “Vetted + Data Verified Listing”; Flippa says it verified revenue, primary expen | C7, C9 | 2 |
| fail | [Web calling app + New StartACall iOS App](https://flippa.com/14424825-web-calling-app-19k-revenue-in-12-months-1-870-paying-customers-52-net-margin-no-paid-ads-60k-organic-clicks-per-month-new-startacall-ios-app) | 63000 | 1690 | 892 | “Vetted + Data Verified Listing”; Flippa says it verified Revenue, Primary Expen | C3, C9 | 2 |
| fail | [Automated SaaS for official business certificates with 15–20](https://flippa.com/12224154-automated-saas-for-official-business-certificates-with-15-20-conversion-65-gross-margins-and-low-maintenance-operations-generating-481-monthly-profit) | 46350 | 3540 | 3490 | “Vetted + Data Verified Listing”; Flippa says it reviewed and verified “Revenue  | C3, C9 | 2 |
| fail | [TechScreen](https://flippa.com/13711417-profitable-ai-interview-saas-with-5-7k-users-1-7k-mrr-94-margins-and-60-100-new-free-signups-daily-from-google-ads) | 39999 | 2628 | 870 | Flippa labels it “Vetted + Data Verified Listing” and says its team reviewed rev | C2, C3, C9 | 2 |
| fail | [15-year-old app turning airline crew rosters into live, self](https://flippa.com/13649898-15-year-old-app-turning-airline-crew-rosters-into-live-self-updating-calendars-1-245-subscribers-91-retention-159-airline-integrations) | 35000 | 1380 | -2150 | Vetted Listing: Flippa says its team or broker reviewed and verified Revenue, Pr | C2, C3, C9 | 2 |
| fail | [AI-powered copy trading SaaS](https://flippa.com/14572180-ai-powered-copy-trading-saas-with-34k-revenue-82-margins-and-a-streamlined-subscription-model-in-a-fast-growing-fintech-niche) | 68870 | 2830 | 2333 | Card says “Business Data Verified”; page says “Vetted + Data Verified Listing” a | C7, C9 | 2 |
| fail | [Next-gen AI SaaS hub automating B2B e-commerce with 1M month](https://flippa.com/11905362-next-gen-ai-saas-hub-automating-b2b-e-commerce-with-1m-monthly-price-adjustments-180k-skus-recurring-revenue-high-retention-and-rapid-growth) | 50000 | 1860 | 1541 | Flippa says the listing is “Vetted + Data Verified” and that its team verified R | C9 | 2 |
| fail | [AI UI builder](https://flippa.com/12410367-ai-ui-builder-with-277-paying-users-5k-mrr-90k-email-list-peaked-at-25k-mo-proven-market-100k-mo-competitors-full-sale-incl-socials-content) | 100000 | 12500 | 4167 | Vetted + Data Verified Listing; Flippa says it verified Revenue, Primary Expense | C9 | 2 |
| fail | [Cloud-based Instagram outreach SaaS](https://flippa.com/14568853-cloud-based-instagram-outreach-saas-finds-leads-sends-ai-personalized-cold-dms-on-autopilot-mrr-2-5k-80-margin) | 60000 | 2340 | 1705 | “Verified Listing”; listing says Flippa vetted and verified revenue, primary exp | C9 | 2 |
| fail | [Virtual Health Solution](https://flippa.com/12530181-automated-nhs-it-business-zero-touch-laptop-provisioning-for-healthcare-professionals-30k-revenue-solo-operated-30-mins-month-to-run) | 101469 | 1690 | 1690 | Vetted Listing: Flippa says its team or the broker reviewed and verified revenue | C3, C9 | 2 |
| fail | [Live Longer - Calorie Counter](https://flippa.com/12877299-live-longer-calorie-counter) | 100000 | 6110 | 1944 | Vetted Listing: Flippa team or broker reviewed and verified revenue, primary exp | C9 | 2 |
| fail | [FootyGPT & FootyAI](https://flippa.com/12616026-footygpt-footyai-ai-football-platforms-with-90k-users-40k-55k-revenue-100-organic-growth-perfectly-timed-for-world-cup-growth) | 20029 | 2670 |  | “Vetted + Data Verified Listing”; Flippa says it verified revenue, primary expen | – | 3 |
| fail | [White-label OTT streaming platform](https://flippa.com/12213658-white-label-ott-streaming-platform-web-ios-android-apple-tv-apps-admin-cms-live-b2b-client-production-codebase-full-source-code-sale) | 33600 | 1340 | 1234 | “Vetted + Data Verified Listing”; Flippa says it verified Revenue, Primary Expen | C9 | 3 |
| fail | [LeadFinder.io](https://flippa.com/12265680-98-margin-b2b-lead-gen-saas-with-767-mo-profit-1-seo-rank-premium-domain-and-100-organic-growth-zero-ad-spend-scalable-and-white-label-ready) | 42444 | 503 | 486 | “Vetted + Data Verified Listing”; Flippa says it reviewed and verified Revenue,  | C2, C3, C9 | 3 |
| fail | [Previously $43k USD MRR business left untouched for 1.5 year](https://flippa.com/13434962-previously-43k-usd-mrr-business-left-untouched-for-1-5-years-comfortably-sitting-at-10k-mrr-being-revived-as-of-aug-2026) | 37306 |  |  | Vetted + Data Verified Listing; Flippa says it reviewed and verified Revenue, Pr | C3, C9 | 3 |
| fail | [Unlocktv IPTV](https://flippa.com/12266720-profitable-iptv-saas-with-814-mo-profit-77-margins-260-active-subscribers-low-churn-and-turnkey-infrastructure-ready-to-scale-in-global-markets) | 30990 | 1060 | 814 | Vetted + Data Verified Listing: Flippa says its team reviewed and verified reven | C9 | 3 |
| fail | [LeadSources.io](https://flippa.com/12888398-lead-source-revenue-attribution-saas-that-connects-campaigns-to-real-revenue-0-cac-low-maintenance-and-1-000-ltv) | 44000 | 1150 | 972 | Vetted + Data Verified Listing; Flippa says it reviewed and verified Revenue, Pr | C9 | 3 |
| fail | [Ikare health](https://flippa.com/12813862-profitable-longevity-health-platform-with-39k-yearly-revenue-66-margins-launched-in-2024-scalable-model-with-recurring-income-and-high-paying-customers) | 40000 | 3250 | 2100 | “Vetted Listing”; Flippa says it reviewed and verified Revenue, Primary Expenses | C7, C9, C1 | 3 |
| fail | [Profitable Presentation SaaS for Smart Glasses](https://flippa.com/13528830-profitable-presentation-saas-for-smart-glasses-5-566-revenue-in-3-months-95-margins-100-organic) | 35203 | 1760 | 1670 | “Vetted Listing”; Flippa says it reviewed and verified Revenue, Primary Expenses | C3, C9 | 3 |
| fail | [Lightloop.io](https://flippa.com/13829251-profitable-generative-ai-product-design-saas-1-3k-mrr-94-margins-fully-automated) | 49900 | 1368 | 1396 | Vetted + Data Verified Listing; Flippa says it verified revenue, primary expense | C9 | 4 |
| fail | [Fondeobot](https://flippa.com/14489587-fondeobot-vende-robots-de-trading-automatico-bots-junto-con-instalacion-servidor-vps-senales-de-trading-y-soporte-tecnico-tambien-pasa-de-examen-de-fondeo) | 139639 | 12400 | 10980 | Flippa labels it “Verified Listing” and says its team or broker vetted the infor | C3, C9, C1 | 4 |
| fail | [Profitable AI Powered Core Banking SAAS/FAAS for SACCOs/MFIs](https://flippa.com/13438355-profitable-ai-powered-core-banking-saas-faas-for-saccos-mfis-banks-40k-monthly-visitors-1-churn-includes-10-revenue-fintech-ecosystem-sub-brands-bundled) | 101600 | 6890 | 5685 | Flippa says the listing is “Vetted + Data Verified” and that its team reviewed a | C9 | 4 |
| fail | [Long-established lottery website/software](https://flippa.com/14407429-long-established-lottery-website-software-become-the-new-owner-of-a-unique-fail-safe-number-reduction-system-serving-english-speaking-countries-worldwide) | 79000 | 2300 | 1972 | “Vetted Listing”; Flippa says it reviewed and verified Revenue, Primary Expenses | C9 | 4 |
| fail | [Am I On AI](https://flippa.com/13527476-established-geo-saas-platform-tracking-brand-visibility-on-chatgpt-ai-search-10k-marketer-leads-70-gross-margins-ideal-for-agencies-and-seo-platforms) | 75000 | 10500 | 7163 | Vetted Listing: Flippa says its team or broker reviewed and verified revenue, pr | C9 | 4 |
| fail | [SaaS / Internet Live chat, CRM, AI support & recurring reven](https://flippa.com/12892377-live-chat-crm-ai-support-recurring-revenue-model-607-users-stripe-billing-low-overhead-production-ready-perfect-for-a-growth-focused-buyer) | 33210 | 3750 | 3750 | No Flippa verification badge or verified Stripe/P&L evidence stated. Listing say | C9, C1 | 4 |
| fail | [We are selling our hosting customer database with recurring ](https://flippa.com/12669012-we-are-selling-our-hosting-customer-database-with-recurring-and-lifetime-hosting-plans-it-is-only-an-asset-transaction-not-a-company-sale) | 57216 | 6390 | 2336 | Vetted + Data Verified Listing; Flippa says its team or broker verified revenue, | C7, C9 | 4 |
| fail | [Fully automated social media growth platform](https://flippa.com/12199374-fully-automated-social-media-growth-platform-50k-orders-from-21-243-customers-35-8-repeat-rate-runs-on-2-3-hours-a-week-seo-and-new-markets-untapped) | 29985 | 13200 | 10301 | “Vetted + Data Verified Listing”; Flippa says it reviewed and verified Revenue,  | C9 | 4 |
| fail | [Barilochense.com](https://flippa.com/12062417-24-year-regional-media-site-with-225k-users-661k-pageviews-year-545-monthly-profit-at-68-margin-zero-outbound-sales-major-growth-upside) | 21500 | 800 | 545 | Data Verified Listing; connected Google Analytics and PayPal integrations. No St | C9, C1 | 4 |
| fail | [LocomotiveCMS](https://flippa.com/12255363-locomotivecms-mature-ruby-on-rails-cms-saas-with-recurring-revenue-loyal-customers-and-low-operating-costs) | 48570 | 928 | 761 | Page says “Vetted + Data Verified Listing”; Flippa team or broker reviewed Reven | C2 | 4 |
| fail | [An AI clone software for creating high converting short-form](https://flippa.com/14140564-an-ai-clone-software-for-creating-high-converting-short-form-content-the-best-quality-in-the-industry-with-a-range-of-low-ticket-and-mid-ticket-customers) | 50000 | 34900 | 10961 | “SaaS / Business Data Verified”; Flippa says it verified revenue, primary expens | C9 | 4 |
| fail | [AI prompt-engineering IDE with a BYOK architecture](https://flippa.com/14330356-ai-prompt-engineering-ide-with-a-byok-architecture-zero-inference-cost-88-profit-margin-1hr-week-owner-time-recurring-subscription-revenue) | 48600 | 2520 | 2225 | Listing says TTM revenue of $31,700 and net income of $29,098 are verified via S | – | 4 |
| fail | [AI-first learning platform with 150,000+ users, 440 subscrib](https://flippa.com/12255097-ai-first-learning-platform-with-150-000-users-440-subscribers-5-6k-mrr-instagram-with-60k-following-millions-of-views-month-strong-growth-potential) | 50000 | 1853 | 1791 | Vetted + Data Verified Listing; Flippa says it reviewed and verified revenue, pr | C9 | 4 |
| fail | [Cloud-based IMS SaaS with 28K ARR, 78% margins, low churn an](https://flippa.com/11797351-cloud-based-ims-saas-with-28k-arr-78-margins-low-churn-and-enterprise-grade-features-offering-strong-recurring-revenue-and-major-global-expansion-potential) | 130847 |  | 2373 | Vetted Listing; Flippa says it reviewed and verified Revenue, Primary Expenses,  | C3, C9 | 4 |
| fail | [A Native Email App Built For Whop with over 7000 installs an](https://flippa.com/12268124-a-native-email-app-built-for-whop-with-over-7000-installs-and-active-users-with-monthly-subscriptions-with-a-shopify-app) | 150000 | 4360 | 3660 | “Vetted Listing”; Flippa says its team or broker reviewed and verified Revenue,  | C9 | 4 |
| fail | [Profitable SaaS with 30K users, 1,500+ HD lessons, 86% margi](https://flippa.com/12214696-profitable-saas-with-30k-users-1-500-hd-lessons-86-margins-500-subscribers-and-zero-ad-spend-ready-to-2-3x-growth-by-expanding-to-global-markets) | 135000 | 2920 | 2517 | “Verified Listing”; “Vetted Listing” says Flippa or broker reviewed and verified | C9, C1 | 4 |
| fail | [AI writing platform for authors — 55K+ users, 320K+ projects](https://flippa.com/12868940-ai-writing-platform-for-authors-55k-users-320k-projects-story-bible-keeps-ai-context-aware-across-chapters-free-99-mo-plans-strong-retention-niche) | 39110 | 1745 | 906 | “Vetted + Data Verified Listing”; Flippa says it reviewed and verified revenue,  | C9 | 4 |
| fail | [AI-powered SaaS with 87% profit margins, strong mobile apps,](https://flippa.com/12218166-ai-powered-saas-with-87-profit-margins-strong-mobile-apps-built-in-automation-crm-and-recurring-revenue-from-50-subscribers-ready-to-scale) | 72960 | 2530 | 2197 | Vetted Listing; Flippa says its team or broker reviewed and verified revenue, pr | C9, C1 | 4 |
| fail | [Codemetrics.ai](https://flippa.com/12777113-codemetrics-ai-is-a-developer-analytics-platform-that-turns-git-activity-into-actionable-insights-on-team-productivity-code-quality-and-engineering-velocity) | 35000 | 675 | 221 | “Vetted + Data Verified Listing”; Flippa says it reviewed and verified “Revenue, | C2, C3 | 4 |
| fail | [Line Verifier Data](https://flippa.com/13415937-it-offers-real-time-verification-services-for-phone-numbers-helping-businesses-ensure-contact-data-accuracy-and-reduce-communication-costs) | 44200 | 5420 | 1181 | “Verified Listing”; Flippa says it reviewed and verified Revenue, Primary Expens | C9 | 4 |
| fail | [AI video dubbing SaaS with $62K ARR, 88% margins, 80% revenu](https://flippa.com/12212870-ai-video-dubbing-saas-with-62k-arr-88-margins-80-revenue-from-returning-users-34-international-3-years-of-growth-fully-automated) | 145000 | 4300 | 3798 | Vetted Listing; Flippa says its team reviewed and verified revenue, primary expe | C3 | 4 |
| fail | [AI platform offering advanced chatbot solutions for business](https://flippa.com/13608369-ai-platform-offering-advanced-chatbot-solutions-for-businesses-to-enhance-customer-interaction-and-streamline-communication) | 45000 | 800 | 620 | “Vetted + Data Verified Listing”; Flippa says it verified “Revenue, Primary Expe | C2, C3, C9 | 4 |
| fail | [Automated ADHD Assessment Platform](https://flippa.com/13329162-automated-adhd-assessment-platform-98-profit-near-zero-owner-time-required-0-ad-spend-0-cac-organic-seo-acquisition-proprietary-software) | 25670 | 2268 | 2228 | Data Verified Listing; connected Stripe integration. No P&L verification stated. | C9 | 4 |
| fail | [LangLang: AI chat translator for Android](https://flippa.com/12686264-langlang-ai-chat-translator-for-android-700k-installs-4-4-96-margin-100-organic-2-hrs-week) | 84490 | 4050 | 3883 | Flippa marks it “Verified Listing” and says its team reviewed and verified reven | – | 4 |
| fail | [Pregnancy Test app: Test Check / Baby & Pregnancy Tracker Ap](https://flippa.com/13836644-pregnancy-test-app-test-check) | 56000 | 3290 | 2331 | Vetted + Data Verified Listing; Flippa says it verified revenue, primary expense | – | 4 |
| fail | [FileGuard: Photo Recovery](https://flippa.com/12385827-fileguard-photo-recovery) | 76368 | 6170 | 2238 | Vetted Listing; Flippa says its team or broker reviewed and verified revenue, pr | – | 4 |
| fail | [Sound Meter: Noise & dB Meter](https://flippa.com/13401120-sound-meter-noise-db-meter) | 33120 | 2770 | 1446 | Verified Listing; Flippa says its team or broker reviewed and verified revenue,  | C9 | 4 |
| fail | [Pandish](https://flippa.com/12207933-gamified-calorie-tracking-app-with-150k-downloads-existing-revenue-strong-4-6-star-ratings-growth-potential-for-a-buyer-willing-to-restart-marketing) | 100000 | 4100 | 1386 | Flippa labels it “Verified Listing” and says its team reviewed and verified reve | C3, C9 | 4 |
| fail | [1.5-Year-Old Cloud Construction Quoting Platform for Subcont](https://flippa.com/11868232-1-5-year-old-cloud-construction-quoting-platform-for-subcontractors-autodesk-partner-card-2-907-mrr-bootstrapped-equity-stake-option) | 20000 | 3542 | 1318 | “Vetted + Data Verified Listing”; Flippa says it reviewed and verified Revenue,  | C9 | 5 |
| fail | [An engineer-led mobile app studio running three revenue line](https://flippa.com/14108706-an-engineer-led-mobile-app-studio-running-three-revenue-lines) | 24900 | 3890 | 3416 | “Vetted + Data Verified Listing”; Flippa says it verified revenue, primary expen | C9 | 5 |
| fail | [Screenify](https://flippa.com/12258905-screenify-is-an-ai-agent-that-conducts-interviews-to-help-qualify-top-of-funnel-candidates-in-your-hiring-pipeline) | 75000 | 4085 | 1517 | Flippa labels it “Vetted + Data Verified Listing”; says its team reviewed and ve | C3, C9 | 5 |
| fail | [ArticleReword.com](https://flippa.com/12206076-profitable-saas-est-2019-earning-20-600-with-90-profit-margin-fully-automated-low-maintenance-and-ready-to-scale) | 91906 | 2260 | 2040 | “Vetted + Data Verified Listing”; Flippa says it reviewed revenue, primary expen | – | 5 |
| fail | [Profitable AI SaaS / $1.9K MRR & 74% gross margin / 230+ sub](https://flippa.com/11936046-profitable-ai-saas-1-9k-mrr-74-gross-margin-230-subscribers-stripe-verified-appsumo-launch-jul-27-ai-presentations-powered-by-google-gemini) | 36659 | 2560 | 698 | “Vetted + Data Verified Listing”; Flippa says it reviewed and verified “Revenue  | – | 5 |
| fail | [Rompolo](https://flippa.com/12354774-profitable-event-saas-with-25k-revenue-20k-profit-80-margins-200k-page-views-and-scalable-subscription-model-with-low-overhead-and-global-demand) | 65000 | 1630 | 1513 | Flippa says the listing is “Vetted + Data Verified” and that its team reviewed a | C9 | 5 |
| fail | [Established AI support SaaS](https://flippa.com/12873277-established-ai-support-saas-with-89k-historical-revenue-revenue-has-declined-seeking-a-buyer-to-acquire-the-platform-build-on-it-and-take-it-forward) | 95000 | 9910 | 9310 | Data Verified Listing; connected Google Analytics integration. No Flippa revenue | C2, C9, C1 | 5 |
| fail | [AI-powered B2B lead generation SaaS with 91 paying users, $7](https://flippa.com/14338888-ai-powered-b2b-lead-generation-saas-with-91-paying-users-7-6k-mrr-and-46k-revenue-combining-lead-discovery-outreach-and-crm-automation) | 70000 | 7630 | 6356 | “Vetted + Data Verified Listing”; Flippa says it reviewed and verified revenue,  | C9 | 5 |
| fail | [Profitable Shopify SaaS + supplement fulfillment platform wi](https://flippa.com/14294368-profitable-shopify-saas-supplement-fulfillment-platform-with-47k-arr-api-access-inventory-equipment-and-established-supplier-relationships) | 38500 | 2540 | 976 | No Flippa verification badge or Stripe/P&L verification is stated. Listing says  | C9, C1 | 5 |
| fail | [An AI powered tool for marketers, SEOs, and entrepreurs.](https://flippa.com/11787310-an-ai-powered-tool-for-marketers-seos-and-entrepreurs) | 29414 | 3880 | 2740 | No Flippa verification badge or Stripe/P&L verification stated. Listing says pay | C9, C1 | 5 |
| fail | [AI-powered tax planning SaaS for accounting pros & HNWIs](https://flippa.com/12933874-ai-powered-tax-planning-saas-for-accounting-pros-hnwis-29-9k-arr-3-churn-239-clients-turnkey-workflow-ready-for-a-growth-marketer-to-scale) | 65000 | 2421 | 2421 | “Business Data Verified”; Flippa says its team reviewed and verified revenue, pr | C9 | 5 |
| fail | [VoiceCheap.ai](https://flippa.com/12216298-ai-video-dubbing-saas-that-translates-clones-voices-and-lip-syncs-videos-into-30-languages-for-creators-courses-and-agencies) | 53140 | 1798 | 1600 | The listing says “Vetted + Data Verified” and states Flippa verified revenue, pr | – | 5 |
| fail | [GrandPlugins Profitable WordPress/WooCommerce plugin portfol](https://flippa.com/12279112-profitable-wordpress-woocommerce-plugin-portfolio-50-plugins-8k-annualized-revenue-23-yoy-growth-zero-marketing-spend-massive-untapped-potential) | 30000 | 616 | 604 | No Flippa verification badge or Stripe/P&L verification is stated. Listing advis | C1 | 5 |
| fail | [n8nchatui.com](https://flippa.com/13478751-n8nchatui-com-is-a-no-code-saas-that-lets-people-build-customize-and-embed-ai-chat-widgets-that-connect-to-their-n8n-ai-automation-workflows) | 34999 | 1310 | 1232 | Vetted + Data Verified Listing; Flippa says it reviewed and verified revenue, pr | – | 5 |
| fail | [The operating system for B2B energy brokers. One platform fr](https://flippa.com/12592459-the-operating-system-for-b2b-energy-brokers-one-platform-from-lead-to-signed-contract-crm-supplier-comparison-e-signature-analytics) | 36737 | 4050 | 3990 | “Verified Listing”; Flippa says its team or broker vetted the listing and review | C9 | 5 |
| fail | [Production-ready email verification SaaS with API, 2.2K user](https://flippa.com/12849062-production-ready-email-verification-saas-with-api-2-2k-users-strong-seo-dr59-300-backlinks-includes-domain-code-infra-scale-from-day-one) | 55889 | 1350 | 789 | “Vetted Listing”; Flippa says its team or broker reviewed and verified “Revenue  | C3, C1 | 5 |
| fail | [Leisio](https://flippa.com/12667051-leisio-est-une-solution-saas-de-creation-instantanee-de-messages-d-accueil-telephonique-professionnels-et-personnalises) | 24333 | 409 |  | “Verified Listing” and “Vetted Listing”; Flippa says its team reviewed and verif | C2, C3, C9 | 5 |
| fail | [Kiddy](https://flippa.com/12103097-kiddy-is-a-multilingual-communication-platform-and-app-that-simplifies-communication-between-parents-and-institutions-such-as-schools-childcare-sports-clubs) | 100000 | 1670 | 0 | “Verified Listing”; Flippa says it vetted and verified Revenue, Primary Expenses | C2, C3, C9 | 5 |
| fail | [Audio to Text for WhatsApp](https://flippa.com/12768374-audio-to-text-for-whatsapp) | 64220 | 2370 | 2176 | Flippa Vetted Listing: team reviewed and verified Revenue, Primary Expenses, and | – | 5 |
| fail | [Automotive AI app, 15K downloads/mo](https://flippa.com/11985223-automotive-ai-app-15k-downloads-mo) | 149990 | 3250 | 3014 | Verified Listing; Flippa says its team vetted revenue, primary expenses, and tra | C3 | 5 |
| fail | [Lumyer](https://flippa.com/12767008-offers-a-platform-for-creating-and-editing-videos-with-effects-relying-on-in-app-purchases-and-subscriptions-for-monetization) | 90861 | 5380 | 3516 | Verified Listing; listing text says Flippa vetted and verified Revenue, Primary  | – | 5 |
| fail | [IPTV Smart Pro - Live TV](https://flippa.com/12223583-iptv-smart-pro-live-tv) | 130500 | 5827 | 5827 | Vetted Listing; Flippa says its team or broker reviewed and verified Revenue, Pr | – | 5 |
| fail | [MFA Authenticator: Secure 2FA](https://flippa.com/12275085-mfa-authenticator-secure-2fa) | 145000 | 3620 | 3609 | “Vetted Listing”; Flippa says its team or broker reviewed and verified “Revenue, | C3 | 5 |
| fail | [AI EdTech SaaS for Teachers / $6,673 MRR / $80K ARR / 428 Su](https://flippa.com/11990705-ai-edtech-saas-for-teachers-6-673-mrr-80k-arr-428-subscribers-growing-recurring-revenue) | 100000 | 1200 | 3436 | Page says “Verified Listing” and “Vetted + Data Verified Listing”; Flippa says i | C2, C3 | 6 |
| fail | [LGBTI Jobs Data Verified](https://flippa.com/13912553-australia-s-national-lgbti-job-board-dedicated-to-assisting-all-graduates-and-jobseekers-connect-with-organisations-engaged-in-lgbti-inclusion-initiatives) | 34225 | 3080 | -1500 | Flippa says the listing is “Vetted + Data Verified” and its team verified revenu | C2, C3 | 6 |
| fail | [Profitable Online Course Selling Business - ~$2.5K/Month / $](https://flippa.com/13717509-profitable-online-course-selling-business-2-5k-month-30-700-lifetime-earnings-established-automated-autopilot-business) | 60000 | 1825 | 1825 | “Vetted Listing”; Flippa says its team or broker reviewed and verified “Revenue, | – | 6 |
| fail | [Profitable SaaS add-on with 15K+ installs, $827 MRR, 97% mar](https://flippa.com/12043701-profitable-saas-add-on-with-15k-installs-827-mrr-97-margins-and-4-5-star-rating-offering-low-maintenance-recurring-revenue-and-strong-growth-potential) | 49000 | 1452 | 584 | Vetted + Data Verified Listing. Flippa says its team or broker reviewed and veri | C3, C9, C2 | 6 |
| fail | [Swedish vehicle history and automotive data SaaS platform](https://flippa.com/13703384-swedish-vehicle-history-and-automotive-data-saas-platform-providing-instant-vehicle-checks-ownership-insights-and-key-vehicle-information) | 30430 | 980 | 507 | Vetted + Data Verified Listing; Flippa says it verified Revenue, Primary Expense | C3, C9, C2 | 6 |
| fail | [An AI-powered tenant referencing platform helping UK landlor](https://flippa.com/13470450-an-ai-powered-tenant-referencing-platform-helping-uk-landlords-and-letting-agents-make-faster-more-informed-tenant-decisions-1-500-properties-80-margins) | 25427 | 676 | -6400 | Vetted + Data Verified Listing; Flippa says it reviewed and verified Revenue, Pr | C2, C3, C9, C1 | 6 |
| fail | [PADEFI is committed to helping you launch and raise funds th](https://flippa.com/11627222-padefi-is-committed-to-helping-you-launch-and-raise-funds-through-various-blockchains) | 35000 | 1860 | 1143 | No Flippa verification badge or Stripe/P&L verification is stated. The listing a | C9, C1 | 6 |
| fail | [AI-powered SaaS platform for job seekers](https://flippa.com/12856617-ai-powered-saas-platform-generating-13-5k-revenue-with-56-margins-launched-2025-scalable-model-with-growing-authority-and-recurring-income) | 31999 | 720 | 470 | Flippa says the listing is “Vetted + Data Verified” and that revenue, primary ex | C3, C2 | 6 |
| fail | [Kodo](https://flippa.com/14084761-kodo-is-an-ai-design-platform-for-editable-presentations-social-graphics-and-more-with-paying-customers-and-ca-2-122-in-august-revenue) | 50358 | 794 | -2500 | “Vetted + Data Verified Listing”; Flippa says it reviewed and verified Revenue,  | C2, C3 | 6 |
| fail | [Custom-built education SaaS](https://flippa.com/11973041-custom-built-education-saas-with-86k-in-development-2-276-users-and-3-years-of-real-transaction-history-live-scalable-and-ready-for-licensing) | 42281 | 462 | 256 | “Vetted Listing”; Flippa says its team or broker vetted the listing and reviewed | C2, C3, C9, C1 | 6 |
| fail | [My Student Lounge](https://flippa.com/10572590-my-student-lounge-is-the-online-student-lounge) | 35000 |  | 0 | No Flippa verification badge or verified financials stated. Listing says “Monthl | C3, C9, C1, C2 | 6 |
| fail | [MasarCO for smart systems (E-Scooter) Project Masarco](https://flippa.com/13400188-masarco-is-a-full-micromobility-business-with-apps-iot-fleet-system-scooters-batteries-and-scalable-gcc-ready-infrastructure-for-acquisition) | 30400 | 317 | 311 | Vetted Listing; Flippa says its team or broker reviewed and verified Revenue, Pr | C3, C9, C2 | 6 |
| fail | [AI SaaS turning product photos into marketing videos](https://flippa.com/12456740-ai-saas-turning-product-photos-into-marketing-videos-43-ai-models-224-mrr-90-margins-310-seo-posts-full-pipeline-production-ready) | 21504 | 224 | 61 | No Flippa verification badge, Stripe verification, or verified P&L stated. The l | C2, C3, C1 | 6 |
| fail | [Android App / Hobbies and Games](https://flippa.com/11895309-a-gps-based-digital-item-collection-game-players-discover-rare-digital-treasures-trade-with-others-and-create-custom-collections-includes-in-app-purchases) | 75000 | 2470 | 2064 | “Vetted Listing”; Flippa says it reviewed and verified Revenue, Primary Expenses | C9, C1 | 6 |
| fail | [AI Video Maker - Hug & Dance](https://flippa.com/11983346-ai-video-maker-hug-dance) | 21150 | 1500 | 1565 | Flippa “Vetted Listing”; says revenue, primary expenses, and traffic were review | C2, C3, C1 | 6 |
| fail | [Confidential (App X)](https://flippa.com/12766308-profitable-ai-powered-aviation-saas-platform-helping-aviation-enthusiasts-and-student-pilots-practice-atc-communications-through-immersive-simulations) | 74900 | 2400 | 2380 | “Verified Listing” / “Vetted Listing”; Flippa says it reviewed and verified Reve | C9, C1 | 6 |
| fail | [RoastGPT - AI Roast Generator](https://flippa.com/12287932-roastgpt-ai-roast-generator) | 100000 | 7480 | 7467 | Verified Listing; Flippa says its team reviewed and verified revenue, primary ex | – | 6 |
| fail | [Learn English Words - Alpa Cards](https://flippa.com/12786053-revenue-generating-english-learning-business-with-195k-l12m-revenue-ios-web-subscriptions-and-growth-upside) | 76160 | 16300 | 5075 | “Vetted Listing”; Flippa says its team reviewed and verified “Revenue, Primary E | – | 6 |
| fail | [Indexing tool SaaS (indexpro.app)](https://flippa.com/12894251-established-saas-business-indexing-tool-in-seo-with-5000-ar-revenue-85-profit-margin-wordpress-plugin-and-android-app-included-good-backlinks-profile) | 25000 | 479 | 435 | Vetted + Data Verified Listing; Flippa says it reviewed and verified revenue, pr | C2 | 7 |
| fail | [Profitable SaaS (est. 2020) generating $9K revenue with 96% ](https://flippa.com/12631135-profitable-saas-est-2020-generating-9k-revenue-with-96-margins-streamline-b2b-and-retail-sales) | 40270 | 557 | 538 | “Vetted Listing” — Flippa says its team or broker reviewed and verified Revenue, | C3, C2 | 7 |
| fail | [Thriving SaaS business in the Business industry with impress](https://flippa.com/12200735-thriving-saas-business-in-the-business-industry-with-impressive-revenue-and-profit-margin-established-in-2024) | 35721 | 1170 | 917 | “Vetted Listing”; Flippa says its team reviewed and verified Revenue, Primary Ex | C3, C1 | 7 |
| fail | [whats-pro.com](https://flippa.com/10526102-saas-internet) | 29000 | 751 | 751 | Card says “Data Verified”; listing page says “Financials are seller-provided inp | C9, C1, C2 | 8 |
| fail | [People Also Ask (Ai)](https://flippa.com/12759034-people-also-ask-ai-a-platform-offering-insights-and-analysis-on-what-people-also-ask-on-any-keyword-topic) | 28080 | 497 | 482 | “Vetted Listing”; Flippa says it reviewed and verified Revenue, Primary Expenses | C2 | 8 |
| fail | [Turnkey e-com biz for innovative antitheft and car security ](https://flippa.com/12005392-turnkey-e-com-biz-for-innovative-antitheft-and-car-security-device-sale-includes-custom-app-database-e-store-inventory-great-investment-for-individual) |  |  |  | No Flippa verification badge or Stripe/P&L verification stated. The listing says | C9, C1, C2 | 8 |

## Subscription SaaS for Amazon Self-Published Authors | 450+ Paying Members | 70%+ Adjusted Margin | VA-Run, 5 hrs/week

https://flippa.com/14387997-subscription-saas-for-amazon-self-published-authors-450-paying-members-70-adjusted-margin-va-run-5-hrs-week

| Row | Status | Evidence | Note |
|---|---|---|---|
| C1 | stated | “Vetted + Data Verified Listing”; Flippa says it verified “Revenue Primary Expenses Traffic” and the seller connected Stripe. | The text does not say revenue was specifically verified through Stripe or a P&L; it also says financials are seller-provided inputs and advises buyers to ask for verified financials. |
| C2 | stated | Card: “Monthly Revenue USD $5K” and “Monthly Profit USD $3.8K.” Page: “MRR AUD $10,600” and “Monthly Profit AUD $5,414 /mo.” | Both displayed currencies and figures indicate revenue above $1,000/month and positive profit. |
| C3 | stated | Asking price “USD $118,167”; card “Profit Multiple 2.6x.” Using the card’s rounded USD figures, $118,167 ÷ ($3,800 × 12) ≈ 2.59x. | The asking price is within $20,000–$150,000 and the stated multiple is below 5x. The page separately gives AUD profit and a 2.6x multiple. |
| C4 | stated | “organic traffic source, primarily unpaid”; “Marketing efforts have been minimal.” | The text describes traffic as primarily organic/unpaid and does not describe owner outreach or sales as the main acquisition channel. |
| C5 | stated | “approximately five hours per week, focusing on member communication”; a virtual assistant “manages daily operations, including data handling and member email dispatches.” | Owner hours and tasks are specified; the listing does not quantify the VA’s hours. |
| C6 | missing | “450+ paying members” and “Total Active Subscribers 826.” | No customer-level revenue breakdown or largest-customer share is provided, so the >20% concentration condition cannot be checked. |
| C7 | stated | Assets include “the platform's domain, source code, Stripe account, and member databases”; owner offers “support after the transition.” | The text identifies transferable assets and does not mention dependence on the seller’s face or personal brand. |
| C8 | missing | “Overall Churn 6%”; “organic traffic source, primarily unpaid”; the service facilitates reviews on “Amazon books.” | No historical revenue or traffic trend is given to check for a decline over 30%. The text does not establish whether Amazon or another platform could restrict the service. |
| C9 | missing | “A virtual assistant manages daily operations”; the owner focuses on “member communication” for “approximately five hours per week.” | A 90-day handover plan and AI-agent coverage are not specified. The text describes member communication and review-platform operations but does not establish which tasks require human judgment or can be automated; post-handover hours cannot be confirmed. |

**90-day handover plan (draft):**
- Days 1–30: Transfer domain, source code, Stripe account, member databases, and access to connected analytics; document current VA procedures.
- Days 31–60: Map member communication, data handling, email dispatches, subscriptions, points bundles, and featured-book upsells; identify tasks suitable for AI-agent automation.
- Days 61–90: Run the documented workflows with the buyer and AI agents, with seller support during transition; measure exceptions and weekly owner time.
- The listing provides no evidence that this plan is feasible or that it would end at five or fewer owner hours per week.

Steady-state hours: The listing states approximately 5 hours/week for the current owner. Post-handover hours are missing; the <=5 hours/week target is unverified.

**Questions for the seller:**
1. Can you provide read-only Stripe access and a monthly revenue and expense breakdown that reconciles the USD and AUD figures?
2. What are the monthly revenue and profit trends for the full two-year age shown, and has either declined by more than 30%?
3. What share of revenue comes from the largest customer, and how many paying members and active subscribers are current?
4. Can you provide a 90-day handover schedule, including seller support, VA duties and hours, and the tasks you expect AI agents to take over?
5. What are the service’s dependencies on Amazon policies or APIs, and have there been any warnings, restrictions, or account risks?

## Kliptok

https://flippa.com/12255808-kliptok-cutting-edge-ai-video-saas-sora-2-veo-3-kling-2-6-71-profit-margin-premium-tech-100-organic-mrr

| Row | Status | Evidence | Note |
|---|---|---|---|
| C1 | stated | “Vetted + Data Verified Listing”; “verified: Revenue Primary Expenses Traffic”; Stripe is connected. | Listing states revenue was verified and Stripe connected; it does not specify a P&L verification. |
| C2 | stated | Monthly Revenue USD $4.95K; Monthly Profit USD $4.16K. | Both exceed the stated thresholds. |
| C3 | stated | Asking price USD $22,877; Monthly Profit USD $4.16K; Profit Multiple 0.5x. | Price is within $20,000–$150,000. Annualized profit is $49,920; asking price ÷ annualized profit ≈ 0.46x, within 5x. |
| C4 | stated | Listing title says “100% Organic MRR”; card says “100% Organic MRR.” | The listing claims organic MRR but does not describe acquisition channels or provide traffic-source details. |
| C5 | stated | “estimated time commitment is about three hours per week, focusing on financial and technical monitoring”; maintenance includes “monitoring API response times and client support concerning prompt quality.” | States about 3 hours/week and describes monitoring and client support tasks. |
| C6 | missing | Customers include “premium content creators, digital marketers, advertising agencies, and independent filmmakers”; clientele is “international, predominantly from the US and Europe.” | No customer-level revenue breakdown or evidence that no customer exceeds 20% of revenue. |
| C7 | missing | “The current owner is selling to focus on a new project”; comprehensive training is offered during transition. | No statement about transferability of accounts, code, API access, or whether sales depend on the owner’s face or personal brand. |
| C8 | looks off | “Overall Churn 28%”; the listing also claims “stable monthly recurring revenue.” | Churn is reported, but no trend data is provided to assess a decline over 30%. The service orchestrates third-party video APIs, but the listing gives no platform-ban or continuity-risk information. |
| C9 | missing | “Operational maintenance demands are minimal”; “client support concerning prompt quality”; “comprehensive training to the buyer during the transition.” | The listing does not give a 90-day handover plan or show that AI agents can handle at least 50% of work and reduce the owner’s time to ≤5 hours/week. Client support is mentioned, with no details about its volume or complexity. |

**90-day handover plan (draft):**
- Days 1–30: Seller trains buyer on the service, API orchestration, prompt workflows, credit management, and cost optimization.
- Days 31–60: Buyer documents deployment, monitoring, billing, and support processes; map API dependencies and credentials for transfer.
- Days 61–90: Buyer takes over monitoring and client support, then evaluates which repeatable tasks can be handled by AI agents.
- After handover: Listing estimates about 3 hours/week for financial and technical monitoring; AI-agent coverage and ongoing support hours are not specified.

Steady-state hours: About 3 hours/week stated; AI-agent coverage and whether the ≤5-hour target can be sustained are not established.

**Questions for the seller:**
1. Can you provide the monthly revenue and expense history, plus the Stripe and P&L records underlying the verified figures?
2. What are the traffic and customer acquisition sources by channel, and what does “100% Organic MRR” mean in those records?
3. What percentage of revenue comes from each of the largest customers, and what are subscriber churn and revenue trends month by month?
4. Which API provider accounts, software, domains, code, and other assets transfer with the sale, and are any provider terms or access limits relevant?
5. What exact tasks, support volume, and hours are included in the 90-day training, and which of them can already be automated with AI agents?

## AI customer service chatbot platform for SMBs

https://flippa.com/14142133-ai-customer-service-chatbot-platform-for-smbs-model-agnostic-80-languages-4-7k-mrr-90-active-clients-zero-owner-hours-declined-from-no-marketing

| Row | Status | Evidence | Note |
|---|---|---|---|
| C1 | stated | “$86,311” trailing 12-month revenue and “$9,054” net income “verified through Stripe”; listing also says “Vetted Listing” and revenue, primary expenses, and traffic were reviewed. | Stripe verification is stated; no Flippa verification badge or P&L verification is specified. |
| C2 | stated | Card: “Monthly Revenue USD $6.9K”; listing: “Monthly Profit USD $985 /mo.” | Both thresholds are met by the stated figures. |
| C3 | stated | Asking price “USD $45,000”; trailing 12-month net income “$9,054.” | $9,054 × 5 = $45,270, so the price is about 4.97× trailing annual profit and within the stated range. |
| C4 | stated | “Customer acquisition remains primarily organic”; operational costs include “Google/Meta ads.” | Organic acquisition is stated as primary, with paid ads also used; traffic-channel breakdown is not provided. |
| C5 | stated | “Current owner dedicating zero hours per week”; operations “managed by contractors.” | Owner tasks are not specified. |
| C6 | missing | “90 active subscribers”; subscription pricing reaches “$1,000 annually.” | No customer-level revenue distribution is given, so concentration above 20% cannot be assessed. |
| C7 | missing | Sale includes “full source code, IP, brand assets, and social media accounts”; contractors are “open to staying post-sale.” | No seller face or personal-brand dependence is stated, but customer, brand, and operational dependence are not assessed. |
| C8 | looks off | “Although revenue has recently declined”; listing headline says “declined from no marketing.” | The decline is stated, but its size and duration are not. No platform-ban risk information is provided. |
| C9 | missing | Owner currently spends “zero hours per week”; seller offers “up to 12 months of transition support”; contractors are “ready to continue operations.” | A 90-day AI-agent handover plan and post-handover hours are not given. Human handoff is part of the product, but the listing does not establish how much ongoing human work it needs. |

**90-day handover plan (draft):**
- Obtain access to source code, hosting, billing, analytics, support records, and contractor runbooks.
- Document deployment, incident response, model and integration changes, billing, refunds, and customer support workflows.
- Have contractors train AI agents on routine support and operational tasks; retain a human escalation path during transition.
- Run the agents alongside contractors, review errors and customer outcomes, and progressively transfer routine work.
- At day 90, measure owner workload and confirm whether ongoing work fits within five hours per week.

Steady-state hours: Not established; the listing states zero current owner hours but gives no post-sale owner-hour estimate.

**Questions for the seller:**
1. Can you provide Stripe read-only access and the monthly revenue and net-income breakdown for the trailing 12 months?
2. What are the monthly revenue trends and customer counts, and how large was the recent decline?
3. What share of revenue comes from each customer, and what are churn and retention by cohort?
4. Which tasks do contractors perform, what do they cost, and will they continue under what terms?
5. Can you provide channel-level acquisition data, paid-ad spend and results, and details of any platform, policy, or account risks?

## COPA: Football Predictions

https://flippa.com/12822051-new-ai-powered-football-prediction-app-with-recurring-revenue-large-user-base-proven-growth-potential-ready-to-scale-or-monetize-further

| Row | Status | Evidence | Note |
|---|---|---|---|
| C1 | stated | “Verified Listing”; vetted listing says revenue, primary expenses, and traffic were reviewed and verified. | This is a Flippa verification claim; the text does not mention Stripe or P&L verification. |
| C2 | stated | Monthly Revenue USD $8.91K; Monthly Profit USD $629 /mo. | Revenue exceeds $1,000/month and stated profit is positive. |
| C3 | stated | Asking price USD $30,000; monthly profit $629; profit multiple 4.0x. | Price is within $20,000–$150,000. Annualized stated profit is $7,548; $30,000 ÷ $7,548 ≈ 3.97x, within 5x. |
| C4 | looks off | “The user base…is largely acquired through paid social media campaigns.” | Acquisition is described as mostly paid social, not organic, app-store, or marketplace acquisition. |
| C5 | stated | “Operations require minimal effort, estimated at about two hours per week,” for “push notifications, performance monitoring, and updates.” | Current stated workload is about 2 hours/week; no further task breakdown is given. |
| C6 | missing | “Revenue primarily comes from in-app purchases.” | No revenue share or customer-level breakdown is provided to establish whether any one customer exceeds 20%. |
| C7 | stated | Sale includes “full intellectual property, codebase, branding, and a detailed onboarding guide”; app has “over 200,000 downloads.” | No face or personal-brand reliance is stated. Transfer is described, but the listing does not detail account, store, or third-party rights transfer. |
| C8 | looks off | “Overall Churn 40%”; “seasonal fluctuations”; users “engage most during major football events”; acquisition is largely paid social. | The text gives no revenue trend sufficient to assess a decline over 30%. Paid-social dependence creates acquisition-platform exposure; no platform-ban risk is described. |
| C9 | missing | “Minimal maintenance requirements”; estimated 2 hours/week; tasks include push notifications, performance monitoring, and updates. | No 90-day handover steps or AI-agent operating plan are stated, so ≤5 hours/week after handover is not established. |

**90-day handover plan (draft):**
- Listing provides no 90-day handover plan.
- Request access and transfer steps for app stores, Bubble.io, payment/subscription systems, analytics, and ad accounts.
- Document push notification, monitoring, and release/update procedures with the seller.
- Have the buyer validate subscription revenue, churn, paid-social performance, and seasonal patterns during handover.
- After transfer, measure whether routine monitoring and updates can be delegated to AI agents within the stated workload.

Steady-state hours: About 2 hours/week claimed by the listing; AI-agent share and post-handover workload are not stated.

**Questions for the seller:**
1. Can you provide read-only access or exports showing monthly revenue, expenses, and subscription receipts for the last 24 months?
2. Please share customer-level revenue concentration data and subscription cohort, churn, refund, and annual-plan renewal figures.
3. What are monthly downloads and acquisition costs by channel, including paid-social spend, app-store organic traffic, and ROAS by campaign?
4. What exact accounts, code, IP, app-store listings, payment integrations, and third-party contracts transfer, and are any tied to your personal identity?
5. What are the specific 90-day handover deliverables, and which recurring tasks require your judgment or manual work after transfer?

## Internet Web Browser for Google TV

https://flippa.com/12008497-internet-web-browser-for-google-tv-4-9k-mrr-2-400-active-subs-2-5m-installs-100-organic-99-margin

| Row | Status | Evidence | Note |
|---|---|---|---|
| C1 | stated | “Vetted Listing”; Flippa says it “verified: Revenue Primary Expenses Traffic.” | The listing states Flippa vetted these areas; it does not mention a Stripe or P&L badge. |
| C2 | stated | Monthly revenue USD $5.47K; monthly profit USD $5.42K. Description: “€4,900 in monthly revenue” and “99% profit margin.” | Stated revenue exceeds $1,000/month and profit is positive. |
| C3 | stated | Asking price USD $117,782; monthly profit USD $5.42K; displayed profit multiple 1.8x. | Price is within $20K–$150K. Annualized stated profit is $65,040; asking price divided by that is about 1.81x, below 5x. |
| C4 | stated | “2.5M+ organic installs”; “100% Organic”; “zero ad spend.” | Listing attributes acquisition to organic installs and reports no ad spend. |
| C5 | stated | “The app needs about 0–1 hour per month and no own server.” | The listing gives current time but does not specify the seller’s tasks. |
| C6 | missing | “About 2,500 active subscriptions”; no customer-level revenue breakdown stated. | Subscription count is given, but the text does not establish whether any one customer contributes over 20% of revenue. |
| C7 | missing | Sale includes “Google Play app transfer with existing subscribers, the complete source code with handover documentation, the Firebase project.” | Transferable assets are described; seller face or personal-brand dependence is not addressed. |
| C8 | missing | Revenue “stable between €4.5K and €5.2K per month”; live on Google Play “since May 2021.” | The stated range does not indicate a decline over 30%, but the listing gives no historical trend detail or evidence about platform-ban risk. |
| C9 | stated | “0–1 hour per month”; “no own server”; includes source code, handover documentation, and “2 weeks of technical support.” | A plausible 90-day handover: 1) transfer the Play app and subscriptions; 2) transfer Firebase and source code; 3) review handover documentation and operational access; 4) use the two weeks of support to resolve technical questions; 5) document recurring checks and monitor subscription revenue. The listing supports a low-hours estimate, but does not describe automation or prove that AI agents can perform at least 50% of ongoing work. |

**90-day handover plan (draft):**
- Transfer the Google Play app and existing subscribers to the buyer.
- Transfer the Firebase project and complete source code.
- Review the handover documentation and confirm access to the required services.
- Use the included two weeks of technical support to resolve handover questions.
- Document recurring checks and monitor subscription revenue during the 90-day transition.

Steady-state hours: Listing states about 0–1 hour per month; it does not specify which tasks this includes.

**Questions for the seller:**
1. Can you provide read-only access to Google Play Console and supporting reports showing monthly revenue, refunds, fees, and subscriber counts for the last 12 months?
2. Can you provide customer or subscriber revenue concentration data, including whether any single payer accounts for more than 20% of revenue?
3. What specific recurring tasks make up the stated 0–1 hour per month, and which have required technical intervention in the past year?
4. Can you share monthly install, active user, subscription, and revenue history since May 2021, plus any Google Play policy notices, suspensions, or account risks?
5. What exactly is included in the app, Firebase, source-code, and subscriber transfer, and what support or transition assistance is available beyond the two weeks?
