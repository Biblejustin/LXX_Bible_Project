#!/usr/bin/env python3
"""Import Scrivener 1894 Textus Receptus NT rows for the fresh translation pipeline."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

try:
    from build_study_bible import STANDARD_BOOK_NAMES, parse_ukjv_xml
except ImportError:  # pragma: no cover - supports module execution from repo root.
    from scripts.build_study_bible import STANDARD_BOOK_NAMES, parse_ukjv_xml


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
TR_ROOT = RAW / "tr_greek"
SOURCE_DIR = TR_ROOT / "byztxt_greektext_scrivener_textonly"
DEFAULT_OUTPUT = TR_ROOT / "nt_full.csv"
DEFAULT_README = TR_ROOT / "README.md"
DEFAULT_MANIFEST = TR_ROOT / "source_manifest.json"

SCRIVENER_REPO = "https://github.com/byztxt/greektext-scrivener"
SCRIVENER_COMMIT = "6049a43b135ed870f843b83eb6a04764fc796678"
RAW_BASE = f"https://raw.githubusercontent.com/byztxt/greektext-scrivener/{SCRIVENER_COMMIT}/textonly"

BOOKS = [
    ("MT.SCV", "MAT"),
    ("MR.SCV", "MRK"),
    ("LU.SCV", "LUK"),
    ("JOH.SCV", "JHN"),
    ("AC.SCV", "ACT"),
    ("RO.SCV", "ROM"),
    ("1CO.SCV", "1CO"),
    ("2CO.SCV", "2CO"),
    ("GA.SCV", "GAL"),
    ("EPH.SCV", "EPH"),
    ("PHP.SCV", "PHP"),
    ("COL.SCV", "COL"),
    ("1TH.SCV", "1TH"),
    ("2TH.SCV", "2TH"),
    ("1TI.SCV", "1TI"),
    ("2TI.SCV", "2TI"),
    ("TIT.SCV", "TIT"),
    ("PHM.SCV", "PHM"),
    ("HEB.SCV", "HEB"),
    ("JAS.SCV", "JAS"),
    ("1PE.SCV", "1PE"),
    ("2PE.SCV", "2PE"),
    ("1JO.SCV", "1JN"),
    ("2JO.SCV", "2JN"),
    ("3JO.SCV", "3JN"),
    ("JUDE.SCV", "JUD"),
    ("RE.SCV", "REV"),
]

ASCII_GREEK = {
    "a": "α",
    "b": "β",
    "g": "γ",
    "d": "δ",
    "e": "ε",
    "z": "ζ",
    "h": "η",
    "y": "θ",
    "i": "ι",
    "k": "κ",
    "l": "λ",
    "m": "μ",
    "n": "ν",
    "x": "ξ",
    "o": "ο",
    "p": "π",
    "r": "ρ",
    "s": "σ",
    "v": "ς",
    "t": "τ",
    "u": "υ",
    "f": "φ",
    "c": "χ",
    "q": "ψ",
    "w": "ω",
}
ASCII_GREEK.update({key.upper(): value.upper() for key, value in ASCII_GREEK.items() if key != "v"})
ASCII_GREEK["V"] = "Σ"

VERSE_RE = re.compile(r"^\s*(\d+):(\d+)\s*(.*)$")
TITLE_RE = re.compile(r"^\[.*\]$")
SOURCE_COLUMNS = [
    "ref",
    "book_code",
    "book_name",
    "chapter",
    "verse",
    "greek_text",
    "transliteration",
    "literal_gloss",
    "syntax_notes",
    "draft_translation",
]


def download_sources(source_dir: Path, *, force: bool = False) -> dict[str, object]:
    source_dir.mkdir(parents=True, exist_ok=True)
    downloaded: list[str] = []
    for filename, _book_code in BOOKS:
        target = source_dir / filename
        if target.exists() and not force:
            continue
        write_normalized_download(f"{RAW_BASE}/{filename}", target)
        downloaded.append(filename)
    for filename in ["TITLES.SCV", "REVISION.LST"]:
        target = source_dir / filename
        if target.exists() and not force:
            continue
        write_normalized_download(f"{RAW_BASE}/{filename}", target)
        downloaded.append(filename)
    return {"downloaded": downloaded, "source_dir": str(source_dir)}


def write_normalized_download(url: str, target: Path) -> None:
    with urllib.request.urlopen(url) as response:
        raw = response.read().decode("utf-8", errors="replace")
    normalized = "\n".join(line.rstrip() for line in raw.replace("\r\n", "\n").replace("\r", "\n").split("\n"))
    if not normalized.endswith("\n"):
        normalized += "\n"
    target.write_text(normalized, encoding="utf-8")


def ascii_to_greek(value: str) -> str:
    return "".join(ASCII_GREEK.get(char, char) for char in value)


def normalize_line(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def parse_scv(path: Path, book_code: str) -> list[dict[str, object]]:
    verses: dict[tuple[int, int], list[str]] = {}
    current: tuple[int, int] | None = None
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        match = VERSE_RE.match(line)
        if match:
            chapter = int(match.group(1))
            verse = int(match.group(2))
            rest = normalize_line(match.group(3))
            current = (chapter, verse)
            verses.setdefault(current, [])
            if rest and not TITLE_RE.match(rest):
                verses[current].append(rest)
            continue
        stripped = normalize_line(line)
        if not stripped or TITLE_RE.match(stripped) or current is None:
            continue
        verses.setdefault(current, []).append(stripped)

    book_name = STANDARD_BOOK_NAMES[book_code]
    rows: list[dict[str, object]] = []
    for chapter, verse in sorted(verses):
        transliteration = normalize_line(" ".join(verses[(chapter, verse)]))
        rows.append(
            {
                "ref": f"{book_name} {chapter}:{verse}",
                "book_code": book_code,
                "book_name": book_name,
                "chapter": chapter,
                "verse": verse,
                "greek_text": ascii_to_greek(transliteration),
                "transliteration": transliteration,
            }
        )
    return rows


def load_ukjv_nt() -> dict[tuple[str, int, int], str]:
    records, _diagnostics = parse_ukjv_xml()
    return {
        (record.book_code, record.chapter, record.verse): record.text
        for record in records
        if record.book_code in {book_code for _filename, book_code in BOOKS}
    }


def build_rows(source_dir: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    ukjv = load_ukjv_nt()
    rows: list[dict[str, object]] = []
    counts: Counter[str] = Counter()
    book_counts: dict[str, int] = {}
    for filename, book_code in BOOKS:
        parsed = parse_scv(source_dir / filename, book_code)
        book_counts[book_code] = len(parsed)
        for row in parsed:
            key = (str(row["book_code"]), int(row["chapter"]), int(row["verse"]))
            row["literal_gloss"] = ""
            row["syntax_notes"] = ""
            row["draft_translation"] = ukjv.get(key, "")
            if row["draft_translation"]:
                counts["seeded_from_ukjv"] += 1
            else:
                counts["missing_ukjv_seed"] += 1
            rows.append(row)
    return rows, {
        "rows": len(rows),
        "book_count": len(book_counts),
        "book_counts": book_counts,
        **dict(counts),
    }


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=SOURCE_COLUMNS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in SOURCE_COLUMNS})


def write_manifest(path: Path, diagnostics: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "source": "Scrivener 1894 Textus Receptus, text-only files",
        "upstream_repo": SCRIVENER_REPO,
        "upstream_commit": SCRIVENER_COMMIT,
        "raw_base": RAW_BASE,
        "license": "Public Domain. Copy freely.",
        "editor": "Dr. Maurice A. Robinson",
        "maintainer": "Dr. Ulrik Sandborg-Petersen / Scripture Systems ApS",
        "files": [filename for filename, _book_code in BOOKS],
        "diagnostics": diagnostics,
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_readme(path: Path, output_csv: Path, manifest: Path, diagnostics: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = f"""# Textus Receptus Greek NT Source

Source: Scrivener 1894 Textus Receptus text-only files from byztxt/greektext-scrivener.

- Upstream: <{SCRIVENER_REPO}>
- Pinned commit: `{SCRIVENER_COMMIT}`
- License notice from upstream README: `Public Domain. Copy freely.`
- Imported CSV: `{output_csv.relative_to(ROOT).as_posix()}`
- Source manifest: `{manifest.relative_to(ROOT).as_posix()}`

Import notes:

- Upstream files use an ASCII Greek encoding. The importer preserves that source string in `transliteration` and converts it to unaccented Unicode Greek in `greek_text`.
- Downloaded SCV files are normalized to LF line endings with trailing source-line whitespace trimmed.
- `draft_translation` is seeded from the public-domain UKJV so the Logos builder has a complete NT baseline. Treat it as an alignment seed, not final literal revision.
- `literal_gloss` and `syntax_notes` are intentionally blank until verse-level TR review fills them.

Import counts:

- Rows: {diagnostics.get("rows", 0)}
- Books: {diagnostics.get("book_count", 0)}
- UKJV-seeded draft rows: {diagnostics.get("seeded_from_ukjv", 0)}
- Missing UKJV seed rows: {diagnostics.get("missing_ukjv_seed", 0)}
"""
    path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, default=SOURCE_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--readme", type=Path, default=DEFAULT_README)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--force-download", action="store_true")
    parser.add_argument("--skip-download", action="store_true")
    args = parser.parse_args()

    if not args.skip_download:
        download_sources(args.source_dir, force=args.force_download)
    missing = [filename for filename, _book_code in BOOKS if not (args.source_dir / filename).exists()]
    if missing:
        raise FileNotFoundError(f"Missing Scrivener source files: {', '.join(missing)}")

    rows, diagnostics = build_rows(args.source_dir)
    write_csv(args.output, rows)
    write_manifest(args.manifest, diagnostics)
    write_readme(args.readme, args.output, args.manifest, diagnostics)
    print(json.dumps({"output": str(args.output), "diagnostics": diagnostics}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
