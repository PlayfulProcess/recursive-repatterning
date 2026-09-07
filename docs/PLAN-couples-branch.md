# Plan — the couples branch (a branch, not a rebrand)

*Stub, 6 September 2026. The full plan lives in the modelling repo; this file records what
lands **here** and why the library is not being narrowed to do it.*

## The decision

The couples/relationship line splits by layer:

- **Engine** → `emergence-lab` — the models, the parameter sweeps, the logged failures.
  Model 03, `models/dyad-lab.html`, already runs.
- **Surface** → **here** — the course and the tool, because this is where a person looking
  for a practice already lands.
- **Argument** → `book-repo`, NWTO ch. 11 ("The lip") and ch. 17.

**Full plan:** `emergence-lab/docs/PLAN-couples-course-and-agenda.md`.

## What this repo is NOT doing

Not becoming a couples/family platform. Rule 7 of this repo's `CLAUDE.md` forbids
totalising scope, and the library's actual value is that it holds Rasa beside DBT beside
the Affektenlehre. Narrowing that to one relational domain would trade away the only thing
here that nothing else has. A **branch** gets the reach without the cost.

## What lands here

1. ~~**A course — "Two Rims"**~~ — **BUILT: `tools/two-rims.html`**, registered in
   `tools/_tools.json` (renders as a hosted card, first in the list).

   **It shipped as a tool, not as `course/<slug>.mdx`, and that was a deliberate departure
   from `HOW-TO-WRITE-A-COURSE.md`.** That pipeline renders prose; this course's whole
   engagement mechanic is a live model the reader drives, which MDX through
   `pages/course-viewer.html` cannot carry. `tools/` is already where this repo puts
   self-guided interactives (`nvc-journaling`, `living-into-values`), so it went there.
   The prose guardrails from that doc still applied and were followed — honesty spine,
   no overclaiming, report against yourself.

   **v2 REBUILD (Sep 6, evening) — the builder walked v1 and did not understand it.**
   "If I did not understand nobody will." Diagnosis, in order of damage: (1) v1 quizzed
   before it showed — you cannot predict a system you have not seen, so the gate felt like
   a test you were set up to fail; (2) numbers instead of meaning ("resting tone 1.20");
   (3) two wobbling lines labelled A and B — nothing to picture; (4) nine dense steps, the
   first two being setup for a modeller. v2 inverts all four: **watch first, then guess
   about one change, then see it**; two faces (Sam and Alex — not real, not you) whose
   expression and colour ARE the mood, with words (warm / okay / tense / cold / icy) and no
   numbers anywhere; six steps; the population lesson as a room of a hundred couples with
   a fortune-teller putting rings on them, then the endings colouring in. Both the
   dial-sweep discipline and the "watch the words, not the prose" rule caught a fresh bug
   in v2 (the repair step's dial looked dead because the caption only reported endings and
   the dip happens in the middle — now the caption reports the dip).

   **v1 shape, for the record:** nine steps, each with a **prediction gate** — you must commit to an answer
   before the model will show you, which is the same discipline `LAB-DESIGN.md` used with
   H1–H5, enacted rather than described. Then a *lab beat* (one dial, live chart, verdict on
   your guess) and a *life beat* ("On a Tuesday", a question, never advice). Ends with a
   scorecard of what you called before seeing it, plus the *what this cannot tell you*
   table. Progress and answers in `localStorage` only. Yardstick inherited from AI 101: a
   curious 70-year-old must enjoy it.

   **Three errors were caught by testing the dials rather than trusting the prose** — worth
   keeping, because all three were plausible-sounding and wrong:
   - Step 4's threshold dial did *nothing* across its whole range: the pair opened warm, so
     the threshold never bound. Fixed by opening the conversation cold (and switching repair
     off, since it isn't introduced until step 5).
   - Step 5's repair dial did nothing: the knock never carried them below zero. Fixed with
     a larger symmetric knock from the warm attractor.
   - Step 1's explanation claimed inertia changes only *how long* recovery takes. False —
     the resting point is baseline/(1−inertia), so inertia moves the destination too.
     Rewritten, and it now sets up step 2 instead of contradicting it.
2. **A tool entry** in `tools/_tools.json` — done, schools
   `gottman-method` / `eft-bonds` / `attachment-theory`.
3. **Enrichment of the four relational schools already here** — `gottman-method`,
   `eft-bonds`, `attachment-theory`, `nvc-needs` — with the verified numbers from
   `book-repo/books/what-survives-the-number/research/couples-therapy-dossier.md`.
   Note the `evidence_tier` discipline applies: Johnson's EFT and the Gottman method do not
   have equivalent evidence bases and the library must keep saying so.

## The floor (non-negotiable)

The modelling form of this repo's existing rule that a feeling-label is never a diagnosis
nor something to obey:

- **Never state a simulation output as a prediction about a person.**
- No scoring, no "your couple type", no persistence, nothing sent anywhere.
- Partners are labelled **A and B**.
- Every published model carries a *what this cannot tell you* table.

Claims are **psychoeducational, not clinical.** A simulation can show a story is coherent
and teach a mechanism; it cannot make a claim about people true.

## Naming — deliberately unresolved

The couples surface is **not** branded "overflow" for now. Couples are one instance of
overflow, not its home, and the work has to be usable by someone who rejects the overflow
thesis entirely — otherwise it is advocacy wearing a lab coat. `schools/overflow` keeps the
name; the couples branch does not take it. Rung R2 in the full plan (a body-budget reserve
variable in the dyad) is the actual test of whether overflow says anything a dyadic model
needs — **let that decide.**

## Disambiguation, per `CLAUDE.md` rule 5

"EFT" here means Sue Johnson's *Emotionally* Focused Therapy (couples, attachment) —
`schools/eft-bonds`. Not Greenberg's *Emotion*-Focused Therapy.
