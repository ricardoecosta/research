# The Most Useful AI Skill You Can Learn Today

- **Video:** [By9zAwSl3qg](https://www.youtube.com/watch?v=By9zAwSl3qg) · **Channel:** The Koerner Office · **Uploaded:** 2025-07-08 · **Length:** 42 min · **Transcript:** ok
- **Speakers:** Chris Koerner (host), Mike (Rasmiki) (guest) · **Format:** operator_interview
- **Evidence quality:** C — Mostly general advice and illustrative ideas; the guest's only concrete builds (pizza agent, church payments) are unmonetised, and no first-hand revenue figures are given. Third-party numbers are hearsay. · Promotional conflict: Host promotes TK Owners ($99/month community) and his newsletter; guest uses and mentions Tempo (a vibe-coding tool) and admits bias.
- **Extraction:** claude-sonnet-5-5 · quotes verified 26/26

## Summary

Chris Koerner interviews a Canadian developer/YouTuber (Mike, X handle 'Rasmiki') about how non-technical people can use AI automation and vibe-coding tools. He urges viewers to build at least one automation, shares his AI pizza-ordering agent, and explains n8n webhooks for packaging automations into web apps. The key advice is to solve problems from your own industry (outside the tech bubble), use UX/design taste as a moat, pick LLMs by task (Claude for code, OpenAI for consumer chat, Gemini for cost), and keep learning tools. Business ideas are mostly illustrative and unvalidated.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Industry-specific AI app built by an insider (e.g. pharmacy software)** — Domain insiders use AI/vibe-coding tools to build software for the boring, compliance-heavy pain points of their own industry. | saas_software | moderate | 2/3/4/5/3 | 4 |
| I2 | **AI-first bookkeeping app** — A bookkeeping/receipt app built AI-first, ideally by an accountant or bookkeeper who knows the pain points. | saas_software | mention | 3/4/4/5/3 | 3 |
| I3 | **Church / charity payment solution** — Cheaper donation-payment software for churches and charities, built by an insider who knew the problem. | saas_software | mention | 2/3/4/5/3 | 3 |
| I4 | **AI pizza-ordering agent (Domino's)** — Chatbot web app with an AI agent that converses with the user and places a Domino's order via an unofficial API. | ai_automation | moderate | 0/3/3/2/1 | 2 |
| I5 | **Packaged n8n automation as web app (webhooks + vibe coding)** — Wrap an n8n automation behind a simple web front-end using webhooks, e.g. a shoe price-drop alert service. | ai_automation | moderate | 3/4/4/5/3 | 4 |
| I6 | **Thumbnail-request email auto-responder** — Automation that reads emails, detects thumbnail inquiries, and asks the sender for their price. | ai_automation | mention | 0/0/5/0/0 | 5 |
| I7 | **AI-first clone of an incumbent app (Cal AI model)** — Take an established app category and rebuild it AI-first, as Cal AI did against MyFitnessPal. | saas_software | mention | 3/4/4/5/3 | 5 |
| I8 | **Beautiful-UX version of an ugly incumbent (Linear vs Jira)** — Compete by building a much better-designed version of an established but ugly tool, as Linear did to Jira. | saas_software | moderate | 3/4/3/5/3 | 5 |

### I1. Industry-specific AI app built by an insider (e.g. pharmacy software)

- **Customer:** Professionals and businesses in a specific industry, e.g. pharmacies.
- **Problem:** Annoying billing, medication-registration software and compliance burdens that tech-bubble builders find boring and ignore.
- **Offer:** A tailored app or wrapper solving a specific workflow pain point in the builder's own industry.
- **Business model:** Software subscription or sales to businesses in a niche industry (not specified in detail).
- **Pricing:** not stated.  No pricing given.
- **Acquisition:** referrals_word_of_mouth: Distribute wrappers to friends and co-workers in the industry to test and gather feedback, then iterate.
- **Delivery:** Built with AI/vibe-coding tools by the industry insider; hosted software.
- **Unit economics (claims):** 
- **Tools:** ChatGPT deep research, vibe-coding tools, Tempo
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Approach is general; UK pharmacy or other regulated sectors have their own compliance (e.g. NHS, GDPR) requiring adaptation.
- **Risks:** Regulated industries (pharmacy) carry compliance and data-protection obligations; Builder needs real domain knowledge and distribution; No validation or revenue evidence given
- **Automation [E]:** acquisition 2/5 (Outreach to personal network is human; later marketing in niche could use content/SEO with tooling.); onboarding 3/5 (Self-serve SaaS onboarding can be largely automated.); delivery 4/5 (Software product runs itself once built; agents can maintain it with occasional human review.); billing 5/5 (Subscription billing via Stripe-type tools.); support 3/5 (AI support with human escalation for compliance questions.)
> "I have a a friend who works with works at a pharmacy and he's having fun building things forarmacies" — Mike (Rasmiki) (~20:33)

### I4. AI pizza-ordering agent (Domino's)

- **Customer:** The builder himself.
- **Problem:** Convenience of ordering pizza through chat.
- **Offer:** Chat interface with agent that gathers order details, stores them in a DB, then calls the Domino's API and pays.
- **Business model:** Personal project; not monetised.
- **Pricing:** not applicable.  Not sold.
- **Acquisition:** 
- **Delivery:** Software agent calling an unofficial Domino's API.
- **Unit economics (claims):** 
- **Tools:** Domino's API (unofficial), n8n, database
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 2/5 — Depends on an unofficial Domino's Canada API; UK would need a different integration and it is not a viable business.
- **Risks:** Unofficial API with no secure payment handling; Breach of terms of service; Never published by the builder
- **Automation [E]:** acquisition 0/5 (Not a commercial product.); onboarding 3/5 (Chat handles it.); delivery 3/5 (Agent places the order; real-world pizza made by Domino's.); billing 2/5 (Payment handled via insecure unofficial API.); support 1/5 (Not designed.)
> "the API that it used to interact with Domino's was like not an official API. It was like some guy who built it six years ago" — Mike (Rasmiki) (~5:08)

### I5. Packaged n8n automation as web app (webhooks + vibe coding)

- **Customer:** Consumers or users who want simple tools (e.g. shoe price alerts).
- **Problem:** Automations are hard for non-technical users to use; they need a simple interface.
- **Offer:** A web app where the user enters their email, and the automation scrapes for a shoe price and notifies them when it drops.
- **Business model:** Sell an easy interface to an automation (e.g. subscription); not specified.
- **Pricing:** not stated.  Speaker asks how to package and sell it but gives no price.
- **Acquisition:** 
- **Delivery:** n8n workflow triggered by webhook from a vibe-coded front end.
- **Unit economics (claims):** 
- **Tools:** n8n, Gumloop, Tempo, webhooks
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — Works in the UK; marketing emails to subscribers need consent under PECR/GDPR and scraping must respect site terms.
- **Risks:** Scraping may breach retailer terms; Low willingness to pay for price alerts; Idea is illustrative only
- **Automation [E]:** acquisition 3/5 (Inbound SEO/ads can be automated.); onboarding 4/5 (User just enters an email.); delivery 4/5 (Scraping and notification run automatically, with occasional fixes for broken scrapers.); billing 5/5 (Stripe subscription.); support 3/5 (AI support with human check.)
> "how do you package that? How do you sell that? Or how do you build an interface that makes it very very simple for someone to use that automation" — Mike (Rasmiki) (~7:24)

### I8. Beautiful-UX version of an ugly incumbent (Linear vs Jira)

- **Customer:** Teams using clunky incumbent software.
- **Problem:** Existing tools work but are ugly and unpleasant to use.
- **Offer:** Same functionality with elegant, fast, thoughtful UX.
- **Business model:** SaaS subscription.
- **Pricing:** not stated.  Argued customers may pay more for better design.
- **Acquisition:** 
- **Delivery:** Software; design taste developed by studying sites and using vibe-coding with screenshot workflow.
- **Unit economics (claims):** 
- **Tools:** Linear, Jira, Magic UI, Tempo
- **Startup cost:** not stated
- **Time to first revenue:** not stated
- **UK applicability [E]:** 5/5 — Software design competition is global.
- **Risks:** Hard to displace entrenched incumbents; Design alone may not be enough
- **Automation [E]:** acquisition 3/5 (Content and product-led growth.); onboarding 4/5 (Self-serve.); delivery 3/5 (AI can build UI but design judgement needs human taste.); billing 5/5 (Subscription billing.); support 3/5 (AI support.)
> "Jira except pretty that's their their business model." — Chris Koerner (~27:05)

## Revenue and metric claims (unverified claims)

- **A company raised upwards of $10 million for something the speaker and a colleague thought would take 2-3 days to build.** (valuation, second-hand, claimant: Mike (Rasmiki))
  > "raised so much money, like I think upwards to like $10 million for something that honestly would have probably taken us maybe two to three days to build" — Mike (Rasmiki) (~17:02)
- **MyFitnessPal has $100M+ revenue (hearsay).** (revenue, second-hand, claimant: Chris Koerner)
  > "It's a nine figure company or it has $100 million plus of revenue." — Chris Koerner (~24:41)
- **Airbnb is a hundred-billion-dollar company that used design as its strategy.** (valuation, second-hand, claimant: Chris Koerner)
  > "look at Airbnb. They were designed first from day one and it's a hundred billion dollar company." — Chris Koerner (~30:38)
- **TK Owners community costs $99 per month.** (price, first-hand, claimant: Chris Koerner)
  > "And it's 99 bucks a month, about the cost of an energy drink per day." — Chris Koerner (~9:15)
- **Speaker fixed a cousin's API issue in 30 seconds after the cousin spent 2-3 days stuck.** (hours, first-hand, claimant: Mike (Rasmiki))
  > "he like spent two three days. So guess what I did Chris? I hopped in. I fixed it for him. It was a 30-cond fix for me." — Mike (Rasmiki) (~33:50)

## Tactics and playbook steps

**Mine industry pain points with ChatGPT deep research** (product)
1. Tell ChatGPT your profession and ask for common pain points in that industry
2. Use deep research to scan Reddit, message boards and social media for gripes and complaints
3. Take the 7 most relevant of the 20 returned and ask for 20 more like them
4. Repeat until you have 30-50 problems that ring true
5. Pick the top three, build wrappers, share with friends and co-workers, and iterate on feedback
> "Pretty soon, you'll have 30 to 50 problems, and all of them will ring true to you as someone in the industry." — Chris Koerner (~22:02)

**Package an n8n automation as a product via webhooks** (product)
1. Build the automation in n8n
2. Search 'n8n webhooks' and read the first doc
3. Create a webhook trigger so a web app can send user input (e.g. email) to the workflow
4. Use a vibe-coding tool (e.g. Tempo) to build the front end
5. Expect several attempts and debugging
> "I can connect this automation with a web app and that's when it becomes interesting." — Mike (Rasmiki) (~7:01)

**Recreate a site's design with screenshot-to-AI workflow** (product)
1. Screenshot the target site
2. Feed the screenshot to a vibe-coding tool and ask it to copy the design
3. Expect roughly 40% fidelity
4. Go section by section telling the model what is off (button roundness, gradients, spacing)
5. Iterate until pixel-close
> "The way you get the 40% to 100 is by going through every section of the site that doesn't look pixel perfect and telling it." — Mike (Rasmiki) (~34:53)

**Debug by screenshotting errors into ChatGPT** (mindset)
1. Screenshot each error or stuck point
2. Ask ChatGPT what happened and how to learn from it
3. Retry, or return the next day
> "I will literally either screenshot whatever error I've experienced or where I've got stuck at and let's chat GBT what happened and how do I learn from this?" — Mike (Rasmiki) (~3:41)

**Build design taste** (product)
1. Collect sites and apps you wish you had built
2. Study frameworks and component libraries such as Magic UI
3. Analyse what makes Apple's style work: fonts, spacing, bento grid
4. Use that taste to guide AI tools

## Lessons

- *mindset_execution*: Build at least one small automation for a task you do regularly; learning by doing beats watching.
- *niche_selection*: The best opportunities are in industries you already know, where you understand customers' problems and how to reach them.
- *niche_selection*: Boring, compliance-heavy industry problems are where money is because tech-bubble builders ignore them.
- *customer_acquisition*: Building is only part one; marketing is a separate challenge, easier if you are inside the industry.
- *offer_design*: UX and design taste can be a moat; customers will pay more for polished experiences.
- *automation_ai*: Choose LLMs per task: Claude for code/agentic, OpenAI for consumer chat and personality, Gemini for cost; beginners should default to OpenAI. Cost matters little at the prototyping stage.
- *mindset_execution*: Stay flexible and switch tools when better models launch; knowledge from failed experiments still compounds.
- *hiring_outsourcing*: Non-technical founders should learn base technical concepts (front end, back end, auth, database) and keep developer friends.
- *automation_ai*: MCP standardises LLM access to third-party services, reducing custom API integration work.
- *validation_testing*: Beginners may build a landing page first for momentum, but experienced builders should build the product first and treat design separately.

## Warnings and mistakes

- The Domino's agent was never published because it relied on an unofficial API with no secure payment handling.
- Don't start in the crowded tech bubble as a beginner; competition is intense.
- Don't prompt a vibe-coding tool with no plan or understanding; expect failures, especially with databases and back ends.
- Model recommendations go stale quickly; Claude 3.7 was previously dropped as a waste of money before Claude 4 changed his mind.

## Tools mentioned

n8n (No-code automation platform with webhooks; free trial mentioned), Gumloop (No-code AI automation platform), Zapier (Automation platform), Lindy (AI agent/automation platform), Tempo (Vibe-coding tool), Claude (Claude 4) (Coding, agentic and complex tasks; more expensive), OpenAI / ChatGPT (User-facing chatbots, personality, deep research; mid-priced), Gemini (Cost-effective all-rounder, image generation, 2.5 Pro for coding; cheapest), MCP (Model Context Protocol) (Standard for LLMs to connect to third-party services), Linear (Ticketing tool cited as UX example), Magic UI (React component library for design inspiration), Perplexity (Search; speaker no longer uses it), Grok (Used to explain tweets; not for API), Stripe (Payments), TK Owners (Host's paid community (promotional); $99/month)
