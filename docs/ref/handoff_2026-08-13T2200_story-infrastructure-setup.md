# Session Handoff — 2026-08-13 (claude.ai, Career 2026 project)

Read this + `plan_story-development.md` to resume. This session set up the story-development infrastructure for the mb3design-site build.

---

## What happened this session

1. **Story inventory ranked.** Reviewed existing `docs/content` files. Verdict: BADM is the quality bar (real fork, "model caught it" moment, honest 1,728→4,487 CAD hours, verified outcomes). Sails and LAX were the thinnest files despite being the flagship projects. Octopus and Ark reclassified as career-arc (origin story), not client-facing case studies.

2. **Folder structure created** under `docs/content/`: case-studies / career-arc / capabilities / philosophy / process / about / insights, plus `docs/ref/`. All 18 existing files moved into category folders. Moves are in git — review with `git status`.

3. **Working kit created:**
   - `CLAUDE.md` (repo root) — session context: positioning, voice rules, content rules, start checklist
   - `docs/ref/framework_story-development.md` — five-beat spine (Impossible Ask → Fork → Judgment Under Irreversibility → Verified Outcome → Transfer), sourcing rules, extraction-interview method, derivative-cut map
   - `docs/ref/plan_story-development.md` — status board + work order (the authoritative next-actions list)
   - `docs/content/case-studies/_TEMPLATE_casestudy.md` — BADM-derived template
   - `rewrite_2026-08-13T1100_intuit-dome-clipper-ship.md` — full Sails rewrite draft from resume bullets + storyboard; ASK blocks on the fork, VERIFY flags on $1.6M/$1.8M attribution, weight, dims, install duration
   - `rewrite_2026-08-13T1100_lax-distance-of-the-sun-skeleton.md` — deliberate skeleton, 12 extraction questions; needs a grill-me interview before prose

4. **Design-track decision.** Content-first, but not waterfall: write a site-arc one-pager (page list, narrative progression, emotional beat per page, which content file feeds it), then prototype in Claude Design using real BADM content while the LAX interview runs in parallel. Claude Design = divergent exploration; production build stays in this repo via CC CLI. Mark has not used Claude Design yet — first experiment pending.

5. **Notion BI reviewed and linked** (end of session). Parent page: "MB3-D Website" (notion: 2c5a1d764c1e8052a6c7ed2b218bf560). Contains audience/business intelligence that feeds the site arc:
   - **Visitor Intelligence — Intent Capture & Lead Enrichment** (notion: 32fa1d764c1e81e48cc7dcb2c93f2f6a). Approved DIY approach: Plan 1 intent-signal tracking (portfolio+contact same session, >60s, multi-project views, return visits) with contextual CTAs; Plan 2 form-submit enrichment (Clearbit/Apollo/Hunter, ~$50/mo). Deanonymization purchase rejected. Build timed with contact form redesign.
   - **Contact Form Redesign — Options & Build Spec** (notion: 32da1d764c1e8108891af51c408f7954). Option A "Guided Inquiry" recommended. The card selector is the de facto AUDIENCE SEGMENTATION: (1) project taking shape, (2) active RFP, (3) extra hands on active project, (4) AI systems & automation, (5) other. Strategic note: AI services is a different audience — branch in-form now, dedicated landing page if volume grows. Open items on that page: choose A/B/C, confirm platform (answer: this repo — Vite/React/Cloudflare), decide AI-services page split.
   - **Main page action item:** career timeline with visual thumbnails, synced to CV, medium-depth with links to detail pages. Maps to career-arc/ content + about/bio.

## Open decisions (Mark's calls)

- Sails fork ruling: adjustability-engineered-mounts proposed; two alternates in the draft's ASK block
- $1.6M vs $1.8M install attribution between Intuit Dome and LAX
- Octopus: stay career-arc or promote to 4th case study
- Filename category prefixes: keep or strip now that folders encode category
- Contact form: Option A/B/C (spec recommends A); AI-services dedicated page now or later

## Immediate next actions (fresh CLI session in mb3design-site)

1. `git add -A`, review diff, commit the restructure + kit (uncommitted as of handoff)
2. Drop source docs into `docs/ref/`: podcast-prep_2026-04-21 brief, podcast deck, Sails video storyboard — blocking traceability
3. Site-arc one-pager (~20 min dictation) → `docs/ref/` — **must incorporate the Notion BI**: the five inquiry segments as the audience model, Guided Inquiry as the CTA endpoint, intent-capture touchpoints, and the career-timeline page. Per governance convention, this one-pager is a meta/strategy doc → keep in BOTH repo and Notion, synced.
4. Sails rewrite review session (resolve ASK/VERIFY, promote over original, log numbers in `about/stat_verified-numbers.md`)
5. LAX extraction interview (12 questions in the skeleton)

## Standing rules (recap for any Claude session)

No overwrites — rewrites are timecoded siblings, Mark promotes explicitly. No unverified numbers ship — `about/stat_verified-numbers.md` is the single ledger. Interview STAR versions of these stories live in Career 2026, never this repo. Voice: short, declarative, metric-anchored, no corporate softening.
