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

1. **A course — "Two Rims", one course with two beats per lesson.** Each lesson is one dial
   in the Dyad Lab (a *lab beat*: one aha, one under-the-hood panel) plus the same idea as a
   question to sit with (a *life beat*, never advice). Nine lessons; the built lab already
   supports 1–6, and 7–9 need only text. Uses the existing `course/` pipeline and
   `pages/course-viewer.html`. Yardstick inherited from AI 101: a curious 70-year-old must
   enjoy it.
2. **A tool entry** in `tools/_tools.json`, beside `nvc-journaling` and
   `living-into-values` — the bare lab with all dials exposed.
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
