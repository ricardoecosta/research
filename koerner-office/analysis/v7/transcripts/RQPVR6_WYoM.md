# Do these 7 Things Immediately When Building Apps with AI

- **Video:** [RQPVR6_WYoM](https://www.youtube.com/watch?v=RQPVR6_WYoM) · **Channel:** Mikey No Code · **Uploaded:** 2026-10-06 · **Length:** 29 min · **Transcript:** cached
- **Speakers:** Mikey No Code (host) · **Format:** tutorial_howto
- **Evidence quality:** C — Generic process tutorial with a demo build; no first-hand business numbers. Useful build hygiene for AI-built SaaS but not a business case. · Promotional conflict: Promotes the creator's own Base44 masterclass ($499 'normally', free via link) twice; Base44 is presented very favourably.
- **Extraction:** grokbot · quotes verified 18/18

## Summary

Tutorial from Mikey No Code on seven habits to adopt immediately when building apps with AI, demonstrated by building a task manager in Base44. The steps are: prototype only the core function first, write structured prompts (what it does, looks like, what users can do, what to leave out), add authentication right after the prototype works, plan the data structure in Base44's discuss mode before adding features, run Base44's free security scan before publishing, test with realistic data across multiple accounts, and make scale-ready structural choices (workspace-based data model, back-end functions). The key takeaway is that most problems blamed on AI builders come from the process around them, and the order of decisions matters. The video repeatedly promotes the creator's Base44 masterclass ($499 'normally', offered free).

## Revenue and metric claims (unverified claims)

- **His masterclass on building SaaS apps, websites, AI agents and mobile apps with AI normally costs $499 but is offered free to viewers** (price, first-hand, claimant: Mikey No Code)
  > "my masterclass here normally costs $499 to join, but since you are watching this video and taking the time to do so, thank you so much, you can join completely free" — Mikey No Code (~1:43)
- **Base44's built-in security scan is free and takes less than a minute** (hours, second-hand, claimant: Mikey No Code)
  > "the scan is free here. It takes less than a minute, and it checks for common vulnerabilities" — Mikey No Code (~18:00)
- **Spending a few extra minutes structuring the first prompt can prevent around 10 follow-up prompts** (other, second-hand, hypothetical, claimant: Mikey No Code)
  > "Spending a few, just a few extra minutes here deciding what the app should do and how it should behave can actually prevent 10 follow-up prompts later" — Mikey No Code (~8:07)
- **Structural weaknesses start causing inconsistent behaviour at around 100 users and become major performance and reliability problems at 10,000 users** (customers, second-hand, hypothetical, claimant: Mikey No Code)
  > "at a hundred users and more, weaknesses in the structure can start causing inconsistent behavior or even unnecessary database activity" — Mikey No Code (~25:24)

## Tactics and playbook steps

**Prototype the single core function first** (product)
1. Identify the one most important user loop (for a task manager: type a task and see it in a list)
2. Prompt only that loop, explicitly excluding extras (no categories, priorities, due dates or auth yet)
3. Specify minimal design (e.g. white background, blue accent)
4. Test the loop manually (enter, add button, display, delete) before adding anything else
> "it means building the single most important function and making sure it works correctly before adding anything around it" — Mikey No Code (~3:06)

**Four-part structured build prompt** (product)
1. State what the app does and the data each item holds (title, priority low/medium/high, due date)
2. State what it should look like (layout, grouping, colours)
3. State what the user can do (checkbox to complete, delete, completed items move to bottom with strikethrough)
4. State what to leave out (no authentication, categories or team features yet)
> "It should explain what the app does, what it should look like, what the user can do, and what should be left out" — Mikey No Code (~6:29)

**Add authentication straight after the prototype works** (product)
1. Once the core loop works, prompt: add sign-up/login, each user sees only their own data, keep existing functionality and design unchanged
2. Create two test accounts, add different tasks in each
3. Switch accounts and confirm data is fully isolated
> "Add user authentication with sign up and login. Each user should only be able to see and manage their own tasks" — Mikey No Code (~9:52)

**Plan the data model in discuss mode before adding features** (product)
1. Open Base44 discuss mode (no code changes)
2. Describe all future features (categories, team assignment, projects) and ask how data should be structured to support them without rebuilds
3. Challenge weak suggestions (e.g. categories stored inside each task vs a separate category structure)
4. Return to build mode and add one feature at a time with 'Do not change anything else'
> "Before I add any new features, I want to plan the full data structure for this task management app" — Mikey No Code (~14:29)

**Mandatory pre-publish security scan** (operations)
1. Run Base44's built-in security scan before every publish
2. Review flagged exposed API keys, broken access-control rules and dependency vulnerabilities
3. Apply recommended fixes one at a time
4. Re-run the scan until the app passes
> "Making it a required step before every publish is one of the simplest ways to avoid shipping an app that works on the surface great, but is not secure underneath" — Mikey No Code (~19:30)

**Realistic-data testing** (operations)
1. Fill the app with realistic items: short and long titles, mixed priorities, overdue and future deadlines, active and completed states
2. Use more than one user account
3. Exercise every core flow as a real user would (create, complete, delete, switch priorities)
4. Fix layout and logic issues (e.g. long titles pushing buttons, overdue dates not flagged) before sharing

**Scale-ready structural defaults** (product)
1. Make records belong to a workspace rather than directly to a user, without changing visible functionality
2. Move important, consistency-critical logic into back-end functions instead of the browser
3. Avoid hard-coded values that should be configurable
> "Update the data structure so that tasks belong to a workspace rather than directly to a user" — Mikey No Code (~24:18)

## Lessons

- *automation_ai*: With AI builders, speed makes it easier to dig a hole: process discipline at the start matters more than generation speed.
- *validation_testing*: An MVP prototype means the single most important function working, not a rough version of the whole app.
- *automation_ai*: Prompt quality determines first-build quality: say what it does, how it looks, what users can do and what to exclude.
- *operations*: Cross-cutting concerns (auth, data ownership) should be added early because every later feature depends on them.
- *operations*: Plan the data model with the AI before writing code; design decisions are cheap before features depend on them.
- *legal_risk*: Security review and realistic-data testing should be standard gates before publishing or sharing, even for small apps.
- *scaling*: Building for scale means a few smart structural defaults (workspace-based ownership, server-side logic), not building every future feature.
- *automation_ai*: Many problems blamed on AI builders are actually caused by the process used around them.
- *mindset_execution*: If changing the whole workflow is too much, start with structured first prompts and early authentication for the biggest immediate gain.

## Warnings and mistakes

- Putting the full feature set into one giant first prompt produces bloated, inconsistent, partly missing builds whose early mistakes get harder to fix.
- Vague one-line prompts make the AI fill gaps with its own defaults, leading to round after round of corrections.
- Leaving authentication to the end forces retrofitting user ownership into the data model, queries and every page.
- AI code generators prioritise making features work and may not catch exposed API keys, weak access rules or vulnerable dependencies.
- Testing only with tidy placeholder data hides layout bugs and edge cases that real users will hit.
- The creator's '$499 normally, free for you' masterclass pitch is a promotional funnel; treat claims about students' 'successful AI-powered businesses' as unverified.

## Tools mentioned

Base44 (AI no-code app builder used for the demo; built-in auth, discuss mode, security scan and back-end functions; security scan is free), Mikey No Code Base44 Masterclass (Creator's own course on building SaaS apps, websites, AI agents and mobile apps with AI; $499 normally, offered free via link)
