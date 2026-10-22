# He Asked AI To Make Money. It Did.

- **Video:** [l0Vqm0ZIySc](https://www.youtube.com/watch?v=l0Vqm0ZIySc) · **Channel:** The Koerner Office · **Uploaded:** 2026-03-20 · **Length:** 30 min · **Transcript:** transcribeyoutube
- **Speakers:** Chris Koerner (host), Robbie (guest) · **Format:** operator_interview
- **Evidence quality:** B — First-hand operator with specific figures (MRR, pre-orders, costs), but the business is only 13 days old, the numbers are unverified, and the intro's profit figure is not reconciled with the stated costs and MRR. Sales are essentially a hype-driven AI novelty with unproven retention. · Promotional conflict: Robbie sells the AI Co-Founder Club and offers Chris a coupon; the host promotes TK Owners and a Go High Level sponsor read.
- **Extraction:** claude-sonnet-5-5 · quotes verified 24/24

## Summary

Chris Koerner interviews Robbie, a non-technical operations employee who gave an OpenClaw AI agent ('Ron') $100 and 90 days to make money, inspired by the 2023 HustleGPT experiment. Ron's first idea (SWOT analysis gigs on Fiverr) failed for lack of visibility, but Ron scraped 200 TikTok comments from people wanting their own Ron. Robbie then launched 'AI Co-Founder Club', hosted containerised OpenClaw agents on rented Contabo servers, took $10 pre-orders and converted them to $29/month memberships. He claims about $8.4k MRR after 13 days with ~$2.6k monthly costs. Key takeaway: document the build publicly, validate with paid pre-orders, and sell to the audience your experiment attracts.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **AI Co-Founder Club (hosted containerised OpenClaw agents)** — Monthly membership giving each member a hosted, sandboxed OpenClaw AI agent plus a Discord community and templates. | saas_software | deep | 3/4/4/5/2 | 4 |
| I2 | **AI employee cohort for business builders** — Planned upsell: a small cohort programme for members who want to turn their agent into a real AI employee for a business. | education_coaching | mention | 4/3/1/5/2 | 5 |
| I3 | **SWOT / market research gigs on Fiverr** — AI agent lists SWOT and market analysis services for small businesses on Fiverr. | b2b_service | moderate | 2/3/4/5/3 | 4 |
| I4 | **TikTok audit service** — AI audits people's TikTok accounts for $9 to stay alive. | content_media | mention | 3/4/4/5/3 | 4 |
| I5 | **TikTok Shop selling (fallback plan)** — Robbie's original side-hustle plan to sell products such as vacuum cleaners on TikTok Shop. | ecommerce_physical | mention | 2/4/1/5/3 | 4 |
| I6 | **Customer-built apps via personal agents (golf tracker)** — A member's agent built a golf shot tracker app with an AI caddy, an example of member use cases. | saas_software | mention | 2/4/4/4/3 | 5 |

### I1. AI Co-Founder Club (hosted containerised OpenClaw agents)

- **Customer:** Non-technical people curious about agentic AI who want their own OpenClaw agent without installing it on their own machine; hobbyists and aspiring AI-employee builders.
- **Problem:** OpenClaw is risky to run on a local machine (deleted emails/repos) and hard to set up for non-technical users.
- **Offer:** A cloud-hosted OpenClaw agent in its own sealed Docker container, working out of the box, reachable via Telegram, Discord or a web UI, with persistent memory, a Discord community and templates.
- **Business model:** Monthly subscription ($29/month founding price) with a $10 refundable-style deposit to hold a spot; token costs absorbed by the operator.
- **Pricing:** Monthly subscription, founding members locked at the launch price; $10 deposit to pre-order. Founding member price, locked forever USD 29 per month; Pre-order deposit USD 10 one-off Plans to cap free tokens, then use a fallback cheaper model or let users bring their own API keys.
- **Acquisition:** organic_social_content: TikTok video about giving the AI $100 and 90 days went over 1M views and gave ~15,000 subscribers; follow-up videos with Ron as a raccoon avatar; no paid ads and no cold outreach. Scraped ~200 'I want a Ron' comments with Apify as demand proof.; existing_audience: Sold to the audience built by the viral experiment video; sign-up page linked in bio with a closing date to create urgency.
- **Delivery:** Four rented bare-metal Contabo servers host Docker containers, one per member; Ron the agent designed the hosting setup. Operator absorbs LLM inference costs and runs the community and support himself, and plans a browser extension for connecting a member's own computer.
- **Unit economics (claims):** MRR about $8,374 after 13 days; 617 pre-orders at $10 in two weeks, 270 converted to members; Servers about $600/month and inference about $2,000/month (about $2,500 COGS); Roughly $6,000/month net profit claimed in the intro
- **Tools:** OpenClaw, Claude (Max subscription), Contabo bare-metal servers, Docker, Stand (pre-order payments), Apify, TikTok, Discord, Telegram
- **Startup cost:** $100 initial budget; servers about $600/month, inference about $2,000/month
- **Time to first revenue:** About two weeks from the viral video to 617 pre-orders; pre-orders were taken before anything was built
- **UK applicability [E]:** 4/5 — Works largely the same in the UK. Needs GDPR and UK consumer-law compliance, VAT on subscriptions, and care with user data in containers. Organic TikTok is not restricted by PECR.
- **Risks:** Inference cost overruns from heavy users (1.3M tokens in 48 hours); Security and liability if agents get access to users' computers or credentials; Dependent on OpenClaw, a roughly 100-day-old project, and on LLM provider terms and pricing; Fad/churn risk after the novelty fades; claims are only 13 days old; Reliance on one viral TikTok and the founder's personal brand
- **Automation [E]:** acquisition 3/5 (Content posting and comment scraping can be agent-assisted, but it depends on a viral personal-brand founder narrative and on-camera presence.); onboarding 4/5 (Containers can be provisioned automatically and agents work out of the box; limited human approval needed.); delivery 4/5 (Hosted infrastructure runs unattended, though capacity, abuse (a user spawned 125 sub-agents) and token caps need monitoring.); billing 5/5 (Subscription payments via a payments platform are fully automated.); support 2/5 (Community management in Discord and safety questions about agent permissions need a human, though an agent can answer common questions.)
> "in two weeks, we had like 617 pre-orders." — Robbie (~13:57)
> "From those 600 people, 270 of them actually join the community." — Robbie (~18:51)
> "Founding members, 29 bucks a month, locked forever. $10 deposit holds your spot." — Robbie (~18:00)

### I3. SWOT / market research gigs on Fiverr

- **Customer:** Small businesses needing basic research or SWOT analysis.
- **Problem:** Businesses lack time or AI skills to produce research.
- **Offer:** SWOT analysis and market research produced by the AI agent, with listing copy written by it.
- **Business model:** Per-gig freelance fees via Fiverr (price not stated).
- **Pricing:** per gig.  not stated
- **Acquisition:** marketplace_platform: Brand new Fiverr account with no reviews and no ads; failed due to no visibility.
- **Delivery:** Agent creates the research; human clicked through the Fiverr account setup buttons.
- **Unit economics (claims):** 
- **Tools:** Fiverr, OpenClaw
- **Startup cost:** not stated
- **Time to first revenue:** Never earned revenue; abandoned quickly
- **UK applicability [E]:** 4/5 — Fiverr works in the UK; UK sellers need self-assessment tax registration rather than a W9, and Fiverr terms on AI-delivered work apply.
- **Risks:** New-account invisibility; Fiverr terms on automated or AI-delivered work; Low-priced competitive gig market
- **Automation [E]:** acquisition 2/5 (Marketplace ranking needs reviews and a seller identity; account creation and tax forms need a human.); onboarding 3/5 (Order requirements handled by agent with checks.); delivery 4/5 (LLM research and SWOT writing is agent-friendly with review.); billing 5/5 (Handled by Fiverr.); support 3/5 (Messaging via agent with oversight.)
> "Ron came up with a proposal to do SWAT analysis and research for small businesses." — Robbie (~6:11)

## Revenue and metric claims (unverified claims)

- **MRR of $8,374 after 13 days open** (mrr, first-hand, claimant: Robbie)
  > "it's 8374 right now." — Robbie (~19:35)
- **617 pre-orders in two weeks at $10 deposit** (customers, first-hand, claimant: Robbie)
  > "in two weeks, we had like 617 pre-orders." — Robbie (~13:57)
- **270 of about 600 depositors joined (about 45%)** (conversion_rate, first-hand, claimant: Robbie)
  > "From those 600 people, 270 of them actually join the community." — Robbie (~18:51)
- **Servers cost about $600/month** (cost, first-hand, claimant: Robbie)
  > "So 600 a month for the servers." — Robbie (~28:41)
- **Inference costs about $2,000/month** (cost, first-hand, claimant: Robbie)
  > "The big cost that we have right now is about two grand a month for inference." — Robbie (~28:43)
- **One viral TikTok got over a million views and about 15,000 subscribers** (traffic, first-hand, claimant: Robbie)
  > "it blew up almost immediately and got over a million views." — Robbie (~3:36)
- **One user burned 1.3M tokens in about 48 hours with 125 sub-agents** (other, first-hand, claimant: Robbie)
  > "They've burned 1.3 million tokens in like 48 hours." — Robbie (~29:07)
- **Intro claim of about $6,000/month net profit and $8,500 monthly revenue** (profit, second-hand, claimant: Chris Koerner)
  > "he's making $8,500 a month in revenue and about $6,000 a month in net profit." — Chris Koerner (~1:24)

## Tactics and playbook steps

**Paid pre-order validation** (sales)
1. Post the idea publicly and gauge interest
2. Require a $10 deposit to pre-order to filter tire-kickers
3. Build only after deposits arrive
4. Convert depositors to monthly members (about 45% converted here)
> "the only way that you could pre-order was if you put down 10 bucks." — Robbie (~14:43)

**Mine comments for demand** (acquisition)
1. Post a video about what you are building
2. Scrape comments with Apify
3. Let the agent summarise recurring requests
4. Build the offer people asked for and announce it to the same audience

**Document the experiment publicly** (acquisition)
1. Do something novel and visible
2. Post the journey on TikTok without worrying about views
3. Rely on interest-based distribution rather than follower count
4. Follow up with launch and sign-up videos with a closing date
> "you can start a fresh Tik Tok account tomorrow and post something and it just hits the people that are into that thing right now." — Robbie (~28:13)

**Containerise agents for safety** (operations)
1. Run each user's agent in a sealed Docker container on rented servers
2. Give it only the credentials the user chooses
3. Add token caps, then a cheaper fallback model or bring-your-own-key option

## Lessons

- *validation_testing*: Charging a small deposit before building filters curious tire-kickers and proves real demand.
- *validation_testing*: Letting the AI experiment lead can reveal a better business than the one you planned; the winning idea came from audience comments, not the agent's first gig.
- *customer_acquisition*: Build in public: document what you are doing and post it, since small targeted audiences convert better than large untargeted ones.
- *niche_selection*: Do not assume other business owners and consumers use AI as much as you do; it opens opportunities for AI-enabled services.
- *mindset_execution*: Being early on new infrastructure (agentic AI) gives a large advantage over the mainstream.
- *finance_unit_economics*: Variable AI inference costs can erode subscription margins, so plan caps and fallback models from the start.
- *automation_ai*: Non-technical founders can use the AI itself to research hosting and architecture, but should keep human oversight on security.
- *customer_acquisition*: Interest-based algorithms mean follower count matters less, so a new account can still reach a niche.

## Warnings and mistakes

- Running OpenClaw on a local machine is risky; agents have deleted mailboxes and a whole GitHub repo.
- Heavy users can blow up token costs, so caps or bring-your-own-key options are needed.
- A brand new marketplace account with no reviews or ads gets no visibility, which killed the Fiverr attempt.
- Giving agents sensitive data such as tax IDs or credentials carries security implications; roll out computer access slowly.

## Tools mentioned

OpenClaw (Autonomous AI agent framework that controls a computer), Claude Max (LLM subscription behind the agent; $200/month), Contabo (Bare-metal server hosting; about $150/month each, four servers), Docker (Containerising each user's agent), Apify (Scraping TikTok comments), Stand (Collecting pre-order payments from TikTok), Fiverr (Freelance marketplace for the failed SWOT gig), TikTok (Main marketing channel), Discord (Community and agent interface), Telegram (Agent interface), Go High Level (Sponsor: AI receptionist and white-label platform; 30-day free trial)
