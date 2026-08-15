# Music sources — research notes

**Status: research only. Nothing in this repo except this file was changed. No audio was
downloaded, uploaded, or attached to any grammar.** This is a sourcing map for whoever does
the audio pass, following the same principle already used for artwork
(`docs/ILLUSTRATION-SOURCES.md`, `docs/SOURCES-AND-CAVEATS.md` §2): each school accompanied,
where possible, by sound contemporary to its own author and place. Every URL below was
checked at research time (2026-08-15); re-check licences at the point of use — file pages on
Commons and IMSLP can be re-tagged, and archive.org lending items can be pulled.

## Why this exists

None of the `schools/*/grammar.json` files in this repo (eighteen school folders at research
time, including the new `affektenlehre` this document accompanies) carry a `performance`
object or a `metadata.audio` field yet — confirmed by grepping every grammar file for both.
`schools/affektenlehre/` — a Baroque school literally built on the claim that music
represents affect — is the sharpest possible argument for finally doing this work, but the
same logic applies to every school that has a documented period musical tradition: Gregorian
chant for Aquinas, guqin for the Chinese qíng school, raga for rasa, and so on. This document
maps where a genuinely free recording of each could come from, states the one licensing trap
that will quietly undermine the whole effort if missed, and reports exactly what this repo's
existing chassis (`viewers/perform.html`, `viewers/sequence.html`) can and cannot play.

---

## 1. The trap, stated plainly

**A composition being centuries old does not make a modern performance of it public domain.**
Copyright in music has two independent layers:

1. **The composition** — the notes themselves. Bach, Monteverdi, Purcell, Dowland, and the
   Gregorian chant repertory are all long out of copyright everywhere; nobody owns "Dido's
   Lament" as a piece of music.
2. **The recording** — a specific performance, fixed in a specific take, by specific
   performers, on a specific date. *This* is almost always separately copyrighted, on its own
   term, regardless of how old the underlying composition is. A 2015 recording of a 1689 aria
   is a 2015 copyrighted work layered on top of a public-domain composition. The composition's
   age tells you nothing about the recording's rights status.

This is not a hypothetical risk for this project specifically — it showed up twice in the
course of this research, both times on pieces already named as candidates for this library:

- **IMSLP's own recordings of Purcell's Dido's Lament** are tagged **CC BY-NC** (non-commercial)
  or **CC BY-NC-ND** (non-commercial, no derivatives). Both fail this library's own licence —
  `docs/SOURCES-AND-CAVEATS.md` §1 states plainly that a CC-BY-SA-4.0 grammar must permit
  *commercial* reuse and remixing downstream. An NC-tagged recording cannot legally be folded
  into a CC-BY-SA-4.0 grammar; it is a dead end here even though it costs nothing to download.
- **Archive.org hosts several Hildegard von Bingen recordings** (Sequentia's *Canticles of
  Ecstasy*, Gothic Voices' *A Feather on the Breath of God*), but these are commercial 1990s
  record-label releases made available for streaming/lending, not public-domain or
  openly-licensed audio. Archive.org hosting a recording is not evidence of its rights status
  either way — check the item's own stated rights, every time, the same way
  `docs/ILLUSTRATION-SOURCES.md` insists on checking each image's own file page rather than
  trusting the hosting site's reputation.

**The corollary for very old traditions specifically (rasa, guqin):** the fact that a raga or
a guqin melody may be a thousand years old does not help at all if every *recording* of it
available online is a 20th- or 21st-century commercial release, which is the normal case (see
§3, rasa row).

---

## 2. Where genuinely free recordings actually live

| Source | What it's actually good for | The catch |
|---|---|---|
| **IMSLP** (imslp.org) | Scores — essentially unlimited PD sheet music for anything pre-1929ish. Also hosts a real but small library of user-submitted **recordings** on individual work pages (a "Recordings" or "Compositions/Performances" section, separate from the score files). | Recording licences on IMSLP vary file by file — commonly **CC BY-NC** or **CC BY-NC-ND**, which do not clear this library's commercial-reuse bar. Check the specific licence tag on the specific audio file; do not assume IMSLP's PD reputation (earned on scores) carries over to its recordings. |
| **Musopen** (musopen.org) | A nonprofit specifically formed to fund and release **public-domain and CC0/CC-BY-SA recordings** of classical repertoire — the one source on this list built for exactly this problem. Their 2012 Kickstarter-funded collection (mirrored on archive.org, see below) is stated **Public Domain Mark 1.0**. | Coverage skews hard toward 18th–19th century Classical/Romantic orchestral repertoire (Beethoven, Brahms, Mozart, Schubert) — the collection checked for this document contains **no** Dowland, Monteverdi, Purcell, or Gregorian chant. Good for `darwin-expression`'s Victorian-adjacent needs; weak-to-empty for the Baroque-and-earlier schools this document was mainly asked to cover. Musopen's live site (musopen.org) blocked automated fetches during this research; browse it directly rather than trusting this document's coverage claim as final. |
| **Wikimedia Commons audio** (commons.wikimedia.org, `Category:Audio files of…`) | The strongest hit rate in this research by far. Commons requires every upload to carry a real free licence (PD, CC0, CC BY, CC BY-SA, GFDL) stated on the file's own page, and a meaningful number of contributors have uploaded their own real performances — not synthesized MIDI — of exactly this repertoire. **Three of this document's four verified top candidates (§3) are Commons audio files.** | Quality and completeness are uneven — these are volunteer recordings (a solo singer, a chant enthusiast, a guqin player recording at home), not professional label releases, and most pieces simply have no Commons recording at all. Always read the individual file page; Commons audio categories mix PD self-releases with CC BY-SA and GFDL-tagged files, and the exact tag changes what downstream reuse is permitted. |
| **archive.org** | Two very different things live here under one domain: (a) **Musopen's own PD-tagged collection**, mirrored as a bulk download (`archive.org/details/MusopenCollectionAsFlac`); (b) the **lending library** of commercial LPs/CDs digitized for streaming or two-week borrowing — the Hildegard example above. Only (a) is usable here. | Nothing on the item page visually distinguishes (a) from (b) at a glance; the rights statement has to be read every time. A "Free Download, Borrow, and Streaming" item is very often (b). |

---

## 3. Per-school candidates

Verified = an actual HTTP fetch of the file's own Commons/IMSLP/archive.org page was made
during this research and the licence tag transcribed directly from it, not inferred.

### `greek-pathe` — the Seikilos epitaph and the Delphic Hymns

| Candidate | URL | Licence (verified) | Note |
|---|---|---|---|
| Epitaph of Seikilos, sung reconstruction | https://commons.wikimedia.org/wiki/File:%CE%9F_%CE%95%CF%80%CE%B9%CF%84%CE%AC%CF%86%CE%B9%CE%BF%CF%82_%CF%84%CE%BF%CF%85_%CE%A3%CE%B5%E1%BF%96%CE%BA%CE%B9%CE%BB%CE%BF%CF%85_-_Epitaph_of_Seikilos.ogg | **CC BY-SA 2.5** — attribution required. Recorded and uploaded by a Wikimedia contributor (username Byz), Koine Greek pronunciation, 50 seconds, 2006. The file's own description notes one mispronounced word near the start. | **This is one of this document's top candidates** (see below) — the oldest surviving complete notated composition, and a rare case where a direct, checkable, free recording actually exists. |
| Epitaph of Seikilos, MIDI realization | https://commons.wikimedia.org/wiki/File:Seikilos.mid | Public domain (stated on file page) | A synthesized fallback if a sung/attributed recording is undesirable — no attribution needed, but it is a MIDI rendering, not a performance. |
| Delphic Hymns (2nd c. BCE, to Apollo) | — | Not found | No free recording located in the time available. The Delphic Hymns exist in modern scholarly/period-instrument recordings (e.g. by ensembles specializing in ancient Greek music), but every one found in this research is a commercial release; treat as an open gap, not a solved candidate. |

### `aquinas-passions` — Gregorian chant, Hildegard of Bingen

| Candidate | URL | Licence (verified) | Note |
|---|---|---|---|
| *Dies Irae* (Requiem sequence, Gregorian chant) | https://commons.wikimedia.org/wiki/File:Dies.irae.ogg | **Public domain** — the uploader (username Membeth) states on the file page: "I, the copyright holder of this work, release this work into the public domain." Solo voice, 7:14, uploaded 2010. | Clean PD, no attribution legally required (crediting the tradition and the specific Commons file is still good practice). |
| *Kyrie eleison*, *Ave Maria*, *Pater Noster* and other Schola Gregoriana recordings | https://commons.wikimedia.org/wiki/Category:Audio_files_of_Gregorian_chant | Varies by file — the category page itself states "files are available under licences specified on their description page." Not blanket-verified; check each file individually. | 43 files in this category at research time — the richest single pool of freely-licensed period-adjacent chant found in this research. Worth a dedicated pass rather than picking one file blind. |
| Hildegard of Bingen — Sequentia's *Canticles of Ecstasy*, Gothic Voices' *A Feather on the Breath of God* | archive.org (multiple items) | **Commercial, not free** — see §1. Flagged here specifically as the trap example, not a usable candidate. | If a genuine Hildegard performance is wanted, it will need a purpose-built free recording (a Commons upload, or a new performance commissioned/recorded for this project) — none was found free in this research. |

### `affektenlehre` / `descartes-passions` — Dowland, Monteverdi, Purcell

| Candidate | URL | Licence (verified) | Note |
|---|---|---|---|
| Monteverdi — *Lamento della Ninfa* | https://commons.wikimedia.org/wiki/File:Monteverdi_-_Lamento_della_Ninfa.ogg | **CC BY-SA 3.0 / CC BY 2.5 / GFDL** (triple-licensed, as stated on the file page) | **The single best find in this whole research pass.** A full professional concert recording — Daphne Ramakers (soprano, Ninfa), Brenden Gunnell (tenor), Wiard Witholt (baritone), Dennis Wilgenhof (bass), Israel Golani (theorbo), Tal Canetti (cello), conducted by Trisdee na Patalung — recorded live at the Concertgebouw, Amsterdam, 22 December 2006, uploaded 2007. This is the exact piece named in the `affektenlehre` `lamento` item's own `Definition` section. |
| John Dowland — "Fine knacks for ladies" (Second Booke of Songs, 1600) | https://commons.wikimedia.org/wiki/File:John_Dowland_--_Fine_knacks_for_ladies.opus | **CC BY 3.0 Unported** — attribution required | Collegium Vocale performance, 2:27. Not the melancholy-identity pieces (*Flow My Tears*, *Semper Dowland semper dolens*) named in the brief, but the same composer, freely licensed, and directly usable. |
| John Dowland — "Now, O now I needs must part" | https://commons.wikimedia.org/wiki/File:John_Dowland_--_Now,_o_now_I_needs_must_part.opus | **CC BY 3.0 Unported** | Same performer/ensemble as above, 4:14; a parting/sorrow text, closer in affect to the lament/melancholy cluster than "Fine knacks." |
| Purcell — *Dido's Lament* ("When I am laid in earth") | IMSLP, multiple recordings on the work page | **CC BY-NC / CC BY-NC-ND** | **The trap case, see §1.** Every recording found on IMSLP's own Dido and Aeneas page is non-commercial-licensed and therefore unusable here. No free (BY, BY-SA, CC0, or PD) recording of this specific aria was located in the time available — an open gap, not a solved candidate. |
| Purcell — miscellaneous odes, anthems, and instrumental works | https://commons.wikimedia.org/wiki/Category:Audio_files_of_music_by_Henry_Purcell | Varies by file, generally CC-family | Not the Dido material specifically, but confirms Purcell is otherwise reasonably well represented on Commons if the Dido gap needs a same-composer substitute (e.g. music from the same funeral-music register as *Music for the Funeral of Queen Mary*). |

### `humoral-temperaments` — Dowland again, period-keyed temperament music

The two Dowland tracks above (§ affektenlehre row) apply equally here — Dowland's own
self-fashioned melancholic persona ("Semper Dowland, semper dolens" — "always Dowland, always
doleful," the motto he set to music himself) is the most direct musical-historical link
between a real Renaissance/Baroque composer and the humoral melancholic type this school
already covers. No further period-temperament-specific recording (e.g. music explicitly
composed *about* the four humours as a set) was found in this research; that remains an open
gap.

### `chinese-qing` — guqin repertoire and its affective associations

| Candidate | URL | Licence (verified) | Note |
|---|---|---|---|
| Guqin — *Yangguan Sandie* (陽關三疊, "Three Refrains on the Yang Pass Theme") | https://commons.wikimedia.org/wiki/File:Guqin-Yangguan_Sandie.ogg | **CC BY-SA 3.0 Unported / GFDL** (dual-licensed) | **Third of this document's top candidates.** A real, documented guqin performance — recorded by a Commons contributor (username Charles R Tsua) in Birmingham, UK, 6 October 2013, played from the score in the historical instruction manual *Qínxué Rùmén* (1867). *Yangguan Sandie* is a traditional farewell piece, based on a Wang Wei poem, with a documented affective association (parting, sorrow) that long predates any specific recording — exactly the kind of tradition-carries-the-affect case this school needs. |

### `rasa` — raga–rasa associations

No free recording candidate is offered here, deliberately. Raga–rasa associations are
extensively documented in the musicological and traditional literature (which the `rasa`
school itself should cite in prose, independent of audio), but every raga recording located in
preliminary searches for this document was a commercial release by a named performing artist —
exactly the pattern the brief warned about: an ancient tradition whose actual audio record is
almost entirely still in copyright. This is worth stating as a finding in its own right rather
than papering over with a weak candidate: **`rasa` is very likely the hardest of these seven
schools to source audio for honestly**, and may be better served for now by citing the
tradition in prose (as the grammar already does) than by attaching a specific recording that
overstates how free the available audio actually is.

### `darwin-expression` — Victorian-era material

No single verified candidate is offered here either, but the path is the more promising of the
two open schools: Musopen's PD-tagged 2012 collection (archive.org mirror,
`archive.org/details/MusopenCollectionAsFlac`) does cover 19th-century repertoire (Brahms,
Schubert, and others contemporary with or close to Darwin's lifetime, 1809–1882) — unlike the
Baroque-and-earlier schools above, this is a case where the *right kind* of free source exists
and simply needs a specific-work pass rather than a new-source search.

---

## Top 3 immediately-usable candidates (HTTP-checked)

Direct URLs below were resolved from each file's `Special:FilePath` redirect and confirmed
`200 OK` by an actual HTTP request during this research (not guessed from the filename
pattern) — this matters because Wikimedia's hash-bucket path (the `/4/41/`, `/6/60/`-style
folder) cannot be predicted from the filename alone.

1. **Monteverdi, *Lamento della Ninfa*** —
   https://upload.wikimedia.org/wikipedia/commons/4/41/Monteverdi_-_Lamento_della_Ninfa.ogg
   (file page: https://commons.wikimedia.org/wiki/File:Monteverdi_-_Lamento_della_Ninfa.ogg,
   HTTP 200 confirmed) — CC BY-SA 3.0 / CC BY 2.5 / GFDL. A full professional concert
   recording of the exact piece named in `schools/affektenlehre/grammar.json`'s `lamento`
   item.
2. **Epitaph of Seikilos, sung reconstruction** —
   https://upload.wikimedia.org/wikipedia/commons/b/b6/%CE%9F_%CE%95%CF%80%CE%B9%CF%84%CE%AC%CF%86%CE%B9%CE%BF%CF%82_%CF%84%CE%BF%CF%85_%CE%A3%CE%B5%E1%BF%96%CE%BA%CE%B9%CE%BB%CE%BF%CF%85_-_Epitaph_of_Seikilos.ogg
   (file page: https://commons.wikimedia.org/wiki/File:%CE%9F_%CE%95%CF%80%CE%B9%CF%84%CE%AC%CF%86%CE%B9%CE%BF%CF%82_%CF%84%CE%BF%CF%85_%CE%A3%CE%B5%E1%BF%96%CE%BA%CE%B9%CE%BB%CE%BF%CF%85_-_Epitaph_of_Seikilos.ogg,
   HTTP 200 confirmed) — CC BY-SA 2.5. The oldest surviving complete notated composition, for
   `greek-pathe`.
3. **Guqin, *Yangguan Sandie*** —
   https://upload.wikimedia.org/wikipedia/commons/6/60/Guqin-Yangguan_Sandie.ogg (file page:
   https://commons.wikimedia.org/wiki/File:Guqin-Yangguan_Sandie.ogg, HTTP 200 confirmed) —
   CC BY-SA 3.0 / GFDL. A documented farewell/parting piece from the guqin repertoire, for
   `chinese-qing`.

(Honourable mention: *Dies Irae* Gregorian chant, plain public domain, for `aquinas-passions` —
https://upload.wikimedia.org/wikipedia/commons/f/f2/Dies.irae.ogg (file page:
https://commons.wikimedia.org/wiki/File:Dies.irae.ogg, HTTP 200 confirmed) — held out of the
top three only because it is a solo amateur recording rather than a full ensemble performance
like the other three.)

**The composition-vs-recording trap, restated once more because it is the single most
important sentence in this document:** every one of the four candidates above was chosen
*because* its specific recording — not just its centuries-old composition — carries a
free licence stated on its own file page. A work being old is necessary but nowhere near
sufficient; the recording has to clear the bar on its own.

---

## 4. How the chassis would carry it

This repo already ships two players, and they are built for genuinely different hosting
models — reading their actual source (`viewers/perform.html`, `viewers/sequence.html`) rather
than just `GRAMMAR_FORMAT.md`'s description matters here, because the two diverge in ways the
format doc alone doesn't make obvious.

### `viewers/sequence.html` — YouTube only

Built entirely on the YouTube IFrame API. Each `segment`-category item needs
`metadata.youtube_video_id` (or a parseable `metadata.youtube_url`); `performance.start_sec` /
`performance.end_sec` crop the embedded player to that range, and `performance.video_visible:
false` swaps in a static cover image (`performance.cover_image_url`, falling back to the
YouTube thumbnail) for audio-only playback. **This viewer cannot play a directly-hosted audio
file at all** — there is no `<audio>` element in it, only the YouTube embed. None of the
Commons/IMSLP/Musopen candidates in §3 are YouTube videos, so this viewer is not the target for
any of them as-is, unless a candidate is separately re-findable as an actual YouTube upload
(some Commons audio does get re-uploaded to YouTube by libraries or the original uploader —
worth checking case by case, but not assumed here).

### `viewers/perform.html` — one shared audio track, many timestamped items

This is the viewer that actually plays plain hosted audio files (Wikimedia OGG/Opus, R2, or
any HTTPS URL), and it is the right target for the candidates above — with one real structural
constraint. Per `recording/docs/performance-grammar.md` and the live source: the grammar
**root** carries a single `metadata.audio` URL; the page loads that one `<audio>` element and
drives a single shared clock from it. Every item in `items[]` is treated as a **passage within
that one track** — `performance.start_sec` marks where the passage begins inside the shared
file, `performance.end_sec` is read for cropping, `performance.video_visible: false` is the
convention for "audio + still image, not video," and `performance.overlays[]` can carry timed
caption text over the item's `image_url`. This is exactly the model `GRAMMAR_FORMAT.md`
documents under "Audio karaoke mode (`words`)" for a narrated audiobook: **one track, many
items marking different ranges of it — not one independently-hosted file per item.**

**The concrete consequence for this document's candidates:** the four pieces in §3's top list
are four *different* audio files from four *different* sources (Monteverdi, Seikilos, guqin,
chant) — not four passages of one shared recording. `perform.html` as it stands has no field
for "this item's own independent audio URL, different from the grammar's" — only the one
grammar-root track. Two honest ways to attach these without inventing anything silently:

1. **One school, one candidate, one small `sequence` grammar per piece** — e.g. a tiny
   `affektenlehre`-adjacent sequence grammar whose `metadata.audio` *is* the Monteverdi OGG
   URL directly, with a single item spanning `start_sec: 0` to the file's actual length. This
   works today, with zero chassis changes, and matches how `recording/performances/
   death-across-the-centuries.json` is structured (one grammar, one shared track). It does mean
   one extra small grammar file per attached piece rather than attaching audio inline to the
   school's own `grammar.json` items.
2. **If attaching genuinely different audio per item within a single grammar becomes a real,
   recurring need** (multiple pieces under one school, not one), that is a legitimate small
   gap in the current chassis — worth raising with the maintainer as an additive field (e.g.
   an item-level audio-URL override alongside the existing grammar-root `metadata.audio`)
   rather than a new parallel structure, per this repo's own "consolidate, don't multiply"
   rule (`CLAUDE.md`). This document flags the gap; it does not resolve it, and no such field
   should be invented without the maintainer's sign-off.

Either way, **the four verified URLs in §3 are ready to use as-is** — they are direct,
stable, HTTPS-reachable file URLs (Wikimedia's `upload.wikimedia.org` hosting, the same
pattern `schools/*/grammar.json` already uses for images) and need no rehosting to be linked
from a `metadata.audio` field.

---

## 5. What not to do

- **Don't reach for a pop song merely because its title names an emotion.** A song called
  "Melancholy" or "Joy" contributes nothing to this project even if it happens to be free —
  the entire point of every school in this library is that a *specific tradition* built its
  *own* conventionalized means of representing an affect (a ground bass, a mode, a raga, a
  guqin gesture). A modern song's title matching an English emotion word is coincidence, not
  evidence of a tradition; it would be the audio equivalent of illustrating Aquinas's *timor*
  with a random modern photo of someone looking scared.
- **Don't imply a piece of music *is* an emotion, full stop.** This library's own substrate
  (`CLAUDE.md` rule 1) holds that there are no fixed biological fingerprints for emotion and
  every school here is a working interface, not a discovery. The same caution applies to
  music: Dowland's lute songs represent melancholy *within Renaissance English convention*;
  they are not evidence that a descending phrase makes anyone, anywhere, actually feel sad.
  Pairing a school with period-appropriate audio should illustrate how *that tradition* built
  its own musical vocabulary for feeling — never suggest the pairing proves the feeling is
  universal or that the music working on a period audience means it works the same way on a
  present-day listener.
- **Don't treat an old composition and a free recording as the same fact.** Restated one final
  time because it is the error most likely to slip through review: check the *specific
  recording's* licence on its *own* page, every time, regardless of how confidently public
  domain the underlying composition is.
- **Don't assume a hosting site's general reputation tells you a specific file's rights
  status.** IMSLP is overwhelmingly PD for scores and mixed for recordings; archive.org hosts
  both genuinely free collections and paywalled-adjacent commercial lending items under one
  domain. Read the file's own page.
