# I Asked AI to Help Me Beat the Stock Market

- **Video:** [KYtg48UoEQ8](https://www.youtube.com/watch?v=KYtg48UoEQ8) · **Channel:** The Koerner Office · **Uploaded:** 2025-10-15 · **Length:** 12 min · **Transcript:** ok
- **Speakers:** Chris Koerner (host) · **Format:** tutorial_howto
- **Evidence quality:** C — First-hand, screen-shared build with specific cost and time figures, but the return figure is a hobbyist backtest with survivorship bias and missing data. The business element is a minor aside with no revenue. · Promotional conflict: Promotes Replit (a frequent tool of the host) and the host's own email-gated site.
- **Extraction:** grokbot · quotes verified 17/17

## Summary

Chris Koerner shows how he vibe-coded a stock portfolio backtesting app in Replit (Agent 3) to test his thesis that founder-led S&P 500 companies with strong network effects beat the market. He used ChatGPT deep research to find candidates, then built a live Google Sheet using the GOOGLEFINANCE formula, and used GPT for Sheets to score every S&P 500 company 1-10 on network effects and founder leadership for about $15 in credits. Replit then turned the sheet into a filterable dashboard. On his 8-10/8-10 filter over 10 years he reports 22.4% vs the S&P's 9% weighted and 12% unweighted. He shares about a dozen ChatGPT prompts for generating stock-picking theses and says he put the free tool ("Nel Stocks") behind an email form on a domain he bought. The business angle is small: a free, email-gated vibe-coded tool used as a lead magnet. Most of the video is personal investing, not a business.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Free vibe-coded niche tool gated behind an email form (lead magnet)** — Build a niche data tool quickly with an AI coding agent, put it on its own domain, and give it away in exchange for an email address. | content_media | moderate | 3/5/5/5/4 | 3 |

### I1. Free vibe-coded niche tool gated behind an email form (lead magnet)

- **Customer:** Retail investors interested in stock-picking frameworks
- **Problem:** Retail investors lack an easy way to backtest a simple thesis against the S&P 500
- **Offer:** Free web app (Nel Stocks) that filters S&P 500 companies by network-effect and founder-led scores and charts returns vs the index
- **Business model:** Free tool as an audience and email-list builder; no monetisation stated
- **Pricing:** free (email required).  Host says there is nothing to pay for; you just enter your email.
- **Acquisition:** youtube: Tool promoted in the host's video; access requires email sign-up.
- **Delivery:** Replit Agent 3 app reading a live Google Sheet (GOOGLEFINANCE prices, GPT for Sheets 1-10 scores). Built in about 45 minutes of prompting.
- **Unit economics (claims):** About $15 of GPT for Sheets credits to score all S&P 500 companies; About 45 minutes of prompting to build the app
- **Tools:** Replit, ChatGPT deep research, Google Sheets, GPT for Sheets, Wikipedia
- **Startup cost:** About $15 AI credits plus a domain and Replit plan (not quantified)
- **Time to first revenue:** not stated (no revenue model)
- **UK applicability [E]:** 3/5 — Works in the UK, but investment tools risk FCA financial-promotion and advice rules if they recommend stocks. Keep it educational with disclaimers. Email capture needs UK GDPR consent, and PECR consent for marketing emails.
- **Risks:** Backtests are survivorship-biased (current S&P 500 constituents) and incomplete (missing IPO data); Could be seen as investment advice or a financial promotion; No revenue model stated; AI-generated scores may be inaccurate
- **Automation [E]:** acquisition 3/5 (Inbound from content; the email gate captures leads automatically. Any later marketing emails need consent under UK PECR (opt-in at sign-up).); onboarding 5/5 (Self-serve email form.); delivery 5/5 (Web app with prices auto-refreshed via the GOOGLEFINANCE formula.); billing 5/5 (No billing; free.); support 4/5 (Minimal; AI FAQ.)
> "I went and bought a domain name, ntocks.com. I put this free website behind an email form." — Chris Koerner (~11:56)
> "this probably took 45 minutes of prompting. All in all, boom, right here. It's called Neil Stocks, NEL, Network Effects, Founderled." — Chris Koerner (~7:57)

## Revenue and metric claims (unverified claims)

- **Scoring all S&P 500 companies with GPT for Sheets cost about $15 in credits** (cost, first-hand, claimant: Chris Koerner)
  > "I just drugg it down. It cost me like 15 bucks in credits and I got this sliding scale of how much a company has network effects" — Chris Koerner (~5:56)
- **The app took about 45 minutes of prompting to build** (hours, first-hand, claimant: Chris Koerner)
  > "And so at the end of the day to see the final product, this probably took 45 minutes of prompting." — Chris Koerner (~7:54)
- **Filtered portfolio returned 22.4% vs S&P 9% weighted and 12% unweighted over 10 years (backtest)** (other, first-hand, hypothetical, claimant: Chris Koerner)
  > "The S&P has returned 9% over this time frame weighted and 12% unweed and this portfolio would have returned 22.4%." — Chris Koerner (~8:28)
- **Initial ChatGPT deep research found 26 S&P 500 companies that are founder-led with network effects** (other, first-hand, claimant: Chris Koerner)
  > "Find me all of the companies in the S&P 500 that have both network effects and are still founderled." There were 26 of them." — Chris Koerner (~3:02)

## Tactics and playbook steps

**Use GPT for Sheets to score a list at scale** (operations)
1. Put the entity names in a Google Sheet column
2. Write a prompt with a 1-10 rubric that references the cell
3. Drag the formula down the whole column
4. Use the scores as filterable data in an app
> "I had a prompt that said tell me on a scale of 1 to 10 and then I inserted the name of the company how much in this case Kagra Brands enjoys network effects." — Chris Koerner (~5:15)

**Point a vibe-coded app at a live Google Sheet and define every column** (product)
1. Start with a hardcoded spreadsheet upload for a rough draft
2. Replace it with an editable live Google Sheet link as the database
3. Explain what each column means rather than letting the AI guess
4. Request formatting fixes and a visible list of filtered rows to check the math
> "Now, it can surmise what each column means, but I don't want to assume that it knows. I would rather get ahead of it, take a few more extra minutes" — Chris Koerner (~7:23)

**Gate a free tool behind an email form** (acquisition)
1. Buy a domain for the tool
2. Require an email to access
3. Promote it in content
> "You just got to put in your email and you can play around with it." — Chris Koerner (~12:05)

## Lessons

- *automation_ai*: Give the AI coding agent explicit definitions of your data rather than letting it infer them; it reduces errors.
- *automation_ai*: Newer agents (Replit Agent 3) test and fix their own builds, removing much of the prompt-debug loop.
- *automation_ai*: AI-in-spreadsheet tools let you turn fuzzy judgements into numeric scores across hundreds of rows cheaply.
- *validation_testing*: Ask the app to show the underlying rows so you can verify the filtering and the maths.
- *customer_acquisition*: A quick free tool on its own domain can double as an email list builder.
- *other*: Look for mismatches between fundamentals and price, such as a company holding more cash than its market value.

## Warnings and mistakes

- Host admits impulsive retail trading is not good and frames the tool as a way to avoid risking family finances.
- Data was incomplete; some filtered companies lacked valid IPO price data, so results should be verified.
- The backtest uses today's S&P 500 constituents (survivorship bias) and is not investment advice; this is an extractor note, not said in the video.

## Tools mentioned

Replit (Agent 3) (Vibe-coding the app; agent self-tests and fixes the app), ChatGPT deep research (Finding candidate companies and building the initial spreadsheet), Google Sheets (GOOGLEFINANCE formula) (Live price data as the app's database), GPT for Sheets (Running AI prompts per row to score companies; about $15 in credits), Robinhood (Host's brokerage; chart style inspiration), Wikipedia (Source for IPO dates and prices)
