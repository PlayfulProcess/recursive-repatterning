# Build plan

Supersedes the v1 "Repatterning Grammars" design doc. The key reframing: **this is an
assembly job, not a from-scratch authoring project.** Roughly 240 authored items across
eight emotion/psychology grammars already exist in `recursive.eco-schemas`; only three
schools are genuinely missing.

## Decisions locked

| Decision | Choice |
|---|---|
| Repo name | `recursive-repatterning` |
| Architecture | **Constellation** — one grammar per school, composited by a meta-grammar. Not one mega-grammar with schools as L3 items. |
| Barrett placement | **Substrate, not a peer school.** The frame the whole library sits inside. Lives in the constellation root's own commentary and in `viewers/voices.json` → `shared_intention`. |
| Register (kids vs adult) | **Hybrid.** Adopt the unused adult-toned Plutchik draft; keep `dbt-wise-heart` as a clearly-labeled "for children" branch. |
| `grammar_type` | Not load-bearing — chosen per grammar for whichever recursive.eco features that grammar should light up (casting, courses, sequences). The casting mechanism is **wanted**, not stripped. |
| Cross-grammar links | `metadata.source_deck` / `source_item_id` / `deck`. **Not** `item_type: "reference"` — see CLAUDE.md. |

## Status

### Done — chassis
- Copied from `recursive-tarot` per `docs/REPLICATE-THE-PATTERN.md` (copy the working
  files; change only data paths, branding, accent, content; never restructure).
- Excluded at copy time: `.git`, `print/` (422MB of gitignored build artifacts),
  `_private/`, `research/`, `_research/`, `env-local.txt`, `CNAME`. **No credentials or
  personal notes were ever copied.**
- Stripped: tarot games/book pages, tarot `.mdx` courses, tarot history docs, roadmap
  and changelog docs, ~22 one-shot tarot data-builder scripts.
- **Kept deliberately:** the casting chassis (`caster-studio.html`, `caster.html`,
  `spreads.json`, `spread-builder.html`), all viewers, `assistant.js`, the meta-grammar
  tree viewer, both CI workflows, `.nojekyll`.
- Renamed the data folder `tarot/` → `schools/` across 107 references in 34 files, using
  a negative lookbehind so the `recursive-tarot` GitHub URLs in the workflows survived
  intact. Verified: zero stray `tarot/` path refs remain.
- Seeded `schools/_collection.json` with the seven constellation branches, and
  `schools/_eco_ids.json` as an empty map. Both must exist even when empty — several
  files `fetch()` them unconditionally.

### Not done yet
- [ ] **Provision `repatterning.recursive.eco`** and add a `CNAME`. Until then the AI
      assistant will not authenticate — its session cookie is inherited from the
      `.recursive.eco` parent domain, so a `github.io` URL cannot work.
- [ ] Confirm GitHub Pages is set to deploy-from-branch on `main` at repo root
      (`gh api repos/PlayfulProcess/recursive-repatterning/pages`).
- [ ] Swap the accent colour family in `theme.css` (tarot=gold, astro=sky-blue; this repo
      needs its own). Bump `theme.css?v=`.
- [ ] Edit the nav arrays in `site-header.js` (mechanism untouched, data only). Bump
      `site-header.js?v=`.
- [ ] Rewrite `viewers/voices.json` — keep the shape, replace every string. This is where
      the substrate creed lives.
- [ ] Rewrite the remaining page copy in `pages/*.html` and `index.html` (shells are
      chassis; the prose is tarot's).
- [ ] Rewrite `viewers/spreads.json` for repatterning draws. The existing
      `relationship-cards` "Pattern → Need → Move" spread is the model.

## Next: content

**Assemble (mostly mechanical).** Bring the eight existing grammars into `schools/`,
assign `emotion_key` and `evidence_tier` metadata, wire the constellation. Strip the
`[SESSION-N:]` build tags still present in all 298 sections of `relationship-cards`.

**Author (the real work) — only two schools for v1:**
1. **NVC / Rosenberg.** Feelings as signals of met/unmet needs. Note in the grammar that
   there is no single canonical CNVC list — trainers publish variants — rather than
   picking one silently. Also worth stating: NVC's hard split between "real feelings" and
   "pseudo-feelings" doesn't survive the constructionist substrate cleanly; that tension
   belongs in a `Constructionist lens` section, not hidden.
2. **Constructed Emotion / Barrett.** Adapt from `_seeds/prose/interoception-to-emotion-pipeline.md`.
   Written as the substrate, not as a peer entry.

**Deferred past v1:** Atlas of the Heart (copyright care), Ekman, the family-therapy
superset build-out (`_seeds/plans/family-therapy-grammar-plan.md` has the full ~120–160
item taxonomy ready), society-scale values grammar, illustration pipeline.

## Re-populating `_seeds/`

The seed working copies are gitignored. To restore them, copy from:

| Into | From |
|---|---|
| `_seeds/grammars/<slug>.json` | `recursive.eco-schemas/grammars/<slug>/grammar.json` |
| `_seeds/grammars/plutchik-ADULT-DRAFT.json` | `recursive.eco-schemas/schemas/tarot/plutchik-wheel-emotions.json` |
| `_seeds/plans/` | `recursive.eco-schemas/plan/` |
| `_seeds/prose/` | `emergence-lab/docs/` and `tarot-as-myth/research/tarot-self-knowledge/` |

See `_seeds/README.md` for the full index, known issues, and what was deliberately left
out on privacy grounds.
