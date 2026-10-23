# Pain points people want automated (forum and social sweep, Oct 2026)

**Scope:** Reddit, Hacker News and X (public search), plus vendor and blog pages where they explain how a workflow is done today. LinkedIn and Facebook groups are behind logins and gave no usable verbatim posts, so they're not cited. The search was weighted toward high-volume industries: e-commerce, real estate, insurance, legal, healthcare admin, finance, recruiting, customer support and logistics.

**Method:** This was one lean pass with no long verification loops.
- Every quote below is verbatim text from the linked page.
- Where Reddit blocked a full-page fetch, the quote is the thread **title**, marked *(title)*.
- **Frequency** is the number of independent posts or threads found in this pass. It's a relative signal, not a market size.
- On X, most hits for these phrases were **vendors and agencies pitching** ("I automate X for you"), not end users. That fits the earlier v7 finding that these spaces are crowded with sellers.

**Scoring:** Frequency (1–5) × Ease of AI automation (3 = easy, 2 = medium, 1 = hard) × Fit with Ricardo's constraints (3 = online, self-serve, no face, not a local business; 2 = online B2B niche that may need some sales; 1 = regulated, US-only or relationship-heavy). Maximum score is 45.

## Ranked themes

| Rank (section) | Theme | Industry | Freq | Ease | Fit | Score | Already solved by |
|---|---|---|---|---|---|---|---|
| 1 (§1) | Repetitive customer emails / "where is my order" | E-commerce, customer support | 5 | 3 | 3 | **45** | Gorgias, Shopify Inbox, Tidio, Rep AI, AfterShip (crowded) |
| 2 (§2) | PDF invoices, bank statements and vendor files typed into spreadsheets | Finance, logistics, e-commerce | 5 | 3 | 3 | **45** | Dext, Hubdoc, Docparser, Rossum, Veryfi, Power Query (crowded, but SMBs call them pricey or complex) |
| 3 (§4) | Product listing creation and variants (Etsy, print-on-demand, Shopify) | E-commerce | 4 | 3 | 3 | **36** | Vela, Printify/Printful APIs, Etsy copy listing, Shopify import apps |
| 4 (§3) | Collecting receipts and invoices for the accountant every month | Finance, solo founders, SaaS | 4 | 2 | 3 | **24** | Ramp, Dext, Hubdoc, GetMyInvoices (portals behind 2FA aren't solved) |
| 5 (§7) | Freight rate confirmations and load emails re-typed into the TMS | Logistics | 4 | 3 | 2 | **24** | X-TMS TED, Tai TMS, DAT Broker TMS, EDI (mostly US; small shops still brute-force it) |
| 6 (§9) | Freelancers chasing late invoices and client status updates | Finance, freelancers | 4 | 3 | 2 | **24** | FreshBooks, Wave, Stripe invoicing, Chaser (UK), Zoho (users push back on automated chasing) |
| 7 (§6) | Amazon FBA reimbursement and claims tracking | E-commerce | 3 | 2 | 3 | **18** | Getida, Seller Investigators, Carbon6 / refund services, Lumian (buyer-fraud SAFE-T claims still manual) |
| 8 (§8) | Insurance: one client's data re-entered on 10–30 carrier portals, and commission statement reconciliation | Insurance | 4 | 2 | 2 | **16** | EZLynx, PL Rater, SinglePoint, Gaya, Carpe AI, PolicyNest, AMS modules (raters "never work quite right") |
| 9 (§5) | Accountants chasing clients for documents, plus UK MTD ITSA quarterly updates | Finance (UK practices) | 3 | 2 | 2 | **12** | Karbon, Portali, Keeper, PracticeNudge, aligned.tax, MTD Assist |
| 10 (§10) | Recruiting: screening 500+ AI-written CVs and interview scheduling | Recruiting | 4 | 2 | 1 | **8** | Metaview, Calendly, HackerEarth, Workable, Ashby (crowded; UK agency rules) |
| 11 (§11) | Real estate: MLS/CRM/portal re-entry, listing copy, transaction-coordinator deadlines | Real estate | 4 | 2 | 1 | **8** | ListedKit, Jointly, ReBillion, Leni, ListHub (US MLS-centric) |
| 12 (§12) | Legal and healthcare: medical chronologies, prior authorisation, insurance verification | Legal, healthcare admin | 5 | 1 | 1 | **5** | InPractice, ProPlaintiff, Filevine MedChron, Medrecords AI, R1/Humata (regulated, US, liability) |


**Easiest to automate in high-volume industries:**
- **E-commerce:** themes 1, 2 and 4 are easy and sit in the biggest-volume industry that fits Ricardo. He can sell there self-serve through the Shopify App Store, Etsy tools or a web tool, with no face and no local-business sales.
- **Logistics:** theme 7 is easy (email or PDF to structured data), but buyers are mostly US small brokerages reached by sales.
- **Finance:** themes 2, 3 and 9 are easy to medium. The open gap is the part existing tools skip: what's missing, receipts behind portals, and exception lists.
- **Insurance, real estate, recruiting, legal and healthcare:** high volume, but medium to hard because of portals, regulation and trust. They also mostly fail Ricardo's fit filter.

**Key takeaway:** the best-fit pains (1, 2, 4) are real and frequent, but each already has funded incumbents. The angle that survives is a narrow, cheap, UK-flavoured or channel-specific wedge (for example a Shopify app for one sub-task, or "upload messy file, get a clean one" for one document type). A general "AI does your admin" product won't survive. This matches the Shopify add-on idea already at #1 in IDEAS_WORTH_PURSUING.md.

---

## 1. Repetitive customer emails / "where is my order" (WISMO)
- **Industry:** E-commerce, customer support. **Who has it:** Shopify and DTC store owners and small support teams.
- **Frequency:** 5+ independent threads and posts, plus many vendor posts on X.
- **Example quotes:**
  - *(title)* "Spending 3 hours daily just answering where is my order, anyone else drowning in the same repetitive questions?" ([r/shopifyQuestions](https://www.reddit.com/r/shopifyQuestions/comments/1pvxad5/spending_3_hours_daily_just_answering_where_is_my/))
  - *(title)* "How do you handle repetitive customer emails without losing your mind?" ([r/ShopifyeCommerce](https://www.reddit.com/r/ShopifyeCommerce/comments/1spau3l/how_do_you_handle_repetitive_customer_emails/))
  - *(title)* "Managing a Shopify store manually is getting hard, any advice?" ([r/ShopifyeCommerce](https://www.reddit.com/r/ShopifyeCommerce/comments/1smfdvs/managing_a_shopify_store_manually_is_getting_hard/))
  - "Growing a D2C brand shouldn't mean ... replying to every WISMO (Where is my Order) message yourself." ([X, Shiprocket](https://x.com/ShiprocketIndia/status/2031273526469210444)). This is vendor framing, but it shows the pain is mainstream.
- **Existing tools:** Shopify Inbox order lookup, Gorgias, Tidio, Rep AI, AfterShip, intoCHAT. Heavily served.
- **Ease:** **Easy.** Order status comes from an API, and answers come from templates plus a language model. The hard part is distribution against incumbents, not the technology.

## 2. PDF invoices, bank statements and vendor files typed into spreadsheets
- **Industry:** Finance, logistics, e-commerce. **Who has it:** SMB admins, bookkeepers, ops staff.
- **Frequency:** 5+ (r/smallbusiness ×3, r/excel ×2, plus an X bot that found "PDF invoice → structured data" as the #1 pain across 34 posts in one week).
- **Example quotes:**
  - "the admin literally types the line items (price, quantity, SKU) into a giant Excel sheet manually. It takes her like 4 hours every Friday... existing tools are either too expensive (Enterprise level) or too complex to set up." ([r/smallbusiness](https://www.reddit.com/r/smallbusiness/comments/1p2of5v/how_do_you_guys_handle_data_entry_from/), Nov 2025)
  - "Vendor names come through as "AMZ\*234KL PRIME" instead of "Amazon Prime"... I usually spend 2-3 hours a month just on this." ([r/smallbusiness](https://www.reddit.com/r/smallbusiness/comments/1swxpjc/i_spend_hours_every_month_cleaning_bank/), Apr 2026)
  - "every vendor sheet has different naming, column order, and formats — so my PQ steps break every time." ([r/excel](https://www.reddit.com/r/excel/comments/1ow0u5r/how_do_you_clean_vendor_excel_files_that_all_have/), Nov 2025)
  - "Found 34 this week. Top 3 pains: → PDF invoice → structured data → Spreadsheet report aggregation → Lead qualification scoring" ([X, @TheCalKnox](https://x.com/TheCalKnox/status/2055273256832115156), May 2026)
- **Existing tools:** Dext, Hubdoc, Docparser, Rossum, Veryfi, receiptconverter.com, Power Query, n8n flows.
- **Ease:** **Easy.** Vision models plus a schema handle it, with a review queue for low-confidence fields. The gap people describe is price and setup: "upload messy, download clean".

## 3. Collecting receipts and invoices for the accountant every month
- **Industry:** Finance. **Who has it:** founders, solo operators, SaaS-heavy small companies.
- **Frequency:** 4 (levelsio and a near-copy post on X, plus the same r/startups and r/smallbusiness post, plus an X demo of an agent doing it).
- **Example quotes:**
  - "By far THE most annoying part of running a business for me is collecting receipts for my accountant. Every month my accountants hounds me for invoices and receipts of every single expense" ([X, @levelsio](https://x.com/levelsio/status/2054158385742823894), May 2026)
  - "I spend about an hour every month logging into all our vendor accounts to grab receipts for the accountant. Two factor auth, SMS codes, all that... Is there a tool that just pulls them automatically" ([r/startups](https://www.reddit.com/r/startups/comments/1sz5jvo/monthly_receipts_i_will_not_promote/), Apr 2026)
  - "Told it to log into my online banking, search every transaction from the last month which has no invoice attatched, find the invoice (in mail or download from p..." ([X, @AleksDoesCode](https://x.com/AleksDoesCode/status/2096295694298481047), Sep 2026)
- **Existing tools:** Ramp receipt automation, Dext, Hubdoc, GetMyInvoices. They handle email receipts well and portal-only receipts poorly.
- **Ease:** **Medium.** Email matching is easy. Portals behind 2FA run into security and terms-of-service issues, which is exactly what users object to.

## 4. Product listing creation and variants (Etsy, print-on-demand, Shopify)
- **Industry:** E-commerce. **Who has it:** Etsy and print-on-demand sellers, multi-channel shops.
- **Frequency:** 4 threads (most are older, 2020–2025, but the pain keeps recurring).
- **Example quotes:**
  - "I find the workflow of creating a design on Canva, then uploading to printful/printify/whatever, then importing it to Etsy and making all the variations etc. to be so tedious." ([r/printondemand](https://www.reddit.com/r/printondemand/comments/1hsxh1l/advice_needed_sales_stagnated_on_etsy_and_i_want/), Jan 2025)
  - "I wish there was a better way. I have searched up and down and I haven't come up with one. Variations in general is kind of a nightmare." ([r/EtsySellers](https://www.reddit.com/r/EtsySellers/comments/15rwcxk/listing_items_is_a_pain_in_the_ass_with_clothing/))
  - "a single listing on Etsy can take more than an hour." *(title)* ([r/EtsySellers](https://www.reddit.com/r/EtsySellers/comments/ist98f/why_is_it_so_tedious_and_difficult_to_list_items/))
  - "What do you guys use to sync inventory between the two places? Manually doing it is so tedious" ([r/shopify](https://www.reddit.com/r/shopify/comments/fhh26c/etsy_seller_starting_shopify/))
- **Existing tools:** Vela, Printify and Printful APIs, Shuttle, Etsy's copy-listing feature, AI listing generators.
- **Ease:** **Easy.** Image to title, tags and variants via an API or CSV. A seller with technical skills already scripts it with ChatGPT and the Printify API.

## 5. Accountants chasing clients for documents, plus UK MTD ITSA
- **Industry:** Finance (accounting practices; UK MTD for Income Tax from Apr 2026).
- **Frequency:** 3 (r/Accounting ×2, r/ukaccounting), plus a cluster of new UK MTD vendors.
- **Example quotes:**
  - "Chasing clients for documents – bank statements, invoices, receipts, payroll information, etc. I feel like I'm constantly sending reminder emails" ([r/Accounting](https://www.reddit.com/r/Accounting/comments/1v578ch/what_tools_do_you_use_to_cut_down_on_admin_work/), Jul 2026)
  - "Dext and Hubdoc are capture and extraction... Neither of them knows what your client hasn't sent yet, which is the half eating your week." (same thread, reply)
  - *(title)* "What tools to use for MTD ITSA? (for small practices)" ([r/ukaccounting](https://www.reddit.com/r/ukaccounting/comments/1t836ep/what_tools_to_use_for_mtd_itsa_for_small_practices/))
- **Existing tools:** Portali, Keeper, Karbon, PracticeNudge (free MTD tracker plus paid reminders), aligned.tax, MTD Assist (£36 + VAT a year).
- **Ease:** **Medium.** A "missing documents list" built from the bank feed versus uploads is automatable. HMRC filing adds compliance work. The buyers are accounting practices, which is B2B but sold online. Note that the UK MTD space is filling up fast.

## 6. Amazon FBA reimbursement and claims tracking
- **Industry:** E-commerce. **Who has it:** Amazon FBA sellers.
- **Frequency:** 3 threads (r/AmazonFBA, r/FulfillmentByAmazon ×2).
- **Example quotes:**
  - *(title)* "What tools are you using for FBA reimbursements? Anything that handles return fraud specifically?" ([r/AmazonFBA](https://www.reddit.com/r/AmazonFBA/comments/1syxoat/what_tools_are_you_using_for_fba_reimbursements/))
  - *(title)* "How do FBA sellers actually handle reimbursement/recovery tracking?" ([r/FulfillmentByAmazon](https://www.reddit.com/r/FulfillmentByAmazon/comments/1tacnvd/how_do_fba_sellers_actually_handle/))
  - *(title)* "How do I know when to request an FBA reimbursement versus when to keep investigating?" ([r/FulfillmentByAmazon](https://www.reddit.com/r/FulfillmentByAmazon/comments/1vl64i8/how_do_i_know_when_to_request_an_fba/))
- **Existing tools:** Getida, Seller Investigators, Carbon6, Lumian, ReturnPort. Warehouse-loss recovery is crowded. SAFE-T claims for buyer and return fraud are still filed by hand.
- **Ease:** **Medium.** Report reconciliation and evidence packets can be automated. Submission is manual in Seller Central.

## 7. Freight rate confirmations and load emails into the TMS
- **Industry:** Logistics. **Who has it:** freight brokers and dispatchers (mostly US).
- **Frequency:** 4 (r/FreightBrokers, r/Truckers, r/FreightBrokerStartup, X).
- **Example quotes:**
  - "is someone on your team literally opening each PDF and manually typing the amounts and dates into Excel/TMS?" ([r/FreightBrokers](https://www.reddit.com/r/FreightBrokers/comments/1q8wfyg/how_much_time_does_your_team_actually_waste/), Jan 2026)
  - "Yes this is completely standard at most small shops — pure brute force data entry. The mixed formats make it worse" (same thread)
  - "Every single booking is like 15 separate actions across 8 different windows." ([r/Truckers](https://www.reddit.com/r/Truckers/comments/1te9mb3/is_anyone_else_spending_half_their_day_just/), May 2026)
  - "4 independent research docs all pointed to the same problem: freight rate confirmations." ([X, @JOSlAH_ai](https://x.com/JOSlAH_ai/status/2085705489472442767), Aug 2026)
- **Existing tools:** X-TMS TED (email-to-load), Tai TMS, DAT Broker TMS, EDI. One broker said "Its a nice to have, never a MUST HAVE", which is a counter-signal on willingness to pay.
- **Ease:** **Easy.** Email or PDF to structured fields with a draft for review. Fit is medium: US buyers who need sales, and the TMS vendors are bundling this in.

## 8. Insurance: multi-carrier data re-entry and commission reconciliation
- **Industry:** Insurance. **Who has it:** independent agencies (mostly US personal and commercial lines).
- **Frequency:** 4+ (r/InsuranceAgent: quoting ×2, commissions ×3).
- **Example quotes:**
  - "My agency has like 30 different carriers for home/auto and everyone just quotes the few that are easiest... if a human can move data from a CSV to a portal field then realistically some kind of AI should be able to as well" ([r/InsuranceAgent](https://www.reddit.com/r/InsuranceAgent/comments/1ng3ynh/has_anyone_encountered_a_tool_that_can_actually/), Sep 2025)
  - "I've used raters in the past and while they never work quite right... i spent more time fixing quotes after the rater bridged" ([r/InsuranceAgent](https://www.reddit.com/r/InsuranceAgent/comments/1b7qnff/software_for_generating_quotes_from_multiple/))
  - *(title)* "Agency owners, do you actually check your carrier commission statements, or just trust the deposit?" ([r/InsuranceAgent](https://www.reddit.com/r/InsuranceAgent/comments/1tuxzqr/agency_owners_do_you_actually_check_your_carrier/))
  - *(title)* "How do you handle commission reconciliation when carriers are late reporting?" ([r/InsuranceAgent](https://www.reddit.com/r/InsuranceAgent/comments/1te25ya/how_do_you_handle_commission_reconciliation_when/))
- **Existing tools:** EZLynx, PL Rater, SinglePoint, First Connect, Gaya, Carpe AI (trycarpetai.com), PolicyNest (claims manual reconciliation takes 6–12 hours per agent per month), AMS commission modules.
- **Ease:** Portal form-filling is **hard to medium** (brittle browser automation, and carriers resist it). Commission statement reconciliation is **medium** (PDF/CSV to matching), and it's the better wedge.

## 9. Freelancers chasing late invoices and client updates
- **Industry:** Finance and freelancers.
- **Frequency:** 4 (r/FreelanceProgramming, r/Entrepreneur ×2, r/Freelancers_2025).
- **Example quotes:**
  - "another thing i rly wish i had is like auto reminder emails for invoices… like 1 before the due date, 1 on the day, and 1 after... all the tools i see are bloated or made for teams" ([r/FreelanceProgramming](https://www.reddit.com/r/FreelanceProgramming/comments/1nlzrhc/freelancers_with_5_clients_how_r_u_keeping_track/), Sep 2025)
  - "there have been many times where I can see that a client has viewed my invoice and it will sit for another week or so before I get paid." ([r/Freelancers_2025](https://www.reddit.com/r/Freelancers_2025/comments/1l81lyy/struggles_of_contracting/), Jun 2025)
  - Counter-signal: "I get paid late, I hate chasing invoices, but I've turned off automatic reminder features." ([r/Entrepreneur](https://www.reddit.com/r/Entrepreneur/comments/1pjtqd9/found_a_validated_problem_85_of_freelancers_paid/), Dec 2025)
- **Existing tools:** FreshBooks, Wave, Zoho, Stripe invoicing, Chaser (UK).
- **Ease:** **Easy** technically, but willingness to pay looks weak and the space is saturated.

## 10. Recruiting: CV floods and scheduling
- **Industry:** Recruiting.
- **Frequency:** 4 (r/Recruiter_Advice, r/Recruitment, r/recruitinghell, r/RecruitmentAgencies; all 2026).
- **Example quotes:**
  - "500 to 800 applications per role, most of them not close... most of them feel like ATS keyword filters with a better sales deck." ([r/Recruiter_Advice](https://www.reddit.com/r/Recruiter_Advice/comments/1tn583e/application_review_tools_that_anyone_using_where/), May 2026)
  - "when 80% of applications are AI-polished, trying to detect which ones are "real" is a waste of time." ([r/Recruitment](https://www.reddit.com/r/Recruitment/comments/1riqm61/how_do_you_avoidfilter_ai_job_application_spam/), Mar 2026)
  - "they run hiring through email, spreadsheets, forms, Calendly, maybe Notion, and it feels fine right up until the moment candidates start slipping through the cracks." ([r/RecruitmentAgencies](https://www.reddit.com/r/RecruitmentAgencies/comments/1sosvmx/how_do_small_startups_sololean_hr_agencies_manage/), Apr 2026)
- **Existing tools:** Metaview, HackerEarth, TheCognitive, Workable, Recruitee, Greenhouse, Ashby, Calendly.
- **Ease:** Scheduling is easy. Screening is medium, with bias and legal risk. In the UK, the 2003 Conduct of Employment Agencies Regulations and UK GDPR apply. Fit is low.

## 11. Real estate admin
- **Industry:** Real estate (mostly US agents and transaction coordinators).
- **Frequency:** 4+ (r/RealEstateTechnology ×4, r/RealEstateAdvice, r/realtors).
- **Example quotes:**
  - *(title)* "Manually managing data across the MLS, listings, and other databases?" ([r/RealEstateTechnology](https://www.reddit.com/r/RealEstateTechnology/comments/1mngoih/manually_managing_data_across_the_mls_listings/))
  - *(title)* "How do you write listing descriptions faster without copy-pasting old ones?" ([r/realtors](https://www.reddit.com/r/realtors/comments/1qnu6xa/how_do_you_write_listing_descriptions_faster/))
  - *(title)* "Automate transaction coordinators manual process?" ([r/RealEstateTechnology](https://www.reddit.com/r/RealEstateTechnology/comments/1q0kokq/automate_transaction_coordinators_manual_process/))
  - Small landlords: "spreadsheets are getting annoying" *(title fragment)* ([r/PropertyManagement](https://www.reddit.com/r/PropertyManagement/comments/1s17mmh/what_do_you_guys_use_to_track_rent_payments_for_a/), 2026)
- **Existing tools:** ListedKit (Ava), Jointly, ReBillion, Leni, ListHub. For landlords: Stessa, Baselane, Innago, plus Etsy spreadsheet templates "for under $10".
- **Ease:** Listing copy is easy. TC deadline extraction is medium. MLS sync is hard because access is gated. Fit is low because the buyers are local agents.

## 12. Legal and healthcare admin: medical chronologies, prior auth, eligibility checks
- **Industry:** Legal (personal injury), healthcare admin (US).
- **Frequency:** 5+ (r/legaltech, r/LawFirm, r/medicine with 674 upvotes, many X posts, KevinMD).
- **Example quotes:**
  - "you enter tax ID, NPI, member ID, date of birth, name, your name, your job. Then they transfer you to someone else who asks the same information. Then they repeat this for 20-30 minutes" ([r/medicine](https://www.reddit.com/r/medicine/comments/1en4nxv/prior_auths_are_insane/), 2024)
  - "Most I have seen are not great and struggle with duplicate records." ([r/LawFirm](https://www.reddit.com/r/LawFirm/comments/1nm2mia/ai_medical_chronologies/), Sep 2025)
  - "it cuts my para's time down from like 6 hours to maybe 45 minutes per case." (same thread, Jan 2026)
  - "Tools like ChatGPT work well up to maybe 200 pages, after that the context gets too long" ([r/legaltech](https://www.reddit.com/r/legaltech/comments/1qomvsi/what_actually_works_once_medical_records_hit/), Jan 2026)
- **Existing tools:** InPractice ($0.07/page), ProPlaintiff, Filevine MedChron, Medrecords AI, ChartInsight, DodonAI. For prior auth: R1/Humata, Epic, and many revenue-cycle vendors.
- **Ease:** **Hard** for Ricardo because of US-centric regulation (HIPAA), sensitive data under UK GDPR, professional liability and heavy competition. Volume is huge, but fit is the lowest.

---

## Also seen (small, but easy and good fit)
- **Marketplace job alerts:** "Upwork removed their RSS feed. I'd like a tool that sends me an email when a certain job matching certain job/client filter criteria is made... The inbuilt Upwork alert system sucks." ([HN](https://news.ycombinator.com/item?id=48045237)). Existing tools: Vollna, GigRadar. Easy.
- **Google Sheets formatting:** "Formatting Google Sheets. I work all day every day in google sheets." (same HN thread). Easy to medium.
- **Solo accounting and invoicing:** "As a solo person running a website: Accounting and invoicing. Even for a tiny outfit with quarterly invoicing, it's tedious." ([HN](https://news.ycombinator.com/item?id=46585643))
- **Demand-signal monitoring:** the "is there a tool that..." phrase-mining tactic is itself heavily marketed on X (F5Bot, Syften, PainRadar, Redreach). Founders already treat it as a lead source, so it's a crowded meta-niche.

## Gaps and caveats
- LinkedIn and Facebook groups weren't readable without logging in, so no quotes from them.
- Reddit blocked full-thread fetches. Some quotes are thread titles only, and comment counts weren't re-checked.
- X results were dominated by vendors. User-voice quotes on X came mainly from founders (levelsio and others).
- Frequency counts come from one pass. Treat them as relative, not absolute.
