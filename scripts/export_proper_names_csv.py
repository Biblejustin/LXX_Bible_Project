#!/usr/bin/env python3
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "name_meanings_appendix.md"
OUT = ROOT / "data" / "proper_names.csv"


def main() -> None:
    lines = SRC.read_text(encoding="utf-8").splitlines()
    rows = []
    current = None
    for raw in lines:
        line = raw.rstrip()
        if line.startswith("- "):
            body = line[2:]
            if " — " not in body:
                continue
            head, meaning = body.split(" — ", 1)
            name = head.strip()
            language = ""
            form = ""
            paren = re.findall(r"\(([^()]*)\)", head)
            if paren:
                tail = paren[-1]
                if "Hebrew" in tail or "Greek" in tail or "Aramaic" in tail or "Latin" in tail:
                    form = tail.strip()
            if form:
                name = re.sub(r"\s*\([^)]*\)\s*$", "", name).strip()
            lang_match = re.search(r"\((Hebrew|Greek|Aramaic|Latin|Hebrew/Greek)[^)]*\)", meaning)
            if lang_match:
                language = lang_match.group(1)
            current = {
                "name": name,
                "language": language,
                "form": form,
                "meaning": meaning.strip(),
                "first_reference": "",
                "footnote": "",
            }
            rows.append(current)
        elif current and line.startswith("  "):
            current["footnote"] = line.strip()

    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["name", "language", "form", "meaning", "first_reference", "footnote"],
        )
        writer.writeheader()
        writer.writerows(rows)
    print(OUT)


if __name__ == "__main__":
    main()
