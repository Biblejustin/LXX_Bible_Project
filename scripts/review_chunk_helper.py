#!/usr/bin/env python3
"""Helpers for repetitive translation-review bookkeeping."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OT_SOURCE = ROOT / "data/raw/lxx_greek/ot_full.csv"
NT_SOURCE = ROOT / "data/raw/tr_greek/nt_full.csv"
FOOTNOTES = ROOT / "data/research/translation_footnotes.csv"
GUARDS = ROOT / "data/research/reviewed_phrase_guards.csv"
RESEARCH = ROOT / "data/research"


REF_RE = re.compile(r"^(.+?)\s+(\d+):(\d+)(?:-(\d+))?$")


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        if reader.fieldnames is None:
            raise ValueError(f"No CSV header: {path}")
        return reader.fieldnames, rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def expand_refs(spec: str) -> list[str]:
    refs: list[str] = []
    for part in spec.split(","):
        item = part.strip()
        if not item:
            continue
        match = REF_RE.match(item)
        if not match:
            refs.append(item)
            continue
        book, chapter, start, end = match.groups()
        if end is None:
            refs.append(f"{book} {chapter}:{start}")
            continue
        refs.extend(f"{book} {chapter}:{verse}" for verse in range(int(start), int(end) + 1))
    return refs


def source_rows(testament: str) -> dict[str, dict[str, str]]:
    path = OT_SOURCE if testament == "ot" else NT_SOURCE
    _, rows = read_csv(path)
    return {row["ref"]: row for row in rows}


def sync_translation_footnotes(refs: set[str], source_by_ref: dict[str, dict[str, str]]) -> int:
    fieldnames, rows = read_csv(FOOTNOTES)
    changed = 0
    for row in rows:
        if (
            row["ref"] in refs
            and row["note_type"] == "translation"
            and row["source_basis"] == "translation comparison"
        ):
            new_phrase = source_by_ref[row["ref"]]["draft_translation"]
            if row["trigger_phrase"] != new_phrase:
                row["trigger_phrase"] = new_phrase
                changed += 1
    write_csv(FOOTNOTES, fieldnames, rows)
    return changed


def upsert_full_verse_guards(testament: str, refs: set[str], source_by_ref: dict[str, dict[str, str]], note: str) -> int:
    if GUARDS.exists():
        fieldnames, rows = read_csv(GUARDS)
    else:
        fieldnames = ["testament", "ref", "mode", "phrase", "note", "status"]
        rows = []

    existing = {
        (row["testament"], row["ref"], row["mode"], row["note"]): row
        for row in rows
    }
    changed = 0
    for ref in sorted(refs, key=lambda value: (source_by_ref[value]["book_name"], int(source_by_ref[value]["chapter"]), int(source_by_ref[value]["verse"]))):
        key = (testament, ref, "equals", note)
        phrase = source_by_ref[ref]["draft_translation"]
        if key in existing:
            row = existing[key]
            if row["phrase"] != phrase or row["status"] != "reviewed":
                row["phrase"] = phrase
                row["status"] = "reviewed"
                changed += 1
        else:
            rows.append(
                {
                    "testament": testament,
                    "ref": ref,
                    "mode": "equals",
                    "phrase": phrase,
                    "note": note,
                    "status": "reviewed",
                }
            )
            changed += 1

    write_csv(GUARDS, fieldnames, rows)
    return changed


def create_pass_file(pass_id: int, scope: str, changes: str) -> Path:
    path = RESEARCH / f"ot_review_pass_{pass_id:03d}.md"
    if path.exists():
        return path
    path.write_text(
        "\n".join(
            [
                f"# OT Review Pass {pass_id}",
                "",
                f"Scope: {scope}.",
                "",
                "Changes:",
                f"- {changes}",
                "- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.",
                "",
                "Validation:",
                "- Pending.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return path


def check_sync(refs: set[str], source_by_ref: dict[str, dict[str, str]]) -> None:
    _, footnotes = read_csv(FOOTNOTES)
    footnote_by_ref = {
        row["ref"]: row["trigger_phrase"]
        for row in footnotes
        if row["ref"] in refs
        and row["note_type"] == "translation"
        and row["source_basis"] == "translation comparison"
    }
    missing = [
        ref
        for ref in refs
        if ref in footnote_by_ref and footnote_by_ref[ref] != source_by_ref[ref]["draft_translation"]
    ]
    if missing:
        for ref in missing[:20]:
            print(f"mismatch {ref}: source={source_by_ref[ref]['draft_translation']} note={footnote_by_ref[ref]}")
        raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--testament", choices=["ot", "nt"], default="ot")
    parser.add_argument("--refs", required=True, help="Comma-separated refs or same-chapter ranges, e.g. 'Isaiah 44:13-23'.")
    parser.add_argument("--sync-footnotes", action="store_true")
    parser.add_argument("--add-full-verse-guards", action="store_true")
    parser.add_argument("--guard-note", default="review chunk")
    parser.add_argument("--pass-id", type=int)
    parser.add_argument("--scope")
    parser.add_argument("--changes", default="Reviewed article and readability cleanup.")
    parser.add_argument("--check-sync", action="store_true")
    args = parser.parse_args()

    refs = set(expand_refs(args.refs))
    source_by_ref = source_rows(args.testament)
    missing_refs = sorted(ref for ref in refs if ref not in source_by_ref)
    if missing_refs:
        raise SystemExit(f"Unknown refs: {', '.join(missing_refs)}")

    if args.sync_footnotes:
        print({"footnotes_synced": sync_translation_footnotes(refs, source_by_ref)})
    if args.add_full_verse_guards:
        print({"guards_upserted": upsert_full_verse_guards(args.testament, refs, source_by_ref, args.guard_note)})
    if args.pass_id is not None:
        scope = args.scope or args.refs
        print({"pass_file": str(create_pass_file(args.pass_id, scope, args.changes))})
    if args.check_sync:
        check_sync(refs, source_by_ref)
        print({"sync_ok": len(refs)})


if __name__ == "__main__":
    main()
