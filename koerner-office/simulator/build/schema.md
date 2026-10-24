You are tagging business opportunities for Ricardo's "constraint simulator". Use ONLY the context given (it comes from his research reports). Never invent numbers: if a value isn't in the context and can't be reasonably estimated from it, use null and status "unknown". Estimates are allowed for hours/budget/months when the context gives the model type (mark the reason "est."). Ricardo: UK-based (Bromley), technical, Portuguese/Spanish/English, wants a software/digital/data business run by AI agents.

For each input record output one object:
{
 "id": <same id>,
 "name": <short clean name, <=70 chars>,
 "description": <one sentence, <=30 words>,
 "model_type": one of ["app","saas","plugin/extension","directory/seo","content/media","digital product","data/api","marketplace","ecommerce/physical","service/agency","local service","acquisition","other"],
 "track": "build" | "buy",
 "markets": list of ISO-ish codes from ["UK","US","EU","PT","ES","DE","BR","MX","CA","CO","AU","GLOBAL"] (GLOBAL = sells online worldwide),
 "revenue": {"text": <revenue claim quoted/paraphrased from context or "unknown">, "gbp_mo_low": number|null, "gbp_mo_high": number|null}   (convert $ at 0.75, € at 0.85; monthly; only from claims in the context — the operator's/listing's revenue, not a forecast),
 "verdicts": [{"round": "v8".., "verdict": "pursue"|"maybe"|"kill"|"seen", "confidence": str|null, "reasons": [short strings, with rule codes like K0/K2/C9 when present]}],
 "c": { constraint_key: {"s": "pass"|"soft"|"hard"|"unknown", "v": value, "r": "<=18-word reason"} }
}
Constraint keys (all required):
- "automation": v = % of all work automatable by agents (int). hard <50, soft 50-60.
- "hours": v = Ricardo's steady-state hours/week (number; for a bought business after handover). hard >5 (soft if 5-8 and uncertain).
- "local": v = true if it sells to local businesses / high-street / local trades (or needs local sales). hard if true.
- "face": v = true if it needs Ricardo's face, voice, personal brand or a seller-dependent brand. hard if true.
- "outreach": v = "none" (inbound: SEO, app store, marketplace, ads, integrations), "lawful_cold" (cold email to company inboxes/B2B where opt-out law allows), or "unlawful_cold" (cold SMS/calls/DMs, emailing individuals/sole traders in UK/EU, scraped emails in PT/ES). pass if none, soft if lawful_cold, hard if unlawful_cold.
- "digital": v = true if software/digital/data product; false for physical goods, inventory, or services Ricardo/staff must deliver. hard if false.
- "interest": v = 0-10 fit/interest to Ricardo (use the report's fit score when present). soft <6, hard <4.
- "budget": v = upfront £ needed to start or buy (for acquisitions: asking price ×0.75). pass <=50, soft <=5000, hard above unless buy-track (soft up to 150000 for buys).
- "first_revenue": v = months to first £ (est. ok). pass <=3, soft <=6, hard >6.
- "moat": v = months a rival would need to copy it (est.; 0.5 for a UI/prompt/clone; use defensible_asset or K0/time_to_moat if given: K0 kill => <3). pass >=3, soft 1-3, hard <1. Also "score": defensible asset 0-10 if given else null.
- "evidence": v = 0-3: 0 none/self-described failure, 1 anecdotal, unverified or older than 18 months, 2 dated (<=18 months) first-hand revenue claim or paying-proof snippets, 3 verified revenue (verified listing/Stripe) or validated paid demand. "count" = number of paying-proof items/operators if given else null. pass >=2, soft 1, hard 0.
- "crowded": v = number of competitors/incumbents/new launches mentioned (int or null). hard if killed for K2 (>=2 launches in 6 months), K4 (>=5 incumbents at price floor) or "crowded/price war/saturated"; soft if several competitors; pass otherwise.
- "platform": platform-owner or platform-policy risk (K3, platform bans, API control, app-store removal, Google updates). v = short label or null. hard if killed for it.
- "claim_age": K5: hard if the only payment evidence is >18 months old ("~20-year-old evidence", stale); v = newest claim date YYYY-MM or null.
- "dead_demand": K6: hard if need/regulation/platform withdrawn or users gone. v = bool.
- "legal": other legal/regulatory risk (e.g. UK legal risk flag, licensing, liability, data protection) – hard only if the report killed it for this. v = short label or null.
Status should mirror why the report killed it where the report says so (e.g. checklist C9 => hours hard; C7 => face hard; C3 => budget (price multiple) soft/hard; C1/C2 missing or off => evidence; K0 => moat hard; K1 => whichever hard rule; K2/K4 => crowded; K3 => platform; K5 => claim_age; K6 => dead_demand). For v11 checklist kills ("checklist too many missing") use "unknown" for the missing items.
Return ONLY JSON: {"records":[...]} in the same order as the input. Be terse.
