# CLAUDE.md — recursive-repatterning

## The spine: the substrate and its interfaces

1. **The creed is the spine.** This project turns on one claim: *there are no fixed
   biological fingerprints for emotions, and we still have to make meaning — so every
   school here is a working interface, not a discovery.* The constructionist account
   (Barrett) is the **substrate**, not a peer school. Everything else — Plutchik, NVC,
   DBT, attachment, Jung — sits on top of it as a usable map. **A map being constructed
   is not the same as a map being wrong.**
2. **Let each school speak as itself.** Under that container, present each tradition
   *faithfully, in its own terms* — an NVC section should sound like NVC, not like us
   editorializing about it. Render any *disagreement* with a school in the long form
   (its course or a clearly-marked `Research note`), never inside the school's own
   sections. The hard floor everywhere: stay autonomy-preserving — never state a
   feeling-label as a diagnosis or as something to obey.
3. **Name a school, not a living person.** Schools drawn from a living teacher are
   titled by their tradition (NVC, DBT, EFT, Constructed Emotion) and say "inspired by"
   or "after". Only dead, eponymous figures (Darwin, James, Jung) carry their own name.
4. **Consolidate, don't multiply.** Prefer turning a new idea into something we already
   have — a **school** (`schools/<slug>/`), a **voice** (`viewers/voices.json`), or a
   **course** — over a parallel structure.
5. **"EFT" is two different frameworks.** Sue Johnson's *Emotionally* Focused Therapy
   (couples, attachment) and Leslie Greenberg's *Emotion*-Focused Therapy (individual,
   experiential) are different people and different models. Always disambiguate.

## Honesty by construction — two required metadata conventions

- **`metadata.evidence_tier`** on every school-level item — one of
  `independently-replicated` / `growing` / `observational-only` / `theoretical`, plus an
  `evidence_note`. Johnson's EFT and Gottman's method do **not** have equivalent evidence
  bases; the library must say so rather than issue both an undifferentiated
  "evidence-based" badge. This is the whole point of the project — do not skip it.
- **`metadata.emotion_key`** on every emotion-level item — the cross-grammar matching key
  (lowercase, singular: `fear`, `shame`, `contempt`). This is the equivalent of tarot's
  "trump key" and astrology's "entity name". **Picking this wrong fails silently** — see
  `docs/REPLICATE-THE-PATTERN.md`.

## Theme & colour — ONE source (`theme.css`)

- **All colour lives in `theme.css`** (a single `:root` of tokens), linked by every page
  and viewer. **Never redeclare colour tokens locally** and never add a
  `@media(prefers-color-scheme:dark)` block — that's what caused recurring light-on-light
  bugs in the parent repo (each page had its own divergent palette).
- **Light only.** Backgrounds always light, text always dark enough to read on them.
  Legacy aliases resolve: `--panel`=`--surface`, `--muted`=`--mut`, `--accent`=`--gold`,
  `--ink-strong`/`--fg`/`--text`=`--ink`.
- To re-apply consolidation if a new file drifts: `python scripts/apply_theme.py`.
- **Bump `?v=N` whenever a shared asset changes** — `theme.css?v=N`, `style.css?v=N`,
  `site-header.js?v=N`. Forgetting is a known recurring bug class in this repo family.

## Core architecture

- Grammar files live in `schools/<slug>/grammar.json`. Never hand-edit
  `schools/all-schools-many-lenses/grammar.json` — it is generated.
- Always run `python scripts/check_all.py` before committing. Must end "all checks
  passed" with `dangling=0`.
- After any grammar edit: `python scripts/build_meta_grammar.py`, then check_all again.
- **ONE branch: `main`.** Site, app-sync and Pages all live there.
  - **GitHub Pages serves `main` in deploy-from-branch mode** (`build_type: "legacy"`,
    `source: {branch: "main", path: "/"}`). GitHub publishes the branch itself on every
    push; there is **no** Pages deploy job in Actions, and `actions/deploy-pages` would
    fail against a legacy-configured site. Root **`.nojekyll` must stay** — it's what
    stops Pages running Jekyll over the site.
  - `.github/workflows/build-meta.yml` only rebuilds and commits the meta-grammar.
    **Never re-add `pages: write` / `deploy-pages` to it** unless Pages is first switched
    to `build_type: "workflow"`. (A past incident in the parent repo: a stale branch's
    copy of this workflow fought main's Pages publish and won intermittently.)
  - CI lands `chore: rebuild meta-grammar [skip ci]` commits on `main`; always
    `git pull --rebase` before pushing.

## The AI assistant — how it is actually wired

`assistant.js` injects `https://recursive.eco/js/assistant-launcher.js`, which iframes
`flow.recursive.eco/assistant`. **Auth is cookie-based and inherited from the
`.recursive.eco` parent domain** — it only works when this site is served from a
`*.recursive.eco` subdomain. A bare `github.io` URL will **not** authenticate.

Grounding: it parses `?src=../schools/<slug>/grammar.json` off the page URL and resolves
the slug to a grammar UUID via `schools/_eco_ids.json`. Both that file and
`schools/_collection.json` must exist at those paths even when empty — several files
`fetch()` them unconditionally.

## The one cross-link pattern (DO NOT INVENT ANOTHER)

The viewer renders a pill link automatically when an item has:
```json
{
  "metadata": {
    "source_deck": "<slug>",
    "source_item_id": "<item-id>",
    "deck": "<human label>"
  }
}
```
The pill reads: **"Open in [label] →"**. This is the ONLY cross-grammar navigation
mechanism in this chassis. Use it for everything — constellation → school, school →
related school. **Never add a new link field.**

> Note: `GRAMMAR_FORMAT.md` also documents an `item_type: "reference"` /
> `ref_document_id` mechanism. It is **not used anywhere in this repo family** and is
> effectively untested. Use `source_deck`/`source_item_id` — it is the path that works.

The pill suppresses itself if the current page URL already contains `/<slug>/`, so it
never shows a circular link.

## Cross-grammar embeds — always framed

An item carrying the cross-link above also gets the OTHER grammar's content resolved into
its detail view (`viewers/reference-resolve.js`). That embed is **always framed** — a
bounded, collapsed `<details>` box that names the relationship and says whose content it
is. Never render resolved content in the host's own section markup. The one exception is
the aggregator (meta) grammar — its items are pointer stubs, so there the box opens
expanded. `RefResolve.renderEmbed()` is the single implementation for `cards.html`,
`tree-viewer.html` and `caster-studio.html`; change it there, not per viewer.

## Sections used across grammars

| Section | Meaning |
|---------|---------|
| `Definition` | What this school means by this term, in its own words |
| `In the body` | Interoceptive/somatic notes where the school makes them |
| `Where it shows up` | Cross-school appearances of the same `emotion_key` |
| `Research note` | Sourced claims with `[@citation]` keys — **the repo's own voice**, exempt from the one-source rule |
| `Constructionist lens` | The substrate reading of this item — clearly marked as our editorial layer, never presented as the school's own claim |
| `Practice` | What a person actually does with this |

## Copyright

Public-domain foundations (Darwin 1872, James 1890) can be used directly. Where a school's
source is in copyright — **Rosenberg (NVC), Johnson (EFT), Brown (Atlas of the Heart),
Linehan (DBT)** — paraphrase category definitions and write entirely original prose. Never
quote passages. Credit the source in `_grammar_commons.attribution` with explicit "no text
is copied from copyrighted works" language, following the pattern in the existing
`relationship-cards` grammar.

**One source per grammar:** a grammar carries one school's voice. A second author's take
on the same subject becomes a *separate* grammar, cross-linked — never stacked into the
same item.

## Privacy

**No real personal names anywhere** — not in content, commits, attribution, or docs.
Attribution is **PlayfulProcess** only. Git commits must use the PlayfulProcess noreply
identity; set `user.email` locally per-repo (GitHub blocks pushes that would expose a
private email).

## Scripts cheat-sheet

| Script | What it does |
|--------|-------------|
| `scripts/build_meta_grammar.py` | Rebuild the constellation meta-grammar |
| `scripts/refresh_collection.py` | Sync `_collection.json` from grammars |
| `scripts/check_all.py` | Pre-commit gate |
| `scripts/apply_theme.py` | Re-consolidate colour onto `theme.css` |
| `scripts/one_source_per_deck.py` | Strip over-repeated per-item attribution |
| `scripts/validate-grammar.mjs` | CI grammar validation (also runs as a PR gate) |
