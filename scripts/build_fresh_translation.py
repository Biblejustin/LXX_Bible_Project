#!/usr/bin/env python3
import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from fresh_bible.book_scope import filter_rows_by_scope


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RESEARCH = DATA / "research"
LXX_GREEK = DATA / "raw" / "lxx_greek"
OUTPUT = ROOT / "output"

DEFAULT_SOURCE = LXX_GREEK / "genesis_1_3_pilot.csv"
DEFAULT_LOGOS_NOTES = RESEARCH / "logos_notes.csv"
DEFAULT_DECISIONS = RESEARCH / "translation_decisions.csv"
DEFAULT_FOOTNOTES = RESEARCH / "translation_footnotes.csv"
DEFAULT_VARIANTS = RESEARCH / "variant_notes.csv"
DEFAULT_STACK = RESEARCH / "logos_translation_stack.json"
DEFAULT_OUTPUT = OUTPUT / "fresh_translation_genesis_1_3_pilot.md"
DEFAULT_TRANSLATION_ONLY = OUTPUT / "fresh_translation_genesis_1_3_translation_only.md"
DEFAULT_DIAGNOSTICS = OUTPUT / "fresh_translation_genesis_1_3_pilot_diagnostics.json"

REQUIRED_SOURCE_COLUMNS = [
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

csv.field_size_limit(sys.maxsize)


def load_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_json(path: Path) -> Dict[str, object]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def ensure_source_columns(rows: List[Dict[str, str]]) -> None:
    if not rows:
        return
    missing = [column for column in REQUIRED_SOURCE_COLUMNS if column not in rows[0]]
    if missing:
        raise ValueError(f"Missing source columns: {', '.join(missing)}")


def group_by_ref(rows: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    grouped: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        ref = row.get("ref", "").strip()
        if ref:
            grouped[ref].append(row)
    return grouped


def bullet_lines(rows: List[Dict[str, str]], fields: List[str]) -> List[str]:
    lines: List[str] = []
    for row in rows:
        parts = []
        for field in fields:
            value = row.get(field, "").strip()
            if value:
                parts.append(f"{field}: {value}")
        if parts:
            lines.append("- " + " | ".join(parts))
    return lines


def describe_scope(source_rows: List[Dict[str, str]]) -> str:
    if not source_rows:
        return "Unknown scope"
    ordered_books: List[str] = []
    for row in source_rows:
        book_name = row.get("book_name", "").strip()
        if book_name and book_name not in ordered_books:
            ordered_books.append(book_name)
    if not ordered_books:
        return "Unknown Book"
    if len(ordered_books) > 1:
        return f"{ordered_books[0]}-{ordered_books[-1]} ({len(ordered_books)} books)"
    chapters = sorted({int(row.get("chapter", "").strip()) for row in source_rows if row.get("chapter", "").strip()})
    if not chapters:
        return ordered_books[0]
    if chapters == list(range(chapters[0], chapters[-1] + 1)):
        return f"{ordered_books[0]} {chapters[0]}-{chapters[-1]}"
    chapter_list = ", ".join(str(ch) for ch in chapters)
    return f"{ordered_books[0]} {chapter_list}"


def filter_output_rows(source_rows: List[Dict[str, str]], skip_undrafted: bool) -> List[Dict[str, str]]:
    if not skip_undrafted:
        return source_rows
    return [row for row in source_rows if row.get("draft_translation", "").strip()]


def build_markdown(
    source_rows: List[Dict[str, str]],
    logos_notes: Dict[str, List[Dict[str, str]]],
    decisions: Dict[str, List[Dict[str, str]]],
    footnotes: Dict[str, List[Dict[str, str]]],
    variants: Dict[str, List[Dict[str, str]]],
    stack: Dict[str, object],
    scope_rows: List[Dict[str, str]] | None = None,
    drafted_only: bool = False,
) -> str:
    scope = describe_scope(scope_rows or source_rows)
    preferred_resources = stack.get("preferred_resources", []) if isinstance(stack, dict) else []
    lines = [
        "# Fresh Translation Worksheet",
        "",
        f"Scope: {scope}",
        "",
    ]
    if drafted_only:
        lines.extend(
            [
                "Display: drafted verses only",
                "",
            ]
        )
    lines.extend(
        [
        "Method:",
        "- Greek source text first",
        "- Era-aware lexical research",
        "- Phrase-level decision logging",
        "- Variant-impact notes kept separate",
        "",
        ]
    )

    if preferred_resources:
        lines.append("Preferred Logos stack:")
        for resource in preferred_resources:
            if not isinstance(resource, dict):
                continue
            role = str(resource.get("role", "")).strip()
            title = str(resource.get("title", "")).strip()
            resource_id = str(resource.get("resource_id", "")).strip()
            purpose = str(resource.get("purpose", "")).strip()
            parts = [part for part in [role, title, resource_id, purpose] if part]
            if parts:
                lines.append("- " + " | ".join(parts))
        lines.append("")

    current_book = None
    current_chapter = None
    for row in source_rows:
        ref = row["ref"].strip()
        book_name = row.get("book_name", "").strip()
        chapter = row.get("chapter", "").strip()
        if book_name != current_book:
            current_book = book_name
            current_chapter = None
            lines.append(f"# {book_name}")
            lines.append("")
        if chapter != current_chapter:
            current_chapter = chapter
            lines.append(f"## Chapter {chapter}")
            lines.append("")
        lines.append(f"### {ref}")
        lines.append("")
        lines.append(f"Greek: {row.get('greek_text', '').strip() or '[TODO add Greek text]'}")
        lines.append(f"Transliteration: {row.get('transliteration', '').strip() or '[TODO]'}")
        lines.append(f"Literal gloss: {row.get('literal_gloss', '').strip() or '[TODO]'}")
        lines.append(f"Syntax notes: {row.get('syntax_notes', '').strip() or '[TODO]'}")
        lines.append(f"Draft translation: {row.get('draft_translation', '').strip() or '[TODO]'}")
        lines.append("")

        decision_lines = bullet_lines(
            decisions.get(ref, []),
            ["greek_phrase", "lemma", "morphology", "chosen_rendering", "alternate_renderings", "rationale", "status"],
        )
        lines.append("Decision rows:")
        lines.extend(decision_lines or ["- [TODO add decision rows]"])
        lines.append("")

        footnote_lines = bullet_lines(
            footnotes.get(ref, []),
            ["note_type", "trigger_phrase", "footnote_text", "source_basis", "status"],
        )
        lines.append("Publishable footnotes:")
        lines.extend(footnote_lines or ["- [TODO add footnote draft if needed]"])
        lines.append("")

        logos_lines = bullet_lines(
            logos_notes.get(ref, []),
            ["greek_phrase", "lemma", "resource", "location", "claim_paraphrase", "usage_note", "confidence", "next_action"],
        )
        lines.append("Logos research:")
        lines.extend(logos_lines or ["- [TODO add Logos note]"])
        lines.append("")

        variant_lines = bullet_lines(
            variants.get(ref, []),
            ["witnesses", "reading", "translation_impact", "decision", "status"],
        )
        lines.append("Variant notes:")
        lines.extend(variant_lines or ["- [TODO add variant note]"])
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def build_translation_only_markdown(
    source_rows: List[Dict[str, str]],
    scope_rows: List[Dict[str, str]] | None = None,
    drafted_only: bool = False,
) -> str:
    scope = describe_scope(scope_rows or source_rows)
    lines = [
        "# Fresh Translation Draft",
        "",
        f"Scope: {scope}",
        "",
    ]
    if drafted_only:
        lines.extend(
            [
                "Display: drafted verses only",
                "",
            ]
        )

    current_book = None
    current_chapter = None
    for row in source_rows:
        book_name = row.get("book_name", "").strip()
        chapter = row.get("chapter", "").strip()
        ref = row.get("ref", "").strip()
        draft = row.get("draft_translation", "").strip()
        if book_name != current_book:
            current_book = book_name
            current_chapter = None
            lines.append(f"## {book_name}")
            lines.append("")
        if chapter != current_chapter:
            current_chapter = chapter
            lines.append(f"### Chapter {chapter}")
            lines.append("")
        lines.append(f"**{ref}**")
        lines.append("")
        lines.append(draft or "[TODO]")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def build_diagnostics(
    source_rows: List[Dict[str, str]],
    selected_rows: List[Dict[str, str]],
    output_rows: List[Dict[str, str]],
    logos_notes: List[Dict[str, str]],
    decisions: List[Dict[str, str]],
    footnotes: List[Dict[str, str]],
    variants: List[Dict[str, str]],
    stack: Dict[str, object],
) -> Dict[str, object]:
    book_rows: Dict[str, Dict[str, int]] = {}
    for row in source_rows:
        book_name = row.get("book_name", "").strip() or "Unknown Book"
        current = book_rows.setdefault(book_name, {"verse_rows": 0, "drafted_rows": 0})
        current["verse_rows"] += 1
        if row.get("draft_translation", "").strip():
            current["drafted_rows"] += 1
    return {
        "verse_rows": len(source_rows),
        "verses_with_greek_text": sum(1 for row in source_rows if row.get("greek_text", "").strip()),
        "verses_with_draft_translation": sum(1 for row in source_rows if row.get("draft_translation", "").strip()),
        "selected_scope": describe_scope(selected_rows),
        "selected_verse_rows": len(selected_rows),
        "selected_drafted_rows": sum(1 for row in selected_rows if row.get("draft_translation", "").strip()),
        "output_verse_rows": len(output_rows),
        "output_drafted_rows": sum(1 for row in output_rows if row.get("draft_translation", "").strip()),
        "book_count": len(book_rows),
        "book_rows": book_rows,
        "logos_note_rows": len(logos_notes),
        "decision_rows": len(decisions),
        "footnote_rows": len(footnotes),
        "variant_rows": len(variants),
        "decision_status_counts": {
            "todo": sum(1 for row in decisions if row.get("status", "").strip().lower() == "todo"),
            "drafted": sum(1 for row in decisions if row.get("status", "").strip().lower() == "drafted"),
            "reviewed": sum(1 for row in decisions if row.get("status", "").strip().lower() == "reviewed"),
        },
        "footnote_status_counts": {
            "todo": sum(1 for row in footnotes if row.get("status", "").strip().lower() == "todo"),
            "drafted": sum(1 for row in footnotes if row.get("status", "").strip().lower() == "drafted"),
            "reviewed": sum(1 for row in footnotes if row.get("status", "").strip().lower() == "reviewed"),
        },
        "chapters": sorted(
            {row.get("chapter", "").strip() for row in source_rows if row.get("chapter", "").strip()},
            key=lambda value: int(value),
        ),
        "preferred_resource_roles": [
            resource.get("role", "")
            for resource in stack.get("preferred_resources", [])
            if isinstance(resource, dict) and resource.get("role", "")
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--logos-notes", default=str(DEFAULT_LOGOS_NOTES))
    parser.add_argument("--decisions", default=str(DEFAULT_DECISIONS))
    parser.add_argument("--footnotes", default=str(DEFAULT_FOOTNOTES))
    parser.add_argument("--variants", default=str(DEFAULT_VARIANTS))
    parser.add_argument("--stack", default=str(DEFAULT_STACK))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--translation-only-output", default=str(DEFAULT_TRANSLATION_ONLY))
    parser.add_argument("--diagnostics", default=str(DEFAULT_DIAGNOSTICS))
    parser.add_argument("--book")
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--chapter-start", type=int)
    parser.add_argument("--chapter-end", type=int)
    parser.add_argument("--skip-undrafted", action="store_true")
    args = parser.parse_args()

    source_path = Path(args.source)
    logos_path = Path(args.logos_notes)
    decisions_path = Path(args.decisions)
    footnotes_path = Path(args.footnotes)
    variants_path = Path(args.variants)
    stack_path = Path(args.stack)
    output_path = Path(args.output)
    translation_only_output_path = Path(args.translation_only_output)
    diagnostics_path = Path(args.diagnostics)

    source_rows = load_csv_rows(source_path)
    ensure_source_columns(source_rows)
    selected_rows = filter_rows_by_scope(
        source_rows,
        args.book,
        args.chapter,
        args.chapter_start,
        args.chapter_end,
    )
    if not selected_rows:
        raise ValueError("No source rows matched requested scope.")
    logos_rows = load_csv_rows(logos_path)
    decisions_rows = load_csv_rows(decisions_path)
    footnote_rows = load_csv_rows(footnotes_path)
    variant_rows = load_csv_rows(variants_path)
    stack = load_json(stack_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    translation_only_output_path.parent.mkdir(parents=True, exist_ok=True)
    diagnostics_path.parent.mkdir(parents=True, exist_ok=True)

    output_rows = filter_output_rows(selected_rows, skip_undrafted=args.skip_undrafted)

    markdown = build_markdown(
        output_rows,
        group_by_ref(logos_rows),
        group_by_ref(decisions_rows),
        group_by_ref(footnote_rows),
        group_by_ref(variant_rows),
        stack,
        scope_rows=selected_rows,
        drafted_only=args.skip_undrafted,
    )
    output_path.write_text(markdown, encoding="utf-8")

    translation_only_markdown = build_translation_only_markdown(
        output_rows,
        scope_rows=selected_rows,
        drafted_only=args.skip_undrafted,
    )
    translation_only_output_path.write_text(translation_only_markdown, encoding="utf-8")

    diagnostics = build_diagnostics(
        source_rows,
        selected_rows,
        output_rows,
        logos_rows,
        decisions_rows,
        footnote_rows,
        variant_rows,
        stack,
    )
    diagnostics_path.write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False), encoding="utf-8")

    print(
        json.dumps(
            {
                "worksheet": str(output_path),
                "translation_only": str(translation_only_output_path),
                "diagnostics": str(diagnostics_path),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
