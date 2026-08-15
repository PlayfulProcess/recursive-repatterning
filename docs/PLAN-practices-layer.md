# Plan — bringing the wellness tools in as a practices layer

Draft for review. Nothing built yet.

---

## 1. The artifact question, answered first

**Can a Claude.ai artifact be rewired to use your database?** In the way you'd want — authenticated, per-user, persistent — **no.** The reasons are structural, not fixable with effort:

- A published artifact runs sandboxed on `claude.ai`, not on your domain. It **cannot carry your `.recursive.eco` session cookie**: that's a cross-site cookie, and browsers block those by default. Every auth mechanism this project already uses depends on that cookie.
- `window.claude.complete()` — which `ParentalLoveBankApp` calls — exists **only inside the artifact runtime**. Paste that component onto any other host and the AI features fail immediately. That single call is the whole portability problem.
- You could embed a Supabase anon key and rely on RLS. Anon keys are designed to be public, so that isn't a leak — but with no signed-in user there's no identity, so no per-user rows. You'd get a shared bucket, not a journal.

**So the arrow points the other way.** Rather than teaching an artifact to reach your database, move the tool onto your domain, where the cookie already works and where `flow.recursive.eco/api/ai/chat` is already reachable with `credentials: 'include'` — the same route `recursive-tarot`'s course assistant uses. Artifacts stay what they're good at: a fast place to prototype before porting.

## 2. What the two tools actually are

| Tool | AI? | Port difficulty | Notes |
|---|---|---|---|
| [NVC journaling](https://jongu-old.vercel.app/nvc_journaling.html) | **None** — explicitly self-guided | **Easy** | A four-column T-chart: my feelings, my needs, their feelings, their needs — plus reference lists of feelings and needs. Print or copy out. |
| Parental Love Bank (React) | Yes — `window.claude.complete()` ×4 | **Medium** | Four steps: 24-hour reflection, Love Map, AI strategies, commitment. Also React + lucide-react, so it needs either a build step or a rewrite to plain JS. |

**The important find:** the NVC tool's reference lists of feelings and needs are *the same content* as `schools/nvc-needs`. Right now they're hardcoded in a standalone page. If the tool reads them from the grammar instead, the library stops being a thing you read next to the tool and becomes the thing the tool **runs on**. That is the whole argument for bringing them in.

Similarly, the Love Bank's "Love Map" is Gottman's own term, and its bids/deposits framing is Gottman's — so it practises `gottman-method`, with a foot in `attachment-theory`.

## 3. Proposed shape

A third content type beside schools and courses:

```
tools/
  _tools.json          manifest
  nvc-journaling.html  self-contained page
  love-bank.html
```

Each manifest entry declares which schools the tool practises:

```jsonc
{
  "id": "nvc-journaling",
  "title": "NVC Journaling",
  "blurb": "Four columns: what I feel and need, what I imagine you feel and need.",
  "schools": ["nvc-needs"],          // reads its lists from these grammars
  "needs_ai": false,
  "needs_auth": false
}
```

**Why the relation lives in the manifest and not in the grammars:** `CLAUDE.md` is explicit that `source_deck`/`source_item_id`/`deck` is the only cross-grammar link and that no new link field may be invented. That mechanism is grammar→grammar. A grammar→tool pointer would be a new field. Keeping the relation in `_tools.json` gives the same result — a school page can list its practices by reverse lookup — without touching the grammar contract. One place to edit, nothing scattered.

### What "wired to a school" should mean concretely
Not decoration. Three real behaviours, in increasing order of effort:

1. **The tool reads the school.** NVC journaling fetches `schools/nvc-needs/grammar.json` and builds its feelings/needs pickers from the actual items. Add a feeling to the grammar, it appears in the tool. This is the one that proves the idea.
2. **The school lists its practices.** A school page shows "Practices drawing on this school →", by reverse lookup over `_tools.json`.
3. **A draw hands off to a tool.** After casting from `across-the-schools`, offer "journal on this" — passing the drawn item into the tool as a starting prompt. This is the "as if it were the oracles" part, and it's the piece that makes the library and the practices one system rather than two tabs.

## 4. Sequencing

**Phase 1 — port NVC journaling.** No AI, no auth, self-contained. Add the `tools/` scaffold and manifest alongside it. Make it read its lists from `nvc-needs` (behaviour 1). Smallest change that proves the whole design.

**Phase 2 — surface tools on the site.** A tools index page, the Practices section on school pages (behaviour 2), and a nav entry.

**Phase 3 — port Love Bank.** Rewrite `window.claude.complete()` → `fetch('https://flow.recursive.eco/api/ai/chat', {credentials:'include'})`, matching how `assistant.js` and the tarot course assistant already authenticate. Decide React-with-build vs. plain-JS rewrite; **plain JS is recommended** — every other page here is dependency-free and self-contained, and adding a build step for one page would break that.

**Phase 4 — draw → practice handoff** (behaviour 3).

## 5. Open questions

1. **Where does written work go?** Both tools currently persist nothing — print or copy to clipboard. Options: keep it that way (privacy by construction, and the NVC tool advertises "your responses are private"); localStorage; or real per-user storage via the flow API. The last needs sign-in and changes the tools' privacy claim, so it is a product decision, not a technical one.
2. **Are tools part of the channel?** `recursive-eco.json` currently declares only grammars. Should tools be importable to recursive.eco too, or stay site-only?
3. **Licensing.** Tool code would be MIT like the rest of the code here; their *content* (prompts, reference lists) is CC-BY-SA. Worth stating in `docs/SOURCES-AND-CAVEATS.md` once tools exist.
4. **Which other wellness-channel tools exist?** This plan covers the two seen so far. An inventory of the rest would change the phasing.

## 6. Recommendation

Do Phase 1 only, then look at it. Porting one AI-free tool and having it read a real grammar answers the question the whole idea rests on — *does the library make the tools better?* — at a fraction of the cost of porting everything. If the NVC pickers built from `nvc-needs` feel better than the hardcoded lists, the rest is worth building. If they don't, we have learned that cheaply.
