# Hidden gems validation (Grok Bot, web-checked)

**Date:** 23 October 2026 (UK time). **Scope:** the top five gems in `HIDDEN_GEMS.md`, checked to the same standard as `TOP10_validation_opus_high.md`, plus a lighter web check of `TOP10_relaxed.md` #6 (inbound call and lead-response agent) and the AI automation agency (C0006), which the relaxed list left out.

**Method.** Each gem rests on one video, so I reread its mined note (`analysis/v7/transcripts/<id>.md`) and raw transcript (`transcripts/raw/<id>.txt`), took quotes verbatim from them, and then checked the founder, product, competitors, prices and legal points on the web on 23 October 2026. Quotes come from Whisper-tier transcripts, so they keep the transcript's wording and spelling. "My estimate" marks numbers that are mine and not sourced. Where the data or the web doesn't support a figure, I say "unknown".

**Scores.** Success is the chance, out of 10, of a real paying business within 12 months for a UK solo part-timer with no audience. Automation is the realistic share of recurring work that agents can do. Fit is fit for Ricardo, who is technical, based in Bromley, part-time, wants minimal involvement and finds local-business websites boring.

## Summary

| Gem | Verdict | Success | Automation | Fit | One-line reason |
|---|---|---|---|---|---|
| C1094 Encrypted on-device file vault (iOS) | **Validated with caveats**, only as a candidate niche inside the ASO app experiment | 3/10 | ~70% | 8/10 | Real product with public pricing, plus a reusable agent-run SEO loop. But the category is crowded (Keepsafe, Private Photo Vault, new vibe-coded entrants), and the founder is an ex-Google serial founder |
| C1098 AI support agent SaaS | **Not validated** as a new SaaS. The implementation variant folds into the automation-agency option | 2/10 (SaaS) | ~65% | 7/10 | DocsBot, Chatbase and Intercom Fin already sell this at $40–$499/month or $0.99 per outcome. DocsBot's founder says self-serve demand has shifted to agencies, and DIY now drives 13% of cancellations |
| C1095 Dictation app for seniors and disabled users | **Not validated** | 2/10 | ~55% | 5/10 | The source *is* the London incumbent in this exact niche (Voicy, $8.49/month, ~200 blog posts). Wispr Flow has a free tier and Windows and Apple dictation are free. Support for older users is human-heavy |
| C0467 Daily niche geography web games | **Not validated** | 2/10 | ~60% | 6/10 | Source creator has ~3.5M followers, a funded studio ($500k raised) and a 4-person team, and still writes the questions himself. 75–85% of the revenue is programmatic ads. The category is crowded |
| C0450 AI sports video analysis app | **Not validated** | 2/10 | ~45% | 4/10 | First month $17K, then "it started fizzling" to ~$500 MRR. Seasonal, relies on creators and ads, and was removed by Apple once. Several clones and rivals already exist |

**Bottom line.** None of the five gems justifies its own track. Only the vault app survives, and only as one keyword cluster to test inside the existing ASO single-app experiment (strict #1). What is worth keeping from the gems is two *methods*, not the products:
1. **The Vaultaire agent-run SEO loop.** Each morning an agent reads Search Console, finds pages with impressions but no clicks, and writes one high-quality guide. That suits the ASO app, the Shopify add-on's marketing site and the directory.
2. **Voicy's segment move.** Serve the neglected segment of a crowded category, where the product is "a painkiller" for them. That's a useful lens for the Shopify gap scan.

---

## 1. Encrypted on-device file vault iOS app (C1094)

**Verdict: VALIDATED WITH CAVEATS, as a candidate niche inside the strict list's ASO app experiment, not as a separate track.**
Success **3/10** · automation **~70%** · fit **8/10**

**Source.** `NuYO7DWzlaM`, "This app is making $2,000 PER DAY" (Starter Story, uploaded 18 Oct 2026). Evidence grade A in the mined note: the founder shows a revenue dashboard. The product is **Vaultaire** (transcribed "Voltaire"), by Rasty Turek (transcribed "Rastie Turek"). Third-party write-ups confirm the product and its pricing: [GTM Sauce episode page](https://gtmsauce.com/episodes/2026-10-18-this-app-is-making-2-000-per-day) and [Starter Story growth page](https://www.starterstory.com/businesses/vaultaire/growth-channels).

### Evidence for
- "The first month, it made $66, got a couple of downloads" and "It's currently averaging around $2,000 to $3,000 a day" (`NuYO7DWzlaM`).
- Lifetime purchases dominate: "I will say good 60% at this point, they also account for majority of the revenue, north of 80% I think. And then I just passed 60,000 overall downloads" (`NuYO7DWzlaM`).
- Pricing from the mined note, garbled by Whisper but matching GTM Sauce: $1.99/week, $19.99/year, $39.99 lifetime. Conversion is lowest on day 1, at 5.47%.
- The acquisition is agent-run and reproducible. "it runs through keyboard planner every single morning, looks at all the traffic, it identifies keywords that are being surfaced, but not essentially being driven to the site". It is also quality-capped: "you only do one article a day" (host, summarising the founder). The mined note says web traffic converts about 10% to the app.

### Evidence against
- **The founder isn't a newcomer.** He is a former Google engineer and serial founder who mentions selling a previous company ("sold that last year"), and he wrote his own open-source agent library ("I wrote this library called gum"). His six-month curve doesn't transfer to a first-time UK operator.
- **The category is crowded and has big, long-standing incumbents.** The founder's own framing is that he is taking on "really big competitor[s]". The mined note's risks list "Crowded category with large old competitors" and "Law-enforcement pressure on encryption apps".
- **New entrants are already copying the play.** Several new vault apps publish "best photo vault" SEO comparison pages, for example [ArkWarden](https://arkwarden.app/guides/best-photo-vault-apps-iphone), [YorkVault](https://yorkvault.com/compare/private-photo-vault-vs-keepsafe) and [Mavaul](https://mavaul.com/best-photo-vault-iphone/). That is the same SEO tactic, already contested.
- **Lifetime-heavy revenue means low recurring income.** The mined note says "Low MRR since most buy lifetime".

### Competitors (prices as listed, 23 Oct 2026)
- **Keepsafe:** Premium $9.99/month or $23.99/year, with a 200-item free cloud tier ([App Store](https://apps.apple.com/us/app/secret-photo-vault-keepsafe/id510873505), via [ArkWarden's comparison](https://arkwarden.app/guides/best-photo-vault-apps-iphone)).
- **Private Photo Vault:** one-time $39.99 upgrade. Cloud Vault is paid ([App Store](https://apps.apple.com/us/app/private-photo-vault-pic-safe/id417571834)).
- **Vaultaire** itself, plus newer local-encryption entrants such as ArkWarden.

### Legal and platform check
- **UK encryption climate.** Apple's Advanced Data Protection is still unavailable to new UK users ([Apple Support](https://support.apple.com/en-us/122234)). Apple's challenge to the replacement Investigatory Powers Act notice has a substantive hearing listed for December 2026 ([Privacy International](https://privacyinternational.org/legal-action/pi-apple-tcn-challenge), [Reuters, 17 Sep 2026](https://www.reuters.com/legal/government/uk-silence-over-demand-apple-data-access-is-farcical-lawyer-says-2026-09-17/)). Those notices target large providers, so a small on-device app with no server keys isn't the obvious target. The legal position still isn't settled, and Ricardo should get advice before adding any cloud backup or recovery feature. Encryption marketing claims must be exact.
- **Apple review.** Strict #1's risks apply in full: guideline 4.3 spam, review delays and the 84% submission surge. Encryption apps also need Apple's export-compliance declaration in App Store Connect (verify the current form). Vault apps can attract teens hiding content, so set a sensible age rating and avoid "hide from parents" marketing.
- **DMCC Act subscriptions.** The consumer subscription regime starts on **1 January 2027** ([Mills & Reeve](https://www.mills-reeve.com/publications/time-to-subscribe-to-the-detail-the-new-dmcca-rules/), [TLT](https://www.tlt.com/insights-and-events/insight/dmcca-subscriptions-regime-are-you-ready-for-1-january)). A lifetime-first price model reduces exposure. The weekly plan stays in scope.
- **UK GDPR.** If there is genuinely no server and no telemetry, exposure is minimal. Any analytics needs PECR consent controls.

### Is the single-source claim credible and transferable?
It looks **credible**: a dashboard was shown, pricing is public, and a third-party episode write-up exists. It is **not transferable** at that scale, because the founder's background and the six-month curve aren't a baseline for a first-time operator. The lesson that does transfer is the SEO loop plus lifetime pricing.

### Realistic 12-month revenue
**My estimate:** within strict #1's range of £0 to ~£6k, most likely under £1,500. This niche adds no reason to expect more, because the incumbents are entrenched and new SEO copycats exist. Upside beyond that is unknown.

### Cheapest test this week (~£79 Apple fee if no account; £0–50 tools)
Run it inside strict #1's keyword gate, using the same thresholds:
- Add about 20 vault, privacy and document-safe keywords to the 100-keyword mine.
- **Pass:** at least 3 vault keywords with popularity ≥30, ≤2 top-10 apps with the keyword in the title, and at least one top-10 app estimated at ≥$1k/month. As an extra check, at least 3 of the top-10 apps must have had no update in 12+ months, the "neglected incumbents" condition the founder relied on.
- **Fail:** any of those conditions misses. Drop vault as a niche and keep testing other keywords.

The Apple fee is £78.99/year according to a third-party UK guide ([Lola Squared](https://www.lolasquared.com/blog-apple-developer-account-price-uk)). Apple's own page states US$99, shown in local currency ([Apple](https://developer.apple.com/programs/)).

### Agent-run operating sketch
- **Agents:** keyword research; app build with CryptoKit on-device and no server; the RevenueCat paywall; App Store listing and screenshots; a daily Search Console loop that writes at most one guide a day; support triage. On "lost my pattern" requests, the agent answers "no recovery by design", backed by a clear warning at setup.
- **Ricardo, about 1–2 h/week after launch:** approve releases, check the security claims, handle Apple appeals.

---

## 2. AI support agent SaaS (C1098)

**Verdict: NOT VALIDATED as a new SaaS.** Success **2/10** · automation **~65%** · fit **7/10**

The *implementation* variant, building support bots for UK limited companies on an existing platform, isn't a SaaS. It is a narrow version of the AI automation agency (see the C0006 check below).

**Source.** `22Jpzt683jw`, Chris Koerner with Aaron Edwards, founder of **DocsBot** (evidence grade A).

### Evidence for
- "I think we got like 3 months we hit like 10k MR" and "We hit more than a million dollars uh in ARR" (`22Jpzt683jw`).
- Unit economics: "Our ARPU a revenue per p per user is I think like about 130 ... lifetime value ... it's a little over $2,000 ... our revenue churn is around 3%" (`22Jpzt683jw`).
- Agencies charge "roughly like around a $2,000 setup fee" and "As much as 500 bucks a month like like maintenance" (`22Jpzt683jw`).

### Evidence against
- **Self-serve demand is moving away from tools like this.** "most of our effort goes into like courting agencies and and implementers instead of like going directly after customers" (`22Jpzt683jw`). The mined note records "Self-serve demand dried up".
- **DIY is eating the market.** Cancellations to "I'll build my own" have gone "from like 1% ... to like about 13%" (`22Jpzt683jw`).
- **The early growth isn't repeatable.** The mined note says a Japanese tech influencer's repost brought ~3M views, and the founder launched early in the GPT wave. A newcomer in 2026 gets neither.
- **The strict validation already flagged this video.** It found that TOP10 misattributed this video's "10 grand in like two months" quote, which was about an AI profile-picture product, not DocsBot (`TOP10_validation_opus_high.md`, ASO section).

### Competitors (23 Oct 2026)
- **DocsBot:** Free; Personal $49, Standard $149 and Business $499 a month ([pricing](https://docsbot.ai/pricing)).
- **Chatbase:** Hobby $40, Standard $150 and Pro $500 a month ([pricing](https://www.chatbase.co/pricing)).
- **Intercom Fin:** $0.99 per outcome on top of seats from $19–$29 a month ([pricing](https://www.intercom.com/pricing), [outcomes](https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes)).
- Helpdesk-native AI from Zendesk and others. Not price-checked here.

### Legal and platform check
B2B SaaS is fine in the UK. Ricardo would need an Article 28 processor contract, and customer documents may contain personal data. Cold email would be limited to verified limited companies, under Ricardo's rule.

### Credible and transferable?
The claim is credible: specific ARR, ARPU, churn and margin figures, an incumbent you can name, and public pricing. It is **not transferable**. The window has closed, and the source's own founder is moving to the agency channel.

### Realistic 12-month revenue
£0 is the most likely result for a new general-purpose SaaS. Upside is unknown (my estimate).

### Cheapest test
None recommended as a SaaS. If Ricardo chooses the agency or implementation path, use the C0006 test below, built on DocsBot or Chatbase white-label rather than his own platform.

### Agent-run sketch
Not built out, because the idea isn't recommended.

---

## 3. Dictation app for seniors and disabled users (C1095)

**Verdict: NOT VALIDATED.** Success **2/10** · automation **~55%** · fit **5/10**

**Source.** `LrLDsvbdPr0`, "I built this app for my dad. Now it makes $18K/month" (Starter Story). The founder is Kourosh Ghaffari and the product is **Voicy** (transcribed "Voice C"/"Boise"), founded in London in 2024 ([Voicy about page](https://usevoicy.com/about/)).

### Evidence for
- "We're at 11K MRR. But on a monthly basis, we make anywhere from like 16 to 20K" and "usually our monthly plan is like $8.49" (`LrLDsvbdPr0`).
- A side project with a real segment insight. The founder serves people "who can't really type normally on their computers without any pain", and "20% of our users are on that disability discount" (`LrLDsvbdPr0`).
- SEO-led growth: "the true growth of voice C is from SEO ... We have like 200 blog posts. We have like 30 different landing pages. Our website is localized in like four or five different languages" (`LrLDsvbdPr0`).

### Evidence against
- **The niche already has a London incumbent.** Voicy is UK-based, two years ahead, and holds the SEO footprint, the Chrome Web Store reviews and a YouTube series. Starter Story reports the series grew from about 1,000 to 12,000 subscribers in roughly a month ([Starter Story growth](https://www.starterstory.com/businesses/voicy/growth-channels)). A newcomer would be copying a well-defended position.
- **The category is crowded and free options exist.** The founder himself says "Everyone and their mom has built one" ([transcript](https://exa.ai/library/podcast/18qshyvwdvt/episode/6w04nn0rqbz)).
  - Wispr Flow is free for 2,000 words a week on desktop; Pro is $15/month ([pricing](https://wisprflow.ai/pricing)).
  - Windows 11 Voice Access and Windows voice typing are free and built in ([Microsoft](https://support.microsoft.com/en-us/accessibility/windows/voice-access/dictate-text-with-voice)).
  - Apple Dictation and Voice Control come with every Apple device.
- **Support load is high.** The mined note's risks include "Seniors may need heavier support". The founder's support address says every message is read by a person ([Voicy about](https://usevoicy.com/about/)). That conflicts with minimal involvement.
- **The API dependency squeezes margins.** Lifetime deals at $260 carry open-ended Whisper API costs.

### Competitors
Voicy ($8.49/month), Wispr Flow (free / $15), the OS built-ins (free), and Dragon and others (not price-checked).

### Legal
- Audio is personal data, and could be special-category data where it reveals health conditions. That means UK GDPR care, a DPIA and a clear retention policy.
- Avoid making medical claims.
- The DMCC subscription rules apply from 1 Jan 2027.

### Credible and transferable?
Credible: a named founder, a public product and public pricing. **Not transferable**, because the gap it found is now taken by that founder in the same city.

### Realistic 12-month revenue
Unknown. £0 is the most likely result for a copycat (my estimate).

### Cheapest test
None recommended. Keep the *method*: look for the neglected, painkiller segment of a crowded category. Apply it in the Shopify gap scan.

---

## 4. Daily niche geography web games (C0467)

**Verdict: NOT VALIDATED for Ricardo.** Success **2/10** · automation **~60%** · fit **6/10**

**Source.** `s9aLA4IOSZE`, "I built this website in 8 hours with Claude. Now it makes $40K/month". The creator is Frank Michael Smith, with GeoGames, GeoSports, GeoHistory and GeoFooty ([geogames.co](https://www.geogames.co/)).

### Evidence for
- "We have about 700,000 monthly active users, and we make about $40,000 monthly" and "which is closer to $30,000, $35,000 in programmatic right now" (`s9aLA4IOSZE`).
- A built-in sharing loop: "We have a 53% organic share rate" (`s9aLA4IOSZE`).
- A cheap stack: "Claude Max, the 20X version ... Vercel Pro ... map Libre for the globe, upstashed Redis ... Google sheets for the questions and stripe for the pro subscriptions" (`s9aLA4IOSZE`).

### Evidence against
- **The audience and the capital came first.** "I've grown the audience now until report million followers across social media" (`s9aLA4IOSZE`).
  - Sportico reports more than 3.5M followers, Rhino Studios raising $500,000 at a $4M valuation, and a four-person team on GeoSports by late May 2026. Two earlier games "neither of which had garnered mainstream success" ([Sportico, 28 May 2026](https://www.sportico.com/business/tech/2026/geosports-trivia-game-creator-viral-wordle-1234901573/)).
  - A third-party breakdown credits the first-week spike to Barstool promotion ([Matt Cullerton analysis](https://www.mattcullerton.com/tokdocs/geosports-took-a-weekend-to-build-and-about-16-weeks-to-reach-40k-a-month-roughl/)).
- **Humans write the questions.** Sportico says Smith "maintained question-writing duties, since AI doesn't 'understand the pulse of the sports fan'". So the core content isn't agent-run.
- **Mostly ad income across three games.** By the same analysis, 75–85% of the $40K is programmatic ads, the figure covers the whole three-game portfolio, and it is gross, before four salaries.
- **Crowded and cloneable.** GeoSports is itself a remix of MapTap. Worldle, Globle, Travle and MapTap are established; MapTap sells MapTap+ at $2.99/month or $14.99/year ([comparison](https://borderline.world/geography-games-compared)).

### Legal
- Ad cookies need PECR consent through a consent banner.
- Sports content uses league and club marks and imagery, which raises IP risk.
- Don't cold-DM creators.

### Credible and transferable?
Partly credible: Sportico independently reported ~$47k ARR in subscriptions at about 1,000 Pro members. **Not transferable**: the distribution came from a creator with 3.5M followers and a funded studio.

### Realistic 12-month revenue
Unknown. £0 is most likely without a distribution asset. Web-game ad income needs very large daily player numbers (my estimate).

### Cheapest test (optional, only if Ricardo wants a fun side bet)
- Spend one weekend building a UK-niche daily game, for example London history geography, using original or OGL-licensed facts.
- Post it once in 3 relevant communities, following their rules.
- **Pass:** ≥1,000 total players in 14 days and ≥15% of day-1 players returning on day 7.
- **Fail:** either misses. Stop.

These thresholds are my own, not sourced. **Not recommended** for the plan.

---

## 5. AI sports video analysis app (C0450)

**Verdict: NOT VALIDATED.** Success **2/10** · automation **~45%** · fit **4/10**

**Source.** `oaXnY1YExjE`, "This Kid Found the Fastest Way to Make Money With AI Apps". George's **Wrestle AI** is live on the [App Store](https://apps.apple.com/us/app/wrestle-ai/id6751189075) at $9.99/month or $59.99/year.

### Evidence for
- "Wrestle AI the first month did 17K" (`oaXnY1YExjE`). Pricing: "10 bucks a month 60 for a year".
- Built without code on an AI app builder, so the build cost is low.

### Evidence against
- **It decays fast.** On an earlier app: "we got like 40,000 views ... And then it started fizzling out. And then from there we made like 500 bucks. It was like 500 MR". On Wrestle AI: "it was like 8K first week. Okay. 8K, six, four, two ... It had a huge up and then it's starting to fizzle" (`oaXnY1YExjE`).
- **Demand is seasonal.** "wrestling season ended" and "wrestling season is our best season" (`oaXnY1YExjE`).
- **Platform risk.** "They removed us for two weeks" (Apple, `oaXnY1YExjE`). The mined note also records a competitor threatening legal action.
- **Acquisition costs money.** It relied on paid creators and Meta ads. The mined note's automation score for acquisition is 2/5.
- **Crowded.** There are wrestling clones on the App Store, such as [Wrestle AI Coach & Trainer](https://apps.apple.com/lc/app/wrestle-ai-coach-trainer/id6755329359) and [Wrestling AI: Mat Coach](https://apps.apple.com/us/app/wrestling-ai-mat-coach/id6759972415). In combat sports there's JAB AI ([Google Play](https://play.google.com/store/apps/details?hl=en_US&id=com.limitnil.jabai)) and Cage Coach, mmaGPT and Fight AI ([overview](https://mmagpt.app/blog/best-ai-coaching-apps-combat-sports-2026)). In coach tools there's OnForm ([onform.com](https://onform.com/)).

### Legal
- Many users are minors, which brings the ICO Children's Code and consent for footage of other athletes.
- Weight-management advice for young athletes is a safety risk, flagged in the mined note.
- The DMCC subscription rules apply from 1 Jan 2027.

### Credible and transferable?
Credible as a short spike; the founder is candid about the decline. **Not transferable** as a durable business for a part-timer, and it depends on niche product judgement Ricardo would have to buy in.

### Realistic 12-month revenue
Unknown. A spike followed by decay is the documented pattern.

### Cheapest test
None recommended.

---

## Light check: relaxed #6, inbound call and lead-response agent for local UK firms (C0004 + C0139)

**Verdict: NOT VALIDATED as written; park.** Success **3/10** · automation **~50%** · fit **4/10** (local businesses, which Ricardo finds boring)

- **Productised UK rivals have pushed prices down.** Trade Receptionist sells this exact product to UK trades at **£49/£89/£159/£249 a month**, with a 14-day free trial and no contract ([tradereceptionist.com](https://tradereceptionist.com/)). Arcscribe starts from £24 + VAT ([pricing](https://arcscribe.co.uk/receptionist/pricing)), and Loyal Receptionist from £49 ([pricing](https://loyalreceptionist.co.uk/pricing)).
- **The relaxed test's price is out of line with the market.** UK agencies that publish prices for voice agents and AI receptionists show a median monthly starting price of **£250**, from 17 agencies ([TrustedAIAgencies, Oct 2026](https://trustedaiagencies.com/guides/uk-ai-automation-agency-prices-2026/)). The relaxed list's test asks for a **£150–£300 two-week pilot**, which is hard to win against £49/month SaaS with a free trial.
- **Most likely buyers are sole traders.** Many trades are sole traders, and under Ricardo's rule they can't be cold-emailed. That narrows outreach to limited companies, warm introductions or TPS/CTPS-screened calls.
- **Legal.** Inbound-only calls are largely outside Ofcom's nuisance-call focus. Callers must still be told about recording and transcription, and the business needs UK GDPR notices, retention rules and a DPA ([VoxSystems summary](https://voxsystems.ai/insights/uk-rules-for-ai-voice-calls), [Softomate summary](https://www.softomatesolutions.com/blog/gdpr-pecr-call-recording-ai-voice-agents-uk-2026/)). These are vendor blogs, so verify against ICO guidance before launch.
- **What could still work.** A higher-value vertical where a missed enquiry is worth hundreds of pounds and the buyer is a limited company with existing booking software, sold at the market's ~£250/month managed tier. That is really the automation-agency idea below, narrowed to one workflow.

## Light check: AI automation and implementation agency (C0006)

**Verdict: VALIDATED WITH CAVEATS as a human-in-the-loop option, outside the "agents run it" brief; park unless Ricardo opts in.** Success **4/10** · automation **~40%** · fit **5/10**

- **Catalogue evidence.** It is the most-cited idea in the set, at 14 videos, with success 89 but automation 49 (`ideas_scored.csv`). DocsBot's founder independently confirms that the money is in implementation, at about a $2,000 setup and $500/month (`22Jpzt683jw`).
- **The UK market is crowded but has published prices.** One directory lists **276 UK agencies**, and 107 of them publish prices. Medians: **£1,500** starting project, **£700** audit, **£297/month** plan; for AI chatbots, a **£175/month** median monthly plan ([TrustedAIAgencies, Oct 2026](https://trustedaiagencies.com/guides/uk-ai-automation-agency-prices-2026/)). Generic offers are commoditised. Narrow, outcome-specific workflows are the advised route ([same source](https://trustedaiagencies.com/guides/uk-ai-automation-agency-prices-2026/), [IdeaStack](https://www.ideastack.co/blog/how-to-make-money-with-ai-uk-2026)).
- **Why the success score is the highest here, but the idea is parked.** Services get a first paying client faster than products, but they need human sales and delivery. That breaks the minimal-involvement brief, and the 5-hour-a-week relaxed cap would be used up quickly.
- **Cheapest test, if Ricardo opts in.**
  - Pick one workflow: a docs-grounded support bot built on DocsBot or Chatbase white-label for UK SaaS or e-commerce limited companies.
  - Build 3 demo bots on public help-centre content.
  - Send compliant cold email to 30 verified limited companies, with an opt-out, plus warm intros.
  - **Pass:** at least 1 paid setup at ≥£750 within 21 days. **Fail:** none.
  - These thresholds are mine, anchored to the published medians above.

---

## Quote and source verification
- Every transcript quote above was taken verbatim from `transcripts/raw/<id>.txt` or `analysis/v7/transcripts/<id>.md`.
- Web sources were fetched or searched on 23 Oct 2026, and prices are as listed then. Third-party summaries (vendor blogs, comparison sites) are marked as such.
- Scores and revenue ranges are my own judgement wherever "my estimate" appears.
