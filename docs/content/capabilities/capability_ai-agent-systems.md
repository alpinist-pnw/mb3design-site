---
category: capability
title: AI Agent Systems for Design and Fabrication Coordination
source: podcast-prep_2026-04-21T0930_jordan-salvador-full-brief.md, podcast_2026-04-22_jordan-salvador-deck.html
verified: true
---

## AI Agent Systems

MB3 is building AI agent systems where agents handle coordination — tracking which decisions affect which other decisions across multiple construction disciplines — and judgment gates stay with the human.

The agents do not decide. They surface the right decision to the right person at the right time.

**Current state:** Testing on MB3's own ADU project in Seattle. Real permits, real money. This project is being used to validate the system before it goes near client work.

**Architecture:** SQLite + YAML schema, constraint propagation, event-driven. Not a proprietary platform — a designed system built on durable primitives.

**Production AI use (now):** Proposal acceleration, material takeoff support, content pipelines, structured data extraction. Applied where MB3 has deep enough context to direct it.

**Experimental AI use (testing):** The agent coordination system described above. Not yet validated for client projects.

---

## The Governing Principle

The system is designed around the insight that the human judgment layer is the highest-value input at specific decision points — not at every step. AI handles the coordination, tracking, and pattern-matching inside the project. The human brings cross-domain experience that tells you which pattern from a different industry applies to the problem in front of you.

Automate the coordination. Keep the judgment human.
