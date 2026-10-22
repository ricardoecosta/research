# Stop Guessing. Here’s How to Build What People Will Actually Pay For

- **Video:** [IHy07Ny72kA](https://www.youtube.com/watch?v=IHy07Ny72kA) · **Channel:** The Koerner Office · **Uploaded:** 2025-12-21 · **Length:** 13 min · **Transcript:** ok
- **Speakers:** Chris Koerner (host) · **Format:** tutorial_howto
- **Evidence quality:** C — A live demo of a validation and build workflow, not a running business: no sales, customers or revenue; poll is from paid US panelists; the product is a prototype with unproven quality. Process details (times, tools, poll results) are first-hand and consistent. · Promotional conflict: Mocha is a 'friend of the pod' with a link in the description; host denies PickFu sponsorship but recommends it.
- **Extraction:** claude-sonnet-5-5 · quotes verified 25/25

## Summary

Chris Koerner demonstrates a 'validate before you build' workflow: he polls 100 US small business owners via PickFu on which website feature they'd pay for, then uses the Mocha vibe-coding app to build an appointment booking widget (BookFlow) in under 20 minutes. Appointment booking tied with chatbot for first place; ChatGPT analysis of the written responses suggests bundling booking, forms, price calculator and a chatbot layer, leading with scheduling in ads. Key takeaway: poll your target buyer first, mine the free-text answers with an LLM, then prototype quickly with AI and sell before fully building. Mocha is described as a 'friend of the pod' (promotional link).

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Embeddable appointment booking widget (BookFlow), niche-rebrandable** — A white-label booking widget for small business websites, vibe-coded with Mocha and sold into specific verticals such as dog groomers. | saas_software | deep | 4/4/4/5/3 | 5 |
| I2 | **Multi-module 'super widget' (booking + forms + price calculator + chatbot)** — A bundle of website modules sold as 'the last widget your business ever needs', with a chatbot layer to make the offer feel premium. | saas_software | moderate | 4/4/4/5/3 | 5 |
| I3 | **Audience-poll validation service/workflow via PickFu** — Using PickFu to poll a targeted audience on what they'd pay for before building. | other | moderate | 0/0/4/0/0 | 5 |

### I1. Embeddable appointment booking widget (BookFlow), niche-rebrandable

- **Customer:** Small business owners with websites (dog groomers, tree trimmers, home service businesses, tarot readers, etc.)
- **Problem:** Businesses need clients to see their calendar and book appointments without messy email back-and-forth.
- **Offer:** An embeddable widget where visitors pick a service, date and time and enter their details; branding, colours and name are easy to swap per industry.
- **Business model:** Software sold to small businesses (pricing not stated; implied subscription/widget licence)
- **Pricing:** not stated.  No price for the widget is given; only the demo's dog-grooming service prices (45, 75, 15 dollars) which are example content, not product pricing.
- **Acquisition:** paid_social: Suggests running ads to a specific industry, with the top-of-funnel ad pitching scheduling and the other modules shown once they are inside.
- **Delivery:** Software built by Mocha from prompts; multi-tenant app hosted at bookflow.mocha.app with custom domain option. Swapping to a new niche reportedly takes one prompt.
- **Unit economics (claims):** Build took about 5 minutes for first version and about 18-20 minutes for the full site and demo; Agency build quoted at 10,000 USD in the US or 5,000 USD overseas, taking weeks
- **Tools:** Mocha, ChatGPT, PickFu
- **Startup cost:** Mocha 20 USD per month plus PickFu poll cost (hundreds of dollars, exact not stated)
- **Time to first revenue:** not stated (no sales made in the video)
- **UK applicability [E]:** 5/5 — Software works the same in the UK; need GDPR/UK data handling for bookings and PECR compliance for outbound. Competes with Calendly and similar tools.
- **Risks:** Crowded market with established free/cheap booking tools; Vibe-coded app quality, security and reliability are unproven; Demo only; no customers or willingness-to-pay validated beyond a poll; Poll answers are stated preference, not purchase behaviour
- **Automation [E]:** acquisition 4/5 (Paid ads to a niche landing page are inbound and can be run and optimised largely by agents with occasional human approval.); onboarding 4/5 (Self-serve signup and widget embed code can be fully software-driven; per-niche rebranding is a prompt.); delivery 4/5 (The widget is software running unattended once built; fixes and new niches are done via prompts.); billing 5/5 (Standard subscription billing (e.g. Stripe) is unattended.); support 3/5 (AI support can answer most install and config questions, but bugs in vibe-coded software need human review.)
> "I want to build a widget that small businesses can easily add to their websites that will enable potential customers to book an appointment with them." — Chris Koerner (~4:45)
> "Just make one really good appointment booking widget for dog groomers and nothing else." — Chris Koerner (~11:15)

### I2. Multi-module 'super widget' (booking + forms + price calculator + chatbot)

- **Customer:** Small business owners wanting a website feature set
- **Problem:** Businesses need scheduling, structured lead capture and quoting on their sites.
- **Offer:** Appointment booking, contact form intake, price calculator builder and a simple chatbot answering from the site's pages; forms bundled free-feeling inside the main product.
- **Business model:** Bundled software sold to small businesses; pricing not stated
- **Pricing:** not stated.  ChatGPT analysis suggests the chatbot signals higher value and willingness to pay a lot.
- **Acquisition:** paid_social: Lead ads with scheduling pain point, then upsell other modules once inside.
- **Delivery:** Built by Mocha via phased prompts; the host then scaled back to booking only.
- **Unit economics (claims):** 
- **Tools:** Mocha, ChatGPT
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 5/5 — Same in the UK; chatbot must handle UK GDPR and disclose AI use.
- **Risks:** Chatbot opinion is split (half find them annoying); Scope creep; host himself scaled back to a single widget; Analysis relies on LLM interpretation of 100 responses
- **Automation [E]:** acquisition 4/5 (Ads and landing pages can be agent-run.); onboarding 4/5 (Self-serve setup flows.); delivery 4/5 (Software product; chatbot requires ongoing model costs but runs unattended.); billing 5/5 (Subscription billing is automatic.); support 3/5 (Chatbot-related complaints and edge cases need some human checks.)
> "You're basically selling the last widget your business ever needs." — Chris Koerner (~10:28)

### I3. Audience-poll validation service/workflow via PickFu

- **Customer:** Founders validating ideas
- **Problem:** Founders build things nobody will pay for.
- **Offer:** Pay PickFu to poll 100 targeted respondents with written explanations.
- **Business model:** Not a business sold in the video; a validation method costing the founder money
- **Pricing:** pay per poll, per audience trait and per option.  Host says it costs hundreds of dollars for 100 respondents with targeting and five options; exact price not given.
- **Acquisition:** 
- **Delivery:** PickFu panel returned 27 responses in a short time and 100 later (same day).
- **Unit economics (claims):** PickFu poll costs hundreds of dollars
- **Tools:** PickFu, ChatGPT
- **Startup cost:** hundreds of dollars per poll
- **Time to first revenue:** not applicable
- **UK applicability [E]:** 5/5 — PickFu supports other audiences; UK business-owner panels may be smaller or pricier.
- **Risks:** Respondents are paid panelists, so stated willingness to pay may be inflated; Cost can add up with targeting and multiple options
- **Automation [E]:** acquisition 0/5 (Not a customer-facing business.); onboarding 0/5 (Not applicable.); delivery 4/5 (Poll set-up and LLM analysis can be scripted; platform does the respondent work.); billing 0/5 (Not applicable.); support 0/5 (Not applicable.)
> "What one website feature does your business need the most right now that you would be willing to pay for?" — Chris Koerner (~1:20)

## Revenue and metric claims (unverified claims)

- **Agency would charge at least 10,000 USD in the US to build something like this** (cost, second-hand, hypothetical, claimant: Chris Koerner)
  > "If you hire them here in the States, it's going to cost you at least $10,000." — Chris Koerner (~12:41)
- **Overseas dev team would cost at least 5,000 USD** (cost, second-hand, hypothetical, claimant: Chris Koerner)
  > "Overseas, like the Philippines or Ukraine, at least $5,000." — Chris Koerner (~12:45)
- **Mocha subscription costs 20 USD per month** (cost, first-hand, claimant: Chris Koerner)
  > "I'm paying for the $20 a month account, and I'm going to click create new app." — Chris Koerner (~4:40)
- **Poll results after 27 responses: 11 appointment booking, 2 contact forms, 6 testimonials, 6 chatbot, 2 pricing calculator** (conversion_rate, first-hand, claimant: Chris Koerner)
  > "we have 11 votes for appointment booking, two for contact forms, six for testimonials, six for chatbot, two for pricing calculator." — Chris Koerner (~3:05)
- **First build took 4 minutes 47 seconds, 12 changes, 10 files** (hours, first-hand, claimant: Chris Koerner)
  > "it took 4 minutes and 47 seconds to make 12 changes and deliver 10 files." — Chris Koerner (~6:53)
- **Whole expanded build took about 18 minutes** (hours, first-hand, claimant: Chris Koerner)
  > "That's a wrap. It took about 18 minutes flat." — Chris Koerner (~11:20)
- **Final poll: 100 responses, appointment booking tied first with chatbot** (customers, first-hand, claimant: Chris Koerner)
  > "appointment booking was clearly number one, but it ended as tied for first with a chatbot" — Chris Koerner (~7:30)

## Tactics and playbook steps

**Poll your target buyer before building** (product)
1. Pick a platform like PickFu and target e.g. 100 US small business owners
2. Ask 'what one feature does your business need most that you would be willing to pay for?'
3. Offer 5 concrete options and require a written explanation
4. Optionally poll only ~20 people to save money, or ask friends, Twitter, Reddit or Facebook groups for free
> "What one website feature does your business need the most right now that you would be willing to pay for?" — Chris Koerner (~1:20)

**Mine free-text poll answers with an LLM** (product)
1. Paste the written responses and vote totals into ChatGPT
2. Ask 'what can I learn from this that will help me make money?'
3. Look for gaps between what people want and what they'd pay for, and for bundling signals
> "I posted a survey to business owners asking what features they would pay to have on their website." — Chris Koerner (~8:17)

**Ask the AI to rewrite your prompt** (product)
1. Write a rough prompt for the vibe-coding tool
2. Ask ChatGPT to rewrite it better, and to ask you questions if needed
3. Paste the long prompt as an attachment into Mocha
4. Trade-off: longer prompts cost more credits but may need fewer iterations
> "ask it what to ask it" — Chris Koerner (~5:34)

**Lead with the strongest pain point in ads, upsell modules inside** (acquisition)
1. Run top-of-funnel ads pitching scheduling only
2. Once the customer is inside, show other modules (forms, calculator, chatbot)
3. Bundle forms rather than selling them alone
4. Target a single industry per campaign by swapping branding via one prompt
> "the top of the funnel ad should always pitch scheduling." — Chris Koerner (~10:32)

**Sell before you build** (mindset)
1. Poll, prototype in minutes, then pitch the prototype
2. Scale scope back to one niche widget (e.g. dog groomers) for a working demo
3. Clone to other niches with one prompt
> "Poll, build, launch. Sell it before you have it. Ready, fire, aim." — Chris Koerner (~13:04)

## Lessons

- *validation_testing*: Ask the target buyer what they would pay for before building anything, instead of assuming demand.
- *validation_testing*: You can validate without an audience by renting one (PickFu) or using free communities, friends and family.
- *validation_testing*: Free-text reasons in a poll are often more valuable than the vote count, especially when analysed by an LLM for pricing and bundling signals.
- *offer_design*: Bundle commodity features (contact forms) into the main product rather than selling them standalone, since buyers expect them to be free.
- *offer_design*: A feature perceived as hard to build (chatbot) can raise the perceived value of an entire bundle even if few need it.
- *automation_ai*: Vibe-coding collapses prototype time from weeks and thousands of dollars to minutes, so speed to market becomes the advantage.
- *niche_selection*: White-label a single codebase for multiple verticals so one product can be tested across niches cheaply.
- *mindset_execution*: Execution matters more than watching; act on the information.

## Warnings and mistakes

- Being needed is not the same as being willing to pay; sell painkillers not vitamins.
- Stated popularity (votes) can differ from willingness to pay; chatbot ranked high partly because respondents think it is hard and expensive, and nobody will pay for testimonials.
- Don't assume 'build it and they will come'.
- Long AI-generated prompts may cost more credits in vibe-coding tools.

## Tools mentioned

PickFu (Paid audience polling with targeted respondents and written explanations; hundreds of dollars for 100 targeted responses with 5 options (not exact)), Mocha (getmocha.com) (Vibe-coding app that builds and hosts apps from natural-language prompts; 20 USD per month), ChatGPT (Rewriting prompts and analysing poll responses), Twitter / Instagram story / Reddit / Facebook groups (Free alternatives to poll an audience; free)
