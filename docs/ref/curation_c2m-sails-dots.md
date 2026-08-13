# Curation Brief — C2M (Sails + DOTS) Media Pass

Survey date: 2026-08-13. TWO source locations (both read-only — copy selects out, never move/rename/delete originals):

1. `/Users/mark/Library/CloudStorage/GoogleDrive-mark@mb3ltd.com/My Drive/01_PROJECTS_MB3-DESIGN/z_PROJECTS_ARCHIVE/C2M/` — surveyed 2026-08-13; findings below.
2. `/Users/mark/Documents/_temp/_C2M misc/` — NOT YET SURVEYED (outside claude.ai Filesystem MCP scope; reachable from Claude Code CLI). Contents unknown; likely overlaps source 1 (local transfer staging vs. Drive backup) with possible uniques.

CLI session step zero: survey source 2, then run all triage across BOTH roots with dedup (file hash + creation date) so contact sheets are a single merged, deduplicated set.

## State of the folder

~350 files flat at root. Two populations:
1. **Named technical assets** — CAD (.3dm), drawing sets (PDF), permit packages, presentation sheets, named renders/animations. High value, identifiable by filename. Plus subfolders: `Clippers Install videos/`, `Photos/`, `Rhino Exports/`, `STL exports/`, `Rigging/`, `Yardarm comparison/`, `Screenshots_misc./`, `2.1 - Site Survey/`, `3 - 3D Model/`, `1 - C2M Drawings/`.
2. **~300 unnamed iPhone clips** (`IMG_xxxx.MOV`, `7xxxxxxxxxx__UUID.MOV`) — content unknown, dates recoverable from metadata. Also personal strays to ignore (e.g. "Haddie Gets A Bone", "Hot Skier").

Note: folder contains BOTH projects mixed — Clipper Ship (Sails/Intuit Dome) and DOTS (The Distance of the Sun/LAX).

## Candidate selects — named assets mapped to story beats

**Sails / Clipper Ship:**
- Impossible Ask: `CLIPPER_OVERVIEW_double backboard concept sketch.3dm`, `2023.12.14 PRESENTATION SHEETS.pdf`
- Fork / Prototyping: `BOW-STUDY_01–05` (iteration sequence — render as progression), `Yardarm comparison/`, `cast ply backboard.3dmbak`, `hull-05-VERSION-B`, `clipper_50%.pdf`
- **Irreversibility: `#4321 LCI Clipper Ship Concrete Rebar SD (F114).pdf`** — documentary artifact of the same-day anchor-bolt/rebar resolution. Pair with: `Clipper Ship - Baseplate Depression Letter 2.7.2024.pdf`, baseplate depression sets, permit resubmittal packages (12.20.2023 → 1.17.2024 loop), `CLIPPER_BACKBOARD ALUM 240604 -for comment by DCI.pdf`
- Fabrication/Install: `Clippers Install videos/`, `Photos/`, rigging drawings, `Steel Detailing Updates 3.19.2024.pdf`
- Motion assets: `clipper_hull_5_1920px_.1.mov`, `clipper_spin_25percent.mov`, `360-spin_at_55inch_POV.mov`

**DOTS / LAX:**
- Segmentation (likely the Fork): `DOTS-SECTION 01–11` drawing sets — eleven section packages documenting decomposition of the 150' form
- Assembly/rigging: `DOTS-ASSEMBLY DETAILS 240126.PDF` (+ DCI variant), `DOTS-RIGGING ASSEMBLY 231214.PDF`, `Hanger Load Map 1.31.2024.pdf`, `DotS Hangers 2023-12-01_moved_cables.DXF`
- Mock-up: `DOTS-01-MOCK UP 240226.PDF`
- Model: `DOTS Model_2024.07.12-AND Chad 240722...3dm.rhl`
- Progress sets: `23111-0051 Origami Progress Set` (multiple dates — good for timeline visuals)

Cross-check drawing evidence against the extraction questions in the LAX skeleton rewrite — these documents likely ANSWER several of them (segmentation logic, seam decisions, rigging approach).

## The unnamed-MOV problem → CC CLI triage script

Manual review of ~300+ clips is the stall. Script it (across BOTH sources, deduplicated):

1. Read creation date (EXIF/QuickTime metadata) for every `.MOV/.mov` at C2M root
2. Cluster into timeline bins against project phases (approx: shop fab 2023–early 2024 → Sails install → DOTS fab → DOTS install 2024–2025; Mark corrects bin boundaries)
3. Extract 1–3 thumbnail frames per clip (ffmpeg)
4. Generate one contact-sheet HTML/PDF per bin: thumbnail grid + filename + date + duration
5. Mark reviews contact sheets, marks selects; script copies selects (never moves) into the selects structure

Tools: exiftool + ffmpeg, or pure ffprobe. Output contact sheets to a local working dir, not the vault. Prereq check: confirm Google Drive files are locally synced/downloadable (CloudStorage placeholders may need materializing).

## Selects destination

Pending Mark's convention ruling (vault-root `04-Website Vault/` vs. per-project selects). Since C2M was never in the vault, recommendation: create `VAULT/MB3 DESIGN-VAULT/04-Website Vault/` with `sails/` and `dots/` using the locked chapter structure (`01_Vision … 07_Documents`). Selects are copies; the C2M cleanup/canonicalization proper stays a separate, later, optional project — the site does not depend on it.

## Definition of done for this pass

- 3–5 selects per story beat per project, hero candidates flagged
- Every select traceable to its C2M original (keep a manifest: select path ← source path)
- Rebar PDF + DOTS section drawings staged for case-study embedding
- Contact sheets archived so the eventual full canonicalization starts from an index, not from zero
