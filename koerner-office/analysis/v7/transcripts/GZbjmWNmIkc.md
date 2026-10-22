# This AI Finds the Idea, Customers, and Does the Work

- **Video:** [GZbjmWNmIkc](https://www.youtube.com/watch?v=GZbjmWNmIkc) · **Channel:** The Koerner Office · **Uploaded:** 2026-09-16 · **Length:** 43 min · **Transcript:** cached
- **Speakers:** Chris Koerner (host), Alex (guest) · **Format:** tool_review
- **Evidence quality:** C — Product demo by a vendor employee with no revenue or conversion data; anecdotal customer stories; AI-generated research figures unverified. Useful as a capability illustration only. · Promotional conflict: Alex works for Hyper Agent and Chris promotes it with a referral/credits link; likely sponsored.
- **Extraction:** claude-sonnet-5-5 · quotes verified 26/26

## Summary

Chris Koerner interviews Alex from Hyper Agent (built by Airtable), a platform for persistent, named AI agents that browse the web, spin up sub-agents and run on schedules ('live mode'). Demos include an agent that finds local businesses with great reviews but no or poor websites and builds them new sites, an always-on 'Signal' outbound sales agent that builds personalised landing pages per prospect, a pond-dredging lead database proof of concept, and a Facebook Marketplace scout. Chris then uses Hyper Agent to research boring $500k businesses, builds a laundromat opportunity map and saves it as a daily 'Deal Scout' agent. Key takeaway: treat agents as 24/7 employees with narrow permissions, and use them for lead generation, personalised outreach and agency delivery; the content is largely a product demo with promotional bias.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Agent-built websites for local businesses with great reviews but no website** — An AI agent finds well-reviewed local businesses with no or outdated websites, builds a bespoke site for each, and drafts outreach offering to sell or give it away. | agency | deep | 2/3/4/4/3 | 4 |
| I2 | **Always-on outbound sales agent with personalised landing pages (Signal)** — A persistent agent finds prospects matching an ICP, researches each, builds a personalised landing page/video proposal, handles replies and CRM, and reports to Slack hourly. | ai_automation | deep | 3/3/4/3/3 | 4 |
| I3 | **AI visual proposals for inbound leads (landscaping, paving, apparel)** — Agents reply instantly to inbound leads with AI-generated visuals of the proposed work, such as a redesigned yard, repaved lot or branded apparel. | local_service | moderate | 4/3/1/3/3 | 4 |
| I4 | **Pond dredging lead database** — Build a database of ponds needing dredging from satellite, GIS, tax and zoning data and sell leads to pond dredging/maintenance companies. | data_leads | moderate | 2/3/4/4/3 | 2 |
| I5 | **Sell niche AI agents to clients (AI automation agency on Hyper Agent)** — AI agencies build a niche agent (e.g. pond dredging project manager) and stamp it out per client in separate workspaces, with clients paying the AI costs. | ai_automation | moderate | 2/2/3/4/2 | 5 |
| I6 | **Facebook Marketplace scout agent** — A persistent agent browses Facebook Marketplace hourly for items matching criteria and messages sellers or alerts the owner. | arbitrage_reselling | mention | 4/4/1/3/3 | 4 |
| I7 | **Laundromat opportunity map / deal scout** — Agent maps laundromats within 100 miles of a zip code, flags gap areas and re-runs daily to scout new locations. | real_estate | moderate | 3/4/4/3/3 | 4 |
| I8 | **Parking lot striping** — Parking lot line striping business where paint fades every 18-48 months, giving repeat work. | local_service | moderate | 2/2/0/4/2 | 4 |
| I9 | **Other boring businesses from AI research list** — Septic and drainage, portable restroom routes, commercial janitorial, pest control routes, elevator maintenance, fire protection inspection, tree care, towing/impound, pallet recovery, multi-store laundromats and car washes. | local_service | mention | 2/2/0/4/2 | 3 |

### I1. Agent-built websites for local businesses with great reviews but no website

- **Customer:** Local small businesses (e.g. auto shops) with 300+ Google reviews but no or outdated website
- **Problem:** Great local businesses are hard to find online because they lack a modern website
- **Offer:** A ready-made, business-specific website with booking and estimate features, stood up within days; possibly given free as a hook
- **Business model:** One-off website build fees (or free site as a lead-in to paid services)
- **Pricing:** Per-site implementation fee, or free giveaway as lead magnet.  No prices stated; example site's estimate pricing was just agent best-guess
- **Acquisition:** cold_email: Agent finds contact info, drafts per-business outreach from the user's email; user can approve or let the agent send. Old manual approach was said to get 0.5-1% response.; google_business_profile_maps: Candidates sourced by finding businesses with strong Google reviews but weak or no web presence
- **Delivery:** Agent researches the brand and customer reviews, then builds the website (with booking system and estimate tool) in roughly 20-30 minutes for a batch; a human would customise it to the specific business once the deal is won.
- **Unit economics (claims):** Whole run (research to multiple built sites) took about 20-30 minutes; Manual outreach response rate 0.5-1%
- **Tools:** Hyper Agent, Google reviews/Business Profile, email
- **Startup cost:** Free skill on the Hyper Agent marketplace; platform credits needed
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Works in the UK via Google reviews; outreach must respect PECR (cold email to limited companies only, no unsolicited messages to sole traders). Many UK micro-businesses are sole traders, shrinking the legal target pool.
- **Risks:** PECR restricts cold outreach to sole traders; Building sites unsolicited may be low-converting; AI sites need customisation and quality checks; Response rates are low
- **Automation [E]:** acquisition 2/5 (Agent finds prospects and drafts emails, but UK PECR bars unsolicited email to sole traders/individuals; only limited companies are legal targets, so heavy filtering and human approval needed.); onboarding 3/5 (Agent can reply to inbound responses, collect requirements and tailor the site; human confirms scope.); delivery 4/5 (Agent generates the site from reviews and brand research; human spot checks and domain/hosting setup.); billing 4/5 (Invoices and payment links can be automated with standard tools.); support 3/5 (Inbox agent handles routine queries; edits and issues need occasional human input.)
> "Your agent can go and find these candidates and actually build them new digital properties to the point where you could sell the implementation of that website specific to them." — Alex (~3:40)
> "Or there's even this notion that maybe that website is just like a free giveaway because of just how easy it is and how fast it is to do this at scale." — Alex (~4:04)

### I2. Always-on outbound sales agent with personalised landing pages (Signal)

- **Customer:** B2B companies selling high-consideration products (example: Swiss Solar selling self-cleaning solar panel tech to industrial solar project leads)
- **Problem:** Cold emails get ignored; buyers say 'send me materials'; slow follow-up loses warm leads
- **Offer:** Hyper-personalised proposal pages (hero video, screenshots, explainers) for each prospect, with a CTA to book a study or pilot
- **Business model:** Platform subscription/credits for the user; the underlying use is B2B lead generation
- **Pricing:** Not stated.  Hyper Agent pricing not given; free initial credits via link
- **Acquisition:** cold_email: Personalised outreach linking to a bespoke landing page per project lead, plus overnight inbox agent replying to inbound and replies; paid_social: Agents also run ads end to end: creative strategy, spend optimisation, scaling winners and killing losers
- **Delivery:** Agent runs in 'live mode', re-running its self-written prompt hourly: sources prospects, deep research, builds pages and videos, updates CRM, posts to Slack, and learns which messaging gets replies.
- **Unit economics (claims):** Runs hourly, 24/7; No conversion data given
- **Tools:** Hyper Agent, Slack, CRM, AI image/video generation
- **Startup cost:** not stated; free credits offered via link
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Technique is location-agnostic; apply PECR and GDPR to prospect data.
- **Risks:** Platform vendor demo with no conversion numbers; PECR/GDPR compliance for outreach; Platform dependence
- **Automation [E]:** acquisition 3/5 (Agent sources and personalises at scale; UK PECR limits cold email to limited companies and needs human approval/screening.); onboarding 3/5 (Inbox agent responds immediately and books calls.); delivery 4/5 (Pages, videos and research generated by agents.); billing 3/5 (Depends on the seller's own process; not covered.); support 3/5 (Agent handles replies; humans take sales calls.)
> "The most popular agent on our marketplace... is called Signal. This is your always on 247 sales agent." — Alex (~9:17)

### I3. AI visual proposals for inbound leads (landscaping, paving, apparel)

- **Customer:** Landscaping, commercial paving and corporate apparel companies and their customers
- **Problem:** Competitors take days to respond and customers cannot visualise the result
- **Offer:** Instant reply with a visual of the finished result and rough estimate
- **Business model:** Per-job sales for service companies, enhanced by agent-generated proposals
- **Pricing:** not stated.  
- **Acquisition:** other: Inbound leads answered immediately; paving firm uses satellite imagery plus AI image generation with cost estimates; apparel firm puts a prospect's branding on products
- **Delivery:** Physical work (landscaping, paving) done by crews; agent only produces proposals.
- **Unit economics (claims):** Competitors typically take one to two days to respond
- **Tools:** Satellite imagery, AI image generation, Hyper Agent
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Works the same; UK satellite imagery available.
- **Risks:** Anecdotal, no results given; AI visuals may overpromise vs actual work
- **Automation [E]:** acquisition 4/5 (Inbound lead response and proposal generation can be fully agent-run.); onboarding 3/5 (Agent collects photos and job details.); delivery 1/5 (Physical landscaping/paving work needs crews.); billing 3/5 (Invoicing automatable; quotes need human sign-off.); support 3/5 (Agent handles follow-up questions.)
> "We have a paving company that is using satellite imagery of uh large lots like parking lots that are clearly, you know, past their prime." — Alex (~16:04)

### I4. Pond dredging lead database

- **Customer:** Pond dredging and maintenance companies; ranch/farm owners
- **Problem:** No directory of the roughly 800,000 Texas farm and ranch ponds exists
- **Offer:** Sheet of ponds with size, address and need signals
- **Business model:** Sell lead lists or run pond dredging leads
- **Pricing:** not stated.  
- **Acquisition:** 
- **Delivery:** Agent sub-agents check satellite data and zoning applications in parallel and produce a leads webpage.
- **Unit economics (claims):** Claude claimed about 800,000 ponds on Texas farms and ranches (unverified)
- **Tools:** Hyper Agent, satellite/GIS data
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 2/5 — Texas ranch ponds are US-specific; UK analogue (farm ponds, lakes) is much smaller and data sources differ.
- **Risks:** Unproven proof of concept; Data accuracy; Small market in the UK
- **Automation [E]:** acquisition 2/5 (Selling lead lists to companies needs outreach; limited-company cold email is legal.); onboarding 3/5 (Data delivery could be self-serve.); delivery 4/5 (Agent compiles lead data; accuracy needs checks.); billing 4/5 (Standard online billing.); support 3/5 (Routine queries handled by an agent.)
> "I said, is there a directory? Is there a place where I could sort through that? It's like, no, that's not a thing." — Chris Koerner (~17:36)

### I5. Sell niche AI agents to clients (AI automation agency on Hyper Agent)

- **Customer:** Small niche businesses; AI implementation agencies
- **Problem:** Agencies hack together private servers and struggle to package, deploy and bill agents
- **Offer:** Templated, niche-specific agents managed by the agency in per-client workspaces
- **Business model:** Agency setup and management fees; client pays platform AI usage
- **Pricing:** not stated.  Client pays ongoing AI costs
- **Acquisition:** 
- **Delivery:** Agency configures and edits agents; clients use them as end users.
- **Unit economics (claims):** 
- **Tools:** Hyper Agent teams/workspaces
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 5/5 — Location-independent.
- **Risks:** Platform dependence; Vendor-sourced claim
- **Automation [E]:** acquisition 2/5 (Outbound to limited companies only; needs human sales.); onboarding 2/5 (Needs client-specific configuration.); delivery 3/5 (Template stamped out; agency tweaks.); billing 4/5 (Platform handles usage billing.); support 2/5 (Agency handles config changes.)
> "that becomes your template that you then stamp out across all your clients." — Alex (~21:40)

### I7. Laundromat opportunity map / deal scout

- **Customer:** Prospective laundromat investors/operators
- **Problem:** Hard to see which towns lack laundromats
- **Offer:** Interactive published map with reviews, start-up cost and first-customer plan
- **Business model:** Research asset for investing in a multi-store laundromat portfolio
- **Pricing:** n/a.  
- **Acquisition:** seo_organic_search: Chris published the page with search engine indexing allowed
- **Delivery:** Agent scraped Google Places, used census data, and built an interactive map with 78 laundromats and 4 gap areas.
- **Unit economics (claims):** 78 laundromats and four screening gap areas found
- **Tools:** Hyper Agent, Google Places, Census data
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Same approach works with UK Google Places and ONS data.
- **Risks:** Scraped data may be incomplete; Demo not a validated business
- **Automation [E]:** acquisition 3/5 (SEO pages can attract investors.); onboarding 4/5 (Self-serve.); delivery 4/5 (Map generation is automated; the underlying laundromat business is physical.); billing 3/5 (No billing model stated.); support 3/5 (Minimal.)
> "Interactive map with 78 laundromats and four screening gap areas, overlapping searches, and then it even has a design here." — Chris Koerner (~41:47)

### I8. Parking lot striping

- **Customer:** Commercial property owners with parking lots
- **Problem:** Faded lot lines need repainting regularly
- **Offer:** Striping services
- **Business model:** Per-job and contract services
- **Pricing:** per job.  
- **Acquisition:** 
- **Delivery:** Physical night work by crews.
- **Unit economics (claims):** Agent report: 8,000-90,000 to start; 35-40% net profit; needs $1.25-1.43M revenue for $500k profit
- **Tools:** 
- **Startup cost:** 8,000-90,000 per AI report; Chris says you could start for almost nothing
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Demand exists in the UK; regulations and pricing differ.
- **Risks:** Night work, weather windows, bid accuracy
- **Automation [E]:** acquisition 2/5 (Quote-driven B2B sales.); onboarding 2/5 (Site measurement.); delivery 0/5 (Physical painting.); billing 4/5 (Invoicing.); support 2/5 (Scheduling.)
> "You could start this for almost nothing. The guy that I talked to actually did." — Chris Koerner (~39:45)

## Revenue and metric claims (unverified claims)

- **Agent run from research to built websites took about 20-30 minutes** (hours, first-hand, claimant: Alex)
  > "This whole run was about maybe 20 to 30 minutes from the research finding the candidates to actually building all these unique websites." — Alex (~4:23)
- **Cold outreach response rate of 0.5-1% under the old manual approach** (response_rate, second-hand, hypothetical, claimant: Chris Koerner)
  > "Your response rate is going to be 0.5%, 1% maybe." — Chris Koerner (~5:33)
- **Agents cost 99% less than a human** (cost, first-hand, claimant: Chris Koerner)
  > "This is someone on my quote unquote payroll that never stops working and costs, you know, 99% less than an actual human." — Chris Koerner (~43:11)
- **About 800,000 ponds on farms and ranches in Texas** (other, second-hand, claimant: Claude (relayed by Chris Koerner))
  > "How many ponds are there on farms and ranches in Texas?" 800,000." — Chris Koerner (~17:32)
- **Parking lot striping has 35-40% net profit** (margin, second-hand, claimant: AI research brief (read by Chris))
  > "35 to 40% net profit. You would need $1.25 to $1.43 million in revenue to have 500,000 in net profit." — Chris Koerner (~39:51)
- **Parking lot striping startup cost 8,000-90,000 per AI report** (cost, second-hand, claimant: AI research brief (read by Chris))
  > "8,000 to 90,000 to start, which is not fully accurate." — Chris Koerner (~39:42)
- **Laundromat map found 78 laundromats and four gap areas** (other, first-hand, claimant: Chris Koerner)
  > "Interactive map with 78 laundromats and four screening gap areas, overlapping searches" — Chris Koerner (~41:47)
- **Hyper Agent team has about 20 agents for 4 people** (other, first-hand, claimant: Alex)
  > "we've got four of us on the growth and marketing team here, and we have probably 20 agents" — Alex (~8:41)

## Tactics and playbook steps

**Agent-built website as outreach hook** (acquisition)
1. Prompt the agent to find local businesses with strong reviews but no or outdated website
2. Agent gathers contact info and learns brand from reviews
3. Agent builds a bespoke site and drafts a personalised email
4. Offer to implement within days, or give it free to open the conversation
5. Human approves emails, or trusts the agent to send
> "here is an example of the type of website we'd be able to stand up for you within days." — Alex (~3:59)

**Personalised landing page per prospect** (sales)
1. Define ICP
2. Agent researches the specific project lead
3. Build a personal landing page with hero video, screenshots and a CTA to a study or pilot
4. Send it instead of a plain cold email
5. Review which messaging earns replies and feed learnings back

**Persistent 'live mode' agent with permission separation** (operations)
1. Describe the job like a job description
2. Let the agent write its own loop prompt
3. Schedule it hourly
4. Have it post updates to Slack or Telegram
5. Separate agents for brand posting versus customer/financial data to enforce guardrails
> "I can create hard guard rails by assigning those permissions to different agents." — Alex (~8:33)

**Instant visual response to inbound leads** (sales)
1. Agent replies to inbound leads immediately
2. Generate an image of the finished result from the customer's photo
3. Send with an estimate before competitors respond

**Save research as a scheduled agent** (operations)
1. Run the research prompt
2. Click save as agent and name it
3. Add an invocation schedule in plain English with specifics (e.g. every morning 7am, new laundromats in other zip codes)

## Lessons

- *automation_ai*: Treat agents as persistent employees with a job description, narrow permissions and scheduled runs rather than one-off prompts.
- *customer_acquisition*: Personalised, visual deliverables (a built site, a mock-up) beat generic cold outreach because they show effort and let buyers self-serve asynchronously.
- *customer_acquisition*: Fast response to inbound leads is a competitive advantage in local services.
- *automation_ai*: Start with a tedious computer task you already do and ask an agent to build a dedicated agent for it.
- *scaling*: Agencies can package a niche agent as a template and deploy it per client in separate workspaces.
- *operations*: Have agents prompt humans (reports, approvals) rather than humans prompting agents.
- *finance_unit_economics*: Use the 'seller's discretionary earnings' view, not profit, when judging what a small business pays its owner.
- *validation_testing*: Treat AI-generated income figures skeptically; verify with primary sources.

## Warnings and mistakes

- Agent output needs iteration: the motion design agent typically needs three or four rounds of feedback to meet a high standard.
- Broker-reported earnings are unaudited; the AI flagged strong claims as unverified.
- Keep customer/financial data agents separate from public-posting agents to avoid data crossing.
- Reaching $500k owner profit usually requires multi-crew or multi-location scale.

## Tools mentioned

Hyper Agent (Persistent AI agent platform with browser, sub-agents, live mode and marketplace; Free initial credits via link), Airtable (Company behind Hyper Agent), Slack (Agent status updates and messaging), Telegram (Messaging agents), WhatsApp (Messaging agents/notifications), Claude (Used for research and to prepare criteria files), Facebook Marketplace (Equipment sourcing), Google Places / Maps (Scraping laundromats and map), GPT 5.6 (Default model in Hyper Agent)
