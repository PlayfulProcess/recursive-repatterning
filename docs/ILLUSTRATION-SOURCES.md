# Illustration sources — research notes

**Status: research only. Nothing in this repo was changed except this file. No images
were downloaded.** This is a sourcing map for whoever does the illustration pass, not a
finished asset list — every URL below should be re-checked at the point of use, licences
especially.

## Why this exists

The site currently ships no art of its own. The homepage hero, the "school" cards, and
the explorer thumbnails all still point at `visconti-sforza-tarot` files inherited from
the `recursive-tarot` chassis this repo was copied from (see `README.md` → Provenance).
That's an honest placeholder, not a secret — `index.html` even labels the hero image
`alt="A placeholder plate — this library's own emotion-school illustrations are still
being made"` — but a tarot deck is the wrong picture for a library about the schools of
emotion, and it should be swapped for something on-topic before this site is called done.

Confirmed placeholder locations (`index.html`, current `main`):

| Line | What it shows | Current file |
|---|---|---|
| 190 | Hero plate | `visconti-sforza-tarot/Visconti-sforza-21-world.jpg` |
| 206 | Card top | `visconti-sforza-tarot/Visconti-sforza-03-empress.jpg` |
| 214 | Card top | `visconti-sforza-tarot/Visconti-sforza-18-moon.jpg` |
| 222 | Card top | `visconti-sforza-tarot/Visconti-sforza-17-star.jpg` |
| 277 | Thumbnail | `visconti-sforza-tarot/Visconti-sforza-00-fool.jpg` |
| 285 | Thumbnail | `visconti-sforza-tarot/Visconti-sforza-14-temperance.jpg` |
| 293 | Thumbnail | `visconti-sforza-tarot/Visconti-sforza-19-sun.jpg` |
| 297 | Thumbnail | `visconti-sforza-tarot/Bembo-Visconti-tarot-coins-13-queen.jpg` |

Separately: `schools/plutchik-wheel/grammar.json` already sets `image_url` on all 32
items, but every single one points at the same file — the Wikimedia Plutchik-wheel SVG
diagram (`cover_image_url` reused as every item's `image_url`). That's not a tarot
leftover, it's this repo's own placeholder pattern, and it has the same problem as the
tarot cards: one picture standing in for 32 different things. Worth fixing in the same
pass — ideally one image per `emotion_key`, not one diagram repeated 32 times.

---

## The repo's actual image field shapes

The task brief that generated this document expected a `metadata.illustrations[]`
array. **That field does not exist anywhere in this codebase** — I grepped
`GRAMMAR_FORMAT.md`, `_seeds/README.md`, every script under `scripts/`, and
`schools/plutchik-wheel/grammar.json` and found no such array, in this repo or (by
inheritance) in `recursive-tarot`. What actually exists, confirmed by reading
`GRAMMAR_FORMAT.md` and the working scripts `scripts/rehost_to_r2.py`,
`scripts/backfill_image_provenance.py`, and `scripts/audit_image_usage.py`:

| Field | Level | Shape | Purpose |
|---|---|---|---|
| `cover_image_url` | grammar root | string (URL) | Hero/deck-cover image |
| `cover_image_credit` | grammar root | object `{title, creator, date, source, file_page, license, pd_basis, verified}` | Structured credit for the cover — the shape `scripts/backfill_image_provenance.py` writes |
| `image_credit` | grammar root | **string** | One factual credit line for the deck, read by `viewers/course-embeds.js` and `pages/course-viewer.html`. Stays a string — do not turn it into an object |
| `_grammar_commons.attribution` | grammar root | array of `{name, role, note}` | The licence/attribution block `GRAMMAR_FORMAT.md` documents; also where per-source "no text copied" language goes |
| `_image_provenance` | grammar root | object `{schema_version, holding_institution, archive, license, pd_basis, verified, per_item_field, mapping_rule, unknown}` | One deck-level block naming where every image in the deck came from, so you don't repeat the same paragraph per card |
| `image_url` | item | string (URL) | Per-item image — R2 URL or any HTTPS URL (Wikimedia works directly) |
| `metadata.image_source` | item | string (URL) | That specific item's upstream file/folio page — set alongside `image_url` |
| `_image_usage` | grammar root (generated) | array of `{image, used_on}` | Written by `scripts/audit_image_usage.py`; tracks which site pages reuse which image so the same picture doesn't repeat across Home/Play/About |

There is no per-item array of multiple images — one `image_url` per item is the pattern
throughout this repo family. If a school genuinely needs more than one image per item
(e.g. a Darwin plate *and* a Duchenne comparison photo on the same emotion), the
precedent (`GRAMMAR_FORMAT.md` → "Composite items") suggests either picking the single
best image for `image_url` and mentioning the rest in prose, or, if it becomes a real
pattern, raising it as a genuinely new field rather than inventing one silently —
`CLAUDE.md`'s core rule is "consolidate, don't multiply."

### The two valid URL shapes

1. **R2 (this repo's own hosted copies):**
   `https://pub-71ebbc217e6247ecacb85126a6616699.r2.dev/grammar-illustrations/<slug>/<filename>`
   — this is where files land *after* someone runs `scripts/rehost_to_r2.py` against a
   Wikimedia source. Nothing has been rehosted for any emotion-school image yet.
2. **Direct Wikimedia `Special:FilePath`:** `image_url` can point straight at Wikimedia
   without rehosting anything — `schools/plutchik-wheel/grammar.json` already does this
   with plain `upload.wikimedia.org` URLs. The stable, redirect-based form is
   `https://commons.wikimedia.org/wiki/Special:FilePath/File:<exact file name>`, which
   is safer to hand-write than guessing the `upload.wikimedia.org/wikipedia/commons/x/xx/`
   hash-bucket path. **Given the 94%-full disk, direct Wikimedia linking (no rehost) is
   the lower-risk default** until there's a reason to own a local copy (rate limits,
   Commons file gets renamed/deleted, or the maintainer wants final-cropped versions).

---

## Source table

Licence status is stated as verified where I could confirm the exact tag on the file
page or museum object page itself; anything short of that is marked explicitly.

### 1. Darwin, *The Expression of the Emotions in Man and Animals* (1872)

This repo already has a grammar built from this text
(`_seeds/README.md` → `grammars/expression-of-emotions.json`, 19 items, historical-scientific
branch) but it has never carried images. The book's underlying text and plates are
unambiguously public domain everywhere (published 1872, Darwin died 1882) — **the only
open question is which scanned copy to point at**, because two different digitisations
carry different licence claims on top of the same PD content.

| Plate / subject | Source copy | Direct URL | Licence as stated on that page | Fits |
|---|---|---|---|---|
| "Terror" (fig., man) | Wikimedia Commons, ex-Wellcome | https://commons.wikimedia.org/wiki/File:Terror,_from_Darwin%27s_Expression_of_Emotions_in_Man...._Wellcome_L0049512.jpg | **CC BY 4.0** (Wellcome's own tag — see caveat below) | Plutchik `fear`/`terror` |
| "Grief" | Wikimedia Commons, ex-Wellcome | https://commons.wikimedia.org/wiki/File:Grief,_from_Darwin%27s_Expressions_of_Emotions_in_Man....._Wellcome_L0049517.jpg | **CC BY 4.0** (verified on file page: "This file is licensed under the Creative Commons Attribution 4.0 International license") | Plutchik `sadness`/`grief` |
| "Disdain and disgust" | Wikimedia Commons, ex-Wellcome | https://commons.wikimedia.org/wiki/File:Disdain_and_disgust_from_Darwin%27s_Expression_of_Emotions..._Wellcome_L0049514.jpg | CC BY 4.0 (same Wellcome pattern) | Plutchik `disgust` |
| "Surprise and distress" | Wikimedia Commons, ex-Wellcome | https://commons.wikimedia.org/wiki/File:Surprise_and_distress_in_Darwin%27s_Expression_of_Emotions..._Wellcome_L0049511.jpg | CC BY 4.0 (same Wellcome pattern) | Plutchik `surprise` |
| "Horror and agony" | Wikimedia Commons, ex-Wellcome | https://commons.wikimedia.org/wiki/File:Horror_and_agony_from_Darwin%27s_Expression_of_Emotions..._Wellcome_L0049510.jpg | CC BY 4.0 (same Wellcome pattern) | Plutchik `fear` intense form |
| Smiling girl and man | Wikimedia Commons, ex-Wellcome | https://commons.wikimedia.org/wiki/File:Smiling_girl_and_man_from_Darwin%27s_Expression_of_Emotions..._Wellcome_L0049516.jpg | CC BY 4.0 (same Wellcome pattern) | Plutchik `joy` |
| Weeping children | Wikimedia Commons, ex-Wellcome | https://commons.wikimedia.org/wiki/File:Weeping_children_from_Darwin%27s_Expression_of_emotions...._Wellcome_L0049518.jpg | CC BY 4.0 (same Wellcome pattern) | Plutchik `sadness` |
| Hostile dog / Humble dog / Snarling dog | Wikimedia Commons, ex-Wellcome | `Hostile_dog..._Wellcome_L0049528`, `Humble_dog..._Wellcome_L0049530`, `Snarling_dog..._Wellcome_L0049522` (same Commons File: pattern) | CC BY 4.0 | Darwin's cross-species argument — good for the `expression-of-emotions` school itself, not for a human-emotion page |
| Full 1872 first edition (all plates, uncropped) | Internet Archive, Darwin Online | https://archive.org/details/darwin-online_1872_Expression_F1142 | No licence claimed by the uploader; content is 1872 and unambiguously PD | Source of record if you want to crop your own plate instead of using a pre-cropped Wellcome file |
| Full 1916 (D. Appleton) edition | Biodiversity Heritage Library | https://www.biodiversitylibrary.org/item/24064 (bibliographic record: https://doi.org/10.5962/bhl.title.4820) | **BHL states public domain outright, no attribution licence layered on** | Cleanest-licence fallback if the Wellcome CC BY claim below is a concern |

**Licence caveat — read before using any Wellcome-sourced Darwin plate.** Every
Darwin plate on Wikimedia Commons I found is tagged **CC BY 4.0**, attributed to
Wellcome Collection, not `{{PD-old}}` or CC0 — even though the underlying 1872
photographs and text have been public domain for well over a century. This is Wellcome
asserting a fresh copyright claim over its own *scan* of a public-domain 2D work. That
class of claim is legally contested (the US "Bridgeman v. Corel" line of reasoning holds
that a faithful photographic reproduction of a flat public-domain artwork creates no new
copyright), and Wellcome's own site states these images as CC BY-NC 4.0 in one place and
CC BY 4.0 on the Commons upload — the two aren't even consistent with each other. I did
**not** resolve this. Two honest paths forward, not a recommendation to pick one
silently:
1. **Use the Wellcome-sourced Commons files and credit Wellcome Collection** in
   `image_credit` / `_grammar_commons.attribution`, treating the CC BY tag as valid out
   of caution even though the underlying content is PD. Simplest, keeps the
   pre-cropped, well-labelled, high-resolution scans.
2. **Source instead from the Internet Archive or BHL copies**, which carry no
   attribution claim at all — but you'd be cropping your own plate images out of full
   page scans rather than using someone's already-cropped file, which is more work per
   image.

### 2. Duchenne, *Mécanisme de la physionomie humaine* (1862) — flag before using

Duchenne applied galvanic electrodes to isolated facial muscles — mostly of an elderly
patient with facial anaesthesia (a condition that let Duchenne stimulate him without
causing pain) — and photographed the resulting expressions to build a systematic atlas
of "which muscle makes which expression," on the theory that expressions map onto fixed,
universal muscular signatures. Darwin corresponded with Duchenne and reproduced several
of these photographs (as engravings) in the 1872 book, making Duchenne the direct
scientific ancestor of the Darwin grammar this repo already has. Available public-domain
scans, all National Gallery of Art originals, dated 1854–56, printed 1862:

| Subject | Direct URL (NGA) | Commons mirror | Licence |
|---|---|---|---|
| Face in repose | https://www.nga.gov/artworks/169260-face-repose | `File:Guillaume-Benjamin-Amant_Duchenne_(de_Boulogne),_Face_in_repose,_1854-1856,_NGA_169260.jpg` | **CC0 1.0** (verified on the Commons file page: "This file is made available under the Creative Commons CC0 1.0 Universal Public Domain Dedication") |
| Aggression, wickedness | NGA object 169269 (same URL pattern, id swapped) | `File:Guillaume-Benjamin-Amant_Duchenne_(de_Boulogne),_Aggression,_wickedness,_1854-1856,_NGA_169269.jpg` | CC0 1.0, same basis as above |
| Attention / Severity (paired) | NGA object 169268 | `File:...Attention_(left);_Severity,_aggression_(right),_1854-1856,_NGA_169268.jpg` | CC0 1.0 |

NGA's whole open-access programme is CC0 by policy (confirmed via nga.gov/artworks/free-images-and-open-access),
so the ~30 Duchenne photographs in the NGA collection (ids run roughly 169260–169291)
are the **cleanest-licence source in this entire document** — genuinely CC0, no
attribution-claim ambiguity like the Wellcome Darwin scans above.

**But licence-clean is not the same as use-clean, and that's the actual editorial
question.** These are documented experiments on a person who, by any modern informed-consent
standard, was not in a position to freely consent — an institutionalised patient whose
facial nerve condition is what made the experiments possible on him at all, subjected to
electrical stimulation for a researcher's taxonomy of expression. Two separate concerns,
both real:
- **Historical/medical-ethics concern**: this is the same category of 19th-century
  clinical photography (Charcot's hysteria patients at the Salpêtrière are the other
  famous case) that modern medical history treats as a cautionary example, not a neutral
  archive.
- **This library's own thesis concern**: Duchenne's entire project was to prove that
  each emotion has one fixed, universal muscular signature — literally the claim
  `README.md`'s "no fixed biological fingerprints for emotions" is written to complicate.
  Using these images uncritically as *illustration* (rather than as *historical
  argument being examined*) would visually assert the opposite of what the site's text
  says.

**Recommendation, offered as an editorial option rather than a decision made on the
maintainer's behalf:** if used at all, Duchenne photographs belong in the
`historical-scientific` branch (alongside Darwin) captioned as *what the universal-signature
argument looked like*, not dropped into a live Plutchik/NVC/DBT school page as neutral
illustration. A caption in the register the repo already uses for editorial framing
(`CLAUDE.md` → `Research note` / `Constructionist lens` sections) would do the work: name
the method, name the consent problem, name that this is the historical claim the
constructionist substrate revises. Silence would read as endorsement.

### 3. Pre-1800 diagrammatic/emblematic works (Fludd, Kircher)

Both are 17th-century, long past any copyright term in any jurisdiction; Wikimedia
Commons tags this whole space `{{PD-old-100}}` plus (on some files) `{{PD-Art}}`. I did
not find a case where a holding library layers a fresh licence claim on top, the way
Wellcome does for the Darwin plates above — these read as clean PD.

| Work | Artist/date | Source | Direct URL | Licence | Fits |
|---|---|---|---|---|---|
| *Integrae naturae speculum artisque imago* ("Mirror of nature and art" — the ape painting from nature) | Robert Fludd, *Utriusque Cosmi...*, 1617–19 | Wikimedia Commons | https://commons.wikimedia.org/wiki/File:Robert_Fludd,_Integra_naturae_speculum_artisque_imago.jpg | Public domain (`PD-old-100`) | Constellation root / "a map, not a discovery" framing — the emblem literally depicts art copying nature at one remove |
| Fludd's colour wheel | Robert Fludd, early 17th c. | Wikimedia Commons | https://commons.wikimedia.org/wiki/File:Fludd_color_wheel.jpg | Public domain (`PD-old-100`) | Visual echo for a Plutchik "wheel" page — NOT a scientific precursor to Plutchik, just a period wheel-diagram; caption must say so explicitly or it implies false lineage |
| "Diagram of the Human Mind" | Robert Fludd, 1619 | Wikimedia Commons / Public Domain Review | https://publicdomainreview.org/product/diagram-of-the-human-mind/ (Commons category: `Category:Robert_Fludd`) | Public domain | IFS/parts-work or Jungian archetypes page — a period attempt to map the mind's structure |
| Kircher's "Diagram of the names of God" | Athanasius Kircher, *Oedipus Aegyptiacus*, 1652–54 | Wikimedia Commons | https://commons.wikimedia.org/wiki/File:Kircher-Diagram_of_the_names_of_God.png | Public domain (`PD-old-100`, marked CC-PD-Mark on file page) | Constellation/root page — a hub-and-spokes diagram, visually similar to how the meta-grammar tree viewer renders branches |

### 4. Wikimedia Commons — physiognomy / phrenology (label as discredited)

Real Commons categories exist: `Category:Physiognomy`, `Category:Phrenology`,
`Category:Phrenological_charts` (https://commons.wikimedia.org/wiki/Category:Phrenology,
https://commons.wikimedia.org/wiki/Category:Physiognomy). Most material is
Wellcome-sourced 19th-century engravings, same CC BY 4.0-over-PD-content pattern as the
Darwin plates above.

| Work | Source | Direct URL | Licence | Fits |
|---|---|---|---|---|
| "Chart showing the basic elements of phrenology, physiognomy" | Wikimedia Commons, ex-Wellcome | https://commons.wikimedia.org/wiki/File:Chart_showing_the_basic_elements_of_phrenology,_physiognomy_Wellcome_V0009525.jpg | CC BY 4.0 (Wellcome pattern — see caveat under Darwin) | **Historical-scientific branch only**, captioned as a discredited 19th-century pseudoscience that nonetheless shaped how "reading" emotion from the body got imagined — never as a live illustration for any active school |

Phrenology and physiognomy claimed to read character and emotional disposition directly
off skull shape and facial structure — a much harder version of the "fixed universal
signature" claim than Duchenne's, and with an uglier history (it was used to justify
racial and class hierarchy). If used at all, it needs the heaviest labelling of anything
in this document: not "historical illustration," but "an illustration of a pseudoscience
this library does not endorse and is showing you specifically because it was
influential and wrong."

### 5. Non-Western sources (a requirement, not a nice-to-have)

**Sanskrit rasa tradition — the strongest fit found.** Rajput *Ragamala* ("garland of
melodies") paintings were explicitly designed to evoke a specific *rasa* (aesthetic
emotion) and *bhava* (mood) per Bharata Muni's *Natyashastra* — this is a textual
emotion-taxonomy tradition roughly two thousand years older than Plutchik's, illustrated
directly. Smithsonian's National Museum of Asian Art has digitised many, released CC0.

| Work | Date/school | Source | Direct URL | Licence | Fits |
|---|---|---|---|---|---|
| Gauri Ragini, folio from a Ragamala | Central India | Smithsonian NMAA | https://asia.si.edu/object/S2018.1.49/ | **CC0** ("in the public domain... can copy, modify, and distribute this work without contacting the Smithsonian") | A `rasa`-adjacent companion note on the substrate/constructionist page, or Plutchik `trust`/devotion |
| Bangal Ragini, from a Ragamala series | c. 1650, Malwa (Central Indian School) | Smithsonian NMAA | https://asia-archive.si.edu/object/F1930.81/ | CC0 (same programme) | Plutchik `anticipation`/longing — Ragamala ragas are often about waiting (for rain, for a lover) |
| Vilaval Ragini, from a Ragamala | c. 1690–95, Basohli | Smithsonian NMAA | https://asia-archive.si.edu/object/S2018.1.2 | CC0 | General rasa/mood illustration |
| Shri Raga, from the Chawand Ragamala | 1605, Mewar | Smithsonian NMAA | https://asia.si.edu/explore-art-culture/collections/search/edanmdm:fsg_F1991.1/ | CC0 | Devotional/heroic rasa |

**Noh masks (Japan).** Centuries-old carved objects; Tokyo National Museum has released
photographs to Wikimedia Commons tagged public domain (`CC-PD-Mark`/`PD-old-100`). Noh
performance theory itself is built around a small set of masks each keyed to a named
emotional/spiritual register (grief, malice, serenity, madness) — a non-Western,
non-facial-photograph precedent for "a small vocabulary of named affect states," which is
structurally close to what Plutchik's wheel and NVC's feelings-list are both doing.

| Mask | Register | Source | Direct URL | Licence |
|---|---|---|---|---|
| Ko-omote (young woman) | Serenity, youthful beauty | Tokyo National Museum, via Commons | https://commons.wikimedia.org/wiki/File:Ko-omote_(Noh_mask),_Tokyo_National_Museum_C-1551.jpg | Public domain |
| Yoroboshi (blind wandering priest) | Grief, disorientation | Tokyo National Museum, via Commons | https://commons.wikimedia.org/wiki/File:Yoroboshi_(Noh_mask),_Tokyo_National_Museum.jpg | Public domain |
| Shōjō (a spirit associated with sake/joy) | Joy, revelry | Tokyo National Museum, via Commons | https://commons.wikimedia.org/wiki/File:Shōjō_(Noh_mask),_Tokyo_National_Museum_C-1535.jpg | Public domain |

The Metropolitan Museum also holds Noh masks under its CC0 Open Access programme (e.g.
`metmuseum.org/art/collection/search/45501`, a Ko-omote mask) — I could not re-fetch
that specific object page directly (it returned a rate-limit error mid-session), but the
Met's general policy is unambiguous: everything the Met has designated public domain is
released CC0 (confirmed via `creativecommons.org/2017/02/07/met-announcement/` and
`metmuseum.org/press-releases/open-access-2017-news`), and an Edo/Muromachi-period carved
mask is public domain by age regardless. Re-confirm the individual object page before
use; I'm confident in the licence class, not in that specific URL still resolving
identically.

**Chinese Luohan (arhat) paintings.** Buddhist paintings of enlightened figures, a
tradition that specifically prized exaggerated, individualised facial expression —
laughing, scowling, ecstatic, wrathful — as a way of depicting spiritual states rather
than literal likeness. Smithsonian's Freer Gallery holdings, CC0.

| Work | Date/artist | Source | Direct URL | Licence | Fits |
|---|---|---|---|---|---|
| A Group of Luohan | Ding Yunpeng, 1613, Ming dynasty | Smithsonian NMAA (Freer) | https://asia-archive.si.edu/object/F1911.284/ | **CC0** (verified: "in the public domain (free of copyright restrictions)... can copy, modify, and distribute this work without contacting the Smithsonian") | Jungian archetypes / parts-work branch — a tradition of depicting distinct inner "characters" |
| Sixteen Luohan | Ming dynasty | Smithsonian NMAA (Freer) | https://asia-archive.si.edu/object/F1960.1/ | CC0 (same programme) | Same |
| Luohan Meditating in a Grotto | formerly attrib. Guanxiu, Yuan dynasty (dated 1345) | Smithsonian NMAA (Freer) | https://asia-archive.si.edu/object/F2002.4/ | CC0 (same programme, not individually re-verified) | Constructionist/substrate page — stillness rather than a named emotion |

**Ukiyo-e expressive faces (Japan).** Utagawa-school prints of caricatured, highly
individuated faces exist in quantity. Art Institute of Chicago lists a Yoshiiku memorial
portrait of Kuniyoshi as CC0 in search results, but I could not independently re-fetch
`artic.edu/artworks/103332` — it returned a 403 mid-session. **Treat this one lead as
unverified** until someone loads the page directly; Art Institute's general Open Access
programme is CC0-based, so the licence class is plausible, but I have no first-hand
confirmation for this specific object.

### 6. Museum open-access programmes — general policy, verified where stated

| Institution | Genuine CC0? | Verified how | Notes |
|---|---|---|---|
| The Met | **Yes, for PD-designated works** | `creativecommons.org/2017/02/07/met-announcement/`, `metmuseum.org/press-releases/open-access-2017-news` — CC0 since Feb 2017, 375,000+ images at launch | Individual object pages 429'd mid-session; policy-level confirmation only |
| Smithsonian (all units, incl. NMAA/Freer used above) | **Yes** | Object-page text fetched directly for two NMAA items (`F1911.284`, and the earlier NGA/Duchenne cross-check pattern) — explicit "in the public domain... without contacting the Smithsonian" language | Open Access programme launched 2020; this is the strongest, most consistently CC0 source in this whole document |
| National Gallery of Art (US) | **Yes** | Object-page text confirms CC0 1.0 directly (Duchenne file above); policy also stated at `nga.gov/artworks/free-images-and-open-access` | Also donates its open-access set to Wikimedia Commons directly |
| Art Institute of Chicago | Yes, by stated policy | Not independently re-verified this session (see ukiyo-e caveat above) | Re-check before use |
| Rijksmuseum | **Functionally yes, but not a formal CC0 legal tool** | Rijksmuseum's own language is "copyright and royalty free" / "public domain," via Rijksstudio, not a CC0 badge on every record | Treat as PD-equivalent for public-domain-era works; worth a specific per-image check if the maintainer wants the formal CC0 mark |
| Yale Center for British Art | **Public domain, not badged CC0** | `britishart.yale.edu/using-images` — "may be downloaded and used without restrictions" for PD-designated works, but the Center doesn't use the CC0 name | Same practical effect, different label; British portraiture is a plausible source for 18th–19th c. "sentiment/expression" genre painting if that's ever wanted, not searched in depth this session |

---

## What NOT to use

- **In-copyright therapy-book illustrations.** Anything from Rosenberg's NVC materials,
  Johnson's EFT books, Linehan's DBT worksheets/handouts, or Brown's *Atlas of the
  Heart* — `CLAUDE.md` already bars quoting their *text*; their diagrams and cover art
  are equally in copyright and equally off-limits.
- **Stock photography of faces.** Beyond the licensing question, stock "emotion" photo
  sets are themselves built on the assumption of one canonical, photographable face per
  emotion — visually reinforcing the fixed-signature claim this library exists to
  complicate.
- **AI-generated faces.** No provenance, no historical position, and (per the
  maintainer's general practice in this repo family) not how illustration is sourced
  here.
- **Anything visually asserting a fixed, universal facial signature per emotion —
  including some of the historical material recommended above, used carelessly.** This
  is the real tension in this document, worth stating plainly: Darwin's plates and
  Duchenne's photographs were *made* to argue exactly the claim `README.md` says the
  2019 Barrett et al. meta-analysis found no support for. That doesn't make them
  unusable — they're the historical record of how the universal-signature idea got
  built, which is on-topic for the `historical-scientific` branch — but it does mean
  they can't be dropped into a Plutchik or NVC card as neutral decoration without a
  caption doing the work of framing them as *argument*, not *evidence*. A bare Darwin
  "Terror" plate captioned only "Fear" reads as confirming exactly the fingerprint claim
  the site's own front page spends four paragraphs complicating. The same plate
  captioned "Darwin's 1872 case for a universal terror-face — the claim this library's
  constructionist substrate revises" does the opposite. The image can stay the same; the
  caption is load-bearing.
- **Phrenology/physiognomy charts presented without the pseudoscience label** — see §4
  above.
- **Duchenne photographs presented without the consent caveat** — see §2 above.

---

## Shortlist — homepage and Plutchik school (10 images)

Every entry below already appears, with fuller citation, in the tables above.

| # | Image | Direct URL | One-line rationale |
|---|---|---|---|
| 1 | Fludd, *Integrae naturae speculum artisque imago* | https://commons.wikimedia.org/wiki/File:Robert_Fludd,_Integra_naturae_speculum_artisque_imago.jpg | Homepage hero candidate — a 1617 emblem of art-copying-nature-at-one-remove, which is a near-literal picture of this library's "every school is an interface" thesis, replacing the tarot World card currently there |
| 2 | Kircher, "Diagram of the names of God" | https://commons.wikimedia.org/wiki/File:Kircher-Diagram_of_the_names_of_God.png | Constellation-root page — a period hub-and-spokes diagram, visually apt for the meta-grammar tree of schools |
| 3 | Ragamala, Bangal Ragini | https://asia-archive.si.edu/object/F1930.81/ | Homepage or "about" — non-Western anchor image, CC0-clean, directly on-theme (a rasa/bhava painting on a library that must not be Euro-American only) |
| 4 | Darwin, "Grief" plate | https://commons.wikimedia.org/wiki/File:Grief,_from_Darwin%27s_Expressions_of_Emotions_in_Man....._Wellcome_L0049517.jpg | Plutchik `sadness`/`grief` card — captioned as historical argument, not diagnosis (see "what NOT to use") |
| 5 | Darwin, "Terror" plate | https://commons.wikimedia.org/wiki/File:Terror,_from_Darwin%27s_Expression_of_Emotions_in_Man...._Wellcome_L0049512.jpg | Plutchik `fear`/`terror` card, same caveat/caption discipline as #4 |
| 6 | Darwin, "Disdain and disgust" plate | https://commons.wikimedia.org/wiki/File:Disdain_and_disgust_from_Darwin%27s_Expression_of_Emotions..._Wellcome_L0049514.jpg | Plutchik `disgust` card |
| 7 | Darwin, "Surprise and distress" plate | https://commons.wikimedia.org/wiki/File:Surprise_and_distress_in_Darwin%27s_Expression_of_Emotions..._Wellcome_L0049511.jpg | Plutchik `surprise` card |
| 8 | Ragamala, Gauri Ragini | https://asia.si.edu/object/S2018.1.49/ | Plutchik `trust` — a devotional/companionate mood painting, CC0, avoids the "every emotion is Darwin/Duchenne" monoculture |
| 9 | Noh mask, Shōjō | https://commons.wikimedia.org/wiki/File:Shōjō_(Noh_mask),_Tokyo_National_Museum_C-1535.jpg | Plutchik `joy` — a named-mask tradition rather than a photographed human face, deliberately breaking the "one universal face" visual pattern |
| 10 | Noh mask, Yoroboshi | https://commons.wikimedia.org/wiki/File:Yoroboshi_(Noh_mask),_Tokyo_National_Museum.jpg | Plutchik `sadness` alternate, or the constellation-root page — grief rendered as a mask (a made thing) rather than a captured face, which is closer to this library's "interface, not discovery" framing than any photograph could be |

Deliberately not included: any Duchenne photograph. They're licence-clean (CC0) and
thematically exact, but given the consent history and the fact that Plutchik already has
nine other candidates above that don't carry that history, the honest call is to reserve
Duchenne for the `historical-scientific` branch (alongside Darwin, as his acknowledged
source) rather than the front-facing Plutchik cards — that's an editorial recommendation,
not a decision made on the maintainer's behalf; see §2 above for the full reasoning to
weigh.

---

## Open questions I could not resolve

1. **Wellcome's CC BY 4.0 claim over the Darwin plates** — legally contestable, not
   resolved here. See the caveat under §1.
2. **Art Institute of Chicago's Kuniyoshi/Yoshiiku CC0 status** — plausible by policy,
   not independently re-confirmed (page 403'd mid-session).
3. **Individual Met Noh-mask object pages** — policy-level CC0 is solid; the specific
   URLs given by search were not independently re-fetched (rate-limited mid-session).
4. **Whether to rehost any of this to R2 at all.** Given the disk-space constraint noted
   in the root `CLAUDE.md`, direct Wikimedia/museum linking (no local copy, no rehost) is
   the lower-risk default; `scripts/rehost_to_r2.py` exists for later if a specific image
   needs to survive a Commons rename/deletion or needs a controlled crop.
