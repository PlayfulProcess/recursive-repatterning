#!/usr/bin/env python3
"""
Rebuild schools/across-the-schools/grammar.json — the aggregator.

This replaces the tarot-era script of the same name, which resolved ROOT/"tarot"
as its data folder and carried a large hand-maintained table of tarot deck
metadata (trump orders, eras, ancestry lanes). None of that transfers, so this
is a rewrite rather than a path fix.

What the aggregator is FOR: several viewers (cards.html, explorer.html,
caster-studio.html) default to it when no ?src= is given. It is the flattened
pool of every drawable item across every school, so a cast can sample the whole
library at once rather than one school at a time.

What it is NOT: the constellation. schools/schools-of-emotion/grammar.json is
the L1->L2->L3 tree, and it has a builder of its own — scripts/build_constellation.py,
which derives it from _collection.json. Do not write it from here.

Rules this honours (see CLAUDE.md):
  - Cross-links use metadata.source_deck / source_item_id / deck. That is the
    ONLY cross-grammar navigation mechanism in this chassis; item_type:
    "reference" / ref_document_id is documented upstream but unused and
    untested here.
  - Composite items (anything carrying composite_of) are skipped. Those are
    groupings, not drawable content — including them would let a cast return
    "Joy family" instead of an actual emotion.
  - metadata.emotion_key is carried through, so a cross-school cast can still
    tell that Plutchik's "fear" and NVC's "fear" are the same key.

Usage:  python scripts/build_meta_grammar.py [--check]
        --check exits non-zero if the file on disk is stale, without writing.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
SCHOOLS = os.path.join(ROOT, "schools")
OUT_SLUG = "across-the-schools"
OUT = os.path.join(SCHOOLS, OUT_SLUG, "grammar.json")

# Hand-authored; generating over it would destroy real content.
# genealogy-of-emotions is excluded for a different reason: its items are historical
# moments (Descartes 1649, Bharata's Natyashastra), not feelings. They are worth
# browsing but not worth drawing — a cast should return an emotion, not a citation.
# It stays a full member of the channel; it is only kept out of the castable pool.
# ethics-of-fiction is excluded on the same principle: its items are lenses,
# contexts and case verdicts — a judging instrument. Drawing "Bettelheim — the
# Judge Judged" in a pooled emotional reading would be noise. It remains fully
# castable on its own through the deck picker; only the cross-school pool skips it.
# overflow, by contrast, IS a drawable deck and joins the pool.
NEVER_AGGREGATE = {OUT_SLUG, "schools-of-emotion", "genealogy-of-emotions",
                   "ethics-of-fiction"}


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def school_slugs():
    """Every school listed in the collection manifest, in branch order."""
    coll = load(os.path.join(SCHOOLS, "_collection.json"))
    slugs = []
    for branch in coll.get("branches", []):
        for slug in branch.get("school_slugs", []):
            if slug not in NEVER_AGGREGATE and slug not in slugs:
                slugs.append(slug)
    return slugs


def build():
    items = []
    sources = []

    for slug in school_slugs():
        path = os.path.join(SCHOOLS, slug, "grammar.json")
        if not os.path.isfile(path):
            print(f"  WARN  {slug}: no grammar.json, skipped")
            continue

        g = load(path)
        label = g.get("name", slug)
        kept = 0

        for item in g.get("items", []):
            # Composites are groupings, not drawable content.
            if item.get("composite_of"):
                continue

            meta = dict(item.get("metadata") or {})
            # The one permitted cross-link pattern.
            meta["source_deck"] = slug
            meta["source_item_id"] = item.get("id", "")
            meta["deck"] = label

            items.append({
                "id": f"{slug}--{item.get('id','')}",
                "name": item.get("name", ""),
                "category": item.get("category", slug),
                "sections": item.get("sections", {}),
                "keywords": item.get("keywords", []),
                "image_url": item.get("image_url", ""),
                "metadata": meta,
            })
            kept += 1

        sources.append({"slug": slug, "name": label, "items": kept})
        print(f"  ok    {slug}: {kept} items")

    return {
        "_generated": True,
        "_generated_by": "scripts/build_meta_grammar.py",
        "_note": (
            "GENERATED — do not hand-edit. Rebuild with "
            "`python scripts/build_meta_grammar.py`. Edits belong in the "
            "individual school under schools/<slug>/grammar.json."
        ),
        # Deliberately NOT "all schools" — this library holds a handful of the
        # ways people have organised feeling, and could never hold them all.
        # Claiming completeness would be the same overreach the library exists
        # to refuse. Name it for what it does (reads across) not for what it
        # would have to contain.
        "name": "Across the Schools",
        "description": (
            "The drawable items from the schools currently in this library, "
            "pooled into one grammar so a reading can sample across several at "
            "once. This is a partial collection and always will be — there is no "
            "complete set of the ways people have organised feeling. Each item "
            "links back to the school it came from and keeps that school's own "
            "words; the pooling is for reach, not for flattening them into a "
            "single house taxonomy."
        ),
        "grammar_type": "tarot",
        "tags": ["emotions", "meta", "generated"],
        "default_preview": "grammar",
        "_sources": sources,
        "items": items,
        "_grammar_commons": {
            "schema_version": "1.0",
            "license": "CC-BY-SA-4.0",
            "license_url": "https://creativecommons.org/licenses/by-sa/4.0/",
            "attribution": [{
                "name": "PlayfulProcess",
                "note": (
                    "Generated aggregate of the schools in this repo. Each item's "
                    "attribution is carried by its source school."
                ),
            }],
        },
    }


def sync_collection_index():
    """Refresh _collection.json's top-level `grammars[]` index.

    The viewers (viewers/deck-picker.js, viewers/cards.html, pages/courses.html)
    all read `collection.grammars[]` — a flat list of every grammar with its
    slug, name and cover. The hand-written manifest here only had
    `branches[].school_slugs`, so every one of those consumers silently got an
    empty list: the schools dropdown opened blank and the deck switcher showed
    nothing. Generating the index keeps all of them working from one source
    instead of patching each reader in turn.

    Only `grammars` is rewritten; branches and notes are left alone.
    """
    path = os.path.join(SCHOOLS, "_collection.json")
    coll = load(path)

    branch_of = {}
    for branch in coll.get("branches", []):
        for slug in branch.get("school_slugs", []):
            branch_of[slug] = branch.get("id")

    index = []
    for entry in sorted(os.listdir(SCHOOLS)):
        gpath = os.path.join(SCHOOLS, entry, "grammar.json")
        if not os.path.isfile(gpath):
            continue
        g = load(gpath)
        index.append({
            "slug": entry,
            "name": g.get("name", entry),
            "common_name": g.get("common_name") or g.get("name", entry),
            "type": g.get("grammar_type", "custom"),
            "branch": branch_of.get(entry),
            "is_meta": bool(g.get("_generated")) or entry in NEVER_AGGREGATE,
            "default_preview": g.get("default_preview"),
            "items": len(g.get("items", [])),
            "cover_image_url": g.get("cover_image_url", ""),
            "path": f"schools/{entry}/grammar.json",
            "year": g.get("year"),
            "year_label": g.get("year_label"),
            "provenance": g.get("provenance", "record"),
            "category": g.get("category", "historical"),
        })

    if coll.get("grammars") == index:
        return False
    coll["grammars"] = index
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(coll, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"synced _collection.json grammars index: {len(index)} entries")
    return True


def main():
    check = "--check" in sys.argv
    meta = build()

    existing = load(OUT) if os.path.isfile(OUT) else None
    changed = existing != meta

    if check:
        # --check must not write, so the index is compared, not synced.
        if changed:
            print("STALE — run `python scripts/build_meta_grammar.py` and commit the result")
            return 1
        print(f"up to date: {len(meta['items'])} items from {len(meta['_sources'])} schools")
        return 0

    if changed:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, "w", encoding="utf-8") as fh:
            json.dump(meta, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print(f"wrote {os.path.relpath(OUT, ROOT)}: "
              f"{len(meta['items'])} items from {len(meta['_sources'])} schools")
    else:
        print(f"up to date: {len(meta['items'])} items from {len(meta['_sources'])} schools")

    # AFTER the aggregator is on disk — the index records its item count, so
    # syncing first would record the previous run's number.
    sync_collection_index()
    return 0


if __name__ == "__main__":
    sys.exit(main())
