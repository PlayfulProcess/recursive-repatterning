# PLAN — Values Compass (a practices-layer tool)

Status: PROPOSED 2026-09-02, awaiting the builder's green light.
Lives with the other practices (sibling of `tools/nvc-journaling.html`).

## What it is

A guided values-clarification practice, inspired by Brené Brown's "Living
Into Our Values" exercise from *Dare to Lead* (attributed on-page; all
question text paraphrased, with a link to the official worksheet — we never
reproduce her worksheet's prose or layout). Where the paper version picks two
values and fills in blanks, this tool treats values the recursive way: many
values are harvested, ordered, and **grouped until higher values emerge from
clusters of lower ones** — and the result renders as a living tree the
builder (or any visitor) can keep editing.

## The flow (one page, four stages, freely revisitable)

1. **Harvest** — the classic value words as tappable chips (they are common
   single words; the curated set is attributed), plus "write your own". Pick
   everything that resonates — no two-value limit at this stage.
2. **Sort** — drag to reorder what was picked; the order IS data (ranking).
3. **Group** — drag values into clusters and NAME each cluster. A cluster's
   name is itself a value — the emergent, higher-level one. Nesting allowed.
   This is where the tree grows itself.
4. **Deepen** — for the core values (top of the tree), answer the reflection
   prompts (paraphrased): behaviors that express it, slippery behaviors that
   betray it, a story of fully living it; plus the one-time support prompts
   (who supports you, what support looks like, self-compassion, early warning
   signs, how it feels, how to check yourself).

**Views:** ranked list · grouped clusters · tree (inline SVG) · print.
Everything editable at any time; the practice is meant to be revisited.

## Storage (the recursive part)

- **Local first:** autosaves to localStorage; Export/Import JSON buttons.
  Private by default — answers never leave the browser; say so on the page.
- **Save to recursive.eco as a grammar (signed in):** the site is a
  `.recursive.eco` subdomain, so the flow auth cookie carries (same pattern
  as the course assistant calling flow's chat API with credentials). Each
  value = one item (name; category = its cluster; sections = the answers;
  item order = ranking). Grammar storage buys, for free: the platform's tree
  and card viewers, versioned grammar-vault backups, and — later — the
  unified assistant editing it with its existing grammar tools ("help me
  regroup these", "reflect this story back to me").
  Exact write path (flow grammar API vs export→import) decided at build after
  a quick check of which endpoint accepts cross-subdomain authed writes.

## Header change (same session, builder's call)

Remove the current **Play** dropdown (the draw/cast hub at `pages/play.html`)
from the site header, and rename **Practices → Play**, pointing at
`tools/index.html`. Bump the `site-header.js?v=` version everywhere it is
referenced (the known stale-header gotcha). The old play.html page itself can
stay reachable or be tombstoned — builder's call at build time.

## Phasing

- **Phase 1 (1–2 sessions, HIGH confidence):** the four-stage tool with
  list/cluster/tree views, localStorage autosave, export/import, print,
  Practices→Play rename. Static page, free Pages builds, fully testable in a
  local browser.
- **Phase 2 (1 session, MEDIUM until the write path is verified):** "Save to
  recursive.eco" as a private grammar + open-in-flow links.
- **Phase 3 (small):** assistant reflection via the site's existing
  assistant hookup + grammar-editing once Phase 2 lands.

Author on all published surfaces: PlayfulProcess.
