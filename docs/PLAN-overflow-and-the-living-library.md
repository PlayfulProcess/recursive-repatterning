# Plan — Overflow, the Ethics of Fiction, and turning the library into a living practice

What was pulled from the live channels, how it fits, and what enrichment means concretely.
Written after reading the app-side grammars directly via MCP.

---

## 1. What exists in the app, and where each piece belongs

### The centre: Overflow (22 cards, Aug 2026)
The library's missing first-person voice. Everything in repatterning so far curates *other
people's* schools; Overflow is the maintainer's own — Structure / Process / Possibility, the
recursion where possibility hardens into the next structure, and the single ethical question
("Am I overflowing or extracting?"). It is Barrett-grounded (allostasis, prediction, body
budget run all through it), it names The Pattern with `repatterning` as a keyword, and it is
already deck-shaped and castable.

**Fit: `schools/overflow`** — imported verbatim, plus **The Overflow Spread** in
`viewers/spreads.json` (three positions + the recursion rule), which makes it castable in the
existing caster with zero new mechanism. In flight.

**The standard it is held to:** `evidence_tier: "theoretical"`, same as Plutchik and the
alchemists. The maintainer's own school judged by the library's own instrument is the
strongest credibility move available — the one thing a critic cannot say is that the house
school got a pass.

### The judge: The Ethics of Fiction (31 items, Aug 2026)
Four branches grown from one trunk — Lenses (six ways of judging a story), Contexts (soils a
story lands in: the Famine, the Feed, the Hearth…), Cases (worked verdicts: Hansel & Gretel,
Frozen, the Palantír, Bettelheim judged by his own standard), Synthesis (the Freedom Test,
the Two Temperaments). Generativity as a property of *casting × story × context × receiver*,
never of a story alone.

**Fit: `schools/ethics-of-fiction`** — in flight. It interlocks with Overflow (the Freedom
Test is a card in one and a synthesis item in the other) and gives the library something it
did not have: a way to judge *stories*, where the genealogy judges *taxonomies*.

### Together they justify a branch of their own
Neither is a curated historical school; both are the house's own synthesis. Proposed branch:
**"The House School"** — with a note stating plainly that these are the maintainer's own
constructions, held to the same evidence discipline as everything they sit beside. (Name open
to veto; "Overflow & Fiction" also works.)

### The essays: Relationship is Process (6 versions, Substack)
**Fit: a course** — `course/relationship-is-process.mdx`, alongside the history course. The
essay-versions grammar shows the revision history; the course shows the essay. The Substack
posts are the source; the course pipeline (mdx → course-viewer) already exists and works.
Future Substack texts follow the same path: essay → course when it stabilises.

### The fiction: Lilás (116 items), Passarinho (104), A Children's Commedia (40)
**Fit: stay in the app; the repo cross-references.** These are living creative works, not
schools. The Ethics of Fiction already treats Lilás as a Case ("the Judge's Own Garden") —
that is the right relationship: the repo holds the *instrument*, the app holds the *garden*
it is used on. Importing them would freeze them and double the sync surface. When the channel
sync arrives (the later plan), they join as channel members, not repo files.

### The practical tools (Wellness + Relationship & Parenting channels)
Nine tools currently scattered across claude.ai artifacts, a ChatGPT GPT, jongu-old.vercel,
and journal.recursive.eco:

| Tool | Today | Disposition |
|---|---|---|
| NVC journaling | jongu-old.vercel | **Already ported** — `tools/nvc-journaling.html`, reads the grammar |
| Parental Love Bank | claude.ai artifact | Port next (PLAN-practices-layer Phase 3) — practises `gottman-method` + `attachment-theory`; its four `window.claude.complete` calls become the assistant handshake |
| Gottman Bagel Method | **a ChatGPT GPT** | Port eventually — practises `gottman-method` (perpetual problems / Bagel). Highest-friction dependency in the whole set: a rented tool on someone else's platform |
| Wheel of Life | claude.ai artifact | Listed in `tools/_tools.json` as external for now |
| Reframe a Thought | claude.ai artifact | Same — practises CBT territory (`dbt-skills` adjacent) |
| Best Possible Self | journal.recursive.eco | Same — already on own infrastructure, just needs listing |
| Morning Pages | book link | Listing only (reference, not a tool to port) |
| Stoic Framework v1/v2 | claude.ai artifacts | Same — and note `greek-pathe` covers the Stoics; a future stoic tool should read that school the way NVC journaling reads `nvc-needs` |

`tools/_tools.json` gains these as entries with an `external_url` field (the manifest is
repo-owned; extending it is legal where extending grammars is not). The tools index page —
Phase 2 of the practices plan — becomes worth building now that there are nine entries
rather than one.

## 2. "Enrich the thin grammars" — what that means concretely

The skeletons are honest but shallow: most schools have 5–8 L1 items with `_note`s listing
what is unwritten. Enrichment priorities, in value order:

1. **Wire Overflow through the library.** Its cards name concepts other schools hold —
   The Prediction ↔ constructed-emotion, The Ceding ↔ nvc-needs' requests, The Ledger ↔
   the moral-arithmetic NVC's pseudo-feelings critique circles. Cross-links here make the
   house school the connective tissue, which is what a centre is for.
2. **Complete the four most-visited skeletons** (rasa is done; Aquinas's remaining six
   passions, Aristotle's remaining pathē, the Chinese seven, Ekman's contempt debate).
3. **The `untranslatables` school** — the proximity build already produced its evidence:
   45 words absent from a 400k-word English model.
4. **The gap-finder's list** — despair, dismay, indignation, sympathy, humility,
   generosity, bewilderment — as new items in whichever school each genuinely belongs to.

## 3. The mechanistic-interpretability instinct — and the visual for story-release

"Externalize internal states the way mech-interp does" is already half-built: the proximity
viewer IS a cut of a model's internal representation space with the library's vocabulary lit
up in it — interpretability's move (open the model, look at the geometry) applied at word
scale. What is missing is the *dynamics*: release and reintroduction, the recursive turn.

**Proposed: the Spiral view** (`viewers/spiral.html`, later). The Overflow deck defines the
motion — Structure → Process → Possibility → new Structure. The visual:

- A cast reading renders as one turn of a spiral (three positions on an arc).
- "Release" = a story/card consciously retired: it moves to the Heap (the deck has the card
  for this already — compost, not deletion; the record stays, greyed, load-bearing).
- "Reintroduce" = the next turn begins with the previous Possibility placed in the Structure
  position — the recursion made literally visible as geometry.
- Successive readings stack as successive turns, so a person's repatterning history becomes
  a visible spiral: which structures recurred, which were composted, what grew.
- Each card on the spiral can open its proximity neighbourhood — the "internal state" of the
  word in the borrowed model — so the two views answer each other: the spiral shows *your*
  process, the scatter shows *the corpus's* priors you are working inside.

That is the mech-interp gesture done honestly: not claiming to read minds, but externalising
the artifacts — the model's geometry, the person's own sequence of castings — and letting
the person do the interpreting. Sequencing: after the imports land and the spread is
castable, since the spiral is a *history of casts* and needs casts to exist first.

## 4. Sequencing

1. **In flight:** `schools/overflow` + `schools/ethics-of-fiction` + the Overflow Spread.
2. Wire branch ("The House School"), rebuild, verify castable end-to-end.
3. `tools/_tools.json` external entries + the tools index page (Phase 2 of practices plan).
4. `course/relationship-is-process.mdx` from the Substack essays.
5. Overflow cross-links through the library (§2.1).
6. The Spiral view (§3) once casts exist to display.
7. Channel sync via the app UI — later, per the maintainer; everything above keeps working
   standalone until then.
