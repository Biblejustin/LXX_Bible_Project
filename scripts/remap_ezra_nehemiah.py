#!/usr/bin/env python3
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"


def load_rows() -> list[dict[str, str]]:
    with SOURCE.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_rows(rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with SOURCE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = load_rows()
    if not rows:
        raise SystemExit("No rows found.")

    fieldnames = list(rows[0].keys())
    output: list[dict[str, str]] = []

    for row in rows:
        if row["book_name"] == "Ezra":
            continue

        if row["book_name"] != "Nehemiah":
            output.append(row)
            continue

        chapter = int(row["chapter"])
        new_row = dict(row)

        if chapter <= 10:
            new_row["book_code"] = "EZR"
            new_row["book_name"] = "Ezra"
            new_row["chapter"] = str(chapter)
            new_row["ref"] = f"Ezra {chapter}:{new_row['verse']}"
        else:
            new_chapter = chapter - 10
            new_row["book_code"] = "NEH"
            new_row["book_name"] = "Nehemiah"
            new_row["chapter"] = str(new_chapter)
            new_row["ref"] = f"Nehemiah {new_chapter}:{new_row['verse']}"

        output.append(new_row)

    write_rows(output, fieldnames)

    ezra_count = sum(1 for row in output if row["book_name"] == "Ezra")
    nehemiah_count = sum(1 for row in output if row["book_name"] == "Nehemiah")
    total_count = len(output)
    print(
        {
            "total_rows": total_count,
            "ezra_rows": ezra_count,
            "nehemiah_rows": nehemiah_count,
        }
    )


if __name__ == "__main__":
    main()
