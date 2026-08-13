# Orchestration Spec — C2M Vault Canonicalization

Executable plan for a Claude Code CLI session with subagents. Orchestrated per the PS vault convention; Fable-planned 2026-08-13. Companion: `curation_c2m-sails-dots.md` (website selects pass — separate deliverable, feeds off Phase 1 outputs).

---

## Objective

Canonicalize Code2Matter project media into the vault as a sibling of PS:

```
VAULT/MB3 DESIGN-VAULT/01-Projects Vault/
├── PS/     (existing, untouched)
└── C2M/    (new)
    ├── 0000-C2M_Standards/        ← empty template, mirrors PS convention
    ├── 23111-0062-SAILS_Clipper_Ship/
    │   ├── 01_Admin … 10_Closeout
    └── 23111-0051-DOTS_Distance_of_the_Sun/
        ├── 01_Admin … 10_Closeout
```

**Convention (verified from `PS/0000-PS_Standards/` and confirmed consistent across PS projects):**
`01_Admin, 02_Reference, 03_Design, 04_Drawings, 05_Specs, 06_Photos, 07_Video, 08_3D, 09_Submittals, 10_Closeout`

**Naming decision (Fable-proposed, Mark confirms at review gate):** use C2M's native job numbers visible in the drawing sets — `23111-0062` (Clipper Ship) and `23111-0051` (Origami/DOTS) — rather than inventing PS-style sequence numbers. Preserves provenance; drawings self-index against their folder.

## Sources (read-only, all phases)

1. `My Drive/01_PROJECTS_MB3-DESIGN/z_PROJECTS_ARCHIVE/C2M/` (~350 files flat + subfolders; surveyed)
2. `/Users/mark/Documents/_temp/_C2M misc/` (unsurveyed; CLI has access)
3. Any additional locations Mark names before launch (phone offloads, Ops@mb3ltd.com drive, external disks — ASK AT SESSION START)

## Hard safety rails — every subagent inherits these

- NEVER move, rename, or delete anything in source locations. Copy only.
- All writes go to: (a) the new `01-Projects Vault/C2M/` tree, (b) a local working dir `~/Documents/GitHub/mb3design-site/.c2m-triage/` (gitignored) for manifests/thumbnails/logs.
- Phase 1 writes NOTHING into Google Drive at all.
- Every copy is hash-verified against its source before being marked complete in the manifest.
- Personal/non-project files are never deleted — listed in `_NOT-PROJECT_manifest.csv` for Mark's own disposition.
- Google Drive CloudStorage caveat: files may be cloud placeholders. Materialize (download) before hashing; throttle to avoid sync churn; log any file that fails to materialize rather than blocking.

## Phase 1 — Inventory & Propose (overnight-safe, zero source writes)

**Subagent A — Census (Haiku, parallelizable by directory):**
Walk all sources recursively. Emit `inventory.csv`: path, size, ext, created/modified dates, EXIF/QuickTime creation date for media, SHA-256 hash. Flag cloud-placeholder files needing materialization.

**Subagent B — Dedup (Haiku):**
Cross-source duplicate groups by hash; near-duplicate candidates by (creation-date + size) for re-encoded transfers. Emit `dedup_groups.csv` with a proposed canonical-copy winner per group (prefer: highest resolution/size, then Drive source).

**Subagent C — Classification (Sonnet):**
For every unique file, propose: `project` (SAILS | DOTS | SHARED | NOT-PROJECT | UNKNOWN) and `category` (01–10 per convention). Rules of thumb:
- Filename tokens: CLIPPER/clipper/hull/BOW-STUDY/yardarm/backboard → SAILS; DOTS/Origami/23111-0051/hanger → DOTS
- Drawing sets, permit packages, calc packages → 04_Drawings or 09_Submittals (permit/review correspondence → 09)
- .3dm/.3dmbak/.stl/.dxf → 08_3D; proposals/vendor lists/templates → 01_Admin or 02_Reference; presentation sheets → 03_Design
- Undated/unnamed MOVs: assign project by creation-date cluster ONLY after Mark confirms phase boundaries at review; until then → UNKNOWN with date-bin noted
- Obvious personal content (non-project subjects) → NOT-PROJECT
Emit `mapping_proposed.csv`: source path → proposed target path, confidence (H/M/L), one-line rationale for M/L.

**Subagent D — Contact sheets (Haiku + ffmpeg):**
Per curation brief: thumbnails for all video, one HTML contact sheet per date-bin, into the working dir. These double as the review interface for UNKNOWN media.

**Subagent E — QC & report (top-tier model):**
Audit C's low-confidence rows, resolve or escalate; sanity-check date clusters against known project timeline (Clipper install → 2024 opening; DOTS → 2025); compile `PHASE1_REPORT.md`: counts by project/category/confidence, dedup savings, personal-file list, open questions for Mark, and the exact review checklist.

**Phase 1 exit:** report + manifests + contact sheets in the working dir. Nothing in Drive has changed.

## Review Gate — Mark (morning, ~30 min)

1. Confirm naming decision and folder names
2. Confirm date-bin → project-phase boundaries (unlocks UNKNOWN media assignment)
3. Spot-check ~20 mapping rows across confidence levels
4. Rule on dedup winners policy and NOT-PROJECT list
5. Say "execute Phase 2"

## Phase 2 — Copy-Execute (attended start, then unattended)

Create target tree (incl. `0000-C2M_Standards/` empty template). Copy per approved manifest, hash-verify each file, log to `copy_log.csv`. Duplicates: canonical winner copied; losers recorded in manifest as `duplicate-of`, not copied. Re-runnable/resumable: skip rows already verified.

## Phase 3 — Verify & Close

Full tree audit vs. manifest (count + hash). Emit `PHASE3_VERIFICATION.md`. Update vault docs: drop a `_README_provenance.md` at `C2M/` root recording sources, date, and manifest location. Update `mb3design-site/CLAUDE.md` media-vault section: C2M canonical path live, gap closed.

## Phase 4 — Retire originals (MANUAL, LATER, OPTIONAL)

Only on Mark's explicit instruction, only after Phase 3 verification, and as archive-then-delete, never direct delete. Not part of any automated run.

## Relationship to website selects

Website selects pass (`curation_c2m-sails-dots.md`) runs AFTER Phase 2 against the clean canonical tree — selects become trivial to source and cite. `04-Website Vault/` selects-destination decision still pending.

## Launch (Mark, tonight)

```
cd ~/Documents/GitHub/mb3design-site
claude
> Read docs/ref/plan_c2m-canonicalization.md and execute Phase 1.
> Ask me the session-start questions first, then run unattended.
```
Session-start questions: additional source locations? disk space OK for materialization + thumbnails? confirm working-dir path.
