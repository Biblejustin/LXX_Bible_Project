#!/usr/bin/env python3
"""Render a sample print-proof book across Lulu trim sizes and estimate full page counts."""

from __future__ import annotations

import argparse
import csv
import json
import math
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output" / "print" / "size_sweep"
DEFAULT_HEADER = ROOT / "scripts" / "pandoc_print_header_no_perpage.tex"
DEFAULT_LUA_FILTER = ROOT / "scripts" / "pandoc_pericope_keep.lua"
DEFAULT_FULL_PDF = ROOT / "output" / "print" / "the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf"
DEFAULT_FULL_HEADERS = (
    ROOT / "output" / "print" / "the_greek_heritage_study_bible_lulu_print_proof_pandoc_pdf_headers.json"
)
MAX_LULU_PAGES = 800


@dataclass(frozen=True)
class TrimSize:
    key: str
    label: str
    width: float
    height: float
    include_by_default: bool = True

    @property
    def area(self) -> float:
        return self.width * self.height


TRIM_SIZES = [
    TrimSize("letter", "US Letter", 8.5, 11.0),
    TrimSize("crown_quarto", "Crown Quarto", 7.44, 9.68),
    TrimSize("royal", "Royal", 6.14, 9.21),
    TrimSize("us_trade", "US Trade", 6.0, 9.0),
    TrimSize("a5", "A5", 5.83, 8.27),
    TrimSize("digest", "Digest", 5.5, 8.5),
    TrimSize("novella", "Novella", 5.0, 8.0),
]


def run_command(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def page_count(path: Path) -> int:
    return len(PdfReader(str(path)).pages)


def current_full_pages() -> int:
    if DEFAULT_FULL_HEADERS.exists():
        data = json.loads(DEFAULT_FULL_HEADERS.read_text(encoding="utf-8"))
        value = data.get("page_count")
        if isinstance(value, int) and value > 0:
            return value
    if DEFAULT_FULL_PDF.exists():
        return page_count(DEFAULT_FULL_PDF)
    return 0


def build_sample_docx(book: str, out_dir: Path) -> Path:
    docx_path = out_dir / f"{book.lower()}_sample.docx"
    diagnostics_path = out_dir / f"{book.lower()}_sample_diagnostics.json"
    readme_path = out_dir / f"README_{book.lower()}_sample.md"
    run_command(
        [
            sys.executable,
            "scripts/build_print_proof_bible.py",
            "--book",
            book,
            "--lulu-pod-margins",
            "--run-in-verse-paragraphs",
            "--run-in-group-size",
            "0",
            "--output",
            str(docx_path),
            "--diagnostics",
            str(diagnostics_path),
            "--readme",
            str(readme_path),
            "--docx-compresslevel",
            "1",
        ]
    )
    return docx_path


def render_trim(docx_path: Path, trim: TrimSize, out_dir: Path, header_path: Path, lua_filter: Path) -> Path:
    pdf_path = out_dir / f"{docx_path.stem}_{trim.key}.pdf"
    if pdf_path.exists():
        return pdf_path
    run_command(
        [
            "pandoc",
            str(docx_path),
            "-o",
            str(pdf_path),
            "--pdf-engine=xelatex",
            "--lua-filter",
            str(lua_filter),
            "-H",
            str(header_path),
            "-V",
            "documentclass=extarticle",
            "-V",
            "classoption=twoside",
            "-V",
            f"geometry:paperwidth={trim.width}in",
            "-V",
            f"geometry:paperheight={trim.height}in",
            "-V",
            "geometry:inner=0.75in",
            "-V",
            "geometry:outer=0.5in",
            "-V",
            "geometry:top=0.5in",
            "-V",
            "geometry:bottom=0.5in",
            "-V",
            "mainfont=Times New Roman",
            "-V",
            "mainfontoptions=Ligatures=NoCommon",
        ]
    )
    return pdf_path


def write_report(rows: list[dict[str, object]], out_dir: Path, *, book: str, baseline_full_pages: int) -> None:
    csv_path = out_dir / "lulu_size_sweep.csv"
    fieldnames = [
        "trim",
        "width_in",
        "height_in",
        "sample_pages",
        "estimated_full_pages",
        "under_800",
        "trim_area_sq_in",
        "estimated_total_page_area_sq_in",
        "pdf",
        "status",
        "error",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row[key] for key in fieldnames})

    md_path = out_dir / "lulu_size_sweep.md"
    lines = [
        "# Lulu Print Size Sweep",
        "",
        f"Sample book: {book}",
        f"Baseline full PDF pages: {baseline_full_pages}",
        "Margins used for this proof sweep: inner 0.75 in, outer 0.5 in, top/bottom 0.5 in.",
        "Estimated full pages scale from the sample book against the current US Letter Pandoc full proof.",
        "",
        "| Trim | Size | Sample pages | Estimated full pages | Under 800 |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['trim']} | {row['width_in']} x {row['height_in']} | "
            f"{row['sample_pages']} | {row['estimated_full_pages']} | {row['under_800']} |"
        )
    lines.extend(
        [
            "",
            "Notes:",
            "- Failed rows usually indicate TeX could not fit the dense footnote load at that trim size with the current settings.",
        "- This sweep uses proof-risk margins, not Lulu's conservative over-600-page recommendation.",
        "- Pandoc sweep PDFs use continuous footnote numbering for TeX render stability.",
        ]
    )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", default="Genesis", help="Single sample book to render.")
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--header", type=Path, default=DEFAULT_HEADER)
    parser.add_argument("--lua-filter", type=Path, default=DEFAULT_LUA_FILTER)
    parser.add_argument("--full-pages", type=int, default=0)
    args = parser.parse_args()

    out_dir = args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    docx_path = build_sample_docx(args.book, out_dir)
    full_pages = args.full_pages or current_full_pages()
    if full_pages <= 0:
        raise SystemExit("Could not determine baseline full proof page count; pass --full-pages.")

    trim_results: list[tuple[TrimSize, Path | None, int | None, str, str]] = []
    for trim in TRIM_SIZES:
        try:
            pdf_path = render_trim(docx_path, trim, out_dir, args.header, args.lua_filter)
            trim_results.append((trim, pdf_path, page_count(pdf_path), "ok", ""))
        except subprocess.CalledProcessError as error:
            trim_results.append((trim, None, None, "failed", str(error)))

    baseline_pages = next((pages for trim, _pdf, pages, status, _error in trim_results if trim.key == "letter" and status == "ok"), None)
    if not baseline_pages:
        raise SystemExit("US Letter baseline was not rendered.")

    rows: list[dict[str, object]] = []
    for trim, pdf_path, sample_pages, status, error in trim_results:
        estimated_full_pages = math.ceil(full_pages * sample_pages / baseline_pages) if sample_pages else ""
        rows.append(
            {
                "trim": trim.label,
                "width_in": trim.width,
                "height_in": trim.height,
                "sample_pages": sample_pages or "",
                "estimated_full_pages": estimated_full_pages,
                "under_800": bool(estimated_full_pages) and int(estimated_full_pages) <= MAX_LULU_PAGES,
                "trim_area_sq_in": round(trim.area, 2),
                "estimated_total_page_area_sq_in": round(trim.area * int(estimated_full_pages), 1) if estimated_full_pages else "",
                "pdf": str(pdf_path) if pdf_path else "",
                "status": status,
                "error": error,
            }
        )

    rows.sort(
        key=lambda row: (
            row["status"] != "ok",
            not bool(row["under_800"]),
            float(row["trim_area_sq_in"]),
        )
    )
    write_report(rows, out_dir, book=args.book, baseline_full_pages=full_pages)
    print(json.dumps({"output_dir": str(out_dir), "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
