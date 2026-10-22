# I Built a Money-Making App in 1 Hour With AI (Bolt v2 Review)

- **Video:** [OomOCuptgr4](https://www.youtube.com/watch?v=OomOCuptgr4) · **Channel:** The Koerner Office · **Uploaded:** 2025-11-14 · **Length:** 13 min · **Transcript:** ok
- **Speakers:** Chris Koerner (host) · **Format:** tool_review
- **Evidence quality:** C — Live build demo by the host; no revenue results and the tool was only tested on his own inboxes. Likely sponsored by Bolt. · Promotional conflict: Possible bolt.new sponsorship; explicit .online domain sponsor read with discount code.
- **Extraction:** grokbot · quotes verified 11/11

## Summary

Chris Koerner tests bolt.new V2 (now integrating Claude Code) by building a PR outreach app live in about an hour with 15-20 prompts. The app stores company and campaign info, accepts a CSV of journalists, generates AI pitches via OpenAI, sends them through Resend, and tracks opens and replies. Several things broke along the way (saving data before Supabase was connected, a select-all bug, fallback templates until the OpenAI key was added, needing a Resend marketing account) and were fixed by describing errors and pasting screenshots. Bolt refused to scrape journalist emails for privacy reasons. Key takeaway: non-coders can build working internal automation tools quickly, but expect iterative debugging; the video also contains a .online domain sponsor read.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **AI PR outreach app (journalist pitching robot)** — A vibe-coded app that stores company info, finds relevant journalists, writes personalised quirky pitch emails with AI, sends them automatically and tracks opens, clicks and replies. | ai_automation | deep | 4/5/4/5/3 | 4 |

### I1. AI PR outreach app (journalist pitching robot)

- **Customer:** Founders launching new businesses who want press coverage (Chris himself)
- **Problem:** PR and paid ads are expensive; getting the word out about new businesses
- **Offer:** Dashboard for company info and campaigns, journalist database with CSV upload, AI pitch generation, bulk sending and analytics
- **Business model:** Internal tool replacing a PR person / paid ads; could be sold as SaaS (not stated)
- **Pricing:** Self-built tool running costs. stated running cost USD 20-40 per month Chris frames it as hiring a PR person for $20-40 a month; Resend marketing plan needed.
- **Acquisition:** other: Built for own use; no customer acquisition discussed.
- **Delivery:** Built in about an hour with 15-20 prompts on bolt.new V2 using Claude Code, OpenAI for pitch writing, Resend for sending, Supabase/Bolt database for storage; journalist list uploaded as CSV.
- **Unit economics (claims):** About $20-40 a month to run; Built in about an hour with 15-20 prompts; Could save thousands of dollars on paid ads (claim)
- **Tools:** bolt.new, Claude Code, OpenAI API, Resend, SendGrid, Supabase, Google Sheets
- **Startup cost:** Low: tool subscriptions only (not stated precisely)
- **Time to first revenue:** About an hour to build
- **UK applicability [E]:** 4/5 — Tooling works the same in the UK. Bulk unsolicited emails to individual journalists' personal addresses raise PECR/UK GDPR issues; corporate addresses with an opt-out are safer. Deliverability and spam reputation matter.
- **Risks:** The bot refused to scrape journalists for privacy reasons; scraped contact data raises UK GDPR issues; Spammy mass pitches can burn sender domain reputation; Vibe-coded apps break often and need repeated reprompts; Generated pitches were 'wonky' and need prompt tuning
- **Automation [E]:** acquisition 4/5 (Journalist discovery via scraped lists; sending is automated. UK: cold emails to journalists at their work addresses are lower-risk B2B, but UK GDPR legitimate-interest assessment, opt-out and source transparency are needed; scraping personal emails is risky.); onboarding 5/5 (Self-serve company and campaign inputs.); delivery 4/5 (AI writes and sends pitches; a human should review tone and accuracy.); billing 5/5 (Software subscriptions.); support 3/5 (Replies from journalists need human handling.)
> "Build me a PR outreach automation app. I need a dashboard where I can input my company info and campaign details" — Chris Koerner (~1:52)
> "Basically, I'm about to hire a PR person that only charges about 20, 30, 40 bucks a month" — Chris Koerner (~1:41)

## Revenue and metric claims (unverified claims)

- **Running the PR robot costs about $20-40 a month** (cost, first-hand, hypothetical, claimant: Chris Koerner)
  > "I'm about to hire a PR person that only charges about 20, 30, 40 bucks a month" — Chris Koerner (~1:41)
- **App built in about an hour with 15-20 prompts** (hours, first-hand, claimant: Chris Koerner)
  > "with uh I don't know, 15 20 prompts and reprompts and in about an hour's time, we successfully built PR app" — Chris Koerner (~13:01)
- **Chris has started 80-plus businesses (in sponsor read)** (other, first-hand, claimant: Chris Koerner)
  > "After starting 80-plus businesses, I've learned that you can have the perfect idea" — Chris Koerner (~6:10)

## Tactics and playbook steps

**Build an internal tool with a vibe-coding platform** (product)
1. Write one plain-English prompt describing dashboard, data inputs, AI generation, sending and tracking
2. Ask the tool what it needs next instead of specifying integrations yourself
3. Add API keys as secrets (OpenAI, Resend) in the project settings
4. Connect a database (Supabase) before testing saves
5. Test with your own email addresses in a CSV before real sends
6. When something breaks, describe it and drag in a screenshot
> "I love screenshotting stuff and just dragging it over there. It helps a lot" — Chris Koerner (~9:56)

**Quirky personalised PR pitches** (acquisition)
1. Find journalists who cover your niche
2. Use AI to analyse what they write and match their style
3. Keep pitches short, simple and funny so they do not read as spam
4. Track opens, clicks and replies
> "write personalized pitched emails for me that are kind of funny and quirky and don't sound like spam" — Chris Koerner (~1:19)

## Lessons

- *automation_ai*: Non-coders can tell an AI builder the goal and let it explain the integration steps.
- *automation_ai*: Screenshots of errors help an AI coding tool fix bugs in fewer prompts.
- *validation_testing*: Test outbound tools with your own addresses before contacting real people.
- *customer_acquisition*: Earned PR can be an alternative to paid ads for launching new businesses.
- *other*: Secure the right domain early when launching a business (from the sponsor read).

## Warnings and mistakes

- Vibe-coded apps say they are 'ready' when they are not; expect breakage and many reprompts.
- AI builders may refuse to scrape personal contact data for privacy reasons; scraping journalist emails carries data-protection risk (UK GDPR).
- Without the real API key, the app silently used fallback templates rather than AI.
- Transactional email accounts may not allow marketing sends; a separate marketing plan was needed.

## Tools mentioned

bolt.new (V2) (Vibe-coding platform used to build the app), Claude Code (AI coding agent integrated into bolt.new), OpenAI API (Pitch generation; Bolt also offers a built-in OpenAI package), Resend (Sending emails; marketing account needed; paid plan (price not stated)), SendGrid (Alternative email sender suggested by Bolt), Supabase (Database behind the Bolt app), Google Sheets (Creating the journalist CSV), .online domains (get.online) (Sponsor: domain names; 99 cents for the first year with code)
