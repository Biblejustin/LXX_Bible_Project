#!/usr/bin/env python3
import csv
import json
import re
from collections import Counter
from pathlib import Path

from build_english_witness_review import RESOLVED_REVIEW_STATUSES, load_latest_review_statuses


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
OUTPUT = ROOT / "output"

REVIEW_MD = OUTPUT / "fresh_ot_idiom_consistency_review.md"
REVIEW_CSV = OUTPUT / "fresh_ot_idiom_consistency_review.csv"
OUTLIERS_MD = OUTPUT / "fresh_ot_idiom_consistency_outliers.md"
OUTLIERS_CSV = OUTPUT / "fresh_ot_idiom_consistency_outliers.csv"
DIAGNOSTICS = OUTPUT / "fresh_ot_idiom_consistency_diagnostics.json"


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle, lineterminator="\n")
            writer.writerow(["family", "ref"])
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def classify_name_there(english: str) -> str:
    text = english.lower()
    if "called there" in text:
        return "called-there"
    if "cause my name to be called" in text or "cause his name to be called" in text:
        return "called-there"
    if "name to be called there" in text:
        return "called-there"
    if "cause my name to be invoked" in text or "cause his name to be invoked" in text:
        return "invoked-there"
    if "name his name there" in text or "name my name there" in text or "name there" in text:
        return "name-there"
    if "record my name" in text or "record his name" in text:
        return "record-there"
    return "other"


def classify_name_upon(english: str) -> str:
    text = english.lower()
    if "called upon" in text or "called on" in text:
        return "called-upon"
    if "called by my name" in text or "called by his name" in text:
        return "called-by-name"
    if "named upon" in text:
        return "named-upon"
    if "name is upon" in text or "name upon" in text:
        return "name-upon"
    return "other"


def classify_call_on_name(english: str) -> str:
    text = english.lower()
    if "call upon" in text or "call on" in text:
        return "call-on-name"
    if "call in the name" in text:
        return "call-in-name"
    if "invoke" in text:
        return "invoke-name"
    return "other"


def classify_soteria_sacrifice(english: str) -> str:
    text = english.lower()
    if "peace offering" in text or "peace offerings" in text or "sacrifice of peace" in text:
        return "peace"
    if "well-being" in text:
        return "well-being"
    if "salvation" in text:
        return "salvation"
    return "other"


def classify_living_soul(english: str) -> str:
    text = english.lower()
    if "living soul" in text:
        return "living-soul"
    if "living being" in text:
        return "living-being"
    if "living creature" in text or "living creatures" in text:
        return "living-creature"
    return "other"


FAMILIES = [
    {
        "name": "name-there-formula",
        "description": "Name formula with location marker such as 'to have his name called there'.",
        "match": lambda greek: "ονομα" in greek
        and "εκει" in greek
        and re.search(r"ονομα.{0,80}εκει", greek) is not None
        and any(token in greek for token in ("επονομα", "επικληθη", "επικληθηναι", "επικεκλη")),
        "classify": classify_name_there,
    },
    {
        "name": "name-upon-formula",
        "description": "Name formula with 'upon' language for house/people/object.",
        "match": lambda greek: "ονομα" in greek
        and any(token in greek for token in ("επικεκλη", "επικληθη", "επονομα"))
        and re.search(r"ονομα.{0,80}(επ'|εφ')", greek) is not None,
        "classify": classify_name_upon,
    },
    {
        "name": "call-on-name-formula",
        "description": "Active invocation formula, calling on the divine name.",
        "match": lambda greek: "ονομα" in greek
        and any(token in greek for token in ("επικαλεσ", "επικαλεσ", "επικαλουμ")),
        "classify": classify_call_on_name,
    },
    {
        "name": "soteria-sacrifice-formula",
        "description": "Cultic σωτηρι- terms in sacrificial context.",
        "match": lambda greek: "σωτηρι" in greek
        and any(token in greek for token in ("θυσ", "θυσε", "ολοκαυτ", "βωμ")),
        "classify": classify_soteria_sacrifice,
    },
    {
        "name": "into-living-soul-formula",
        "description": "Predicate εἰς ψυχὴν ζῶσαν / into a living soul, especially Genesis 2:7 and its NT echo.",
        "match": lambda greek: re.search(r"ε[ἰι]ς.{0,20}ψυχ.{0,20}ζ[ωῶ]σ", greek) is not None,
        "classify": classify_living_soul,
    },
]


def dominant_bucket(buckets: list[str]) -> tuple[str, int]:
    usable = [bucket for bucket in buckets if bucket != "other"]
    if not usable:
        return "other", 0
    counts = Counter(usable)
    bucket, count = counts.most_common(1)[0]
    return bucket, count


def build_markdown(
    family_rows: list[dict[str, str]],
    outlier_rows: list[dict[str, str]],
    family_stats: list[dict[str, str]],
) -> tuple[str, str]:
    unresolved_outliers = [row for row in outlier_rows if row.get("needs_followup") == "yes"]
    review_lines = [
        "# Fresh OT Idiom Consistency Review",
        "",
        "Repeated Greek idiom families. Use this to check whether one verse is drifting away from how the same formula is handled elsewhere.",
        "",
        f"Families: {len(family_stats)}",
        f"Rows checked: {len(family_rows)}",
        f"Outliers: {len(outlier_rows)}",
        f"Unresolved outliers: {len(unresolved_outliers)}",
        "",
        "## Family Summary",
        "",
    ]
    for stat in family_stats:
        review_lines.extend(
            [
                f"### {stat['family']}",
                f"- description: {stat['description']}",
                f"- rows: {stat['row_count']}",
                f"- dominant bucket: `{stat['dominant_bucket']}` ({stat['dominant_count']})",
                f"- buckets: {stat['bucket_summary']}",
                "",
            ]
        )
        rows = [row for row in family_rows if row["family"] == stat["family"]]
        for row in rows:
            review_lines.extend(
                [
                    f"- {row['ref']} [{row['bucket']}]",
                    f"  - fresh: {row['fresh_translation']}",
                ]
            )
        review_lines.append("")

    outlier_lines = [
        "# Fresh OT Idiom Consistency Outliers",
        "",
        "Rows where current English diverges from the dominant rendering pattern inside a repeated Greek idiom-family.",
        "",
        f"Rows: {len(outlier_rows)}",
        f"Unresolved: {len(unresolved_outliers)}",
        "",
    ]
    for row in outlier_rows:
        outlier_lines.extend(
            [
                f"## {row['ref']}",
                f"- family: `{row['family']}`",
                f"- current bucket: `{row['bucket']}`",
                f"- dominant bucket: `{row['dominant_bucket']}`",
                f"- latest review status: `{row.get('latest_review_status', '') or 'none'}`",
                f"- needs followup: `{row.get('needs_followup', '') or 'yes'}`",
                f"- fresh: {row['fresh_translation']}",
                "",
            ]
        )
    return "\n".join(review_lines).strip() + "\n", "\n".join(outlier_lines).strip() + "\n"


def main() -> None:
    rows = load_rows(SOURCE)
    latest_review_statuses = load_latest_review_statuses()

    family_rows: list[dict[str, str]] = []
    outlier_rows: list[dict[str, str]] = []
    family_stats: list[dict[str, str]] = []

    for family in FAMILIES:
        matches: list[dict[str, str]] = []
        for row in rows:
            greek = row.get("greek_text", "") or ""
            if not family["match"](greek):
                continue
            fresh = row.get("draft_translation", "") or ""
            latest_status = latest_review_statuses.get(row["ref"], "")
            matches.append(
                {
                    "family": family["name"],
                    "description": family["description"],
                    "ref": row["ref"],
                    "book_name": row["book_name"],
                    "chapter": row["chapter"],
                    "verse": row["verse"],
                    "greek_text": greek,
                    "fresh_translation": fresh,
                    "bucket": family["classify"](fresh),
                    "latest_review_status": latest_status,
                    "needs_followup": "no" if latest_status in RESOLVED_REVIEW_STATUSES else "yes",
                }
            )

        bucket_counts = Counter(row["bucket"] for row in matches)
        dominant, dominant_count = dominant_bucket([row["bucket"] for row in matches])
        family_stats.append(
            {
                "family": family["name"],
                "description": family["description"],
                "row_count": str(len(matches)),
                "dominant_bucket": dominant,
                "dominant_count": str(dominant_count),
                "bucket_summary": ", ".join(f"{bucket}={count}" for bucket, count in bucket_counts.most_common()),
            }
        )

        for row in matches:
            enriched = dict(row)
            enriched["dominant_bucket"] = dominant
            enriched["dominant_count"] = str(dominant_count)
            enriched["family_row_count"] = str(len(matches))
            family_rows.append(enriched)
            strong_family = dominant_count * 2 >= len(matches) if matches else False
            if dominant != "other" and row["bucket"] != dominant and (row["bucket"] != "other" or strong_family):
                outlier_rows.append(enriched)

    family_rows.sort(key=lambda row: (row["family"], row["book_name"], int(row["chapter"]), int(row["verse"])))
    outlier_rows.sort(key=lambda row: (row["family"], row["book_name"], int(row["chapter"]), int(row["verse"])))

    write_csv(REVIEW_CSV, family_rows)
    write_csv(OUTLIERS_CSV, outlier_rows)

    review_md, outliers_md = build_markdown(family_rows, outlier_rows, family_stats)
    REVIEW_MD.write_text(review_md, encoding="utf-8")
    OUTLIERS_MD.write_text(outliers_md, encoding="utf-8")

    diagnostics = {
        "families": len(FAMILIES),
        "family_stats": family_stats,
        "row_count": len(family_rows),
        "outlier_count": len(outlier_rows),
        "unresolved_outlier_count": sum(1 for row in outlier_rows if row.get("needs_followup") == "yes"),
        "review_markdown": str(REVIEW_MD),
        "review_csv": str(REVIEW_CSV),
        "outliers_markdown": str(OUTLIERS_MD),
        "outliers_csv": str(OUTLIERS_CSV),
    }
    DIAGNOSTICS.write_text(json.dumps(diagnostics, indent=2), encoding="utf-8")
    print(json.dumps(diagnostics, indent=2))


if __name__ == "__main__":
    main()
