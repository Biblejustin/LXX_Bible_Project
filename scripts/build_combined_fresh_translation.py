#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from typing import Dict, List

from build_fresh_translation import (
    bullet_lines,
    describe_scope,
    ensure_source_columns,
    group_by_ref,
    load_json,
    preferred_resources_for_scope,
    recorded_text,
)
from fresh_bible.pipeline_common import load_csv


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
PUBLICATION_TITLE = "The Greek Heritage Study Bible"
DEFAULT_OT_SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
DEFAULT_NT_SOURCE = ROOT / "data" / "raw" / "tr_greek" / "nt_full.csv"
DEFAULT_LOGOS_NOTES = ROOT / "data" / "research" / "logos_notes.csv"
DEFAULT_DECISIONS = ROOT / "data" / "research" / "translation_decisions.csv"
DEFAULT_FOOTNOTES = ROOT / "data" / "research" / "translation_footnotes.csv"
DEFAULT_VARIANTS = ROOT / "data" / "research" / "variant_notes.csv"
DEFAULT_STACK = ROOT / "data" / "research" / "logos_translation_stack.json"
DEFAULT_OUTPUT = OUTPUT / "the_greek_heritage_study_bible.md"
DEFAULT_TRANSLATION_ONLY = OUTPUT / "the_greek_heritage_study_bible_translation_only.md"
DEFAULT_DIAGNOSTICS = OUTPUT / "the_greek_heritage_study_bible_diagnostics.json"


def ordered_books(rows: List[Dict[str, str]]) -> List[str]:
    books: List[str] = []
    for row in rows:
        book_name = row.get("book_name", "").strip()
        if book_name and book_name not in books:
            books.append(book_name)
    return books


def append_translation_rows(lines: List[str], testament: str, rows: List[Dict[str, str]]) -> None:
    lines.append(f"## {testament}")
    lines.append("")

    current_book = None
    current_chapter = None
    for row in rows:
        book_name = row.get("book_name", "").strip()
        chapter = row.get("chapter", "").strip()
        ref = row.get("ref", "").strip()
        draft = row.get("draft_translation", "").strip()
        if book_name != current_book:
            current_book = book_name
            current_chapter = None
            lines.append(f"### {book_name}")
            lines.append("")
        if chapter != current_chapter:
            current_chapter = chapter
            lines.append(f"#### Chapter {chapter}")
            lines.append("")
        lines.append(f"**{ref}**")
        lines.append("")
        lines.append(draft or "No draft translation recorded.")
        lines.append("")


def combined_scope(ot_rows: List[Dict[str, str]], nt_rows: List[Dict[str, str]]) -> str:
    books = ordered_books(ot_rows) + ordered_books(nt_rows)
    return f"{books[0]}-{books[-1]} ({len(books)} books)" if books else "Unknown scope"


def build_combined_translation_only_markdown(
    ot_rows: List[Dict[str, str]],
    nt_rows: List[Dict[str, str]],
) -> str:
    lines = [
        f"# {PUBLICATION_TITLE}",
        "",
        f"Scope: {combined_scope(ot_rows, nt_rows)}",
        "",
    ]
    append_translation_rows(lines, "Old Testament", ot_rows)
    append_translation_rows(lines, "New Testament", nt_rows)
    return "\n".join(lines).strip() + "\n"


def append_preferred_resources(
    lines: List[str],
    rows: List[Dict[str, str]],
    stack: Dict[str, object],
) -> None:
    preferred_resources = preferred_resources_for_scope(stack, rows)
    if not preferred_resources:
        return
    lines.append("Preferred research stack:")
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


def append_worksheet_rows(
    lines: List[str],
    testament: str,
    rows: List[Dict[str, str]],
    logos_notes: Dict[str, List[Dict[str, str]]],
    decisions: Dict[str, List[Dict[str, str]]],
    footnotes: Dict[str, List[Dict[str, str]]],
    variants: Dict[str, List[Dict[str, str]]],
    stack: Dict[str, object],
) -> None:
    lines.extend([f"## {testament}", "", f"Scope: {describe_scope(rows)}", ""])
    append_preferred_resources(lines, rows, stack)

    current_book = None
    current_chapter = None
    for row in rows:
        ref = row["ref"].strip()
        book_name = row.get("book_name", "").strip()
        chapter = row.get("chapter", "").strip()
        if book_name != current_book:
            current_book = book_name
            current_chapter = None
            lines.append(f"### {book_name}")
            lines.append("")
        if chapter != current_chapter:
            current_chapter = chapter
            lines.append(f"#### Chapter {chapter}")
            lines.append("")
        lines.append(f"##### {ref}")
        lines.append("")
        lines.append(f"Greek: {recorded_text(row, 'greek_text')}")
        lines.append(f"Transliteration: {recorded_text(row, 'transliteration')}")
        lines.append(f"Literal gloss: {recorded_text(row, 'literal_gloss')}")
        lines.append(f"Syntax notes: {recorded_text(row, 'syntax_notes')}")
        lines.append(f"Draft translation: {recorded_text(row, 'draft_translation', 'No draft translation recorded.')}")
        lines.append("")

        decision_lines = bullet_lines(
            decisions.get(ref, []),
            [
                "greek_phrase",
                "lemma",
                "morphology",
                "chosen_rendering",
                "alternate_renderings",
                "rationale",
                "status",
            ],
        )
        lines.append("Decision rows:")
        lines.extend(decision_lines or ["- None recorded."])
        lines.append("")

        footnote_lines = bullet_lines(
            footnotes.get(ref, []),
            ["note_type", "trigger_phrase", "footnote_text", "source_basis", "status"],
        )
        lines.append("Publishable footnotes:")
        lines.extend(footnote_lines or ["- None recorded."])
        lines.append("")

        logos_lines = bullet_lines(
            logos_notes.get(ref, []),
            [
                "greek_phrase",
                "lemma",
                "resource",
                "location",
                "claim_paraphrase",
                "usage_note",
                "confidence",
                "next_action",
            ],
        )
        lines.append("Logos research:")
        lines.extend(logos_lines or ["- None recorded."])
        lines.append("")

        variant_lines = bullet_lines(
            variants.get(ref, []),
            ["witnesses", "reading", "translation_impact", "decision", "status"],
        )
        lines.append("Variant notes:")
        lines.extend(variant_lines or ["- None recorded."])
        lines.append("")


def build_combined_worksheet_markdown(
    ot_rows: List[Dict[str, str]],
    nt_rows: List[Dict[str, str]],
    logos_notes: Dict[str, List[Dict[str, str]]],
    decisions: Dict[str, List[Dict[str, str]]],
    footnotes: Dict[str, List[Dict[str, str]]],
    variants: Dict[str, List[Dict[str, str]]],
    stack: Dict[str, object],
) -> str:
    lines = [
        f"# {PUBLICATION_TITLE} Worksheet",
        "",
        f"Scope: {combined_scope(ot_rows, nt_rows)}",
        "",
        "Method:",
        "- Greek source text first",
        "- Era-aware lexical research",
        "- Phrase-level decision logging",
        "- Variant-impact notes kept separate",
        "",
    ]
    append_worksheet_rows(lines, "Old Testament", ot_rows, logos_notes, decisions, footnotes, variants, stack)
    append_worksheet_rows(lines, "New Testament", nt_rows, logos_notes, decisions, footnotes, variants, stack)
    return "\n".join(lines).strip() + "\n"


def build_diagnostics(
    ot_rows: List[Dict[str, str]],
    nt_rows: List[Dict[str, str]],
    logos_rows: List[Dict[str, str]],
    decisions_rows: List[Dict[str, str]],
    footnote_rows: List[Dict[str, str]],
    variant_rows: List[Dict[str, str]],
    ot_source_path: Path,
    nt_source_path: Path,
    output_path: Path,
    translation_only_output_path: Path,
) -> Dict[str, object]:
    ot_books = ordered_books(ot_rows)
    nt_books = ordered_books(nt_rows)
    return {
        "output": str(output_path),
        "translation_only_output": str(translation_only_output_path),
        "scope": combined_scope(ot_rows, nt_rows),
        "ot_source": str(ot_source_path),
        "nt_source": str(nt_source_path),
        "ot_rows": len(ot_rows),
        "nt_rows": len(nt_rows),
        "total_rows": len(ot_rows) + len(nt_rows),
        "total_drafted_rows": sum(
            1 for row in [*ot_rows, *nt_rows] if row.get("draft_translation", "").strip()
        ),
        "ot_book_count": len(ot_books),
        "nt_book_count": len(nt_books),
        "total_book_count": len(ot_books) + len(nt_books),
        "logos_note_rows": len(logos_rows),
        "decision_rows": len(decisions_rows),
        "footnote_rows": len(footnote_rows),
        "variant_rows": len(variant_rows),
        "ot_books": ot_books,
        "nt_books": nt_books,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ot-source", default=str(DEFAULT_OT_SOURCE))
    parser.add_argument("--nt-source", default=str(DEFAULT_NT_SOURCE))
    parser.add_argument("--logos-notes", default=str(DEFAULT_LOGOS_NOTES))
    parser.add_argument("--decisions", default=str(DEFAULT_DECISIONS))
    parser.add_argument("--footnotes", default=str(DEFAULT_FOOTNOTES))
    parser.add_argument("--variants", default=str(DEFAULT_VARIANTS))
    parser.add_argument("--stack", default=str(DEFAULT_STACK))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--translation-only-output", default=str(DEFAULT_TRANSLATION_ONLY))
    parser.add_argument("--diagnostics", default=str(DEFAULT_DIAGNOSTICS))
    args = parser.parse_args()

    ot_source_path = Path(args.ot_source)
    nt_source_path = Path(args.nt_source)
    logos_path = Path(args.logos_notes)
    decisions_path = Path(args.decisions)
    footnotes_path = Path(args.footnotes)
    variants_path = Path(args.variants)
    stack_path = Path(args.stack)
    output_path = Path(args.output)
    translation_only_output_path = Path(args.translation_only_output)
    diagnostics_path = Path(args.diagnostics)

    ot_rows = load_csv(ot_source_path)
    nt_rows = load_csv(nt_source_path)
    ensure_source_columns(ot_rows)
    ensure_source_columns(nt_rows)
    if not ot_rows:
        raise ValueError("No OT source rows found.")
    if not nt_rows:
        raise ValueError("No NT source rows found.")
    logos_rows = load_csv(logos_path)
    decisions_rows = load_csv(decisions_path)
    footnote_rows = load_csv(footnotes_path)
    variant_rows = load_csv(variants_path)
    stack = load_json(stack_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    translation_only_output_path.parent.mkdir(parents=True, exist_ok=True)
    diagnostics_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(
        build_combined_worksheet_markdown(
            ot_rows,
            nt_rows,
            group_by_ref(logos_rows),
            group_by_ref(decisions_rows),
            group_by_ref(footnote_rows),
            group_by_ref(variant_rows),
            stack,
        ),
        encoding="utf-8",
    )
    translation_only_output_path.write_text(
        build_combined_translation_only_markdown(ot_rows, nt_rows),
        encoding="utf-8",
    )
    diagnostics_path.write_text(
        json.dumps(
            build_diagnostics(
                ot_rows,
                nt_rows,
                logos_rows,
                decisions_rows,
                footnote_rows,
                variant_rows,
                ot_source_path,
                nt_source_path,
                output_path,
                translation_only_output_path,
            ),
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

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
