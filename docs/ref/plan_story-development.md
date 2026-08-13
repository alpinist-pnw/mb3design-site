# Story Development Plan — Status Board & Work Order

Living doc. Update at the end of every working session. Companion to `framework_story-development.md` (the method) and `_TEMPLATE_casestudy.md` (the shape).

**Last updated:** 2026-08-13 (merge: initial setup + Notion BI linkage + media curation/C2M canonicalization restored — curation track was dropped in a concurrent-session rewrite; commit between sessions to let git catch this)

---

## Status board

| Story | File(s) | Status | Blocking |
|---|---|---|---|
| **BADM** | `case-studies/casestudy_badm-...md` | ✅ Reference standard. Ship-ready pending final VERIFY sweep | Confirm nothing in it contradicts `stat_verified-numbers.md` |
| **Sails / Intuit Dome** | original + `rewrite_2026-08-13T1100_intuit-dome-clipper-ship.md` | 🟡 Rewrite drafted from resume bullets + storyboard | Fork confirmation (see ASK in draft) · $1.6M/$1.8M attribution · weight, dims, install duration · Mark's read on voice |
| **LAX / Distance of the Sun** | original + `rewrite_2026-08-13T1100_lax-...-skeleton.md` | 🔴 Skeleton only — 12 extraction questions embedded | Requires interview session with Mark before prose |
| **Octopus** | `career-arc/casestudy_paul-allen-yacht-octopus.md` | 🟢 Good as career-arc. Open question: promote back to case-studies as 4th entry? | Mark's call |
| **Ark / Planet Oasis** | `career-arc/casestudy_ark-interface-...md` | 🟢 Done for its role (origin story) | — |
| **Gateway Arch** | none | ⚪ Deprioritized | Only if slate needs a 4th after top 3 ship |
| **Kuwait Scientific Center** | none | ⚪ Deprioritized | Same |

## Audience model & conversion intelligence (from Notion, 2026-03)

Source pages under "MB3-D Website" (notion parent: 2c5a1d764c1e8052a6c7ed2b218bf560):

- **Five inquiry segments** (from Contact Form Redesign spec, notion: 32da1d764c1e8108891af51c408f7954): project taking shape · active RFP · extra hands on active project · AI systems & automation · other. This is the working audience taxonomy for the site arc — each case study and page should know which segment(s) it converts. AI services = distinct audience; branched in-form for now, dedicated landing page if volume grows.
- **Conversion endpoint:** Guided Inquiry form, Option A recommended (split-screen, card selector, coached textarea, optional budget/timeline, response-time promise).
- **Intent capture** (notion: 32fa1d764c1e81e48cc7dcb2c93f2f6a): behavior-signal tracking → contextual CTAs (e.g., gated case-study PDF); form-submit enrichment via Clearbit/Apollo/Hunter (~$50/mo). Deanonymization purchase rejected. Build alongside the contact form work.
- **Career timeline page** (main-page action item): visual-thumbnail timeline synced to CV, medium depth, links to detail pages. Feeds from `career-arc/` + `about/bio`. Gives Octopus and Ark their proper home on the site.

Implication for case studies: derivative cuts (framework surface table) gain a segment column — a "gated PDF" cut of BADM/Sails becomes the intent-capture CTA payload.

## Work order (in sequence)

1. **Populate `docs/ref/` with source docs.** Missing and blocking traceability: `podcast-prep_2026-04-21T0930_jordan-salvador-full-brief.md`, the podcast deck, the Sails video storyboard doc. Mark knows where they live; copy them in.
2. **Sails rewrite review session.** Mark reads the rewrite draft, answers its ASK blocks, resolves VERIFY flags, rules on the fork. Then promote: `git rm` original, rename rewrite to `casestudy_intuit-dome-clipper-ship.md`, log new verified numbers in `about/stat_verified-numbers.md`.
3. **Site-arc one-pager.** Page list + narrative progression + emotional beat per page + feeding content file + target segment per page. Incorporates the audience model above; endpoint is the Guided Inquiry form. Governance doc → lives in repo AND Notion (under MB3-D Website), kept in sync. Unblocks Claude Design experiments (prototype with real BADM content).
4. **LAX extraction interview.** Run the 12 questions in the skeleton as a grill-me session; checkpoint answers into `ref/`; draft prose to template; review; promote.
5. **BADM final sweep.** VERIFY-flag audit against the stats ledger; flip `verified: true`.
6. **Octopus decision.** Career-arc vs. 4th case study — note the timeline page may resolve this: Octopus as a timeline anchor with a detail page may be stronger than as case study #4.
7. **First Insights piece.** After the slate ships. Leading candidate: earned acceleration vs. avoidance speed (Frisch Test). Alternates: "How We Built a 60-Foot Clipper Ship," front-loading economics (1,728→4,487).
8. **Derivative cuts.** Map shipped case studies to video chapters, LinkedIn posts, and gated-PDF CTA payloads per segment. Sails video master cut resumes here.
9. **Contact form + intent capture build.** Option decision (A/B/C), then implement per Notion spec; platform confirmed as this repo (Vite/React/Cloudflare). Enrichment provider decision pending.

## Standing conventions (recap)

- Rewrites: `rewrite_{YYYY-MM-DDTHHMM}_{descriptor}.md` beside the original; Mark promotes explicitly.
- No number ships unverified; `about/stat_verified-numbers.md` is the single ledger.
- Interview STAR versions of these stories live in the Career 2026 project, never in this repo.

## Media curation & C2M canonicalization track

Vault + C2M sources surveyed 2026-08-13. Curation is demand-driven: selects for 3 case studies + hero shots, not an archive-first pass.

**Per-beat visual needs (selection criteria):**

| Beat | Visual job | BADM example |
|---|---|---|
| Impossible Ask | Constraint made visible | Historic building interior, 3D scan point cloud |
| The Fork | Rejected vs. chosen, side by side | Stack-laminate vs. lattice CAD comparison |
| Irreversibility | "Model caught it" evidence | Tree-to-joist connection: model view + as-built photo |
| Outcome | Finished, in use | Kids on the installed exhibit |
| Transfer | Pattern across domains | Yacht model beside museum model |

**Work order:**
1. **C2M canonicalization** — spec ready: `ref/plan_c2m-canonicalization.md`. Overnight Phase 1 (inventory/dedup/classify/propose, zero source writes; Haiku census + Sonnet classification + top-tier QC) → morning review gate → Phase 2 copy-execute into `01-Projects Vault/C2M/` per PS ten-folder convention (`23111-0062-SAILS`, `23111-0051-DOTS`). Sources: `z_PROJECTS_ARCHIVE/C2M/` + `~/Documents/_temp/_C2M misc/` + any Mark names at session start. Launch from CC CLI.
2. **C2M website selects pass** — after Phase 2, brief: `ref/curation_c2m-sails-dots.md`. Key finds: rebar SD PDF = documentary evidence for Sails Irreversibility beat; DOTS section drawings 01–11 likely answer the LAX skeleton's fork questions. Gated-PDF cuts (per audience model above) source from these selects.
3. Selects-destination convention (vault-root `04-Website Vault/` vs. per-project) — PENDING Mark. Recommendation on file: vault-root, chapter structure.
4. BADM selects pass — `01-Projects Vault/PS/0692-BADM/`; 3–5 selects per beat, hero candidates flagged.
5. Locate podcast video — `02-Podcasts Vault/` holds only YT banners.
6. Web-optimization pipeline: selects → exports → site assets; define at CC CLI build time (Cloudflare R2 or public/).

## Parking lot

- CLAUDE.md references filename prefixes (`casestudy_`, `capability_`) as kept convention — revisit if folder-encoded categories make prefixes feel redundant in practice.
- Frontmatter on the two thin originals says `verified: true` despite embedded VERIFY comments — template now defines `verified: true` = zero unresolved flags. Originals retire at promotion.
- Notion mirroring: build-specific work stays local by default; the site-arc one-pager is the exception (governance doc, dual-home).
- World Labs / spatial-intelligence bookmark on the Notion page — unexplored; possibly relevant to portfolio presentation. Park until core site ships.
- Sails/LAX media: FOUND in `z_PROJECTS_ARCHIVE/C2M/` + `~/Documents/_temp/_C2M misc/` (uncurated). Canonicalization spec on file; C2M cleanup no longer blocks the site — it feeds it.
- Session hygiene: two sessions edited this file today and one dropped the other's section. Convention: `git add -A && git commit` at end of every working session on this repo.
