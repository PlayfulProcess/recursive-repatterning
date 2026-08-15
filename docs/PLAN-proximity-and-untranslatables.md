# Plan — a proximity map, and the words that don't translate

Draft for review. Nothing built yet.

---

## 1. The gap, measured

`metadata.emotion_key` is currently the only automatic connection between schools, and it works by
**string equality**: two items connect when their keys match exactly. Counting what that actually
yields across the 22 schools:

- **8 keys are shared by two or more schools**: `anger`, `fear`, `sadness`, `joy`, `love`,
  `disgust`, `desire`, `surprise`
- **73 keys appear in exactly one school** and therefore connect to nothing:
  `shringara`, `spes`, `xi`, `nigredo`, `bibhatsa`, `saturnine`, `allegrezza`, `karuna`, `bei`…

Read that list of eight again. It is, near enough, **Ekman's six plus two**. So the library's only
automatic linking mechanism fires exactly for the categories the basic-emotion tradition proposed as
universal, and stays silent everywhere else. A reader clicking through connections would experience a
library that quietly agrees with the school it was built to question.

**The orphans are not a bug.** `shringara` must not collapse into `love`; `spes` must not collapse
into `hope`. That refusal is a deliberate, documented decision and it should stand. The problem is
narrower: the schema can say **"the same as"** and nothing else. There is no way to say
**"near, and here is how it differs"** — which is the relation almost every interesting case needs.

## 2. Untranslatables — where the gap bites hardest

Portuguese **saudade** has no clean English equivalent. It sits somewhere among longing, nostalgia,
missing-someone and a bittersweet pleasure in the absence itself, and is exactly none of them. The
reverse holds too: English **grief** does not map cleanly onto Portuguese, which distributes that
territory differently.

Others with the same shape: German *Sehnsucht* and *Schadenfreude*, Japanese *amae*, Russian *toska*,
Czech *lítost*, Danish *hygge*, Greek *meraki*, Yoruba/Nguni *ubuntu*, Tagalog *gigil*.

Under the current schema each of these becomes an orphan key — technically correct, and useless. What
they need is a way to say *"adjacent to longing and nostalgia, overlapping neither."*

This is not a new argument for this library; it is **Wierzbicka's** (already in
`docs/GENEALOGY-OF-EMOTIONS.md` Part C) and **Viveiros de Castro's controlled equivocation** — the
danger in translation is not failing to find the match, it is assuming you found one.

## 3. The proximity map — and its one serious trap

The idea: embed the terms, project to two dimensions, and let a reader *see* that `saudade` sits near
`longing` and `grief` without landing on either. Distance carries the meaning that a boolean key
cannot.

**No new dependency is needed.** This repo already ships both plausible renderers:
- **D3 v7** — loaded by `viewers/genealogy-tree.html` and `viewers/timeline.html`. A 2-D scatter with
  zoom and labels is straightforward D3, and both files already contain working zoom/pan code to copy.
- **Cytoscape.js** — already vendored at `public/vendor/cytoscape.min.js` and used by
  `genealogy.html`. Better if the display is a *nearest-neighbour graph* rather than a plane.

Nothing needs to ship a vector database or a heavy projector. Precompute offline; store almost nothing:

1. Embed each item's name + `Definition` with a sentence-embedding model, as a build step.
2. Reduce to 2-D (UMAP or PCA) **offline, in a script**, and store only `metadata.map_xy: [x, y]`.
   Two floats per item, not 1,536.
3. Optionally store `metadata.nearest: [{id, score}]` — a handful of neighbours per item, which is
   what a graph view needs and is far more inspectable than raw coordinates.
4. Render with D3 or Cytoscape from those precomputed values. No runtime model call, no key, no cost.

### The trap, which is the whole design problem

**A sentence-embedding model trained mostly on English text will place `saudade` where English
writing about saudade puts it — not where Portuguese speakers live it.** Using such a model to map
untranslatability would import precisely the bias the library exists to document. It would be the
forced-choice error again, in vector form: supplying the categories and then measuring agreement with
them.

So the map must not be presented as the truth about these concepts. Two honest framings, and I'd take
the second:

- **(a) Label it plainly** — "how these words cluster in a large, English-dominant text corpus." True,
  useful, and modest.
- **(b) Treat the embedding as one more school.** It *is* one: a folk taxonomy of feeling, learned
  from a corpus, with its own biases and blind spots — exactly the kind of object this library
  collects. Give it an `evidence_tier`, state what corpus produced it, and let it sit beside Plutchik
  and Ekman as another constructed map rather than above them as the measurement.

**(b) is stronger**, and it turns the trap into content: a map that disagrees with the schools is more
interesting than one that confirms them.

**A further move, if it's cheap:** embed with **two different models** and show they disagree. Two
machines trained on different corpora placing `saudade` in different neighbourhoods would demonstrate
the library's central claim more vividly than any paragraph — variability, shown rather than argued.

## 4. Expressing "near but not the same" in the data

Before any map, the relation itself needs somewhere to live. Options:

- **(a) Prose plus an explicit cross-link.** Use the existing `source_deck`/`source_item_id`
  mechanism to point at the nearest terms, and state *the difference* in the item's own sections. No
  schema change; `CLAUDE.md` forbids inventing a second link field.
- **(b) A `metadata.near` array** of `{id, note}`. More machine-readable, but a new field, and the
  rule against those exists for a reason.

**Recommend (a).** A `near` field would quietly assert similarity and leave the difference unwritten;
prose *forces* someone to say how the terms diverge. That is controlled equivocation implemented as
an editorial habit rather than a data structure — and it is the honest version. Precomputed
`nearest` coordinates from §3 can serve the machine-readable need without pretending to be an
editorial judgement.

## 5. Sequencing

1. **An `untranslatables` school** — saudade, Sehnsucht, amae, toska, lítost, gigil, and the reverse
   cases where English carves differently. Each item keyed to its own transliterated term, each
   cross-linked to its nearest neighbours with the *gap* written out. This is buildable now, needs no
   new machinery, and is worth having on its own.
2. **The offline embedding script** — `scripts/build_proximity.py`, writing `map_xy` and `nearest`
   into item metadata. Reproducible, committed, re-runnable.
3. **A map viewer** — `viewers/proximity.html`, D3 scatter or Cytoscape graph, reading the
   precomputed values. Framed per §3(b).
4. **Two-model disagreement**, if step 2 proves cheap.

## 6. Open questions

1. Which embedding model? Local (`sentence-transformers`) keeps it reproducible and free with no key,
   which suits a commons artifact better than an API.
2. Does the map include all 22 schools' items (~194) or only emotion-level ones? Mixing skills,
   gestures and archetypes into a "semantic space of feeling" would muddle it — probably filter to
   items carrying an `emotion_key`.
3. Does the untranslatables school sit in an existing branch, or does it need one? It is a claim about
   *language*, which no current branch covers.
