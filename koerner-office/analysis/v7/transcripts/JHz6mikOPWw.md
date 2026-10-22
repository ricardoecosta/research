# He Can't Code but His AI Agents Make Him $5K/Month

- **Video:** [JHz6mikOPWw](https://www.youtube.com/watch?v=JHz6mikOPWw) · **Channel:** The Koerner Office · **Uploaded:** 2026-04-08 · **Length:** 44 min · **Transcript:** transcribeyoutube
- **Speakers:** Chris Koerner (host), Vadim (guest) · **Format:** operator_interview
- **Evidence quality:** B — First-hand operator with specific figures (revenue, tiers, user count, margin), but all are unverified, only about one month of revenue, a very young product, and margin/cost detail is vague. Conversion and churn data were admittedly missing. · Promotional conflict: Vadim sells Vugola and promotes it; host plugs Beehiiv (sponsor) and TK Owners community.
- **Extraction:** claude-sonnet-5-5 · quotes verified 28/28

## Summary

Chris Koerner interviews Vadim, an 18-year-old non-coder who vibe-coded Vugola, an all-in-one clipping, scheduling and captioning SaaS, using Claude Code, Supabase, Vercel and GitHub. He claims $5K revenue in 30 days at ~80% margin, with 267 paying users on $9/$39/$99 plans, acquired mainly via Twitter after Reddit/X outreach by an OpenClaw agent. He also describes running a small team of Hermes agents (CEO, marketing, growth, coding, support) and shares prompting tips, PostHog analytics, Paperclip, and mind-mapping for niche research. Key takeaway: a solo founder can build and run a niche SaaS with AI agents cheaply, but the numbers are self-reported and the product is still in beta.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Vugola - all-in-one AI clipping, scheduling and captioning SaaS** — Subscription web app that turns long videos into short clips, captions them and schedules posts, aimed at clippers, podcasters and marketers. | saas_software | deep | 2/3/4/5/3 | 4 |
| I2 | **Agentic clipper integration with Content Rewards** — Let AI agents act as clippers by finding campaigns, clipping, scheduling and submitting through an API for payout per thousand views. | ai_automation | moderate | 3/3/4/4/2 | 4 |
| I3 | **Agentic automated lead generation service** — Agent with a daily cron job that finds leads, messages them and follows up, suggested as a niche to build. | data_leads | mention | 2/3/4/5/3 | 3 |

### I1. Vugola - all-in-one AI clipping, scheduling and captioning SaaS

- **Customer:** Clippers, podcasters, streamers, entrepreneurs, affiliate marketers and smaller creators who need short-form clips
- **Problem:** Existing clipping tools (e.g. Opus Clip) are seen as expensive, slow, and reuse the same clip moments across multiple clips, wasting credits
- **Offer:** Clip long-form video using Gemini transcript and visual analysis (face tracking, cropping, speaker emotion), then caption and schedule natively in one tool; built to be agent-friendly
- **Business model:** Monthly subscription tiers with credits, plus quarterly/yearly upsells and one-off credit packs
- **Pricing:** Three monthly paid tiers, no free plan; checkout upsells to quarterly plan and extra credit packs. Starter plan USD 9 per month; Creator plan USD 39 per month; Agency plan USD 99 per month Free plan removed around end of Feb because users farmed free credits with multiple accounts; $9 minimum acted as a filter and sales started. Popup upsell from monthly to quarterly, then custom checkout upselling credit packs; one day reached about $900 after adding upsells.
- **Acquisition:** organic_social_content: Building in public on Twitter/X; purely X for the last two months, personal brand ~27,000 followers; now starting Instagram, YouTube Shorts and TikTok.; cold_sms_dm: OpenClaw marketing agent scanned Reddit, LinkedIn and X for people complaining about clipping tools or Opus Clip (e.g. during a 48-hour outage), produced a list of usernames and posts, and Vadim DMed them offering free trial. Got ~450 free users and lots of feedback. Manual DMs to individuals may breach PECR in the UK.; partnerships: In talks with Content Rewards founder about an API/agent-friendly integration so agent clippers can use Vugola and submit clips to campaigns.
- **Delivery:** Software delivered via web app; clip generation runs on Gemini API credits (transcript and video analysis). Built and maintained by Vadim with Claude Code and Codex plus a team of Hermes agents.
- **Unit economics (claims):** $5,000 revenue in last 30 days; 80% profit margin claimed; 267 paying users; 10,000+ clips generated; ~$400-600/month spent on AI coding and agent subscriptions; one-day revenue spike ~$900 after upsells
- **Tools:** Claude Code, Codex, Lovable, Supabase, Vercel, GitHub, Gemini API, Stripe, PostHog, OpenClaw, Hermes Agent, Chrome DevTools MCP, Paperclip, Miro, Twitter/X
- **Startup cost:** Not stated explicitly; ongoing Claude Max about $200/month plus a second Codex plan (~$200/month), agents ~$400-600/month total; spent ~$500 of Lovable credits in 4 days early on
- **Time to first revenue:** Started building Oct/Nov; first sale around Feb 2 (about 3-4 months); first full month (March) about $5,000
- **UK applicability [E]:** 4/5 — SaaS and Stripe work the same in the UK. Cold DM outreach to individuals needs care under PECR/GDPR; handle VAT and platform terms for social scheduling.
- **Risks:** Self-reported, unverified numbers; product in beta; Competes with Opus Clip, which raised $50M; Churn typically in 1-3 months; no conversion/retention data set up early; Heavy dependence on Gemini API costs and credit pricing; margins could erode; Reliance on Twitter alone as a channel; Platform API/policy changes for scheduling and clipping; Frequent free-credit abuse before the paywall
- **Automation [E]:** acquisition 2/5 (Twitter content is human-led. Agent-found social posts and manual DMs are cold outreach that is risky under PECR for individuals; inbound channels (SEO, app listings, paid ads, content) could be automated.); onboarding 3/5 (Self-serve SaaS signup and Stripe checkout; he admits no onboarding or offboarding flows were set up initially, but they can be built in-app with agents.); delivery 4/5 (Clips are produced by software with Gemini and API credits; agents and Claude Code maintain the product with occasional human oversight.); billing 5/5 (Stripe subscriptions and upsells run unattended.); support 3/5 (He claims a customer support agent and PostHog monitoring via cron jobs, but quality is unverified and a human still handles escalations.)
> "in the last 30 days I made $5,000. So in the last 30 days I made 5K as like no coding experience" — Vadim (~6:24)
> "I have three three paid tiers. So, first is like a $9 plan and then it's a $39 plan and it's a $99 plan." — Vadim (~7:52)
> "I'm going to make the $9 plan like minimum and that's going to filter people and I'm actually going to see if people actually want to use my software." — Vadim (~20:16)

### I2. Agentic clipper integration with Content Rewards

- **Customer:** Clipping campaign platforms (Content Rewards, Whop) and agent-using clippers
- **Problem:** Clipping workflows are manual: find campaign, locate source video, clip, edit, post, and submit links
- **Offer:** Agent-ready API or skill so an agent runs the full clip-schedule-submit loop
- **Business model:** Clipper pay per thousand views via campaign platforms; Vugola would provide agent-ready tooling
- **Pricing:** not stated.  Clippers earn about $0.10-$1 per thousand views per speaker's examples
- **Acquisition:** partnerships: Messaged the Content Rewards founder on Twitter and is in talks about an API for agents.
- **Delivery:** Agents perform the clipping workflow via Vugola; submission to platforms via API
- **Unit economics (claims):** Clippers paid roughly 10 cents, 30 cents or a dollar per thousand views
- **Tools:** Vugola, Content Rewards, Whop, Hermes Agent
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Mostly platform-dependent and works from the UK; check terms about automated accounts and fake-engagement rules.
- **Risks:** Only at idea/talks stage; Platforms may ban automated or bot-run accounts; Payout rules may require human clippers
- **Automation [E]:** acquisition 3/5 (B2B partnership outreach is largely human; the agent supply side could come from platforms.); onboarding 3/5 (API keys and docs could be self-serve.); delivery 4/5 (End-to-end agent workflow is plausible, subject to platform rules on automated posting.); billing 4/5 (Platform payouts and subscription billing are automated.); support 2/5 (Disputes and bans on views or campaigns need humans.)
> "the future of clipping is not going to be like human clippers. It's literally going to be agent clippers clipping for you." — Vadim (~24:41)

## Revenue and metric claims (unverified claims)

- **Made $5,000 in the last 30 days** (revenue, first-hand, claimant: Vadim)
  > "in the last 30 days I made $5,000." — Vadim (~0:00)
- **80% profit margin on Vugola** (margin, first-hand, claimant: Vadim)
  > "85 80% profit margins." — Vadim (~16:26)
- **267 paying users** (customers, first-hand, claimant: Vadim)
  > "right now we have like 267 paying users right now." — Vadim (~19:03)
- **About $900 in one day after adding upsells** (revenue, first-hand, claimant: Vadim)
  > "one day I made a like like 900 bucks just like in one day after I made like the upselling perks and features" — Vadim (~9:21)
- **Agents spend roughly $400-600 per month for coding and agent subscriptions** (cost, first-hand, claimant: Vadim)
  > "all for like 200 bucks a month 400 bucks a month like everything for my own behalf" — Vadim (~29:32)
- **Agent work equals a $50-70K per year human job for one department** (other, second-hand, hypothetical, claimant: Vadim)
  > "this is easily like a 50 60k 70k a year job just for like one department of bugola" — Vadim (~29:24)
- **Claude Max $200 plan allegedly gives about $15,000 of token value** (other, second-hand, claimant: Vadim)
  > "when you buy the $200 a month plan, they're giving you like $15,000 worth of actual credits and tokens" — Vadim (~30:20)
- **Over 10,000 clips generated** (customers, first-hand, claimant: Vadim)
  > "We've generated I think over like 10,000 plus clips" — Vadim (~6:10)
- **Opus Clip raised $50 million** (other, second-hand, claimant: Vadim)
  > "The thing with Opus, they raised $50 million." — Vadim (~23:43)
- **Wasted about $500 of Lovable credits in 4 days** (cost, first-hand, claimant: Vadim)
  > "I spent like $500 of the monthly credits in the span of 4 days." — Vadim (~10:40)

## Tactics and playbook steps

**Replace the free plan with a $9 minimum paid plan** (pricing)
1. Launch with a free plan to gather feedback
2. Notice credit abuse from multiple free accounts and almost no paid conversions
3. Remove the free plan and set a $9/month minimum
4. Use the price as a filter for real users; sales started right after
> "I'm not going to have any free plans I'm going to make like the $9 plan like minimum" — Vadim (~20:14)

**Stack upsells at checkout** (pricing)
1. Offer monthly and yearly plans
2. When a user clicks monthly, show a popup selling a quarterly plan
3. After plan selection, send to a custom checkout page that upsells a one-off pack of extra credits
4. Aim to extract more revenue before typical 1-3 month churn
> "you want to keep upselling them like better better deals maximizing how much revenue you can take" — Vadim (~8:51)

**Agent-driven social listening for early users** (acquisition)
1. Build a marketing agent with keywords tied to the niche
2. Scan Reddit, LinkedIn and X for complaints about competitors
3. Have it list usernames and links to the posts
4. DM those users offering a free trial and collect feedback
5. Check UK PECR rules before copying this for individuals
> "look for users complaining about Opus Clip because even Opus Clip back in the day they had like a 48 hour outage" — Vadim (~18:28)

**Competitor review mining with a browser agent** (product)
1. Test all competitors yourself
2. Have an agent with Chrome DevTools MCP open tabs, screenshot and click through products
3. Read customer reviews for complaints (price, slow processing, duplicate clips)
4. Aim to make your product about 10% better and niche down to smaller creators

**The 'let them cook' autonomy skill** (operations)
1. Give agents the tools and a dummy account logins they need
2. Write a custom skill telling the agent to finish tasks no matter what and self-improve on blockers
3. Only ping the human when the task is done or help is truly needed
4. Ask the agent what MCP servers and API keys it needs to be autonomous
> "you work on it no matter what, you do not bug me at all until you like figure it out" — Vadim (~35:31)

**Reverse prompting and rich context** (product)
1. Tell the agent your goals and ask it to ask you questions back
2. Keep notes on designs you like and screenshot them for the AI
3. Be specific rather than saying 'copy xyz.com'
4. Treat bad AI output as a context problem
> "you want it to ask you questions back" — Vadim (~36:26)

**Set up PostHog event tracking via agent** (product)
1. Create a free PostHog account and get an API key
2. Have the agent embed the code in the app
3. Brainstorm events with the agent: signup, first clip, first download, first post, first caption, cancel
4. Track the whole user journey and conversion from the start

**Niche research with mind mapping** (acquisition)
1. Spend one to two weeks researching a market yourself
2. Understand competitors and where the future is headed
3. Mind-map (e.g. Miro) how ideas connect, e.g. automated leads to agentic leads
4. Become the expert in the niche

## Lessons

- *niche_selection*: Pick one complex, durable software problem and go deep instead of shipping many throwaway apps.
- *validation_testing*: Mine competitor reviews and test their products to find gaps (price, speed, duplicated outputs) and aim to be modestly better in a niche.
- *pricing*: A low paid entry price can validate demand better than a free plan and filters out freeloaders.
- *pricing*: Upsells at checkout (longer plans, credit packs) raise revenue per user given early churn.
- *automation_ai*: Non-technical founders can ship real software with a small stack (Claude Code, Supabase, Vercel, GitHub) if they supply detailed context.
- *automation_ai*: Bad AI output is usually a context and prompting problem; be specific, use screenshots and let the agent ask questions.
- *automation_ai*: Design products to be agent-usable (APIs, skills) since agents may become buyers and users of software.
- *validation_testing*: Set up analytics and funnel tracking early, even if launch speed matters more.
- *mindset_execution*: Persistence through months of failed builds before first revenue (Oct to Feb) was key.
- *finance_unit_economics*: A small agent team can substitute for several salaried roles at a few hundred dollars a month, but subscription token economics may not persist.
- *customer_acquisition*: Build in public on one channel (X) to get first customers before diversifying.

## Warnings and mistakes

- Offering a free plan led to credit abuse via multiple free accounts and almost no paid conversions.
- He did not set up analytics, onboarding or offboarding from the start, so conversion data is missing.
- Lovable was too expensive and produced generic 'AI slop' design; skip it and go straight to Claude Code.
- OpenClaw had poor memory, contradictory behaviour and little visibility into what it was doing.
- Buying Claude through the mobile app costs more (about $250 vs $200) because of Apple's cut; buy on the web.
- Revenue is only one month old and self-reported; churn typically occurs within 1-3 months so durability is unproven.

## Tools mentioned

Claude Code (Vibe coding the whole app; $200/month Max plan (cheaper on web than mobile app, which was ~$250)), Codex (OpenAI) (Backup coding agent when Claude limits run out; $200 plan), Lovable (Initial vibe coding attempt; not recommended; ~$500 credits in 4 days), Supabase (Backend database), Vercel (Hosting), GitHub (Code storage), Gemini API (Transcript and visual video analysis for clip selection; API credits (cost not stated)), Stripe (Payments), PostHog (Product analytics and user-journey events; free plan used), OpenClaw (Initial agent; marketing agent for Reddit/X/LinkedIn scanning), Hermes Agent (Agent framework with built-in memory and 40+ skills; CEO, marketing, growth, coding and support agents), Chrome DevTools MCP (Lets agents open tabs, screenshot and click through sites), Paperclip (Open-source orchestration of agent org (CEO, CMO, CTO agents); open source), Miro (Mind mapping for market research), Telegram (Monitor Hermes agent activity in real time), Opus Clip (Main competitor), Content Rewards (Clipping campaign platform), Whop (Clipping campaign platform for tracking views and payouts)
