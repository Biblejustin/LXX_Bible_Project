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
CROSSREF_EXCLUSION_POLICY = (
    "Generated TSK/OpenBible cross-reference footnotes are excluded from the "
    "physical proof; use the Logos/reference-note edition for dense "
    "cross-references."
)
OPTIONAL_TSK_CROSSREF_POLICY = (
    "Minimal cross-reference layer: TSK phrase-anchored references only, no "
    "OpenBible fallback, capped to one cross-reference footnote per verse and "
    "two references per footnote. This layer is opt-in for print builds."
)
SUPPLEMENTAL_POLICY = (
    "Brenton/source supplemental footnotes are excluded; this copy keeps only "
    "reviewed translation/textual notes and name meanings."
)
NAME_MEANING_POLICY = (
    "Name-meaning notes are included only at their listed first/source occurrence "
    "to keep the physical proof shorter."
)
PRINT_NOTE_LABEL_LEGEND = (
    "Print note label legend: T = translation note; Txt = textual note; "
    "MT/LXX = Masoretic/LXX difference; Heb = Hebrew divine title; "
    "Gk = Greek form or Greek LXX divine title; Tr = transliterated proper noun; "
    "Std = standard English equivalent; Src = source form; Nm = name meaning; "
    "Pn = personal name; Pl = place name; Ppl = people name; "
    "Div = divine or supernatural name; "
    "Eng = common English rendering."
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
    lulu_profile = diagnostics["print_profile"].get("margin_profile") == "lulu_pod_safe"
    preface_line = (
        "- Book preface pages included."
        if diagnostics["print_profile"]["book_prefaces"] == "included"
        else "- Book preface pages excluded for POD page-count limits."
    )
    generated_files = [
        f"- `{docx_path.name}`: compact DOCX for inexpensive physical proofreading.",
        f"- `{diagnostics_path.name}`: build counts and DOCX validation details.",
    ]
    if lulu_profile:
        generated_files.append(f"- `{docx_path.with_suffix('.pdf').name}`: Lulu-ready upload PDF.")
    rebuild_command = "make build-print-proof-lulu-pdf" if lulu_profile else "make build-print-proof"
    lines = [
        "# Print Proof Files",
        "",
        "Generated files:",
        "",
        *generated_files,
        "",
        "Profile:",
        "",
        "- Combined Genesis-Revelation text.",
        "- OT source: LXX Greek source rows; NT source: Scrivener 1894 Textus Receptus Greek source rows.",
        (
            "- Compact single-column DOCX layout with Lulu-safe mirrored POD margins."
            if diagnostics["print_profile"].get("margin_profile") == "lulu_pod_safe"
            else "- Compact single-column DOCX layout with narrow margins."
        ),
        f"- Page size: {diagnostics['print_profile']['page_size']}.",
        f"- Margins: {diagnostics['print_profile']['margins']}.",
        "- Front matter includes an LXX-to-English numbering guide for major reader-facing divergences.",
        "- Reviewed translation/textual notes included.",
        f"- Type profile: {diagnostics['print_profile']['type_profile']}.",
        f"- {PRINT_NOTE_LABEL_LEGEND}",
        f"- {NAME_MEANING_POLICY}",
        preface_line,
        "- Brenton/source supplemental notes excluded.",
        f"- {CROSSREF_EXCLUSION_POLICY}",
        "",
        "Counts:",
        "",
        f"- Verses: `{diagnostics['verse_rows']}`",
        f"- Book preface pages: `{stats['book_preface_pages']}`",
        f"- Translation/textual note footnotes: `{stats['translation_note_footnotes']}`",
        f"- Name-meaning footnotes: `{stats['name_meaning_footnotes']}`",
        f"- Cross-reference footnotes: `{stats['crossref_footnotes']}`",
        f"- Cross-reference refs kept: `{minimal['output_refs']}`",
        f"- Supplemental/Brenton footnotes: `{stats['supplemental_note_footnotes']}`",
        "",
        "Rebuild:",
        "",
        "```bash",
        rebuild_command,
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
    parser.add_argument("--book-intros", type=Path, default=builder.DEFAULT_BOOK_INTROS)
    parser.add_argument(
        "--no-book-prefaces",
        action="store_true",
        help="Omit book preface pages for POD page-count limits.",
    )
    parser.add_argument("--versification-map", type=Path, default=builder.DEFAULT_VERSIFICATION_MAP)
    parser.add_argument("--textual-notes-html", type=Path, default=builder.DEFAULT_TEXTUAL_NOTES_HTML)
    parser.add_argument("--book", help="Limit generated proof copy to one book name or book code.")
    parser.add_argument("--output", type=Path, default=DEFAULT_DOCX)
    parser.add_argument("--diagnostics", type=Path, default=DEFAULT_DIAGNOSTICS)
    parser.add_argument("--readme", type=Path, default=DEFAULT_README)
    parser.add_argument("--max-crossref-refs", type=int, default=2)
    parser.add_argument(
        "--include-tsk-crossrefs",
        action="store_true",
        help="Opt into the thinned TSK cross-reference layer for a less compact print proof.",
    )
    parser.add_argument(
        "--lulu-pod-margins",
        action="store_true",
        help="Use mirrored POD margins for Lulu thick-volume PDF uploads.",
    )
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
    if args.no_book_prefaces:
        book_intros = {}
        book_intro_diag = {
            "present": args.book_intros.exists(),
            "path": str(args.book_intros),
            "rows": 0,
            "usable_rows": 0,
            "included": False,
            "reason": "Omitted by --no-book-prefaces for POD page-count limits.",
        }
        book_prefaces_profile = "excluded"
    else:
        book_intros, book_intro_diag = builder.load_book_intros(args.book_intros)
        book_intro_diag = {**book_intro_diag, "included": True}
        book_prefaces_profile = "included"
    if args.include_tsk_crossrefs:
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
        crossref_policy = OPTIONAL_TSK_CROSSREF_POLICY
        crossrefs_enabled = True
    else:
        full_crossrefs = {}
        full_crossref_diag = {
            "enabled": False,
            "reason": "Generated cross-reference layer excluded from compact print proof.",
            "source_policy": "TSK/OpenBible omitted.",
        }
        minimal_crossrefs = {}
        minimal_crossref_diag = {
            "enabled": False,
            "profile": "print_no_generated_crossrefs",
            "source_policy": "TSK/OpenBible omitted.",
            "selection_policy": "Generated cross-reference footnotes excluded for compact physical proofreading.",
            "input_groups": 0,
            "input_refs": 0,
            "output_groups": 0,
            "output_refs": 0,
            "max_groups_per_verse": 0,
            "max_refs_per_note": 0,
            "verses_with_crossrefs": 0,
        }
        crossref_policy = CROSSREF_EXCLUSION_POLICY
        crossrefs_enabled = False
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
        book_intros=book_intros,
        logos=False,
        datatype="Bible",
        milestone_mode="lxx",
        versification_map=versification_map,
        verse_counts=verse_counts,
        footnote_number_restart="page",
        place_links={},
        place_link_pattern=None,
        crossrefs_enabled=crossrefs_enabled,
        compact_translation_note_labels=True,
        compact_name_note_labels=True,
        docx_compresslevel=args.docx_compresslevel,
        compact_print=True,
        lulu_pod_margins=args.lulu_pod_margins,
        output_kind="print_proof",
        subtitle="Compact physical proofreading copy",
        crossref_policy=crossref_policy,
        name_policy=NAME_MEANING_POLICY,
        supplemental_policy=SUPPLEMENTAL_POLICY,
        note_label_legend=PRINT_NOTE_LABEL_LEGEND,
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
        "book_prefaces": book_intro_diag,
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
            "layout": "compact_single_column",
            "margin_profile": "lulu_pod_safe" if args.lulu_pod_margins else "compact_proof",
            "page_size": "US Letter 8.5 x 11 in",
            "type_profile": "lulu_tight_leading_9_5pt" if args.lulu_pod_margins else "compact_9_5pt",
            "margins": (
                "mirrored; inside 1.0 in; outside 0.75 in; top/bottom 0.5 in"
                if args.lulu_pod_margins
                else "top/bottom 0.5 in; left/right 0.375 in"
            ),
            "book_prefaces": book_prefaces_profile,
            "brenton_supplemental_notes": "excluded",
            "openbible_fallback": "excluded",
            "generated_crossrefs": "excluded",
            "name_meanings": "listed_first_source_occurrence_only",
            "source_policy": "OT LXX Greek rows plus NT Scrivener 1894 Textus Receptus Greek rows.",
            "translation_note_labels": "compact",
            "name_note_labels": "compact",
            "note_label_legend": PRINT_NOTE_LABEL_LEGEND,
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
