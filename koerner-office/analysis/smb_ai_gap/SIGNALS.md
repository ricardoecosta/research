# Signal map: playbook variables -> scanner columns

Sources: `~/hustling/playbooks/ai-support-agency-manual.md` (§3.2 10-factor scorecard /50, §3.3 red flags, §3.6 pain/signal table, §3.8 sourcing, tracker and qualification, §5.1 ICP/signals/disqualifiers, §9 research prompt), `niche-ranking-uk-portugal.md` (12-factor /60), `clarityrelay-operating-brief.md` (§3 ICP, buying committee, disqualifiers).
Code: `tools/smb_ai_gap_scan.py` (crawl) + `tools/smb_playbook_score.py` (scoring; can rescore a CSV without re-crawling).
Rules: public pages only, robots.txt respected, no form submissions, no chatting with bots, no personal contact data (contact-type signals are yes/no only).

Legend: **OBS** = measured by the scanner; **PROXY** = measured indirectly (weak); **UNKNOWN** = can't be seen from outside, so ask in discovery (the column is "unknown").

## Scorecard factors (scale 1-5, playbook weights x1)

| # | Factor (manual /50, niche /60) | Status | How it's measured / column |
|---|---|---|---|
| 1 | Ticket volume | UNKNOWN | `m1_ticket_volume=unknown`, `ticket_volume=unknown`. Ask: requests per month by channel |
| 2 | Knowledge complexity | OBS | `m2_*`: docs/PDF/datasheet counts (homepage + sitemap, EN/PT/ES keywords) + compatibility/warranty/installation keywords (`compat_kw`, `warranty_kw`, `install_kw`) |
| 3 | Existing support team | PROXY | `m3_*`: tech-support page, support role-address present (yes/no), help centre, chat/helpdesk vendor, support roles on the company's own careers page (`support_hiring`) |
| 4 | Ability to pay | UNKNOWN | `m4=unknown`. Size band isn't wired (Companies House/Informa/eInforma need keys or are paid). Ask: budget owner, setup + monthly fee |
| 5 | Tech signal | OBS | `m5_*`: public docs/help centre/FAQ + `chat_type` (none / live_chat_non_ai / ticket_helpdesk_only / ai_capable_vendor / custom_chat / ai_agent). A modern AI agent scores 1 |
| 6 | Reachability (manual: association/chamber/warm intro) | PROXY | `m6_*`: 4 if found via a trade-association directory, else 3 |
| 6' | Async reachability (niche /60) | UNKNOWN | `n6=unknown`. Needs a named buyer reachable by email or LinkedIn, which we don't collect |
| 7 | Recurring need | OBS | `m7_*`: catalogue size (product URLs), new products/launch pages, doc depth |
| 8 | Prospect density | OBS | `m8_*`: number of discovered firms in the same country and sector (>=100 → 5, >=50 → 4, >=20 → 3, >=10 → 2) |
| 9 | Low DIY risk (not solo/indie) | PROXY | `m9_*`: careers page, site size, association membership, support signals. `solo_or_micro` flag |
| 10 | Competitive whitespace (not a commodity receptionist) | OBS | `m10_*`: manufacturer wording, complexity; receptionist-type or local-trade wording lowers it |
| 11 | Founder advantage (niche /60) | OBS | `n11_*`: PT 5, UK 4, ES 3 (Ricardo: Portuguese, UK-based) |
| 12 | Ease of list building (niche /60) | OBS | `n12_*`: 5 if from an association directory, 3 if from open data |

Totals: `manual50_known`, `manual50_unknowns`, `manual50_est` (unknowns filled at a neutral 3); the same for `niche60_*`. `manual_pass_est` = est >= 35, no 1 on factors 2/3/9, and no disqualifier (factor 4 is unknown, so the manual's "no 1 on factor 4" rule can't be checked). `manual_strong_est` = est >= 40.

## Signals (manual §3.6, §5.1; ClarityRelay ICP)

| Signal | Status | Column |
|---|---|---|
| Large FAQ/help centre; "contact support" everywhere | OBS | `faq_or_support_page`, `help_centre`, `tech_support_page` |
| PDFs, spec tables, manuals | OBS | `pdf_links`, `datasheet_links`, `sitemap_doc_urls`, `doc_heavy` |
| Hiring support staff | PROXY | `careers_page`, `support_hiring` (own careers page only; LinkedIn/job boards not crawled because of ToS) |
| Multilingual / global customers / time zones | OBS | `languages` (hreflang and language paths), `export_kw` |
| Pre-sales compatibility questions | OBS | `compat_kw` |
| Old chatbot that only links to docs (Help Scout/Zendesk/Intercom/LiveChat/Drift/Tidio) | OBS | `chat`, `helpdesk`, `chat_type` (vendor fingerprint from scripts, network requests and DOM; the bot is never used) |
| No modern AI answer agent | OBS | `ai_bot`, `chat_type != ai_agent` (vendors with optional AI add-ons are flagged `ai_capable_vendor (AI add-on unknown)`) |
| Recent product launches/expansion | OBS | `new_products_kw` |
| Complex compatibility/warranty/policy questions | OBS | `compat_kw`, `warranty_kw`, `install_kw` |
| Support channels: chat, email, phone, ticketing, contact form | OBS (booleans) | `chat`, `support_email_present`, `phone_present`, `helpdesk`, `contact_form` |
| B2B manufacturer/distributor/technical supplier | OBS | `sector`, `source`, `manufacturer_kw` |
| Knowledge trapped in experts' heads (few docs) | OBS (inverse) | low `m2` / `no_public_docs` |
| Outdated docs | UNKNOWN | ask: when were the manuals last updated? |
| Internal HR/IT repetitive questions | UNKNOWN | ask |
| Large help centre but answers well already | UNKNOWN | needs human review (we don't talk to bots) |

## ICP firmographics and qualification checklist

| Item | Status | Column |
|---|---|---|
| 20-200 employees | UNKNOWN | `size_band=unknown` (no free, key-less source wired; next step: Companies House API key for the UK) |
| B2B/B2B2C maker/distributor | OBS | `sector`, `manufacturer_kw` |
| Real support function | PROXY | `m3`, `no_visible_support_function` |
| Public knowledge source | OBS | `doc_heavy`, `no_public_docs` |
| Visible volume or hiring signal | PROXY | `support_hiring`; volume UNKNOWN |
| Can reach a decision-maker / named buyer | PROXY | `leadership_page`, `named_contact_present` (yes/no only; no names stored) |
| Large enough to pay, too small for an in-house AI team | UNKNOWN | ask; multinationals in the lists (e.g. ABB, Amorim) are obvious by eye |
| Problem is complex, not "answer the phone" | OBS | `m10`, `receptionist_type` |
| Reachable region / trade show | PROXY | `country`, `source` (association) |

## Disqualifiers (`disqualifiers` column)

| Disqualifier | Status | Flag |
|---|---|---|
| Solo owner/installer, no support function | PROXY | `solo_or_micro`, `no_visible_support_function` |
| No public documentation | OBS | `no_public_docs` |
| Only needs a cheap phone receptionist (business type) | PROXY | `receptionist_type_business` |
| Local trade (installer/plumber etc.) | PROXY | `local_trade` |
| Highly regulated data | PROXY | `regulated_data` |
| Already runs a modern AI agent | OBS | `already_has_ai_agent` |
| No budget for £1k pilot / $2k setup + monthly | UNKNOWN | ask |
| Wants a free pilot or custom build first | UNKNOWN | ask |
| "We'll use ChatGPT / build it ourselves" | UNKNOWN | ask |
| Price shopper, no urgency | UNKNOWN | ask |
| Wants safety/compliance/legal advice from the bot | UNKNOWN | ask |
| Wants every product and channel in the pilot | UNKNOWN | ask |
| No access to the decision-maker | UNKNOWN | ask |

## Tracker columns (manual §3.8)
Company, Website, Sub-niche (`sector`), Signal (`chat_type` + `disqualifiers`), Docs/help URL (counts only), Chat/ticketing vendor (`chat`, `helpdesk`) and Source are filled. Employees (est.), estimated tickets per month and loaded cost per hour are unknown. Contact name, title, LinkedIn and support email/phone values are **not collected by design** (yes/no only).

## Coverage
50 playbook variables mapped: **23 observed**, **12 proxied** (weak public evidence), **15 not observable from outside, so ask in discovery**. Of the 13 scorecard factors (10 manual plus 3 extra in the /60 model), 3 are unknown: ticket volume, ability to pay and async reachability. That is why every row carries `manual50_unknowns=2` and `niche60_unknowns=3`.
