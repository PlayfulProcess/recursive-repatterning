# Plan — multi-party spreads, and tools that talk to the assistant

Draft for review. Extends `docs/PLAN-practices-layer.md`. Nothing built yet.

---

## 1. The assistant question is already answered — the contract exists and this side is shipped

There is no need to design a way for tools to reach the assistant. `docs/ASSISTANT-EMBED-CONTRACT.md`
specifies it, and **the host side is already implemented** in `viewers/caster-studio.html`. It does
precisely what you described: rather than navigating away to the flow app, it opens the embedded
assistant sidebar and hands it the reading in place.

```js
window.RecursiveAssistant.open();                       // grows the pinned sidebar
const iframe = document.querySelector('.rec-assistant-shell iframe');
const targetOrigin = new URL(iframe.src).origin;        // derived, never hardcoded, never '*'
iframe.contentWindow.postMessage({
  type: 'recursive:interpret-reading',
  reading: { /* ReadingV1 */ },
}, targetOrigin);
```

**So the rule for every tool in this repo: emit `recursive:interpret-reading`. Never call a second
AI.** A tool that does its own model call would bypass the wallet, the session, and the grounding —
and would be a different assistant with a different voice, which is the thing you don't want.

### Two things that must be fixed for this to work here

1. **This repo is not on the embed's origin allow-list.** The contract tells the flow side to
   allow-list the family — it names `tarot.recursive.eco`, `astro.recursive.eco`, their `dev.`
   counterparts and `localhost`. **`repatterning.recursive.eco` is not in that list.** When the flow
   side ships the listener, it will silently reject everything from this site. This needs adding to
   the flow-side allow-list, and it is a one-line change made now rather than a confusing debug later.
2. **The flow side still has not implemented the listener** (unimplemented as of the contract's last
   status note). Until it does, the host's ~1s ack timeout fires and falls back. So tools should be
   built to emit the message *and degrade gracefully* — exactly as the caster already does.

## 2. ReadingV1 already has the field your "trumps and minors" instinct is reaching for

The payload's per-position card object is:

```ts
card: {
  name: string;
  deck: string | null;
  reversed: boolean;
  arcana: string | null;   // "major" | "minor" | null
  number: number | null;
} | null
```

`arcana` is the trumps/minors distinction — **a field whose entire job is to say what kind of item
this is.** For a practices spread the same slot carries the item's type:

| `arcana` value | Meaning here |
|---|---|
| `feeling-met` | a feeling signalling a met need |
| `feeling-unmet` | a feeling signalling an unmet need |
| `need` | a need |
| `person` | an emergent person-item (see §3) |

That is the existing field used for its actual structural purpose, not a new one invented. `reversed`
has no meaning for feelings and stays `false`; `deck` carries the school slug, which is already how
the caster uses it. The contract says the embed must tolerate unknown extra fields, so anything
genuinely additional can be added without breaking it — but the type belongs in `arcana`.

## 3. People as emergent items — the good idea, and it needs no new mechanism

The NVC tool today is two people and four columns: my feelings, my needs, their feelings, their
needs. Generalising to N people is where it gets interesting, and the grammar already has the
mechanism.

**A person is a composite item.** `composite_of` is how this library builds an L2 from L1s — a
branch from its schools, a rasa group from its rasas. A person in a spread is the same move:

```jsonc
{
  "id": "person-a",
  "name": "Me",
  "category": "person",
  "composite_of": ["frustration", "need-consideration", "loneliness"],
  "metadata": { "role": "self" }
}
```

The person **emerges from** the feelings and needs placed under them — which is both the correct data
model and, not incidentally, true to the library's own thesis. A person in a conflict is not a fixed
thing with an emotion attached; they are the pattern their feelings and needs make at that moment.

**A filled spread is itself a composite** of its person-items — one more level up, same mechanism. So
a session has a natural shape: feelings and needs (L1) → people (L2) → the situation (L3). That is
the identical shape as items → groups → root everywhere else in this repo, which means the tree
viewer can already render it.

### What this unlocks beyond NVC
The same structure fits two schools already in the library:
- **`eft-bonds`** — its `pursue-withdraw-cycle` item *is* a two-person spread: each partner's
  secondary (protective) emotion sitting on top of a primary (vulnerable) one, each triggering the
  other. A spread with two person-items and a primary/secondary layer per person maps it directly.
- **`gottman-method`** — bids, turning toward, and repair attempts are moves *between* person-items.

So this is not an NVC feature. It is the interpersonal layer the library has been missing, and NVC
is simply the cheapest place to prove it.

## 4. Spread definitions

`viewers/spreads.json` already exists — the caster's layout definitions, currently tarot spreads.
Practice spreads belong in the same file or a sibling, with typed positions:

```jsonc
{
  "id": "nvc-two-party",
  "name": "What I feel and need, what I imagine you do",
  "positions": [
    { "n": 1, "label": "My feelings",     "accepts": "feeling-met|feeling-unmet", "person": "self" },
    { "n": 2, "label": "My needs",        "accepts": "need",                      "person": "self" },
    { "n": 3, "label": "Their feelings",  "accepts": "feeling-met|feeling-unmet", "person": "other" },
    { "n": 4, "label": "Their needs",     "accepts": "need",                      "person": "other" }
  ]
}
```

`accepts` is what makes a position typed, and `person` is what lets positions group into person-items.
An N-party spread is then just more positions with more `person` values — the four-column tool is the
two-party case, not a special one.

**One honest caution.** In a tarot spread the cards are *drawn* — chance supplies them. Here the user
*chooses* their feelings and needs, and calling that a "cast" would misdescribe it. Same layout
machinery, different act: **a spread you fill, not a spread you draw.** Worth keeping the language
distinct in the UI, because the whole library is careful about not implying a reading tells you
something you didn't bring.

## 5. Sequencing

1. **NVC tool reads the grammar** — already in flight (`docs/PLAN-practices-layer.md` Phase 1).
2. **Add the `recursive:interpret-reading` emit** to the NVC tool, with the `arcana`-carries-type
   mapping from §2 and the same graceful fallback the caster uses. Ships useful even while the flow
   side is unimplemented, because the fallback path is the current behaviour.
3. **Get `repatterning.recursive.eco` onto the flow-side allow-list** (§1). Do this early — it's
   trivial and invisible until it bites.
4. **Typed spread definitions** (§4), starting with `nvc-two-party` as a formalisation of the existing
   four columns.
5. **N-party spreads and person-items** (§3), once the two-party case works.
6. **Map `eft-bonds`'s pursue-withdraw cycle as a spread** — the payoff, and the point at which the
   practices layer is clearly not just an NVC feature.

## 6. Open questions

1. Do filled spreads persist? Same unresolved question as `docs/PLAN-practices-layer.md` §5 — and it
   matters more here, since a multi-party map is more work to rebuild than four text boxes.
2. Should a person-item be nameable ("Mum", "my manager") — and if so, that is personal data in a
   payload sent to the assistant. Worth deciding deliberately, not by default.
3. Does the flow-side assistant need to know it is receiving a *practice* rather than a *divinatory
   reading*? Its grounding prompt would sensibly differ. If so, `ReadingV1` may want a `kind` field —
   an additive change the contract's tolerate-unknown-fields rule already permits.
