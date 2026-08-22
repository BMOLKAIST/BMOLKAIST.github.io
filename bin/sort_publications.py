#!/usr/bin/env python3
"""sort_publications.py — enforce the publication-list ordering rule for papers.bib.

RULE (2026-08-22, YongKeun Park):
  1. Year groups, newest year first.
  2. Within a year:   preprint  →  in press  →  published.
  3. Within each of those three bands, the existing relative order is preserved (stable sort),
     so hand-curated ordering inside a band survives a re-run.

WHY THIS LIVES IN A SCRIPT, NOT IN A TEMPLATE OR CSS
    This site's jekyll-scholar renders each year group in *file order* — it does no sorting of
    its own. The rendered order IS the order entries appear in _bibliography/papers.bib. So the
    only way to control what a visitor sees is to physically reorder the entries, and the only
    way to keep that stable as papers are added is to re-run this.

CLASSIFICATION
    preprint  — journal is a preprint server (arXiv / bioRxiv / medRxiv / Research Square /
                SSRN / preprints.org). Note this reads the *journal* field, not the presence of
                a `preprint = {url}` field: published papers legitimately carry a preprint link.
    in press  — `additional_info` mentions "in press" (accepted, no DOI/volume yet).
    published — everything else.

USAGE
    python3 bin/sort_publications.py            # rewrite papers.bib in place
    python3 bin/sort_publications.py --check    # exit 1 if not already sorted; writes nothing
    python3 bin/sort_publications.py --diff     # show what would move; writes nothing
"""
import re
import sys
from pathlib import Path

BIB = Path(__file__).resolve().parents[1] / "_bibliography" / "papers.bib"

PREPRINT_JOURNAL = re.compile(
    r"arxiv|biorxiv|medrxiv|research\s*square|ssrn|preprints?\.org", re.I)
IN_PRESS = re.compile(r"in\s*press", re.I)

PREPRINT, INPRESS, PUBLISHED = 0, 1, 2
BAND_NAME = {PREPRINT: "preprint", INPRESS: "in press", PUBLISHED: "published"}


def field(entry: str, name: str) -> str:
    """Read a top-level `name = {...}` field. Good enough for this file's flat entries."""
    m = re.search(r"(?mi)^\s*" + name + r"\s*=\s*\{(.*?)\}\s*,?\s*$", entry)
    return m.group(1).strip() if m else ""


def citekey(entry: str) -> str:
    m = re.match(r"@\w+\{([^,]+),", entry)
    return m.group(1) if m else "?"


def band(entry: str) -> int:
    if PREPRINT_JOURNAL.search(field(entry, "journal")):
        return PREPRINT
    if IN_PRESS.search(field(entry, "additional_info")):
        return INPRESS
    return PUBLISHED


def year(entry: str) -> int:
    m = re.search(r"(?:19|20)\d{2}", field(entry, "year"))
    return int(m.group(0)) if m else -1


def split_entries(text: str):
    """Return (preamble, [entry, ...]). Entries are chunks starting at a column-0 '@'."""
    parts = re.split(r"(?m)^(?=@)", text)
    preamble = parts[0] if parts and not parts[0].startswith("@") else ""
    entries = [p for p in parts if p.startswith("@")]
    return preamble, entries


def sorted_entries(entries):
    keyed = [(year(e), band(e), i, e) for i, e in enumerate(entries)]
    keyed.sort(key=lambda t: (-t[0], t[1], t[2]))
    return [t[3] for t in keyed]


def render(preamble: str, entries) -> str:
    body = "\n\n".join(e.strip() for e in entries)
    head = preamble.strip()
    return (head + "\n\n" if head else "") + body + "\n"


def main() -> int:
    args = sys.argv[1:]
    text = BIB.read_text(encoding="utf-8")
    preamble, entries = split_entries(text)
    if not entries:
        print("no entries found — refusing to write", file=sys.stderr)
        return 1

    ordered = sorted_entries(entries)

    # Reordering must never change content. Compare the normalized multiset both ways.
    before = sorted(e.strip() for e in entries)
    after = sorted(e.strip() for e in ordered)
    assert before == after, "entry set changed — aborting"

    moved = [(citekey(a), citekey(b)) for a, b in zip(entries, ordered)
             if citekey(a) != citekey(b)]

    if "--diff" in args or "--check" in args:
        print(f"{len(entries)} entries, {len(moved)} would change position")
        if "--diff" in args:
            for e in ordered:
                print(f"  {year(e)}  {BAND_NAME[band(e)]:<9} {citekey(e)}")
        return 1 if moved else 0

    BIB.write_text(render(preamble, ordered), encoding="utf-8")
    print(f"[ok] {BIB.name}: {len(entries)} entries sorted "
          f"(year desc → preprint → in press → published); {len(moved)} moved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
