# The Easiest Way to Build & Host a GPT-6 Astra Website (Full Tutorial)

- **Video:** [oBM-m3msUpQ](https://www.youtube.com/watch?v=oBM-m3msUpQ) · **Channel:** Mikey No Code · **Uploaded:** 2026-10-05 · **Length:** 20 min · **Transcript:** cached
- **Speakers:** Mikey No Code (narrator) · **Format:** tutorial_howto
- **Evidence quality:** C — This is a promotional tutorial demonstrating a sample website workflow, not a first-hand account of an operating website business. It contains concrete implementation steps but no customer results, service revenue, or validated business economics. · Promotional conflict: The presenter promotes hosting.com, offers a discount code, and directs viewers to a sign-up link.
- **Extraction:** gpt-6-luna · quotes verified 15/15

## Summary

The video walks through building and hosting a sample fitness and wellness website with Codex and GPT-6 Astra, using five prompts, a production build, and an FTP upload to hosting.com. It covers the page structure, images, mobile layout, SEO metadata, and deployment checks. The presenter says the workflow can be reused for another business site, but does not present an operating web-design business or describe how to find clients, price work, or support customers. The demonstrated contact form is only a front-end placeholder and does not send submissions.

## Business ideas

| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |
|---|---|---|---|---|---|
| I1 | **AI-assisted website creation for businesses** — Use an AI coding assistant to create, build, and host a small business website. | b2b_service | moderate | 1/2/2/1/1 | 5 |
| I2 | **Elevate Studio fitness and wellness concept** — A sample fitness and wellness brand used to demonstrate the website workflow. | local_service | mention | 1/1/0/1/1 | 5 |

### I1. AI-assisted website creation for businesses

- **Customer:** People or businesses that need a professional website; a specific customer profile is not stated.
- **Problem:** The presenter says professional websites can involve high developer quotes and long waits, while drag-and-drop builders can produce generic-looking templates.
- **Offer:** A responsive business website with sections such as services, about, testimonials, gallery, contact, and SEO metadata, created with AI assistance and uploaded to a domain.
- **Business model:** Not stated; the video teaches a workflow and does not describe selling website services.
- **Pricing:** Not stated..  No price for the demonstrated website service is given. ChatGPT Pro and hosting.com shared hosting are presented as prerequisites, but their prices are not stated.
- **Acquisition:** 
- **Delivery:** The user gives prompts to Codex with GPT-6 Astra, reviews the generated React/Vite/TypeScript site, runs a production build, then manually uploads the compiled files from the dist folder to public_html through hosting.com's FTP panel. The video does not describe client handoff or ongoing support.
- **Unit economics (claims):** The presenter says people may have been quoted $3,000–$5,000 for a basic website; this is not a price for the demonstrated service.
- **Tools:** Codex, GPT-6 Astra, ChatGPT Pro, React, Vite, TypeScript, Tailwind CSS, hosting.com shared hosting Pro, hosting.com Enhanced Panel, FTP, npm, Unsplash
- **Startup cost:** Not stated. The presenter says a ChatGPT Pro plan and hosting.com shared hosting account are needed; prices are not provided.
- **Time to first revenue:** Not stated.
- **UK applicability [E]:** 5/5 — The workflow uses general web technologies and static hosting, so it appears usable in the UK. The video gives no UK-specific hosting prices, domain details, or legal guidance.
- **Risks:** The tutorial does not establish customer demand, a route to customers, a service price, or recurring revenue.; The contact form only stores field values in React; without back-end processing it does not deliver enquiries.; The presenter advises checking mobile layout and deployment behavior, and placing compiled files directly at the root of public_html.
- **Automation [E]:** acquisition 1/5 (No customer acquisition method is demonstrated. Finding and agreeing a project with a client would require human work.); onboarding 2/5 (AI can scaffold from prompts, but a person must collect the client's content, branding, images, and requirements.); delivery 2/5 (AI generates much of the code, but the workflow includes human prompting, visual checks, responsive review, and a manual FTP upload.); billing 1/5 (Billing is not covered, so no automated billing process is shown.); support 1/5 (Ongoing support is not covered and would need a human unless separately designed.)
> "And then from here you can go ahead and swap in your own content, images, branding, and domain and use the exact same process for another business site." — Mikey No Code (~20:09)
> "And maybe you've probably been quoted three, four, five, $5,000 just for a basic site." — Mikey No Code (~0:23)

## Revenue and metric claims (unverified claims)

- **The presenter says viewers may have received a quote of roughly $3,000 to $5,000 for a basic website.** (cost, second-hand, claimant: Mikey No Code)
  > "And maybe you've probably been quoted three, four, five, $5,000 just for a basic site." — Mikey No Code (~0:23)

## Tactics and playbook steps

**Set the visual direction before adding sections** (product)
1. Start with a project scaffold and specify the framework, component structure, navigation, and visual palette.
2. Build the navigation and hero first, then use that established style as the basis for later sections.
> "And there is a reason we're not rushing into the other sections yet either because the design choices that we make here in this first prompt." — Mikey No Code (~6:41)

**Build the page in prompt-sized sections** (operations)
1. Add services and about sections after the hero.
2. Add testimonials and a gallery, then a contact section and SEO metadata.
3. Finish with image URLs, a mobile layout, a hamburger menu, and a footer.
> "So, for the next one here, we're going to ask Astra to add a services section with three cards for personal training, nutrition, coaching, and recovery and wellness." — Mikey No Code (~7:36)

**Build and upload only the production output** (operations)
1. Run npm run build to create the dist folder.
2. Check that dist contains the compiled site assets and not development files or node_modules.
3. Upload the contents of dist directly into public_html through the hosting panel's FTP section.
4. Check the live domain on desktop and mobile after upload.
> "So let's ask Astra to run the production build to create the dist folder, add the required.htac htac file for spa routing and make sure that the final folder only contains the compiled output we need for deployment." — Mikey No Code (~15:07)

## Lessons

- *operations*: Set the visual direction early so later sections can follow a consistent style.
- *offer_design*: Make it easy for visitors to understand what the business offers without making them search through the site.
- *customer_acquisition*: Use testimonials and visual proof to help visitors assess a service.
- *operations*: A clear contact path matters; showing a form is not enough if it cannot process submissions.
- *validation_testing*: Check responsive behavior on a small screen and verify the deployed site, not just the development preview.

## Warnings and mistakes

- The contact form is a front-end placeholder and does not send submissions anywhere.
- The presenter says to upload the contents of dist directly into public_html, with index.html at the root, rather than placing the dist folder itself there.
- The presenter promotes hosting.com with a discount code, so the hosting recommendation has a promotional conflict.

## Tools mentioned

Codex (AI coding assistant used to scaffold, edit, and build the website; transcript captions render the name as “codeex” and similar variants.), GPT-6 Astra (Selected model for generating and modifying the site.), ChatGPT Pro (Plan the presenter says is needed to use Codex with Astra.), hosting.com (Shared hosting provider used to host the production site; the video includes a discount code and link.), hosting.com shared hosting Pro plan (Plan selected for the site's static production build.), hosting.com Enhanced Panel (Account panel used to access FTP and manage hosting.), React (Frontend framework used for the sample site.), Vite (Project and production build tooling.), TypeScript (Language used in the website project.), Tailwind CSS (Styling the website and responsive layouts.), Unsplash (Source of image URLs used in the hero, about section, and gallery.), npm (Runs the production build command.), FTP (Used through the hosting panel to upload the compiled files.), SSL certificates (The presenter says they are included with the hosting plan.; Free, according to the presenter.)
