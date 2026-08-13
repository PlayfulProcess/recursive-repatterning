# Sources, credit, and caveats

This is the honest accounting of how Recursive Repatterning sources its content,
credits its influences, and marks the limits of what it's claiming. If something here
looks evasive, that's a bug in the document — please [open an
issue](https://github.com/PlayfulProcess/recursive-repatterning/issues).

---

## 1. Licensing model

This repo splits its license by kind, following the pattern set in [`LICENSE`](../LICENSE)
and [`LICENSE-CONTENT.txt`](../LICENSE-CONTENT.txt):

- **Code is MIT.** Everything under `viewers/`, `scripts/`, `pages/` markup and JS, and the
  chassis mechanics — copy it, fork it, embed it in a commercial product, no attribution
  required (though appreciated).
- **Content is CC-BY-SA-4.0.** The grammars (`schools/*/grammar.json`), the docs, the course
  material — anything that is the library's *voice* rather than its *machinery*.

In plain language, for someone forking a grammar or reusing content from this library:

- **You can:** copy a whole school grammar, translate it, remix it into your own deck,
  publish it commercially, build a different viewer around it.
- **You must:** credit the source (this repo, and the `_grammar_commons.attribution`
  entries inside the grammar you took — see §3), and license *your* version under
  CC-BY-SA-4.0 or a compatible share-alike license. You can't take a CC-BY-SA grammar,
  modify it, and re-release the modified version under a more restrictive license or as
  closed content.
- **You don't need to ask permission first.** That's the point of a share-alike license —
  it's pre-authorized, conditional on passing the same freedom forward.

If you fork the whole repo (code + content together), the two licenses travel with their
respective files — you don't get to relicense the grammars just because the surrounding
code is MIT.

---

## 2. The Wellcome question

`docs/ILLUSTRATION-SOURCES.md` (the illustration research pass) flagged a real tension and
deliberately left it open. This section resolves it.

**The situation:** Darwin's 1872 plates from *The Expression of the Emotions in Man and
Animals* are unambiguously public domain — Darwin died in 1882, the book is 150+ years
old, no jurisdiction extends copyright anywhere near that far. But the specific *scans* of
those plates hosted on Wikimedia Commons via Wellcome Collection are tagged **CC BY 4.0**,
not CC0 or `{{PD-old}}`. That's Wellcome asserting a fresh copyright claim over its
photographic reproduction of a flat, public-domain 2D work — not a claim over anything
Darwin made, but over the act of scanning it.

That class of claim is legally contested. In the US, the *Bridgeman Art Library v. Corel
Corp.* line of reasoning holds that a faithful photographic reproduction of a flat
public-domain artwork is not original enough to generate new copyright — there's nothing
to protect, because the photographer contributed no creative choices the reproduction
required. Other jurisdictions (notably parts of the EU, post the "sweat of the brow"
tradition) have historically been more willing to recognize a reproduction right. Wellcome
itself isn't even internally consistent: their own institutional site states some of these
images as CC BY-NC 4.0 in one place and the Commons upload carries plain CC BY 4.0 — two
different licenses for the same photograph. This is not a resolved question, and this
document does not pretend to resolve it as a matter of law.

**The maintainer's decision:** this library prefers Internet Archive and Biodiversity
Heritage Library (BHL) scans over Wellcome-tagged Wikimedia Commons scans, where an
equivalent scan exists. BHL states these Darwin volumes as public domain outright, with no
attribution license layered on top; Internet Archive's Darwin Online copy claims no license
at all over the 1872 first edition.

**Why, given that CC BY is legally usable here.** CC BY 4.0 is fully compatible with this
library's CC-BY-SA-4.0 content license — attributing Wellcome and using their scan would be
lawful, full stop. The reason to prefer IA/BHL anyway isn't a legal one, it's an editorial
one: this is a commons library, built on the premise that a school's content should be as
forkable and encumbrance-free as the underlying public-domain material actually is. Passing
along a CC BY *attribution obligation* that Wellcome invented on top of already-PD content —
even a lawful one — adds a downstream requirement to something that, by rights, shouldn't
carry one. It's a small tax on forkability, imposed by a scanning institution rather than by
anything Darwin owned, and this library would rather not pass it on when a tax-free
alternative exists.

**Where Wellcome (or any institution making a similar claim) is genuinely the only
available source** — a specific plate, crop, or resolution that no other digitization
offers — this library will use it and attribute it plainly, exactly as the CC BY license
requires, rather than pretend the claim doesn't exist. Silence about a real license claim
would be worse than complying with one this library is skeptical of.

**Stated as policy, for anyone reusing this repo's pattern:**

1. Prefer the least-encumbered available scan of public-domain source material — direct
   archive/library digitizations (Internet Archive, BHL, national libraries) over
   institution-badged Commons uploads, when both exist.
2. Where only a fresh-rights-claimed scan is available, use it and attribute honestly.
   Don't skip a needed image over this; don't hide the attribution either.
3. State the reasoning where a reader can see it (here), rather than leaving the choice
   unexplained in a commit message.

**Reasonable people disagree about whether these claims are valid at all.** Some
institutions and archivists consider Wellcome-style CC BY tags on faithful PD reproductions
to be over-claiming, unenforceable outside jurisdictions with a reproduction right, or
simply irrelevant once the underlying work is PD. Others treat the scan itself — the
lighting, cropping, color correction, restoration work — as enough original labor to merit
its own copyright. This document takes a *practical* position (prefer the cleaner source
when one exists) without taking a *legal* position on who's right.

As of this writing, no Darwin (or any other) plate has actually been added to any grammar
in this repo — `docs/ILLUSTRATION-SOURCES.md` is a sourcing map for future work, not a
record of images already in use. This section documents the policy that will govern that
work when it happens.

---

## 3. How each school is attributed

Every school in this library follows the same shape, verified here against the one
grammar that currently exists (`schools/plutchik-wheel/grammar.json`) and the format
contract in [`GRAMMAR_FORMAT.md`](../GRAMMAR_FORMAT.md):

- **Original prose only.** No text is copied from any in-copyright source. Where a
  school's source material is in copyright (Rosenberg/NVC, Johnson/EFT, Brown/*Atlas of
  the Heart*, Linehan/DBT), category definitions are paraphrased and entirely original
  prose is written for every section — never quoted passages.
- **The framework's originator is credited at grammar root**, in
  `_grammar_commons.attribution` — an array of `{name, role, note}` objects. Plutchik's
  grammar carries two entries: Robert Plutchik as `"source model"` (crediting the
  1980 psychoevolutionary structure, with an explicit "no text is copied" note) and
  PlayfulProcess as `"creator"` (crediting the actual prose, composite items, and
  editorial commentary). The real field shape, from the grammar file:

  ```json
  "_grammar_commons": {
    "schema_version": "1.0",
    "license": "CC-BY-SA-4.0",
    "attribution": [
      {
        "name": "Robert Plutchik",
        "role": "source model",
        "note": "Structural basis: Plutchik's 1980 psychoevolutionary theory of emotion... No text is copied from Plutchik's copyrighted publications."
      },
      {
        "name": "PlayfulProcess",
        "role": "creator",
        "note": "Author of this grammar's text, the composite family/root items, and the library's editorial commentary (Constructionist lens, evidence_tier)."
      }
    ]
  }
  ```

- **One source per grammar.** A grammar carries one school's, one author's voice. If a
  second author's take on the same subject matters enough to include, it becomes a
  *separate* grammar, cross-linked back via the `source_deck`/`source_item_id`/`deck`
  metadata pattern documented in `CLAUDE.md` — never stacked into the same item as a
  second voice. This is the same rule `GRAMMAR_FORMAT.md` documents (under "ONE SOURCE PER
  DECK") for the sibling tarot chassis this repo was copied from, applied here to schools
  of emotion instead of tarot decks.
- **Public-domain foundations used directly.** Darwin (1872) and James (1890) are old
  enough, and their authors dead long enough, that their text itself can be used without
  paraphrase — see §2 above for how that same public-domain status interacts with
  *images* of their work, which is a separate question from the text.

---

## 4. The evidence tiers

Every school-level item carries `metadata.evidence_tier`, one of:

- `independently-replicated` — the model or a specific claim within it has been tested
  and confirmed by researchers other than its originator, more than once.
- `growing` — a meaningful and expanding body of supporting research exists, but
  independent replication is not yet as deep or as settled.
- `observational-only` — support comes from clinical observation, case study, or
  correlational data, without controlled replication.
- `theoretical` — the model is a structural proposal without independent empirical
  confirmation of its specific claims.

Each tier is paired with `metadata.evidence_note` — a short, specific statement of *why*
that tier applies to *this* item, not a generic disclaimer. Plutchik's root item is the
working example:

```json
"metadata": {
  "evidence_tier": "theoretical",
  "evidence_note": "Plutchik's eight-family structure, its opposite pairs, and its dyad adjacencies are a theoretical proposal with no independent empirical confirmation. The 2019 Barrett/Adolphs/Marsella/Martinez/Pollak meta-analysis found no reliable facial or physiological fingerprint for discrete emotion categories generally, which undercuts the basic-emotion premise this wheel depends on."
}
```

**The point of doing this at all:** Sue Johnson's Emotionally Focused Therapy and John
Gottman's method do not rest on equivalent evidence bases — one has a different volume and
kind of outcome research behind it than the other. A library that badges both
"evidence-based" without distinction hides that difference from the reader at exactly the
moment it matters most. `evidence_tier` exists so a reader doesn't have to already know
the literature to see which claims are load-bearing and which are still provisional.

**What this is not.** These tiers are the maintainer's (PlayfulProcess's) editorial
judgment, formed from reading published literature — not a formal systematic review, not
a meta-analysis conducted for this project, and not peer-reviewed. No tier here should be
taken as a verdict a reader can cite; it's a starting orientation. Readers who need to
rely on a claim should check the cited work directly, not this library's summary of it.

---

## 5. AI disclosure

`README.md` already states it plainly: **"Drafted with Claude, reviewed by the
maintainer."** This document repeats it here because it belongs in the sourcing page, not
only the front page.

What that means practically:

- Grammar prose, section text, and documentation in this repo are drafted with AI
  assistance (Claude), then reviewed by PlayfulProcess before being committed.
- **AI-drafted text can misstate a citation, misattribute a claim, or introduce a
  confident-sounding error that isn't in the source.** Review is meant to catch this, but
  review is not the same as independent verification of every citation against its
  primary source.
- If you're relying on a specific factual claim, an `evidence_note`, or a citation
  anywhere in this repo for something that matters, **check it against the primary
  source**, not just against this library's rendering of it.
- Errors that make it through review are the maintainer's to fix, not the AI's or any
  contributor's. If you find one, see §7.

---

## 6. Known caveats and open problems

This is the honest list, not a curated one. Some of these are simple TODOs; a couple are
real tensions the library doesn't try to hide.

- **`relationship-cards` is a seed, not yet imported.** Per `_seeds/README.md`, all 298
  sections of that grammar still carry a literal `[SESSION-N: SUITNAME]` build tag in the
  prose — it's a structured research skeleton, not finished copy, and it isn't part of
  the published library yet.
- **No school grammar sets `image_url` on any item.** Illustration is unstarted.
  `docs/ILLUSTRATION-SOURCES.md` is a research pass toward that work (source candidates,
  licenses, editorial framing) — not a record of images already placed. The one
  `image_url` currently present anywhere in `schools/` (on every Plutchik item) points at
  the same Wikimedia wheel diagram repeated 32 times — a placeholder, not per-item
  illustration.
- **The library currently contains one school.** Plutchik's Wheel of Emotions
  (`schools/plutchik-wheel/`) is the only populated school grammar under `schools/`; every
  other branch listed in `schools/_collection.json` (NVC, attachment/couples, DBT/skills,
  parts-and-depth, historical-scientific) has an empty `school_slugs` array. And
  Plutchik's own `evidence_tier` is `theoretical` — the one school in the library is, by
  its own metadata, the lowest evidence tier this project's schema defines.
- **The taxonomy-vs-discovery tension is real and is stated, not smoothed over.**
  Plutchik's wheel geometry — eight families, four opposing pairs, the specific
  adjacency-dyads — has no independent empirical support; it is Plutchik's own structural
  proposal. Separately, the 2019 meta-analysis by Barrett, Adolphs, Marsella, Martinez, and
  Pollak (*Psychological Science in the Public Interest*) reviewed the evidence for
  discrete emotion categories having reliable, specific facial or physiological signatures
  and found none. That finding bears directly on the basic-emotion premise the wheel is
  built on. This means the library is publishing a taxonomy — a structured, memorable,
  usable vocabulary — while its own `Research note` and `Constructionist lens` sections
  argue that taxonomy is not a discovery about how bodies or brains actually work. That's
  not a contradiction this document is trying to resolve away: the library's stated
  position (see `README.md`) is that a map being constructed is not the same as a map
  being wrong, and a reader is meant to encounter both the map and that caveat together,
  not the map alone.
- **"EFT" names two different, unrelated frameworks**, and this repo — like the rest of
  this project family — always disambiguates:
  - **Sue Johnson's *Emotionally* Focused Therapy** — couples therapy, grounded in
    attachment theory.
  - **Leslie Greenberg's *Emotion*-Focused Therapy** — individual, experiential therapy,
    grounded in humanistic/Gestalt traditions.
  They share an acronym and share no lineage. Any content in this repo referencing "EFT"
  names which one, every time; if you ever find an un-disambiguated "EFT" in this repo,
  that's a bug — see §7.

---

## 7. How to report an error

Open an issue at
**[github.com/PlayfulProcess/recursive-repatterning/issues](https://github.com/PlayfulProcess/recursive-repatterning/issues)**.

That covers: a mis-cited source, a wrong evidence tier, an un-disambiguated "EFT," a
license claim you think this document gets wrong, a factual error in a school's prose, or
anything else. There is no other error-reporting channel for this repo — issues are it.
