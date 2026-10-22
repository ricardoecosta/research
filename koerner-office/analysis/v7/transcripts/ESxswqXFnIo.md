# I Helped a Subscriber to Build an App in 24 Hours

- **Video:** [ESxswqXFnIo](https://www.youtube.com/watch?v=ESxswqXFnIo) · **Channel:** Mikey No Code · **Uploaded:** 2026-10-20 · **Length:** 28 min · **Transcript:** cached
- **Speakers:** Mikey (host), Priya (other) · **Format:** tutorial_howto
- **Evidence quality:** C — First-hand build walkthrough but no revenue or business numbers; promotional for Base44 and the creator's course. · Promotional conflict: Promotes his Base44 Masterclass ($499 list) and Base44 itself.
- **Extraction:** grokbot · quotes verified 19/19

## Summary

Mikey No Code documents building a custom client-tracking app in Base44 for Priya, a one-person interior styling business (Willow Lane Interiors, Manchester), within 24 hours of her community post. The video focuses on scoping: workflow interviews, a one-sentence goal, prioritising four version-one features and parking five, then a single complete build prompt with a visual direction and avoid list. Feedback was routed via AI-generated client questions and screenshots in discussion mode, and real-day use exposed a missing required follow-up date. Key takeaway: with AI builders, deciding what not to build is the hard part.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Custom micro-CRM apps for solo service businesses built with Base44** — Interview a small business owner about their workflow and build a tailored lightweight client tracker with an AI app builder in under 24 hours. | saas_software | deep | 2/2/4/5/3 | 5 |
| I2 | **Base44 masterclass / AI app-building course** — Course teaching people to build SaaS apps, websites, agents and mobile apps with Base44. | education_coaching | mention | 5/5/5/5/3 | 5 |

### I1. Custom micro-CRM apps for solo service businesses built with Base44

- **Customer:** Solo service businesses such as a one-person interior styling firm in Manchester
- **Problem:** Leads scattered across WhatsApp, notebooks and spreadsheets; lost jobs from missed follow-ups; off-the-shelf CRMs force a new process
- **Offer:** Version-one app with client records, a stage board matching the owner's own pipeline, quote values and follow-up dates with a 'needs chasing' list, and a dated activity log
- **Business model:** not stated (built free for a community member; implied as a service or DIY)
- **Pricing:** not stated.  Base44 hosts the app on a free yourapp.base44.app URL; custom domain costs extra.
- **Acquisition:** existing_audience: Request came from a member post in the creator's Skool community.
- **Delivery:** Builder runs a discovery DM, writes one complete Base44 prompt, publishes, routes Base44's clarifying questions to the client, applies screenshotted feedback in discussion mode, removes test data, renames the URL and runs a security scan.
- **Unit economics (claims):** Idea to live URL within 24 hours
- **Tools:** Base44, WhatsApp, Skool
- **Startup cost:** Base44 subscription (cost not stated)
- **Time to first revenue:** Same day
- **UK applicability [E]:** 5/5 — Example client is in Manchester with pounds pricing; works the same in the UK.
- **Risks:** Low barrier lets clients DIY or use cheap CRMs; Hidden requirements only surface in real use; Platform lock-in to Base44
- **Automation [E]:** acquisition 2/5 (Community/inbound requests; selling to UK sole traders by cold DM or SMS would breach PECR.); onboarding 2/5 (Discovery interview is human-led, though question generation can be AI-assisted.); delivery 4/5 (AI builder generates and revises the app from one prompt plus client screenshots.); billing 5/5 (Subscription billing software.); support 3/5 (Client can self-serve changes by prompting; builder handles edge cases.)
> "Coding is rarely the part that kills these projects anymore" — Mikey (~3:21)
> "when building gets this fast, deciding what not to build becomes the hardest part of the whole job" — Mikey (~1:44)

## Revenue and metric claims (unverified claims)

- **Masterclass list price $499 offered free** (price, first-hand, claimant: Mikey)
  > "My masterclass normally costs $499 to join" — Mikey (~2:17)
- **Sample client quote values between £600 and £9,000** (price, second-hand, claimant: Mikey)
  > "quote values between 600 and 9,000 pounds" — Mikey (~14:48)
- **Renaming the Base44 URL takes about 30 seconds** (hours, first-hand, claimant: Mikey)
  > "It only took about 30 seconds, but it makes a surprisingly big difference to the handoff" — Mikey (~26:15)
- **£8,000 vs £800 in 'quote sent' means very different months, so show stage value not counts** (other, second-hand, claimant: Mikey)
  > "£8,000 sitting in quote sent means something completely different for her month than £800" — Mikey (~22:42)

## Tactics and playbook steps

**Workflow-first discovery instead of feature lists** (product)
1. Ask the owner to walk through the business from first inquiry to finished job, including annoying parts
2. Ask who will use the app and the one recent problem they wish hadn't happened
3. Have them finish one sentence: what the app should keep in one place and why
4. Use that sentence as the rule: features that serve it stay, others are parked
> "rather than asking her what features she wanted, we started somewhere much more useful" — Mikey (~4:46)

**Monday-morning prioritisation** (product)
1. Ask which feature they'd miss first if it wasn't there on Monday morning
2. Order version one by the answers
3. Park features with a reason (invoicing, auto emails, client portal, calendar sync, multiple logins)
> "We asked her which thing she would miss first if she opened up the app on Monday morning and they weren't there" — Mikey (~7:37)

**One complete build prompt with an avoid list** (product)
1. Describe business, single user, the core question the app answers
2. Specify fields, pipeline stages, money and follow-up logic and the only screens allowed
3. Give a concrete visual direction and an explicit avoid list (no purple/blue gradients, dark mode, glassy cards, stock illustrations)
4. Ask for 12 realistic sample clients across all stages
> "describing what you do not want is one of the most reliable ways to stop an AI-generated app from falling back into the same default look" — Mikey (~11:02)

**Let the AI generate client questions** (operations)
1. After the first build, ask Base44 to list the 3-4 decisions it had to guess
2. Turn them into plain-language questions for the client
3. Screenshot client replies and paste into Base44 discussion mode
4. Agree the plan before applying changes
> "identify the three or four decisions it had been forced to guess at" — Mikey (~16:35)

**Polished handoff** (operations)
1. Remove test data
2. Rename the app URL to the business name
3. Confirm it works on the client's phone
4. Run the security scan before handing over
> "A random URL still feels like something you're testing" — Mikey (~26:21)

## Lessons

- *validation_testing*: Understand the workflow before talking software; the first ask is usually a symptom.
- *offer_design*: Fit the app to the client's existing process so they keep using it; off-the-shelf CRMs force change and get abandoned.
- *automation_ai*: Scope is the bottleneck when AI makes building fast.
- *validation_testing*: Real-day usage finds bugs a demo click-through never will.
- *offer_design*: Show money values, not counts, on pipeline views for small businesses.
- *offer_design*: Small handoff touches (branded URL) make a build feel like a real product.
- *automation_ai*: Use AI builders' discussion/plan mode before changes to avoid unrequested redesigns.

## Warnings and mistakes

- Building the final version on day one causes overwhelm and abandoned projects.
- The requested feature is often a symptom: a reminders tool would have become a fourth place to check.
- Unstated requirements (e.g. making follow-up date compulsory) only surface in real use.
- Adding features one prompt at a time makes AI builders guess at structure.
- Renaming a Base44 URL kills the old address immediately.

## Tools mentioned

Base44 (AI no-code app builder with hosting and discussion mode), Skool (Community where the request came in), WhatsApp (Client's previous lead tracking), Base44 Masterclass (Creator's course (promotion); $499 list, offered free)
