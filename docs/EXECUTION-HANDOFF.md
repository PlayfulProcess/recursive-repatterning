# Execution handoff — the synthesis pass

**What this is:** the complete, self-contained work order for finishing the current arc.
Written so that any session — any model, no prior chat context — can pick it up: read
`CLAUDE.md` first (every rule binds), then this file, then check the task table against the
git log and the working tree before doing anything.

**Prime rules digest** (full versions in `CLAUDE.md` — read it, this is only a reminder):
verbatim prose for the maintainer's own writing; no totalising claims; public copy never
narrates process; `evidence_tier` honest, per the two-warrants note on `overflow-root`;
emotion_key stays transliterated where English glosses would erase; ONE cross-link mechanism
(`metadata.source_deck`/`source_item_id`/`deck`); bump `?v=N` on shared assets everywhere;
after grammar changes run `python scripts/build_meta_grammar.py` then commit BOTH the
aggregator and `_collection.json`; always `git pull --rebase` before push (CI lands
`[skip ci]` commits).

---

## Task table

| # | Task | Status at writing | Owner |
|---|---|---|---|
| 1 | Course: Relationship is Process | DONE (de77ec4) | — |
| 2 | School: untranslatables | DONE (01c209d) | — |
| 3 | Skeleton completion pass | DONE (c956470) — 3 residual stale Research-note sentences flagged in its report (timor, eleos, bei) need a copy-edit | next session |
| 4 | Tools index page (practices Phase 2) | DONE (2e9d3e7) | — |
| 5 | Integration: wire 1–4, rebuild, verify live | DONE — untranslatables in new branch language-and-translation | — |
| 6 | Overflow cross-links through the library | **not started** — spec §A | next session |
| 7 | The Spiral view | **not started** — spec §B | next session |
| 8 | Love Bank port (practices Phase 3) | not started — see `docs/PLAN-practices-layer.md` | later |
| 9 | Channel-time dedup | blocked on channel import — see `docs/PLAN-overflow-and-the-living-library.md` §8 | later |

**Task 5 — integration checklist** (do this first if agents 1–4 have finished):
1. `git status` / `git log --oneline -10` — see what landed and what is uncommitted.
2. Validate every grammar: parse + dangling `composite_of` + cross-link resolution (the
   one-liner lives in previous commit messages; or:
   `python -c "import json,glob;[json.load(open(f,encoding='utf-8')) for f in glob.glob('schools/*/grammar.json')];print('parse ok')"`).
3. Wire new schools into `schools/_collection.json` branches: `untranslatables` needs a
   branch decision — recommended: a new branch `language-and-translation` ("what carries
   between languages, and what does not — evidence from a 400,000-word model's gaps"),
   placed after `the-house-school`. Do NOT put it in historical-scientific.
4. `python scripts/build_meta_grammar.py`; commit aggregator + `_collection.json` together.
5. Course wiring if agent 1 didn't finish it: `course/_courses.json` entry, `COURSE_GROUPS`
   in `site-header.js` (bump `?v=` everywhere — currently v=51), `pages/courses.html` card.
6. Push, wait for Pages, verify live: every new endpoint 200, dropdown counts right,
   courses render, tools page renders.

---

## §A — Spec: Overflow cross-links through the library (task 6)

The house school becomes the library's connective tissue. Add cross-links FROM overflow
cards TO the schools that hold the same concept — using the one sanctioned mechanism, and
**verifying every target id by reading the target file first**. Candidate map (verify, don't
trust):

| Overflow card | Target school / item | The shared concept |
|---|---|---|
| the-body | constructed-emotion / interoception | body budget, allostasis |
| the-heap | dbt-skills / radical-acceptance | error composted, not fought |
| the-ledger | nvc-needs (root) | moral arithmetic vs. needs-language |
| the-modulation | eft-bonds / pursue-withdraw-cycle | constructing the shared environment |
| the-ceding | nvc-needs (requests territory) OR parts-work / self | making room as a move |
| the-recognition | jungian-archetypes (individuation) + rasa / shanta | knowing-again |
| the-constriction | acting-traditions (kata/constraint) | constraint as equipment of play |
| the-two-truths | attachment-theory (secure base ↔ exploration) | part and self held together |

Rules: only link where the connection is REAL on reading both items — drop any row that
feels forced (the library's precedent: dbt-skills considered a jung link and dropped it).
Each link is one-directional from overflow unless the target item genuinely gains from the
back-link. 6–10 good links beat 16 plausible ones. After: rebuild aggregator, validate,
commit with reasoning per link in the message.

## §B — Spec: the Spiral view (task 7) — `viewers/spiral.html`

**What it is:** the dynamic half of the mechanistic-interpretability instinct. The proximity
view shows the corpus's priors (static geometry); the spiral shows the person's own process
(casts over time). Release and reintroduction made visible.

**Data:** localStorage only (`repatterning:casts`, a JSON array). No server, no auth, no
tracking — same privacy stance as the NVC tool ("nothing saved" becomes "saved only in your
browser"; say so on the page). Each stored cast: `{ts, spread:'overflow-spread',
positions:[{position:'Structure'|'Process'|'Possibility', card_id, card_name}],
released:[card_id...], note?:string}`.

**Where casts come from:** caster-studio already casts the Overflow Spread (it is in
`viewers/spreads.json`). Add a small "Save to my spiral" button to caster-studio's result
footer — data write only, no mechanism change, mirror how its existing buttons are built.
If touching caster-studio proves risky, fallback: spiral.html offers "record a cast by
hand" (three dropdowns fed from `schools/overflow/grammar.json`) — uglier but zero-risk,
ship that first.

**Render (D3 v7, already used by two viewers — copy their zoom/pan patterns):**
- Archimedean spiral, one turn per cast, oldest at centre. Each turn shows its three
  position-dots (Structure/Process/Possibility) with card names on hover/zoom.
- **The recursion rule drawn, not explained:** a dashed arc connects each turn's
  Possibility dot to the NEXT turn's Structure dot. That arc IS the thesis.
- **Release = the Heap:** a released card greys and drops slightly inward toward a small
  compost pile at centre ("The Heap" — the deck's own card). Never deleted; the record
  stays load-bearing. A "release" button on each past card.
- Clicking any card opens its detail: sections from the overflow grammar, plus a "see its
  neighbourhood" link to `proximity.html?q=<term>` where the term exists there.
- Empty state: explain the practice in the deck's own voice (quote The Spread card's body
  verbatim), link to caster-studio to make a first cast.
- Page caption states plainly: this is your record, held only in this browser; export =
  copy JSON to clipboard; import = paste. (No accounts. Clearing browser data clears it —
  say so.)
- Add to `GRAMMAR_VIEWS` in site-header.js as 'Spiral' (bump `?v=`), theme.css tokens only,
  light-only, no dark block. Verify at 390px.

**What NOT to do:** no interpretation engine, no "insights", no scoring. The person does
the interpreting; the view only externalises the sequence. That restraint is the point.

## §C — Notes for whoever runs this

- Agents in this repo have repeatedly found that Wikimedia/museum CDNs throttle rapid
  checks — never declare an external URL broken on one failed attempt.
- The app-side twins of overflow/ethics-of-fiction are live previews until channel time;
  do not edit them app-side (see the dedup item).
- `_seeds/live/` holds fetched app grammars; `_seeds/` is gitignored except its README.
- If a background agent died mid-task (session caps kill them), its directory may exist
  empty or partial — check before assuming done, delete partials, re-run its task from
  this doc's specs.
