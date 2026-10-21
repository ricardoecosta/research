# Plan: scanner-led AI missed-call text-back for Bromley trades (6 weeks, side-hustle pace)

22 Oct 2026. Combines idea #22 *AI missed-call text-back* (3.90), #25 *AI voice receptionist* (3.85) and #3 *Niche Google Maps lead scraper* (4.15) from `../analysis/all_ideas_ranked.md`. Playbooks: `../playbooks/ai-missed-call-text-back.md`, `../playbooks/apify-actor-wrapper-maps-lead-scraper.md`. UK rules reused from `build-first-websites-plan.md` §5.
**[E]** = my estimate or assumption. Creator figures are claims, cited by video ID (`../transcripts/raw/`). Prices were read on 22 Oct 2026 (UK time) unless marked; $ → £ at 1.32 [E, rate used by keepbooked.co.uk on 30 Sep 2026].

## Bottom line (honest)

- **The idea:** a scanner pulls Bromley trades from Google Maps and checks their websites for chat, bots, WhatsApp and booking. You sell the ones with gaps a **done-for-you AI missed-call text-back**: a missed call gets an SMS within a minute, the AI asks what the job is, and the owner gets a summary. Later you upsell an **AI voice receptionist** and a **website chat widget**.
- **The first data point is in (§9):** on 29 Bromley trade sites that loaded, **0% had live chat or an AI bot**, **0% had online booking**, and **66% had no chat, bot, WhatsApp or booking at all**. The website gap is close to universal. So the scanner is less useful as a filter ("who lacks chat") and more useful for personalising the pitch and choosing the channel. What it **can't** see is whether they miss calls. That gets measured by phone in week 1 (P2).
- **Why it beats the websites idea for you:** it's a product you build once and copy per client. The setup is about 30 minutes. It's built by you in code (Twilio + an LLM), not by hand-crafting sites. It has a natural upgrade path (voice, chat) and a demo that sells itself: "call this number and hang up". Creators call it a "wedge product… you can demo this to a roofer from your phone in like 90 seconds" (`VOo3M3ZHUoA`). They call voice agents "by far… the most advanced and the easiest to sell to small business owners" (`tVbN7XSPnM0`).
- **The honest weaknesses:**
  - The US numbers don't carry over. The videos claim "$500 to $2,000 a month per client" (`g4-3AxelI_Y`, `tKTlzugGgYw`), but UK trades can **self-serve the same thing for £6.49–£97/month** (§3). Your edge has to be *done for you, local, and seen working first*, not the software.
  - No video shows a closed sale. `g4-3AxelI_Y` ends with a prospect asking about price.
  - The proven US outreach (scraped lists plus ringless voicemail drops) is **not legal here** without consent (§6).
  - Selling still needs live calls and conversations, which are your scarcest hours with a toddler.
- **Cost of finding out:** ≈ **£150–£200 cash (cap £300)** and **≈ 40 hours** over 6 weeks (≈ 6–7 h/week).

## 1. The offer and pricing (GBP)

| Plan | Price [E] | What they get | Anchor |
|---|---|---|---|
| **Pilot (the door-opener)** | **£0 for 30 days**. Installed on their phone in 20 minutes, in person or on a call. They keep it only if it caught at least one real enquiry. | AI text-back on missed calls, owner SMS/email summary, weekly "calls you missed" count | Copies the "pays for itself in 90 days or money back" guarantee (`g4-3AxelI_Y`) and the free first install (`AWesz6TJRcA`), but much shorter |
| **Text-back (core)** | **£59/month**, no setup on the pilot (otherwise £99), cancel any time | Pilot features + your business name in the text, emergency flag, after-hours script, monthly report, 2 prompt changes a month | Between TextBack Pro £47 and Callio £79.99 (§3). You add the done-for-you setup and a local person. |
| **Receptionist (upsell, week 5+)** | **£129/month** | AI voice answers after 4–5 rings or out of hours, then text-back; includes a website chat widget fed with the same FAQ | Snag AI £149 setup + £199/month, Trade Receptionist £49–£159, Talka £99.99 (§3) |

- **Pitch math:** one boiler repair, roof leak or patio quote covers a year. The creator's version: "it's a $30,000 job that they might be missing out on" (`VOo3M3ZHUoA`). UK job values are [E].
- **What the pilot measures:** number of missed calls → texts sent → replies → enquiries the owner says were real. If those counts are honest, the pilot does the closing.
- **VAT:** none needed below the £90k threshold.

## 2. Build: what to build, what to buy, hours

**Decision: build the text-back yourself; rent the voice layer.** GoHighLevel is the creators' tool (`g4-3AxelI_Y`, `VOo3M3ZHUoA`; both are GHL-sponsored or affiliate). It costs **$97/month (~£73 [E]) for only 3 sub-accounts**, or $297 for unlimited, priced in USD with usage on top (gohighlevel.com/pricing; agency-crm.co.uk/pricing, read 20 Sep 2026). At that price the test loses money until client 2–3. You're technical, so your own stack costs ~£2–£10 per client per month [E] and gives you a product you own. Use GHL's free 14-day trial **only** to copy its workflow ideas (delay, 5-reply cap, 35 s gap, owner takeover; `../playbooks/ai-missed-call-text-back.md` §7).

| Part | Build or buy | Tool and cost | Hours [E] |
|---|---|---|---|
| Scanner | **Built** (this repo) | `../tools/chat_widget_scanner.py`. Static plus headless Chrome; detects 25 chat tools, 9 AI bots, WhatsApp, 19 booking tools, call tracking, form, mobile, tap-to-call | done (≈3) |
| Prospect source | Buy (pay-as-you-go) | **Outscraper**: first 500 places/month free, then $3/1,000 (outscraper.com/pricing). Or the **Apify** `compass/crawler-google-places` actor, "from $1.50 / 1,000 places" on paid plans, $5 free monthly credit (apify.com, read today). Both scrape Google Maps; see §8 for the terms risk. | 2 |
| Company check | Free | Companies House API: Ltd/LLP → email allowed (§6) | 1 |
| UK number | Buy | **Twilio UK mobile number (+447…) $2.50/month** (Twilio GB pricing). It must be a mobile number so it can send *and receive* SMS. Twilio needs an approved **UK Regulatory Compliance bundle** (KYC: ID plus UK proof of address, or business documents) before UK numbers work (Twilio UK regulatory guidelines; required for all UK long codes since 30 Sep 2024). Start it on day 1, because approval takes time [E]. **Not** an alphanumeric sender ID: those are one-way (no replies possible) and sender names are policed by the MEF SenderID Protection Registry. | 1 + wait |
| Text-back service | **Build** | Small FastAPI/Node app on Fly.io or Cloudflare Workers (£0–£5/month [E]). Twilio voice webhook: on the diverted call, play a 1-line greeting ("Sorry, [name] is on a job, we'll text you now"), hang up, send the SMS after 60 s, then run the LLM conversation (≤5 replies, ≤160 characters each, owner takeover keyword). Owner gets an SMS/email summary. | 10–12 |
| Message cost | Pay as you go | Twilio UK outbound **$0.056 per segment**, inbound $0.0075 (Twilio GB pricing, Oct 2026). One conversation of ~6 outbound texts ≈ £0.25 [E]. 30 missed calls/month ≈ £8 + number ≈ **£10 per client per month** [E]. | — |
| LLM | Buy | Any cheap model; well under £1 per client per month [E]. Hard rules in the prompt: never quote prices, never diagnose; **"smell gas" → tell them to call 0800 111 999**; power cut → 105 (from theaitill.com's trade triage table). | in the 10–12 |
| Owner setup | Free | Conditional divert on their mobile: `**61*07…#` (no answer), `**62*` (unreachable), `**67*` (busy). Works on EE, O2, Vodafone (call2sms.co.uk divert-codes guide). Keep their own number. Check whether their tariff charges for diverted minutes [E]. | 0.3 per client |
| Voice (week 5+) | Rent | **Retell** ~$0.055/min platform + voice + LLM ≈ $0.11/min, using your own Twilio UK number (Retell can't sell UK numbers). Or **Vapi** $0.05/min + providers (retellai.com/pricing, vapi.ai/pricing). ≈ 10p/min all in, the same figure Proly publishes ("roughly 10p a minute"). | 6–8 |
| Demo line | Build (same app) | Your own "sales" number runs a sales version of the bot: "I'm using a missed call text back on you right now… It feels real, doesn't it?" (`g4-3AxelI_Y`). It tags hot leads and texts you. | 2 |

**Not built in the 6 weeks:** a dashboard, self-serve signup, a chat widget, WhatsApp. For now a weekly CSV/email report is the dashboard.

## 3. UK competition (published prices)

| Product | Price | Type | Source |
|---|---|---|---|
| TextTheCaller | £6.49/mo, 50 texts | static text-back | m1studio.co.uk guide (30 Sep 2026) |
| ReplyBack | £29 / £59 | text-back + lead capture | same |
| Call Catchers | £35 + <5p/text | text-back | same; keepbooked.co.uk |
| Call2SMS | £37 / £67 / £97 | AI text conversation | same |
| TextBack Pro | £47 (300 leads) / £97 | AI text + Google Calendar booking | textbackpro.co.uk/pricing |
| Replayable | £49.99 / £79.99 / £129.99 | text-back | replayable.co.uk |
| Callio | £79.99 | AI text booking flow | callio.co.uk |
| M1 Studio "Missed-Call Rescue" | £800 one-off, done-for-you | setup service | m1studio.co.uk |
| Proly | £29 / £59 / £119 | AI voice receptionist (pre-launch) | proly.co.uk/pricing |
| Trade Receptionist | £49 (50 calls) – £249 | AI voice | tradereceptionist.com |
| Talka | £99.99 (600 min) / £199 | AI voice + WhatsApp | talka.co.uk |
| Snag AI | £149 setup + £199/mo | done-for-you AI voice | snagai.co.uk |
| Answer.co.uk | £2.20/call human; AI £10/mo + 85p/call | answering | keepbooked.co.uk |

**What this means:** the software is commoditised and cheap. So price the done-for-you service (£59), not the SMS. The real competition is the trade doing nothing, so the pitch is "it's already working on your phone", not a feature list. One kill question (§7): do prospects say "I'll just get the £6.49 one"?

## 4. The 3 cheapest probes in week 1

| Probe | What | Cash | Measure | Pass mark [E] |
|---|---|---|---|---|
| **P1: scan 200 Bromley trades** (days 1–2) | Outscraper free tier: plumber, electrician, roofer, heating engineer, landscaper, tree surgeon, locksmith × Bromley borough towns (BR1–BR8, Beckenham, Penge). Drop chains, drop businesses under 10 reviews, dedupe. Run `chat_widget_scanner.py --render` on every website. Companies House match. | £0 | % no website · % site with no chat/bot/WhatsApp/booking · % Ltd · reviews and rating | Data, not pass/fail. It confirms or corrects the 66% from §9 on an unbiased sample and gives a list of 200 |
| **P2: ring test + live voicemail** (2 lunch slots, days 3–5) | Screen 60 numbers against **TPS/CTPS** (Data Soap 200 checks for £4.99). Call 30 that are clear, in working hours, yourself, live. **Answered:** "Quick one, I'm Ricardo from Bromley. When you're up a ladder and the phone rings, what happens to that call?" **Missed:** leave the live voicemail (§6) inviting them to ring the demo line. | ~£5 | **% of calls unanswered** (the headline number for every pitch) · call-backs · demo-line calls · "how do you handle it" answers | ≥30% unanswered; ≥3 of 30 ring the demo line or ask the price |
| **P3: "call this number and hang up"** (posted day 3 / sent day 4) | 40 **postcards** (Stannp A6 ≈ £0.90 each) to trades with a postal address, plus 30 **emails to Ltd companies only**. Each one gets its own demo number or a code word. | ~£36 | demo-line calls by source · text conversations · replies · pilot requests | ≥5% of 70 call the demo line; ≥2 ask for a pilot |

Every demo-line caller has started the contact themselves, so the AI texting them back is replying to their call, not cold SMS. Hot leads get a call from you the same day.

## 5. Week by week (≈40 h)

Rhythm [E]: Tue and Thu 20:30–22:30 for building, two 30-minute lunch slots for calls (trades pick up at lunch, not at 21:00), and one Saturday-morning hour for installs.

| Week | Hours | Do | Output |
|---|---|---|---|
| 1 | 8 | Submit the Twilio UK bundle (day 1). Pay the ICO fee. P1 scan of 200. Build the static text-back plus the demo line (AI version if time allows). Write the privacy notice. Run P2 and P3. | Prospect sheet, scan stats, demo line live, probes running |
| 2 | 8 | Finish the AI conversation, owner summary and takeover. QA it (§7 gate). Follow up every demo caller and every P2 "maybe". Send email follow-up 2 on day 7. **Install the first 1–3 pilots** (20-minute divert setup). | First pilots live |
| 3 | 6 | Second wave: 30 more screened calls plus 40 postcards to the best-performing trade from P2/P3. Weekly pilot reports ("you missed 7 calls; 4 people replied to your text"). | **Week-3 gate** |
| 4 | 6 | Convert pilots that reach day 30 to £59 (Stripe Payment Link). Ask every "no": "What would have made it a yes?" Fix the prompt from real transcripts. | First paid customers, or the reasons why not |
| 5 | 6 | Voice add-on with Retell on one willing customer at £129 (or a free trial). Optional: publish the scanner as an Apify actor (§10). | Upsell signal |
| 6 | 6 | **Week-6 gate.** If continuing, turn it into a monthly wave (one trade, one area, 60 calls + 40 cards) and write up the numbers. | Decision and write-up |

## 6. Outreach (UK rules) and scripts

**Rules** (from the websites plan, ICO B2B guidance; re-read before sending):
- **No cold SMS or WhatsApp** to anyone without consent.
- **No ringless voicemail or automated calls.** Under PECR, automated marketing calls need prior consent. This rules out the videos' method (`tKTlzugGgYw`, `g4-3AxelI_Y`).
- **Email** only to **Ltd/LLP** addresses, with your identity and an opt-out. Sole traders and partnerships get post, a screened call, or in person.
- **Live calls** only after **TPS + CTPS** screening (re-screen every 28 days) and against your own do-not-call list.
- **Post** sits outside PECR; UK GDPR still applies.
- **ICO fee** Tier 1, £52 (£47 by direct debit).
- **Text-back to callers:** in my reading [E], a text replying to someone who just rang a business is a service message, not unsolicited marketing, as long as it stays about their enquiry. Keep promotional content out of it, and check ICO guidance before launch.

**Live voicemail (P2, when they don't answer):**
> "Hi, it's Ricardo, I live in Bromley. I just rang and you were probably on a job, which is exactly why I'm calling. Ring 07xxx back and hang up straight away. You'll get the text your customers would get from you when you miss them. Ignore this if it's not for you. Thanks."

**Call (when they answer):**
> "Hi, is that [name]? It's Ricardo, I live locally in Bromley, I'll be 30 seconds. When you're up a roof and the phone goes, what happens to that call? … I set up a thing that texts those callers back in under a minute and asks what the job is, so they don't ring the next roofer. Can I put it on your phone free for 30 days? If it doesn't catch you a job, you just switch it off."

**Postcard (P3), front:** "Missed a call today? Ring 07xxx, let it ring, hang up." **Back:**
> "In 60 seconds you'll get the text your customers would get from you. I set this up for Bromley trades, free for 30 days, then £59/month if it's earned it. Ricardo Costa, [town] · [email] · [privacy URL]. Not interested? Bin this and you won't hear from me."

**Email (Ltd only):**
> Subject: [Business] — the calls you miss while on a job
>
> "Hi [name], I'm Ricardo in [Bromley]. I checked [business]'s site: no way for a caller to leave details out of hours [use the scan finding]. Ring 07xxx and hang up, and you'll see what I set up for local trades: callers who don't get through get a text in under a minute, and you get their name and the job. Free for 30 days. Reply 'stop' and I won't email again. Ricardo Costa · [address]"

The "I live in Bromley" opener is the line the websites video calls "the most critical sentence" (`_aGMxMmJJj4`).

## 7. Gates (kill / continue) and the product QA gate

- **Day 7:** **kill** if P2 shows **under 20% of calls unanswered** (no pain) *and* none of the ~100 contacts calls the demo line or asks the price.
- **Week 3:** continue if **≥3 pilots are live**. If prospects like it but won't install, test one variant for 2 weeks: you do the divert in person, or a paid £99 setup with a refund guarantee. **Kill** if under 2 pilots after ~130 contacts.
- **Week 6:** keep going only if **≥2 pilots converted to paid (≥£59/month)**, each pilot logged at least one enquiry the owner agrees was real, cost to serve is **≤£12/client/month**, support is **≤30 min/client/month**, and the cost to win a customer is **≤£150**. **Stop** if the common "no" is "I'll use a cheaper app" (§3), or if 2 weeks in a row slip.

**QA gate before any client goes live:** test call rings out → text arrives within 60–90 s with the business name · each branch works (job, emergency, out of area) · gas smell → 0800 111 999 · the bot stops after 5 replies · owner takeover silences the bot · the owner approved services, area and hours · STOP handling works (adapted from `../playbooks/ai-missed-call-text-back.md` §8).

## 8. Risks and mitigations

- **Cheap UK rivals (£6.49–£97).** Sell done-for-you and local, prove it with the pilot's counts, and don't compete on features.
- **Divert friction.** Some trades use personal iPhones on mixed tariffs, and some networks charge for diverts [E]. Set it up with them on the phone and check it with `*#61#`.
- **The AI saying something wrong** (a price, safety advice). Hard rules, a short reply cap, owner summaries and weekly transcript review.
- **SMS deliverability and number KYC.** Twilio's RC bundle can take time. Keep texts ≤160 characters and include the business name. Keep one spare number.
- **Legal: call recording and AI.** If the voice tier records or transcribes calls, tell callers at the start ("You're through to [business]'s assistant; calls may be recorded"). UK GDPR transparency applies, and the client is the controller, you the processor, so put a short **DPA** in the terms. Keep transcripts 90 days by default [E].
- **Legal: scraped data under GDPR.** Sole-trader listings are personal data. Use legitimate interest with a short written LIA, send an Art. 14 privacy notice on first contact, keep a suppression list, collect business fields only, and pay the ICO fee.
- **Legal: Google's terms.** Scraping Maps (Outscraper, Apify) breaches Google's terms. For internal prospecting the risk is mostly service blocking [E]. **Reselling** Maps-derived lists is the riskier route. The official **Places API** is compliant, but you may store **place IDs only** long-term (developers.google.com/maps … places/policies). Text Search Pro is $32/1,000 with 5,000 free calls a month. If you ever sell data, build it on Companies House, OpenStreetMap and your own website scans, not Maps.
- **Time and toddler.** Calls are the bottleneck: only two lunch slots, and installs on Saturday mornings. The gates are fixed dates.

## 9. Proof: the scanner on 32 real Bromley-borough trade sites

Script: `../tools/chat_widget_scanner.py` (static fetch + headless Chrome, homepage plus one same-site contact/quote page, network requests included). Input: `../tools/scan-results/bromley-trades-sample-input.csv`. Output: `../tools/scan-results/bromley-trades-sample-2026-10-22.csv`.
- **Sample:** businesses found by web search for plumber, electrician, roofer, landscaper, heating, tree surgeon, fencing/driveways, locksmith, decorator and builder in Bromley, Beckenham, Orpington, Petts Wood, Hayes, Chislehurst and Penge. Directories (Checkatrade, TrustATrader, Which?, Yell) were excluded. 32 sites; 29 loaded (one blocked bots with HTTP 418, one returned 401, one timed out).
- **Validation:** detection was checked on vendor sites. Tidio, Crisp, tawk.to, LiveChat, Intercom, Smartsupp and Chatbase were all detected. JivoChat was missed at first, the signature was fixed, and it's now detected (`../tools/scan-results/vendor-controls-*`). Six trade sites were also checked by hand through their full third-party request list: no chat vendor appeared, only analytics, reviews (Trustindex, Trustpilot) and Elfsight.

| # | Business | Site | Chat / bot | WhatsApp | Booking | Form | Mobile | Tap-to-call |
|---|---|---|---|---|---|---|---|---|
| 1 | DRMB Plumbing & Heating | drmb-plumbing.co.uk | none | yes | — | yes | yes | yes |
| 2 | CityFix Ltd | cityfixltd.co.uk | none | — | — | yes | yes | yes |
| 3 | Plumber Bromley (BR1) | plumberbromley.co.uk | none | — | — | yes | yes | yes |
| 4 | 1st Plumbers | 1st-plumbers.co.uk | none | yes | — | yes | yes | yes |
| 5 | SR Francis | plumbersbromley.co.uk | none | yes | — | no | yes | yes |
| 6 | Homecure Plumbers | homecureplumbers.co.uk | none | — | — | yes | yes | yes |
| 7 | JRS Group | jrs-group.co.uk | none | yes | — | yes | yes | yes |
| 8 | Peter Whiting Electrical | peterwhitingelectricalcontractors.co.uk | (blocked, HTTP 418) | — | — | — | — | — |
| 9 | S Cloud Electrical | scloudelectricalservices.co.uk | none | — | — | yes | yes | yes |
| 10 | Bromley Electrical | bromleyelectrical.com | (timed out) | — | — | — | — | — |
| 11 | LTS Electrical | ltselectrical.co.uk | none | — | — | yes | yes | yes |
| 12 | First Rate Roofing | firstrateroofingltd.co.uk | none | — | — | yes | yes | yes |
| 13 | Bexley & Bromley Roofing | bexleyandbromleyroofing.co.uk | none | — | — | yes | yes | no |
| 14 | MK Landscape and Design | mk-landscapes.com | none | yes | — | yes | yes | yes |
| 15 | NE Gardencare | negc.co.uk | none | — | — | yes | yes | yes |
| 16 | Elitescapes | elitescapes.co.uk | none | — | — | yes | yes | yes |
| 17 | Prestige Landscaping | prestige-landscaping.co.uk | none | yes | — | yes | yes | yes |
| 18 | Terra Firma Landscapes | terrafirmalandscapes.co.uk | none | — | — | yes | yes | yes |
| 19 | Fine Landscaping | finelandscape.co.uk | none | yes | — | yes | yes | yes |
| 20 | MA Construction & Landscaping | maconstructionandlandscaping.co.uk | none | — | — | yes | yes | yes |
| 21 | Crown Paving | crownpavingltd.co.uk | none | — | — | yes | yes | yes |
| 22 | Beckingham Block Paving | beckinghamblockpavingltd.co.uk | none | — | — | yes | yes | yes |
| 23 | Kent Tree Care | kent-treecare.co.uk | none | — | — | yes | yes | yes |
| 24 | Bromley Tree & Garden Care | btgc.co.uk | none | — | — | no | yes | no |
| 25 | JJ&B Tree Care | jjandbtreecare.co.uk | none | yes | — | yes | yes | yes |
| 26 | BR2 Locksmith Hayes | br2locksmithhayes.co.uk | none | — | — | no | yes | yes |
| 27 | SJ Locksmiths | sjlocksmiths.com | none | yes | — | yes | yes | yes |
| 28 | The Key Locksmith | thekeylocksmith.co.uk | none | — | — | no | yes | yes |
| 29 | Splat Decorating | splatdecorating.com | (HTTP 401) | — | — | — | — | — |
| 30 | Addspace Building | addspacebuilding.co.uk | none | — | — | yes | yes | no |
| 31 | PJ Dunbar Builders | pjdunbarbuildersltd.com | none | — | — | yes | yes | yes |
| 32 | CS Lofts | cs-lofts.co.uk | none | yes | — | yes | yes | yes |

**Results (29 loaded):**

| Measure | Count | % |
|---|---|---|
| No live chat or AI bot | 29/29 | **100%** |
| No online booking tool | 29/29 | **100%** |
| No chat, bot, WhatsApp **or** booking | 19/29 | **66%** |
| Has a WhatsApp button | 10/29 | 34% |
| No contact/quote form found | 4/29 | 14% |
| No tap-to-call link | 3/29 | 10% |
| No mobile viewport / not HTTPS | 0/29 | 0% |

**How to read it:**
- This sample is **biased toward better sites**: they ranked in web search, and businesses with no website weren't included. The share of gaps across a full Maps pull will be the same or higher; P1 measures it.
- Every site is mobile-ready, and nearly all have a form and tap-to-call. So "your website is broken" isn't the pitch here. The universal gap is **nothing answers when the owner can't**.
- WhatsApp users (34%) are a segment for a later WhatsApp version.

## 10. The secondary stream: sell the scanner or the data?

| Route | Evidence | Verdict |
|---|---|---|
| Nico-style lead site ($35/month credits, `50iWtrj9Mkw`: "3500 bucks in monthly recurring revenue" after "like 7 months", word of mouth, his claim) | One anecdote; it resells Google Maps data (the ToS risk in §8); UK buyers are agencies and cold callers who face PECR | **Not now.** Reconsider only if 3+ agencies ask for your lists |
| **Apify pay-per-event actor:** "UK trade website gap scanner" (input: a URL list; output: chat/booking/WhatsApp/form flags) | Apify keeps **20%** and deducts platform costs from PPE payouts; rentals retired 1 Oct 2026 (docs.apify.com … monetize). It doesn't touch Google data, so it's low-risk. No transcript or Apify figure shows typical developer earnings. | **Cheap week-5 probe:** publish it in ~3 h [E] at a few dollars per 1,000 sites [E]. Kill if under 10 outside users in 30 days |

The Docsbot founder's tip, "use BuiltWith or things like that… here's all the websites that are using this Help Scout widget… there's your niche right there" (`22Jpzt683jw`), and theirstack.com ("like built with, but it's much cheaper", `vB08-7RzgOs`) are the paid versions of this scanner. At Bromley scale you don't need them.

## 11. Metrics (`plans/funnel-missedcall.csv`)

- **Prospecting:** scanned · gap % · Ltd % · TPS-clear %
- **Outreach:** contacted by channel (call/voicemail/card/email) · **unanswered %** · demo-line calls · conversations · hot leads
- **Pilots:** pilots · missed calls caught per pilot · reply rate to texts · real enquiries logged
- **Revenue:** pilot → paid % · MRR · churn
- **Costs:** cost to serve per client · support minutes · cash per paying customer
- **Learning:** reasons for "no"

## 12. Budget (6 weeks, GBP)

| Item | £ |
|---|---|
| ICO fee (skip if already paid for the websites test) | 52 (47 by direct debit) |
| Postcards: 40 (P3) + 40 (week 3) × ~£0.90 | ~72 |
| TPS/CTPS screening (Data Soap 200 checks) | ~5–10 |
| Twilio: 2–3 UK mobile numbers × 2 months + test SMS/voice | ~20 [E] |
| Voice platform testing (Retell/Vapi) | ~10 [E] |
| LLM tokens | ~5 [E] |
| Hosting, Outscraper/Apify free tiers, Companies House, Stripe (no fixed fee) | 0 |
| Domain for the privacy page and demo | ~10 [E] |
| **Total** | **≈ £175 (≈ £125 if the ICO fee is already paid); cap £300** |
