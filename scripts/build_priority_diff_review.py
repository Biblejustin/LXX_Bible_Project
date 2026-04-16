#!/usr/bin/env python3
import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

from build_idiom_consistency_review import FAMILIES
from build_crossref_clue_review import OPENBIBLE_BOOK_MAP, STANDARD_BOOK_NAMES, load_openbible_crossrefs, parse_openbible_ref


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RAW = DATA / "raw"
RESEARCH = DATA / "research"
DEFAULT_SOURCE = ROOT / "output" / "fresh_vs_brenton_ot_drafted.csv"
DEFAULT_OT_SOURCE = RAW / "lxx_greek" / "ot_full.csv"
DEFAULT_NT_IDIOMS = RESEARCH / "nt_idiom_parallels.csv"
DEFAULT_OUTPUT = ROOT / "output" / "fresh_vs_brenton_ot_priority_review.md"
DEFAULT_CSV = ROOT / "output" / "fresh_vs_brenton_ot_priority_review.csv"
DEFAULT_DIAGNOSTICS = ROOT / "output" / "fresh_vs_brenton_ot_priority_review_diagnostics.json"

IMPORTANCE_SCORE = {"none": 0, "low": 1, "medium": 2, "high": 4}
KEYWORD_RE = re.compile(
    r"\b("
    r"spirit|wind|soul|being|covenant|mercy|truth|righteous|righteousness|justice|law|altar|priest|"
    r"sacrifice|sin|forgive|salvation|savior|holy|holiness|lord|god|name|glory|king|anointed|"
    r"firstborn|shepherd|faith|grace|compassion|beloved|virgin|servant|messenger|angel|day one|"
    r"firm span|hades|abyss|seed|offspring|image|created|create|resurrection|repent|peace|judgment"
    r")\b",
    re.IGNORECASE,
)


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_by_ref(path: Path) -> dict[str, dict[str, str]]:
    return {row["ref"]: row for row in load_rows(path)}


def load_nt_parallels(path: Path) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in load_rows(path):
        grouped[row["family"]].append(row)
    return grouped


def family_map(source_by_ref: dict[str, dict[str, str]]) -> dict[str, set[str]]:
    mapped: dict[str, set[str]] = {}
    for ref, row in source_by_ref.items():
        greek = row.get("greek_text", "") or ""
        mapped[ref] = {family["name"] for family in FAMILIES if family["match"](greek)}
    return mapped


def nt_parallel_info(row: dict[str, str], source_by_ref: dict[str, dict[str, str]], nt_map: dict[str, list[dict[str, str]]]) -> tuple[int, list[str], list[str]]:
    source_row = source_by_ref.get(row["ref"])
    if not source_row:
        return 0, [], []
    greek = source_row.get("greek_text", "") or ""
    families = [family["name"] for family in FAMILIES if family["name"] in nt_map and family["match"](greek)]
    if not families:
        return 0, [], []
    refs: list[str] = []
    weights: list[int] = []
    for family_name in families:
        for nt_row in nt_map[family_name]:
            refs.append(nt_row["nt_ref"])
            weights.append(int(nt_row["weight"]))
    deduped_refs = list(dict.fromkeys(refs))
    return (max(weights) if weights else 0), families, deduped_refs


def crossref_info(
    row: dict[str, str],
    source_by_ref: dict[str, dict[str, str]],
    families_by_ref: dict[str, set[str]],
    crossrefs_by_ref: dict[str, list[dict[str, str]]],
) -> tuple[int, int, int, int]:
    top_vote = 0
    nt_count = 0
    shared_family_hits = 0
    targets = crossrefs_by_ref.get(row["ref"], [])
    source_families = families_by_ref.get(row["ref"], set())
    for target in targets:
        parsed = parse_openbible_ref(target["target_raw"])
        if not parsed:
            continue
        code, chapter, verse, _ = parsed
        votes = int(target["votes"])
        top_vote = max(top_vote, votes)
        if code not in source_by_ref and code in {
            "MAT", "MRK", "LUK", "JHN", "ACT", "ROM", "1CO", "2CO", "GAL", "EPH", "PHP",
            "COL", "1TH", "2TH", "1TI", "2TI", "TIT", "PHM", "HEB", "JAS", "1PE", "2PE",
            "1JN", "2JN", "3JN", "JUD", "REV",
        }:
            nt_count += 1
            continue
        target_ref = f"{STANDARD_BOOK_NAMES[code]} {chapter}:{verse}"
        target_families = families_by_ref.get(target_ref, set())
        if source_families and target_families and source_families & target_families:
            shared_family_hits += 1

    bonus = 0
    if top_vote >= 100:
        bonus += 3
    elif top_vote >= 50:
        bonus += 2
    elif top_vote >= 20:
        bonus += 1
    if nt_count:
        bonus += 1
    if shared_family_hits >= 2:
        bonus += 2
    elif shared_family_hits == 1:
        bonus += 1
    return bonus, top_vote, nt_count, shared_family_hits


def score_row(
    row: dict[str, str],
    source_by_ref: dict[str, dict[str, str]],
    nt_map: dict[str, list[dict[str, str]]],
    families_by_ref: dict[str, set[str]],
    crossrefs_by_ref: dict[str, list[dict[str, str]]],
) -> tuple[int, list[str], list[str], int, list[str], int, int, int]:
    text = f"{row.get('fresh_translation', '')} {row.get('brenton_translation', '')}"
    keyword_hits = sorted({match.group(0).lower() for match in KEYWORD_RE.finditer(text)})
    decision_count = int(row.get("decision_count", "0") or "0")
    footnote_count = int(row.get("footnote_count", "0") or "0")
    importance = row.get("importance", "none")
    nt_weight, nt_families, nt_refs = nt_parallel_info(row, source_by_ref, nt_map)
    crossref_bonus, crossref_top_vote, crossref_nt_count, crossref_shared_family_hits = crossref_info(
        row, source_by_ref, families_by_ref, crossrefs_by_ref
    )

    score = 0
    score += IMPORTANCE_SCORE.get(importance, 0)
    score += min(decision_count, 2) * 3
    score += min(footnote_count, 2) * 2
    score += len(keyword_hits) * 2
    score += nt_weight
    score += crossref_bonus
    score += 0 if row.get("same_normalized", "") == "yes" else 1

    reasons: list[str] = []
    if decision_count:
        reasons.append(f"decisions={decision_count}")
    if footnote_count:
        reasons.append(f"footnotes={footnote_count}")
    if importance != "none":
        reasons.append(f"importance={importance}")
    if keyword_hits:
        reasons.append("keywords=" + ", ".join(keyword_hits[:6]))
    if nt_refs:
        reasons.append("nt=" + ", ".join(nt_refs[:4]))
    if crossref_top_vote:
        reasons.append(f"crossref_top_vote={crossref_top_vote}")
    if crossref_shared_family_hits:
        reasons.append(f"crossref_shared_family={crossref_shared_family_hits}")

    return (
        score,
        keyword_hits,
        reasons,
        nt_weight,
        nt_refs,
        crossref_top_vote,
        crossref_nt_count,
        crossref_shared_family_hits,
    )


def build_priority_rows(
    rows: list[dict[str, str]],
    per_book_limit: int,
    min_score: int,
    source_by_ref: dict[str, dict[str, str]],
    nt_map: dict[str, list[dict[str, str]]],
    families_by_ref: dict[str, set[str]],
    crossrefs_by_ref: dict[str, list[dict[str, str]]],
) -> list[dict[str, str]]:
    grouped: dict[str, list[tuple[int, int, dict[str, str], list[str], list[str]]]] = defaultdict(list)
    for index, row in enumerate(rows):
        (
            score,
            keyword_hits,
            reasons,
            nt_weight,
            nt_refs,
            crossref_top_vote,
            crossref_nt_count,
            crossref_shared_family_hits,
        ) = score_row(row, source_by_ref, nt_map, families_by_ref, crossrefs_by_ref)
        if score < min_score:
            continue
        enriched = dict(row)
        enriched["nt_parallel_weight"] = str(nt_weight)
        enriched["nt_parallel_count"] = str(len(nt_refs))
        enriched["nt_parallel_refs"] = ", ".join(nt_refs)
        enriched["crossref_top_vote"] = str(crossref_top_vote)
        enriched["crossref_nt_count"] = str(crossref_nt_count)
        enriched["crossref_shared_family_hits"] = str(crossref_shared_family_hits)
        grouped[row["book_name"]].append((score, index, enriched, keyword_hits, reasons))

    selected: list[tuple[int, dict[str, str], list[str], list[str]]] = []
    for book_rows in grouped.values():
        ranked = sorted(book_rows, key=lambda item: (-item[0], item[1]))[:per_book_limit]
        selected.extend((item[1], item[2], item[3], item[4]) for item in ranked)

    selected.sort(key=lambda item: item[0])
    out_rows: list[dict[str, str]] = []
    for _, row, keyword_hits, reasons in selected:
        score = score_row(row, source_by_ref, nt_map, families_by_ref, crossrefs_by_ref)[0]
        out_rows.append(
            {
                "ref": row["ref"],
                "book_name": row["book_name"],
                "chapter": row["chapter"],
                "verse": row["verse"],
                "importance": row["importance"],
                "priority_score": str(score),
                "decision_count": row["decision_count"],
                "footnote_count": row["footnote_count"],
                "nt_parallel_count": row.get("nt_parallel_count", "0"),
                "nt_parallel_weight": row.get("nt_parallel_weight", "0"),
                "nt_parallel_refs": row.get("nt_parallel_refs", ""),
                "crossref_top_vote": row.get("crossref_top_vote", "0"),
                "crossref_nt_count": row.get("crossref_nt_count", "0"),
                "crossref_shared_family_hits": row.get("crossref_shared_family_hits", "0"),
                "keyword_hits": ", ".join(keyword_hits),
                "reasons": "; ".join(reasons),
                "fresh_translation": row["fresh_translation"],
                "brenton_translation": row["brenton_translation"],
            }
        )
    return out_rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_markdown(rows: list[dict[str, str]], per_book_limit: int, min_score: int) -> str:
    by_book: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_book[row["book_name"]].append(row)

    lines = [
        "# OT Priority Difference Review",
        "",
        f"Per-book limit: {per_book_limit}",
        f"Minimum score: {min_score}",
        f"Selected verses: {len(rows)}",
        "",
        "Use:",
        "- review verses most likely to matter for theology or core language choices",
        "- not exhaustive",
        "",
        "## By Book",
    ]
    for book, book_rows in by_book.items():
        lines.append(f"- {book}: {len(book_rows)}")

    for book, book_rows in by_book.items():
        lines.append("")
        lines.append(f"## {book}")
        for row in book_rows:
            lines.append("")
            lines.append(f"### {row['ref']}")
            lines.append(f"- score: {row['priority_score']}")
            lines.append(f"- reasons: {row['reasons']}")
            if row.get("nt_parallel_refs"):
                lines.append(f"- nt refs: {row['nt_parallel_refs']}")
            if row.get("crossref_top_vote") not in {"", "0"}:
                lines.append(f"- crossref top vote: {row['crossref_top_vote']}")
            if row.get("crossref_shared_family_hits") not in {"", "0"}:
                lines.append(f"- crossref shared-family hits: {row['crossref_shared_family_hits']}")
            lines.append(f"- fresh: {row['fresh_translation']}")
            lines.append(f"- brenton: {row['brenton_translation'] or '[missing]'}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--ot-source", default=str(DEFAULT_OT_SOURCE))
    parser.add_argument("--nt-idioms", default=str(DEFAULT_NT_IDIOMS))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--csv-output", default=str(DEFAULT_CSV))
    parser.add_argument("--diagnostics", default=str(DEFAULT_DIAGNOSTICS))
    parser.add_argument("--per-book-limit", type=int, default=6)
    parser.add_argument("--min-score", type=int, default=4)
    args = parser.parse_args()

    source_rows = load_rows(Path(args.source))
    source_by_ref = load_by_ref(Path(args.ot_source))
    nt_map = load_nt_parallels(Path(args.nt_idioms))
    families_by_ref = family_map(source_by_ref)
    crossrefs_by_ref = load_openbible_crossrefs()
    priority_rows = build_priority_rows(
        source_rows,
        args.per_book_limit,
        args.min_score,
        source_by_ref,
        nt_map,
        families_by_ref,
        crossrefs_by_ref,
    )
    if not priority_rows:
        raise SystemExit("No priority rows selected.")

    output_path = Path(args.output)
    csv_path = Path(args.csv_output)
    diagnostics_path = Path(args.diagnostics)

    output_path.write_text(build_markdown(priority_rows, args.per_book_limit, args.min_score), encoding="utf-8")
    write_csv(csv_path, priority_rows)
    diagnostics_path.write_text(
        json.dumps(
            {
                "source": str(Path(args.source)),
                "selected_rows": len(priority_rows),
                "per_book_limit": args.per_book_limit,
                "min_score": args.min_score,
                "rows_with_nt_parallels": sum(1 for row in priority_rows if row.get("nt_parallel_count") not in {"", "0"}),
                "rows_with_crossref_signal": sum(
                    1
                    for row in priority_rows
                    if row.get("crossref_top_vote") not in {"", "0"} or row.get("crossref_shared_family_hits") not in {"", "0"}
                ),
                "books": sorted({row["book_name"] for row in priority_rows}),
                "output": str(output_path),
                "csv_output": str(csv_path),
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": str(output_path),
                "csv_output": str(csv_path),
                "diagnostics": str(diagnostics_path),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
