# I Built an AI Agent That Works While I Sleep (Cheap & Easy)

- **Video:** [AA-EL571oG4](https://www.youtube.com/watch?v=AA-EL571oG4) · **Channel:** The Koerner Office · **Uploaded:** 2025-11-28 · **Length:** 15 min · **Transcript:** ok
- **Speakers:** Chris Koerner (host) · **Format:** tutorial_howto
- **Evidence quality:** C — Tutorial with hypothetical income projections; no client results shown. · Promotional conflict: Sponsored by Hostinger (discount code, Black Friday sale).
- **Extraction:** grokbot · quotes verified 16/16

## Summary

Chris Koerner explains the difference between automations and AI agents. On camera, he builds a 'content multiplication' agent in n8n self-hosted on a Hostinger VPS that turns his latest YouTube transcript into short, medium and long LinkedIn posts with GPT-5. He warns about n8n cloud costs and pitches selling such agents to creators and businesses for $300-800/month plus a $2,000 setup fee, projecting $10-30k/month with 10-30 clients. The video is sponsored by Hostinger and the income figures are hypothetical.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Content multiplication agent service (YouTube to LinkedIn posts)** — Build n8n agents on a self-hosted Hostinger VPS that turn a creator's latest YouTube video transcript into short, medium and long LinkedIn posts, and sell setup plus monthly maintenance to creators and businesses. | ai_automation | deep | 2/3/4/5/3 | 5 |
| I2 | **n8n template/agent builds for vertical niches** — Build reusable n8n agents (inbox triage, lead to CRM, scheduling) for real estate, fitness, restaurants or healthcare clients. | ai_automation | mention | 2/3/4/5/3 | 5 |

### I1. Content multiplication agent service (YouTube to LinkedIn posts)

- **Customer:** Creators, podcasters and business owners overwhelmed by social media (real estate, fitness, restaurants, health care)
- **Problem:** Repurposing long-form content into social posts takes time
- **Offer:** Daily scheduled agent: fetch newest video, pull transcript via youtube-transcript.io, extract 3-5 insights with GPT-5, write three LinkedIn posts in a set tone
- **Business model:** Setup fee plus monthly retainer per client
- **Pricing:** Setup + monthly retainer. USD 300-800 per month per client; USD 2000 one-off setup fee Chris's hypothetical: 10 clients = ~$5k/month; with setups up to ~$20k/month.
- **Acquisition:** referrals_word_of_mouth: Build for friends for free first, use the first client as a case study to get the next three.
- **Delivery:** n8n self-hosted on a Hostinger KVM 2 VPS; YouTube API, youtube-transcript.io API, OpenAI API; VA after 5-10 clients.
- **Unit economics (claims):** $300-800/month per client; 10 clients ~$5k/month, almost pure profit; 10-30 clients in 6-12 months = $10-30k/month
- **Tools:** n8n, Hostinger, OpenAI GPT-5, youtube-transcript.io, YouTube API, LinkedIn
- **Startup cost:** VPS plan (price not stated)
- **Time to first revenue:** not stated
- **UK applicability [E]:** 5/5 — Works the same in the UK.
- **Risks:** Competition from other agencies and SaaS repurposing tools; Workflows break (shown on camera); LinkedIn/YouTube API changes; Hypothetical income figures
- **Automation [E]:** acquisition 2/5 (Starts with friends and referrals; selling to businesses needs human sales. UK cold email allowed only to limited companies (PECR); inbound content and templates better.); onboarding 3/5 (Credential connection per client needs some hand-holding.); delivery 4/5 (Scheduled agent runs unattended; posts may need approval.); billing 5/5 (Stripe retainers.); support 3/5 (Fixing broken workflows needs a human or a VA.)
> "You could charge between $300 and $800 a month per client. 10 clients equals, call it $5,000 a month" — Chris Koerner (~13:59)
> "You could charge $2,000 one time for a setup fee, and before you know it, you're at $20,000 a month in revenue" — Chris Koerner (~14:07)

## Revenue and metric claims (unverified claims)

- **n8n cloud starts at $20/month but can balloon past $100/month** (cost, second-hand, claimant: Chris Koerner)
  > "n8n offers cloud hosting that starts at 20 bucks a month, but once you have half a dozen automations running" — Chris Koerner (~4:56)
- **Charge $300-800/month per client** (price, second-hand, hypothetical, claimant: Chris Koerner)
  > "You could charge between $300 and $800 a month per client" — Chris Koerner (~13:59)
- **10 clients ~ $5,000/month** (revenue, second-hand, hypothetical, claimant: Chris Koerner)
  > "10 clients equals, call it $5,000 a month, and that's almost pure profit" — Chris Koerner (~14:02)
- **$2,000 setup fee; up to $20k/month revenue** (revenue, second-hand, hypothetical, claimant: Chris Koerner)
  > "before you know it, you're at $20,000 a month in revenue" — Chris Koerner (~14:11)
- **10-30 clients in 6-12 months = $10-30k/month** (revenue, second-hand, hypothetical, claimant: Chris Koerner)
  > "After six to 12 months, you scale to 10 to 30 clients, and you're making 10 to $30,000 a month" — Chris Koerner (~15:01)
- **Hostinger n8n setup takes about 5 minutes** (hours, first-hand, claimant: Chris Koerner)
  > "Should take about 5 minutes" — Chris Koerner (~6:05)

## Tactics and playbook steps

**Self-host n8n on Hostinger** (operations)
1. Choose Hostinger self-hosted n8n, KVM 2 plan, 12 months
2. Pick a nearby server location
3. Set password and owner account (~5 minutes)
4. Use templates library or build workflows

**YouTube-to-LinkedIn workflow** (product)
1. Schedule trigger 6am daily
2. YouTube node: get latest video by date from channel ID
3. HTTP POST to youtube-transcript.io with Basic auth header and video ID
4. Merge transcript chunks
5. OpenAI node (GPT-5): extract 3-5 LinkedIn-worthy insights
6. Three OpenAI nodes: short (<300 chars, hook <120 chars on two lines), medium (800-1,200), long (1,200-1,500); spartan tone, no emojis
7. Check each node pulls from the insights node
> "Write in a spartan tone of voice. That helps these LLMs not just go off the rails" — Chris Koerner (~12:16)

**Agency ramp** (acquisition)
1. Build templates for yourself
2. Build for friends for free
3. Ask them to pay for more agents
4. Use first client as case study
5. Hire a VA after 5-10 clients

## Lessons

- *automation_ai*: Automations follow fixed rules; agents interpret and decide, enabling multi-step work like inbox triage.
- *finance_unit_economics*: Self-hosting open-source tools gives flat costs regardless of agent count.
- *automation_ai*: Constrain LLM output with explicit lengths, tone and no-emoji rules.
- *customer_acquisition*: Start with free builds for friends to get case studies.
- *operations*: Template libraries let you avoid building from scratch.
- *pricing*: Most competitors aren't using AI yet, so you can deliver as good or better for less.

## Warnings and mistakes

- Cloud pricing trap: hosted n8n costs balloon with active automations; self-host instead.
- Agents need good prompting and break sometimes; nodes must reference the right inputs.
- Don't try to learn hardware and software at once with a Raspberry Pi.
- Most viewers will do nothing; execution is the bottleneck.

## Tools mentioned

n8n (AI-native automation/agent builder (open source, self-hostable); Cloud from $20/month), Hostinger (VPS hosting for n8n (sponsor, discount code)), Zapier (Rule-based automation), Make (Rule-based automation), OpenAI GPT-5 (LLM in workflow), youtube-transcript.io (Transcript API), YouTube API (Fetch latest videos), Raspberry Pi (Alternative self-hosting (not recommended)), ElevenLabs (Seen in templates (TikTok avatar videos)), templated.io (Seen in templates (thumbnails))
