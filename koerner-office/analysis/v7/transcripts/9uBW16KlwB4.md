# You Can Now Build Apps for Free With Google AI Studio (w/ Google Insider)

- **Video:** [9uBW16KlwB4](https://www.youtube.com/watch?v=9uBW16KlwB4) · **Channel:** The Koerner Office · **Uploaded:** unknown · **Length:** 50 min · **Transcript:** ok
- **Speakers:** Chris Koerner (host), Logan Kilpatrick (guest) · **Format:** operator_interview
- **Evidence quality:** C — Mostly speculative discussion and live demos from a Google product lead; few concrete business numbers, and the only revenue claims are second-hand (John Rush, levels.io). Chris has a brief first-hand voice-agent anecdote without numbers. · Promotional conflict: Logan promotes Google AI Studio (his employer's product) and Chris is a Google shareholder; the episode also includes ads for Go High Level and Chris's TK Owners community.
- **Extraction:** claude-sonnet-5-5 · quotes verified 23/23

## Summary

Chris Koerner interviews Logan Kilpatrick, who leads the developer product team for Google AI Studio and the Gemini API at Google DeepMind. They discuss how vibe coding in AI Studio makes it nearly free to build and ship many small AI apps, and they live-build two apps: a video analysis engine and a voice AI lead-gen agent. Ideas covered include niche single-purpose AI apps, bundles of AI tools for one persona, an AI implementation agency for small businesses, voice AI agents and a text-based AI travel companion. Key takeaway: the cost of building software is now trivial, so take many niche shots, iterate through about 10 prompts, and use vibe-coded demos as outreach. Chris states this is not sponsored but he is a Google shareholder.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **AI implementation agency for small businesses** — Sell AI setup and custom vibe-coded tools to small businesses, using free vibe-coded demos of their own site or products as outreach. | agency | moderate | 2/2/3/4/2 | 4 |
| I2 | **Voice AI agent lead-gen landing page** — Replace a web lead form with a voice AI agent that collects name, email and company, then triggers email and CRM entry. | ai_automation | moderate | 3/4/4/4/3 | 4 |
| I3 | **AI video analysis app** — A tool that ingests video and extracts key takeaways, scenes, trends and customisable reports using Gemini's native video understanding. | saas_software | moderate | 3/4/5/4/3 | 5 |
| I4 | **Niche single-purpose AI apps (haircut, curtains, furniture)** — Build many very thin vertical AI apps (haircut preview, curtains, furniture placement, photo restoration) using new models, and use them as a funnel. | saas_software | moderate | 3/5/5/4/4 | 5 |
| I5 | **Persona bundle of AI tools** — Package around 7-10 thin AI tools for one persona (student, lawyer) to reach critical mass in go-to-market. | saas_software | mention | 3/5/4/4/3 | 5 |
| I6 | **Portfolio of AI tools with cross-selling (John Rush model)** — Run a dozen to 20 AI tools sold to indie hackers, cross-selling across email lists and sharing ad accounts and infrastructure. | saas_software | mention | 4/5/5/5/3 | 5 |
| I7 | **Text-message AI travel companion** — An AI travel companion that texts you at each stage of a journey and can join group chats, built with Twilio. | saas_software | mention | 3/4/5/4/3 | 4 |
| I8 | **Video archive search pipeline for creators and companies** — Pipeline that searches across a creator's or company's video library to surface insights. | ai_automation | mention | 2/3/4/4/3 | 5 |

### I1. AI implementation agency for small businesses

- **Customer:** Small businesses and family businesses with little time or AI know-how
- **Problem:** Owners know AI matters but lack the time and skill to implement it; even Fortune 200 executives need hand-holding
- **Offer:** Implement AI tools for them, e.g. redesigned websites, mood boarding or virtual try-on apps built with vibe coding
- **Business model:** Service fees, possibly monthly retainers
- **Pricing:** Monthly service fee (speculative). Chris's example of what some small businesses may not afford USD 1000 per month Pricing not discussed in detail; the $1,000/month is only a passing remark
- **Acquisition:** other: Personalised outreach: vibe code a redesign of the prospect's website or products with AI and send it as a lead-gen demo, e.g. 'I redesigned your website using AI. Here it is.'
- **Delivery:** Vibe code apps in AI Studio, sometimes live on a sales call, then deploy them for the client; the agency operator does the work
- **Unit economics (claims):** 400 million small businesses worldwide (Chris, hypothetical); Demo build cost is basically zero
- **Tools:** Google AI Studio, Gemini
- **Startup cost:** Approximately zero for demos; building in AI Studio is free
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Works the same in the UK. Cold email only to limited companies under PECR; sole traders need consent.
- **Risks:** Market size unverified; Logan admits he doesn't know the numbers; Clients may not pay for easily built tools; Low barrier means many competitors
- **Automation [E]:** acquisition 2/5 (Agents can generate demo redesigns, but UK PECR bars unsolicited outreach to sole traders, so outreach is limited to limited companies by email.); onboarding 2/5 (Discovery calls and scoping with owners are mostly human, with AI tooling support.); delivery 3/5 (Vibe coding tools build most of each app, but iteration and client fit need human checks.); billing 4/5 (Invoices and subscriptions can be automated.); support 2/5 (Non-technical owners need hand-holding and change requests.)
> "I redesigned your website using AI. Here it is. If this seems interesting to you, let me know. If not, like your marginal cost was basically nothing." — Logan Kilpatrick (~42:06)
> "there will always be business owners that just want someone to do it for them" — Chris Koerner (~39:01)

### I2. Voice AI agent lead-gen landing page

- **Customer:** Businesses with web lead forms; Chris uses it on his own lead magnet
- **Problem:** Forms are low-engagement; callers hate hold times
- **Offer:** Voice agent built on Gemini Live API that fills a lead form conversationally and kicks off follow-up workflows
- **Business model:** Build and sell to businesses as a service, or use on own site as a lead magnet
- **Pricing:** not stated.  not stated
- **Acquisition:** 
- **Delivery:** Vibe coded in AI Studio from one prompt in 66 seconds; the demo worked nearly zero-shot but misheard the name, and the system prompt needs guardrails (only talk about the company).
- **Unit economics (claims):** Built in 66 seconds with one prompt
- **Tools:** Google AI Studio, Gemini Live API
- **Startup cost:** Free to build
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Works in the UK. Must disclose AI and handle recordings and personal data under UK GDPR.
- **Risks:** Name transcription errors; Agent answers off-topic questions unless constrained; Novelty effect may fade
- **Automation [E]:** acquisition 3/5 (Inbound website visitors; marketing around it is not covered.); onboarding 4/5 (Template deploy per client.); delivery 4/5 (The agent runs unattended once deployed, with occasional prompt tuning.); billing 4/5 (Subscription billing is automatable.); support 3/5 (Agents handle most issues, with occasional human checks.)
> "I had this lead magnet that was just a form for this initiative I have and I just swapped it out with a voice AI agent" — Chris Koerner (~33:24)

### I3. AI video analysis app

- **Customer:** Content creators, companies with internal video archives
- **Problem:** Hard to extract intelligence from video content
- **Offer:** Upload a video and get analysis, 10 insights and customisable reports
- **Business model:** Not stated; product concept
- **Pricing:** not stated.  not stated
- **Acquisition:** 
- **Delivery:** Software built with one prompt using Gemini 2.5 Pro in AI Studio; a 270MB video was analysed live
- **Unit economics (claims):** 
- **Tools:** Google AI Studio, Gemini 2.5 Pro
- **Startup cost:** Free to build
- **Time to first revenue:** not stated
- **UK applicability [E]:** 5/5 — No location dependence.
- **Risks:** Gemini does the heavy lifting so the product is easy to copy; Needs a distinct product experience
- **Automation [E]:** acquisition 3/5 (Would be SEO or content driven; not discussed.); onboarding 4/5 (Self-serve upload.); delivery 5/5 (Model processes video unattended.); billing 4/5 (Standard SaaS billing.); support 3/5 (Agents can handle routine support.)
> "The question then is like what is the product experience that you sort of build around that model and I think that's where the magic is." — Logan Kilpatrick (~20:20)

### I4. Niche single-purpose AI apps (haircut, curtains, furniture)

- **Customer:** Consumers with one specific problem
- **Problem:** People want one narrow outcome without complex everything-apps
- **Offer:** Single-purpose AI tools, e.g. upload a photo and see seven curtain types
- **Business model:** Paid usage or subscriptions; funnel into a larger offer
- **Pricing:** not stated.  not stated
- **Acquisition:** organic_social_content: Free social-first engagement and showing off builds
- **Delivery:** Vibe code in AI Studio and deploy in about 90 seconds; hosting costs when serving users
- **Unit economics (claims):** Tens of thousands of apps vibe coded on Nano Banana launch day (Logan)
- **Tools:** Google AI Studio, Nano Banana
- **Startup cost:** Free to build
- **Time to first revenue:** not stated
- **UK applicability [E]:** 5/5 — Works the same.
- **Risks:** Crowded; many copy the same idea on day one; Thin search volume per niche
- **Automation [E]:** acquisition 3/5 (Social posting can be agent-run; SEO volume for tiny niches is thin.); onboarding 5/5 (Self-serve.); delivery 5/5 (Model generates outputs unattended.); billing 4/5 (Stripe-style billing.); support 4/5 (Low support needs.)
> "I just wish people had more of a bias towards like that's not niche enough as opposed to that's too niche." — Chris Koerner (~17:16)

## Revenue and metric claims (unverified claims)

- **Building in AI Studio costs nothing; paid only when deploying and serving users** (cost, second-hand, claimant: Logan Kilpatrick)
  > "to actually build the thing is doesn't cost anything" — Logan Kilpatrick (~6:14)
- **Voice agent app built in 66 seconds** (hours, first-hand, claimant: Chris Koerner)
  > "All right, it looks like it's done. 66 seconds." — Chris Koerner (~0:04)
- **John Rush makes $3M a year from a dozen AI tools** (revenue, second-hand, claimant: Chris Koerner)
  > "he makes 3 million bucks a year from a dozen AI tools" — Chris Koerner (~14:10)
- **Levels.io style: three of 20 ideas worked and became $100,000/month businesses** (revenue, second-hand, claimant: Logan Kilpatrick)
  > "they had like 20 ideas and only three of them worked and the three that worked are now like, you know, $100,000 a month businesses" — Logan Kilpatrick (~11:35)
- **400 million small businesses worldwide that need AI** (customers, second-hand, claimant: Chris Koerner)
  > "there's 400 million small businesses around the world" — Chris Koerner (~42:38)
- **Tens of thousands of apps built on Nano Banana launch day** (customers, second-hand, claimant: Logan Kilpatrick)
  > "users inside of AI Studio were vibe coding literally tens of thousands of AI-powered apps using that new model" — Logan Kilpatrick (~5:38)

## Tactics and playbook steps

**Vibe-coded demo as lead gen** (acquisition)
1. Pick a target company website or product
2. Reimagine it with AI via a vibe coding tool in minutes
3. Send the redesign to the owner as outreach
4. Frame it as zero marginal cost to them
5. Optionally vibe code live on a sales call
> "you can go find this com- the company website that you want to work with, you can take their products or their website, reimagine it with AI" — Logan Kilpatrick (~41:48)

**High-volume shots on goal** (product)
1. Build one AI app a day with about 30 minutes of work
2. Expect the first ~50 to flop
3. Remix existing ideas with your own twist
4. Publish everything
> "you actually could be building one AI app every day with like probably 30 minutes of work" — Logan Kilpatrick (~10:52)

**Iterate about ten prompts** (product)
1. Don't abandon after a first imperfect output
2. Use follow-up prompts and suggested prompts to refine
3. Keep going until it works
> "you're 10 prompts away from the home run" — Logan Kilpatrick (~0:30)

**Constrain voice agent via system instructions** (product)
1. Review the generated system instructions
2. Add 'only talk about [company]' and 'do not talk about anything else'
3. Disclose that it's an AI
4. Review transcripts daily and follow up with leads

**Win on a niche, then funnel to the larger product** (acquisition)
1. Solve one very specific problem (e.g. curtains)
2. Use it to pull users into the broader offering

## Lessons

- *validation_testing*: When building software costs near zero, the winning strategy shifts from one big swing to many cheap experiments.
- *niche_selection*: Solving your own problems, where you have domain insight, gives the best odds, but outsiders sometimes find overlooked angles.
- *niche_selection*: Err towards niches that feel too small; the real customer need is often one narrow task.
- *offer_design*: The moat is the product experience built around a commodity model, not the model itself.
- *customer_acquisition*: Many decision makers, even senior executives, lack AI skills, which creates demand for implementation services.
- *mindset_execution*: Persistence and agency matter more than syntax knowledge; error messages build resilience.
- *customer_acquisition*: A fast working demo of the prospect's own problem sells the idea's feasibility and beats a generic pitch.
- *scaling*: New model launches spawn thousands of copycats on day one; differentiate via remixing, positioning and niche insight.
- *scaling*: A portfolio of tools lets you cross-sell across lists, share ad accounts and infrastructure, and learn faster what customers want.

## Warnings and mistakes

- AI flight-booking is overhyped: easy problem, high cost when wrong; solve the hard orchestration instead.
- Giving up after the first imperfect output is the most common vibe coding mistake.
- The voice agent demo mis-transcribed the name and, without guardrails, would answer off-topic questions; it didn't work zero-shot.
- The voice agent novelty effect may fade over time.

## Tools mentioned

Google AI Studio (Vibe coding platform for AI apps (ai.studio/build); Free to build; pay when deploying and serving users), Gemini API / Gemini 2.5 Pro (Model for code generation and video understanding), Gemini Live API (Real-time voice agents), Nano Banana (Image generation/editing model), Veo 3 (Video generation), NotebookLM (Research assistant that repurposes content), Google Labs / Opal (Early-stage Google AI experiments), AI Mode in Google Search (Conversational AI search), Gemini computer use model (Agent that navigates UIs and automates repetitive UI tasks), Twilio (SMS/text integration for travel companion), Go High Level (White-label CRM platform (sponsor ad); 30 days free via gohighlevel.com/chris)
