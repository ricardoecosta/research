# Gemini 4 Argon - Full Tutorial: How To Build an App In Minutes

- **Video:** [J9GXGqd3isM](https://www.youtube.com/watch?v=J9GXGqd3isM) · **Channel:** Mikey No Code · **Uploaded:** 2026-10-19 · **Length:** 24 min · **Transcript:** cached
- **Speakers:** Mikey (host) · **Format:** tutorial_howto
- **Evidence quality:** C — Tool tutorial with a demo app; no customers, pricing or revenue; heavily promotional. · Promotional conflict: Base44 masterclass promotion (likely Base44 affiliate).
- **Extraction:** grokbot · quotes verified 12/12

## Summary

Mikey (Mikey No Code) builds 'Lumen', an AI journaling web app, in Base44 using Google's Gemini 4 Argon across six layered prompts: liquid-glass design and core screens, organisation features, AI reflections and chat, authentication, a Stripe premium tier (PIN-locked entries, mood insights), and a UX polish pass, then tests the full new-user journey. The point is that coherence across many prompts, not the first impressive prompt, is the real test. The video repeatedly promotes his 'normally $499' Base44 masterclass, offered free. No revenue or distribution is covered.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Lumen: AI journaling app with freemium subscription (built on Base44)** — A liquid-glass journaling web app with tags, search, streaks, AI reflections and an AI chat over past entries, with a Stripe premium tier for PIN-locked entries and mood insights. | saas_software | deep | 3/5/5/5/4 | 5 |
| I2 | **Base44 masterclass (creator's course)** — Course teaching how to build profitable SaaS, websites, AI agents and mobile apps with Base44, normally $499 but offered free. | education_coaching | mention | 4/5/4/5/3 | 5 |

### I1. Lumen: AI journaling app with freemium subscription (built on Base44)

- **Customer:** Consumers who journal regularly
- **Problem:** Hard to find old entries and to reflect on patterns in personal writing; privacy of personal thoughts
- **Offer:** Journal with moods, tags, favourites, calendar, writing streak, AI reflect button, daily AI prompt, assistant chat; premium: 4-digit PIN entry lock, mood trends, writing stats, themes, AI monthly summary
- **Business model:** Freemium monthly subscription (Stripe)
- **Pricing:** Monthly premium subscription.  Price not stated; Stripe in test mode
- **Acquisition:** other: Not covered; tutorial demo app only
- **Delivery:** Built by prompting Gemini 4 Argon inside Base44 in six layered prompts; Base44 provides database, auth, AI integration and Stripe; published to a public link
- **Unit economics (claims):** 
- **Tools:** Base44, Gemini 4 Argon, Stripe, Google sign-in
- **Startup cost:** Base44 Builder plan or higher (needed for manual model selection); price not stated
- **Time to first revenue:** Not stated (built in one session)
- **UK applicability [E]:** 5/5 — Software works in the UK; journal entries are sensitive personal data under UK GDPR (possibly special category, e.g. health), requiring a lawful basis, privacy policy and care sending data to AI providers.
- **Risks:** Crowded journaling app market (Day One etc.); Platform lock-in to Base44; Sensitive personal data and AI processing (UK GDPR); Demo, no traction or revenue shown
- **Automation [E]:** acquisition 3/5 (Distribution not covered; a consumer app needs app-store/SEO/content marketing, which can be largely automated.); onboarding 5/5 (Self-serve signup with Google login.); delivery 5/5 (Software runs unattended; AI features via Base44 integration.); billing 5/5 (Stripe subscription.); support 4/5 (Mostly self-serve; AI assistant could handle support.)
> "let's ask Argon to create Lumen using Apple's iOS 26 liquid glass design" — Mikey (~4:04)
> "the first feature is entry locking, which lets users protect individual entries using a four-digit" — Mikey (~15:44)
> "Users on the free version should see now a blurred preview of the insights page" — Mikey (~16:12)

## Revenue and metric claims (unverified claims)

- **Masterclass normally costs $499 (also said $4.99), offered free** (price, first-hand, claimant: Mikey)
  > "my masterclass normally costs $499 to join" — Mikey (~1:49)
- **Manual model selection requires Base44's Builder plan or higher** (cost, second-hand, claimant: Mikey)
  > "manually selecting a model requires Base 44's Builder plan or higher" — Mikey (~3:04)

## Tactics and playbook steps

**Build an AI app in layered prompts, not one prompt** (product)
1. Prompt 1: design system (liquid glass) and core screens with database; explicitly defer tags, search, AI, accounts, payments
2. Prompt 2: organisation features (tags, favourites, search, filters, calendar, streaks)
3. Prompt 3: built-in AI features (reflect, daily prompt, assistant chat with retry)
4. Prompt 4: authentication and per-user data isolation; publish to test
5. Prompt 5: Stripe test-mode premium with locked features and blurred previews
6. Prompt 6: global design/UX polish pass (empty states, loading, mobile)
7. Run a full new-user test on the published app
> "It's the 10th decision that's hard, because now it has to agree with the other nine." — Mikey (~0:42)

**Freemium paywall design** (pricing)
1. Show free users a blurred preview of premium insights
2. Trigger upgrade prompt when trying a locked feature
3. Show premium badge and manage-subscription option after payment

**Test payments on the published app** (operations)
1. Stripe checkout doesn't work in the Base44 preview, so publish first
2. Use Stripe test mode and test cards
3. Verify features unlock after checkout
> "Stripe checkout doesn't work [music] inside the Base44 editor preview" — Mikey (~17:04)

## Lessons

- *operations*: Establish the design system early so later features stay consistent.
- *automation_ai*: Explicitly defer features in prompts to keep the AI focused.
- *automation_ai*: Use platform-native auth, AI and payments instead of building from scratch.
- *pricing*: Gate premium features with visible previews to drive upgrades.
- *offer_design*: Do a final whole-app UX pass for empty states, loading and readability.
- *customer_acquisition*: Building is the easy part; the tutorial does not address customer acquisition.

## Warnings and mistakes

- Most AI app videos stop at the first prompt; coherence across many changes is the real test.
- Features can work in preview but break in the published version; test the live app end to end.
- Most people build basic apps that don't make money (creator's framing for course upsell).
- UK GDPR: journal content is sensitive personal data; sending it to AI models needs disclosure and safeguards.

## Tools mentioned

Base44 (No-code AI app builder with database, auth, AI integration and Stripe; Builder plan or higher for manual model selection), Gemini 4 Argon (Google model used to build the app), Stripe (Subscription payments (test mode)), Google sign-in (Account creation)
