#!/usr/bin/env python3
"""Build a compact physical proofreading DOCX for the combined fresh translation."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import replace
from pathlib import Path

import build_fresh_logos_bible as builder
from fresh_bible.book_scope import filter_items_by_book


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output" / "print"
DEFAULT_DOCX = OUTPUT_DIR / "the_greek_heritage_study_bible_print_proof.docx"
DEFAULT_DIAGNOSTICS = OUTPUT_DIR / "the_greek_heritage_study_bible_print_proof_diagnostics.json"
DEFAULT_README = OUTPUT_DIR / "README.md"

PRINT_TITLE = "The Greek Heritage Study Bible - Print Proof"
PRINT_DESCRIPTION = (
    "Compact physical proofreading copy of The Greek Heritage Study Bible draft "
    "from OT LXX Greek and NT Scrivener 1894 Textus Receptus Greek."
)
MINIMAL_CROSSREF_POLICY = (
    "Minimal cross-reference layer: TSK phrase-anchored references only, no "
    "OpenBible fallback, capped to one cross-reference footnote per verse and "
    "two references per footnote."
)
SUPPLEMENTAL_POLICY = (
    "Brenton/source supplemental footnotes are excluded; this copy keeps only "
    "reviewed translation/textual notes, name meanings, and minimal cross-references."
)
NAME_MEANING_POLICY = (
    "Name-meaning notes are included only at their listed first/source occurrence "
    "to keep the physical proof shorter."
)


def minimal_print_crossrefs(
    verses: list[builder.Verse],
    crossrefs: dict[str, list[builder.CrossReferenceNote]],
    *,
    max_refs_per_note: int,
) -> tuple[dict[str, list[builder.CrossReferenceNote]], dict[str, object]]:
    selected: dict[str, list[builder.CrossReferenceNote]] = {}
    counts: Counter[str] = Counter()
    for verse in verses:
        notes = crossrefs.get(verse.ref, [])
        counts["input_groups"] += len(notes)
        counts["input_refs"] += sum(len(note.refs) for note in notes)
        candidates = [
            note
            for note in notes
            if note.source == "tsk"
            and note.trigger_phrase.strip()
            and note.display_phrase.strip()
            and note.refs
        ]
        if not candidates:
            if notes:
                counts["verses_with_only_unselected_crossrefs"] += 1
            continue
        note = candidates[0]
        limited = tuple(note.refs[:max_refs_per_note])
        if not limited:
            continue
        selected[verse.ref] = [replace(note, refs=limited)]
        counts["output_groups"] += 1
        counts["output_refs"] += len(limited)
        if len(note.refs) > len(limited):
            counts["truncated_refs"] += len(note.refs) - len(limited)

    return selected, {
        **dict(counts),
        "enabled": True,
        "profile": "minimal_print",
        "source_policy": "TSK only; OpenBible fallback omitted.",
        "selection_policy": "First phrase-anchored TSK group per verse.",
        "max_groups_per_verse": 1,
        "max_refs_per_note": max_refs_per_note,
        "verses_with_crossrefs": len(selected),
    }


def source_ref_name_notes(
    verses: list[builder.Verse],
    source_notes: dict[str, list[builder.NameMeaningNote]],
) -> tuple[dict[str, list[builder.NameMeaningNote]], dict[str, int]]:
    verse_by_ref = {verse.ref: verse for verse in verses}
    selected: dict[str, list[builder.NameMeaningNote]] = {}
    counts: Counter[str] = Counter()

    for source_ref, notes in source_notes.items():
        counts["input_refs"] += 1
        counts["input_notes"] += len(notes)
        verse = verse_by_ref.get(source_ref)
        if verse is None:
            counts["skipped_missing_source_ref"] += len(notes)
            continue

        best_by_text: dict[str, builder.NameMeaningNote] = {}
        for note in notes:
            key = note.display_text
            current = best_by_text.get(key)
            if current is None:
                best_by_text[key] = note
                continue
            current_matches = builder.find_trigger_span(
                verse.text,
                current.trigger_phrase,
                case_sensitive=current.case_sensitive,
            )
            note_matches = builder.find_trigger_span(
                verse.text,
                note.trigger_phrase,
                case_sensitive=note.case_sensitive,
            )
            if note_matches and not current_matches:
                best_by_text[key] = note

        selected_notes = list(best_by_text.values())
        if selected_notes:
            selected[source_ref] = selected_notes
            counts["output_refs"] += 1
            counts["output_notes"] += len(selected_notes)
            counts["deduplicated_alternate_triggers"] += len(notes) - len(selected_notes)

    return selected, {
        **dict(counts),
        "enabled": True,
        "profile": "source_ref_only",
        "selection_policy": "Listed first/source occurrence only; repeated chapter placements omitted.",
    }


def write_readme(
    path: Path,
    *,
    docx_path: Path,
    diagnostics_path: Path,
    diagnostics: dict[str, object],
) -> None:
    stats = diagnostics["print_docx"]
    minimal = diagnostics["minimal_crossrefs"]
    lines = [
        "# Print Proof Files",
        "",
        "Generated files:",
        "",
        f"- `{docx_path.name}`: compact DOCX for inexpensive physical proofreading.",
        f"- `{diagnostics_path.name}`: build counts and DOCX validation details.",
        "",
        "Profile:",
        "",
        "- Combined Genesis-Revelation text.",
        "- Compact two-column DOCX layout with narrow margins.",
        "- Front matter includes an LXX-to-English numbering guide for major reader-facing divergences.",
        "- Reviewed translation/textual notes included.",
        f"- {NAME_MEANING_POLICY}",
        "- Book preface pages excluded.",
        "- Brenton/source supplemental notes excluded.",
        f"- {MINIMAL_CROSSREF_POLICY}",
        "",
        "Counts:",
        "",
        f"- Verses: `{diagnostics['verse_rows']}`",
        f"- Translation/textual note footnotes: `{stats['translation_note_footnotes']}`",
        f"- Name-meaning footnotes: `{stats['name_meaning_footnotes']}`",
        f"- Cross-reference footnotes: `{stats['crossref_footnotes']}`",
        f"- Cross-reference refs kept: `{minimal['output_refs']}`",
        f"- Supplemental/Brenton footnotes: `{stats['supplemental_note_footnotes']}`",
        "",
        "Rebuild:",
        "",
        "```bash",
        "make build-print-proof",
        "```",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=builder.DEFAULT_SOURCE)
    parser.add_argument("--nt-source", type=Path, default=builder.DEFAULT_NT_SOURCE)
    parser.add_argument("--footnotes", type=Path, default=builder.DEFAULT_FOOTNOTES)
    parser.add_argument("--translation-decisions", type=Path, default=builder.DEFAULT_TRANSLATION_DECISIONS)
    parser.add_argument("--proper-names", type=Path, default=builder.DEFAULT_PROPER_NAMES)
    parser.add_argument(
        "--transliterated-proper-names",
        type=Path,
        default=builder.DEFAULT_TRANSLITERATED_PROPER_NAMES,
    )
    parser.add_argument("--names-of-god", type=Path, default=builder.DEFAULT_NAMES_OF_GOD)
    parser.add_argument("--versification-map", type=Path, default=builder.DEFAULT_VERSIFICATION_MAP)
    parser.add_argument("--textual-notes-html", type=Path, default=builder.DEFAULT_TEXTUAL_NOTES_HTML)
    parser.add_argument("--book", help="Limit generated proof copy to one book name or book code.")
    parser.add_argument("--output", type=Path, default=DEFAULT_DOCX)
    parser.add_argument("--diagnostics", type=Path, default=DEFAULT_DIAGNOSTICS)
    parser.add_argument("--readme", type=Path, default=DEFAULT_README)
    parser.add_argument("--max-crossref-refs", type=int, default=2)
    parser.add_argument(
        "--docx-compresslevel",
        type=int,
        choices=range(10),
        default=builder.DOCX_DEFAULT_COMPRESSLEVEL,
        metavar="0-9",
    )
    args = parser.parse_args()

    source_verses = [*builder.load_verses(args.source), *builder.load_verses(args.nt_source)]
    verses = filter_items_by_book(
        source_verses,
        args.book,
        book_name=lambda verse: verse.book_name,
        book_code=lambda verse: verse.book_code,
        item_label="verse",
    )
    versification_map, versification_map_diag = builder.load_versification_map(args.versification_map)
    variant_decisions, variant_decision_counts = builder.load_variant_decisions(args.translation_decisions)
    base_notes, note_counts = builder.load_translation_notes(args.footnotes, variant_decisions)
    textual_export_notes, textual_export_counts = builder.load_textual_notes_export(
        args.textual_notes_html,
        verses,
        versification_map,
    )
    notes = builder.filter_translation_notes_to_verses(
        builder.merge_translation_notes(base_notes, textual_export_notes),
        verses,
    )
    source_name_notes, name_note_counts = builder.load_name_meaning_notes(
        proper_names_path=args.proper_names,
        transliterated_proper_names_path=args.transliterated_proper_names,
        names_of_god_path=args.names_of_god,
        source_filter=None,
    )
    name_notes, name_note_placement_counts = source_ref_name_notes(
        verses,
        source_name_notes,
    )
    name_note_counts = {
        **name_note_counts,
        **{f"placement_{key}": value for key, value in name_note_placement_counts.items()},
    }
    full_crossrefs, full_crossref_diag = builder.build_crossrefs_for_verses(
        verses,
        "combined",
        enabled=True,
    )
    minimal_crossrefs, minimal_crossref_diag = minimal_print_crossrefs(
        verses,
        full_crossrefs,
        max_refs_per_note=args.max_crossref_refs,
    )
    verse_counts = json.loads((builder.DATA / "kjv_versification.json").read_text(encoding="utf-8"))
    print_stats = builder.build_docx(
        path=args.output,
        title=PRINT_TITLE,
        description=PRINT_DESCRIPTION,
        testament="combined",
        verses=verses,
        translation_notes=notes,
        name_notes=name_notes,
        supplemental_notes={},
        crossrefs=minimal_crossrefs,
        book_intros={},
        logos=False,
        datatype="Bible",
        milestone_mode="lxx",
        versification_map=versification_map,
        verse_counts=verse_counts,
        footnote_number_restart="chapter",
        place_links={},
        place_link_pattern=None,
        crossrefs_enabled=True,
        docx_compresslevel=args.docx_compresslevel,
        compact_print=True,
        output_kind="print_proof",
        subtitle="Compact physical proofreading copy",
        crossref_policy=MINIMAL_CROSSREF_POLICY,
        name_policy=NAME_MEANING_POLICY,
        supplemental_policy=SUPPLEMENTAL_POLICY,
    )
    validation = builder.validate_docx(args.output)
    diagnostics: dict[str, object] = {
        "verse_rows": len(verses),
        "book_count": len({verse.book_code for verse in verses}),
        "translation_note_filter": note_counts,
        "translation_decision_filter": variant_decision_counts,
        "textual_note_export": textual_export_counts,
        "included_translation_note_refs": len(notes),
        "included_translation_note_total": sum(len(items) for items in notes.values()),
        "name_meaning_note_filter": name_note_counts,
        "included_name_meaning_note_refs": len(name_notes),
        "included_name_meaning_note_total": sum(len(items) for items in name_notes.values()),
        "supplemental_notes": {
            "enabled": False,
            "reason": "Excluded for compact print proof.",
            "included_refs": 0,
            "included_total": 0,
        },
        "full_crossrefs": full_crossref_diag,
        "minimal_crossrefs": minimal_crossref_diag,
        "versification_map": versification_map_diag,
        "print_profile": {
            "layout": "compact_two_column",
            "book_prefaces": "excluded",
            "brenton_supplemental_notes": "excluded",
            "openbible_fallback": "excluded",
            "name_meanings": "listed_first_source_occurrence_only",
            "tsk_study_note_text": "excluded",
        },
        "print_docx": vars(print_stats),
        "validations": [validation],
        "outputs": {
            "print_docx": str(args.output),
            "diagnostics": str(args.diagnostics),
            "readme": str(args.readme),
        },
    }
    args.diagnostics.parent.mkdir(parents=True, exist_ok=True)
    args.diagnostics.write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_readme(args.readme, docx_path=args.output, diagnostics_path=args.diagnostics, diagnostics=diagnostics)
    print(json.dumps(diagnostics["outputs"], indent=2))


if __name__ == "__main__":
    main()
