# Missed Every Gold Rush? This One Started Just 2 Days Ago

- **Video:** [-Whqjr6ZnmY](https://www.youtube.com/watch?v=-Whqjr6ZnmY) · **Channel:** The Koerner Office · **Uploaded:** 2025-04-25 · **Length:** 29 min · **Transcript:** ok
- **Speakers:** Chris Koerner (host), Jacob Posel (guest) · **Format:** operator_interview
- **Evidence quality:** C — Speculative brainstorm on launch day; no revenue from any idea; Jacob has hands-on prompting experience but no business results stated. · Promotional conflict: Host promotes his newsletter tkopod.com.
- **Extraction:** grokbot · quotes verified 37/37

## Summary

Chris Koerner interviews Jacob Posel, an Australian AI builder in San Francisco, on the day OpenAI released its image generation API. They brainstorm consumer wrapper apps (Ghibli-style portraits, future-baby images, weight-loss visualiser, ageing), vertical uses (virtual staging, Airbnb photos, tree-trimming lead images) and, most deeply, AI ad creative: white-labelling high-volume ad variants for agencies or selling a $200/month tool to agencies via permissionless remade ads. Jacob shares reference-image prompting tips and says reliable viable-ad systems are still unsolved. Key takeaway: be ready to ship the moment a new capability drops, and target outputs that make customers money.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Focused consumer image-filter apps (Ghibli-me, anime-me)** — Wrap a viral ChatGPT image capability (e.g. Ghibli-style portraits) in a single-purpose app for non-technical people. | saas_software | deep | 4/5/5/5/4 | 5 |
| I2 | **'What would our baby look like' app** — Combine photos of two partners to generate an image of their future child. | saas_software | mention | 4/5/5/5/4 | 5 |
| I3 | **Weight-loss visualiser (rightsizeme.com)** — Show people what they would look like if they lost 30 pounds; Chris bought rightsizeme.com for $10 during the interview. | saas_software | mention | 4/5/5/5/4 | 5 |
| I4 | **Ageing / hairstyle / beard try-on app** — Show people what they will look like older or with different hairstyles or a beard. | saas_software | mention | 4/5/5/5/4 | 5 |
| I5 | **AI virtual staging / interior design for real estate** — Fill empty room photos with furniture using image generation for real estate and interior design. | saas_software | mention | 3/4/5/5/4 | 4 |
| I6 | **Airbnb photo lighting/vibe enhancement** — Improve the lighting or vibe of Airbnb listing photos with AI. | saas_software | mention | 3/4/5/5/4 | 4 |
| I7 | **Personalised 'tree fell on your house' images to sell tree trimming** — Generate images of a prospect's own home with a tree fallen on it to prompt them to buy tree trimming. | local_service | mention | 2/1/0/4/1 | 3 |
| I8 | **White-label AI ad creative service for ad agencies** — Partner with existing performance ad agencies and produce high volumes of AI-generated ad variants that they resell to their clients. | agency | deep | 3/3/3/4/3 | 5 |
| I9 | **AI ad-generation SaaS wrapper for ad agencies with permissionless outreach** — Scrape agencies' client portfolios, remake their clients' ads, and send them proactively with a link to a $200/month unlimited-generation tool built on Replit. | saas_software | deep | 4/4/5/5/4 | 5 |
| I10 | **Themed wrapper from top Sora Explore prompts (e.g. jacked Harry Potter characters)** — Browse Sora's most-liked prompts and turn a popular one into a single-purpose app. | saas_software | mention | 4/5/5/5/4 | 5 |
| I11 | **AI stock imagery** — Create stock images on demand with image generation. | digital_products | mention | 4/5/5/5/4 | 5 |
| I12 | **Micro-personalised ad creative (e.g. per event, per persona)** — Use cheap image generation to make ads for many narrow personas or every single event. | agency | mention | 3/3/4/4/3 | 5 |

### I1. Focused consumer image-filter apps (Ghibli-me, anime-me)

- **Customer:** Non-technical consumers who don't know what ChatGPT can do
- **Problem:** People outside tech don't know how to get these images from ChatGPT
- **Offer:** Single-purpose app that turns your photo into a style (Ghibli, anime)
- **Business model:** Subscription plus credit packs for extra images (suggested)
- **Pricing:** subscription + credits (suggested, no prices).  
- **Acquisition:** organic_social_content: Hope for virality on TikTok (suggested)
- **Delivery:** Thin app wrapping the OpenAI image generation API; user uploads photos and gets edited images.
- **Unit economics (claims):** 
- **Tools:** OpenAI image generation API
- **Startup cost:** Low (API costs; domain $10 for rightsizeme.com)
- **Time to first revenue:** Days (API released the day of recording)
- **UK applicability [E]:** 5/5 — Consumer apps work in the UK; uploads of personal photos require UK GDPR compliance.
- **Risks:** High churn and fad risk; Commoditised by ChatGPT itself; IP issues with styles like Studio Ghibli
- **Automation [E]:** acquisition 4/5 (Viral TikTok content and app store/SEO are inbound; content generation can be automated.); onboarding 5/5 (Self-serve sign-up and upload.); delivery 5/5 (Image API generates output unattended.); billing 5/5 (Subscription/credits via Stripe or app store.); support 4/5 (FAQ/refund handling by agent.)
> "take whatever whatever you know everyone is loving that Chad GPT does and just turn that into a super focused app like Giblly Me" — Jacob Posel (~3:01)

### I8. White-label AI ad creative service for ad agencies

- **Customer:** Performance marketing/ad agencies and their brand clients
- **Problem:** Ad algorithms reward creative volume and variety; ads fatigue; creative is the bottleneck
- **Offer:** Ad variants made from reference winning ads plus product images, delivered as finished ads in Google Drive folders in the client's format
- **Business model:** Per accepted ad, revenue split with agency, or base retainer plus per-ad fee
- **Pricing:** per ad / revenue split / retainer + per accepted ad.  No figures; Jacob suggests pricing per ad with markup or retainer plus ads accepted.
- **Acquisition:** cold_sms_dm: DM agencies on Twitter offering a white-labelled service; partnerships: Piggyback on agencies' existing trusted client portfolios, including dormant clients
- **Delivery:** Operator uses Sora/the image API with reference ads to create variants, curates the best, and delivers completed ads to the agency.
- **Unit economics (claims):** A $100 ad can make a brand $20,000 (Jacob's example); Images: about 60% of outputs good vs 90% text, 5% video
- **Tools:** Sora, OpenAI image generation API, Google Drive, Twitter/X
- **Startup cost:** Low
- **Time to first revenue:** not stated
- **UK applicability [E]:** 5/5 — Agencies and Meta/Google ads work the same in the UK.
- **Risks:** Best practices for viable ads are unsolved; high churn if output is poor; Agencies may build in-house; Margin squeezed by tools
- **Automation [E]:** acquisition 3/5 (B2B outreach to agencies (limited companies) by email/DM is allowed in the UK if targeted at businesses; agents can draft.); onboarding 3/5 (Briefing via format questions.); delivery 3/5 (Generation automated but curating viable ads still needs human taste; best practices unsolved.); billing 4/5 (Invoicing per ad/retainer.); support 3/5 (Revisions with oversight.)
> "ads are the perfect output for image generation because they make people money" — Jacob Posel (~0:09)
> "I would probably partner with existing ad agencies and I would say I'm going to help you to offer a service to your customers" — Jacob Posel (~20:51)

### I9. AI ad-generation SaaS wrapper for ad agencies with permissionless outreach

- **Customer:** Ad agencies not yet using AI creative
- **Problem:** Agencies need cheap high-volume creative
- **Offer:** Agency-branded image-generation tool (Sora-like) plus sample remade ads
- **Business model:** Subscription $200/month
- **Pricing:** subscription. USD 200 per month Chris prefers flat monthly over per-ad because brands want predictable costs; must watch API credits. Jacob argues to deliver done-for-you first because tools are hard to adopt.
- **Acquisition:** cold_email: Scrape agencies listing clients; remake six ads for one of their clients and send proactively with a link to the tool
- **Delivery:** Self-serve web app built on Replit wrapping the image API.
- **Unit economics (claims):** 
- **Tools:** Replit, OpenAI image generation API
- **Startup cost:** Low
- **Time to first revenue:** not stated
- **UK applicability [E]:** 5/5 — Works in UK; B2B cold email to companies allowed under PECR.
- **Risks:** Tool adoption friction (Jacob); API cost on unlimited plans; Using client brand assets without permission
- **Automation [E]:** acquisition 4/5 (Scraping and personalised B2B email to agencies (limited companies) is legal in UK and automatable.); onboarding 4/5 (Self-serve.); delivery 5/5 (Software.); billing 5/5 (Stripe subscription.); support 4/5 (Agent support.)
> "And then you charge 200 bucks a month for it. And it's just a tool. It's just a tool that they use for unlimited image generation" — Chris Koerner (~24:28)
> "it's really difficult to get people to use tools, like to actually use it themselves, even if there's really obvious value there" — Jacob Posel (~25:06)

## Revenue and metric claims (unverified claims)

- **A $100 ad can make an advertiser $20,000** (other, second-hand, hypothetical, claimant: Jacob Posel)
  > "if a single ad cost them a h 100red bucks, they could make like $20,000 from that" — Jacob Posel (~9:56)
- **Domain rightsizeme.com cost $10** (cost, first-hand, claimant: Chris Koerner)
  > "Rightizeme.com. How much was it? Done. 10 bucks" — Chris Koerner (~6:13)
- **Charge agencies $200/month for unlimited generation** (price, second-hand, hypothetical, claimant: Chris Koerner)
  > "And then you charge 200 bucks a month for it" — Chris Koerner (~24:28)
- **Roughly 90% of text outputs good, 60% of images, 5% of video** (conversion_rate, second-hand, claimant: Jacob Posel)
  > "if you use text, like I would say 90% of outputs are going to be good. If you use images, 60% of outputs are going to be good" — Jacob Posel (~16:18)
- **Two-thirds of Americans are overweight (market size)** (customers, second-hand, claimant: Chris Koerner)
  > "I mean twothirds of Americans are overweight. So there's your market" — Chris Koerner (~4:44)
- **Sora generates four images at once vs one in ChatGPT** (other, second-hand, claimant: Jacob Posel)
  > "Sora is limited to creating four images at once. With the API you can create more than that" — Jacob Posel (~13:38)

## Tactics and playbook steps

**Reference-ad variant generation** (operations)
1. Screenshot a competitor's or your own winning ad as the reference
2. Add your product image
3. Tell the model clearly which image is the reference ad to reproduce and which is the product
4. Generate multiple variants (4 in Sora, 50 via API) and pick the best to refresh fatigued ads
> "the reference image can be one the reference ad which is just a screenshot of the ad that you like and two can be your product" — Jacob Posel (~11:50)

**Piggyback on agencies with a white-label offer** (acquisition)
1. List agencies (DM on Twitter)
2. Offer to deliver AI ads under their brand to existing and dormant clients
3. Price per ad with markup, revenue split, or retainer plus per-ad-accepted
4. Deliver finished ads in Google Drive in the client's format
> "I would literally send them Google Drive folders of just completed ads" — Jacob Posel (~25:22)

**Permissionless spec work for agencies** (acquisition)
1. Scrape agency sites listing clients
2. Pick agencies not yet using AI
3. Remake several of a client's ads
4. Send them proactively with a link to your tool
> "a lot of these ad agencies list out their customers, right? They just make it too easy for growth hackers like us" — Chris Koerner (~23:36)

**Mine Sora Explore for app ideas** (product)
1. Scroll Sora's explore page sorted by likes
2. Look at the exact prompts and former popular filters
3. Turn a top prompt into a focused wrapper
> "I highly recommend anyone listening to this just scroll through Sora and just take a look at their explore page" — Jacob Posel (~17:19)

## Lessons

- *mindset_execution*: New API releases create short gold rushes; prepare in advance and launch the day they drop.
- *niche_selection*: Most people outside tech don't know what AI can do; packaging one capability into a focused app is the opportunity.
- *niche_selection*: Image outputs tied to revenue (ads) are the best use because buyers see ROI.
- *customer_acquisition*: Ad algorithms now reward creative volume and variety, so demand for cheap high-volume creative is rising.
- *automation_ai*: Reference images improve output far more than describing the image.
- *customer_acquisition*: Agencies are arbitrage businesses and will resell any service they can mark up.
- *pricing*: Clients want predictable monthly costs; flat pricing or approval-based per-ad pricing avoids bill shock.
- *mindset_execution*: People look for excuses not to launch.
- *customer_acquisition*: Cheap creative enables hyper-targeted personas instead of a few broad ones.

## Warnings and mistakes

- Without solving how to reliably produce viable ads you'll get a spike then massive churn.
- AI video is still a gimmick; not worth investing time yet.
- Getting customers to use tools themselves is hard; do it for them first.
- Some image-enhancement uses (Airbnb photos) draw backlash as deceptive.
- Spreading thin across opportunities means not winning at anything.

## Tools mentioned

OpenAI image generation API (Core image generation, released the day of recording), ChatGPT (Image generation (one image at a time)), Sora (Generates 4 images at once; explore library of prompts), Replit (Building wrapper apps), TikTok (Virality for consumer apps), Google Drive (Delivering ads to agencies), Google Photos (Comparison photos), Twitter/X (Finding and DMing agencies), tkopod.com newsletter (Host's free newsletter)
