# Backlog 10: where can we lawfully cold-email doc-heavy SMBs?

24 Oct 2026 (UK time). Desk research only. **Not legal advice.** Nobody contacted, nothing spent.
Scope: B2B cold email (and social DMs where a regulator says so) offering an AI support/knowledge assistant or an "AI readiness" audit to manufacturers, distributors and exporters with manuals, spec sheets and FAQs. Ricardo can operate in English, Portuguese and Spanish, from Bromley (UK).

Legend: ✅ opt-out regime (send first, honour unsubscribes) · ⚠️ workable with conditions · ❌ prior consent needed (cold email effectively dead).
"Uncertain" marks points I could not pin to a primary source this pass.

## Top 5 (ranked)

1. **United States** – Pure opt-out (CAN-SPAM), no B2B or sole-trader distinction, ~235k manufacturing firms under 500 staff, English, highest willingness to pay. Just don't scrape sites that forbid it.
2. **Brazil** – No federal anti-spam statute; B2B prospecting can run on LGPD *legitimate interest* (ANPD guide), Portuguese, very large industrial base (~669k manufacturing local units). Needs a documented balancing test and instant unsubscribe.
3. **Mexico** – No B2B email ban; new LFPDPPP (2025) works on privacy notice + tacit consent + right to oppose; ~634k manufacturing units; Spanish; many USMCA exporters with English/Spanish manuals.
4. **Canada** – Consent law (CASL), but "conspicuous publication" implied consent covers addresses a firm publishes itself when the pitch fits the recipient's role. ~47k manufacturing employers, English/French, US-level pricing. Harsh penalties, so keep records per address.
5. **Colombia** – Regulator (SIC) says corporate contact data of a legal entity (e.g. info@/ventas@) is **not** personal data under Ley 1581, so generic company addresses can be contacted; Spanish; honour cese/supresión requests. Named-person addresses need authorisation, so stick to generic inboxes.

Honourable mentions: **Argentina** (explicit opt-out under Ley 25.326 art. 27, but FX/payment friction), **Chile** (opt-out under consumer law art. 28 B; new GDPR-style Ley 21.719 in force 1 Dec 2026 adds uncertainty), **Singapore** (opt-out + `<ADV>` label, but bans harvesting software).
Lawful but bad for an *automated crawler*: **Australia** and **New Zealand** (inferred/deemed consent from conspicuous publication exists, but using harvesting software or harvested lists is itself prohibited).

## All countries

| Country | Cold B2B email? | Conditions | Sole traders | Scraping published addresses | DMs (LinkedIn/IG) | SMB density (cited) | Language | WTP / payment notes |
|---|---|---|---|---|---|---|---|---|
| **US** | ✅ | CAN-SPAM: truthful headers/subject, identify as ad, physical postal address, working opt-out honoured within 10 business days. No consent needed, applies to B2B too. [FTC guide][us1] | Same rules | Allowed in general; harvesting from a site that says it won't share addresses (or dictionary generation) is an **aggravated** violation, 15 USC 7704(b)(1) [us2] | CAN-SPAM covers email only; platform ToS bans automated DMs | 239,265 mfg firms, 235,088 <500 staff (Census SUSB 2022) [us3] | EN | Highest; USD cards/Stripe; $500–1k/mo plausible |
| **Brazil** | ⚠️ (opt-out in practice) | No federal anti-spam law. LGPD applies to named work emails; *legítimo interesse* with documented balancing test, minimal data, transparency, easy opt-out [ANPD guide][br1] | Personal data → LGPD | Public data still needs purpose compatibility; bought lists high risk | Uncertain; treat like email | 668,372 local units in manufacturing (IBGE CEMPRE 2024) [br2] | PT | Lower (BRL); Pix/Stripe BR; price R$ not $ |
| **Mexico** | ⚠️ | New LFPDPPP (Mar 2025): privacy notice (simplified at first contact + link), tacit consent if no opposition, ARCO rights. LFPC protects *consumers* who refuse ads; REPEP is mainly phone/SMS. Secondary source [mx1][mx2] | Personal data | Not "fuente pública" just because it's on LinkedIn (uncertain, secondary source) | Uncertain | 634,248 manufacturing units (INEGI CE 2024) [mx3] | ES | Mid; many US-facing exporters pay USD |
| **Canada** | ⚠️ consent, but implied | CASL needs consent; implied consent from **conspicuous publication** if no "no spam" note and message is relevant to the person's business role; ID + unsubscribe; keep records. [CRTC][ca1] [ca2] | Same rules | Address must be published by/for the person; lists from third parties or database queries generally don't qualify [ca1]. PIPEDA also restricts address harvesting (uncertain detail) | CASL covers any "electronic address" incl. social messaging (uncertain on CRTC wording) | 44,502 small + 2,370 medium mfg employers (ISED, Dec 2023) [ca3] | EN/FR | High; CAD; penalties up to C$10M per violation |
| **Colombia** | ⚠️ (generic inboxes) | SIC: corporate data of a *persona jurídica* isn't personal data under Ley 1581 → no prior authorisation for company contact [co1]. Named-person emails = personal data → authorisation. Must honour cese/supresión for marketing [co2] | Personal data → authorisation | Generic corporate addresses OK; personal ones not | Uncertain | Not pinned this pass | ES | Mid-low; COP |
| **Argentina** | ✅ | Ley 25.326 art. 27: marketing data from publicly accessible documents allowed; right to withdrawal/block; Disp. 4/2009: label "publicidad", show opt-out right + mechanism [ar1][ar2] | Same | Public-access sources expressly allowed | Uncertain | Not pinned | ES | Low/volatile; FX controls → USD via Stripe/Payoneer uncertain |
| **Chile** | ✅ (until/with Ley 21.719) | Ley 19.496 art. 28 B: subject line, sender ID, valid address to request suspension; SERNAC "No Molestar" list [cl1][cl2]. Ley 21.719 (GDPR-style, legitimate interest basis) in force 1 Dec 2026 [cl3] | Same | Uncertain after Dec 2026 | Uncertain | Not pinned | ES | Mid; CLP |
| **Singapore** | ✅ | Spam Control Act: for bulk (>100/day etc.) unsolicited CEMs, unsubscribe email, English statement, `<ADV>` label, stop within 10 business days; publishing an address ≠ consent but consent isn't required [sg1][sg2]. PDPA excludes business contact info (uncertain detail) | Same | **s.9: no sending to addresses from harvesting software or dictionary attack** [sg3] | Not addressed | Small | EN | High; SGD |
| **Australia** | ⚠️ consent, but inferred | Spam Act s.16 needs consent; Sch. 2 cl. 4: inferred from conspicuous publication if role-relevant and no "no spam" statement [au1][au2] | Same | **Using/supplying harvesting software or harvested lists is prohibited** (ss.20–22) [au3][au4] | Spam Act covers IM; ACMA treats DMs as electronic messages (uncertain) | 90,663 mfg businesses (ABS, Jun 2025) [au5] | EN | High; AUD |
| **New Zealand** | ⚠️ deemed consent | UEMA 2007 s.4 deemed consent from conspicuous publication in business capacity + relevance; s.13 bans harvesting software/lists [nz1] | Same | Harvesting software banned | DIA FAQ [nz2] | Small | EN | High; NZD |
| **UAE** | ⚠️ / uncertain | Federal PDPL (2021) consent-led; exec regs still thin; DIFC/ADGM free zones allow legitimate interest with right to object; corporate addresses may be fine, sole traders are individuals [ae1][ae2] | Personal data | Uncertain | Uncertain | Not pinned | EN/AR | High |
| **Saudi Arabia** | ❌ | PDPL art. 25: prior consent to use personal email for advertising; implementing regs add documentation, opt-out [sa1] | — | — | — | — | AR/EN | High but consent kills cold email |
| **India** | ✅ for now, ⚠️ from May 2027 | No email anti-spam statute (TRAI rules cover calls/SMS). DPDP Act core consent obligations start 13 May 2027 under DPDP Rules 2025 [in1] | Personal data after 2027 | Publicly made-available data by the person is excluded from DPDP (uncertain scope) | Uncertain | Very large, mostly micro | EN | Low WTP; INR |
| **South Africa** | ❌ | POPIA s.69: e-marketing to non-customers needs prior consent; may ask **once** with prescribed Form 4; POPIA covers juristic persons too; Regulator lists LinkedIn/Instagram DMs as electronic marketing [za1][za2] | — | — | **DMs explicitly covered** [za1] | — | EN | — |
| **UK (contrast)** | ✅ to corporates | PECR reg 22: corporate subscribers opt-out OK; sole traders/partnerships need consent; ICO: when emailing abroad, follow the destination country's rules [uk1][uk2] | Consent | — | ICO treats DMs as e-mail-like (earlier note) | — | EN | — |
| **Ireland (contrast)** | ✅ to corporates (uncertain) | S.I. 336/2011 reg 13: individuals need consent; non-natural persons opt-out (not re-verified this pass) | Consent | — | — | — | EN | — |
| **Spain / Portugal (contrast)** | ❌ / ⚠️ | ES: LSSI art. 21 prior consent even B2B. PT: Lei 41/2004 + opt-out list; CNPD says scraping emails unlawful (see NOTES.md) | — | — | — | — | — | — |

## Does UK law follow Ricardo abroad?

- **UK GDPR: yes.** Art. 3(1) covers any controller established in the UK, wherever the people are. Named work emails are personal data, so he needs a lawful basis (legitimate interests + a written assessment), an Art. 14 privacy notice by first contact, and must honour objections to marketing (Art. 21) immediately. Generic info@ addresses are mostly outside it.
- **PECR: probably not for overseas recipients**, but uncertain. The ICO says organisations marketing abroad must follow each destination country's rules and it can't advise on them [uk1].
- **Destination laws reach him anyway.** CASL, the Spam Act and Singapore's Act all bite on messages *accessed* in their country (Singapore s.7 [sg1]). Australia, NZ and Canada enforce cross-border, at least in theory.

## Biggest caveats

1. **Automation vs harvesting bans.** Australia, NZ and Singapore ban sending to addresses from harvesting software, and the US aggravates penalties when the site forbids sharing. Our crawler would probably count. Mitigation: pull addresses only from opted-in directories or trade-association member lists with permitted use, or only email the generic address a firm publishes for enquiries, and log the source.
2. **"Lawful" is not "deliverable."** Gmail and Yahoo bulk-sender rules (SPF/DKIM/DMARC, one-click unsubscribe, complaint rate under 0.3%) and blacklist risk constrain volume more than the law does. Use separate sending domains and low volume.
3. **Named vs generic addresses.** Everywhere except the US and Argentina, generic company inboxes are the safe default (Colombia makes this explicit). Named contacts trigger data-protection duties, including UK GDPR via Ricardo.
4. **Role relevance.** Canada, Australia and NZ only infer consent if the pitch fits the published role, e.g. support@ or the customer-service manager for an AI support pitch. Pitching the CEO's personal address doesn't qualify.
5. **Moving targets.** Chile (1 Dec 2026), India (13 May 2027) and Mexico (2025 rewrite) are all changing. Re-check before any campaign.
6. **Fit with Ricardo's rules.** Cold email plus done-for-you setup is still agency work. The best-aligned plays remain the inbound self-serve audit and selling scan data/benchmarks. Lawful opt-out outreach in the US/Brazil/Mexico could seed the audit with a single, clearly-labelled email per company.
7. **Stats are crude.** Unit counts include micro firms without manuals. The real addressable share (docs + support team + no AI chat) needs the scanner run per country.

## Suggested next step (free, no contact)

Run the fixed scanner on ~100 manufacturer/distributor sites each in the US (English), Brazil (Portuguese) and Mexico (Spanish), sourced from public directories (e.g. Thomasnet categories, ABIMAQ/FIESP member lists, CANACINTRA). Measure the docs-heavy/no-AI-chat share before choosing a market.

## Sources

- [us1]: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- [us2]: https://uscode.house.gov/us/usc/119-124/t15/s7704/
- [us3]: https://www.census.gov/data/tables/2022/econ/susb/2022-susb-annual.html
- [br1]: https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia_orientativo_hipoteses_legais_tratamento_de_dados_pessoais_legitimo_interesse
- [br2]: https://sidra.ibge.gov.br/pesquisa/cempre/quadros/brasil/2024
- [mx1]: https://www.zalesmachine.com/es/blog/cold-email-legal-mexico (secondary)
- [mx2]: https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPC.pdf
- [mx3]: https://www.inegi.org.mx/programas/ce/2024/
- [ca1]: https://www.crtc.gc.ca/eng/com500/guide.htm
- [ca2]: https://crtc.gc.ca/eng/internet/anti/reg.htm
- [ca3]: https://ised-isde.canada.ca/site/sme-research-statistics/en/key-small-business-statistics/key-small-business-statistics-2024
- [co1]: https://sedeelectronica.sic.gov.co/boletin-juridico/conceptos/ambito-de-aplicacion-de-la-ley-1581-de-2012-en-datos-corporativos
- [co2]: https://www.sic.gov.co/boletin/juridico/habeas-data/la-supresion-del-dato-personal-procede-en-casos-de-publicidad-o-marketing
- [ar1]: https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/texto
- [ar2]: https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-4-2009-151221/texto
- [cl1]: https://sernac.cl/portal/609/w3-article-52798.html
- [cl2]: https://www.sernac.cl/portal/617/w3-article-9184.html
- [cl3]: https://www.bcn.cl/leychile/navegar/imprimir?idNorma=1209272&idVersion=2026-12-01
- [sg1]: https://sso.agc.gov.sg/Act/SCA2007
- [sg2]: https://sso.agc.gov.sg/Act/SCA2007?ProvIds=Sc2-.
- [sg3]: https://sso.agc.gov.sg/Act/SCA2007?ProvIds=pr9-
- [au1]: https://austlii.edu.au/cgi-bin/viewdoc/au/legis/cth/consol_act/sa200366/s16.html
- [au2]: https://austlii.edu.au/cgi-bin/viewdoc/au/legis/cth/consol_act/sa200366/sch2.html
- [au3]: https://www.austlii.edu.au/cgi-bin/viewdoc/au/legis/cth/num_act/sa200366/s20.html
- [au4]: https://www.acma.gov.au/avoid-sending-spam
- [au5]: https://www.abs.gov.au/statistics/economy/business-indicators/counts-australian-businesses-including-entries-and-exits/jul2021-jun2025
- [nz1]: https://www.legislation.govt.nz/act/public/2007/0007/latest/whole.html
- [nz2]: https://www.dia.govt.nz/Spam-Frequently-Asked-Questions
- [ae1]: https://www.dlapiperdataprotection.com/?c=AE4&t=electronic-marketing (secondary)
- [ae2]: DIFC direct marketing guidance (difc.com, Commissioner of Data Protection)
- [sa1]: https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulation.pdf
- [in1]: https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa
- [za1]: https://inforegulator.org.za/wp-content/uploads/2020/07/GUIDANCE-NOTE-ON-DIRECT-MARKETING-IN-TERMS-OF-THE-PROTECTION-OF-PERSONAL-INFORMATION-ACT-4-OF-2013-POPIA.pdf
- [za2]: https://inforegulator.org.za/wp-content/uploads/2020/07/MEDIA-STATEMENT-ENFORCEMENT-NOTICE-ON-DIRECT-MARKETING-COMPLAINT.pdf
- [uk1]: https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/
- [uk2]: https://www.legislation.gov.uk/uksi/2003/2426/regulation/22

AI-adoption-gap signals weren't quantified per country this pass. The scanner's docs-heavy/no-AI-chat share is the measure to use.
