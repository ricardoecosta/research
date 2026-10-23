# v9 validation (METHOD step 10)

**Run:** 23 Oct 2026, 17:26–17:31 BST. Claude Opus 5.5 with live WebSearch/WebFetch, one call per candidate, on the top 8 of `SCORES.md`. Grok Bot did not add its own web checks (no pursue/maybe to spot-check).

**Result: 0 pursue, 0 maybe, 8 kill.** No maybe arose, so no in-iteration desk test was triggered (several validators ran their deciding desk check anyway; see each entry).

| # | ID | Candidate | Source | Verdict | Confidence | One-line reason |
|---|---|---|---|---|---|---|
| 1 | L074 | Foreign-currency bank-feed importer for MTD | S4 | **kill** | medium | Kill under K3: Wise has official integrations with FreeAgent and Xero that feed foreign-currency accounts into MTD-compatible software, FreeAgent can be free, and the only gap found is in Clear Books' cheapest plans, so a separate formatter has no lasting wedge. |
| 2 | L003 | Accountant multi-client Companies House filing console | S1 | **kill** | high | The April 2028 iXBRL mandate is real and was confirmed today, but the multi-client filing space is already crowded with low-cost incumbents that offer multi-client dashboards and batch filing. At least two practice-capable Companies House filing products appear to have launched since April 2026, and the change most likely to create new demand (small and micro companies filing their P&L) was paused today. |
| 3 | L019 | SAML Request Tracer successor | S2 | **kill** | high | This fails K2 (copy speed) on re-check: at least two direct, free SAML-debugging extensions launched after 23 Apr 2026. One of them, ClavionX, already ships the planned wedge (explaining configuration mistakes and redacted exports) for free. The 400k-user incumbent is free, maintained and BSD-licensed, and there is no evidence anyone pays for this. |
| 4 | L009 | Contractual land-rights submission preparation tool | S1 | **kill** | medium | The legal duty is real and has fixed dates, but the government's own figure puts total ongoing business compliance cost at only about £3.7m a year, HM Land Registry (HMLR) is building the submission service and mapping tools itself, a regulated lawyer must personally submit, and there is no evidence anyone would pay. The opportunity is too small and too exposed to HMLR to meet Ricardo's success and 5 h/week limits. |
| 5 | L037 | Fire-and-rehire decision record tool | S1 | **kill** | medium | Few employers have this problem, the government aims to shrink it, the start date keeps moving, and free advice from Acas or advice bundled with existing HR services already covers it. I found no evidence that anyone pays for it within the last 18 months, so a SaaS product would be unlikely to reach meaningful revenue in 12 months. |
| 6 | L014 | Hey Product Page Banner support-rescue alternative | S2 | **kill** | high | Re-checking the launches kills this lead on K2 copy-speed: at least 2 product-page banner apps have launched since 23 Apr 2026, plus a near-identical one on 1 Apr 2026. The rescue/monitoring angle rests on 2 support complaints, and the core widget is already free or $4.99/month from 6+ apps. |
| 7 | L070 | Spreadsheet-to-MTD transaction importer | S4 | **kill** | high | Killed on K2 and K4. Two competing products went live after 23 Apr 2026: NJT Tax Return Manager, which is built in Access (20 Jun 2026), and suiteSheets (submissions live by 9 Jul 2026). At least 7 incumbents cost £30/yr or less, including a free one that imports CSV with column mapping. The only demand evidence is one Reddit anecdote with no purchase. |
| 8 | L031 | Landlord ombudsman complaint workflow | S1 | **kill** | medium | Mandatory ombudsman membership is not expected until 2028. The government has already said the Ombudsman will give landlords complaint-handling tools. Bundled incumbents and a pre-launch £6.99/month rival already cover the record-keeping. No one was found paying for a complaint workflow inside the 12-month window. |

## L074 Foreign-currency bank-feed importer for MTD: kill (medium)

Kill under K3: Wise has official integrations with FreeAgent and Xero that feed foreign-currency accounts into MTD-compatible software, FreeAgent can be free, and the only gap found is in Clear Books' cheapest plans, so a separate formatter has no lasting wedge.

**Why**

- Platform/partner overlap (K3): Wise runs an official integration with FreeAgent. FreeAgent says you add one bank account per Wise currency, such as 'Wise GBP' and 'Wise EUR', and enable a Wise feed for each one: https://support.freeagent.com/hc/en-gb/articles/360016070920/ ; https://wise.com/gb/business/freeagent ; https://www.wise.com/help/articles/2978070/connecting-your-wise-account-with-freeagent
- FreeAgent's sole-trader plan, with full MTD Income Tax submission and support for multi-currency bank accounts, costs £0 for people with a NatWest, RBS or Ulster Bank business current account, or a Mettle account used at least once a month. Otherwise it is £19/month. This is a free bundled substitute: https://www.freeagent.com/pricing/ ; https://www.freeagent.com/en/features/banking/
- Wise also syncs directly with Xero every 4 hours. Xero includes multi-currency from its Comprehensive plan, £55/month after the introductory period: https://wise.com/help/articles/2960335/how-do-i-manually-upload-my-wise-statements-to-xero ; https://www.xero.com/uk/pricing-plans/
- The gap only appears in cheap MTD-only plans. Clear Books' MTD Income Tax plans (£0 or £5/month) list no multi-currency, which appears only on the Large plan at £44/month. Clear Books, or a low-cost rival, could close this gap quickly. Already live: TaxMTD advertises Wise and Revolut multi-currency feeds, and lists multi-currency on its Business plan at £39–49/month. Announced but not yet live: Pippa plans a £6/month Pro tier with 'FX at HMRC spot rate', 'later in 2026': https://www.clearbooks.co.uk/pricing/ ; https://taxmtd.uk/ ; https://pippa.tax/
- Demand is not established. The two Reddit signals cited in the lead could not be fetched (reddit.com blocked automated access). Searches of Reddit and AccountingWEB found no MTD-ITSA foreign-exchange complaint dated within 18 months. The AccountingWEB thread found is from 2019 and about MTD for VAT, and its replies already point to FreeAgent's automatic FX conversion: https://www.accountingweb.co.uk/any-answers/mtd-for-foreign-currency-records
- Free converters already exist for the technical core. ofxstatement-wise, an open-source tool, converts Wise CSV exports to OFX, which FreeAgent accepts: https://github.com/Wigny/ofxstatement-wise ; https://www.propersoft.net/howto/import-csv-as-ofx-into-freeagent/

**Competitors checked**

| Name | Price | Launched | URL |
|---|---|---|---|
| FreeAgent (official Wise feed, multi-currency, MTD ITSA) | £19/month ex VAT (intro £9.50); £0 with NatWest/RBS/Ulster/Mettle | Wise partnership announced 2020 | https://www.freeagent.com/pricing/ |
| Xero (official Wise sync, multi-currency) | £55/month Comprehensive, £70/month Ultimate (after the 6-month intro) | established | https://www.xero.com/uk/pricing-plans/ |
| TaxMTD (Wise/Revolut multi-currency feeds) | Free to £129/month; multi-currency listed on Business at £39/month annual, £49 monthly | unverified (site shows 'v1.0.5-24Beta', 'MTD ready for April 2026') | https://taxmtd.uk/ |
| Pippa (cross-currency FX at spot rate) | £0 Free; £6/month Pro | not launched; 'later in 2026'; HMRC listing pending | https://pippa.tax/ |
| Clear Books (gap: no FX feeds on MTD plans) | MTD plans £0/£5/£15; multi-currency on Large plan £44/month | established | https://www.clearbooks.co.uk/pricing/ |
| QuickFile (CSV/OFX import; MTD ITSA requires Power User) | unverified (no price shown on the pages fetched) | established | https://support.quickfile.co.uk/t/making-tax-digital-mtd-for-income-tax-a-guide-for-existing-users/63237 |
| ofxstatement-wise (open source) | free | unverified | https://github.com/Wigny/ofxstatement-wise |

**Demand:** Only the broad MTD population is verified (864k people in scope from April 2026, more cohorts in 2027 and 2028): https://www.gov.uk/government/statistics/making-tax-digital-for-income-tax-business-population-statistics/making-tax-digital-for-income-tax-business-population-statistics-commentary. The two Reddit posts (2025-09 and 2026-04) could not be fetched live and remain unverified. No other foreign-currency MTD complaint dated within 18 months was found. The FX segment's size, search volume and willingness to pay are all unverified.

**Legal:** Lawful as a file formatter. HMRC accepts CSV import/export as a digital link, but the user must still submit through compatible MTD software (https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/create-digital-records). FX method must be applied consistently under BIM39500 onward (https://www.gov.uk/hmrc-internal-manuals/business-income-manual/bim39510). No regulatory block found, but wrong exchange rates create liability and support risk.

**Channel:** SEO pages for specific bank and app combinations, and moderator-approved community posts. Both are lawful under PECR as long as there are no cold DMs or emails to sole traders (https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/). The search intent this content would target is answered by free help pages from Wise and FreeAgent.

**Owner hours:** 2–5 h/week claimed; unverified. Support for parsing banks' CSV formats and FX-method questions could push it higher.

**Desk check run:** Ran a live check for substitutes and demand. Substitutes: confirmed official Wise integrations with FreeAgent (multi-currency, per currency) and Xero, FreeAgent's £0 plan for NatWest/RBS/Ulster/Mettle customers, Clear Books multi-currency limited to the £44 Large plan, TaxMTD advertising Wise/Revolut multi-currency, Pippa not yet launched, and the free ofxstatement-wise converter. Demand: Reddit could not be fetched; Reddit and AccountingWEB searches found no foreign-currency MTD-ITSA complaint dated within 18 months, only a 2019 VAT-era thread. Result: K3 is triggered (partner integration serves the need, free or bundled), and no live demand evidence dated within 18 months.

**First test (if revived):** n/a (killed). For a recheck: in about 6 months, look for complaints that FreeAgent or Xero handle Wise or Revolut FX badly once the £30k cohort arrives in April 2027.

**Unverified:**
- Reddit comment of 2025-09-09 on an FX-feed workaround (fetch blocked)
- Reddit report of Sage fees rising from £46.80 to £70.80 after a foreign-currency tier change (fetch blocked)
- Clear Books support article on foreign-currency feeds (SSL fetch failure); the workaround described in the lead is unconfirmed live
- QuickFile Power User and bank-feed prices
- TaxMTD launch date, which plan includes the Wise feed, and HMRC recognition
- Number of MTD users holding foreign-currency accounts; search volume
- Owner hours and the 65% automation share

## L003 Accountant multi-client Companies House filing console: kill (high)

The April 2028 iXBRL mandate is real and was confirmed today, but the multi-client filing space is already crowded with low-cost incumbents that offer multi-client dashboards and batch filing. At least two practice-capable Companies House filing products appear to have launched since April 2026, and the change most likely to create new demand (small and micro companies filing their P&L) was paused today.

**Why**

- K1/K6 pass, and the trigger is live and dated today. On 23 Oct 2026 Companies House said: 'from April 2028, we will require all UK registered companies to file their accounts in … iXBRL … using commercial software … This requirement is going ahead as planned', covering 'those who use third party agents or accountants'. Web and paper accounts filing will close. https://www.gov.uk/government/news/companies-house-update-to-accounts-filing-from-april-2028
- The same announcement removes some of the new demand. Government 'decided to pause implementing the requirement for small companies and micro-entities to file profit and loss accounts' and keeps abridged and filleted accounts. That cuts the extra disclosure work a new tool could have charged for. https://www.gov.uk/government/news/companies-house-update-to-accounts-filing-from-april-2028
- K2 copy-speed fails on re-check, though both launch dates are inferred. AccountsGear is a direct practice-focused trial balance → accounts → iXBRL → filing product at £35/month for 10 clients. Its earliest dated content is 7 Jul 2026, it says it has no customer evidence yet, and its launch date is unverified (https://accountsgear.co.uk/, https://accountsgear.co.uk/blog). Taxley says its Companies House accounts filing has been 'live since 28 September 2026', with an 'agent mode' for accountants (https://taxley.co.uk/). Both dates fall after 23 Apr 2026, so the count reaches 2.
- K4 incumbents fail. At least 5 maintained products sit at or below a plausible price floor. TaxCalc is £164/yr for 12 clients and already has a batch filer (https://shop.taxcalc.com/accountancy-software-prices, https://www.taxcalc.com/products/tax-and-accounts). TinyTax is £189/yr for 12 companies and £999/yr for 1,000, with a Multi-Client Dashboard and bulk plans (https://tinytax.co.uk/pricing). Andica starts at £100/yr (https://www.andica.com/andica-accounts-production-software-cloud-pricing.html), IRIS Elements at £125.18 per user per year (https://www.iris.co.uk/products/iris-elements/accounts-production/), and Forbes at £335/yr (https://www.tax.co.uk/products_accounts.html). Bright, Silverfin, Digita and Absolute also sell iXBRL accounts production (https://brightsg.com/brightap-cloud-based-accounts-production-software/, https://silverfin.com/en-gb/product/accounts-production/, https://www.absolutetax.co.uk/products/absolute-integrated/absolute-accounts). No UK or niche wedge is evident, because the proposed 'readiness/exception queue' overlaps existing batch filing and multi-client dashboards.
- Ecosystem platforms are moving into the space. Xero launched limited-company accounts production in March 2026 (https://blog.xero.com/uk/product-updates/streamlined-accounts-production/). Sage launched multi-client Period Review on 15 Sep 2026 (https://www.sage.com/en-gb/company/digital-newsroom/2026/09/sage-unveils-period-review-to-help-accountants-and-bookkeepers-manage-growing-mtd-workload/). Companies House itself offers no free tool after 2028; the 23 Oct announcement only points to a list of software providers (https://www.gov.uk/government/news/companies-house-update-to-accounts-filing-from-april-2028). This is not a K3 kill, but it adds pressure.
- Fit with Ricardo's agent-run model is poor. Statutory filings carry liability, and failed or rejected iXBRL filings need human support, so ≤5 h/week is doubtful. Taxonomy changes are also ongoing upkeep. https://www.gov.uk/guidance/using-software-to-file-your-companys-information

**Competitors checked**

| Name | Price | Launched | URL |
|---|---|---|---|
| AccountsGear (Super Digital Solutions Ltd) | £35/mo for 10 clients; £99/mo for 40; £249/mo for 150; £549/mo unlimited (ex VAT) | Around Jul 2026, inferred from earliest blog post (7 Jul 2026); exact date unverified | https://accountsgear.co.uk/ |
| Taxley | Per filing: £9.50 dormant, £39.95 micro, £129 small; Companies House filing included | Companies House accounts filing 'live since 28 September 2026'; product launch date unverified | https://taxley.co.uk/ |
| TinyTax | £189/yr for 12 companies, £319 for 50, £549 for 150, £999 for 1,000 (ex VAT) | Established; date unverified | https://tinytax.co.uk/pricing |
| TaxCalc Accounts Production + Batch Filer | £164/yr for 12 clients, £368 for 50, £744 for 150, £1,050 for 1,000 (ex VAT) | Established | https://shop.taxcalc.com/accountancy-software-prices |
| Andica Cloud Accounts Production | From £100/yr ex VAT | Established | https://www.andica.com/andica-accounts-production-software-cloud-pricing.html |
| IRIS Elements Accounts Production | £125.18 per user per year plus client band; 10-client minimum | Established | https://www.iris.co.uk/products/iris-elements/accounts-production/ |
| Forbes Accounts | £335/yr + VAT | Established | https://www.tax.co.uk/products_accounts.html |
| Capium | From £140/mo for 100 clients (suite) | Established | https://www.capium.com/pricing/ |
| Xero accounts production (UK) | Bundled in Xero practice tools; iXBRL Companies House filing unverified | Mar 2026 | https://blog.xero.com/uk/product-updates/streamlined-accounts-production/ |

**Demand:** There is real, dated regulatory demand. The software-only iXBRL mandate from April 2028 was reconfirmed on 23 Oct 2026 (https://www.gov.uk/government/news/companies-house-update-to-accounts-filing-from-april-2028). Companies House expects about 2.2m accounts a year, about 75% already filed electronically (https://download.companieshouse.gov.uk/en_monthlyaccountsdata.html). That means about 25% of filers must switch, and most of them are directors filing their own accounts, not accountants. Accountants mostly already use commercial software, which limits new practice-side demand. No product-specific willingness-to-pay evidence dated ≤18 months was found. The only revenue figure (TaxCalc parent turnover for the year to 31 Mar 2025) is older than 18 months and gets zero weight (https://find-and-update.company-information.service.gov.uk/company/03948264/filing-history).

**Legal:** Selling software to UK accountancy practices is lawful. The product must use Companies House's software filing gateway and follow its taxonomy and validation rules (https://www.gov.uk/guidance/using-software-to-file-your-companys-information). The software finder is a directory, not an endorsement (https://www.gov.uk/software-company-accounts). The product would process client financial data, so UK GDPR and processor controls apply, and incorrect statutory filings create liability. Professional indemnity needs are unverified.

**Channel:** A lawful channel exists through SEO on the 2028 change, the Companies House software finder, and paid search. Accountancy practices that are limited companies are corporate subscribers, so B2B email to them is permitted with opt-out. Sole-practitioner accountants would need consent. https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/ The channel is crowded, though: TaxCalc, Xero, Taxley, TinyTax and others already publish 2028 guides (https://www.taxcalc.com/blog/companies-house-accounts-filing-changes-april-2028, https://taxley.co.uk/guides/companies-house-software-only-accounts-filing-2028).

**Owner hours:** Unverified. Supporting statutory filings (rejections, taxonomy updates, deadline-season spikes) for accountants is unlikely to fit ≤5 h/week at steady state.

**Desk check run:** n/a. The verdict is kill, not maybe. As part of re-checking K2 and K4, I compared prices and features of AccountsGear, Taxley, TinyTax, TaxCalc, Andica, IRIS and Forbes live. TinyTax and TaxCalc already cover the multi-client dashboard and batch filing wedge at £164–£189/yr for 12 clients.

**First test (if revived):** n/a (kill). If this were ever revisited, the only angle left is a non-filing data layer, such as a portfolio-wide 2028-readiness audit built from free Companies House bulk accounts data. That would be a different lead and would need its own kill-check.

**Unverified:**
- AccountsGear exact launch date and paying customers
- Taxley product launch date (only the Companies House filing go-live, 28 Sep 2026, is stated)
- Whether Xero's March 2026 accounts production files iXBRL directly to Companies House
- Practice-side willingness to pay for a readiness/exception layer
- Owner hours and automation share
- Number of products in the Companies House software finder (it is a step-by-step tool and no list was retrievable)
- TinyTax traction claims, which are internally inconsistent (80k filings vs 1,000+ companies)

## L019 SAML Request Tracer successor: kill (high)

This fails K2 (copy speed) on re-check: at least two direct, free SAML-debugging extensions launched after 23 Apr 2026. One of them, ClavionX, already ships the planned wedge (explaining configuration mistakes and redacted exports) for free. The 400k-user incumbent is free, maintained and BSD-licensed, and there is no evidence anyone pays for this.

**Why**

- K2 fail, launch 1: Awesome SAML Tracer's first GitHub commit is dated 11 May 2026 ('Initial release: Awesome SAML Tracer Chrome extension'). Chrome-Stats gives its creation date as 19 May 2026. The listing says it is free and open source. https://github.com/jsegers1974/awesome-saml-tracer ; https://chromewebstore.google.com/detail/awesome-saml-tracer/pilkjgooejhajccieiebbihilnclbpej
- K2 fail, launch 2: Product Hunt lists 'SAML Debugger by ClavionX' as Free, 'Launched in 2026' and 'Launched 3mo ago', which puts it around July 2026, well after the 23 Apr 2026 cutoff. Its description says it 'correlate[s] requests with responses, explain[s] common configuration mistakes, identif[ies] protocol and security issues, and export[s] redacted diagnostics for collaboration'. https://www.producthunt.com/posts/saml-debugger-by-clavionx ; https://samldebugger.clavionx.com
- The proposed defensible asset (a diagnostic rules engine with safe team handoffs) is already offered for free by ClavionX, and partly by SSO Tracer on Firefox, which 'flags common failure causes' with redaction on by default. That leaves no evident wedge. https://www.producthunt.com/posts/saml-debugger-by-clavionx ; https://addons.mozilla.org/en-US/firefox/addon/sso-tracer-saml-oidc-debugger/
- The category is not empty. SimpleSAMLphp SAML-tracer has 400,000 Chrome users, is rated 4.5 from 36 ratings, version 1.9.5 was updated on 20 Aug 2026, and it is free. On Firefox it has 21,442 users and was updated on 30 Jul 2026. https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch ; https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/
- There is no evidence of willingness to pay. Every live competitor found is free. samltracer.com, the only paid offer ($2.90/month), returned HTTP 402 today, and its Chrome listing ID shows as removed. The AppBox claim about paying subscribers is self-reported and has no figures. https://samltracer.com/ ; https://groups.google.com/a/chromium.org/g/chromium-extensions/c/m9V8BJOgTEg

**Competitors checked**

| Name | Price | Launched | URL |
|---|---|---|---|
| SAML-tracer (SimpleSAMLphp) | Free, BSD-2 | Long-established; v1.9.5 updated 2026-08-20 (Chrome), 2026-07-30 (Firefox) | https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch |
| Awesome SAML Tracer | Free, open source | First commit 2026-05-11; Chrome-Stats creation date 2026-05-19 | https://github.com/jsegers1974/awesome-saml-tracer |
| SAML Debugger by ClavionX | Free | 2026, around July (Product Hunt '3mo ago'; exact day unverified) | https://www.producthunt.com/posts/saml-debugger-by-clavionx |
| SSO Tracer: SAML & OIDC Debugger (Ninjalabs, Firefox) | Free, MIT | First version 0.3.0 on 2026-02-15 (before the cutoff); 123 users | https://addons.mozilla.org/en-US/firefox/addon/sso-tracer-saml-oidc-debugger/versions/ |
| Entra Auth Tracer | Free, open source | Chrome-Stats creation date 2026-04-07 (before the cutoff) | https://github.com/darrenjrobinson/EntraAuthTracer |
| SAML Chrome Panel | Free, open source | Older | https://github.com/milton-lai/saml-chrome-panel |
| SAMLScope | Free per a review | Review dated 2026-06-01; the product itself is not verified | https://toolsforchrome.com/samlscope-saml-tracer-chrome-extension-review |
| samltracer.com 'SAML Tracer' | $2.90/month or $9.90 lifetime (unverified; the site returned HTTP 402) | Unknown; the store listing appears removed | https://samltracer.com/ |

**Demand:** People clearly use this kind of tool, but nobody is shown paying for it. The free incumbent has 400k Chrome users (updated 20 Aug 2026) and 21,442 Firefox users (updated 30 Jul 2026), and GitLab and Okta documentation still tells users to install SAML tracers. No paid buyer, paid plan or revenue was found dated within the last 18 months. https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch ; https://docs.gitlab.com/user/group/saml_sso/troubleshooting/ ; https://developer.okta.com/docs/guides/saml-tracer/main/

**Legal:** No UK legal blocker. Distributing through browser stores and SEO is lawful. A local-only design that collects no trace data avoids most UK GDPR exposure. Chrome Web Store policy requires disclosure of data handling and minimal permissions, and Chrome DevRel's July 2026 comments in the AppBox thread show real removal risk for monetised extensions. https://developer.chrome.com/docs/webstore/program-policies/policies/ ; https://groups.google.com/a/chromium.org/g/chromium-extensions/c/m9V8BJOgTEg

**Channel:** There is a lawful inbound channel (browser-store search, GitHub, SEO troubleshooting guides) that needs no face and no PECR-banned outreach. ICO guidance treats private social DMs as electronic mail, so they must not be used. However, three or more free tools now compete for the same store searches. https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/key-concepts-for-direct-marketing-using-electronic-mail/

**Owner hours:** Unverified. A local-only extension could plausibly stay under 5 hours a week. A paid team-sync product, which is the only plausible way to make money here, would need a security review and support, so 5 hours a week is unproven.

**Desk check run:** n/a. The verdict is kill rather than maybe. I did re-check copy speed live: two direct launches after 23 Apr 2026 were found (Awesome SAML Tracer, first commit 11 May 2026; ClavionX SAML Debugger, launched in 2026, around July), which is enough to trigger K2. I also checked whether anyone sells a paid version: none of the current competitors charges, and samltracer.com returned HTTP 402.

**First test (if revived):** None recommended (killed). If this is ever revisited, it would only be as a paid enterprise IdP-diagnostics product, which is a different lead with a sales motion.

**Unverified:**
- Exact ClavionX launch day (Product Hunt only says '3mo ago')
- Whether ClavionX has a Chrome listing and how many users it has
- Whether SAMLScope exists and when it launched
- samltracer.com's pricing and status (the site returned HTTP 402)
- The AppBox claim of 27,000+ users and paying subscribers
- Current Awesome SAML Tracer user count (the Chrome listing hit a consent redirect; the lead's earlier figures were 3,000 to 4,000)
- Owner hours and automation share

## L009 Contractual land-rights submission preparation tool: kill (medium)

The legal duty is real and has fixed dates, but the government's own figure puts total ongoing business compliance cost at only about £3.7m a year, HM Land Registry (HMLR) is building the submission service and mapping tools itself, a regulated lawyer must personally submit, and there is no evidence anyone would pay. The opportunity is too small and too exposed to HMLR to meet Ricardo's success and 5 h/week limits.

**Why**

- The demand is real and recent. The Regulations were made on 8 June 2026 and come into force on 6 April 2027. Rights granted from 8 June 2026 must be reported by 6 October 2027, and later rights within 60 calendar days. https://www.gov.uk/guidance/hm-land-registry-new-reporting-rules-for-contractual-control-rights ; https://www.burges-salmon.com/articles/102n2se/contractual-control-regulations-made/
- The whole market is small. The government estimates the total business cost at about £4.2m a year, made up of £3.7m a year in ongoing compliance across all developers, land promoters and conveyancers, plus £4.5m one-off familiarisation (2019 prices). Software spend would be a fraction of that, so the realistic reachable revenue for a niche tool is low. https://www.legislation.gov.uk/ukdsi/2026/9780348280630/pdfs/ukdsiem_9780348280630_en_001.pdf (paras 9.2, 9.6)
- Nobody knows how many agreements there will be. The consultation-stage impact assessment says the government lacks 'robust estimates of the number of contractual controls', and HMLR will only learn prevalence from submission metadata after launch. https://assets.publishing.service.gov.uk/media/65b1289ff2718c000dfb1c95/Contractual_controls_consultation_stage_impact_assessment.pdf ; https://www.legislation.gov.uk/ukdsi/2026/9780348280630/pdfs/ukdsiem_9780348280630_en_001.pdf (para 10.1)
- HMLR owns the platform. It will launch its own digital service on 6 April 2027 in a 'prescribed digital format', with online mapping tools so conveyancers can identify land without uploading a spatial file. Its private beta for legal professionals starts in November 2026. That leaves only a thin pre-fill layer for a third party. https://www.gov.uk/government/publications/contractual-control-agreements/contractual-control-agreements ; https://hmlandregistry.blog.gov.uk/2026/09/17/help-shape-our-new-contractual-control-service/
- Buyers face high legal stakes. Submission must be made 'personally by an individual who is regulated', not a paralegal, and false or misleading information is a criminal offence under s.225 of the Levelling-up and Regeneration Act 2023. Commercial property firms will want security reviews, supplier vetting and human sign-off, which makes ≤5 h/week of Ricardo's time implausible. https://www.gov.uk/guidance/hm-land-registry-new-reporting-rules-for-contractual-control-rights ; https://www.legislation.gov.uk/ukdsi/2026/9780348280630/pdfs/ukdsiem_9780348280630_en_001.pdf (para 6.6)
- There is no evidence of payment. Law firms are publishing free how-to-prepare guidance, and established vendors could add a field-extraction feature cheaply. https://www.hsfkramer.com/notes/realestate/2026-posts/contractual-control-rights-how-to-prepare-for-the-new-disclosure-regime ; https://www.bevanbrittan.com/insights/articles/2026/the-contractual-control-rights-register-what-do-developers-and-landowners-need-to-know/

**Competitors checked**

| Name | Price | Launched | URL |
|---|---|---|---|
| HMLR contractual control digital service (government, the required channel) | No fee stated (unverified) | Private beta Nov 2026; launch 6 Apr 2027 | https://hmlandregistry.blog.gov.uk/2026/09/17/help-shape-our-new-contractual-control-service/ |
| RegLand (adjacent: pre-validates HMLR applications) | unverified (free pilot reported) | 26 May 2026 | https://thenegotiator.co.uk/news/products-services-news/new-legal-tech-platform-to-end-submit-and-hope-conveyancing/ |
| ClearPathOS (adjacent: AI conveyancing and contract analysis) | unverified | 24 Aug 2026 | https://propertysoup.co.uk/clearpath-ai-launches-to-target-conveyancing-overhaul/ |
| Business Gateway-integrated case management suppliers (potential fast followers) | varies, unverified | existing | https://www.gov.uk/government/publications/software-suppliers-integrated-with-business-gateway/software-suppliers-integrated-with-business-gateway |

**Demand:** Regulatory demand is live and recent: Regulations made 8 June 2026, in force 6 April 2027, transitional deadline 6 October 2027, and HMLR guidance published 29 September 2026. Its size is small and uncertain: about £3.7m a year in total ongoing compliance cost (2019 prices), and agreement volume is not estimated anywhere. No evidence of willingness to pay for a third-party tool was found. Sources: https://www.gov.uk/guidance/hm-land-registry-new-reporting-rules-for-contractual-control-rights ; https://www.legislation.gov.uk/ukdsi/2026/9780348280630/pdfs/ukdsiem_9780348280630_en_001.pdf

**Legal:** The grantee (usually a developer or land promoter) holds the duty, but submission must be made personally by an individually regulated conveyancer through HMLR's prescribed digital service. Non-compliance or false information is a criminal offence (LURA 2023 s.225), and HMLR may refuse to register linked notices or restrictions. A tool can lawfully prepare drafts for lawyer review but cannot submit. Sources: https://www.gov.uk/government/publications/contractual-control-agreements/contractual-control-agreements ; https://www.gov.uk/guidance/hm-land-registry-new-reporting-rules-for-contractual-control-rights

**Channel:** Lawful channels exist: SEO on 'contractual control register', a company-branded checklist and sample extraction, opt-in newsletters, paid ads, and possible integration once HMLR publishes technical guidance (still 'in due course'). ICO rules on sole traders and partnerships forbid cold email or DMs to those buyers. Reach is weak because the audience is a few hundred specialist commercial property and development lawyers. Sources: https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/ ; https://www.gov.uk/government/publications/contractual-control-agreements/contractual-control-agreements

**Owner hours:** Unverified. Likely above 5 h/week: law-firm security and supplier vetting, handling unusual clauses, tracking HMLR format changes before and after the April 2027 launch, and partner sales. All are hard to automate because outputs carry criminal-offence liability for the submitting lawyer. https://www.gov.uk/guidance/hm-land-registry-new-reporting-rules-for-contractual-control-rights

**Desk check run:** I ran the desk checks: (1) market size from the explanatory memorandum: £3.7m a year ongoing compliance cost across all businesses, 2019 prices; (2) agreement volume from the 2024 consultation impact assessment: none estimated; (3) whether HMLR's service and mapping tools cover the workflow: yes for submission and mapping, with no fee stated; (4) searches for any direct competitor, and for Orbital, LEAP, Landmark, Thirdfort or Search Acumen features: none found. Result: copy-speed passes (no direct launches), but market size and HMLR's ownership of the platform rule it out. The deciding unknown, whether firms would pay, cannot be tested at a desk.

**First test (if revived):** Only if re-opened after HMLR publishes its technical guidance: post a cited sample extraction page plus a paid-pilot form (£X per agreement) via opt-in conveyancing newsletters and ads, and count paid pilot commitments within 2 weeks. Pass is at least 3 paid commitments. This would take more than a day to produce a result, so it was not run in v9.

**Unverified:**
- Number of qualifying agreements per year
- Fee for the HMLR contractual control service
- Whether HMLR will offer an API or Business Gateway route for contractual control submissions
- Willingness to pay of conveyancers or developers for a preparation tool
- Prices of RegLand and ClearPathOS
- Whether any incumbent case management or legal-AI vendor plans a contractual control feature
- Owner hours and automation share

## L037 Fire-and-rehire decision record tool: kill (medium)

Few employers have this problem, the government aims to shrink it, the start date keeps moving, and free advice from Acas or advice bundled with existing HR services already covers it. I found no evidence that anyone pays for it within the last 18 months, so a SaaS product would be unlikely to reach meaningful revenue in 12 months.

**Why**

- The start date is still moving. GOV.UK (updated 22 Oct 2026) lists the fire-and-rehire protections under 'Measures that will take effect in March 2027'. Acas (updated 20 Oct 2026) still says January 2027 and will publish detailed advice in December 2026. https://www.gov.uk/government/publications/implementing-the-plan-to-make-work-pay-and-employment-rights-act/plan-to-make-work-pay-and-employment-rights-act-timeline-update ; https://www.acas.org.uk/changing-an-employment-contract/employer-responsibilities/if-employment-contract-changes-cannot-be-agreed
- The revised Code of Practice on dismissal and re-engagement was only published for consultation on 22 Oct 2026 and closes on 17 Dec 2026. The rules a workflow product would encode are therefore not final. https://www.gov.uk/government/consultations/make-work-pay-revised-code-of-practice-on-dismissal-and-re-engagement
- Very few employers do this. DBT (4 Feb 2026) estimates about 12,100 businesses a year (<1% of employers), probably an overestimate because the data covers the pandemic. ONS Wave 133 had to suppress the figure as too low. Of the employers changing terms, 63% do so by agreement and <1% use fire and rehire. The policy's stated aim is to reduce the practice further. https://assets.publishing.service.gov.uk/media/698370ef20fe1bb69ac24429/fire-and-rehire-options-assessment.pdf
- The broader market (agreed contract changes) is a routine HR process. Free Acas guidance and a free helpline cover it, and paid HR/advice services such as BrightHR are already marketing Employment Rights Act readiness to the same SMEs. https://www.acas.org.uk/changing-an-employment-contract/employer-responsibilities/if-employment-contract-changes-cannot-be-agreed ; https://brighthr.com/campaign/employment-rights-act/
- Observed prices are low or the work is done by people. Tarn.hr's AI HR guidance costs £15/month or £150/year and does not yet cover contract changes. ConsultantLM sells solicitor-led stages from £264 to £3,432. No realized revenue was found for any product in this niche. https://tarn.hr/pricing ; https://consultantlm.uk/service/fire-and-rehire-legal-advice
- Copy-speed (K2) passes on re-check: I found no dated fire-and-rehire workflow SaaS launch. That is weak comfort, because the absence of competitors fits the low demand. https://aimac-hr.co.uk/fire-and-rehire-2/ (an advisory page, not software)

**Competitors checked**

| Name | Price | Launched | URL |
|---|---|---|---|
| Acas guidance + helpline | free | established; page updated 20 Oct 2026 | https://www.acas.org.uk/changing-an-employment-contract/employer-responsibilities/if-employment-contract-changes-cannot-be-agreed |
| Tarn.hr (adjacent AI HR guidance; no contract-change scenario yet) | £0 for one scenario; £15/month; £150/year | unverified (sources checked 10 Oct 2026) | https://tarn.hr/pricing |
| BrightHR Employment Rights Act readiness (advice + templates) | unverified | campaign page live, date unverified | https://brighthr.com/campaign/employment-rights-act/ |
| ConsultantLM fire-and-rehire legal service | £264–£3,432 by stage | page dated 25 Aug 2026 | https://consultantlm.uk/service/fire-and-rehire-legal-advice |
| HRVANTA Etsy fire-and-rehire PDF toolkit | $20.98 (unverified; Etsy returned 403) | 8 Sep 2026 per cheaper pass (unverified) | https://www.etsy.com/listing/4571155465/uk-changing-employment-terms-and-fire |
| HRDocBox dismissals toolkit | £24.99 (unverified; page timed out) | unverified | https://hrdocbox.co.uk/category.cfm/subcategory/04.09/dismissals-templates-toolkit |

**Demand:** Within the last 18 months there is plenty of regulatory and legal-commentary activity: the DBT consultation and options assessment (Feb 2026), the GOV.UK timeline (22 Oct 2026), the Code consultation (22 Oct 2026), and law-firm and HR-press coverage such as https://hrreview.co.uk/hr-news/employment-law/fire-and-rehire-ban-delayed-to-2027/386064. None of this shows anyone paying. The affected pool is about 12,100 employers a year at most, and DBT expects it to fall (https://assets.publishing.service.gov.uk/media/698370ef20fe1bb69ac24429/fire-and-rehire-options-assessment.pdf). The wider pool of employers changing contract terms is 3.4% of businesses a year (same source), and that is a commodity HR task.

**Legal:** ERA 2025 s.28 makes dismissal for refusing a 'restricted variation' automatically unfair unless the employer is in severe financial difficulty with no reasonable alternative. The start date is March 2027 per GOV.UK and January 2027 per Acas. The revised Code is under consultation until 17 Dec 2026, and secondary rules on shift patterns and expenses are still pending. A product could not guarantee a lawful dismissal, so legal content would need human review. Employee records may include special-category data (ICO lawful-basis rules). https://www.legislation.gov.uk/ukpga/2025/36/section/28 ; https://www.gov.uk/government/consultations/make-work-pay-revised-code-of-practice-on-dismissal-and-re-engagement ; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/employment-practices-and-data-protection-keeping-employment-records/collecting-and-keeping-employment-records/

**Channel:** Lawful channels exist: SEO under a product brand, opt-in updates and referrals from HR or payroll advisers. Corporate B2B email is permitted, but sole traders count as individuals under PECR (https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/). The SEO terms are already crowded with law firms and HR vendors (see the search results above), so organic reach is unverified and likely hard.

**Owner hours:** Unverified. Monitoring legal changes and ensuring legal review while the rules are still moving (Code, regulations, start date) would likely push owner time above 5 h/week through 2027.

**Desk check run:** I re-verified the deciding facts live. (1) GOV.UK says March 2027 while Acas says January 2027, so the conflict is confirmed. (2) The revised Code consultation is open until 17 Dec 2026. (3) The DBT options assessment confirms about 12,100 employers a year (<1%), likely overstated, with ONS suppressing the figure as too rare. (4) Two searches (one standard, one extended) for any fire-and-rehire or contract-variation software launched in 2026 found none. (5) Tarn.hr does not cover contract changes. Result: no demand signal tied to payment, and the need is policy-shrinking. The only remaining test (a paid reservation) is not desk-only, and these facts make it unlikely to pass.

**First test (if revived):** Not recommended. If revisited after the Code is finalised (2027), run a one-day landing page offering a contract-change consultation record at £15/month with a refundable reservation, shared only through opt-in HR-adviser channels. Stop if there are zero reservations from employing companies.

**Unverified:**
- Etsy HRVANTA listing price, date and sales (403 on fetch)
- HRDocBox toolkit price (timeout)
- BrightHR pricing and whether its product includes a contract-change workflow
- Tarn.hr launch date
- UK search volume for fire-and-rehire or contract-change terms
- Owner hours and the 55% automation share
- Absence of any dated competing SaaS launch (a negative search result)

## L014 Hey Product Page Banner support-rescue alternative: kill (high)

Re-checking the launches kills this lead on K2 copy-speed: at least 2 product-page banner apps have launched since 23 Apr 2026, plus a near-identical one on 1 Apr 2026. The rescue/monitoring angle rests on 2 support complaints, and the core widget is already free or $4.99/month from 6+ apps.

**Why**

- K2 fail: Lantera's 'Product Page Banners' launched 11 May 2026. It does product-page banners through theme blocks, with scheduling, at $9.99/month: https://apps.shopify.com/product-page-banners
- K2 fail: 'Carti Badge' launched 26 Jun 2026. It is a free app for banners on selected product pages: https://apps.shopify.com/carti-badge
- Close miss on the window: 'Dynamic Product Banners' launched 1 Apr 2026. It is the same as Hey (free up to 3 blocks, then $4.99/month or $49.99/year). Banners All Over (3 Mar 2026, free or $4.99/month) also has a product-page banner type: https://apps.shopify.com/dynamic-product-banners https://apps.shopify.com/banners-all-over
- K4 pressure: at least 6 apps sell the widget at or below $4.99/month or free, including DECO (5.0 stars, 1,735 reviews, free tier). That leaves no price wedge. Nothing UK-specific turned up: https://apps.shopify.com/product-labels https://apps.shopify.com/xblocks https://apps.shopify.com/product-page-badges
- Thin rescue demand: Hey has 32 reviews (3.6 stars) and an estimated 125 stores, down 34% year on year. One review edited 7 Oct 2026 says 'stops working every few months… no response'. A 12 Jun 2025 outage review was edited to say it was fixed: https://apps.shopify.com/product-page-descriptions-hey https://storeleads.app/reports/shopify/app/product-page-descriptions-hey
- On Shopify's side, app blocks only work in compatible sections, activation data covers the published theme only, and Canvas/Sidekick adds pressure on simple widgets. That limits automatic 'repair' to guiding the merchant: https://help.shopify.com/en/manual/online-store/themes/customizing-themes/apps https://shopify.dev/docs/api/app-home/latest/apis/authentication-and-data/app-api https://changelog.shopify.com/posts/design-a-fully-bespoke-store-with-canvas

**Competitors checked**

| Name | Price | Launched | URL |
|---|---|---|---|
| Hey! Product Page Banner& Text (HeyMerch) | Free ≤3 products; $4.99/mo or $49.99/yr | 2022-10-28 | https://apps.shopify.com/product-page-descriptions-hey |
| Product Page Banners (Lantera) | $9.99/mo or $99.99/yr | 2026-05-11 | https://apps.shopify.com/product-page-banners |
| Carti Badge (Carti Apps) | Free | 2026-06-26 | https://apps.shopify.com/carti-badge |
| Dynamic Product Banners (Plug Digital) | Free; $4.99/mo or $49.99/yr | 2026-04-01 | https://apps.shopify.com/dynamic-product-banners |
| Banners All Over (White Pixel Solutions) | Free; Pro $4.99/mo or $49/yr | 2026-03-03 | https://apps.shopify.com/banners-all-over |
| Store-Tip Emergency Banner | $4.99/mo | 2026-08-14 (general announcement banner, not product-page specific) | https://apps.shopify.com/emergency-banner |
| XBlocks: Product Page Blocks (Sotadev) | Free banner block; paid Pro (price unverified) | 2025-09-19 | https://apps.shopify.com/xblocks |
| Product Page Banners & Text | $4.95/mo; $19.95/mo for Plus | 2021-09-03 | https://apps.shopify.com/product-page-badges |
| DECO Product Labels & Badges (PieLab) | Free; $9/$19/$39 per month | 2016-05-13 | https://apps.shopify.com/product-labels |

**Demand:** Weak. Two support-failure signals fall within 18 months. First, a Hey review edited 7 Oct 2026 says the app 'stops working every few months' and support doesn't reply. Second, a 8 Dec 2025 review of Product Page Banners & Text says the developer can't be reached and the app 'seems abandoned' (https://apps.shopify.com/product-page-descriptions-hey https://apps.shopify.com/product-page-badges). DECO's 2026 display problems were all fixed quickly by support (https://apps.shopify.com/product-labels). Hey's install base is small and shrinking: an estimated 125 stores, down 34.2% year on year (https://storeleads.app/reports/shopify/app/product-page-descriptions-hey). There is general developer pain around app blocks not rendering (https://community.shopify.dev/t/app-block-showing-in-customize-but-not-showing-in-preview/24164), but I found no evidence merchants would pay for monitoring.

**Legal:** No specific UK regulatory barrier found for a Shopify theme app extension. Shopify App Store requirements apply, and theme changes must go through theme app extensions (https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements). Under PECR, cold email or DMs to sole-trader merchants need consent or the soft opt-in (https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/).

**Channel:** Lawful and reachable: Shopify App Store search/listing, SEO troubleshooting content, and Shopify ads. With 5+ near-identical free or $4.99 listings, getting ranked is the binding problem (https://apps.shopify.com/dynamic-product-banners).

**Owner hours:** Unverified. Theme-specific breakage support is exactly the failure mode this lead targets, so support load could exceed 5 h/week. No operating data exists.

**Desk check run:** Not needed for a maybe. I re-ran the copy-speed check live by fetching the App Store listings for launch dates (https://apps.shopify.com/product-page-banners https://apps.shopify.com/carti-badge). Two qualifying launches are after 23 Apr 2026, which triggers K2. I also read the Hey, Product Page Banners & Text and DECO reviews: there are 2 unresolved support complaints from 2025–26, and DECO's 2026 issues were resolved.

**First test (if revived):** n/a (killed). If it were ever revisited: a one-day check on whether any banner or badge app markets 'auto-detect when the block disappears' and whether reviews ask for it.

**Unverified:**
- Hey's real install count (only a third-party estimate)
- Original posting date of the Homio Decor review (only its 7 Oct 2026 edit date is shown)
- Date of the Bop Canvases 'stopped working' review
- Paid user counts or revenue for any competitor
- XBlocks Pro price
- Whether any app already offers storefront health monitoring for app blocks (none found; the search wasn't exhaustive)
- Owner hours and automation share

## L070 Spreadsheet-to-MTD transaction importer: kill (high)

Killed on K2 and K4. Two competing products went live after 23 Apr 2026: NJT Tax Return Manager, which is built in Access (20 Jun 2026), and suiteSheets (submissions live by 9 Jul 2026). At least 7 incumbents cost £30/yr or less, including a free one that imports CSV with column mapping. The only demand evidence is one Reddit anecdote with no purchase.

**Why**

- K2 copy-speed fails. NJT says its Access-built Tax Return Manager released 'Quarterly Update' functionality on 20 June 2026 and imports Excel, CSV, Sage and VT files: https://www.neilsonjamestech.co.uk/index.php
- K2, second launch. suiteSheets replied on Trustpilot on 9 Jul 2026 that it was still finishing HMRC recognition at 17 June 2026 and that 'suiteSheets is now HMRC-recognised software and quarterly submissions are available'. It charges £20 for four quarterly updates: https://uk.trustpilot.com/review/suitesheets.co.uk and https://suitesheets.co.uk/
- K4 incumbents fail. At least 7 established tools cost no more than the £30–40/yr price floor: My Tax Digital is free, TaxHeaven has a free plan, 123 e-Filing is £18, 123 Sheets is £19.75 in year one, Abridge is £29, VitalTax is £30+VAT and Andica is £30. They also include GoFile, TaxNav, Forbes MTD and AbraTax: https://www.abratax.co.uk/blog/best-mtd-bridging-software-income-tax/ and https://mtd.digital/mtd-income-tax/mtd-bridging-software/
- No wedge. My Tax Digital is free for Income Tax, imports .xlsx/.xls/.ods/.csv, and maps columns automatically or by dropdown. An Access user who can already export to Excel, as the Reddit poster can, is served for free: https://mytaxdigital.co.uk/docs/faqs and https://mytaxdigital.co.uk/docs/transactions
- The platform rules make a plain CSV export enough. HMRC (page updated 16 Oct 2026) lists 'CSV importing and exporting' as a valid digital link, so a dedicated Access converter adds little: https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/create-digital-records
- Demand is real for MTD overall but not for this niche. More than 570k people had signed up by 12 Aug 2026. The only Access-specific evidence is one Reddit post from Jan 2026 with no purchase, and no search turned up any other Access-plus-MTD demand: https://www.gov.uk/government/news/436000-sole-traders-and-landlords-make-their-tax-digital

**Competitors checked**

| Name | Price | Launched | URL |
|---|---|---|---|
| My Tax Digital (Open Answers) | Free (Income Tax and VAT) | 2019 | https://mytaxdigital.co.uk/docs/faqs |
| NJT Tax Return Manager (built in MS Access) | £40/yr for quarterly updates (ITQU); £49 with year-end from Jan 2027; free evaluation | 20 Jun 2026 (quarterly updates) | https://www.neilsonjamestech.co.uk/tax-prices.php |
| suiteSheets | £20 for quarterly updates per income source; £15 year-end (coming soon) | Submissions live between 17 Jun and 9 Jul 2026 | https://suitesheets.co.uk/ |
| Easy MTD (Fly Software) | Tokens from £2+VAT per submission | 13 Apr 2026 (Income Tax 'rolling out soon') | https://easymtd.com/news/easy-mtd-launched |
| VitalTax | £30+VAT/yr | unverified (established) | https://mtd.digital/mtd-income-tax/mtd-bridging-software/ |
| 123 Sheets | £19.75 in year one, about £39.50 on renewal | unverified (established) | https://www.abratax.co.uk/blog/best-mtd-bridging-software-income-tax/ |
| Abridge | £29/yr incl. VAT | unverified | https://www.abratax.co.uk/blog/best-mtd-bridging-software-income-tax/ |
| Andica | From £30/yr ex VAT | unverified (established) | https://www.abratax.co.uk/blog/best-mtd-bridging-software-income-tax/ |
| TaxHeaven | Free plan; Pro £49/yr | unverified | https://www.abratax.co.uk/blog/best-mtd-bridging-software-income-tax/ |
| 123 e-Filing | £18 incl. VAT for up to 5 returns | unverified | https://www.abratax.co.uk/blog/best-mtd-bridging-software-income-tax/ |
| GoFile | £39.99 in year one, then £49.99+VAT | unverified | https://www.abratax.co.uk/blog/best-mtd-bridging-software-income-tax/ |

**Demand:** There is broad MTD demand: HMRC reported more than 570,000 sign-ups and 436,000 first quarterly updates by 12 Aug 2026, and the threshold drops to £30k in April 2027 (https://www.gov.uk/government/news/436000-sole-traders-and-landlords-make-their-tax-digital). Access-specific demand is limited to one Reddit post from Jan 2026, with no purchase stated. I could not re-fetch it because Reddit blocks the fetcher. An extended search for 'Access database' plus 'Making Tax Digital' found no further demand signals.

**Legal:** Legal and low-risk. HMRC accepts CSV import and export as a digital link, but forbids copy-paste between products (https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/create-digital-records). A local converter feeding recognised software needs no HMRC recognition of its own. Filing directly would need recognition, which competitors took months to get (https://uk.trustpilot.com/review/suitesheets.co.uk).

**Channel:** Lawful routes are SEO, guides, paid search and accountant referrals. Cold DMs, email or SMS to sole traders are not lawful without consent under PECR (https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/). SEO competition is heavy: at least 10 vendors publish comparison and guide content (https://www.abratax.co.uk/blog/best-mtd-bridging-software-income-tax/).

**Owner hours:** Unverified. Bespoke Access schemas imply mapping support for each customer, which could push past 5 h/week. Nothing has been measured.

**Desk check run:** I re-checked competitors and copy-speed on the live web. Two competing launches fall after the 23 Apr 2026 cutoff: NJT on 20 Jun 2026, which is built in Access, and suiteSheets, live by 9 Jul 2026. At least 7 incumbents cost £30/yr or less, including a free one with CSV mapping. Result: K2 and K4 kills confirmed, so no further test is needed.

**First test (if revived):** n/a (killed). If it is ever revisited, the 1-day test would be a landing page for an 'Access to MTD CSV export' guide with a paid-pilot button, run on paid search for 'access database making tax digital'. It should count paid commitments only.

**Unverified:**
- How many MTD-mandated sole traders keep their records in MS Access
- Search volume for Access-plus-MTD queries
- Launch dates for VitalTax, 123 Sheets, Abridge, Andica, TaxHeaven and 123 e-Filing (assumed established before Apr 2026)
- Whether NJT has finished HMRC recognition (its own page says queries are still open)
- The text of the Reddit thread (fetch blocked; I relied on the earlier pass)
- Owner hours and automation share for a built product

## L031 Landlord ombudsman complaint workflow: kill (medium)

Mandatory ombudsman membership is not expected until 2028. The government has already said the Ombudsman will give landlords complaint-handling tools. Bundled incumbents and a pre-launch £6.99/month rival already cover the record-keeping. No one was found paying for a complaint workflow inside the 12-month window.

**Why**

- The trigger falls outside the 12-month window. The government roadmap says 'Stage 2 will require landlords to be members of the new service – we expect this to be in 2028'. Its PRS Database rolls out only 'from late 2026'. https://www.gov.uk/government/publications/renters-rights-act-2025-implementation-roadmap/implementing-the-renters-rights-act-2025-our-roadmap-for-reforming-the-private-rented-sector
- The platform owner plans to cover this (K3 risk, though not yet live). The roadmap says the Ombudsman 'will also support landlords with tools, guidance and training on handling complaints from tenants early'. The 2026 regulations only set up a framework: they do not approve or designate a scheme, and the start date is still to come. https://www.gov.uk/government/publications/renters-rights-act-2025-implementation-roadmap/implementing-the-renters-rights-act-2025-our-roadmap-for-reforming-the-private-rented-sector , https://www.bevanbrittan.com/insights/articles/2026/private-landlord-redress-the-framework-takes-shape/ , https://westminsterbrief.co.uk/archive/debate/30-june-2026/private-landlord-redress-schemes-approval-designation-64ec
- A near-identical rival already exists. Dealtwith markets 'PRS Landlord Ombudsman. Keep complaints, decisions and responses together now, ready for the future redress scheme' at £6.99/month, though its apps are still 'coming soon'. https://dealtwith.co.uk/ , https://dealtwith.co.uk/pricing
- Incumbents bundle the core workflow at or below the likely price floor. Landlord Vision Standard includes a 'Tenant portal and service desk' and Premium adds a 'Correspondence tracking diary'. August is free for up to 2 tenancies and promotes its audit-trail document storage for ombudsman readiness. Landlord Studio has a free plan for up to 3 units. https://www.landlordvision.co.uk/landlord-software-pricing.html , https://www.augustapp.com/blog/prs-landlord-ombudsman , https://www.landlordstudio.com/uk/pricing
- Demand is about awareness, not payment. Recent articles from Aug–Oct 2026 tell landlords to keep a DIY complaint log in a spreadsheet. The only priced complaint item found is a £19 template, with no sales evidence. https://www.netrent.co.uk/2026/10/09/the-landlord-ombudsman-is-coming-why-complaints-records-need-to-improve-now/ , https://landlordsportal.co.uk/landlord-ombudsman-how-it-works/ , https://letsafeuk.co.uk/guides/prs-ombudsman-landlord-registration-guide-2026

**Competitors checked**

| Name | Price | Launched | URL |
|---|---|---|---|
| Dealtwith | Free tier; £6.99/month for up to 2 tenancies, +£2.99/month per extra tenancy | Pre-launch (apps 'coming soon'); launch date unverified | https://dealtwith.co.uk/pricing |
| Landlord Vision | Starter £7.99/month ex VAT; Standard (includes service desk) £23.98/month promotional, list £34.97; Premium (adds correspondence diary) £31.98/month, list £44.97 | Established; mobile app reportedly launched in 2026 (per lead evidence, not re-verified) | https://www.landlordvision.co.uk/landlord-software-pricing.html |
| Landlord Studio | Free up to 3 units; Pro £12/month + VAT | Established (50K+ Play downloads) | https://www.landlordstudio.com/uk/pricing |
| August | Free for up to 2 tenancies; paid price not fetched | Established; claims 3,000+ UK landlords and tenants | https://www.augustapp.com/blog/prs-landlord-ombudsman |
| LetSafe UK (template) | £19 'PRS Ombudsman Complaint Response' template | Page updated 10 Sep 2026; product launch date unverified | https://letsafeuk.co.uk/guides/prs-ombudsman-landlord-registration-guide-2026 |
| Stead | unverified | Closed beta May 2026 (per lead evidence, not re-verified) | https://stead.space/press |

**Demand:** There is no live demand evidence for a paid complaint workflow. The adjacent signals are dated within 18 months but none shows payment. The Property Ombudsman reported a 58% rise in tenant complaints (Nov 2025–Feb 2026 vs the prior year), but that covers agents, not this scheme (https://landlordassociation.org.uk/renters-rights-act-is-already-driving-a-surge-in-tenant-complaints/, dated 12 Mar 2026). There is also a steady flow of preparation articles from Aug–Oct 2026 (https://www.netrent.co.uk/2026/10/09/the-landlord-ombudsman-is-coming-why-complaints-records-need-to-improve-now/). LetSafe UK says there is currently 'no live scheme... no complaints jurisdiction' (https://letsafeuk.co.uk/guides/prs-ombudsman-landlord-registration-guide-2026).

**Legal:** The Renters' Rights Act 2025 provides for a mandatory PRS Landlord Ombudsman. The Private Landlord Redress Schemes (Approval and Designation) Regulations 2026 set the framework (in force 17 Sep 2026 per Bevan Brittan), but no scheme has been approved or designated yet. Mandatory membership is expected in 2028 (https://www.legislation.gov.uk/uksi/2026/1033/made, https://www.bevanbrittan.com/insights/articles/2026/private-landlord-redress-the-framework-takes-shape/, gov.uk roadmap). The Housing Ombudsman homepage has no news of being designated for the PRS (https://www.housing-ombudsman.org.uk/). K6 is not formally triggered because 2028 is not 'beyond 2028', but the need sits outside the 12-month window.

**Channel:** Inbound SEO, paid search and free templates are lawful and need no founder face. Cold email, SMS or DMs to individual or sole-trader landlords are not allowed (https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/). The ombudsman SERP is already crowded with free guides from agents, insurers and app vendors (search results above), so organic reach is unverified and likely to be expensive.

**Owner hours:** unverified. ≤5 h/week looks plausible for a self-serve log/export tool. However, the product holds tenant personal data, so GDPR and security duties apply, and rules need to be kept current as the scheme is defined. Those duties are not measured.

**Desk check run:** Searched live for (a) any paid, launched product dedicated to landlord-side PRS ombudsman complaints, (b) dated demand or payment signals, and (c) the status of official or platform tooling. Result: the only offerings found are Dealtwith (pre-launch, £6.99/month), LetSafe (£19 template, no sales evidence) and bundled features in Landlord Vision and August. The government has said the Ombudsman will supply landlord complaint tools. No scheme is designated yet and membership is expected in 2028. No payment evidence for this workflow was found, so the test came out negative.

**First test (if revived):** Not recommended now. Set a recheck for when a scheme administrator is designated or a membership start date is published. At that point, run a 1-day concept page with an SEO/ads smoke test against the £6.99/month anchor.

**Unverified:**
- Dealtwith launch date and user count
- Stead product scope and launch date
- Search volume for landlord complaint-log terms
- Whether the Housing Ombudsman will be the PRS administrator and what its free landlord tools will include
- Awaab's Law extension to the PRS (a consultation reportedly opened 9 Oct 2026; seen only in third-party search summaries)
- Owner hours and automation share
- 15 Dec 2026 PRS Database date (cited by third parties, not in the gov.uk roadmap)
