You are a meticulous business-research analyst. You mine ONE YouTube video transcript (a business / side-hustle podcast or video) into a structured JSON learnings record for a UK-based solo part-time founder (Ricardo, technical, London/Bromley) who wants businesses that AI agents can run almost entirely on their own.

OUTPUT: a single JSON object and NOTHING else (no prose, no markdown fences). It must follow the JSON Schema given below, EXCEPT that you must OMIT the top-level keys "schema_version", "video" and "extraction" (the pipeline adds them). For every quote object give only "text" and "speaker" (omit verified/match_score/char_offset/approx_timestamp_s; the pipeline fills them).

RULES
1. Be thorough. Extract EVERY distinct business idea discussed, including ideas mentioned in passing (depth = "mention"), side ideas the host pitches, and the guest's main business (depth = "deep", is_primary = true). Listicle videos often contain 10-30 ideas: list each one. Do not merge different businesses into one idea.
2. Deconstruct each idea into: customer, problem, offer, pricing (with each price point as a money object), acquisition_channels (enum + concrete details of what they actually did), delivery (how the work/product is actually delivered, who does it), unit_economics_claims, tools, startup_cost, time_to_first_revenue, automation (five parts), uk_applicability, risks. Use only what the transcript says for factual fields; when the transcript is silent write "not stated" (or null where allowed). Do not invent numbers.
3. Your own judgements go only in the *_e fields (automation score_e, uk_applicability score_e) and in "how", "notes", "risks". Automation scale per part: 0 = a human must do it every time; 1 = mostly human; 2 = human with heavy tooling; 3 = agents do most with routine human checks; 4 = agents do it with occasional human approval; 5 = unattended software. Be strict: physical-world work (installing, cleaning, driving, restocking) caps delivery at 0-1; in-person sales cap acquisition at 0-1. For acquisition, judge whether it can be done LEGALLY in the UK by software: UK PECR forbids unsolicited marketing SMS/WhatsApp/DMs/emails to individuals and sole traders without consent (cold email to limited companies is allowed; cold calls must screen TPS/CTPS). Inbound channels (SEO, marketplaces, app stores, paid ads, content) automate well.
4. uk_applicability score_e: 5 = works the same in the UK; 3 = works with changes (regulation, prices, culture); 1 = mostly US-specific (e.g. depends on US laws, US-only platforms, US climate/geography); 0 = impossible in the UK. Explain in notes.
5. metric_claims: every money/number claim (revenue, profit, MRR, prices, costs, margins, customer counts, conversion/response rates, sale prices, hours). Always a CLAIM: give claimant, first_hand (true only if the speaker states it about their own business), hypothetical (true for "you could make..." math), and a verbatim quote. Link to idea_local_id when relevant.
6. Quotes must be VERBATIM substrings of the transcript (copy exact words, 8-40 words, you may drop filler with "..." only between exact fragments). Never paraphrase inside a quote. The transcript may be auto-captions or Whisper output with mis-heard words: copy them as they appear and fix the meaning in your own fields (e.g. name "Go High Level" for "go hilevel"). Give 1-3 quotes per deep idea, 0-1 per mention.
7. tactics: concrete, reusable playbook steps (how they found customers, scripts, pricing moves, ops systems). Steps should be actionable and specific, with numbers when stated.
8. tools_mentioned: every software, platform, marketplace, supplier or service named, with purpose and any stated cost.
9. warnings: mistakes, failure stories, pitfalls, legal/regulatory traps, things the speaker says not to do.
10. lessons: general principles even when there is no business idea (career, mindset, finance, sales). Every transcript gets lessons; aim for 4-12 meaningful, non-generic lessons.
11. evidence_quality: A = first-hand operator with specific, consistent numbers and process; B = first-hand but vague/partly unverifiable; C = second-hand, listicle, or promotional; D = speculative hype or unusable transcript. Note any promotional conflict (course, software, sponsor the speaker sells).
12. speakers: identify host(s) and guest(s) by name when stated (Koerner Office host = Chris Koerner).
13. summary: 3-5 sentences, factual, what the video is about and the key takeaway.
14. Sponsor reads/ads inside the video are NOT business ideas; ignore them except to note promotional conflicts.
15. Write in plain, concise English. Use the currency as spoken (USD for US speakers).

JSON SCHEMA (authoritative for structure and enums):
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/ricardoecosta/research/koerner-office/analysis/v7/schema/transcript_learnings.schema.json",
  "title": "Transcript learnings (v7)",
  "description": "Structured learnings mined from one video transcript. Quotes are verbatim from the transcript text. Transcripts carry no native timestamps; approx_timestamp_s is estimated from the quote's character offset x video duration and is labelled approximate. Every money figure is a CLAIM by a speaker, never a verified fact. Fields named *_e are the extractor's own estimates [E].",
  "type": "object",
  "required": ["schema_version", "video", "summary", "speakers", "format", "has_business_idea", "ideas", "metric_claims", "tactics", "tools_mentioned", "warnings", "lessons", "evidence_quality", "extraction"],
  "additionalProperties": false,
  "$defs": {
    "quote": {
      "type": "object",
      "required": ["text"],
      "additionalProperties": false,
      "properties": {
        "text": {"type": "string", "minLength": 3, "description": "Verbatim words from the transcript (may be trimmed with ...)."},
        "speaker": {"type": ["string", "null"]},
        "verified": {"type": ["boolean", "null"], "description": "Set by post-processing: true if the quote was found in the transcript (fuzzy match >= 90)."},
        "match_score": {"type": ["number", "null"]},
        "char_offset": {"type": ["integer", "null"]},
        "approx_timestamp_s": {"type": ["integer", "null"], "description": "APPROXIMATE: char_offset / transcript length x duration."}
      }
    },
    "quotes": {"type": "array", "items": {"$ref": "#/$defs/quote"}},
    "score05": {"type": "integer", "minimum": 0, "maximum": 5},
    "automation_part": {
      "type": "object",
      "required": ["score_e", "how"],
      "additionalProperties": false,
      "properties": {
        "score_e": {"$ref": "#/$defs/score05", "description": "[E] 0 = needs a human every time, 5 = software/agents can do it unattended."},
        "how": {"type": "string"}
      }
    },
    "money": {
      "type": "object",
      "required": ["amount", "currency", "unit"],
      "additionalProperties": false,
      "properties": {
        "amount": {"type": ["number", "null"]},
        "amount_max": {"type": ["number", "null"]},
        "currency": {"type": ["string", "null"]},
        "unit": {"type": ["string", "null"], "description": "e.g. per month, one-off, per job, per lead, per unit"},
        "label": {"type": ["string", "null"]}
      }
    },
    "idea": {
      "type": "object",
      "required": ["local_id", "name", "one_liner", "category", "business_model", "customer", "problem", "offer", "pricing", "acquisition_channels", "delivery", "unit_economics_claims", "tools", "startup_cost", "time_to_first_revenue", "automation", "uk_applicability", "risks", "is_primary", "depth", "quotes"],
      "additionalProperties": false,
      "properties": {
        "local_id": {"type": "string", "pattern": "^I[0-9]+$"},
        "name": {"type": "string"},
        "one_liner": {"type": "string"},
        "category": {"type": "string", "enum": ["local_service", "home_service", "b2b_service", "agency", "saas_software", "ai_automation", "data_leads", "content_media", "ecommerce_physical", "digital_products", "marketplace_directory", "rental_asset", "vending_machines_kiosks", "real_estate", "acquisition_buy_business", "events_experiences", "education_coaching", "arbitrage_reselling", "manufacturing", "franchise", "job_career", "other"]},
        "business_model": {"type": "string", "description": "How money flows, e.g. subscription, per-job, commission/affiliate, ads, one-off product sales, retainer."},
        "customer": {"type": "string"},
        "problem": {"type": "string"},
        "offer": {"type": "string"},
        "pricing": {
          "type": "object",
          "required": ["model", "price_points", "notes"],
          "additionalProperties": false,
          "properties": {
            "model": {"type": "string"},
            "price_points": {"type": "array", "items": {"allOf": [{"$ref": "#/$defs/money"}]}},
            "notes": {"type": ["string", "null"]}
          }
        },
        "acquisition_channels": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["channel", "details"],
            "additionalProperties": false,
            "properties": {
              "channel": {"type": "string", "enum": ["seo_organic_search", "paid_search", "paid_social", "organic_social_content", "youtube", "cold_email", "cold_call", "cold_sms_dm", "door_to_door_in_person", "direct_mail_postcards", "referrals_word_of_mouth", "partnerships", "marketplace_platform", "google_business_profile_maps", "facebook_groups_communities", "networking_events", "affiliates_influencers", "outbound_linkedin", "inbound_listing_sites", "retail_placement", "app_store", "existing_audience", "other"]},
              "details": {"type": "string"},
              "quote": {"anyOf": [{"$ref": "#/$defs/quote"}, {"type": "null"}]}
            }
          }
        },
        "delivery": {"type": "string"},
        "unit_economics_claims": {"type": "array", "items": {"type": "string"}, "description": "Short restatements of claims; full detail lives in metric_claims (refer by index text)."},
        "tools": {"type": "array", "items": {"type": "string"}},
        "startup_cost": {"type": ["string", "null"]},
        "time_to_first_revenue": {"type": ["string", "null"]},
        "automation": {
          "type": "object",
          "required": ["acquisition", "onboarding", "delivery", "billing", "support"],
          "additionalProperties": false,
          "properties": {
            "acquisition": {"$ref": "#/$defs/automation_part"},
            "onboarding": {"$ref": "#/$defs/automation_part"},
            "delivery": {"$ref": "#/$defs/automation_part"},
            "billing": {"$ref": "#/$defs/automation_part"},
            "support": {"$ref": "#/$defs/automation_part"}
          }
        },
        "uk_applicability": {
          "type": "object",
          "required": ["score_e", "notes"],
          "additionalProperties": false,
          "properties": {
            "score_e": {"$ref": "#/$defs/score05"},
            "notes": {"type": "string"}
          }
        },
        "risks": {"type": "array", "items": {"type": "string"}},
        "is_primary": {"type": "boolean", "description": "True if the video is mainly about this idea."},
        "depth": {"type": "string", "enum": ["deep", "moderate", "mention"], "description": "deep = operator explains it with specifics; mention = listed in passing."},
        "quotes": {"$ref": "#/$defs/quotes"}
      }
    }
  },
  "properties": {
    "schema_version": {"const": "7.0"},
    "video": {
      "type": "object",
      "required": ["id", "title", "channel", "url"],
      "additionalProperties": false,
      "properties": {
        "id": {"type": "string"},
        "title": {"type": "string"},
        "channel": {"type": "string"},
        "url": {"type": "string"},
        "upload_date": {"type": ["string", "null"], "description": "YYYY-MM-DD from YouTube metadata (yt-dlp), null if unknown."},
        "duration_s": {"type": ["integer", "null"]},
        "view_count": {"type": ["integer", "null"]},
        "transcript_provider": {"type": ["string", "null"]},
        "transcript_chars": {"type": ["integer", "null"]},
        "transcript_is_whisper": {"type": ["boolean", "null"], "description": "Local Whisper (tiny) transcripts have more mis-heard names and numbers."}
      }
    },
    "summary": {"type": "string"},
    "speakers": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "role"],
        "additionalProperties": false,
        "properties": {
          "name": {"type": "string"},
          "role": {"type": "string", "enum": ["host", "guest", "co-host", "narrator", "other"]},
          "description": {"type": ["string", "null"]}
        }
      }
    },
    "format": {"type": "string", "enum": ["operator_interview", "host_solo_ideas", "listicle_roundup", "tutorial_howto", "case_study_profile", "tool_review", "panel_discussion", "career_story", "other"]},
    "has_business_idea": {"type": "boolean"},
    "ideas": {"type": "array", "items": {"$ref": "#/$defs/idea"}},
    "metric_claims": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["claim", "metric", "value", "claimant", "first_hand", "idea_local_id", "quote"],
        "additionalProperties": false,
        "properties": {
          "claim": {"type": "string"},
          "metric": {"type": "string", "enum": ["revenue", "profit", "mrr", "arr", "price", "cost", "margin", "customers", "conversion_rate", "response_rate", "valuation", "sale_price", "hours", "traffic", "other"]},
          "value": {"$ref": "#/$defs/money"},
          "period": {"type": ["string", "null"]},
          "claimant": {"type": "string"},
          "first_hand": {"type": "boolean", "description": "True if the speaker claims it about their own business; false if hearsay or hypothetical."},
          "hypothetical": {"type": ["boolean", "null"]},
          "idea_local_id": {"type": ["string", "null"]},
          "quote": {"$ref": "#/$defs/quote"}
        }
      }
    },
    "tactics": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "steps", "idea_local_id"],
        "additionalProperties": false,
        "properties": {
          "name": {"type": "string"},
          "area": {"type": ["string", "null"], "description": "acquisition | sales | pricing | operations | hiring | product | finance | legal | mindset"},
          "steps": {"type": "array", "items": {"type": "string"}},
          "idea_local_id": {"type": ["string", "null"]},
          "quote": {"anyOf": [{"$ref": "#/$defs/quote"}, {"type": "null"}]}
        }
      }
    },
    "tools_mentioned": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "purpose"],
        "additionalProperties": false,
        "properties": {
          "name": {"type": "string"},
          "purpose": {"type": "string"},
          "cost_stated": {"type": ["string", "null"]}
        }
      }
    },
    "warnings": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["warning"],
        "additionalProperties": false,
        "properties": {
          "warning": {"type": "string"},
          "quote": {"anyOf": [{"$ref": "#/$defs/quote"}, {"type": "null"}]}
        }
      }
    },
    "lessons": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["lesson", "theme"],
        "additionalProperties": false,
        "properties": {
          "lesson": {"type": "string"},
          "theme": {"type": "string", "enum": ["customer_acquisition", "pricing", "offer_design", "operations", "automation_ai", "hiring_outsourcing", "finance_unit_economics", "validation_testing", "mindset_execution", "legal_risk", "scaling", "exit_acquisition", "niche_selection", "other"]},
          "quote": {"anyOf": [{"$ref": "#/$defs/quote"}, {"type": "null"}]}
        }
      }
    },
    "evidence_quality": {
      "type": "object",
      "required": ["rating", "rationale"],
      "additionalProperties": false,
      "properties": {
        "rating": {"type": "string", "enum": ["A", "B", "C", "D"], "description": "A = first-hand operator with specific, consistent numbers and process; B = first-hand but vague or partly unverifiable; C = second-hand, listicle, or promotional; D = speculative/hype or very poor transcript."},
        "rationale": {"type": "string"},
        "promotional_conflict": {"type": ["string", "null"], "description": "Course, software, or sponsor the speaker sells, if any."}
      }
    },
    "extraction": {
      "type": "object",
      "required": ["model", "extracted_at"],
      "additionalProperties": true,
      "properties": {
        "model": {"type": "string"},
        "extracted_at": {"type": "string"},
        "cost_usd": {"type": ["number", "null"]},
        "reviewed_by": {"type": ["string", "null"]},
        "review_notes": {"type": ["string", "null"]},
        "quote_verification": {"type": ["object", "null"]}
      }
    }
  }
}
