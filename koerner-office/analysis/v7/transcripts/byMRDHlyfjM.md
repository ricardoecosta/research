# How to Use Claude in Xcode to Make an App in 2026 (No Coding)

- **Video:** [byMRDHlyfjM](https://www.youtube.com/watch?v=byMRDHlyfjM) · **Channel:** Mikey No Code · **Uploaded:** 2026-10-08 · **Length:** 18 min · **Transcript:** cached
- **Speakers:** Mikey No Code (host) · **Format:** tutorial_howto
- **Evidence quality:** C — The presenter gives a first-hand, step-by-step software demo, but the transcript provides no independently verifiable project output, customer evidence, or business economics. The video also includes a strong promotion for the presenter's master class. · Promotional conflict: The presenter promotes his AI and app-building master class, says it normally costs $499, and offers viewers free access through the video description.
- **Extraction:** gpt-6-luna · quotes verified 25/25

## Summary

The video walks through building a native iPhone journal app by describing features to Claude inside Xcode. The app uses local storage and supports creating, viewing, editing, and deleting entries, then gets a design pass and is tested in the simulator and on an iPhone. The presenter suggests reusing the workflow for a recipe box, reading list, habit tracker, or personal notes app. The video does not cover app sales, customer acquisition, or revenue, and it promotes the presenter’s master class.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **Native iPhone journal app** — A native iPhone journal app where users create, mood-tag, edit, delete, and locally save entries. | saas_software | deep | 1/4/5/0/1 | 5 |
| I2 | **Recipe box app** — A simple recipe box app suggested as a project for the same AI-assisted build workflow. | saas_software | mention | 1/3/4/0/1 | 5 |
| I3 | **Reading list app** — A reading list app suggested as a project for the same AI-assisted build workflow. | saas_software | mention | 1/3/4/0/1 | 5 |
| I4 | **Habit tracker app** — A habit tracker app suggested as a project for the same AI-assisted build workflow. | saas_software | mention | 1/3/4/0/1 | 5 |
| I5 | **Personal notes app** — A personal notes app suggested as a project for the same AI-assisted build workflow. | saas_software | mention | 1/3/4/0/1 | 5 |

### I1. Native iPhone journal app

- **Customer:** iPhone users who want to keep journal entries; no narrower customer segment is stated.
- **Problem:** Users need a way to write, save, view, edit, and delete journal entries; no broader pain point is stated.
- **Offer:** A native iPhone app with a title, text body, creation date, and mood for each entry; a recent-first list; creation and detail screens; editing and deletion; local SwiftData storage; and a design pass with light and dark themes and animations.
- **Business model:** not stated
- **Pricing:** not stated.  No price or monetization is discussed for the journal app.
- **Acquisition:** 
- **Delivery:** The presenter builds the app in Xcode with Claude generating Swift and SwiftUI code. SwiftData stores entries locally. The app is tested in the iOS simulator and installed on a connected iPhone.
- **Unit economics (claims):** No revenue, customer, margin, or operating-cost economics are stated for the journal app.
- **Tools:** Xcode, Claude, Swift, SwiftUI, SwiftData, Xcode Intelligence panel, iOS Simulator, iPhone
- **Startup cost:** The tutorial requires a Mac with Apple Silicon and a Claude Pro or Max account; their prices are not stated. Xcode is described as free. A physical iPhone is optional for testing.
- **Time to first revenue:** not stated
- **UK applicability [E]:** 5/5 — A native iPhone journal app has no stated US-only dependency. The video does not discuss UK privacy or data-protection requirements for journal entries.
- **Risks:** The demonstration does not cover publishing the app, finding customers, or validating willingness to pay.; Entries are stored locally; backup or sync is not described, so data could be lost if device or app data is lost.; The presenter tests features at each stage, but the video does not establish that the generated app is free of bugs.
- **Automation [E]:** acquisition 1/5 (The video gives no customer acquisition process. A founder would still need to find and attract users.); onboarding 4/5 (The app is a self-serve iPhone app, and users can create entries directly. No automated onboarding flow is described.); delivery 5/5 (Once installed, the app stores entries locally and handles creating, viewing, editing, and deleting them in software.); billing 0/5 (No paid offer, payment flow, or billing system is described.); support 1/5 (No support process is described; the app creator would need to handle user issues.)
> "10 minutes ago, that app did not exist." — Mikey No Code (~0:27)
> "I broke the whole build into five small conversations with Claude instead of just one giant prompt." — Mikey No Code (~0:41)
> "The app can use native iPhone features, follow standard iOS design patterns, and be developed further like any other Xcode project." — Mikey No Code (~17:01)

## Revenue and metric claims (unverified claims)

- **The presenter says the journal app did not exist 10 minutes before his statement.** (hours, first-hand, claimant: Mikey No Code)
  > "10 minutes ago, that app did not exist." — Mikey No Code (~0:27)
- **The presenter says he built the app without writing any Swift code.** (other, first-hand, claimant: Mikey No Code)
  > "I just built a fully working iPhone app without writing a single line of swift, just by talking to Claude inside Xcode." — Mikey No Code (~0:01)
- **The presenter says he broke the build into five conversations with Claude.** (other, first-hand, claimant: Mikey No Code)
  > "I broke the whole build into five small conversations with Claude instead of just one giant prompt." — Mikey No Code (~0:41)
- **The presenter says the journal app's four core interactions work together.** (other, first-hand, claimant: Mikey No Code)
  > "So this confirms that all four core interactions are now working together properly, creating, reading, editing, and deleting entries." — Mikey No Code (~12:42)
- **The presenter says Xcode is free.** (price, second-hand, claimant: Mikey No Code)
  > "Xcode itself is completely free, but the installation is quite large" — Mikey No Code (~4:12)
- **The presenter says viewers need around 10 GB of free storage for Xcode and its simulators.** (other, second-hand, claimant: Mikey No Code)
  > "make sure you have around 10 GB of free storage available for the app and its simulators." — Mikey No Code (~4:16)
- **The presenter says his master class normally costs $499 to join.** (price, first-hand, claimant: Mikey No Code)
  > "my master class normally costs $499 to join, but since you are taking the time to watch this video, thank you very much." — Mikey No Code (~1:35)
- **The presenter offers viewers free access to his master class.** (price, first-hand, claimant: Mikey No Code)
  > "you can join completely free. Just check out that link in the description to get free access to my master class" — Mikey No Code (~1:42)

## Tactics and playbook steps

**Build the app through five focused prompts** (product)
1. Start by asking Claude to create the entry data model and local storage.
2. Add the recent-first main list and test that the screen loads.
3. Add an entry form with title, body, mood selection, and save; test that a saved entry appears.
4. Add a detail view with edit and delete controls; test the full flow.
5. Finish with a design prompt for navigation, typography, spacing, colors, themes, and animations.
> "I broke the whole build into five small conversations with Claude instead of just one giant prompt." — Mikey No Code (~0:41)

**Test each feature before adding the next** (operations)
1. Run the main list in the simulator before adding entry creation.
2. Create an entry and check that it appears in the list.
3. Open an entry, edit it, save changes, and delete a separate entry.
4. After the design pass, move through the list, creation screen, and detail view in both themes.
5. Connect an iPhone and repeat the core flow on the physical device.
> "And each step here was tested before moving forward, which made the whole process then easier to manage." — Mikey No Code (~16:44)

**Write prompts as explicit feature requirements** (product)
1. Specify the fields each record needs.
2. State how records should be sorted and what each list row should display.
3. Describe the controls and expected result for saving, editing, and deleting.
4. Ask for a final design pass after the core interactions work.
> "Claude will handle the code throughout the build while we just focus on describing what the app should do and then just testing each feature as it is added." — Mikey No Code (~5:00)

## Lessons

- *operations*: Break a large build into small, focused prompts so each stage can build on the previous one.
- *other*: Define the data model and storage before building screens that depend on them.
- *validation_testing*: Test a feature as soon as it is added, including checking that the interface is connected to storage.
- *offer_design*: Describe user actions and expected outcomes explicitly, such as saving, editing, and deleting an entry.
- *other*: Complete the core interactions before asking for a full visual polish pass.
- *validation_testing*: Test on a physical device as well as in the simulator when device access is available.
- *validation_testing*: A working demo does not establish a business: validate demand, pricing, customer acquisition, and ongoing costs separately.

## Warnings and mistakes

- The presenter says the Xcode installation is large and recommends having around 10 GB of free storage for the app and simulators.

## Tools mentioned

Claude (Coding assistant used inside Xcode to answer questions, generate features, write code, and work through problems.; A Claude Pro or Max account is required for the described sign-in method; no subscription price is stated.), Claude Pro (Account plan used to connect Claude to Xcode.; Subscription required; price not stated.), Claude Max (Account plan used to connect Claude to Xcode.; Subscription required; price not stated.), Anthropic API key (Alternative way to connect Claude to Xcode, described as giving more control over usage and billing.; Not stated.), Claude Agent SDK (Xcode integration for more advanced capabilities, including subagents and background tasks.; Not stated.), Claude Sonnet 5 (Model the presenter says is active as of the June 2026 release.; Not stated.), Xcode (IDE used to create the iOS project, connect Claude, generate code, build, and run the app.; Described as free.), Xcode Intelligence panel (Where the presenter connects Claude and opens the coding assistant.; Not stated.), Mac App Store (Download source for Xcode.; Xcode is described as free.), claude.ai (Source of the Claude account connected to Xcode.; No plan price stated.), Swift (Programming language Claude writes for the native iOS app.), SwiftUI (Interface framework selected for the iOS app.), SwiftData (Local storage used to save journal entries between app launches.), iOS Simulator (Built-in Xcode environment used to run and test the app.), iPhone (Optional physical device used to install and test the native app.; Not stated.), macOS 26 Tahoe (Operating system the presenter says is required for Xcode 26.), Apple Silicon (Mac hardware requirement stated for the tutorial.; Not stated.), Evernote (Design reference named for the journal app's visual style.)
