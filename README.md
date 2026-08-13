# Recursive Repatterning

An open library of the ways people have organized feeling — each school in its own voice,
none of them mistaken for the truth underneath.

**Status: scaffolding.** The chassis is up; the content is being assembled. See
[docs/BUILD-PLAN.md](docs/BUILD-PLAN.md).

---

## The premise

There are no fixed biological fingerprints for emotions. The 2019 meta-analysis behind
that claim (Barrett, Adolphs, Marsella, Martinez & Pollak) found no reliable, specific
facial or physiological signature for discrete emotion categories — the same labeled
emotion varies enormously by context and culture.

That result is usually read as deflationary. It isn't. If emotion concepts are learned
rather than found, then the concepts are doing real work — and which ones you have
access to changes what you can regulate. Emotional granularity research bears this out:
people who distinguish finely between unpleasant states are meaningfully better at
regulating them.

So this library takes a specific position:

> **The constructionist account is the substrate. Every school above it is an interface.**
> Plutchik's wheel, NVC's needs, DBT's skills, attachment theory's bonds — none of them
> is the machinery. All of them are usable. A map being constructed is not the same as a
> map being wrong.

You can play tarot without believing Hermes Trismegistus handed it down. You can name a
feeling without believing the name was waiting inside your body to be discovered.

## How it's organized

Each school of emotion is **its own grammar, in its own voice** — never flattened into a
single house taxonomy. A constellation meta-grammar composites them:

```
schools-of-emotion  (constellation root)
├── Constructionist — the substrate      ← the frame, not a peer
├── Basic-Emotion Schools                 Plutchik · Ekman
├── Needs-Based Schools                   NVC / Rosenberg
├── Attachment & Couples                  Gottman · Johnson (EFT) · Bowlby
├── Skills-Based                          Linehan / DBT · behavior activation
├── Parts & Depth                         IFS / parts work · Jung
└── Historical & Scientific               Darwin 1872 · James 1890
```

This is the same `composite_of` mechanism the rest of this project family uses for
meta-grammars — one mechanism catalogues everything.

### Honesty by construction

Two conventions carry the epistemics into the data itself, so a reader doesn't have to
already know what to ask:

- **`metadata.evidence_tier`** on every school — `independently-replicated` /
  `growing` / `observational-only` / `theoretical`, with a note. Sue Johnson's EFT and
  Gottman's method do not have the same evidence base, and the library should say so
  rather than issue both an undifferentiated "evidence-based" badge.
- **`metadata.emotion_key`** on every item — the cross-grammar matching key, so "fear"
  in Plutchik resolves to "fear" in NVC resolves to "fear" under the constructionist
  lens. Chosen deliberately: in this repo family, picking this key wrong fails silently.

## Repo layout

| Path | What it is |
|---|---|
| `schools/` | The content. One folder per school, each with a `grammar.json`. |
| `schools/_collection.json` | Manifest: branches and their member schools. |
| `schools/_eco_ids.json` | Slug → recursive.eco grammar UUID map. Powers the AI assistant's grounding. |
| `viewers/` | Renderers — cards, tree (the meta-grammar viewer), explorer, timeline, caster. |
| `pages/` | Site pages. |
| `_seeds/` | Local working copies of source material (gitignored; see `_seeds/README.md`). |
| `docs/` | Mechanism docs inherited from the chassis, plus the build plan. |

## Provenance

The chassis is copied from [`recursive-tarot`](https://github.com/PlayfulProcess/recursive-tarot)
per that repo's own `docs/REPLICATE-THE-PATTERN.md` — copy the working files, change only
data paths, branding, accent color, and content; never restructure. All viewers, the
assistant integration, the meta-grammar system, and the validation workflows are that
repo's, unmodified.

## License

Code MIT (`LICENSE`) · Content CC-BY-SA-4.0 (`LICENSE-CONTENT.txt`).

Grammars are original synthesis. Where a school's source material is in copyright
(Rosenberg, Johnson, Brown, Linehan), category definitions are paraphrased and the
source credited in `_grammar_commons.attribution` — no text is copied from copyrighted
works. Public-domain foundations (Darwin 1872, James 1890) are used directly.

Drafted with Claude, reviewed by the maintainer.
