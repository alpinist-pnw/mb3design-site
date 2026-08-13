# Story Development Framework — MB3 Design Site

How project stories get built in this repo. This is the method; `plan_story-development.md` is the status board; `_TEMPLATE_casestudy.md` is the output shape.

---

## The narrative spine

Every MB3 case study runs on the same five-beat spine. This is derived from BADM (the reference standard) and from the Sails video storyboard arc (wonder → complexity → craft → awe). A story missing a beat isn't done — it's either under-researched or the project doesn't belong in the case-study slate.

**1. The Impossible Ask.**
What walked in the door and why couldn't a conventional shop deliver it? Named constraints, not adjectives. BADM: NPS reversibility + as-built uncertainty + kids-museum durability. Sails: an artist's sketch of a 60' clipper ship with basketball-hoop sails, inside an arena, on an immovable opening date.

**2. The Fork.**
The real decision with real tradeoffs, where the "obvious" choice was wrong once fully costed. BADM: stack-laminate vs. optimized lattice. This beat is where strategic-partner positioning lives — a vendor executes the drawing; a partner reframes the problem. Every case study needs its fork identified before drafting begins.

**3. Judgment Under Irreversibility.**
The moment where the front-loaded model (or field judgment) caught something that would have been unrecoverable later. BADM: tree-to-joist connections resolved before fabrication. Sails candidates: same-day anchor-bolt/rebar resolution; adjustability engineered into mounts before the pour. Concrete, timestamped, specific.

**4. The Verified Outcome.**
Numbers with provenance. Quoted-vs-actual honesty is a feature, not a liability (BADM's 1,728 → 4,487 CAD hours reads as integrity, not overrun). Delivery record, rework reduction, field-mod counts, schedule performance. Anything unconfirmed carries a VERIFY flag until Mark signs off.

**5. The Transfer.**
What pattern this project proves that carries to the next domain — and to a prospective client's problem. BADM ← Octopus (virtual coordination). Sails → any structure with a fixed public opening. This beat is the bridge to the consulting thesis: same judgment, new domain.

## Sourcing rules

- **Three source classes:** (a) verified repo sources in `docs/ref/` (podcast-prep brief, storyboard, resume bullets Mark authored); (b) Mark's direct recall captured in-session; (c) inference. Classes (a) and (b) can ship. Class (c) never ships — it becomes a question.
- **`stat_verified-numbers.md` is the canonical metrics ledger.** New verified numbers get added there when confirmed, then cited from case studies. One source of truth; no number drift between files.
- **VERIFY flags are HTML comments** so they never render: `<!-- VERIFY: total sculpture weight -->`. **ASK blocks** mark places where the story needs Mark's memory, phrased as specific interview questions, not "add details here."

## The extraction interview

When a story is thin (LAX currently), don't pad — interview. Per beat:

- *Impossible Ask:* What did the client/artist believe couldn't be done? What did competitors say or decline?
- *Fork:* What alternative did you reject, and what would it have cost fully accounted? What made the chosen path look expensive up front?
- *Irreversibility:* What single mistake would have been unrecoverable? What did the model catch? What broke anyway, and how fast was it resolved?
- *Outcome:* What numbers exist in project records (weights, hours, mod counts, schedule deltas)? What did the client do next (repeat work, referral, adopted your method)?
- *Transfer:* Where had you seen this problem shape before? Where since?

Run these as a working session (grill-me style), checkpoint answers into the story's ref file, then draft.

## One story, many surfaces

Each case study is the master source; derivatives are cuts, never rewrites from scratch:

| Surface | Cut |
|---|---|
| Site case study | Full five-beat spine (the master) |
| Video chapters (Sails model) | Vision / Translation / Prototyping / Fabrication / Logistics / Install / Reveal — map beats 1–5 across chapters |
| LinkedIn post | One beat per post — a Fork or an Irreversibility moment stands alone |
| SRD consulting proof | Beat 3 + Beat 5 pairing (judgment + transfer) |
| Interview STAR story | Lives in Career 2026, NOT here — different register, keep separated |

## Definition of done

A case study ships when: all five beats present · zero unresolved VERIFY flags · every metric traced to `stat_verified-numbers.md` or a ref/ source · voice passes the "could any fabricator say this?" cut test · Mark can put his name on it and defend it (Visceral Residue Test).
