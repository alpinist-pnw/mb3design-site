---
type: session-handoff
created: 2026-08-13T2221
project: mb3design-site
branch: main
status: in-progress
verification: passing
descriptor: c2m-canonicalization-complete
---

# Session Handoff — C2M Canonicalization Complete (Phases 1–3)

## Goal & Next Action
**Goal:** Canonicalize C2M project media into the vault per `docs/ref/plan_c2m-canonicalization.md`; unblock the website selects pass.
**Success criteria:** Clean canonical tree, hash-verified, provenance documented, sources untouched. ✅ Met.
**Verification state:** Everything executed, not just written. Phase 3 independent re-hash audit ran twice; final verdict CLEAN — 1,601 files / 24.7 GB byte-for-byte vs `copy_log.csv` (`python3 .c2m-triage/phase3_audit.py`, report: `.c2m-triage/PHASE3_VERIFICATION.md`). Sources verified untouched throughout (copy-only rails).

▶ **Next immediate action (Sat 2026-08-15):** Start the website selects pass — read `docs/ref/curation_c2m-sails-dots.md`, and first rule on the pending selects-destination convention (recommendation on file: vault-root `04-Website Vault/` with chapter structure).

## Progress & Files
**Done this session:**
- Phase 1 overnight run: census 1,771 files/19.5 GB, dedup (51 groups), classification, 32 contact sheets (2 subagent bugs caught in QC and fixed)
- Review gate passed: M100/M101/M000/M999 job numbers minted (23111-* ruled date codes); 2022 videos ruled personal; 1871 = unsuccessful bid → RFP vault
- Phase 2 wave 1: 435 verified copies (named/classified files)
- Interactive triage tool built (`triage.html` + save server); Mark's pass: 107 personal, 96 explicit assignments, 27 tags, untouched-=-SAILS rule
- Phase 2 wave 2: 1,165 verified copies (unnamed media, month subfolders)
- Phase 3: audit caught + repaired one case-insensitive collision (IMG_4316, full history in log); 7 Google stubs logged non-copyable; final audit CLEAN
- Provenance README at C2M vault root; CLAUDE.md media-vault gap closed

**Key files touched:**
- `.c2m-triage/` (gitignored) — all manifests, logs, reports, triage state, tooling
- `CLAUDE.md` — C2M canonical path live; FACTURE + 05-RFP Vault noted
- `docs/ref/plan_story-development.md` — curation track item 1 marked complete

## Decisions & Blockers
**Decisions made:**
- MB3 job numbers M100 Sails / M101 DOTS / M999 Misc / M000 Standards — C2M had no real job numbers
- Dedup winners-only (clean-name > drive > shallow); near-dups copied flagged; SHARED → both projects; month subfolders for unnamed media
- Untouched triage cards = SAILS (Mark's rule; 24 flagged `date-suggests-DOTS` for optional spot-check)
- New vault conventions: `05-RFP Vault/` for unsuccessful bids; `01-Projects Vault/FACTURE/` for FACTURE-era portfolio material

**Blockers / open questions:**
- Selects-destination ruling (04-Website Vault vs per-project) — first thing Saturday
- Optional: spot-check 24 `date-suggests-DOTS` files; manual Drive-UI copies of 7 Google-native docs if wanted in tree
- Phase 4 (retire source originals): manual, Mark-only, unscheduled
- Triage server is session-bound and will be dead Saturday; restart if needed: `python3 .c2m-triage/server.py &`
