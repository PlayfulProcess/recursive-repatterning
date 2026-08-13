# Seed material index

The files alongside this README are **local working copies, deliberately gitignored.**
They live canonically elsewhere; duplicating them into git would fork the content and
create exactly the drift this project family tries to avoid. This index is the
committed part — it records what exists and where the real copy lives.

Re-populate the working copies at any time by re-running the copy step (see
`docs/BUILD-PLAN.md`).

## Built grammars — canonical home: `recursive.eco-schemas/grammars/<slug>/grammar.json`

| Seed file | Items | State | Register | Constellation branch |
|---|---|---|---|---|
| `grammars/plutchik-wheel-of-emotions.json` | 42 | Polished | **Kids / myth-retelling** | basic-emotion |
| `grammars/plutchik-ADULT-DRAFT.json` | 32 | Unpublished draft | **Adult / oracle** | basic-emotion |
| `grammars/dbt-wise-heart.json` | 35 | Polished | **Kids / myth-retelling** | skills-based |
| `grammars/relationship-cards.json` | 68 | Built, unpolished | Adult / oracle | attachment-couples |
| `grammars/expression-of-emotions.json` | 19 | Built | Adult / scientific | historical-scientific |
| `grammars/jungian-archetypes.json` | 34 | Built | Adult / oracle | parts-and-depth |
| `grammars/bus-passengers.json` | 33 | Built, **published** | Adult / contemplative | parts-and-depth |
| `grammars/principles-of-psychology.json` | 21 | Built | Adult / scientific | historical-scientific |
| `grammars/decolonizing-childhood.json` | 64 | Built | Mixed | skills-based |

Canonical source for the adult Plutchik draft is
`recursive.eco-schemas/schemas/tarot/plutchik-wheel-emotions.json` — note it is **not**
in that repo's `manifest.json` and has never been published. Per the hybrid-register
decision it is the basis for the adult-facing Plutchik school.

### Known issues to fix before reuse
- `relationship-cards.json` — **every one of its 298 sections still carries a
  `[SESSION-N: SUITNAME]` build tag** in the prose. It is a deliberate content skeleton
  (structured research notes, 50–100 words), not final copy. Needs a polish pass.
- `jungian-archetypes.json` — has no `roots`/`shelves`/`lineages` set, inconsistent
  with every other grammar here.
- **None** of these grammars set `image_url` on any item (0 coverage across all nine).
  Illustration is a clean-slate decision here, not an inheritance.

## Plans — canonical home: `recursive.eco-schemas/plan/`

| Seed file | What it is |
|---|---|
| `plans/family-therapy-grammar-plan.md` | **Unbuilt** ~120–160 item taxonomy: Gottman, EFT, attachment, child/play therapy, pedagogy, trauma, family systems. The taxonomy work is done; nothing is built. `relationship-cards` was extracted from this and built first, so this is the superset. |
| `plans/relationship-cards-game-plan.md` | Design record for the built deck. **Contains a ready-made AI system prompt** for interpreting card draws — directly reusable for the casting feature. |

## Prose research — not yet grammar-shaped

| Seed file | Canonical home | What it gives us |
|---|---|---|
| `prose/interoception-to-emotion-pipeline.md` | `emergence-lab/docs/` | Barrett, interoception, affect labeling, the four-stage pipeline, **and an explicit argued critique of Plutchik vs. NVC's structural fit**. This is the constellation's connective tissue. |
| `prose/evidence-based-practices.md` | `emergence-lab/docs/` | Evidence-ranked practices (social connection > sleep > exercise > MBSR > journaling > gratitude). Seeds the behavior-activation grammar and the `evidence_tier` metadata. |
| `prose/08-process-oriented-therapy.md` | `tarot-as-myth/research/tarot-self-knowledge/` | Distinguishes Greenberg's **Emotion-Focused** Therapy from Johnson's **Emotionally Focused** Therapy. Two different frameworks, one acronym — do not conflate them in the grammars. |

## Deliberately NOT copied

`recursive.eco-schemas/writing/` holds four personal essays (couples therapy, DBT for
kids, a social-work masters, NVC notes) with real bibliographies that would otherwise be
good seed material. **They are personal and discuss family and career specifics.** They
need a privacy review before any sentence of them enters a public repo. Left out on
purpose — not an oversight.

## Genuinely missing — the actual authoring work

No grammar exists anywhere for:

1. **NVC / Rosenberg** — feelings/needs, met vs. unmet. Note there is no single canonical
   CNVC list; trainers publish variants. Say so in the grammar rather than picking one
   silently.
2. **Barrett / Theory of Constructed Emotion** — adapt from `prose/interoception-to-emotion-pipeline.md`.
   Per the editorial stance this is the **substrate**, not a peer school.
3. **Brené Brown / Atlas of the Heart** — 87 emotions across 13 categories. In copyright:
   paraphrase category definitions, never quote. Deferred past MVP.
4. **Ekman basic-emotions** — optional; the other basic-emotions school beside Plutchik.
