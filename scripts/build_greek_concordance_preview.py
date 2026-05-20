#!/usr/bin/env python3
"""Build a separate compact Greek-driven concordance preview.

The source rows do not yet carry full lemmatization or word-level alignment.
This preview therefore starts from a curated Greek form table, scans the LXX/TR
Greek source text, and groups each Greek-term hit by the English rendering seen
in the draft translation.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

import build_print_proof_bible as print_builder


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TERMS = ROOT / "data" / "research" / "greek_concordance_terms.csv"
DEFAULT_OT = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
DEFAULT_NT = ROOT / "data" / "raw" / "tr_greek" / "nt_full.csv"
DEFAULT_OUTPUT = ROOT / "output" / "concordance" / "the_greek_heritage_study_bible_greek_concordance_preview.md"
DEFAULT_DIAGNOSTICS = (
    ROOT / "output" / "concordance" / "the_greek_heritage_study_bible_greek_concordance_preview_diagnostics.json"
)

GREEK_TOKEN_RE = re.compile(r"[Ͱ-Ͽ]+")


@dataclass(frozen=True)
class Term:
    entry_id: str
    english_heading: str
    greek_lemma: str
    transliteration: str
    testament: str
    greek_forms: frozenset[str]
    english_renderings: tuple[str, ...]
    priority: str
    note: str


@dataclass(frozen=True)
class VerseRow:
    ref: str
    book_name: str
    source_stream: str
    greek_text: str
    draft_translation: str


def normalize_greek(value: str) -> str:
    decomposed = unicodedata.normalize("NFD", value.casefold())
    stripped = "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")
    return unicodedata.normalize("NFC", stripped).replace("ς", "σ")


def greek_tokens(value: str) -> set[str]:
    return {normalize_greek(match.group(0)) for match in GREEK_TOKEN_RE.finditer(value)}


def normalize_english(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip()


def load_terms(path: Path) -> list[Term]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    terms: list[Term] = []
    for row in rows:
        if row["include"].strip().lower() not in {"yes", "true", "1"}:
            continue
        forms = {
            normalize_greek(form.strip())
            for form in row["greek_forms"].split(";")
            if form.strip()
        }
        forms.add(normalize_greek(row["greek_lemma"]))
        renderings = tuple(
            rendering.strip()
            for rendering in row["english_renderings"].split(";")
            if rendering.strip()
        )
        terms.append(
            Term(
                entry_id=row["entry_id"].strip(),
                english_heading=row["english_heading"].strip(),
                greek_lemma=row["greek_lemma"].strip(),
                transliteration=row["transliteration"].strip(),
                testament=row["testament"].strip().lower() or "both",
                greek_forms=frozenset(forms),
                english_renderings=renderings,
                priority=row["priority"].strip(),
                note=row["note"].strip(),
            )
        )
    return terms


def count_configured_terms(path: Path) -> tuple[int, int]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    included = sum(1 for row in rows if row["include"].strip().lower() in {"yes", "true", "1"})
    return len(rows), included


def load_source_rows(path: Path, source_stream: str) -> list[VerseRow]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = []
        for row in csv.DictReader(handle):
            greek_text = row["greek_text"].strip()
            if greek_text == "MT-only insertion; no LXX Greek row":
                continue
            rows.append(
                VerseRow(
                    ref=row["ref"],
                    book_name=row["book_name"],
                    source_stream=source_stream,
                    greek_text=greek_text,
                    draft_translation=row["draft_translation"],
                )
            )
    return rows


def term_applies(term: Term, source_stream: str) -> bool:
    return term.testament in {"both", source_stream}


def rendering_bucket(term: Term, draft_translation: str) -> str:
    normalized = normalize_english(draft_translation)
    for rendering in term.english_renderings:
        if re.search(rf"\b{re.escape(normalize_english(rendering))}\b", normalized):
            return rendering
    return "other rendering"


def format_refs(refs: list[str]) -> str:
    return "; ".join(print_builder.abbreviate_print_crossref(ref) for ref in refs)


def build_concordance(terms: list[Term], verses: list[VerseRow]) -> tuple[str, dict[str, object]]:
    term_matches: dict[str, dict[str, list[str]]] = {}
    term_totals: Counter[str] = Counter()
    rendering_totals: Counter[str] = Counter()

    verse_tokens = [(verse, greek_tokens(verse.greek_text)) for verse in verses]

    for term in terms:
        groups: dict[str, list[str]] = defaultdict(list)
        for verse, tokens in verse_tokens:
            if not term_applies(term, verse.source_stream):
                continue
            if tokens.isdisjoint(term.greek_forms):
                continue
            bucket = rendering_bucket(term, verse.draft_translation)
            groups[bucket].append(verse.ref)
            term_totals[term.entry_id] += 1
            rendering_totals[f"{term.entry_id}:{bucket}"] += 1
        term_matches[term.entry_id] = dict(groups)

    lines = [
        "# Greek-Driven Concordance Preview",
        "",
        "Separate working preview for a possible compact print appendix. Entries are driven by curated Greek source forms, not by English surface words alone. Verse lists use the current project numbering.",
        "",
        "This is not wired into the print Bible yet. It is a sizing and usefulness draft.",
        "",
    ]

    for term in terms:
        groups = term_matches[term.entry_id]
        if not groups:
            continue
        lines.extend(
            [
                f"## {term.english_heading}",
                "",
                f"Greek: {term.greek_lemma} ({term.transliteration}). {term.note}",
                "",
            ]
        )
        for rendering in sorted(groups, key=lambda key: (key == "other rendering", key.casefold())):
            refs = groups[rendering]
            lines.extend(
                [
                    f"**{rendering}** ({len(refs)}): {format_refs(refs)}",
                    "",
                ]
            )

    markdown = "\n".join(lines).rstrip() + "\n"
    word_count = len(re.findall(r"\S+", markdown))
    diagnostics: dict[str, object] = {
        "terms_configured": len(terms),
        "terms_with_matches": sum(1 for term in terms if term_matches[term.entry_id]),
        "source_rows_scanned": len(verses),
        "total_greek_term_hits": sum(term_totals.values()),
        "rough_word_count": word_count,
        "rough_page_estimate_at_450_words": round(word_count / 450, 1),
        "page_budget_target": 30,
        "term_hit_counts": dict(term_totals),
        "rendering_hit_counts": dict(rendering_totals),
        "method": "curated Greek forms normalized for accents/final sigma, grouped by English rendering hints in draft_translation",
        "reference_format": "print book abbreviations via build_print_proof_bible.abbreviate_print_crossref",
    }
    return markdown, diagnostics


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--terms", type=Path, default=DEFAULT_TERMS)
    parser.add_argument("--ot-source", type=Path, default=DEFAULT_OT)
    parser.add_argument("--nt-source", type=Path, default=DEFAULT_NT)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--diagnostics", type=Path, default=DEFAULT_DIAGNOSTICS)
    args = parser.parse_args()

    configured_terms, included_terms = count_configured_terms(args.terms)
    terms = load_terms(args.terms)
    verses = load_source_rows(args.ot_source, "ot") + load_source_rows(args.nt_source, "nt")
    markdown, diagnostics = build_concordance(terms, verses)
    diagnostics["terms_configured"] = configured_terms
    diagnostics["terms_in_table"] = configured_terms
    diagnostics["terms_included"] = included_terms

    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.diagnostics.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.write_text(markdown, encoding="utf-8")
    args.diagnostics.write_text(json.dumps(diagnostics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(diagnostics, ensure_ascii=False))


if __name__ == "__main__":
    main()
