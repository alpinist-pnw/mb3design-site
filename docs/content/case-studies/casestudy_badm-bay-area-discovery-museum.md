---
category: casestudy
title: Bay Area Discovery Museum — Fort Baker, Sausalito CA
source: podcast-prep_2026-04-21T0930_jordan-salvador-full-brief.md, snoopy-questing-thacker.md
verified: true
---

## Project Overview

**Client:** Bay Area Discovery Museum
**Location:** Fort Baker, Golden Gate National Recreation Area, Sausalito, CA
**Architect:** Olson Kundig
**Fabricator:** Pacific Studio, Seattle WA (Mark Buchanan, Director of Technical Design)
**Scope:** Three exhibit environments across three historic Army buildings on National Park Service land
**Production approval:** M. Buchanan, 03/18/2020

---

## The Challenge

The Bay Area Discovery Museum sits inside historic U.S. Army buildings at Fort Baker, managed by the National Park Service. Three hard constraints eliminated every conventional shortcut:

**NPS Reversibility.** No permanent alterations to the historic structures. Every attachment must be fully reversible — full restoration to original condition possible. You cannot lag into the structure.

**As-Built Uncertainty.** Every building interior was 3D laser-scanned to create a digital as-built envelope: every ceiling joist, rafter, column, out-of-plumb wall, window placement. The exhibit had to fit that envelope precisely without permanently touching the building — and no architectural plans could be trusted over the scan.

**Children's Museum Durability.** Thousands of kids climbing, jumping, and crawling daily. Museum-grade structural integrity throughout, non-negotiable.

---

## The Fork in the Road

Early in the Bay & Water Room, a fundamental fabrication decision:

**Option 1 — Stack-laminate (rejected):** 2D CNC-cut plywood sheets stacked horizontally. Approximately 2x faster to production, approximately 2x less CAD/engineering time up front. But approximately 2.5x heavier than the optimized approach, massive material consumption, gaps between exhibit and building requiring scribing filler pieces on-site, and unable to satisfy NPS reversibility cleanly.

**Option 2 — Optimized 3D lattice (chosen):** Engineered lattice structures covered in thin plywood skins, with human-decided weight-reducing cutouts drawn in the 3D model and output to 2D drawings and CNC g-code. More CAD/engineering hours up front. Approximately 2.5x lighter, every connection to the building pre-resolved against the 3D scan, reversible attachment strategy validated digitally.

The "obvious" efficient choice was actually the expensive one when material, shipping, installation, and NPS constraints were fully accounted for. The only way to make that evaluation with confidence was inside the 3D model.

---

## Fabrication Complexity

- **3 buildings** (BLDG 559, 637, 645)
- **564 pages of shop drawings** across 6 PDFs
- **84 pages of individual part file drawings**, each a unique fabricated component
- **500+ CNC-carved plywood slices** — Bay & Water Room: direct stack forming landscape; Forest Room: vertical stack with block separators and custom blackened steel organic plates
- **500+ sheets of 1/2" burple plywood** (maple and Baltic birch faced, expressed edge as design element)
- **Multiple fabrication methods on one project:** CNC router (wood slices), waterjet (steel plates up to 3/4"), laser cut, brake forming, laser engraving

**Tree structures (Forest Room):** At least 3 tree sculptures, each unique, each with its own bill of materials. Tree #2 alone: 36+ unique waterjet-cut steel parts. Main vertical: 0.750" steel plate, 260 lbs, approximately 114" tall, cut to an organic profile. Tolerances: ±1/16" on waterjet profiles (±0.030" at best); ±0.0005" on CNC-machined pilot holes only. All parts etched with part numbers — traceability baked in.

**Two CAD systems, one pipeline:** Rhino 3D for organic surfaces; SolidWorks for structural steel.

**Part numbering:** Hierarchical — `692-[building]-[system].[subsystem].[part]-[sequence]`

---

## The "Model Caught It" Moment

The tree sculptures tie into ceiling joists above for seismic stability. Only a few joists were available above each tree — not evenly spaced. The trees were locked into the landscape base: everything interconnected.

If a tree had to shift to find a joist, the entire exhibit base would have had to move, or major rework to connection points. Because the 3D scan captured every joist position and the model was fit-tolerance checked against as-built conditions, every tree-to-joist connection was resolved before fabrication. The install crew walked in and the connections were where they needed to be.

---

## Front-Loading Investment and Outcome

- **CAD labor quoted:** 1,728 hours
- **CAD labor actual:** 4,487 hours (2.6x) — CAD and drawing hours only, not total project budget

The overage was not a failure. It was the cost of virtual prototyping at the level required by the project's constraints.

**Installation outcomes (verified by install crew):**
- Integrated leveling feet eliminated the need to shim and scribe large plywood sections on site
- Varying window placements, out-of-plumb walls, floor anomalies, and irregular joist spacing — all resolved in the model
- Rework estimated at 60–80% less than what Pacific Studio normally expects on ambitious installations

Pacific Studio adopted the front-load approach on virtually all subsequent projects.

---

## The Cross-Domain Connection

The virtual prototyping discipline applied on BADM came directly from the Paul Allen yacht project (M/Y Octopus, 2000–2003). On the yacht — a 410-foot, $250M vessel — the team built a fully coordinated 3D model shared with the shipyard, trades, and vendors at a time when BIM had barely launched. The lesson: front-load the model, coordinate in virtual space, go to fabrication with certainty.

Different industry, different scale, different constraints. Same pattern.
