# CLAUDE.md — mb3design-site

Context file for Claude Code sessions in this repo. Read this before touching content.

---

## What this repo is

The MB3 Design website (mb3ltd.com rebuild). Vite + React + TypeScript, deployed via Wrangler/Cloudflare. Content lives in `docs/content/` as markdown with frontmatter; source material and working docs live in `docs/ref/`.

Owner: Mark Buchanan (Papa Bucky). Principal, MB3 Design. MIT-trained architect, 20+ years computational design + fabrication, 80+ museum installations, Sails (Intuit Dome 2024), The Distance of the Sun (LAX Metro 2025).

## Positioning

**Brand line:** "I turn 'impossible' into installed."

**Position:** Strategic partner, not vendor. The person teams call when nobody else can figure it out. Bridges artistic vision and technical execution — computational design + master fabrication + AI-augmented workflows.

**Core thesis:** Judgment under irreversibility. Experience in contexts where mistakes cannot be undone (concrete pours, live installations, fixed opening dates) produces tacit judgment. Front-load the model, coordinate in virtual space, fabricate with certainty.

**Site goal:** Move visitors from "call us for a quote" to "book a strategic consultation." Case studies are the proof engine.

## Voice rules — non-negotiable

- Short, declarative, outcome-first sentences. Em-dash phrasing is native.
- No corporate softening. No AI cheerleading. No "passionate about," "leveraging synergies," "world-class."
- Metric-anchored. Every claim carries a number or gets a VERIFY flag.
- First person where Mark speaks; the work speaks otherwise.
- Signature register: "my project, my risk" / "a pencil is the better tool."
- Behavioral evidence over philosophy. If a paragraph could appear on any fabricator's site, cut it.

## Content rules

1. **Never state an unverified number.** Unverified claims get `<!-- VERIFY: ... -->` comments. Mark supplies or confirms every metric before a file ships.
2. **No overwrites.** Rewrites are new files named `rewrite_{YYYY-MM-DDTHHMM}_{descriptor}.md` alongside the original. Mark promotes a rewrite over the original explicitly (git mv/rm), never Claude silently.
3. **Provenance in frontmatter.** Every content file cites its `source:` documents. Source docs belong in `docs/ref/`.
4. **The quality bar is BADM.** `case-studies/casestudy_badm-bay-area-discovery-museum.md` is the reference standard: real fork-in-the-road decision, a "model caught it" moment, honest cost accounting (quoted vs. actual hours), verified outcomes, cross-domain transfer. New and rewritten case studies match that structure and depth.
5. **Case studies = client-facing proof.** Career-arc pieces (Octopus, Ark/Planet Oasis) are origin-story context and live in `career-arc/`, not the case study slate.

## Directory map

```
docs/
├── content/
│   ├── case-studies/     client-facing proof. Template: _TEMPLATE_casestudy.md
│   ├── career-arc/       origin-story material (Octopus, Ark)
│   ├── capabilities/     what MB3 does (5 files)
│   ├── philosophy/       how Mark thinks (front-loading, pattern transfer, builder's instinct)
│   ├── process/          how engagements run
│   ├── about/            bio, direct quotes, stat_verified-numbers.md (canonical metrics)
│   └── insights/         future articles (empty)
└── ref/
    ├── framework_story-development.md   how stories get built here — read before writing any
    ├── plan_story-development.md        current status + work order
    └── (source docs: podcast-prep brief, Sails storyboard — pending, see plan)
```

## Working style with Mark

- He dictates compressed direction; execute without over-asking. When intent is genuinely ambiguous, stop, name the ambiguity, ask targeted questions, wait.
- Flag uncertainty over polishing unverifiable claims. He'd rather see the VERIFY flag.
- Build iteratively; don't replace wholesale.
- When a correction implies a pattern, propose the convention, not just the single fix.

## Media vault

Canonical media archive (drawings, photos, video, 3D):
`/Users/mark/Library/CloudStorage/GoogleDrive-mark@mb3ltd.com/My Drive/VAULT/MB3 DESIGN-VAULT/`

- `01-Projects Vault/PS/` — 39 Pacific Studio projects, numbered. `0692-BADM` is the case-study project. Per-project structure: `01_Admin` … `10_Closeout`, with `04_Drawings`, `06_Photos`, `07_Video`, `08_3D`.
- `01-Projects Vault/C2M/` — **canonicalized 2026-08-13** (gap closed). `M100-SAILS_Clipper_Ship`, `M101-DOTS_Distance_of_the_Sun`, `M999-C2M_Misc`, `M000-C2M_Standards`; same ten-folder convention, month subfolders for unnamed media. Provenance + flag legend: `_README_provenance.md` at C2M root; manifests in `mb3design-site/.c2m-triage/` (gitignored). Also created: `01-Projects Vault/FACTURE/` (portfolio material), `05-RFP Vault/` (unsuccessful bids).
- `04-Website Vault/{sails,dots,badm}/{01_Vision…07_Reveal}/` — **derived, generated, never hand-curated** (ruled 2026-08-15). Selects are rows in `docs/ref/selects_manifest.csv` (repo); `scripts/materialize_selects.py` copies + hash-verifies them into the vault folder. Edit the manifest, re-run the script; `--prune` removes stale files.
- Vault originals are read-only in practice: curation = copy selects out; never move, rename, or delete originals. C2M sources (`z_PROJECTS_ARCHIVE/C2M/`, `~/Documents/_temp/_C2M misc/`) remain in place uncurated; retiring them is Phase 4, manual, Mark-only.
- Media binaries never get committed to this git repo. Web-optimized exports only, into the site asset pipeline.

## Session start checklist

1. Read `docs/ref/plan_story-development.md` for current status and next task.
2. Read `docs/ref/framework_story-development.md` before drafting narrative.
3. Check `docs/content/about/stat_verified-numbers.md` before citing any metric.
4. Confirm with Mark which work-order item is live before generating.
