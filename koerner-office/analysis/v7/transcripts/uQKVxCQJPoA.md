# Watch This Overlooked AI Tool Build Me a Business in 23 Minutes

- **Video:** [uQKVxCQJPoA](https://www.youtube.com/watch?v=uQKVxCQJPoA) · **Channel:** The Koerner Office · **Uploaded:** 2025-09-12 · **Length:** 23 min · **Transcript:** ok
- **Speakers:** Chris Koerner (host) · **Format:** tutorial_howto
- **Evidence quality:** C — This is a live product demo rather than a validated business. The host says he does not plan to run the app as a business, there is no customer, revenue or conversion data, and the economics are hypothetical. The tool demo itself is first-hand and credible, but the market 'validation' is only search-trend evidence. · Promotional conflict: Promotes his TK Owners community and Replit (says it is not an ad, but it is a product showcase); asks viewers to subscribe.
- **Extraction:** claude-sonnet-5-5 · quotes verified 25/25 · reviewed by claude-opus-5-5

## Summary

Chris Koerner demonstrates finding, validating and launching a business idea in one sitting using Replit Agent 3. He uses Google Trends and Google autocomplete to spot demand for free invoicing software for contractors, then vibe-codes an AI chat/email invoicing app with Stripe payment links and Resend email, and publishes it on a new domain (invoicefree.com). The app works after fixing email-domain verification, though emails land in spam. Key takeaway: search trends plus autocomplete are a cheap demand signal, and AI app builders can produce a working MVP in under an hour; Koerner says he does not plan to turn it into a business.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Invoice Freely: AI chat/email invoicing for contractors** — Free natural-language invoicing app where contractors text, email or chat a request and the customer gets an invoice with a Stripe payment link; revenue from a markup on card processing. | saas_software | deep | 3/4/5/4/3 | 3 |
| I2 | **Demand-research method: Google Trends plus autocomplete** — Find a business idea by checking Google Trends for a rising keyword and reading Google autocomplete suffixes to see which niches have demand. | other | moderate | 0/0/4/0/0 | 5 |

### I1. Invoice Freely: AI chat/email invoicing for contractors

- **Customer:** Small businesses and contractors (tree trimmers, roofers, general contractors, home service businesses, gutter cleaners) who dislike filling in CRM/invoicing forms.
- **Problem:** Invoicing software is painful and rarely industry-specific; contractors on a job site do not want to log into a CRM and fill in name, phone, email and address.
- **Offer:** Free invoicing software where the user types or emails something like 'send an invoice for $800 to Mary Smith for tree trimming services'; the app extracts the details with OpenAI, asks for confirmation, and emails the customer an invoice with a Stripe checkout link. Includes a dashboard of invoices sent, paid and pending.
- **Business model:** Free software monetised by a markup on Stripe card processing (about 0.5% on top of Stripe's 2.9%).
- **Pricing:** Free to users; platform earns a processing markup (e.g. about 3.5% charged vs Stripe's ~2.9%); users can mark it up or pass it on. Stripe fee (approx.)  2.9 percent Stripe processing fee; Platform markup  0.5 percent markup on each payment; Hypothetical revenue at 100 customers USD 1000 per month The transcript garbles the figure ('3 12%'), most likely '3 1/2%' (3.5%). He calls the margin 'half a percent', though 3.5% minus 2.9% is about 0.6%. Not a stated price to customers.
- **Acquisition:** other: Host plans a lead capture / email capture / lead magnet on the site and exposure from this video; no real acquisition plan stated.; existing_audience: The YouTube audience is expected to try the app after the video goes live.
- **Delivery:** Software delivered as a web app on a custom domain, built with Replit Agent 3. Uses OpenAI API for natural language parsing, Stripe for payment links and Resend for transactional email. Text/SMS via Twilio was left out of the MVP because of US A2P registration (about 2 weeks).
- **Unit economics (claims):** Even 100 customers could be $1,000/month with almost no cost (hypothetical); Domain cost $11; Twilio number would cost $1/month; Over 33 million small businesses need invoicing software
- **Tools:** Replit Agent 3, Google Trends, Google autocomplete, Stripe, Resend, OpenAI API, Namecheap, Twilio (not implemented)
- **Startup cost:** About $11 for the domain plus Replit subscription and API usage (not stated); Resend free plan expected to suffice.
- **Time to first revenue:** not stated; a working MVP was built in under an hour, but no revenue and no stated plan to run it as a business
- **UK applicability [E]:** 3/5 — Software idea works in the UK with changes: Stripe supported, UK contractors and sole traders need invoices and VAT handling (Making Tax Digital), and a 0.5% markup needs Stripe Connect/payments compliance. A2P registration is US-specific; UK SMS is simpler. Market is very crowded (Xero, FreeAgent, QuickBooks, Zoho).
- **Risks:** Crowded invoicing software market; Invoice emails from a no-reply address landed in spam; Payments markup may need Stripe Connect and regulatory compliance; Early AI-generated app had bugs (wrong $150 amount, emails not arriving); Free pricing means revenue depends on payment volume; Host himself says he does not plan to run it as a business
- **Automation [E]:** acquisition 3/5 (No acquisition plan exists yet. Inbound routes (SEO, directories, app listings, ads) could be run by agents; cold outreach to sole traders would be restricted in the UK under PECR.); onboarding 4/5 (Self-serve signup and chat interface; an agent can handle setup, with occasional human review.); delivery 5/5 (The product is software: OpenAI parses the request, Stripe and Resend handle payment and email. Deliverability issues (spam folder) need occasional fixes.); billing 4/5 (Stripe processes payments and the platform markup is automatic; the host would handle payouts, tax and Stripe Connect setup.); support 3/5 (AI support agents can field most questions, but payment disputes and failed emails need human escalation.)
> "Build me a free invoicing software for contractors where my customers can use natural language either via SMS or a chatbot window" — Chris Koerner (~3:56)
> "Even if we had a 100 customers on this business, that could be $1,000 a month. That's awesome. With almost no cost." — Chris Koerner (~11:05)
> "Am I planning on making this a business? No." — Chris Koerner (~22:34)

### I2. Demand-research method: Google Trends plus autocomplete

- **Customer:** Aspiring founders looking for ideas
- **Problem:** Finding and validating ideas with real demand
- **Offer:** A free process: check Trends over 5 years, type the keyword plus a space into Google, and read the autocomplete suffixes (small business, free, freelancers, contractors, etc.) as signals of volume and trend.
- **Business model:** Not a business; a research method used to pick a product niche.
- **Pricing:** free method.  
- **Acquisition:** 
- **Delivery:** Manual research in Google Trends and Google search.
- **Unit economics (claims):** 
- **Tools:** Google Trends, Google autocomplete
- **Startup cost:** $0
- **Time to first revenue:** not stated
- **UK applicability [E]:** 5/5 — Google Trends and autocomplete work in the UK; use the UK region filter.
- **Risks:** Autocomplete shows interest, not willingness to pay; Demand for 'free' may not convert to revenue
- **Automation [E]:** acquisition 0/5 (Not a business.); onboarding 0/5 (Not applicable.); delivery 4/5 (An agent can pull trends and autocomplete data and shortlist niches.); billing 0/5 (Not applicable.); support 0/5 (Not applicable.)
> "the autocomplete tells us where the demand is. It's giving us a combo of which of these keywords have the highest search volume and which of them are trending in the right direction." — Chris Koerner (~1:20)

## Revenue and metric claims (unverified claims)

- **Invoicing software search interest has surged in Google Trends over the last year** (traffic, first-hand, claimant: Chris Koerner)
  > "Especially over the last year, for whatever reason, invoicing software is surging." — Chris Koerner (~1:06)
- **Stripe charges about 2.9% to process a card payment** (cost, second-hand, claimant: Chris Koerner)
  > "Stripe is going to charge about 2.9% to process that credit card payment." — Chris Koerner (~2:06)
- **Platform could earn about half a percent of every payment by marking up processing** (margin, second-hand, hypothetical, claimant: Chris Koerner)
  > "So then we can make half a percent of every single scent pushed through our software" — Chris Koerner (~2:22)
- **Domain invoicefree.com cost $11** (cost, first-hand, claimant: Chris Koerner)
  > "this domain name is unregistered. It's 11 bucks. I'm going to go ahead and buy it." — Chris Koerner (~10:32)
- **There are 33 million small businesses that need invoicing software** (customers, second-hand, claimant: Chris Koerner)
  > "there's 33 million small businesses that all need invoicing software and most of them are not happy with it." — Chris Koerner (~10:49)
- **100 customers could equal $1,000 per month** (revenue, second-hand, hypothetical, claimant: Chris Koerner)
  > "Even if we had a 100 customers on this business, that could be $1,000 a month." — Chris Koerner (~11:05)
- **Twilio phone number costs $1 a month** (cost, second-hand, claimant: Chris Koerner)
  > "You're going to buy a phone number in Twilio for $1 a month." — Chris Koerner (~8:44)
- **Replit Agent 3 runs for up to 200 minutes autonomously and claims 10x more autonomy than version two** (hours, second-hand, claimant: Chris Koerner (relaying Replit's claim))
  > "It claims to have 10 times more autonomy than version two." — Chris Koerner (~3:28)
- **The app was vibe coded in under an hour** (hours, first-hand, claimant: Chris Koerner)
  > "The app works. We vibe coded it in under an hour." — Chris Koerner (~22:52)

## Tactics and playbook steps

**Google Trends + autocomplete niche discovery** (acquisition)
1. Search a broad product keyword in Google Trends and set the range to 5 years to confirm it is rising
2. Type the keyword plus a space into google.com and read the autocomplete suffixes as demand signals
3. Note unexpected terms (e.g. 'free') that show what buyers want
4. Pick a suffix that maps to a big niche (e.g. contractors) and rewrite the product idea for it
> "I'm going to go to google.com just to the homepage and type in invoicing software 4." — Chris Koerner (~1:14)

**Monetise a free tool through payment processing markup** (pricing)
1. Offer the software free
2. Process payments through Stripe at about 2.9%
3. Charge a slightly higher rate (about 3.5%) and keep the difference of roughly half a percent
4. Let customers pass the fee on or mark it up to their clients

**Vibe-code an MVP with Replit Agent 3** (product)
1. Write one clear prompt describing the product and the simplest functional version
2. Prepare API keys first (Stripe secret key starting SK, Stripe public key starting PK, Resend, OpenAI)
3. Store keys in Replit Secrets
4. Ask the agent to verify the keys work
5. Test in preview, then paste errors and observations back to the agent
6. Publish to the Replit domain first, then connect the custom domain via DNS records
> "Let's oneshot prompt this bad boy." — Chris Koerner (~6:39)

**Set up Resend with a spare domain for transactional email** (operations)
1. Add a domain you own in Resend
2. Add the MX, TXT (SPF/DKIM) and DMARC records at your registrar's advanced DNS
3. Wait for verification
4. Set a FROM_EMAIL secret such as no-reply@verified-domain
5. Use a different domain from the app domain if desired, since it only sends and does not receive

**Launch an ugly MVP** (mindset)
1. Start with the simplest working version (scooter, not car)
2. Defer things like A2P registration, logo, perfect design and business plan
3. Launch, then upgrade over time
> "if you're not at least a little bit embarrassed by version one of your product or service, then you probably waited too long to launch." — Chris Koerner (~10:01)

## Lessons

- *validation_testing*: Google Trends plus autocomplete gives a quick, free signal of both demand and which niche to target.
- *niche_selection*: A crowded market can still be worth entering if it is large and customers are unhappy; a vertical focus gives a way to stand out.
- *finance_unit_economics*: 'Free' demand can be monetised indirectly, for example by taking a small cut of payment flow.
- *mindset_execution*: Ship an ugly MVP quickly instead of polishing; friction before launch kills projects.
- *offer_design*: Choose a name that is broad, easy to spell and says what you do so it does not box you into a sub-niche.
- *automation_ai*: AI app builders now handle full-stack MVPs with payments and email, but integration plumbing (DNS, email auth, spam) still needs human debugging.
- *automation_ai*: Feeding observations from third-party dashboards (e.g. Resend queue status) back to the AI agent speeds up debugging.
- *operations*: Keep the human confirmation step on money-related AI actions such as sending invoices.

## Warnings and mistakes

- Asking an AI builder for many things at once used to lead to hallucinations and partial work; Replit now queues prompts and limits this.
- Resend will not send from an unverified domain; the invoice email failed until DNS records were added and a verified FROM address was set.
- In the US, texting customers, including transactional texts, requires A2P registration that takes about 2 weeks.
- Invoices sent from a generic no-reply address landed in spam, and Resend advises that open tracking can reduce deliverability.
- Waiting for a perfect launch (design, logo, marketing plan) means you may never launch.

## Tools mentioned

Replit Agent 3 (AI vibe-coding app builder that can run autonomously for up to 200 minutes and self-test in a browser), Google Trends (Check demand trend for a keyword; free), Stripe (Payment links and card processing; about 2.9% per payment), Resend (Transactional email API; free plan likely sufficient), OpenAI API (Natural language parsing of invoice requests), Twilio (SMS integration (not built in the MVP); $1/month per phone number), Namecheap (Domain registration and DNS; $11 for invoicefree.com), ChatGPT (Help with API setup steps), TK Owners (Host's community of founders, including a pod for vibe coders (promotion))
