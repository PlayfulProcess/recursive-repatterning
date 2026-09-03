# PLAN — Practices ↔ recursive.eco integration

Status: PROPOSED 2026-09-03 (builder's direction after the Living Into Values
launch). Companion to PLAN-values-compass.md and, on the eco side,
docs/future_plan/PLAN-emergence-view.md.

## The direction

Practices on this site should stop being islands: they can (1) hand what the
user wrote to the recursive.eco assistant for a real conversation, (2) save
their results as grammars, and (3) lean on /emerge for structure-editing —
while the site keeps its soul (light, quiet, no forced AI).

## 1. The assistant on every page — with the AI-free promise kept

`assistant.js` already runs on content pages; the tools deliberately omit it
("self-guided, no AI"). Resolution: the assistant becomes available on tool
pages as an **explicit invitation, not a resident** — a quiet "Talk this
through with the assistant" button at the END of a practice. Nothing loads
until tapped; the promise text changes from "no AI" to "no AI unless you ask
for it". Mobile launcher clipping: FIXED in eco's assistant-launcher.js
(visualViewport sync, Sep 2) — verify on the builder's phone after the
landing deploy; the `?v=` on the injector here is bumped to bust caches.

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

## 5. Sequencing

- **I1 (small):** "Talk this through" button on Living Into Values +
  NVC — injects launcher + passes context. 1 session, MEDIUM-HIGH
  (launcher option surface is the unknown).
- **I2:** "Save to recursive.eco" on both tools (cookie-authed create).
  1 session, MEDIUM until the create endpoint's CORS/auth posture is
  verified.
- **I3:** category color-coding in /emerge + first sourced tradition pack.
  1–2 sessions (research gates the pack, not the code).
