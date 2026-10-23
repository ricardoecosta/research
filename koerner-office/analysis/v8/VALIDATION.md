# v8 validation (METHOD step 10: high-effort, web-checked)

Run 23 Oct 2026 (UK time) by Grok Bot (Researcher), under the METHOD.md FALLBACKS rule: Claude Opus is out until 5:20pm BST, so Researcher runs the validation itself with live web checks. Every verdict below rests on pages fetched today (WebSearch/WebFetch, Atlassian Marketplace REST, App Store pages, GOV.UK). Codex wasn't used for drafting. Under the EFFICIENCY rules, nothing here comes from a cheap-token pass.

**Scope:** the 15 ranked clusters in `TOP_SLICE.md` plus the 20 scout records in `scouts/scouts.jsonl`.

**Not in scope:** the 5 most-cited clusters (C0001–C0005). The parent run excluded them because each already breaks at least one hard constraint (local selling, physical work, hours, PECR), and those rule kills stand. They were not re-web-checked here. METHOD step 11 asks for a web-checked kill reason for them, so this is a recorded gap.

**Rules applied (RULES_LOCKED.md):**
- **Staleness:** claims older than 18 months, or that rest on a tool, price or platform, were rechecked live.
- **Moat check, applied extra hard:** how fast can a competitor or the platform copy it? We counted live competitors and launches in 2026.
- **UK PECR:** banned cold channels (SMS, WhatsApp, DMs or email to individuals and sole traders) can't be relied on.
- **Ricardo's hard constraints:** high automation, 5 h/week or less, no selling to local businesses, no face or personal brand.
- **"Unverified"** marks any figure we couldn't confirm.

**Verdict key:** **pursue** = passes the gate. **Maybe** = passes the rules, with named open questions that would decide it. **Kill** = fails, with the reason.

This file is the step-10 output. It is not a final shortlist.

## Summary

**Result: 0 pursue, 2 maybe, 33 kill.** No candidate passes the gate outright. The two maybes each need a cheap, named test before any build.

| Candidate | Verdict | Confidence | Key evidence (live, 23 Oct 2026) | Biggest risk |
|---|---|---|---|---|
| C1143 One-time downloadable software | Kill | High | The "$4k/mo" claim is Rob Walling's 2005 DotNetInvoice purchase; no niche named | ~20-year-old evidence |
| C0215 Claude/AI skill bundles | Kill | Medium | Anthropic directory is free-only; skills are copyable markdown | Needs an audience; no moat |
| C2350 Encrypted file vault | **Maybe** | Low | Voltaire about $40k/mo (AI-compiled, unverified); 9 of 72 vault apps make >$20k/mo | Only 1 new entrant in 18 months broke in ($5–10k); data-loss liability |
| C2242 Social posting API | Kill | Medium | Post for Me at $10/mo vs Upload-Post, Zernio, Ayrshare and others | Price war and platform API control |
| C0899 Weekly competitor-ad reports | Kill | High | Rival Ads does it for $29/mo; the $300 price was hypothetical | Already productised |
| C2253 Community analytics app | Kill | Medium-high | Statbot, ServerLens and free Discord Insights; source says it "never took off" | Commoditised |
| C2446 QR ordering for print vendors | Kill | High | 6+ live competitors (Vixie, ReadyPix, PrintBooth…) | Moat fails |
| C2354 AI paraphrase app | Kill | Medium | QuillBot plus built-in rewrite tools; "bypass detection" use case | Commoditised feature |
| C0168 Niche search utility sites | **Maybe** | Low-medium | AI Overviews cut clicks 40–58%, but tool queries are least exposed | Google's generated tools; revenue unmeasured |
| C1091 Company funding alerts | Kill | High | Crunchbase bans scraping; UK SH01 trackers already exist | Legal and crowded |
| C1124 Developer boilerplate | Kill | High | ShipFast down from $126k/mo to ~$2k/mo; 248 boilerplates | Agents generate scaffolds |
| C1145 Star-naming registry | Kill | Medium | Crowded; no official recognition; misleading-claims law | Consumer-protection risk |
| C0131 AI social video accounts | Kill | High | YouTube's Jul 2026 demonetisation of templated AI content | Platform policy |
| C0174 Custom AI portraits | Kill | Medium | Etsy allows it with disclosure; buyers can self-serve with free AI | Fad and commoditised |
| C1037 YouTube review cross-posting | Kill | High | Needs an Amazon Influencer video library; tool costs $20/mo | Breaks rules (physical, face or voice) |
| SC01 Edge MV2 orphan replacements | Kill | Medium-high | Top MV2 extensions migrated or vendor-owned; tail averages ~2.4k installs | No payers |
| SC02 Premium Bonds checker | Kill | Medium | New NS&I app (2025) plus text and email prize alerts | No willingness to pay; trademark |
| SC03 Octopus tariff companion | Kill | Medium-high | OctoTracker and Octopus Compare moved to the web; free API | Apps don't pay |
| SC04 FreeAgent connector layer | Kill (watch) | Medium | Equali is FreeAgent's official partner (help centre, 20% off) | Official partner owns distribution |
| SC05 Google Chat for Jira replacement | Kill | Medium-high | Incumbent is Google's free app; free Advanced alternative; new Chatpane (16 Oct 2026) targets the exact complaints | Competing against free; copied already |
| SC06 Harvest for Jira | Kill | High | 9 Harvest apps live | Moat fails |
| SC07 Orphaned Atlassian integrations | Kill | Medium | Copying confirmed again (Chatpane, InVision) | Fast copying |
| SC08 Better Mermaid for Confluence | Kill | High | 107 matching apps | Crowded |
| SC09 Stripe/PayPal→Xero fix | Kill | Medium | Complaints target Stripe and Xero, not features (not re-fetched) | Not addressable |
| SC10 Xero export/archive | Kill | High | Boxkite $49, Xportmydata $120, Numerint | Served |
| SC11 Smart-meter companion | Kill | High | Bright app is free with DCC data | Free incumbent |
| SC12 Tide times successor | Kill | High | My Tide Times 4.8★; EasyTide free | Served |
| SC13 UK digital templates | Kill | Medium | Gumroad "uk landlord" 8 products, 0 ratings | No demand, no moat |
| SC14 Productised automation gig | Kill | High | It's a service | Breaks rules (hours, automation) |
| SC15 UK inspection SaaS | Kill | High | FireCert ~$4.5k MRR is real | Breaks rules (local trades, sales) |
| SC16 HubSpot UK→Xero sync | Kill | Medium | Funded connectors (not re-fetched) | Crowded |
| SC17 Companies House software filing | Kill | Medium-high | **Date is 1 Apr 2028**; P&L filing paused (GOV.UK, 23 Oct 2026); £5–£20 floor | Commodity plus liability |
| SC18 WordPress abandoned-plugin successors | Kill | Medium | Maintained alternatives (BackWPup, UpdraftPlus) | Support hours |
| SC19 Gift Aid WP plugin | Kill | High | Tinwell, Donor Merchant, Charitable, Sky Gift Claim | v7 gap has closed |
| SC20 Click & Drop sync (benchmark) | Kill | High | MakePost (7 Oct 2026), Postbag (24 Sep 2026) | Copied in weeks |

## Cross-cutting findings

1. **The moat check killed most of these.** In 2026, every live gap we rechecked already had a recent copy:
   - Chatpane, released 16 Oct 2026 for Google Chat in Jira
   - MakePost, launched 7 Oct 2026 for Click & Drop sync
   - Harvest for Jira, now 9 apps
   - Mermaid for Confluence, now 107 apps
   - seed-phrase vaults, with several recent apps

   The Forge 0% revenue-share incentive and coding agents make clones nearly free.
2. **Two scout gaps have closed since v7:**
   - Gift Aid on WordPress now has at least 4 suppliers.
   - FreeAgent has an official e-commerce partner, Equali.
3. **Scoring quirk to fix in Part 2:** first-hand revenue claims lifted old or failed anecdotes to the top. C1143 is a 2005 acquisition, and C2253's own guest says the app "never really took off". The scorer should check how old the event behind a claim is, not just the video date.
4. **Companies House:** software-only accounts filing is confirmed for **1 April 2028**. Today GOV.UK also paused the requirement for small and micro companies to file P&L accounts. Abridged and filleted accounts remain.
5. **Not covered:**
   - The 5 most-cited clusters (rule kills; see the scope note).
   - SC09 and SC16 were not re-fetched.
   - Install counts for Chatpane aren't shown publicly.
   - App Store guideline specifics for security apps weren't rechecked.
## Part A: transcript clusters (top 15)

### C1143: One-time downloadable software. **Kill**, confidence high
- **Source claim rechecked:** the transcript (4IETgMZy1o0, The Koerner Office, Sep 2025) says: *"I went and acquired… a software product, but it was pre-SaaS because it was only one time download… that got up to like $4,000 a month."* The speaker, "Rob", is almost certainly Rob Walling describing DotNetInvoice, which he bought in 2005 for $11k ([robwalling.com, 2007](https://robwalling.com/essays/2007/09/16/inside-story-small-software-acquisition-1-of-3); [Startups for the Rest of Us #525](https://www.startupsfortherestofus.com/episodes/episode-525-a-bootstrapping-artifact-from-2005)). Matching the speaker to Walling is our inference, not confirmed in the transcript.
- **Staleness:** the video is from 2025, but the evidence itself is roughly 20 years old. The cluster names no niche, no customer and no channel.
- **Why kill:** this is a historical anecdote, not a current opportunity. The scorer ranked it #1 only because a first-hand revenue figure was attached. That is a scoring quirk worth fixing in Part 2: down-weight first-hand claims when the event they describe is old.

### C0215: Claude and AI skill bundles. **Kill**, confidence medium
- **Platform rechecked:** Anthropic's directory lists plugins and MCP servers for free, and has no paid listings or payouts ([Claude docs](https://claude.com/docs/directory/publish); [Claude Code plugins](https://code.claude.com/docs/en/plugins/publish)). Paid sales would have to go through third-party marketplaces such as Agensi or SkillHQ ([Agensi comparison](https://www.agensi.io/learn/ai-agent-skills-marketplace-comparison-2026); [SkillHQ](https://skillhq.dev/)). Their traction is unverified.
- **Source context:** the strong video (quYKZushRPo, May 2026) sells skills to *his existing* SEO and newsletter audience. The second video (Sep 2026) is hypothetical.
- **Moat:** none. A skill is a markdown file, so a buyer can copy and share it instantly, and free skill repos are plentiful.
- **Why kill:** there's no paid discovery channel and no moat, and sales depend on an audience Ricardo doesn't have and can't build without a personal brand.

### C2350: Encrypted on-device file vault (Voltaire/Vaultaire). **Maybe**, confidence low
- **Source claim rechecked:** the founder is Rasty Turek. Starter Story's AI-compiled profile estimates about $40k/month in 2026, "triangulated from 6 public sources", not founder-verified ([Starter Story](https://www.starterstory.com/businesses/vaultaire)). A news write-up says $41k in one month ([biggo](https://finance.biggo.com/news/4873b81dd6555acd)). The transcript says $2–3k/day after about 6 months. Pricing is $1.99/week, $19.99/year or $39.99 lifetime, and lifetime brings in more than 80% of revenue. The revenue is plausible, but it is one outlier and not independently verified.
- **Demand:** real. Appaloma (Sep 2026) counts 72 photo-vault apps; 9 make over $20k/month, and the top two earn $250k+ ([Appaloma](https://www.appaloma.com/research/photo-vaults)).
- **Moat (extra-hard):**
  - The leaders have held the top spots since 2011 and 2012.
  - Only **one** app launched in the last 18 months made Appaloma's catalogue, and it sits in the $5–10k band.
  - The crypto seed-phrase angle Voltaire's SEO targets ([its guide](https://vaultaire.app/guides/store-crypto-seed-phrase-iphone/)) already has several recent apps: SafeVault, Syfra, LockSeed and Sealby ([SafeVault](https://apps.apple.com/us/app/safevault-offline-storage/id6763192087), [Syfra](https://apps.apple.com/us/app/syfra/id6754493673)).
  - Once users store data, switching costs keep them. That favours incumbents, and a newcomer would need to beat them on SEO or ASO.
- **Risks:**
  - The top 1★ themes are data lost on a new phone and lifetime purchases turned into subscriptions (Appaloma). One data-loss bug means refunds and reputational damage.
  - Security-sensitive apps are reviewed harder under App Store guidelines (not rechecked today).
  - Copycat rejections under App Store guideline 4.3 are a risk for a me-too vault.
- **Agent-runnability:** high once it's built. SEO guides and ASO can be agent-written. Support for lost data can't be automated away.
- **Build effort:** about 2–4 weeks for a native iOS app with on-device encryption, export and tests (estimate).
- **Realistic revenue:** most new vault apps never reach the $5k/month catalogue floor. The only recent entrant that did sits at $5–10k/month peak. Voltaire's ~$40k/month is the outlier.
- **What would decide it:**
  1. A 1-day ASO and keyword check, for example "ID document vault UK" or "seed phrase vault": does a cluster exist where the top 10 are weak or dormant? Appaloma found 18 of 72 apps dormant.
  2. Whether Ricardo is comfortable owning data-loss liability, mitigated by an on-device-only design with mandatory encrypted export.
  3. Finding Voltaire's actual keyword wins, for example with AppTweak or Sensor Tower, before copying the SEO playbook.

### C2242: Social posting API. **Kill**, confidence medium
- **Source claim rechecked:** the product is Post for Me (postforme.dev, DayMoon Development). It charges $10/month for 1,000 posts, rising to $1,000/month for 200k ([pricing](https://www.postforme.dev/pricing)). The 5K MRR milestone on 8 Apr 2026 is the founder's own Twitter claim from the transcript; unverified.
- **Competition (live):** Upload-Post ($16–24/mo), Ayrshare ($149+/mo), Late (now Zernio, $6 per account), PostPeer, SkedCast, Blotato and others ([Upload-Post comparison](https://www.upload-post.com/pricing-comparison/); [PostPeer](https://www.postpeer.dev/blog/best-social-media-posting-apis); [SkedCast vs Post for Me](https://skedcast.com/alternatives/post-for-me)).
- **Platform risk:** every network (X, Meta, TikTok, LinkedIn) controls API access and app review and can change its terms. Developer support load is high.
- **Why kill:** the source is itself the $10 price leader in a crowded race to the bottom. It grew on a founder-led Twitter build-in-public channel, which counts as a personal brand.

### C0899: Weekly competitor-ad reports. **Kill**, confidence high
- **Staleness:** the video is from Apr 2025 (stale), and its $300/month price is hypothetical.
- **Rechecked live:** the exact product already exists for much less. Rival Ads charges $29/month for 2 competitors, with a weekly email digest and AI strategy notes ([Rival Ads](https://www.rivalads.io/pricing)). Panoramata starts at $99/month for 20 competitors ([Panoramata](https://www.panoramata.co/pricing)) and Foreplay at $175/month ([Foreplay](https://www.foreplay.co/pricing)). Atria lists 14 tools ([Atria](https://www.tryatria.com/blog/competitive-ad-tracking)).
- **Why kill:** it's already productised at about a tenth of the proposed price. Selling to businesses would also mean cold outreach, which PECR limits to limited companies.

### C2253: Community analytics app. **Kill**, confidence medium-high
- **Source:** the transcript (LrLDsvbdPr0, Oct 2026) is a low-quality Whisper transcription. The product name "Meatwaves" is unverified, and the guest says it *"never really took off"*. His real business is a speech-to-text app.
- **Competition (live):** Statbot ($8.97–14.95/mo), ServerLens ($1.99/mo), and Discord's own Server Insights, free for servers with 500+ members ([ServerLens](https://serverlens.co/blog/best-discord-analytics-tools-2026)). Skool has Grow Your Skool at $29–49/mo ([site](https://growyourskool.com/)).
- **Why kill:** the market is commoditised and has a free native option. Even the source says it failed.

### C2446: QR ordering software for event print vendors. **Kill**, confidence high
- **Moat check fails:** at least six live competitors do exactly this: NINEMAGS Live, Vixie, ReadyPix, PrintBooth, MagFlow and MagnetSnap ([Vixie](https://vixie.app/), [ReadyPix](https://readypix.co/), [PrintBooth](https://printbooth.co/), [MagFlow](https://www.magflowme.com/), [NINEMAGS](https://ninemags.com/)).
- **Buyers:** small, mostly US event vendors reached through Facebook groups. The source founder had her own audience of kit buyers.

### C2354: AI paraphrase app. **Kill**, confidence medium
- **Source claim:** the transcript (t9yFAJzsOkE, Jun 2026) says *"paraphrase… making about $2600 a month"* (unverified). The stated use case includes making ChatGPT text *"bypass"* AI detection.
- **Competition:** QuillBot's iOS app costs $19.99/mo or $99.99/yr. Its revenue estimates conflict: $150k/mo per screensdesign versus $618/mo per Bumetric ([screensdesign](https://screensdesign.com/apps/quillbot-ai-writing-keyboard/); [Bumetric](https://bumetric.com/revenue/quillbot-ai-writing-keyboard)). Small dedicated paraphrase apps report about $1–3k/mo (e.g. [Paraphrase AI GTM](https://gtmsauce.com/companies/paraphrase-ai)). Rewriting is also built into general assistants and into OS-level writing tools (the iOS writing-tools point is from our own knowledge, not rechecked today).
- **Risks:** pitching "bypass AI detection" invites academic-integrity backlash and possible App Store rejection (not rechecked).
- **Why kill:** it's a commoditised feature with OS-level substitutes, and the source's edge was keyword timing that has now passed.

### C0168: Niche search utility sites (tools, not articles). **Maybe**, confidence low-medium
- **Staleness:** the strongest first-hand claim, $10–20k/month from AdSense exact-match-domain sites by **2011**, is 15 years old, so it's stale and not evidence. The word-unscrambler's "$5–6M/year" is a second-hand estimate (unverified).
- **Search shift rechecked:**
  - In a randomised field experiment, AI Overviews cut outbound organic clicks by 39.8% when shown ([SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6513059)).
  - Ahrefs measures a 58% lower CTR in position 1 ([Ahrefs](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/)).
  - Tool and calculator queries are the least exposed: one *modelled* estimate puts the loss at 6%, against 53% for definitions ([snowballr, modelled](https://snowballr.io/research/ai-mode-vs-calculator-publishers-10000-scenarios)).
  - Google's generated interfaces are starting to compete with tool pages directly ([SEJ](https://www.searchenginejournal.com/googles-generated-interfaces-could-compete-with-tool-pages/586589/); [SEW](https://searchenginewatch.com/google-is-coming-for-the-free-tools-small-websites-depend-on/)).
- **Fit:** good. It needs no face, no outreach and no local selling. Agents can build and maintain tools, and Ricardo is technical.
- **Moat:** weak. Any tool can be cloned. The only defensible version uses proprietary or UK-specific data and logic that a generic generated interface can't reproduce, for example UK rules engines and calculators.
- **Realistic revenue:** unverified. We found no current, sourced RPM or traffic figure for a comparable UK tool site today. Treat as £0–low hundreds a month for the first year until measured.
- **What would decide it:**
  1. Pick 3 UK tool queries with measurable volume, then check the live SERP for whether an AI Overview or generated tool appears and how strong the competing tools are.
  2. Ship one tool and watch Search Console impressions and clicks for 8 weeks.
  3. Kill if clicks after 8 weeks don't support at least £100/month at measured RPM.

### C1091: Company funding alerts. **Kill**, confidence high
- **Legal and platform:** Crunchbase's terms ban scraping ([ToS](https://about.crunchbase.com/terms-of-service)), and the free Basic API is retired ([docs](https://data.crunchbase.com/docs/crunchbase-basic)).
- **UK variant (Companies House SH01 filings, lawful and free data):** already served by Funding Spotter ([site](https://www.fundingspotter.com/)), CompanyTrack ([site](https://companytrack.com/for/investors)), Tero and InvestorUniverse ([site](https://www.investoruniverse.uk/funding)), plus Fundz, Dealroom and Beauhurst.

### C1124: Developer software boilerplate. **Kill**, confidence high
- **Benchmark rechecked:** ShipFast went from $0 to $126k/month and back down. Marc Lou reports about $2k/month in 2026 ([Marc Lou](https://newsletter.marclou.com/tweets/shipfast-went-from-0-mo-to-126-000-mo-then-back-down)).
- **Crowding:** there were 248 boilerplate submissions, 94 of them in 2026 by mid-October ([BoilerplateHub](https://boilerplatehub.com/blog/state-of-saas-boilerplates-2026)).
- **Why kill:** coding agents now generate scaffolds on demand, and distribution depends on a dev-Twitter personal brand.

### C1145: Star-naming registry. **Kill**, confidence medium
- **Competition:** crowded (star-register.eu, AstraName, International Star Registry and more), and no naming is officially recognised ([AstraName explainer](https://astraname.com/is-naming-a-star-real); [SMSU FAQ](https://www.smsu.edu/campuslife/attractions/planetarium/starnamingfaq/index.html)).
- **Legal:** consumer-protection risk around "official" or "registered" wording. ISR faced a New York deceptive-advertising action in 1998 ([archive](https://web.archive.org/web/20060111052632/http:/www.naic.edu/~gibson/starnames/isr_news.html)). In the UK, the DMCC Act 2024 lets the CMA fine directly for misleading practices. No ASA ruling was found (unverified).
- **Source:** the "made millions" claim is second-hand.
- **Why kill:** it's a commodity novelty gift that depends on paid ads, and it's ethically thin.

### C0131: AI-generated social video accounts. **Kill**, confidence high
- **Platform rechecked:** YouTube (13 Jul 2026) spelled out that generic, repetitive, templated or mass-produced AI content can't be monetised ([Tubefilter](https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/); [TechCrunch](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)). A fully agent-run channel is exactly the pattern that policy targets.
- **Source:** the cited Higgsfield "Earn" payouts are a tool vendor paying for its own promotion.

### C0174: Custom AI portrait downloads. **Kill**, confidence medium
- **Platform rechecked:** Etsy allows AI pet portraits made with your own prompts, provided AI use is disclosed ([Etsy](https://www.etsy.com/seller-handbook/article/1275449912004); [Etsy update](https://www.etsy.com/seller-handbook/article/1522733284810)).
- **Why kill:**
  - Buyers can now do this themselves for free in mainstream image models.
  - The source's own profile-picture business *"fad died off"*.
  - Custom orders mean revisions for every order, which costs hours.

### C1037: YouTube product-review cross-posting. **Kill (rules)**, confidence high
- **Rechecked:** the Cha-Ching Automate tool exists at $20/month or $200/year ([site](https://cha-ching-automate.averageguymakingmoney.com/)). YouTube's reused-content rule applies ([YouTube](https://support.google.com/youtube/answer/1311392)).
- **Why kill:** it needs an existing Amazon Influencer library of product-review videos, which means physical products and a creator on camera or on voice. The source says the uplift is only 5–10% on an operation that already exists.
## Part B: market scout leads (SC01–SC20)

### SC01: MV3 replacements for orphaned Edge/Chrome MV2 extensions. **Kill**, confidence medium-high
- **Rechecked live:** exstats (5 Sep 2026) counts 3,339 live MV2 listings on Edge with 85.6M installs. The 52 listings with 100k+ installs hold 90.7% of those installs. The other 3,287 listings hold 7.9M installs, about 2.4k each ([exstats](https://exstats.com/blog/mv2-purge-in-numbers)). Microsoft (7 Aug 2026) says 95% of the top MV2 extensions have already moved. By its count only 58 MV2 extensions have meaningful usage, and only 3 of those lack an MV3 version ([Edge blog](https://blogs.windows.com/msedgedev/2026/08/07/moving-the-microsoft-edge-extensions-ecosystem-forward-with-manifest-version-3/)). Enterprise switch-off runs Jan–Apr 2027 ([MC1467356](https://mc.merill.net/message/MC1467356)).
- **Demand:** Chrome is the precedent. After its purge the catalogue grew 44%, but total users stayed flat, and 70.8% of the removed extensions had fewer than 100 users (exstats). The large Edge orphans belong to vendors (Microsoft Purview, Cisco Webex, HP Dynamic Audio, bank Ukey extensions), so a third party can't replace them.
- **Moat:** none. Anyone can port an extension, and the window closes at the end of 2026.
- **Revenue:** no evidence that orphaned-extension users pay. Unverified.
- **Why kill:** the popular extensions have already migrated or belong to vendors, and each orphan in the long tail is too small to pay.

### SC02: Premium Bonds checker app (iOS first). **Kill**, confidence medium
- **Rechecked live:** the NS&I checker on iOS is 2.6★ from 1.4k ratings. It was last updated 28 Nov 2024 (v6.1.3) and sits at #122 in Finance ([App Store](https://apps.apple.com/gb/app/premium-bonds-prize-checker/id474172893)).
- **What changed:** NS&I launched a new main app in late 2025 that shows Premium Bonds prize history; it was updated Aug 2026 ([NS&I](https://www.nsandi.com/mobile-app)). NS&I already sends prize notifications by text and email ([NS&I corporate](https://nsandi-corporate.com/news-research/news/nsi-introduces-more-ways-whole-family-stay-touch-premium-bonds)). Android already has a 4.1★ third-party checker (scout record).
- **Risks:** "Premium Bonds" and NS&I are NS&I's marks, so expect App Store review and trademark trouble. The winning-numbers data is free, so the app is trivial to clone.
- **Revenue:** no evidence anyone pays for a prize checker. Unverified.
- **Why kill:** the official channel now covers the job, and nobody has shown willingness to pay. At most it's a weekend portfolio app, not a business.

### SC03: Octopus tariff companion (OctoTracker successor). **Kill**, confidence medium-high
- **Rechecked live:** OctoTracker's iOS app was last updated 25 Jun 2025 ([App Store](https://apps.apple.com/us/app/octotracker/id6463722470)). A LinkedIn post says "OctoTrack is now available as a web app". That looks like the same developer moving to the web, but the name match is unverified ([LinkedIn](https://www.linkedin.com/posts/vincent-tc-lee_oct-track-activity-7501962584661663744-81Xz)). Octopus Compare also dropped its app for a web version ([blog](https://octopus.compare/blog/welcome-to-octopus-compare-web)).
- **Moat:** none. The Octopus API is free and public, OctoDash and Octopus Watch are active, and Octopus's own app shows tariff prices.
- **Why kill:** two incumbents abandoned their apps for the web, which suggests the apps don't pay. This is the copy pattern again.

### SC04: FreeAgent connector layer (e-commerce settlements and missing Zapier actions). **Kill for now (watch)**, confidence medium
- **Rechecked live:** Equali is FreeAgent's official, help-centre-documented integration. It covers Shopify, Amazon, eBay and Etsy, has TikTok Shop and Facebook/Instagram due in 2026, and FreeAgent users get 20% off ([FreeAgent help](https://support.freeagent.com/hc/en-gb/articles/33737714948626-How-the-Equali-integration-works)). Equali's Shopify app has one review: 1★ on 22 Oct 2026, saying eBay settlements failed to post ([Shopify](https://apps.shopify.com/equali)). A2X, Link My Books and Synder still don't support FreeAgent ([foundationaltech](https://foundationaltech.co.uk/articles/a2x-vs-link-my-books-vs-synder-which)). Make already covers FreeAgent invoices (scout record).
- **Moat:** Equali holds FreeAgent's official listing and the discount, a distribution edge a newcomer can't match. Accounting correctness also brings support load and liability.
- **What would reopen it:** Equali falters, for example more 1★ reviews or a dropped listing, *and* FreeAgent agrees to list a second partner.
- **Why kill:** the gap is real, but it now has an officially endorsed owner.

### SC05: Google Chat for Jira Cloud replacement. **Kill**, confidence medium-high
- **Rechecked live (REST):** the incumbent is **Google LLC's own free app**. It has 11,005 installs, 924,125 total users, 2.30★ from 110 reviews, and its last release was 11 Nov 2021 ([REST](https://marketplace.atlassian.com/rest/2/addons/linovi-hangoutschat-bot); [versions](https://marketplace.atlassian.com/rest/2/addons/linovi-hangoutschat-bot/versions?limit=3)). 2026 reviews on Google's Workspace listing complain that you can't filter out your own actions and ask for one Chat thread per issue ([Workspace Marketplace](https://workspace.google.com/marketplace/app/jira_for_google_chat/1063804824442)).
- **Competitors (live):**
  - Advanced Google Chat for Jira (Move Work Forward): 406 installs, **free**, v4.5.0 on 13 Oct 2026 ([listing](https://marketplace.atlassian.com/apps/1233491/advanced-google-chat-for-jira)).
  - Canary Apps "Google Chat for Jira": 123 installs, updated Oct 2026.
  - Canary's automation actions: 3 installs, paid.
  - **Chatpane** (Brain Static Threads): a paid Forge app, v3.0.0 on 16 Oct 2026. Its pitch matches the 1★ complaints point for point: webhook setup, no Google sign-in, one thread per work item ([listing](https://marketplace.atlassian.com/apps/2126201930/chatpane-google-chat-notifications-for-jira)). It wasn't in this morning's scout data. Its install count isn't shown.
  - DIY: Jira Automation's "Send web request" can post to a Chat webhook for free ([Atlassian community](https://community.atlassian.com/forums/discussion/2568907/custom-google-chat-messages-through-automation)).
- **Economics:** Atlassian takes 0% of Forge revenue until $1M lifetime, then 17%. Connect apps pay 25% ([Atlassian](https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/)). The terms are favourable, but the competition is free.
- **Why kill:** a new entrant already targets the exact complaints and a competent free alternative exists, so a paid app would compete against free twice over. Google could also fix its own app at any time. The extra-hard moat check fails.

### SC06: Harvest for Jira replacement. **Kill**, confidence high
- **Rechecked live:** an Atlassian REST search for "harvest" returns 9 apps. The official app has 2,439 installs (2.53★ from 145), and the others are 42nd (375), Twin Sun (27), MarcelBag (9), Metronome (3), Appvibe (2) and Valandir (1). The moat fails, as the scout found.

### SC07: Orphaned Atlassian integrations (pattern). **Kill as a strategy**, confidence medium
- Copying was confirmed again today: SC05's best orphan already has a fresh competitor (Chatpane, Oct 2026) built around its complaints, and InVision drew 2 replacements (scout). The Forge 0% revenue-share incentive makes cloning cheap for everyone.

### SC08: Better Mermaid for Confluence. **Kill**, confidence high
- **Rechecked live:** an Atlassian REST search for "mermaid" now returns **107** apps; the scout's query found 84. Several are rated 4.0–4.6★ (for example Stratus, 6,223 installs, 4.02★; weweave, 2,181 installs, 4.58★).

### SC09: Stripe/PayPal-to-Xero fix. **Kill**, confidence medium
- Not rechecked beyond the scout's Xero pages. The complaints are aimed at Stripe and Xero themselves, and A2X etc. already cover reconciliation. Nothing a third party can fix.

### SC10: Xero data export and archive. **Kill**, confidence high
- **Rechecked live:** the market is served. Boxkite sells a $49 one-off export with attachments ([Boxkite](https://www.getboxkite.com/download-xero-data)), Xportmydata charges $120 one-off ([Xportmydata](https://www.xportmydata.com/single-download/)), and Numerint also exists ([Numerint](https://numerint.com/)).

### SC11: UK smart-meter data companion. **Kill**, confidence high
- **Rechecked live:** Hildebrand's **Bright** app is free and gives consumers half-hourly smart-meter data through the DCC ([App Store](https://apps.apple.com/gb/app/bright/id1369989022)), and n3rgy runs a consumer portal ([n3rgy](https://www.n3rgy.com/consumer/)). Data access is cheap for the incumbents and their apps are free.

### SC12: Tide Times UK successor. **Kill**, confidence high
- **Rechecked:** My Tide Times is rated 4.8★ on both stores ([App Store GB](https://apps.apple.com/gb/app/my-tide-times-tables-chart/id777280890)). ADMIRALTY EasyTide is free for 7 days ([UKHO](https://www.admiralty.co.uk/access-data/tidal-data/easy-tide)), and Tides Near Me uses UKHO data under the OGL ([source](https://tidesnear.me/data-sources)).

### SC13: UK-specific digital templates (Gumroad/Etsy). **Kill**, confidence medium
- **Rechecked live:** the Gumroad JSON for "uk landlord" still returns a total of 8 products. Supply is thin, but there is still no demand signal (0 ratings, per the scout). Etsy PLR bundles at £1.49–£1.65 would copy any winner. No moat.

### SC14: Productised spreadsheet/n8n automation gig. **Kill (rules)**, confidence high
- It's a service: client scoping and comms break the 50% automation and 5 h/week limits. Not rechecked; the rule kill doesn't depend on the market.

### SC15: UK statutory-inspection SaaS (FireCert/LolerFlow pattern). **Kill (rules)**, confidence high
- The revenue evidence here is the strongest of any scout (FireCert at about $4.5k MRR, Stripe-verified per [wlad.me](https://www.wlad.me/blog/companies/firecert)). But the buyers are local trade contractors reached through sales, which Ricardo has ruled out. Recorded so the reason is visible.

### SC16: HubSpot UK payments-to-Xero/QBO sync. **Kill**, confidence medium
- Carried from the scout, not re-fetched. Funded connectors (Invoice Stack, Synder, the native QBO integration) already serve it, and the demand evidence is one community post.

### SC17: Companies House software accounts filing for micro and dormant companies. **Kill**, confidence medium-high
- **Date resolved (GOV.UK, live):** software-only (iXBRL) accounts filing starts **1 April 2028**; the 2027 date is superseded. WebFiling and paper close for accounts, with no transition period ([GOV.UK guidance](https://www.gov.uk/guidance/using-software-to-file-your-companys-information)). The Written Ministerial Statement records the one-year postponement from April 2027 ([Hansard](https://hansard.parliament.uk/debates/GetDebateAsText/26060938000008)).
- **New today:** the 9 Jun 2026 news story was **withdrawn on 23 Oct 2026** and replaced. Small and micro companies will no longer have to file profit and loss accounts; that requirement is paused, and abridged and "filleted" accounts stay. The software mandate still goes ahead in April 2028 ([GOV.UK update](https://www.gov.uk/government/news/companies-house-update-to-accounts-filing-from-april-2028); [withdrawn notice](https://www.gov.uk/government/news/companies-house-to-bring-in-changes-to-accounts-filing-from-april-2028)). That makes the filing job simpler and pushes the market further toward cheap commodity tools.
- **Competition and price floor:** HMRC's free CATO service already closed on 31 Mar 2026 ([GOV.UK](https://www.gov.uk/guidance/closure-of-the-service-to-file-your-company-accounts-and-tax-return)). Dormant Return charges £5 ([site](https://dormantreturn.co.uk/)), SimpleCompanyTax £10+VAT, DormantFile £19 and TinyTax £20/yr ([TinyTax](https://tinytax.co.uk/pricing)).
- **Why kill:** the market is crowded at £5–£20/yr before the mandate even lands, and filing errors carry liability and support load.

### SC18: Successors to abandoned WordPress.org plugins. **Kill**, confidence medium
- **Rechecked:** BackUpWordPress's last release was Apr 2024 and its homepage now promotes UpdraftPlus, while BackWPup was still shipping updates in Oct 2026. WP Media says Heartbeat Control is still supported. Third parties already publish "abandoned plugin" lists for 2026 ([musthaveplugins](https://musthaveplugins.com/blog/abandoned-wordpress-plugins-2026-part-2/)). The large orphans have maintained alternatives, and support threads cost hours.

### SC19: Gift Aid plugin for small charities. **Kill**, confidence high
- **v7's "no dedicated plugin" claim is out of date.** Tinwell exports in HMRC's column order ([Tinwell](https://tinwell.org/gift-aid-wordpress/)), and Donor Merchant ([site](https://www.donormerchant.com/features/gift-aid/)), Charitable's Gift Aid extension ([site](https://www.wpcharitable.com/extensions/charitable-gift-aid/)) and the HMRC-listed Sky Gift Claim ([site](https://skywebdesign.co.uk/products/sky-gift-claim/)) all cover it too.

### SC20: Royal Mail Click & Drop sync on Shopify (benchmark). **Kill**, confidence high
- **Benchmark reconfirmed:** MakePost launched 7 Oct 2026 with a free plan and a $5.99/mo plan ([Shopify](https://apps.shopify.com/makepost)), and Postbag launched 24 Sep 2026 ([pickyourapp](https://pickyourapp.com/products/postbag)). Postly is established ([Shopify](https://apps.shopify.com/click-and-drop-integration)).
