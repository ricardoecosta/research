# Make Money With This New AI Agent That Works 24/7

- **Video:** [gmwDBNcFXFU](https://www.youtube.com/watch?v=gmwDBNcFXFU) · **Channel:** The Koerner Office · **Uploaded:** unknown · **Length:** 11 min · **Transcript:** cached
- **Speakers:** Chris Koerner (host), Billy (other) · **Format:** tutorial_howto
- **Evidence quality:** C — A first-hand live demo of building a product, but there are no sales, revenue or customer evidence, and the build is a single novelty test. The app is useful as a proof of agent capability only; the commercial case is speculation. · Promotional conflict: Promotes his Playmakers.ai paid community; says the video is not sponsored by Grok Bot.
- **Extraction:** claude-sonnet-5-5 · quotes verified 18/18

## Summary

Chris Koerner tries the agentic AI tool he calls 'Grok Bot' for the first time and uses it to build a 'Morning Lock' product: a Mac menu bar app plus Chrome extension that locks Gmail and the Mail app outside set hours (e.g. 5-10am), with an accountability password held by a spouse. He had Claude write the prompt, then Grok Bot built, tested and fixed the app via Replit, GitHub and Stripe in about 31 minutes of recording. He says he plans to sell it as a SaaS in a part two, but no sales or revenue are shown. The takeaway is that agentic AI can produce a working, personally useful software product from one detailed prompt; whether it sells is untested.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Morning Lock: email/website time-lock app (Mac app + Chrome extension) sold as SaaS** — A productivity app that blocks Gmail, the Mac Mail app and chosen distracting sites outside set hours, with an accountability password held by a spouse or friend. | saas_software | deep | 2/4/4/5/3 | 5 |
| I2 | **AI-agent-built software products as a repeatable approach** — Use an agentic AI such as Grok Bot to build, test and fix software end to end from a single prompt, then sell the products. | ai_automation | mention | 2/3/4/4/2 | 5 |
| I3 | **Agent finishes the 90%-complete projects in Replit** — Idea floated of having Grok Bot go into his Replit account and finish all unfinished projects. | ai_automation | mention | 0/0/3/0/0 | 5 |

### I1. Morning Lock: email/website time-lock app (Mac app + Chrome extension) sold as SaaS

- **Customer:** Knowledge workers and people who struggle with inbox management or distraction and want forced time-boxing
- **Problem:** Calendar time-boxing is hard to stick to because nobody else is accountable; people get distracted and fall behind on email.
- **Offer:** Mac menu bar app plus Chrome extension that locks Gmail/Mail (and other chosen apps and sites) outside defined windows, lets users block most-visited sites, and sends the unlock password to a spouse or loved one.
- **Business model:** SaaS subscription sold via a website with Stripe payments (planned, not yet launched)
- **Pricing:** SaaS subscription planned; no price stated.  Selling is deferred to 'part two'; no pricing discussed.
- **Acquisition:** existing_audience: Implied: Koerner would sell to his YouTube audience; he says selling will be covered in part two. No channel plan is given.
- **Delivery:** Software built by the AI agent (Grok Bot) driving Replit and GitHub. Chrome extension and Mac app are downloaded and installed by the user. Human steps needed: Apple developer account and Chrome Web Store developer account (about 20 minutes, per Claude).
- **Unit economics (claims):** Build took about 31 minutes 37 seconds of recording time; Grok Bot was authorised to approve Replit overages up to $100 per day
- **Tools:** Grok Bot, Claude, Replit, GitHub, Stripe, Resend, Arc / Chrome, Mac Mail
- **Startup cost:** Not stated beyond Replit usage, capped at $100 per day in the prompt; Apple and Chrome developer account fees not stated
- **Time to first revenue:** not stated (no sales yet)
- **UK applicability [E]:** 5/5 — Software product with no US-specific dependency. UK needs normal VAT, GDPR and app-store compliance. Chrome extension and Mac app distribution works the same.
- **Risks:** Unvalidated demand: no customers or sales yet; Crowded market of website and app blockers; Mac and Chrome updates may break the blocking; Password-unlock design may be easy to bypass, and the extension reads browsing history, raising privacy and GDPR concerns; Agent-built code is untested at scale and may have security bugs; App-store review and developer account friction
- **Automation [E]:** acquisition 2/5 (Nothing is planned yet. Realistically SEO, content and app-store listings could be agent-driven, but this is unproven in the video.); onboarding 4/5 (Self-serve download and install, with Stripe checkout and a password setup flow; a browser extension install and Mac permissions need some user effort.); delivery 4/5 (The product is software; the agent built and tested it. Distribution through the Apple and Chrome stores needs one-off human account setup and review handling.); billing 5/5 (Stripe subscriptions run unattended once configured.); support 3/5 (Bugs and OS or browser updates will need agent triage with human oversight; an LLM support bot can handle routine questions.)
> "My idea is to lock me out of my inbox for the majority of the day, so I have to get caught up on my emails in a specific time frame." — Chris Koerner (~2:19)
> "We have a sellable product here. It's done." — Chris Koerner (~9:06)
> "I can even send my password to a spouse, a loved one, whatever, so they have to be the one to unlock it for me." — Chris Koerner (~9:50)

## Revenue and metric claims (unverified claims)

- **Recording of the build took 31 minutes 37 seconds** (hours, first-hand, claimant: Chris Koerner)
  > "it's only been recording for 31 minutes and 37 seconds. And it's done." — Chris Koerner (~7:45)
- **Agent ran 23 tests, all passing** (other, first-hand, claimant: Chris Koerner)
  > "it just tested 23 different things and all of them were green" — Chris Koerner (~7:12)
- **Grok Bot allowed to approve Replit charges up to $100 per day** (cost, first-hand, claimant: Chris Koerner)
  > "approve any and all Replit overages and charges without my approval not exceeding $100 a day" — Chris Koerner (~5:55)
- **Playmakers members find customers paying hundreds to tens of thousands of dollars per month (promotional)** (revenue, second-hand, claimant: Chris Koerner)
  > "We are finding paying customers paying hundreds or thousands or sometimes tens of thousands of dollars per month." — Chris Koerner (~8:49)

## Tactics and playbook steps

**Have Claude write the agent prompt** (product)
1. Describe the product, constraints and goal to Claude in plain English
2. Ask for a 'Grok Bot friendly' prompt using the technical terms you don't know
3. Include build-test-fix loops, a spend cap and a request that the agent asks for the credentials it needs
4. Paste the prompt into the agent and walk away
> "Write a beautiful prompt that is Grokbot friendly using all the technical coding terms I know nothing about" — Chris Koerner (~5:44)

**Manage the agent like an employee** (operations)
1. Give the agent a job and focus rather than micromanaging step by step
2. Connect only the integrations it needs (here Stripe test mode, GitHub, Replit)
3. Cap spend in the prompt
> "A good boss says, "This is your job. Just do this. Just focus on this."" — Chris Koerner (~4:37)

**Iterate with short follow-up prompts** (product)
1. Use the working v1
2. Add features with one-line prompts, e.g. list most-used sites and apps for easy blocking
3. Report bugs briefly (e.g. 'the icon doesn't work') and let the agent fix them

## Lessons

- *validation_testing*: Build tools to solve your own problem first; a product you actually use is the best early validation and a source of content.
- *automation_ai*: Use a stronger model to critique the plan before handing it to an agent; Claude caught that Replit web apps cannot lock a Mac mail app.
- *mindset_execution*: Accountability works better with a third party or money at stake than with a self-made calendar block.
- *automation_ai*: Agent autonomy needs guardrails: spend caps, test mode for payments and limited integrations.
- *customer_acquisition*: Building is now cheap, so the bottleneck shifts to distribution; he defers selling to a part two, and demand is unproven.
- *validation_testing*: Test the habit or demand cheaply before building (Claude suggested testing the habit first for $0).

## Warnings and mistakes

- Some steps cannot be done by an agent: creating the Apple developer account and Chrome Web Store developer account, and a website alone cannot force-quit a Mac app, so a native Mac app plus extension is needed.
- Don't connect the agent to everything; limit its access to what it needs.

## Tools mentioned

Grok Bot (Agentic AI that builds and tests software by driving other tools), Claude (Writing the prompt and sanity-checking feasibility), Replit (Build environment used by the agent; Spend capped at $100 per day in the prompt), GitHub (Code storage), Stripe (Payments for the planned SaaS (test mode)), Resend (Email sending integration authorised during setup), Playmakers.ai (Koerner's paid AI consulting community (promotion))
