#!/usr/bin/env python3
"""Render print backmatter with continuous native page numbers."""

from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MAIN_PDF = (
    ROOT / "output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc_native_headers.pdf"
)
DEFAULT_APPENDIX_MD = ROOT / "output/doc/greek_heritage_study_helps_appendix.md"
DEFAULT_CONCORDANCE_MD = (
    ROOT / "output/concordance/the_greek_heritage_study_bible_greek_concordance_broad_preview.md"
)
DEFAULT_OUTPUT = (
    ROOT
    / "output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc_native_headers_with_appendix_concordance.pdf"
)
WORKING_DIR = ROOT / "output/working/backmatter"
BACKMATTER_HEADER = ROOT / "scripts/pandoc_backmatter_header.tex"
CONCORDANCE_HEADER = ROOT / "scripts/pandoc_concordance_header.tex"


def page_count(path: Path) -> int:
    return len(PdfReader(str(path)).pages)


def render_markdown_pdf(
    *,
    source_md: Path,
    output_pdf: Path,
    start_page: int,
    headers: list[Path],
    side_margin: str,
    twocolumn: bool,
) -> None:
    WORKING_DIR.mkdir(parents=True, exist_ok=True)
    temp_md = WORKING_DIR / f"{output_pdf.stem}.md"
    temp_md.write_text(
        f"\\setcounter{{page}}{{{start_page}}}\n\n" + source_md.read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    command = [
        os.environ.get("PANDOC", "pandoc"),
        str(temp_md),
        "-s",
        "-o",
        str(output_pdf),
        "--pdf-engine=xelatex",
        "-V",
        "documentclass=extarticle",
        "-V",
        "papersize=letter",
        "-V",
        "classoption=twoside",
        "-V",
        f"geometry:left={side_margin}",
        "-V",
        f"geometry:right={side_margin}",
        "-V",
        "geometry:top=0.55in",
        "-V",
        "geometry:bottom=0.35in",
        "-V",
        'mainfont=Times New Roman',
        "-V",
        "mainfontoptions=Ligatures=NoCommon",
    ]
    if twocolumn:
        command.extend(["-V", "classoption=twocolumn"])
    for header in headers:
        command.extend(["-H", str(header)])

    subprocess.run(command, cwd=ROOT, check=True)


def merge_pdfs(inputs: list[Path], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()
    command = [
        os.environ.get("GS", "gs"),
        "-q",
        "-dNOPAUSE",
        "-dBATCH",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.7",
        "-dPDFSETTINGS=/prepress",
        f"-sOutputFile={output}",
        *(str(path) for path in inputs),
    ]
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--main-pdf", type=Path, default=DEFAULT_MAIN_PDF)
    parser.add_argument("--appendix-md", type=Path, default=DEFAULT_APPENDIX_MD)
    parser.add_argument("--concordance-md", type=Path, default=DEFAULT_CONCORDANCE_MD)
    parser.add_argument(
        "--appendix-pdf",
        type=Path,
        default=ROOT / "output/doc/greek_heritage_study_helps_appendix.pdf",
    )
    parser.add_argument(
        "--concordance-pdf",
        type=Path,
        default=ROOT
        / "output/concordance/the_greek_heritage_study_bible_greek_concordance_broad_preview.pdf",
    )
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    main_pages = page_count(args.main_pdf)
    render_markdown_pdf(
        source_md=args.appendix_md,
        output_pdf=args.appendix_pdf,
        start_page=main_pages + 1,
        headers=[BACKMATTER_HEADER],
        side_margin="0.65in",
        twocolumn=False,
    )
    appendix_pages = page_count(args.appendix_pdf)
    render_markdown_pdf(
        source_md=args.concordance_md,
        output_pdf=args.concordance_pdf,
        start_page=main_pages + appendix_pages + 1,
        headers=[BACKMATTER_HEADER, CONCORDANCE_HEADER],
        side_margin="0.45in",
        twocolumn=True,
    )
    merge_pdfs([args.main_pdf, args.appendix_pdf, args.concordance_pdf], args.output)
    print(f"main_pages={main_pages}")
    print(f"appendix_pages={appendix_pages}")
    print(f"concordance_pages={page_count(args.concordance_pdf)}")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
