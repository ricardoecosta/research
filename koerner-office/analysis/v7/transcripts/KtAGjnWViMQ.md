# Now is the Best Time to Make Money with Content (AI Tutorial)

- **Video:** [KtAGjnWViMQ](https://www.youtube.com/watch?v=KtAGjnWViMQ) · **Channel:** The Koerner Office · **Uploaded:** 2026-02-18 · **Length:** 15 min · **Transcript:** transcribeyoutube
- **Speakers:** Chris Koerner (host) · **Format:** tutorial_howto
- **Evidence quality:** C — Technical tutorial that works as shown, but income claims are generic and unsubstantiated, and the resale ideas are hypothetical with no customer evidence. · Promotional conflict: Sponsored by Hostinger; Koerner promotes an affiliate link and the coupon code 'kerneroffice'.
- **Extraction:** claude-sonnet-5-5 · quotes verified 20/20

## Summary

Chris Koerner argues now is a great time to earn from content inspired by other creators' content in any niche. He walks through building an n8n workflow on a Hostinger VPS (about $5/month) that reads YouTube channel RSS feeds on a schedule, appends the videos to a Google Sheet and emails a digest. Setup covers the Google Cloud Console APIs and OAuth consent, an RSS Read node, Google Sheets and Gmail nodes, and an Aggregate node to fix email spam. He suggests the tool could be resold, for example as a $30/month competitor-monitoring email to YouTubers, or sold as n8n templates. The video is promotional for Hostinger.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Content research automation (n8n YouTube RSS digest)** — Self-hosted n8n workflow that tracks competitor YouTube channels and emails new video titles daily so creators get content inspiration. | ai_automation | deep | 5/4/5/5/4 | 5 |
| I2 | **Resell competitor-monitoring email to YouTubers** — Scrape YouTube channel emails and pitch creators a daily email of what their competitors post for $30/month. | ai_automation | moderate | 2/4/5/5/4 | 3 |
| I3 | **Sell n8n templates** — Build n8n automation templates and sell them to others. | digital_products | mention | 3/4/5/5/3 | 5 |
| I4 | **Niche social content creation and monetisation** — Pick a niche, post consistently, build an audience, then monetise, using other creators' content as inspiration. | content_media | moderate | 3/5/3/4/4 | 5 |

### I1. Content research automation (n8n YouTube RSS digest)

- **Customer:** Content creators in any niche who need ongoing content ideas
- **Problem:** Manually checking 10+ creator accounts daily for content inspiration is exhausting and inconsistent
- **Offer:** Automated scan of chosen YouTube channels via RSS, logged to Google Sheets and emailed as a digest
- **Business model:** Internal tool for own content business; could be resold as a subscription
- **Pricing:** Own use; hosting cost only. Hostinger VPS hosting cost USD 5 per month RSS, Google Sheets and n8n automations described as free beyond hosting; other tools cost $30-$300/month
- **Acquisition:** 
- **Delivery:** n8n workflow on a Hostinger VPS: Schedule trigger, RSS Read per channel, Aggregate, Google Sheets append/update, Gmail send. Runs on a schedule (midnight daily in the demo) with no human involvement once built.
- **Unit economics (claims):** Costs about $5/month versus $30-$300/month for other content research tools; Setup takes about 30 minutes
- **Tools:** Hostinger VPS, n8n, Google Cloud Console, Google Sheets, Gmail API, YouTube RSS feeds, ChatGPT
- **Startup cost:** About $5/month for VPS hosting; about 30 minutes of setup
- **Time to first revenue:** not stated
- **UK applicability [E]:** 5/5 — Hostinger, n8n and Google tools are available in the UK and the workflow is not jurisdiction-specific.
- **Risks:** Google OAuth setup is fiddly; Some rows had errors in the sheet; Tool is a thin commodity workflow with little moat; Dependent on YouTube RSS feeds staying available
- **Automation [E]:** acquisition 5/5 (Not a customer-facing business as built; the tool itself needs no acquisition.); onboarding 4/5 (One-off setup of Google OAuth and n8n; agents could template it.); delivery 5/5 (Scheduled workflow runs unattended and emails the digest.); billing 5/5 (Only a fixed hosting subscription.); support 4/5 (Occasional breakage such as API tokens or feed errors needs a fix.)
> "Takes about 30 minutes. It costs about five bucks a month and it will run forever." — Chris Koerner (~1:18)
> "What does this cost you through Hostinger VPS? About five bucks a month. The RSS feeds, the Google Sheets, the automations, all of that is free." — Chris Koerner (~14:11)

### I2. Resell competitor-monitoring email to YouTubers

- **Customer:** YouTube channel owners
- **Problem:** Creators want to spy on competitors' uploads without manual checking
- **Offer:** Daily email listing everything a competitor posted
- **Business model:** Subscription
- **Pricing:** Monthly subscription. Suggested price USD 30 per month Hypothetical suggestion
- **Acquisition:** cold_email: Build another automation to scrape YouTube channel emails and email channel owners with the offer.
- **Delivery:** Same n8n RSS-to-email workflow run per customer.
- **Unit economics (claims):** $30/month per subscriber suggested
- **Tools:** n8n, Hostinger VPS
- **Startup cost:** About $5/month hosting
- **Time to first revenue:** not stated
- **UK applicability [E]:** 3/5 — Works technically, but cold emailing scraped creator addresses to individuals or sole traders breaches UK PECR and GDPR concerns.
- **Risks:** PECR/GDPR issues with scraped emails; Low willingness to pay when free alternatives exist; Easy for customers to copy
- **Automation [E]:** acquisition 2/5 (Cold email can be automated, but scraped creator emails are often sole traders or individuals, which PECR restricts.); onboarding 4/5 (Add the customer's competitor feeds to a workflow.); delivery 5/5 (Scheduled digest runs unattended.); billing 5/5 (Stripe subscription.); support 4/5 (Mostly self-serve with occasional fixes.)
> "I will email you a list of everything your competitor is posting every morning for 30 bucks a month." — Chris Koerner (~14:41)

### I4. Niche social content creation and monetisation

- **Customer:** Audience in a chosen niche
- **Problem:** Finding fresh content ideas daily is a grind
- **Offer:** Own-spin content versions of top-performing posts
- **Business model:** Audience monetisation (unspecified)
- **Pricing:** not stated.  
- **Acquisition:** organic_social_content: Post consistently in a niche, riffing on what top creators post.
- **Delivery:** Creator makes content personally; research is automated.
- **Unit economics (claims):** Claims tens of thousands of dollars a month are possible
- **Tools:** n8n
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 5/5 — Works the same in the UK.
- **Risks:** Slow audience growth; Derivative content may lack differentiation
- **Automation [E]:** acquisition 3/5 (Content can be AI-assisted, though authenticity matters.); onboarding 5/5 (No onboarding.); delivery 3/5 (AI can draft and edit content, with human review.); billing 4/5 (Platform payouts and sponsorships.); support 4/5 (Minimal.)
> "The formula is simple. You pick a niche, you post consistently, and you build an audience, then you monetize." — Chris Koerner (~0:28)

## Revenue and metric claims (unverified claims)

- **Koerner has over 5 million followers posting business ideas** (customers, first-hand, claimant: Chris Koerner)
  > "I got over 5 million followers posting about business ideas because that's what I'm interested in." — Chris Koerner (~0:15)
- **Setup costs about $5 a month via Hostinger VPS** (cost, first-hand, claimant: Chris Koerner)
  > "What does this cost you through Hostinger VPS? About five bucks a month." — Chris Koerner (~14:11)
- **Other content research tools cost $30-$300 a month** (price, second-hand, claimant: Chris Koerner)
  > "any other content research tool out there that's going to cost you between $30 and $300 a month" — Chris Koerner (~14:20)
- **Suggested resale price of competitor-monitoring email** (price, second-hand, hypothetical, claimant: Chris Koerner)
  > "I will email you a list of everything your competitor is posting every morning for 30 bucks a month." — Chris Koerner (~14:41)
- **People can make tens of thousands of dollars a month publishing content inspired by others** (revenue, second-hand, hypothetical, claimant: Chris Koerner)
  > "This is the best time in history to make tens of thousands of dollars a month publishing content that's inspired by someone else's content." — Chris Koerner (~0:00)
- **Setup takes about 30 minutes** (hours, first-hand, claimant: Chris Koerner)
  > "Takes about 30 minutes. It costs about five bucks a month and it will run forever." — Chris Koerner (~1:18)

## Tactics and playbook steps

**Build a YouTube competitor-tracking digest in n8n** (operations)
1. Buy a Hostinger VPS with n8n preinstalled
2. In Google Cloud Console create a project, enable the Gmail and Google Sheets APIs, configure the OAuth consent screen with external audience and test users
3. Add Gmail read/send/modify and Sheets read/write scopes
4. In n8n add a Schedule trigger, then an RSS Read node per channel
5. Get each channel's RSS URL from the page source by searching for RSS, which avoids third-party sites that harvest your email
6. Append publish date, channel name and title to a Google Sheet
7. Add an Aggregate node (titles, links) before the Gmail node so you get one digest email, not one per video
8. Limit to the latest 10 items per channel and schedule daily
> "I'm going to add a node right here between RSS and Gmail. Hit the plus. It's going to be called aggregate." — Chris Koerner (~13:02)

**Use top creators' posts as content inspiration** (product)
1. Pick a niche and identify top creators
2. Watch what they post that performs well
3. Make your own version with your spin and personality
> "if a top healthy recipe account posts 5minute protein breakfast and it crushes, maybe you should make your own version" — Chris Koerner (~1:40)

## Lessons

- *automation_ai*: Consistency, not creativity, is the hard part of niche content; automating the research removes a major source of drop-off.
- *validation_testing*: Study what already works in your niche rather than reinventing the wheel, then add your own spin.
- *finance_unit_economics*: Self-hosting open workflow tools can replace $30-$300/month SaaS for a few dollars a month.
- *scaling*: Internal tools you build can become products you resell, turning a cost saver into a revenue line.
- *operations*: Test automations incrementally and check output at each node before chaining steps; expect to debug aggregation issues.
- *niche_selection*: Pick a niche based on genuine interest, since sustained posting depends on it.

## Warnings and mistakes

- Connecting the Gmail node after the Sheets step or without an Aggregate node sends one email per video, flooding the inbox.
- Third-party RSS lookup sites ask for your email; get the feed URL from page source instead.
- Running the schedule more often costs more credits.

## Tools mentioned

Hostinger VPS (Hosting for n8n; about $5/month; 61% off plus extra 10% with coupon), n8n (Workflow automation platform; free self-hosted on the VPS), Google Cloud Console (Enable Gmail and Sheets APIs and OAuth; free), Google Sheets (Log scraped videos; free), Gmail (Send digest email; free), YouTube RSS feeds (Source of channel video lists; free), ChatGPT (Help with limiting scraped items)
