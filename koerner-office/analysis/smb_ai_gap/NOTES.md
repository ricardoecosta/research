# Backlog 10: SMB AI-gap scanner (PT, UK, ES)

24 Oct 2026 (UK time). This covers the exploration only. Nothing was sold, nobody was contacted and nothing was spent.

## 1. Source

**Video:** *The Easiest Way to Make Money With AI Right Now*
- Channel: Chris Koerner on The Koerner Office Podcast
- Guest: Aaron Edwards, founder of DocsBot AI
- Link: https://www.youtube.com/watch?v=22Jpzt683jw
- Published 11 Oct 2026; 37:47 long
- Transcript: `transcripts/raw/22Jpzt683jw.txt`
- Mined record: `analysis/v8/ideas_flat.jsonl`, `22Jpzt683jw`

**The model:**
- Sell a done-for-you AI support agent to an SMB that already has:
  - a support team
  - a large body of product documentation
  - repetitive customer questions
- Train the agent on the company's own manuals, spec sheets and FAQs.
- It answers with citations and hands off anything uncertain to a human.
- Charge roughly $2,000–3,000 to set it up and $500–1,000 a month to run it. A robot writes the monthly report.
- The guest sells the underlying platform, DocsBot, so his claims are biased.

**Claims (all unchecked):**

| Claim | Who said it | When / how old |
|---|---|---|
| DocsBot reached about $10k MRR with hundreds of customers within 3 months of launch | Guest | Launch was about 3.5 years before the interview, so about spring 2023. The event is about 3 years old. |
| DocsBot is now over $1M ARR, with a gross margin above 90% | Guest | Current as of Oct 2026 |
| About $130 average revenue per user, about 3% revenue churn | Guest | Current as of Oct 2026 |
| Cancellations saying "we'll build our own" rose from about 1% to about 13% | Guest | Current as of Oct 2026 |
| Agency pricing: "$2 to $3,000 to set this up … $500 to $1,000 a month" | Host's framing (second-hand) | Undated |
| Each lead from a conference demo was worth about $2,000 | Guest | Undated |
| A client said the service would save it over $100k a year (the guest's 19-year-old son's first contract) | Second-hand | Undated |

**Playbooks.** Three were written on 20 Oct 2026 in `~/hustling/playbooks/`. That folder is outside the repo and not in git.
- `ai-support-agency-manual.md`: about 97 KB, distilled from this video.
- `clarityrelay-operating-brief.md`:
  - Brand: ClarityRelay.
  - Customers: UK commercial and architectural lighting firms.
  - Pricing: a £1,000 pilot credited against a £2,000 setup, then £500 a month.
  - Selling: async cold email and LinkedIn.
- `niche-ranking-uk-portugal.md`:
  - First choice: UK lighting and electrical.
  - Second: UK construction products.
  - Portugal angle: cork, ceramics and stone exporters.

**History in the repo:**
- v1 ranked this idea #1 at 4.25 ("Done-for-you AI support agents for SMBs", `analysis/opportunity-shortlist.md` at `1e03f1b^`).
- `tools/chat_widget_scanner.py` and the Bromley trades scan were added in commit `2c99d5c`.
- The 30-company prospect list is `~/hustling/data/prospects-starter.csv`, built from Lighting Industry Association (LIA) member pages.

**Other candidates:**
- `McQucrnkSt0` (Aug 2026): a local agency selling chat widgets and AI receptionists. It's a local-business model, so it's ruled out.
- `WpZE-vfLHuA` (Aug 2025): an AI automation consultant for local trades. Also local, also ruled out.

## 2. Can the exploration be automated?

Yes for the scanning. The constraint is the company lists, which vary by country.

| | UK | Portugal | Spain |
|---|---|---|---|
| Company universe | Companies House free bulk CSV and API (SIC codes, but no websites). Trade directories have websites: LIA, BEAMA, and the Construction Products Association (25,728 companies per the niche-ranking doc). | No free bulk register with CAE codes and websites that I know of. Sector associations: APCOR (200+ cork members), APICER (ceramics), and AICEP exporter listings. Commercial aggregators (Racius, eInforma) have restrictive terms. | BORME (the official commercial bulletin) is free open data but has no websites. The ICEX exporter directory and the chambers of commerce have websites. eInforma and Axesor are paid. |
| Finding websites | Directory pages; OSM `website` tags (mostly local shops) | Association pages | ICEX and association pages |
| Signal keywords | English (built) | Need Portuguese: manual, ficha técnica, perguntas frequentes, downloads, documentação | Need Spanish: manual, ficha técnica, preguntas frecuentes, descargas, documentación |
| Verdict | **High.** The proof of concept below runs end to end. | **Medium.** Lists are thin and hand-assembled, and the pool is small. | **Medium–high.** Exporter lists are good; keywords need localising. |

`tools/smb_ai_gap_scan.py` uses only the Python standard library:
- It reads `robots.txt` and skips the site on 401/403 or a Disallow rule.
- It reads the homepage and up to 25 sitemaps.
- It counts documentation, PDF, FAQ and product URLs, detects chat and AI-bot signatures (reusing `chat_widget_scanner.py`), and gives an `ai_gap_score` from 0 to 100:

| Component | Max points |
|---|---|
| Documentation depth | 40 |
| Catalogue size | 20 |
| FAQ or support page | 15 |
| No chat or bot (human chat only scores 10) | 25 |

- It collects no contact data.

Google Places would cost money, so it was avoided. OSM and the directories are free.

## 3. Proof of concept: 30 UK lighting manufacturers and distributors

The input is the company names and URLs only, from the LIA-sourced prospect list. Output: `poc_uk_lighting_2026-10-24.csv`. It took about 1 minute and cost £0.
- 30 of 30 sites fetched OK. 25 have a sitemap, 15 have a FAQ or support page, and 15 have at least 100 product URLs.
- 15 sites scored 50 or more. The top 5:

| Company | Score |
|---|---|
| Ecosense | 84 |
| Advance LED | 81 |
| British Electric Lamps | 78 |
| Aurora | 72 |
| BEX/Robus | 70 |

- **Chat detection undercounts badly in static mode.** It found chat on 1 of 30 sites. The earlier research for the prospect list recorded chat on 17 of 30: Crisp 10, HubSpot 5, Tawk 1, LiveChat 1. Most widgets are injected by JavaScript or Tag Manager after the page loads.
  - A real run needs the existing scanner's `--render` mode (Playwright).
  - It found 0 AI bots, but that number isn't reliable until the render pass is done.
- Sitemaps rarely list PDFs (the PDF count was 0 on most sites), so the score leans on product and documentation URLs.
- Next scanner step: crawl 2–3 product pages per site and count datasheet links.

## 4. Rule check

**The exploration itself breaks no rule.** It reads public pages, respects robots.txt and stores no personal data.

**Monetising it the ClarityRelay way does run into his rules.** That means selling a done-for-you bot to SMBs through async cold email.

1. **Selling to businesses.** The buyers are manufacturers and distributors, not local shops, so it isn't the "local business" model he ruled out. But in practice it's the same agency motion (setup fee, retainer, client support), and v1–v10 kept failing it on hours and outreach.
2. **Cold outreach**, which he declined to loosen when choosing v10 ("same constraints"):

| Country | Rule | Implication |
|---|---|---|
| UK (PECR) | Unsolicited B2B email is allowed to corporate subscribers (Ltd companies, LLPs) if you identify yourself and offer an opt-out. Sole traders and partnerships need consent. | Lawful for Ltd companies, but outside his chosen rules. |
| Portugal (Lei 41/2004, art. 13.º-A/13.º-B) | Unsolicited marketing to legal persons is allowed until they object. You must check the national objection list (DGC), which is updated monthly. Individuals need prior consent. ANACOM also calls automatically harvesting emails from the public web to build marketing databases unlawful. | Lawful B2B with care. Building the list by scraping emails is unlawful. |
| Spain (LSSI art. 21) | Commercial email needs prior express consent even for B2B. The only exception is an existing customer and similar products. The data-protection authority (AEPD) says GDPR legitimate interest doesn't override this. | Cold email is unlawful. |

Sources:
- https://dgsl.pt/legislacao/lei_41-2004/artigo/13-a
- https://anacom.pt/render.jsp?contentId=1140912
- https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758
- https://www.aepd.es/documento/2018-0173.pdf

**Routes that need no outreach:**
- **(a) Self-serve "AI support readiness" audit.** A company pastes its URL and gets a free report on documentation depth, chat or bot coverage and estimated deflectable questions, with a paid fix or a referral. It's found through search, LinkedIn content and benchmark reports. This route fits his rules best.
- **(b) Sell the scan data or sector benchmark to AI chatbot agencies and vendors** (DocsBot partners, Crisp or Tidio agencies). This is a B2B data product. The buyer does any outreach under their own compliance. Company-level data is mostly not personal data, but don't store named contacts.
- **(c) Referral or partner fees.** Pass consenting inbound leads from (a) to an agency.
- **(d) Public benchmark content**, for example "State of AI support in UK lighting, 2026", to feed (a).

## 5. The v11 chatbot kill

v11 killed the Flippa listing "AI customer service chatbot platform for SMBs" (flippa.com/14142133, $45k):
- Revenue was down about 35% on its 12-month average, breaking the "more than 30% decline" rule.
- Profit at the current run-rate is near zero.
- Its "SMB" customers were undefined.
- The category is crowded and cheap.

This idea differs in that it's the discovery and audit layer, not owning a generic chatbot SaaS. But any route that ends in selling bots inherits the same crowding. The guest's own "we'll build our own" cancellations went from 1% to 13%. So the defensible part is the scan data and audit, not the bot.

## 6. Recommended next step (£0)

1. Re-run the 30 sites with `chat_widget_scanner.py --render` to calibrate chat detection against the 17 of 30 already known.
2. Add Portuguese and Spanish keywords plus a product-page datasheet count.
3. Scan one exporter list per country, about 100 sites each: LIA/BEAMA for the UK, APCOR or APICER for Portugal, the ICEX directory for Spain.
4. Then decide between route (a), the audit tool, and route (b), the data product for agencies. No outreach either way.
