#!/usr/bin/env python3
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DECISION_QUEUE = ROOT / "output" / "fresh_vs_brenton_ot_decision_queue.csv"
OT_SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
REVIEW_PASS = ROOT / "data" / "research" / "ot_review_pass_01.md"
LOGOS_SCAN = ROOT / "data" / "research" / "local" / "logos_scan" / "logos_translation_resources.csv"
OUT_DIR = ROOT / "data" / "research" / "local" / "witness_review"
OUT_CSV = OUT_DIR / "ot_witness_matrix.csv"
OUT_RESOURCES = OUT_DIR / "resource_shortlist.csv"
OUT_README = OUT_DIR / "README.md"


GENERIC_RESOURCE_IDS = {
    "greek_base_rahlfs": [
        "LLS:LOGOSLXX",
        "LXXSESB",
        "LLS:LLXXI",
    ],
    "greek_swete": [
        "LLS:OTGRKSWETETXT",
        "LLS:OTGRKSWETEINTTXT",
        "LLS:OTGRKSWETEAPP",
    ],
    "greek_apparatus": [
        "LLS:LXXCAPP",
        "INTERACTIVE:LXX-MANUSCRIPT-EXPLORER",
        "LLS:OTGRKSWETEAPP",
    ],
    "english_les": [
        "LLS:LELXX2",
        "LLS:LELXX",
    ],
    "english_nets": [
        "LLS:NETSOXFORD",
    ],
    "english_saas": [
        "LLS:STATHANASIUSSEPT",
    ],
}


BOOK_RESOURCE_IDS = {
    "Genesis": {
        "greek_gottingen": ["LLS:GSI01GE"],
        "greek_apparatus": ["LLS:GSI01GECAPP1", "LLS:GSI01GECAPP2"],
    },
    "Exodus": {
        "greek_gottingen": ["LLS:GSII02EX"],
        "greek_apparatus": ["LLS:GSII02EXCAPP1", "LLS:GSII02EXCAPP2"],
    },
    "Leviticus": {
        "greek_gottingen": ["LLS:GSII02LE"],
        "greek_apparatus": ["LLS:GSII02LECAPP1", "LLS:GSII02LECAPP2"],
    },
    "Numbers": {
        "greek_gottingen": ["LLS:GSIII1NU"],
        "greek_apparatus": ["LLS:GSIII1NUCAPP1", "LLS:GSIII1NUCAPP2"],
    },
    "Deuteronomy": {
        "greek_gottingen": ["LLS:GSIII2DE"],
        "greek_apparatus": ["LLS:GSIII2DECAPP1", "LLS:GSIII2DECAPP2"],
    },
    "Ruth": {
        "greek_gottingen": ["LLS:GSIV3RU"],
        "greek_apparatus": ["LLS:GSIV3RUCAPP1", "LLS:GSIV3RUCAPP2"],
    },
    "Ezra": {
        "greek_gottingen": ["LLS:GSVIII2ES2"],
        "greek_apparatus": ["LLS:GSVIII2ES2CAPP"],
    },
    "Esther": {
        "greek_gottingen": ["LLS:GSVIII3ES"],
        "greek_apparatus": ["LLS:GSVIII3ESCAPP"],
    },
    "Job": {
        "greek_gottingen": ["LLS:GSXI4JOB"],
        "greek_apparatus": ["LLS:GSXI4JOBCAPP1", "LLS:GSXI4JOBCAPP2"],
    },
    "Psalms": {
        "greek_gottingen": ["LLS:GSXPS"],
        "greek_apparatus": ["LLS:GSXPSCAPP"],
    },
    "Isaiah": {
        "greek_gottingen": ["LLS:GSXIVIS"],
        "greek_apparatus": ["LLS:GSXIVISCAPP1", "LLS:GSXIVISCAPP2"],
    },
    "Jeremiah": {
        "greek_gottingen": ["LLS:GSXVJER"],
        "greek_apparatus": ["LLS:GSXVJERCAPP1", "LLS:GSXVJERCAPP2"],
    },
    "Ezekiel": {
        "greek_gottingen": ["LLS:GSXVI1EZE"],
        "greek_apparatus": ["LLS:GSXVI1EZECAPP1", "LLS:GSXVI1EZECAPP2"],
    },
    "Hosea": {
        "greek_gottingen": ["LLS:GSXIIIPRPH"],
        "greek_apparatus": ["LLS:GSXIIIPRPHCAPP1", "LLS:GSXIIIPRPHCAPP2"],
    },
    "Joel": {
        "greek_gottingen": ["LLS:GSXIIIPRPH"],
        "greek_apparatus": ["LLS:GSXIIIPRPHCAPP1", "LLS:GSXIIIPRPHCAPP2"],
    },
    "Amos": {
        "greek_gottingen": ["LLS:GSXIIIPRPH"],
        "greek_apparatus": ["LLS:GSXIIIPRPHCAPP1", "LLS:GSXIIIPRPHCAPP2"],
    },
    "Obadiah": {
        "greek_gottingen": ["LLS:GSXIIIPRPH"],
        "greek_apparatus": ["LLS:GSXIIIPRPHCAPP1", "LLS:GSXIIIPRPHCAPP2"],
    },
    "Jonah": {
        "greek_gottingen": ["LLS:GSXIIIPRPH"],
        "greek_apparatus": ["LLS:GSXIIIPRPHCAPP1", "LLS:GSXIIIPRPHCAPP2"],
    },
    "Micah": {
        "greek_gottingen": ["LLS:GSXIIIPRPH"],
        "greek_apparatus": ["LLS:GSXIIIPRPHCAPP1", "LLS:GSXIIIPRPHCAPP2"],
    },
    "Nahum": {
        "greek_gottingen": ["LLS:GSXIIIPRPH"],
        "greek_apparatus": ["LLS:GSXIIIPRPHCAPP1", "LLS:GSXIIIPRPHCAPP2"],
    },
    "Habakkuk": {
        "greek_gottingen": ["LLS:GSXIIIPRPH", "LLS:GSXIIIHAB3"],
        "greek_apparatus": ["LLS:GSXIIIPRPHCAPP1", "LLS:GSXIIIPRPHCAPP2", "LLS:GSXIIIHAB3CAPP"],
    },
    "Zephaniah": {
        "greek_gottingen": ["LLS:GSXIIIPRPH"],
        "greek_apparatus": ["LLS:GSXIIIPRPHCAPP1", "LLS:GSXIIIPRPHCAPP2"],
    },
    "Haggai": {
        "greek_gottingen": ["LLS:GSXIIIPRPH"],
        "greek_apparatus": ["LLS:GSXIIIPRPHCAPP1", "LLS:GSXIIIPRPHCAPP2"],
    },
    "Zechariah": {
        "greek_gottingen": ["LLS:GSXIIIPRPH"],
        "greek_apparatus": ["LLS:GSXIIIPRPHCAPP1", "LLS:GSXIIIPRPHCAPP2"],
    },
    "Malachi": {
        "greek_gottingen": ["LLS:GSXIIIPRPH"],
        "greek_apparatus": ["LLS:GSXIIIPRPHCAPP1", "LLS:GSXIIIPRPHCAPP2"],
    },
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def parse_review_pass(path: Path) -> dict[str, dict[str, str]]:
    data: dict[str, dict[str, str]] = {}
    current_ref = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("## "):
            current_ref = line[3:].strip()
            data[current_ref] = {"ref": current_ref}
        elif current_ref and line.startswith("- status:"):
            match = re.search(r"`([^`]+)`", line)
            data[current_ref]["pass_status"] = match.group(1) if match else line.removeprefix("- status:").strip()
        elif current_ref and line.startswith("- focus:"):
            match = re.search(r"`([^`]+)`", line)
            data[current_ref]["focus"] = match.group(1) if match else line.removeprefix("- focus:").strip()
        elif current_ref and line.startswith("- reason:"):
            data[current_ref]["reason"] = line.removeprefix("- reason:").strip()
        elif current_ref and line.startswith("- change:"):
            data[current_ref]["change"] = line.removeprefix("- change:").strip()
    return data


def load_ot_rows(path: Path) -> dict[str, dict[str, str]]:
    return {row["ref"]: row for row in load_csv(path)}


def first_matching_resources(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="ignore", newline="") as handle:
        return list(csv.DictReader(handle))


def shortlist_resources_for_books(rows: list[dict[str, str]], relevant_books: set[str]) -> list[dict[str, str]]:
    rows_by_id = {row.get("resource_id", ""): row for row in rows}
    out = []
    seen = set()
    for slot, resource_ids in GENERIC_RESOURCE_IDS.items():
        for rid in resource_ids:
            row = rows_by_id.get(rid)
            if not row:
                continue
            key = (slot, rid, "")
            if key in seen:
                continue
            seen.add(key)
            out.append(
                {
                    "slot": slot,
                    "book_scope": "",
                    "resource_id": rid,
                    "title": row.get("title", ""),
                    "short_title": row.get("short_title", ""),
                    "path": row.get("path", ""),
                }
            )

    for book in sorted(relevant_books):
        for slot, resource_ids in BOOK_RESOURCE_IDS.get(book, {}).items():
            for rid in resource_ids:
                row = rows_by_id.get(rid)
                if not row:
                    continue
                key = (slot, rid, book)
                if key in seen:
                    continue
                seen.add(key)
                out.append(
                    {
                        "slot": slot,
                        "book_scope": book,
                        "resource_id": rid,
                        "title": row.get("title", ""),
                        "short_title": row.get("short_title", ""),
                        "path": row.get("path", ""),
                    }
                )
    return out


def resource_index(shortlist: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    out: dict[str, list[dict[str, str]]] = {}
    for row in shortlist:
        out.setdefault(row["slot"], []).append(row)
    return out


def label_for_resource(row: dict[str, str]) -> str:
    title = row["title"] or row["short_title"] or row["resource_id"]
    return f"{title} [{row['resource_id']}]".strip()


def pick_resource_label(
    resources: dict[str, list[dict[str, str]]],
    slot: str,
    book: str,
) -> str:
    rows = resources.get(slot, [])
    for row in rows:
        if row.get("book_scope") == book:
            return label_for_resource(row)
    for row in rows:
        if not row.get("book_scope"):
            return label_for_resource(row)
    return ""


def build_matrix_rows(
    decision_rows: list[dict[str, str]],
    review_map: dict[str, dict[str, str]],
    ot_rows: dict[str, dict[str, str]],
    resources: dict[str, list[dict[str, str]]],
) -> list[dict[str, str]]:
    status_rank = {"needs-logos": 0, "keep-provisional": 1, "revised": 2, "keep": 3}
    picked = []
    for row in decision_rows:
        meta = review_map.get(row["ref"])
        if not meta:
            continue
        if meta.get("pass_status") not in {"needs-logos", "keep-provisional"}:
            continue
        source_row = ot_rows.get(row["ref"], {})
        book = row["ref"].rsplit(" ", 1)[0]
        picked.append(
            {
                "sort_status": str(status_rank.get(meta.get("pass_status", "keep"), 9)),
                "sort_score": row["priority_score"],
                "ref": row["ref"],
                "priority_score": row["priority_score"],
                "pass_status": meta.get("pass_status", ""),
                "focus": meta.get("focus", ""),
                "reason": meta.get("reason", ""),
                "change_note": meta.get("change", ""),
                "greek_text": source_row.get("greek_text", ""),
                "our_draft": source_row.get("draft_translation", ""),
                "brenton_translation": row.get("brenton_translation", ""),
                "base_greek_resource": pick_resource_label(resources, "greek_base_rahlfs", book),
                "swete_resource": pick_resource_label(resources, "greek_swete", book),
                "gottingen_resource": pick_resource_label(resources, "greek_gottingen", book),
                "apparatus_resource": pick_resource_label(resources, "greek_apparatus", book),
                "les_resource": pick_resource_label(resources, "english_les", book),
                "nets_resource": pick_resource_label(resources, "english_nets", book),
                "saas_resource": pick_resource_label(resources, "english_saas", book),
                "base_greek_notes": "",
                "swete_notes": "",
                "gottingen_notes": "",
                "apparatus_notes": "",
                "les_notes": "",
                "nets_notes": "",
                "saas_notes": "",
                "smoothing_note": "",
                "textual_issue": "",
                "recommended_action": "",
                "final_decision": "",
                "reviewer_notes": "",
            }
        )
    picked.sort(key=lambda row: (int(row["sort_status"]), -int(row["sort_score"]), row["ref"]))
    out = []
    for index, row in enumerate(picked, start=1):
        row["order"] = str(index)
        out.append({k: v for k, v in row.items() if not k.startswith("sort_")})
    return out


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_readme(path: Path, resource_rows: list[dict[str, str]], matrix_rows: list[dict[str, str]]) -> None:
    by_slot: dict[str, list[dict[str, str]]] = {}
    for row in resource_rows:
        by_slot.setdefault(row["slot"], []).append(row)

    lines = [
        "# Private Witness Review",
        "",
        "Private workspace.",
        "Notes only.",
        "No long copyrighted quotations.",
        "",
        f"Seed rows: {len(matrix_rows)}",
        "",
        "Priority order:",
        "1. `needs-logos`",
        "2. `keep-provisional`",
        "",
        "Suggested workflow:",
        "1. Check base Greek vs Swete vs Göttingen vs apparatus.",
        "2. Compare LES / NETS / SAAS for smoothing or problem detection.",
        "3. Write notes, not copied text.",
        "4. Set `recommended_action` and `final_decision`.",
        "",
        "## Resource Shortlist",
        "",
    ]
    for slot, rows in by_slot.items():
        lines.append(f"### {slot}")
        for row in rows:
            title = row["title"] or row["short_title"] or row["resource_id"]
            scope = row.get("book_scope")
            if scope:
                lines.append(f"- {scope} → {title} [{row['resource_id']}]")
            else:
                lines.append(f"- {title} [{row['resource_id']}]")
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    decision_rows = load_csv(DECISION_QUEUE)
    ot_rows = load_ot_rows(OT_SOURCE)
    review_map = parse_review_pass(REVIEW_PASS)
    logos_rows = first_matching_resources(LOGOS_SCAN)
    pre_matrix_rows = build_matrix_rows(decision_rows, review_map, ot_rows, {})
    relevant_books = {row["ref"].rsplit(" ", 1)[0] for row in pre_matrix_rows}
    resource_rows = shortlist_resources_for_books(logos_rows, relevant_books)
    resources = resource_index(resource_rows)
    matrix_rows = build_matrix_rows(decision_rows, review_map, ot_rows, resources)
    if not matrix_rows:
        raise SystemExit("No witness-review rows selected.")
    write_csv(OUT_CSV, matrix_rows)
    write_csv(OUT_RESOURCES, resource_rows)
    write_readme(OUT_README, resource_rows, matrix_rows)
    print(OUT_CSV)
    print(OUT_RESOURCES)
    print(OUT_README)


if __name__ == "__main__":
    main()
