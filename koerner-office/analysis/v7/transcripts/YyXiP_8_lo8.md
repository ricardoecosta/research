# Decisions API Full Tutorial for Beginners: How to Use & Set up Decisions API

- **Video:** [YyXiP_8_lo8](https://www.youtube.com/watch?v=YyXiP_8_lo8) · **Channel:** Mikey No Code · **Uploaded:** 2026-10-12 · **Length:** 20 min · **Transcript:** cached
- **Speakers:** Mikey No Code (host) · **Format:** tutorial_howto
- **Evidence quality:** C — This is a promotional tutorial with hypothetical bakery examples, not a first-hand business case study. It explains configuration steps but gives no customer, revenue or deployment results. API performance and pricing are attributed to OpenAI rather than demonstrated independently. · Promotional conflict: The host promotes his master class, says it normally costs $499 and offers viewers free access.
- **Extraction:** gpt-6-luna · quotes verified 20/20

## Summary

This is a beginner tutorial for OpenAI’s Decisions API, which returns probabilities for text and image decisions instead of generating a written response. The host demonstrates predicate checks, urgency scores and category choices using hypothetical bakery messages and product photos. The examples show how software could sort and prioritize requests, while routing uncertain cases to a person. The tutorial also promotes the host’s master class, but does not describe a validated standalone business built around these examples.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Bakery delivery-issue message detection** — Use a predicate check to identify bakery messages that describe delivery problems. | ai_automation | moderate | 1/2/4/3/2 | 4 |
| I2 | **Bakery customer-message urgency scoring** — Score bakery messages by urgency so staff can prioritize replies. | ai_automation | moderate | 1/2/4/3/2 | 4 |
| I3 | **Bakery customer-message category routing** — Classify bakery messages as new orders, order changes, complaints or general questions. | ai_automation | moderate | 1/2/4/3/2 | 4 |
| I4 | **Bakery product-photo classification** — Classify bakery product photos as bread, pastry, cake, cookie or something else. | ai_automation | moderate | 1/2/4/3/2 | 4 |

### I1. Bakery delivery-issue message detection

- **Customer:** A bakery receiving customer messages.
- **Problem:** Staff may need to read each message to determine whether it describes a delivery problem.
- **Offer:** Evaluate each message against a clear statement about delivery problems and return a probability that the condition is true. An application can use a threshold to flag messages.
- **Business model:** not stated; the transcript presents this as an illustrative workflow, not a commercial offer.
- **Pricing:** not stated.  No customer-facing price is given. The Decisions API input cost is stated separately as a provider usage cost.
- **Acquisition:** 
- **Delivery:** The Decisions API evaluates text and returns a probability. The application would need to apply a threshold and flag messages; the tutorial does not show a production integration.
- **Unit economics (claims):** The tutorial states a general input cost for the Decisions API; it gives no per-bakery revenue or operating margin.
- **Tools:** OpenAI Decisions API, OpenAI Decisions playground
- **Startup cost:** API usage cost stated as USD 0.10 per 1,000,000 input tokens; other setup costs not stated.
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — The workflow is not tied to a US-specific market. A UK bakery could use it, subject to appropriate handling of customer message data, which the tutorial does not cover.
- **Risks:** A probability does not itself trigger an action; the application needs a suitable threshold.; A poorly chosen threshold could miss delivery complaints or flag ordinary messages.; The tutorial does not demonstrate a deployed bakery integration or measured results.
- **Automation [E]:** acquisition 1/5 (No customer acquisition process is described; finding bakery customers would require founder-led work unless an inbound channel were built.); onboarding 2/5 (A person would need to define and configure a clear predicate and threshold; the playground can help with experiments.); delivery 4/5 (After integration, software can score each message and flag those over the chosen threshold; uncertain or consequential cases can go to a person.); billing 3/5 (No customer billing flow is described. API usage is metered by input tokens, but customer invoicing would need a separate setup.); support 2/5 (People may need to review uncertain classifications and handle exceptions; no support process is described.)
> "whether a customer is reporting a delivery problem, whether a message contains spam or whether someone actually needs urgent assistance." — Mikey No Code (~7:11)

### I2. Bakery customer-message urgency scoring

- **Customer:** A bakery handling customer messages and requests.
- **Problem:** Messages differ in urgency, but staff may otherwise treat them equally or need to read each one to prioritize it.
- **Offer:** Score messages against ordered urgency levels. The example uses level zero for items that can wait, level one for replies due today and level two for issues needing a response now.
- **Business model:** not stated; the transcript presents this as an illustrative workflow, not a commercial offer.
- **Pricing:** not stated.  No customer-facing price is given. The Decisions API input cost is stated separately as a provider usage cost.
- **Acquisition:** 
- **Delivery:** The API returns probabilities for the urgency levels and a probability-weighted score. An application could prioritize messages based on the score; the tutorial does not show a production integration.
- **Unit economics (claims):** The tutorial states a general input cost for the Decisions API; it gives no per-bakery revenue or operating margin.
- **Tools:** OpenAI Decisions API, OpenAI Decisions playground
- **Startup cost:** API usage cost stated as USD 0.10 per 1,000,000 input tokens; other setup costs not stated.
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — The workflow is not tied to a US-specific market. A UK bakery could use it, subject to appropriate handling of customer message data, which the tutorial does not cover.
- **Risks:** The result is a weighted score and may fall between the configured levels.; Poorly described urgency levels could lead to inconsistent priorities.; Thresholds should reflect the consequences of a missed or delayed response.
- **Automation [E]:** acquisition 1/5 (No customer acquisition process is described; finding bakery customers would require founder-led work unless an inbound channel were built.); onboarding 2/5 (A person would need to define and configure ordered levels and descriptions; the playground can help with experiments.); delivery 4/5 (After integration, software can score and sort messages. People can review uncertain cases or messages where a wrong priority could have serious consequences.); billing 3/5 (No customer billing flow is described. API usage is metered by input tokens, but customer invoicing would need a separate setup.); support 2/5 (People may need to review uncertain scores and tune urgency definitions; no support process is described.)
> "It's useful when we need to say measure how urgent, severe or important something is rather than just simply checking whether a condition has been met or not." — Mikey No Code (~10:48)

### I3. Bakery customer-message category routing

- **Customer:** A bakery receiving customer requests throughout the day.
- **Problem:** Staff may need to read and sort each message to identify what the customer wants.
- **Offer:** Use a choice decision to select one category from a provided list and return probabilities for the options. The example categories are new order, change in order, complaint and general question.
- **Business model:** not stated; the transcript presents this as an illustrative workflow, not a commercial offer.
- **Pricing:** not stated.  No customer-facing price is given. The Decisions API input cost is stated separately as a provider usage cost.
- **Acquisition:** 
- **Delivery:** The API selects a category and returns probabilities. An application could route the request; the tutorial does not show a production integration. Vague messages may be sent for human review.
- **Unit economics (claims):** The tutorial states a general input cost for the Decisions API; it gives no per-bakery revenue or operating margin.
- **Tools:** OpenAI Decisions API, OpenAI Decisions playground
- **Startup cost:** API usage cost stated as USD 0.10 per 1,000,000 input tokens; other setup costs not stated.
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — The workflow is not tied to a US-specific market. A UK bakery could use it, subject to appropriate handling of customer message data, which the tutorial does not cover.
- **Risks:** Overlapping categories can split probabilities and make routing harder to interpret.; Vague messages may not have one dominant category and may need human review.; The tutorial does not show how category decisions are connected to a live order system.
- **Automation [E]:** acquisition 1/5 (No customer acquisition process is described; finding bakery customers would require founder-led work unless an inbound channel were built.); onboarding 2/5 (A person would need to define the categories and configure the choice prompt; the playground can help test examples.); delivery 4/5 (After integration, software can classify and route clear messages. People can review cases where probabilities are spread across categories.); billing 3/5 (No customer billing flow is described. API usage is metered by input tokens, but customer invoicing would need a separate setup.); support 2/5 (People may need to resolve ambiguous messages and adjust categories; no support process is described.)
> "Rather, it selects exactly one option from a list that we define, making it useful for sorting messages or routing requests into categories that don't have a particular order." — Mikey No Code (~14:43)

### I4. Bakery product-photo classification

- **Customer:** An online bakery handling product photos, customer uploads or images of damaged orders.
- **Problem:** Someone may otherwise have to review and organize uploaded images manually.
- **Offer:** Use a choice decision on an image to select the closest product category. Include a something-else option for images outside the categories.
- **Business model:** not stated; the transcript presents this as an illustrative workflow, not a commercial offer.
- **Pricing:** not stated.  No customer-facing price is given. The Decisions API input cost is stated separately as a provider usage cost.
- **Acquisition:** 
- **Delivery:** The API evaluates the image and returns probabilities for the categories. An application could use the result to organize or route the image; the tutorial tests examples in the playground but does not show a production integration.
- **Unit economics (claims):** The tutorial states a general input cost for the Decisions API; it gives no per-bakery revenue or operating margin.
- **Tools:** OpenAI Decisions API, OpenAI Decisions playground
- **Startup cost:** API usage cost stated as USD 0.10 per 1,000,000 input tokens; other setup costs not stated.
- **Time to first revenue:** not stated
- **UK applicability [E]:** 4/5 — The workflow is not tied to a US-specific market. A UK bakery could use it, subject to appropriate handling of customer-uploaded images and any personal data, which the tutorial does not cover.
- **Risks:** The model may be uncertain or misclassify an image.; A something-else option helps avoid forcing every image into a known product category, but does not guarantee correct classification.; The tutorial does not show results from a live image workflow.
- **Automation [E]:** acquisition 1/5 (No customer acquisition process is described; finding bakery customers would require founder-led work unless an inbound channel were built.); onboarding 2/5 (A person would need to define the image categories and configure the prompt; the playground can help test examples.); delivery 4/5 (After integration, software can classify images. People may need to review uncertain images or cases where image quality makes classification difficult.); billing 3/5 (No customer billing flow is described. API usage is metered by input tokens, but customer invoicing would need a separate setup.); support 2/5 (People may need to review uncertain or unexpected images and update categories; no support process is described.)
> "And the good thing is that the API works with images as well as text. And all three question types support image inputs." — Mikey No Code (~17:24)

## Revenue and metric claims (unverified claims)

- **The Decisions API costs 10 cents per million input tokens and charges for input only.** (cost, second-hand, claimant: Mikey No Code, describing OpenAI API pricing)
  > "The API cost 10 cents per million input tokens, and you're only charged for the input." — Mikey No Code (~3:52)
- **OpenAI says the Decisions API is around 10 times faster than the Responses API.** (other, second-hand, claimant: Mikey No Code, attributing the claim to OpenAI)
  > "And according to OpenAI, this makes it around 10 times faster." — Mikey No Code (~3:06)
- **The host's master class normally costs $499 to join.** (price, first-hand, claimant: Mikey No Code)
  > "Now, my master class normally costs $499 to join, but since you are watching this video, you can join completely free." — Mikey No Code (~1:53)
- **The host offers viewers of the video free access to his master class.** (price, first-hand, claimant: Mikey No Code)
  > "but since you are watching this video, you can join completely free. I appreciate you and your time." — Mikey No Code (~1:56)
- **An example predicate threshold could be set at 80% to flag delivery issues.** (other, second-hand, hypothetical, claimant: Mikey No Code)
  > "So for example, we could set that threshold at say 80%, meaning messages that receive a probability of 80% or higher would then be flagged as delivery issues." — Mikey No Code (~9:22)

## Tactics and playbook steps

**Test a one-condition predicate and set a consequence-aware threshold** (product)
1. Write the predicate as a clear statement rather than a question.
2. Test it on one message that clearly matches and another that clearly does not.
3. Choose a threshold for the action; the host gives 80% as an example for flagging delivery issues.
4. Use a lower threshold when a person will review the flag and a higher threshold when a mistake could have bigger consequences.

**Define urgency levels with descriptions** (operations)
1. Create ordered levels from low to high urgency.
2. Describe what qualifies for each level instead of relying on names alone.
3. The example uses level zero for items that can wait, level one for replies due today and level two for responses needed now.
4. Use the returned score and probabilities to prioritize messages, with people reviewing uncertain cases.

**Keep routing categories distinct** (product)
1. List the possible customer intents, such as new order, change in order, complaint and general question.
2. Make each option distinct to reduce overlap.
3. Inspect the probabilities: a dominant option suggests a clearer classification, while spread probabilities may call for human review.

**Add a fallback category and test unexpected images** (product)
1. Define image categories such as bread, pastry, cake and cookie.
2. Add a something-else option for images that do not fit.
3. Test both expected products and an unrelated image, as the host does with a croissant, a sourdough loaf and a pizza.
4. Review probabilities to spot uncertain classifications.

## Lessons

- *automation_ai*: Use a probability output when software needs a decision it can act on, rather than generating text that someone must inspect.
- *validation_testing*: Write predicates as clear statements about one condition, then test them against examples where the condition is both met and not met.
- *operations*: Set action thresholds according to the consequences of a false positive or false negative.
- *offer_design*: Describe each level in an ordered score so the model has context for what qualifies as urgent.
- *other*: Keep choice options distinct so probabilities are easier to interpret.
- *automation_ai*: Route unclear or low-confidence cases to a person instead of forcing automatic handling.
- *other*: Give classifiers an option for inputs that do not fit the known categories.

## Warnings and mistakes

- The host says the Decisions API is in public beta and that some details may change.
- A returned probability does not decide the application's next action by itself; the application needs a threshold.
- Overlapping choice categories can spread probabilities across answers and make results harder to interpret.
- The tutorial promotes the host's master class, stating a usual price of $499 and offering viewers free access.

## Tools mentioned

OpenAI Decisions API (Evaluates text, images or both against predicates, ordered levels or choices and returns probabilities.; USD 0.10 per 1,000,000 input tokens; input only, as stated by the host.), OpenAI Responses API (Compared with the Decisions API as an API that generates text.), GPT6 Luna (The single model the host says the Decisions API currently runs on.), OpenAI Decisions playground (Used to configure and test decisions without writing code.), platform.openai.com/decisions (The address the host gives for opening the Decisions playground.)
