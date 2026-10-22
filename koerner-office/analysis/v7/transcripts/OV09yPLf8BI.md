# How I Built This $160K/Month Gym App

- **Video:** [OV09yPLf8BI](https://www.youtube.com/watch?v=OV09yPLf8BI) · **Channel:** Starter Story · **Uploaded:** 2026-09-09 · **Length:** 17 min · **Transcript:** local_whisper_tiny
- **Speakers:** Pat Walls (host), Gus (co-host), Mauro (guest) · **Format:** operator_interview
- **Evidence quality:** A — First-hand operator showing revenue dashboard and experiment database with specific numbers; Whisper tiny transcript garbles names. Starter Story promotes its own app database. · Promotional conflict: Starter Story plugs its free iOS app idea database.
- **Extraction:** grokbot · quotes verified 25/25

## Summary

Starter Story's Pat Walls interviews Mauro, a 22-23-year-old founder of Symmetry, a gym tracking app localised for Spain and Mexico that reports about $160k monthly revenue and about $3 million total after one year. Growth came from UGC rather than their YouTube audience or influencers: nearly 80,000 videos across 500+ accounts, almost a billion views, with nearly half of revenue paid to creators. The core of the interview is his product method: set ambitious quarterly OKRs, instrument every onboarding screen, use interviews for the 'why', start from problems, and A/B test everything for at least two weeks with guardrail metrics. A single commitment screen added 3% retention while redesigns of the home screen moved nothing. Key takeaway: localise into an underserved market and let experiments, not instinct, decide what to build.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Localised gym tracking app for the Spanish-speaking market (Symmetry)** — A gym workout tracker with ranks, streaks and a social feed, localised for Spain and Mexico, grown with UGC to about $160k a month in one year. | saas_software | deep | 3/5/5/5/3 | 5 |

### I1. Localised gym tracking app for the Spanish-speaking market (Symmetry)

- **Customer:** Gym-goers in Spanish-speaking markets (mainly Spain and Mexico), including beginners
- **Problem:** Tracking workouts, weights and reps; staying motivated to train
- **Offer:** Workout plans, set/rep/weight tracking, exercise videos, per-muscle and per-exercise ranks, streaks, social feed of friends' workouts
- **Business model:** Consumer app subscriptions via App Store and Google Play paywall
- **Pricing:** Subscription behind a paywall (prices not stated).  Paywall is A/B tested with Superwall; about half of revenue goes to UGC creators.
- **Acquisition:** organic_social_content: UGC network: nearly 80,000 short videos in a year across 500+ accounts, nearly a billion views; formats segmented and tracked (e.g. iPhone lock-screen notification format; one video hit 17 million views). Creators paid nearly half of revenue.; existing_audience: Founders' prior fitness YouTube channel gave a small launch spike but was not a scalable channel.; affiliates_influencers: Influencer marketing was tried and did not work.; app_store: Distributed on iOS and Android app stores.
- **Delivery:** Small founding team (former fitness YouTubers) builds and iterates the app using quarterly OKRs, event analytics, user interviews and A/B tests of at least two weeks.
- **Unit economics (claims):** About $160k monthly revenue; About $3 million total revenue across iOS and Android; Nearly half of revenue paid to creators; One onboarding commitment screen increased retention by 3%
- **Tools:** RevenueCat, PostHog, Superwall, Claude with MCPs, Wispr Flow, Notion, Slack
- **Startup cost:** not stated
- **Time to first revenue:** Launched about a year ago; company started two years ago
- **UK applicability [E]:** 5/5 — Consumer fitness apps work the same in the UK; localisation to an underserved language/region is the key lesson. UK GDPR applies to health/fitness data; mass multi-account posting may breach platform rules.
- **Risks:** Very saturated fitness app market; UGC economics depend on revenue per download; paying ~50% of revenue to creators squeezes margin; Running 500+ social accounts risks platform bans; Seasonal demand (January spike)
- **Automation [E]:** acquisition 3/5 (UGC video production and posting can be heavily templated and partly AI-assisted, but they rely on 500+ accounts run with paid human creators.); onboarding 5/5 (Self-serve app onboarding.); delivery 5/5 (Software app; content and features maintained by the team.); billing 5/5 (App store subscriptions.); support 3/5 (In-app and community support; some human input.)
> "You can see we're currently at around 160k monthly revenue, and we currently have around $3 million, both across IS and Android" — Mauro (~1:43)
> "basically we give nearly half of the revenue to the creators" — Mauro (~4:23)
> "It's increased 3% retention, adding one screen. That is why you have to A/B test everything" — Mauro (~12:25)

## Revenue and metric claims (unverified claims)

- **Symmetry makes about $160k in monthly revenue** (mrr, first-hand, claimant: Mauro)
  > "You can see we're currently at around 160k monthly revenue" — Mauro (~1:43)
- **About $3 million total revenue across iOS and Android** (revenue, first-hand, claimant: Mauro)
  > "we currently have around $3 million, both across IS and Android" — Mauro (~1:47)
- **Barely 30k downloads early on** (customers, first-hand, claimant: Mauro)
  > "we barely were at around 30k downloads" — Mauro (~3:07)
- **Nearly 80,000 videos posted across 500+ accounts in a year** (other, first-hand, claimant: Mauro)
  > "In the last year we have posted nearly 80,000 videos. We have more than 500 accounts" — Mauro (~3:47)
- **Nearly a billion views in the last year** (traffic, first-hand, claimant: Mauro)
  > "we have done nearly a billion views in the last year" — Mauro (~3:51)
- **One viral video reached 17 million views** (traffic, first-hand, claimant: Mauro)
  > "And this video went extremely viral. You can see 17 million views" — Mauro (~4:16)
- **Nearly half of revenue paid to creators** (cost, first-hand, claimant: Mauro)
  > "basically we give nearly half of the revenue to the creators" — Mauro (~4:23)
- **A single commitment screen increased retention by 3%** (conversion_rate, first-hand, claimant: Mauro)
  > "It's increased 3% retention, adding one screen" — Mauro (~12:25)
- **Typical apps reach $30-50k a month in a year, per Pat** (mrr, second-hand, claimant: Pat Walls)
  > "usually you'll see, you know, maybe get to 30 or 50K within a year" — Pat Walls (~4:59)
- **Dark/light theme might affect only about 2% of daily active users** (other, second-hand, hypothetical, claimant: Mauro)
  > "Let's say you build a dark theme or a light theme, this may affect like 2% of your daily active users" — Mauro (~5:50)

## Tactics and playbook steps

**UGC format factory** (acquisition)
1. Run hundreds of social accounts posting short videos
2. Segment every video into formats and sub-formats and track performance
3. Double down on winners, e.g. fake iPhone lock-screen notifications ending with an app notification to go to the gym
4. Pay creators a large revenue share (about half) so they keep producing long term
5. Use average revenue per download (varies by country) to set what you can pay creators
> "we segment the videos into formats" — Mauro (~3:56)

**Experiment policy for product decisions** (product)
1. Set ambitious quarterly OKRs (more ambitious when the app is new) and review metrics weekly or daily
2. Find high-leverage screens (paywall, onboarding, search) instead of cosmetic features
3. Track every onboarding screen with analytics for the 'what'
4. Interview users and read Discord/Reddit for the 'why'
5. Start from a validated problem, write hypotheses with expected metric impact and guardrail metrics
6. A/B test against control for at least two weeks, then analyse; log all tests in a database
> "after at least two weeks of running the experiment, you then analyze the data" — Mauro (~11:26)

**Pick the right activation metric** (product)
1. Define activation for your product (for a gym app: going to the gym and tracking a workout)
2. Treat activation as the lead indicator for retention
3. Track first-week and 30-day retention and revenue per download
> "if you move activation for attention, follows" — Mauro (~7:59)

## Lessons

- *niche_selection*: Localising a proven app category for an underserved language market can win even in a saturated category.
- *offer_design*: Focus on high-leverage screens like the paywall, onboarding and search; cosmetic features affect few users.
- *validation_testing*: Use analytics for where users drop off and conversations for why.
- *validation_testing*: Come from the problem space, not the solution space, before designing experiments.
- *finance_unit_economics*: Revenue per download decides how much you can pay for acquisition, and it varies a lot by country.
- *customer_acquisition*: Paying creators generously keeps them producing content long term.
- *mindset_execution*: Most changes do not move metrics; knowing this pushes you to focus more on marketing than product.
- *mindset_execution*: Play long-term games with long-term people; the company started a year before launch and they were bad at first.

## Warnings and mistakes

- Building what you want, or literally what users request, gives terrible to mediocre results.
- The most common mistake is having no analytics events at all, so you cannot see where users drop off.
- An existing YouTube audience and influencer marketing did not produce scalable growth.
- Most tests move nothing; completely different redesigns of the home screen had zero metric impact.

## Tools mentioned

RevenueCat (Revenue dashboard for app subscriptions), PostHog (transcribed 'possible'/'postdoc') (Product analytics and A/B testing), Superwall (Paywall A/B testing), Claude with MCPs (Querying analytics data via MCP connections), Wispr Flow (transcribed 'whisper flow') (Voice dictation for faster input), Notion (Documentation and experiment tracking), Slack (Team communication), Starter Story iOS app database (Sponsor-style plug: free database of app ideas)
