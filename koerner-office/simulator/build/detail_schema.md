You are writing the detail view for each business opportunity in Ricardo's research simulator. Use ONLY the source text given for that record (his research reports). Do not invent anything. If a field isn't in the sources, use null (it will be shown as "not in sources"). Plain English, concise, no hype. Keep quotes of numbers exactly as the source states them (currency, dates).

For each input record output:
{
 "id": same id,
 "summary": 2–4 sentences: what the idea/business is and what it would do (from the sources),
 "how_money": how it makes money (pricing/revenue model) or null,
 "customer": target customer, or null,
 "market": market/country/geography, or null,
 "revenue_claims": [{"claim": exact-ish figure and what it is, "date": "YYYY-MM(-DD)" or null, "who": "first-hand"|"second-hand"|"listing (seller-stated)"|"listing (verified)"|"estimate"|null}],
 "paid_demand": one or two sentences on proof that people pay (paying-proof snippets, verified revenue, pricing pages), or null,
 "competitors": [{"name": str, "price": str|null, "note": str|null}]  (competitors, incumbents, comparables, recent launches named in the sources),
 "rounds": [{"round": "v8"|"v9"|"v10"|"v11"|..., "stage": e.g. "transcript scoring","kill-check","scoring","checklist","validation","shadow check", "verdict": e.g. "kill"|"survive"|"pursue"|"maybe"|"seen", "score": e.g. "success 3/10, fit 7/10, moat 2/10" or null, "codes": ["K0","C9",...], "plain": the reason in plain words, 1–2 sentences, explaining what any code means (K0 = moat too weak to take 3+ months to copy; K1 = breaks a hard rule; K2 = 2+ competing launches in 6 months; K3 = platform owner/partner already serves it; K4 = 5+ incumbents at the price floor; K5 = only payment evidence older than 18 months; K6 = demand gone; C1 revenue not verified; C2 revenue under $1k/mo or no profit; C3 price outside $20k–150k or over 5× profit; C7 depends on seller's face/brand; C9 no plausible handover to ≤5 h/week; "too many missing" = over 3 of 9 listing checklist rows missing)}],
 "risks": [short strings] or [],
 "moat": the moat / defensibility assessment from the sources, or null,
 "hours": {"value": str like "5 h/week", "est": true if it's a model/AI estimate (e.g. text marked [E], "estimated", scored by the pipeline) and false if stated by an operator/seller, "note": short} or null,
 "budget": same shape (upfront cost / asking price) or null,
 "first_revenue": same shape (time to first revenue) or null,
 "next_steps": test plan, due-diligence step, seller questions or next steps if the sources give any, else null
}
Return ONLY JSON {"records":[...]} in input order.
