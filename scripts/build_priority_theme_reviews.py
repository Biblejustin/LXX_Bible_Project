#!/usr/bin/env python3
import argparse
import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "output" / "fresh_vs_brenton_ot_priority_review.csv"
DEFAULT_OUTPUT_DIR = ROOT / "output" / "priority_themes"
DEFAULT_OVERVIEW = ROOT / "output" / "fresh_vs_brenton_ot_theme_overview.md"

THEMES = {
    "theology_divine_identity": {
        "title": "Theology / Divine Identity",
        "description": "Name, identity, attributes, titles, and direct God-language.",
        "keywords": {
            "name",
            "glory",
            "holy",
            "holiness",
            "mercy",
            "truth",
            "grace",
            "compassion",
            "messenger",
            "angel",
        },
    },
    "creation_anthropology": {
        "title": "Creation / Anthropology",
        "description": "Creation language, human nature, life-breath, image, seed, cosmic terms.",
        "keywords": {
            "spirit",
            "wind",
            "soul",
            "being",
            "image",
            "created",
            "create",
            "day one",
            "firm span",
            "abyss",
            "seed",
            "offspring",
            "firstborn",
        },
    },
    "covenant_law_judgment": {
        "title": "Covenant / Law / Judgment",
        "description": "Covenant, law, sin, justice, righteousness, repentance, judgment.",
        "keywords": {
            "covenant",
            "law",
            "sin",
            "forgive",
            "judgment",
            "justice",
            "righteous",
            "righteousness",
            "faith",
            "repent",
        },
    },
    "ritual_priesthood": {
        "title": "Ritual / Priesthood",
        "description": "Altar, sacrifice, priesthood, holiness in cultic setting.",
        "keywords": {
            "altar",
            "priest",
            "sacrifice",
            "holy",
            "holiness",
            "sin",
            "forgive",
            "salvation",
        },
    },
    "kingship_messianic": {
        "title": "Kingship / Messianic",
        "description": "Royal, shepherd, servant, anointed, peace, savior language.",
        "keywords": {
            "king",
            "anointed",
            "shepherd",
            "servant",
            "beloved",
            "peace",
            "salvation",
            "savior",
            "seed",
            "offspring",
            "firstborn",
        },
    },
    "death_afterlife": {
        "title": "Death / Afterlife",
        "description": "Death, grave, hades, resurrection, soul-language in death contexts.",
        "keywords": {
            "hades",
            "resurrection",
        },
    },
    "textual_lexical": {
        "title": "Textual / Lexical Crux",
        "description": "Fallback bucket for hard wording, textual variation, lexical judgment.",
        "keywords": set(),
    },
}


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for index, row in enumerate(rows):
        row["_source_index"] = str(index)
    return rows


def parse_keyword_hits(row: dict[str, str]) -> set[str]:
    return {item.strip().lower() for item in (row.get("keyword_hits") or "").split(",") if item.strip()}


def classify_row(row: dict[str, str]) -> list[str]:
    keyword_hits = parse_keyword_hits(row)
    importance = row.get("importance", "none")
    decision_count = int(row.get("decision_count", "0") or "0")
    footnote_count = int(row.get("footnote_count", "0") or "0")
    matches: list[str] = []
    for slug, theme in THEMES.items():
        if slug == "textual_lexical":
            continue
        if keyword_hits & theme["keywords"]:
            matches.append(slug)

    if not matches:
        if decision_count or footnote_count or importance in {"high", "medium"}:
            matches.append("textual_lexical")
    elif decision_count >= 2 or footnote_count >= 2:
        matches.append("textual_lexical")

    return matches


def sort_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return sorted(rows, key=lambda row: int(row["_source_index"]))


def balanced_top_refs(rows: list[dict[str, str]], limit: int = 5, per_book_limit: int = 1) -> list[dict[str, str]]:
    ranked = sorted(rows, key=lambda row: (-int(row["priority_score"]), int(row["_source_index"])))
    counts: dict[str, int] = defaultdict(int)
    selected: list[dict[str, str]] = []
    for row in ranked:
        book = row["book_name"]
        if counts[book] >= per_book_limit:
            continue
        selected.append(row)
        counts[book] += 1
        if len(selected) >= limit:
            break
    return selected


def build_theme_markdown(slug: str, rows: list[dict[str, str]]) -> str:
    theme = THEMES[slug]
    books = sorted({row["book_name"] for row in rows})
    lines = [
        f"# {theme['title']}",
        "",
        theme["description"],
        "",
        f"Rows: {len(rows)}",
        f"Books: {len(books)}",
        "",
    ]
    for row in rows:
        lines.append(f"## {row['ref']}")
        lines.append(f"- score: {row['priority_score']}")
        lines.append(f"- reasons: {row['reasons']}")
        lines.append(f"- keywords: {row['keyword_hits'] or '[none]'}")
        lines.append(f"- fresh: {row['fresh_translation']}")
        lines.append(f"- brenton: {row['brenton_translation'] or '[missing]'}")
        lines.append("")
    return "\n".join(lines)


def build_index(theme_rows: dict[str, list[dict[str, str]]]) -> str:
    lines = [
        "# OT Priority Theme Index",
        "",
        f"Themes: {len(theme_rows)}",
        "",
    ]
    for slug, rows in theme_rows.items():
        theme = THEMES[slug]
        top_refs = ", ".join(row["ref"] for row in balanced_top_refs(rows))
        lines.append(f"## {theme['title']}")
        lines.append(f"- rows: {len(rows)}")
        lines.append(f"- books: {len({row['book_name'] for row in rows})}")
        lines.append(f"- file: {slug}.md")
        lines.append(f"- top refs: {top_refs}")
        lines.append("")
    return "\n".join(lines)


def build_overview(theme_rows: dict[str, list[dict[str, str]]]) -> str:
    lines = [
        "# OT Theme Overview",
        "",
        "Theme-first review pack for highest-value Brenton vs fresh translation differences.",
        "",
    ]
    for slug, rows in theme_rows.items():
        theme = THEMES[slug]
        lines.append(f"## {theme['title']}")
        lines.append(f"- rows: {len(rows)}")
        for row in balanced_top_refs(rows, limit=10, per_book_limit=1):
            lines.append(f"- {row['ref']} → score {row['priority_score']}")
        lines.append("")
    return "\n".join(lines)


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--overview-output", default=str(DEFAULT_OVERVIEW))
    args = parser.parse_args()

    rows = load_rows(Path(args.source))
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        for slug in classify_row(row):
            grouped[slug].append(row)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    sorted_grouped = {slug: sort_rows(theme_rows) for slug, theme_rows in grouped.items()}
    for slug, theme_rows in sorted_grouped.items():
        (output_dir / f"{slug}.md").write_text(build_theme_markdown(slug, theme_rows), encoding="utf-8")
        write_csv(output_dir / f"{slug}.csv", theme_rows)

    (output_dir / "index.md").write_text(build_index(sorted_grouped), encoding="utf-8")
    Path(args.overview_output).write_text(build_overview(sorted_grouped), encoding="utf-8")

    print(output_dir / "index.md")
    print(args.overview_output)


if __name__ == "__main__":
    main()
