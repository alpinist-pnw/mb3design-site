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
1. **C2M canonicalization — ✅ COMPLETE 2026-08-13 (Phases 1–3).** Canonical tree live: `01-Projects Vault/C2M/` (M100 Sails / M101 DOTS / M999 Misc / M000 Standards) + `FACTURE/` + `05-RFP Vault/`. 1,601 hash-verified copies (~24.7 GB); Phase 3 independent re-hash audit: **CLEAN, byte-for-byte**. One case-collision defect caught and repaired (IMG_4316 case-insensitive overwrite; full history in `copy_log.csv`); 7 Google-native stubs not filesystem-copyable (logged). Provenance README at C2M root; manifests + `media_tags.csv` (Mark's 27 type tags) in `.c2m-triage/`. Mark's triage: 107 personal excluded, untouched-=-SAILS rule (1,069 files, 24 flagged `date-suggests-DOTS` for later spot-check). **Phase 4 (retire source originals): MANUAL, Mark-only, not scheduled.** Next: website selects pass (item 2) now runs against the clean tree.
2. **C2M website selects pass — IN PROGRESS 2026-08-15.** First-pass manifest: 39 rows (29 Sails, 10 DOTS) from the brief's named candidates + the 7 pre-named `clippers_*.jpeg`, materialized + hash-verified. 8 hero candidates flagged. Gaps: Sails 06_Install has no rows (install media is unnamed clips — 2024-06 alone is 633 photos; needs contact-sheet triage); DOTS has almost no photo/video at all in M101 (4 photos, 3 clips) — DOTS fab/install/reveal media must come from the 24 `date-suggests-DOTS` files or from outside the vault; 8 rows are `.3dm/.3dmbak/.DXF` needing renders before web use. Brief: `ref/curation_c2m-sails-dots.md` (its "selects destination" section is superseded by item 3).
3. **Selects-destination convention — ✅ RULED 2026-08-15 (Mark, option A with manifest-as-truth).** Three layers: (1) canonical DB = `01-Projects Vault/{PS,C2M,FACTURE,…}/{job}/` ten-folder tree, never touched by curation; (2) selects are *rows* in `docs/ref/selects_manifest.csv` (repo, git-versioned; columns `project,chapter,beat,hero,source_path,notes`, source_path relative to vault root); (3) `04-Website Vault/{project}/{chapter}/` is **derived** — generated by `scripts/materialize_selects.py` (copy-only, sha256-verified, `--prune` for stale, writes `_materialized.csv`), regenerable, never hand-curated. Chapters = the seven framework video chapters. BADM/FACTURE plug in the same way.
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
