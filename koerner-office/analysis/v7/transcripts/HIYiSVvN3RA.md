# I Built an App the Government Doesn't Want You to See

- **Video:** [HIYiSVvN3RA](https://www.youtube.com/watch?v=HIYiSVvN3RA) · **Channel:** The Koerner Office · **Uploaded:** 2026-04-07 · **Length:** 8 min · **Transcript:** transcribeyoutube
- **Speakers:** Chris Koerner (host) · **Format:** tutorial_howto
- **Evidence quality:** C — Sponsored build demo with no users, revenue or business model; market figures are second-hand. · Promotional conflict: Replit is a partner/sponsor of the podcast.
- **Extraction:** grokbot · quotes verified 14/14

## Summary

Chris Koerner builds GovDealFinder, a simple search front end over SAM.gov federal contract listings, using Replit Agent 4 with a Claude-written prompt and the free SAM.gov API, in about four minutes. He adds email alerts for new contracts matching saved filters, SEO blog posts, an eligibility quiz, a generated pitch deck, and publishes on a $12 domain. The pitch: the US government spent $834 billion on contracts last year, about $200 billion is reserved for small businesses, and SAM.gov is clunky. The video is a Replit sponsorship; no revenue or monetisation model is discussed.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Government contract finder built on the SAM.gov API** — A simple search and email-alert site that lets small businesses type what they do and their state to find federal contracts they can bid on. | data_leads | moderate | 4/5/5/5/4 | 3 |

### I1. Government contract finder built on the SAM.gov API

- **Customer:** US small business owners and aspiring owners (e.g. tree trimming, lawn care, IT, construction)
- **Problem:** SAM.gov is clunky and hard to filter, so most small businesses never find contracts
- **Offer:** Search by business type and state with dollar amounts, eligibility quiz, email notifications when matching contracts appear, SEO blog content
- **Business model:** not stated (implied lead-gen/email list; could be subscription alerts)
- **Pricing:** not stated.  
- **Acquisition:** seo_organic_search: Blog posts generated for government contract search terms; Google Trends and Ahrefs showed demand.; existing_audience: Promoted to Chris's YouTube audience.
- **Delivery:** Web app pulling data from the SAM.gov API, built and hosted on Replit; automated email alerts.
- **Unit economics (claims):** Built in about 4 minutes vs $10-20k with developers; Domain $12
- **Tools:** Replit Agent 4, Claude, SAM.gov API, Google Trends, Ahrefs
- **Startup cost:** $12 domain plus Replit subscription
- **Time to first revenue:** not stated
- **UK applicability [E]:** 3/5 — UK equivalent would use Contracts Finder and Find a Tender (public data with APIs); many competitors already exist. Alert emails require opt-in consent under PECR, which the sign-up flow provides.
- **Risks:** Monetisation not defined; Easy to copy; many existing bid-finder services; Dependence on government API access; Avoid fake social proof (Chris rejected a fake success story variant)
- **Automation [E]:** acquisition 4/5 (SEO content and programmatic pages per industry/state can be agent-generated; inbound only.); onboarding 5/5 (Self-serve search and email sign-up.); delivery 5/5 (API data refresh and alert emails run unattended.); billing 5/5 (Subscription billing if monetised.); support 4/5 (FAQ and agent support.)
> "Type in what your business does, pick your state, and see contracts you can actually bid on with dollar amounts" — Chris Koerner (~0:49)
> "add a way for people to be able to subscribe to get email notifications when new contracts appear that match their filters" — Chris Koerner (~4:04)

## Revenue and metric claims (unverified claims)

- **US government spent $834B on contracts last year** (other, second-hand, claimant: Chris Koerner)
  > "The US government spent $834 billion on contracts last year" — Chris Koerner (~0:00)
- **About $200B of federal contracts are reserved for small businesses** (other, second-hand, claimant: Chris Koerner)
  > "about 200 billion of that is reserved for small businesses" — Chris Koerner (~8:05)
- **SAM.gov gets 2.2M visits a month** (traffic, second-hand, claimant: Chris Koerner)
  > "This website gets 2.2 million visits a month, and it's an ugly website" — Chris Koerner (~0:26)
- **Such a website would normally cost $10-20k to build** (cost, second-hand, hypothetical, claimant: Chris Koerner)
  > "a website like this would normally cost between 10 and 20,000 to build" — Chris Koerner (~1:00)
- **Front end generated in about 4 minutes** (hours, first-hand, claimant: Chris Koerner)
  > "Okay, that took about 4 minutes" — Chris Koerner (~3:16)
- **Domain cost $12** (cost, first-hand, claimant: Chris Koerner)
  > "I'm going to spend 12 bucks, buy the domain name" — Chris Koerner (~7:21)
- **Replit referral gives $10 in free credits** (other, second-hand, claimant: Chris Koerner)
  > "you'll get 10 bucks in credits for free" — Chris Koerner (~7:55)

## Tactics and playbook steps

**Wrap a clunky government data site with a simple front end** (product)
1. Find an ugly but high-traffic public data site (SAM.gov, 2.2M visits/month)
2. Get a free API key from the source rather than scraping
3. Ask Claude to turn a three-sentence idea into a detailed build prompt
4. Paste into Replit Agent 4 and let parallel agents build back end, front end and landing page
5. Add saved-filter email alerts with a pop-up after first search
6. Add SEO blog posts and an eligibility quiz
7. Buy a cheap domain and publish
> "this key will enable me to pull all the data I need from sam.gov without having to scrape or work around any of their restrictions" — Chris Koerner (~2:52)

**Use demand tools to pick the space** (product)
1. Check Google Trends and Ahrefs for rising search interest
2. Build in the space they flag
> "Google Trends and AHRefs and all these other random tools were screaming at me, there's opportunity here" — Chris Koerner (~7:32)

## Lessons

- *niche_selection*: Ugly, hard-to-use public data sites are opportunities for simple paid or lead-gen front ends.
- *automation_ai*: Use one AI to write a detailed prompt for another AI builder.
- *legal_risk*: Use official APIs instead of scraping to avoid restrictions.
- *customer_acquisition*: Saved-search email alerts turn one-time visitors into a list.
- *automation_ai*: Non-coders can ship working web apps in minutes with agentic builders.

## Warnings and mistakes

- Don't use fabricated success stories on landing pages.
- The video is sponsored by Replit and shows no traction or revenue.

## Tools mentioned

Replit Agent 4 (AI app builder with parallel agents, canvas variations, pitch deck generation, publishing (sponsor); $10 free credits via referral), Claude (Writing the build prompt), SAM.gov API (Federal contract opportunity data; free), Google Trends (Demand research), Ahrefs (SEO/keyword research)
