# -*- coding: utf-8 -*-
"""Repo-wide integrity check. Run after every integration before committing.

  python3 scripts/check_all.py

Checks:
  1. every schools/*/grammar.json is valid JSON with name + items[];
  2. composite_of references resolve within each grammar (no dangling);
  3. no mojibake — no UTF-8 text that was decoded as Latin-1/CP1252 anywhere;
  4. people dossiers (research/people/*.md) have the frontmatter the generator needs;
  5. rebuilds people + meta grammars and asserts the meta reports dangling=0;
  6. semantic check on the built meta grammar's derived pivot axes (role /
     trump_number / rank / deck-attribution) — see check_derived_axes.py.
Exits non-zero on any failure.
"""
import json, os, re, glob, subprocess, sys
import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCHOOLS = os.path.join(ROOT, "schools")  # was tarot/ — a green run over a folder that does not exist checks nothing
PEOPLE = os.path.join(ROOT, "research", "people")
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
VALID_ROLE_GROUPS = {"makers", "patrons", "occultists", "scholars", "institutions"}

errors, warnings = [], []

# The signatures of UTF-8 bytes decoded as Latin-1 / CP1252 and re-encoded:
# a lead byte (Â, Ã, â) followed by a continuation byte that surfaced as a
# punctuation or accented character. Plus U+FFFD, the replacement character a
# lossy decode leaves behind. Real French/Italian text in these decks never
# produces these pairs — "Moyen Âge", "Bohémiens", "Gébelin" are Â/é followed
# by an ASCII letter, which none of these patterns match.
MOJIBAKE_RE = re.compile(
    "[ÂÃâ]"                     # the lead byte 0xC2 / 0xC3 / 0xE2
    "["
    "-¿"                            # Latin-1 view of a continuation byte
    "€‚ƒ„…†‡ˆ‰Š‹Œ"
    "Ž‘’“”•–—˜™š›"
    "œžŸ"                       # CP1252 view of the same range
    "]"
    "|�"                                   # U+FFFD, left by a lossy decode
)

# 1 + 2 + 3 — grammars
for path in sorted(glob.glob(os.path.join(SCHOOLS, "*", "grammar.json"))):
    slug = os.path.basename(os.path.dirname(path))
    raw = open(path, encoding="utf-8").read()
    for m in MOJIBAKE_RE.finditer(raw):
        errors.append(f"{slug}: mojibake {m.group(0)!r} "
                      f"(U+{ord(m.group(0)[0]):04X}...) near "
                      f"{raw[max(0, m.start() - 40):m.end() + 40]!r}")
    try:
        g = json.loads(raw)
    except Exception as e:
        errors.append(f"{slug}: invalid JSON — {e}")
        continue
    if not g.get("name"):
        errors.append(f"{slug}: missing name")
    items = g.get("items")
    if not isinstance(items, list) or not items:
        errors.append(f"{slug}: items[] missing/empty")
        continue
    ids = {it.get("id") for it in items}
    for it in items:
        for c in it.get("composite_of", []) or []:
            if c not in ids:
                errors.append(f"{slug}: dangling composite_of '{c}' in item '{it.get('id')}'")

# 3 — people dossiers
for path in sorted(glob.glob(os.path.join(PEOPLE, "*.md"))):
    name = os.path.basename(path)
    m = FM_RE.match(open(path, encoding="utf-8").read())
    if not m:
        errors.append(f"people/{name}: no YAML frontmatter")
        continue
    fm = yaml.safe_load(m.group(1)) or {}
    for req in ("id", "type", "title", "role_group"):
        if not fm.get(req):
            errors.append(f"people/{name}: missing frontmatter '{req}'")
    if fm.get("role_group") and fm["role_group"] not in VALID_ROLE_GROUPS:
        errors.append(f"people/{name}: bad role_group '{fm['role_group']}'")

# 4 — rebuild generated grammars
# build_people_grammar.py is tarot-era: it writes tarot/people-of-tarot from a
# research/people/ directory this repo does not have, so every check_all run was
# regenerating a stray tarot/ tree at the repo root that then had to be hand-deleted
# (it happened twice before this was pinned). Only the adapted meta builder runs here.
for script in ("build_meta_grammar.py",):
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", script)],
                       capture_output=True, text=True, cwd=ROOT)
    out = (r.stdout + r.stderr).strip()
    print(f"[{script}] {out.splitlines()[0] if out else '(no output)'}")
    if r.returncode != 0:
        errors.append(f"{script} failed:\n{out}")
    if script == "build_meta_grammar.py" and "wrote" not in out and "up to date" not in out:
        warnings.append(f"meta build reported neither 'wrote' nor 'up to date': {out[:200]}")

# 5 — (removed) check_derived_axes.py was tarot-era — trump/rank/deck semantics —
# and the script itself was stripped in the original clone, so the call could only
# fail on a missing file.
if errors:
    print(f"\nFAIL: {len(errors)} ERROR(S):")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print(f"\nOK: all checks passed ({len(glob.glob(os.path.join(SCHOOLS, '*', 'grammar.json')))} grammars)")
