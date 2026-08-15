#!/usr/bin/env python3
"""
Cut a slice of an open word-vector space and light up this library's vocabulary in it.

This is deliberately NOT a bespoke embedding of our own. It takes an existing,
published, open-weights model and shows where IT already places these words —
an artifact we exhibit rather than a claim we made. Same move the library makes
with Plutchik and Ekman: here is a map somebody else drew, look at it.

What it writes (schools/_proximity.json, small and committed):
  terms[]   one entry per vocabulary word we could locate in the model, with
            a 2-D position, its true nearest neighbours, and which schools use it
  missing[] the words the model has NO vector for. This list is not a failure
            report — it is a finding. A word absent from an English corpus is
            usually a word that does not translate into one.
  outside[] words the MODEL places near our cluster that the library does not
            contain. A gap-finder: the collection's own blind spots, named.

Two deliberate constraints:
  - Nearest neighbours are computed in the FULL vector space, never in the 2-D
    projection. Projections distort distance, and neighbours read off a flattened
    view would be quietly, plausibly wrong.
  - Projection is PCA via numpy's SVD. No scikit-learn, no UMAP. PCA is linear
    and honest about what it discards; UMAP invents pleasing structure that is
    hard to defend when the whole point is not to overclaim.

Runtime cost to the site: zero. The model is used here, at build time, and the
committed output is a small JSON. Nothing is downloaded by a visitor.

Usage:
  python scripts/build_proximity.py                 # default model
  python scripts/build_proximity.py --model glove-wiki-gigaword-100
  python scripts/build_proximity.py --keep-model    # don't delete the cache after
"""
import argparse
import json
import os
import re
import shutil
import unicodedata
import sys
from collections import defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
SCHOOLS = os.path.join(ROOT, "schools")
OUT = os.path.join(SCHOOLS, "_proximity.json")

# Apparatus, not content — their items are pointers or historical moments.
SKIP_SCHOOLS = {"across-the-schools", "schools-of-emotion", "genealogy-of-emotions"}

DEFAULT_MODEL = "glove-wiki-gigaword-100"


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def normalise(term):
    """Lowercase, strip diacritics crudely, keep a single word.

    Vector models are keyed on plain lowercase tokens, so 'Śṛṅgāra' has to become
    'shringara' to have any chance of a hit — and usually still misses, which is
    itself the interesting part.
    """
    t = term.strip().lower()
    # A slash means the source offered alternatives ("rest/sleep", "movement/exercise").
    # Take the first; joining them invents a word no corpus has.
    t = t.split("/")[0]
    # Decompose to strip combining marks generically. Doing this by hand missed
    # macrons and carons — hēdonē came out "hdon", kǒng came out "kng" — which then
    # looked like evidence that Greek and Chinese terms are absent from the corpus
    # when it was only evidence that the normaliser was wrong.
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    # Sanskrit retroflex/palatal sibilants survive decomposition as their own letters.
    t = t.replace("ś", "sh").replace("ṣ", "sh").replace("ß", "ss").replace("ø", "o")
    t = re.sub(r"[^a-z\- ]", "", t).strip()
    return t


def collect_vocabulary():
    """Every word this library actually uses, with the schools that use it.

    Three sources, in descending confidence: emotion_key (the curated key), the
    item's own name, and keywords (where the NVC school carries several hundred
    inventory words that exist nowhere else).
    """
    vocab = defaultdict(lambda: {"schools": set(), "sources": set(), "items": set()})

    for entry in sorted(os.listdir(SCHOOLS)):
        gpath = os.path.join(SCHOOLS, entry, "grammar.json")
        if not os.path.isfile(gpath) or entry in SKIP_SCHOOLS:
            continue
        g = load(gpath)
        for item in g.get("items", []):
            meta = item.get("metadata") or {}
            if item.get("composite_of"):
                continue  # groups and roots are structure, not vocabulary

            def add(raw, source):
                t = normalise(raw)
                if not t or " " in t or len(t) < 3:
                    return
                v = vocab[t]
                v["schools"].add(entry)
                v["sources"].add(source)
                v["items"].add(f"{entry}/{item.get('id','')}")

            if meta.get("emotion_key"):
                add(meta["emotion_key"], "emotion_key")
            if item.get("name"):
                # names are often phrases; take the first word only when short
                nm = item["name"].split("—")[0].split("(")[0].strip()
                if len(nm.split()) == 1:
                    add(nm, "name")
            for kw in (item.get("keywords") or []):
                add(kw, "keyword")

    return vocab


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--keep-model", action="store_true",
                    help="keep the downloaded model cache instead of deleting it")
    ap.add_argument("--neighbours", type=int, default=8)
    args = ap.parse_args()

    vocab = collect_vocabulary()
    print(f"vocabulary collected: {len(vocab)} distinct terms")

    import gensim.downloader as api
    print(f"loading {args.model} (downloads once, then cached)…")
    kv = api.load(args.model)
    dim = kv.vector_size
    print(f"model loaded: {len(kv.index_to_key):,} words, {dim} dims")

    found, missing = {}, []
    for term, info in sorted(vocab.items()):
        if term in kv:
            found[term] = info
        else:
            # Two very different reasons a word can be absent, and conflating them
            # would ruin the finding. A hyphen here means OUR normaliser joined a
            # phrase ("repair attempt" -> "repair-attempt"); the model simply has no
            # such token, which says nothing about language. A single word that is
            # absent — shringara, ko-omote, allegrezza — is the real result: a term
            # an English-dominant corpus never had occasion to learn.
            kind = "compound" if "-" in term else "single-word"
            missing.append({"term": term, "kind": kind,
                            "schools": sorted(info["schools"]),
                            "sources": sorted(info["sources"])})
    n_single = sum(1 for m in missing if m["kind"] == "single-word")
    print(f"in model: {len(found)}   absent: {len(missing)} "
          f"({n_single} single words, {len(missing) - n_single} our own compounds)")

    if not found:
        print("no terms found in model — aborting")
        return 1

    terms = sorted(found)
    M = np.stack([kv[t] for t in terms]).astype(np.float64)

    # Nearest neighbours in the FULL space, on unit vectors so dot == cosine.
    Mn = M / np.linalg.norm(M, axis=1, keepdims=True)
    sims = Mn @ Mn.T
    np.fill_diagonal(sims, -np.inf)

    # PCA by SVD on the centred matrix. Two components, plus the variance they
    # actually explain — reported so the picture cannot be oversold.
    C = M - M.mean(axis=0)
    U, S, Vt = np.linalg.svd(C, full_matrices=False)
    xy = C @ Vt[:2].T
    explained = float((S[:2] ** 2).sum() / (S ** 2).sum())
    # scale to a friendly range for the viewer
    xy = (xy - xy.min(axis=0)) / (xy.max(axis=0) - xy.min(axis=0) + 1e-9)

    out_terms = []
    for i, t in enumerate(terms):
        order = np.argsort(-sims[i])[: args.neighbours]
        out_terms.append({
            "term": t,
            "xy": [round(float(xy[i][0]), 4), round(float(xy[i][1]), 4)],
            "schools": sorted(found[t]["schools"]),
            "sources": sorted(found[t]["sources"]),
            "items": sorted(found[t]["items"])[:6],
            "near": [{"term": terms[j], "score": round(float(sims[i][j]), 3)}
                     for j in order],
        })

    # The gap-finder. An earlier version scored candidates against the centroid of
    # our whole vocabulary and returned "feeling, sense, kind, very, much" — the
    # centroid of several hundred emotion words sits in generic filler, so that
    # measured word frequency, not relevance.
    #
    # This asks a sharper question: which words are near OUR SPECIFIC terms, and
    # near several of them, without being in the library? A word neighbouring both
    # "grief" and "yearning" is a candidate we are missing. One neighbouring only
    # a single term is probably noise.
    have = set(terms)
    # Very common words are neighbours of everything; skip the frequency head.
    # index_to_key is frequency-ordered, so this is a rank cutoff, not a guess.
    too_common = set(kv.index_to_key[:800])
    hits = defaultdict(lambda: {"n": 0, "score": 0.0, "near_our": []})
    for t in terms:
        for w, s in kv.most_similar(t, topn=12):
            if w in have or w in too_common or len(w) < 4 or not w.isalpha():
                continue
            h = hits[w]
            h["n"] += 1
            h["score"] += float(s)
            if len(h["near_our"]) < 5:
                h["near_our"].append(t)
    ranked = sorted(hits.items(), key=lambda kv_: (-kv_[1]["n"], -kv_[1]["score"]))
    outside = [{"term": w,
                "shared_neighbours": h["n"],
                "avg_score": round(h["score"] / h["n"], 3),
                "near_our": h["near_our"]}
               for w, h in ranked[:80] if h["n"] >= 2]

    payload = {
        "_note": ("GENERATED by scripts/build_proximity.py — do not hand-edit. "
                  "A slice of an existing open word-vector model, showing where IT "
                  "places this library's vocabulary. Not a claim about what these "
                  "words mean; a record of how they co-occur in one corpus."),
        "model": args.model,
        "dims": dim,
        "pca_explained_variance": round(explained, 4),
        "counts": {"in_model": len(found), "absent": len(missing),
                   "outside_suggestions": len(outside)},
        "terms": out_terms,
        "missing": missing,
        "outside": outside,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    size = os.path.getsize(OUT) / 1024
    print(f"wrote {os.path.relpath(OUT, ROOT)} ({size:.0f} KB)")
    print(f"PCA explains {explained:.1%} of variance in 2 dimensions")

    if not args.keep_model:
        cache = os.path.expanduser("~/gensim-data")
        if os.path.isdir(cache):
            shutil.rmtree(cache, ignore_errors=True)
            print("deleted model cache (disk is tight; re-downloads on next run)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
