# Playbook: AI missed-call text-back agent for local trades

**Source:** The Koerner Office — *This Might Be the Easiest Way to Sell AI to Businesses* (`g4-3AxelI_Y`, published 3 Apr 2026). Transcript: `../transcripts/raw/g4-3AxelI_Y.txt`
**Ranking:** #22 of 207, weighted 3.90 (E4 V4 S4 Sc4 R3 A4 F4) — `../analysis/all_ideas_ranked.json`
**Template:** the outline in `../analysis/opportunity-shortlist.md` ("What to ask the playbook for"). The original ClarityRelay manual was not found in the repo, on the box or in Google Drive.

> **Evidence status.** Every money figure below is the presenter's own claim. The video shows the build and one live prospect reply asking about price, but **no closed sale**. GoHighLevel sponsors the video. This idea overlaps ClarityRelay (AI support agents). Treat it as a cheap add-on or a separate SMS channel, not as a new business.

---

## 1. ICP and buyer

- **Who:** owner-operated local service businesses that lose jobs when they miss calls. The video's examples are tree trimming, plumbing and HVAC.
- **Buyer:** the owner. The presenter notes "most business owners don't even have employees", so the owner is the buyer and the user.
- **Pain:** "most small businesses are letting calls go to voicemail and hoping people call back. Side note, they don't." He also quotes the claim "57% of sales goes to whoever responds first".
- **Why now:** the plain missed-call text ("sorry I missed your call, our hours are 9–5") already exists, but it is a single static message. The upgrade here is a **two-way AI conversation that books the estimate**.

## 2. Offer and pricing

- **Offer:** a done-for-you missed-call workflow with an AI SMS agent. It replies to a missed call, qualifies the caller, books an estimate and alerts the owner. The owner can take over at any time.
- **Price (from the video):** "a $500 to $2,000 a month per client service". The demo pitch was **$500/month, "if it doesn't pay for itself in the first 90 days, then I'll give you all your money back."**
- **UK note (not from the video):** convert the price to pounds and set it yourself. The video gives no UK pricing evidence.

## 3. Niche-selection scorecard

Score each candidate trade from 1 to 5 on the criteria the video uses:

| Criterion | What to check | Video basis |
|---|---|---|
| Calls are the main lead source | Customers phone rather than book online | Trigger is an inbound call |
| Owner is often on a job | Trades that can't pick up mid-job | Tree trimming / plumbing examples |
| Emergency jobs exist | Needs an "emergency" branch (e.g. tree on a house) | Emergency branch in the build |
| High job value | One extra booked job covers the fee | "pays for itself in 90 days" guarantee |
| You know the trade | Insider language in the prompt | He chose tree trimming "cuz I own a tree trimming business" |

Pick one trade and one area to start.

## 4. First 30 prospects

The video's method was **Outscraper → "tree trimming businesses in Dallas, Texas" → keep phone numbers only → clean the formatting → CSV (181 numbers)**.

For the UK version:
1. Run the same Outscraper (or Google Maps) search for one trade in one town.
2. Keep business name, phone, website and email.
3. Take the first 30. Favour businesses that have reviews but no online booking.
4. Note whether each one is a limited company or a sole trader, because the outreach rules differ (see §5).

## 5. Outreach scripts

**What the video did:** a ringless voicemail drop to the scraped list (the tool is transcribed as "Slack Broadcast", probably Slybroadcast), with a vague message designed to get a call back: *"Hey, this is Chris Kerner. I'm here in Dallas, Texas, and I'm looking for a tree trimming business. So, please give me a call back."* The call-back triggers the same missed-call AI ("dog fooding"), which then pitches the prospect:

> "Hey, I know this is random, but I'm using a missed call text back on you right now that will have a full conversation with you with AI. It feels real, doesn't it? I want to install it for you on your tree trimming business so you can close more jobs. What questions do you have?"

On price: *"It is $500 a month, but if it doesn't pay for itself in the first 90 days, then I'll give you all your money back. Can we hop on a call so I can explain?"*

**UK compliance (not from the video; check ICO PECR guidance before sending):** ringless voicemail drops and unsolicited marketing texts are likely to need prior consent in the UK, especially for sole traders. Use a compliant channel to get the first call-back instead:
- **Email or LinkedIn** to the business, with a one-line hook: "Call this number and hang up. You'll see what your customers would get back."
- That keeps the dog-food demo: the prospect calls your GHL number, and your AI texts them back because they started the contact.

## 6. Demo / validation workflow

The demo is the product. Your GHL number runs the **sales version** of the workflow, so every prospect who calls it experiences the agent before any human talks to them.
- Branches in the sales version: **booked**, **unqualified**, and **hot lead** (defined as "customer is very interested asking detailed questions or wants to start immediately without a demo").
- A hot lead sends you an SMS with the contact's first name and phone number so you can call them.

## 7. Delivery SOP (GoHighLevel build, as shown)

1. **Automation → Create workflow → From template → "missed call text".**
2. **Trigger:** incoming call that is busy, goes to voicemail or isn't answered.
3. **Delay** 1–3 minutes "so SMS doesn't feel like a bot". The template's 0.2 minutes is too short.
4. **Assign to user** (only if the client has staff).
5. **Add contact tag** `missed-call`.
6. **Delete the template's static text step** and replace it with **Conversation AI** (advanced bot configuration on).
7. **Personality/prompt:** paste the template prompt into Claude or ChatGPT and ask it to rewrite it for the client, e.g. "an AI agent representing [Business], a [trade] company in [area] that is engineered to book appointments for quotes". Rules: warm, casual, "talk like a real person". Let the AI draft the FAQ and knowledge base. Trim each field to 300 words or fewer.
8. **Settings:** wait up to 24 hours for a reply · channel SMS · skip questions already answered · **max 5 bot responses** · **35 seconds between responses**.
9. **First message:** "Hey, sorry we missed your call. What's going on with [the job]?" **Remove the quote marks.**
10. **Owner takeover:** a push notification plus an SMS to the assigned user.
11. **Branches:**
   - **Booked**: the customer gave their need, address and preferred day. Send the owner an SMS.
   - **Emergency**: urgent damage. Send the owner an SMS saying "emergency".
   - **Unqualified**: wrong service or out of area. Tag only, no alert.
   - **Timeout**: end the workflow.
12. **Publish → Save.** For the next client: **duplicate the workflow** and swap in that trade's details.

## 8. QA / acceptance gate (before billing)

- [ ] Call the client's number from a test phone and let it ring out. The text arrives after the delay, with no quote marks.
- [ ] Run one conversation each for booked, emergency and unqualified. Each one fires the right alert or tag.
- [ ] The bot stops after 5 replies and never sends two messages within 35 seconds.
- [ ] The owner takes over mid-thread and the bot stays quiet.
- [ ] The owner has approved the business details, hours and service area in the prompt.

## 9. 21-day launch plan

| Days | Action |
|---|---|
| 1–2 | Pick a trade and town with the §3 scorecard. Start the GHL trial (the sponsor link gives 30 days). Connect a number. |
| 3–4 | Build the client workflow (§7) for a fictional business in that trade. Build the sales "dog-food" version. |
| 5 | Run the QA gate (§8) on both. |
| 6–7 | Build the 30-prospect list (§4). Draft compliant email/LinkedIn outreach (§5). |
| 8–14 | Send outreach in batches of 10. Every call-back goes through the AI. Call hot leads the same day. |
| 15–18 | Install for the first client: duplicate the workflow, edit the prompt, QA, go live. |
| 19–21 | Review booked jobs with the client. Decide whether to continue (§10). |

## 10. Metrics and kill criteria

**Track:** prospects contacted · call-backs or replies · AI conversations · hot leads · sales calls · clients closed · client missed calls → AI conversations → booked estimates.

**Kill or rethink if** _(proposed thresholds, not from the video; set your own)_:
- after 30 prospects, no one calls the demo number or asks the price;
- after 21 days, there's no paying client and no agreed pilot;
- a live client's AI conversations don't produce any booked estimates within the 90-day guarantee window. The guarantee then refunds them.

## Risks (from the card)

- No closed revenue shown; pricing is the presenter's claim.
- The sponsor (GoHighLevel) has an interest in the story.
- UK PECR/GDPR limits on ringless voicemail and cold SMS.
- Overlaps the AI support-agent offer already covered by ClarityRelay.
- Crowded among GHL resellers.
