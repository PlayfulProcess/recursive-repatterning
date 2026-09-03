# PLAN — Practices ↔ recursive.eco integration

Status: PROPOSED 2026-09-03 (builder's direction after the Living Into Values
launch). Companion to PLAN-values-compass.md and, on the eco side,
docs/future_plan/PLAN-emergence-view.md.

## The direction

Practices on this site should stop being islands: they can (1) hand what the
user wrote to the recursive.eco assistant for a real conversation, (2) save
their results as grammars, and (3) lean on /emerge for structure-editing —
while the site keeps its soul (light, quiet, no forced AI).

## 1. The assistant on every page — DONE (Sep 3)

The AI-free promise is retired (builder's call, Sep 3: "let's not claim no
AI anymore"). `assistant.js` now loads on the tool pages too (NVC journaling
+ Living Into Values); copy rewritten — the privacy claim that survives is
the true one: nothing you type reaches the assistant unless you bring it
there. The "Talk this through" handoff button (§2) remains the next build:
presence is done, context-passing is not. Mobile launcher clipping: the
visualViewport fix lives on eco branch `claude/ai-101-course`; prod
`recursive.eco/js/assistant-launcher.js` updates AT MERGE — until then the
builder's phone will still show the old launcher.

## 2. Tool → assistant handoff (the NVC upgrade, generalized)

Pattern for ANY practice (NVC first, Values second):
- The tool serializes its state (NVC's four columns; Values' tree + answers)
  into a compact prompt context.
- The "talk it through" button injects the launcher, opens the sidebar, and
  passes that context the same way course pages pass grammar grounding (the
  launcher's init contract / `?src=` mechanism — exact wiring decided at
  build by reading assistant-launcher.js's option surface).
- The assistant then converses WITH the user's actual material — signed-in
  users get their wallet/model options; signed-out get the sign-in nudge.

## 3. Inputs saved as grammars

- Today (shipped): Living Into Values exports **grammar-shaped JSON**
  (items + composite_of + answers-as-sections).
- Next: a "Save to recursive.eco" button for signed-in users (the
  `.recursive.eco` cookie carries) that creates a PRIVATE grammar via the
  flow API — then "Open in /emerge" and "Open in Play" links. NVC gets the
  same: a session becomes a small private grammar (one item per column, or
  per round).
- /emerge is the structure editor for all of it; the assistant (with its
  existing grammar tools) covers bulk operations — bulk delete/retag lives
  THERE, not re-implemented per tool.

## 4. Values enrichment — traditions as PRE-WOVEN TREES (builder's design)

Verdict: **not too much — and the builder's refinement makes it better than
color-coding.** A tradition's real content is not its word-list but its
GROUPING — so a cultural pack ships as a **pre-woven `composite_of` tree**:
the tradition's own categories arrive as emergent items already holding
their members. The practice then becomes a dialogue with the tradition —
adopt a group whole, dissolve it, rename its emergent, re-weave its members
into your own tree. The grouping IS the cultural layer.

- **First pack: NVC needs** — the inventory AND its canonical groupings
  (connection, honesty, play, peace, autonomy, meaning, physical
  well-being…) already live in THIS repo at `schools/nvc-needs/grammar.json`
  (the NVC journaling tool reads them live). Generating the pack = a script
  mapping that school's items+categories into a template grammar where each
  category is an emergent item. No improvised content.
- **/emerge follow-ups this implies**: (a) harvest mode learns groups —
  "keep/discard the whole group" chips, not just loose leaves; (b) a
  grouping TOGGLE: view the tree with a pack's grouping applied vs
  flattened, so you can compare the tradition's cut with your own.
- Later packs (Stoic virtues, Ubuntu, pāramitās…) follow the same
  pre-woven-tree shape, each sourced and attributed per the repo creed (its
  own voice, no totalizing claims, paraphrase in-copyright sources) —
  research gates each pack.
- V0 stays the Brown-inspired flat list; packs are separate templates.
- Optional cosmetics: rows tinted by `category` — nice-to-have after the
  structural layer, not instead of it.

## 5. Collective weaving + repatterning-native viewing (builder, Sep 3)

- **Invite people into HER grammar, not only a V0 fork.** The eco community
  flow already covers it: publish her values grammar with
  `open_to_community: true` — anyone signed in self-adds as Editor and
  proposes edits, she reviews and merges; forks remain for people who want a
  private practice. Like spreads, the WEAVING itself becomes a collective
  artifact. Zero new code; her publish call.
- **Repatterning-native item detail:** practice entries should open inside
  this site's own viewer chassis (the way the tarot repo opens cards) —
  needs the values/needs grammars public, then it's the existing
  `?src=`/viewer pattern. Follow-up build.
- **Editing FROM repatterning:** if cross-site editing proves heavy, ship a
  "How to edit this" guide/course instead (open in eco's Emerge/Play, or ask
  the assistant) — the eco fork/collaboration flow does the real work.

## 6. Sequencing

- **I1 (small):** "Talk this through" button on Living Into Values +
  NVC — injects launcher + passes context. 1 session, MEDIUM-HIGH
  (launcher option surface is the unknown).
- **I2:** "Save to recursive.eco" on both tools (cookie-authed create).
  1 session, MEDIUM until the create endpoint's CORS/auth posture is
  verified.
- **I3:** category color-coding in /emerge + first sourced tradition pack.
  1–2 sessions (research gates the pack, not the code).
