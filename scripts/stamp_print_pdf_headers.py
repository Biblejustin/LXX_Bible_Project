#!/usr/bin/env python3
"""Stamp running page headers onto an already paginated print-proof PDF."""

from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, DecodedStreamObject, DictionaryObject, NameObject

try:
    import fitz  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - optional acceleration dependency
    fitz = None


EMBEDDED_HEADER_FONT = Path("/System/Library/Fonts/Supplemental/Times New Roman.ttf")
EMBEDDED_HEADER_BOLD_FONT = Path("/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf")
FITZ_HEADER_FONT_NAME = "GHHeaderTimes"
FITZ_CHAPTER_FONT_NAME = "GHChapterTimesBold"
HEADER_RED_RGB = (155 / 255, 28 / 255, 28 / 255)
NOTE_BLUE_RGB = (31 / 255, 78 / 255, 121 / 255)
NOTE_BLUE_INT = 0x1F4E79
NOTE_GREEN_RGB = (38 / 255, 112 / 255, 74 / 255)
NOTE_GREEN_HEX = "#26704A"
HEADER_RED_PDF = "0.6078 0.1098 0.1098"
HEADER_BLACK_PDF = "0 0 0"
NOTE_START_RE = re.compile(
    r"^\d+\s+(?:T|Txt|MT/LXX|Heb|Gk|Tr|Std|Src|Nm|Pn|Pl|Ppl|Div|Eng):"
)
CHAPTER_RE = re.compile(r"^Chapter\s+(\d+)\b")
CHAPTER_HEADING_RE = re.compile(r"^Chapter\s+\d+\b")
VERSE_NUMBER_SPAN_RE = re.compile(r"^\d+[A-Za-z]?$")
FOOTNOTE_MARKER_SPAN_RE = re.compile(r"^\d+$")
INTEGER_TOKEN_RE = re.compile(r"\b\d+\b")


@dataclass(frozen=True)
class Ref:
    book: str
    chapter: int
    verse: int


@dataclass
class ParseState:
    book: str | None = None
    chapter: int | None = None
    verse: int | None = None

    def current_ref(self) -> Ref | None:
        if self.book is None or self.chapter is None or self.verse is None:
            return None
        return Ref(self.book, self.chapter, self.verse)


def leading_int(value: str) -> int | None:
    match = re.match(r"\d+", value.strip())
    return int(match.group(0)) if match else None


def load_chapter_bounds(paths: list[Path]) -> tuple[list[str], dict[tuple[str, int], tuple[int, int]]]:
    books: list[str] = []
    verses_by_chapter: dict[tuple[str, int], set[int]] = {}
    for path in paths:
        with path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                book = row["book_name"].strip()
                chapter = leading_int(row["chapter"])
                verse = leading_int(row["verse"])
                if not book or chapter is None or verse is None:
                    continue
                if book not in books:
                    books.append(book)
                verses_by_chapter.setdefault((book, chapter), set()).add(verse)
    bounds = {
        key: (min(verses), max(verses))
        for key, verses in verses_by_chapter.items()
        if verses
    }
    return books, bounds


def main_text_lines(page_text: str) -> list[str]:
    lines: list[str] = []
    for raw_line in page_text.splitlines():
        line = " ".join(raw_line.split())
        if not line:
            continue
        if NOTE_START_RE.match(line):
            break
        lines.append(line)
    return lines


def page_refs(
    page_text: str,
    *,
    state: ParseState,
    book_names: set[str],
    chapter_bounds: dict[tuple[str, int], tuple[int, int]],
) -> list[Ref]:
    lines = main_text_lines(page_text)
    refs: list[Ref] = []
    first_line = lines[0] if lines else ""
    continuation_ref = None
    if (
        first_line
        and state.current_ref()
        and first_line not in book_names
        and not CHAPTER_RE.match(first_line)
        and not re.match(r"^\d+\b", first_line)
    ):
        continuation_ref = state.current_ref()

    for line in lines:
        if line in book_names:
            state.book = line
            state.chapter = None
            state.verse = None
            continue
        chapter_match = CHAPTER_RE.match(line)
        if chapter_match and state.book:
            state.chapter = int(chapter_match.group(1))
            min_verse = chapter_bounds.get((state.book, state.chapter), (1, 1))[0]
            state.verse = min_verse - 1
            continue
        if state.book is None or state.chapter is None:
            continue
        bounds = chapter_bounds.get((state.book, state.chapter))
        if bounds is None:
            continue
        min_verse, max_verse = bounds
        expected = (state.verse + 1) if state.verse is not None else min_verse
        for token in INTEGER_TOKEN_RE.findall(line):
            verse = int(token)
            if verse < min_verse or verse > max_verse:
                continue
            if verse != expected:
                continue
            ref = Ref(state.book, state.chapter, verse)
            refs.append(ref)
            state.verse = verse
            expected = verse + 1

    if continuation_ref and (not refs or refs[0] != continuation_ref):
        refs.insert(0, continuation_ref)
    return refs


def format_ref_range(first: Ref | None, last: Ref | None) -> str:
    if first is None or last is None:
        return ""
    if first == last:
        return f"{first.book} {first.chapter}:{first.verse}"
    if first.book == last.book and first.chapter == last.chapter:
        return f"{first.book} {first.chapter}:{first.verse}-{last.verse}"
    if first.book == last.book:
        return f"{first.book} {first.chapter}:{first.verse}-{last.chapter}:{last.verse}"
    return f"{first.book} {first.chapter}:{first.verse} - {last.book} {last.chapter}:{last.verse}"


def pdf_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def approx_text_width(value: str, size: float) -> float:
    return len(value) * size * 0.46


def stamp_page_header(page, *, page_number: int, ref_range: str, writer: PdfWriter) -> None:
    resources = page.get("/Resources")
    if resources is None:
        resources = DictionaryObject()
        page[NameObject("/Resources")] = resources
    else:
        resources = resources.get_object()
    font_dict = resources.get("/Font")
    if font_dict is None:
        font_dict = DictionaryObject()
        resources[NameObject("/Font")] = font_dict
    else:
        font_dict = font_dict.get_object()
    font_dict[NameObject("/GHHeaderFont")] = DictionaryObject(
        {
            NameObject("/Type"): NameObject("/Font"),
            NameObject("/Subtype"): NameObject("/Type1"),
            NameObject("/BaseFont"): NameObject("/Times-Roman"),
            NameObject("/Encoding"): NameObject("/WinAnsiEncoding"),
        }
    )

    width = float(page.mediabox.width)
    height = float(page.mediabox.height)
    y = height - 24
    size = 8.0
    outer_margin = 36.0
    page_label = str(page_number)
    page_label_width = approx_text_width(page_label, size)
    page_x = width - outer_margin - page_label_width if page_number % 2 else outer_margin
    commands = [
        (
            page_x,
            y,
            page_label,
            HEADER_BLACK_PDF,
        )
    ]
    if ref_range:
        range_width = approx_text_width(ref_range, size)
        commands.append(((width - range_width) / 2, y, ref_range, HEADER_RED_PDF))
    content = ["q"]
    for x, text_y, value, color in commands:
        content.append(
            f"BT /GHHeaderFont {size:.1f} Tf {color} rg {x:.2f} {text_y:.2f} Td ({pdf_text(value)}) Tj ET"
        )
    content.append("Q\n")
    stream = DecodedStreamObject()
    stream.set_data("\n".join(content).encode("latin-1", errors="replace"))
    stream_ref = writer._add_object(stream)

    existing = page.get("/Contents")
    if existing is None:
        page[NameObject("/Contents")] = stream_ref
    elif isinstance(existing, ArrayObject):
        page[NameObject("/Contents")] = ArrayObject([stream_ref, *existing])
    else:
        page[NameObject("/Contents")] = ArrayObject([stream_ref, existing])


def fitz_overlay_fonts(page) -> tuple[str, str]:
    regular_font = "Times-Roman"
    bold_font = "Times-Bold"
    if EMBEDDED_HEADER_FONT.exists():
        page.insert_font(fontname=FITZ_HEADER_FONT_NAME, fontfile=str(EMBEDDED_HEADER_FONT))
        regular_font = FITZ_HEADER_FONT_NAME
        bold_font = FITZ_HEADER_FONT_NAME
    if EMBEDDED_HEADER_BOLD_FONT.exists():
        page.insert_font(fontname=FITZ_CHAPTER_FONT_NAME, fontfile=str(EMBEDDED_HEADER_BOLD_FONT))
        bold_font = FITZ_CHAPTER_FONT_NAME
    return regular_font, bold_font


def stamp_page_header_fitz(shape, page, *, page_number: int, ref_range: str, fontname: str) -> None:
    width = float(page.rect.width)
    y = 24.0
    size = 8.0
    outer_margin = 36.0
    page_label = str(page_number)
    page_label_width = approx_text_width(page_label, size)
    page_x = width - outer_margin - page_label_width if page_number % 2 else outer_margin
    shape.insert_text((page_x, y), page_label, fontsize=size, fontname=fontname, color=(0, 0, 0))
    if ref_range:
        range_width = approx_text_width(ref_range, size)
        shape.insert_text(
            ((width - range_width) / 2, y),
            ref_range,
            fontsize=size,
            fontname=fontname,
            color=HEADER_RED_RGB,
        )


def recolor_chapter_headings_fitz(
    rect_shape,
    text_shape,
    text_dict: dict[str, object],
    *,
    fontname: str,
) -> int:
    if fitz is None:
        return 0

    count = 0
    for block in text_dict.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            spans = [span for span in line.get("spans", []) if span.get("text", "").strip()]
            if not spans:
                continue
            line_text = " ".join("".join(span.get("text", "") for span in spans).split())
            if not CHAPTER_HEADING_RE.fullmatch(line_text):
                continue
            rect = fitz.Rect(spans[0]["bbox"])
            for span in spans[1:]:
                rect |= fitz.Rect(span["bbox"])
            rect.x0 -= 0.5
            rect.y0 -= 0.5
            rect.x1 += 1.5
            rect.y1 += 1.5
            size = max(float(span.get("size", 9.5)) for span in spans)
            origin = spans[0].get("origin")
            if origin is None:
                origin = (rect.x0 + 0.5, rect.y1 - 1.5)
            rect_shape.draw_rect(rect)
            text_shape.insert_text(
                (float(origin[0]), float(origin[1])),
                line_text,
                fontsize=size,
                fontname=fontname,
                color=HEADER_RED_RGB,
            )
            count += 1
    return count


def recolor_verse_numbers_fitz(
    rect_shape,
    text_shape,
    text_dict: dict[str, object],
    *,
    fontname: str,
) -> int:
    if fitz is None:
        return 0

    count = 0
    for block in text_dict.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                span_text = span.get("text", "").strip()
                if not VERSE_NUMBER_SPAN_RE.fullmatch(span_text):
                    continue
                font = span.get("font", "")
                if "Bold" not in font:
                    continue
                if int(span.get("color", 0)) != 0:
                    continue
                size = float(span.get("size", 0))
                if size < 7.5 or size > 12.5:
                    continue
                rect = fitz.Rect(span["bbox"])
                rect.x0 -= 0.4
                rect.y0 -= 0.4
                rect.x1 += 0.8
                rect.y1 += 0.8
                origin = span.get("origin")
                if origin is None:
                    origin = (rect.x0 + 0.4, rect.y1 - 1.2)
                rect_shape.draw_rect(rect)
                text_shape.insert_text(
                    (float(origin[0]), float(origin[1])),
                    span_text,
                    fontsize=size,
                    fontname=fontname,
                    color=HEADER_RED_RGB,
                )
                count += 1
    return count


def split_marker_sequence(
    value: str,
    *,
    expected_original: int | None,
    local_by_original: dict[int, int],
) -> tuple[list[int], int | None]:
    remaining = value
    originals: list[int] = []
    while remaining:
        if expected_original is not None:
            expected_text = str(expected_original)
            if remaining.startswith(expected_text):
                originals.append(expected_original)
                remaining = remaining[len(expected_text) :]
                expected_original += 1
                continue
        whole_value = int(remaining)
        if whole_value in local_by_original:
            originals.append(whole_value)
            remaining = ""
            continue
        originals.append(whole_value)
        expected_original = whole_value + 1
        remaining = ""
    return originals, expected_original


def xref_letter(index: int) -> str:
    if index < 1:
        return ""
    value = index
    letters: list[str] = []
    while value:
        value -= 1
        letters.append(chr(ord("a") + (value % 26)))
        value //= 26
    return "".join(reversed(letters))


def xref_footnote_originals_fitz(text_dict: dict[str, object]) -> set[int]:
    if fitz is None:
        return set()
    originals: set[int] = set()
    for block in text_dict.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            spans = [span for span in line.get("spans", []) if span.get("text", "")]
            if len(spans) < 2:
                continue
            marker = spans[0].get("text", "").strip()
            if (
                not FOOTNOTE_MARKER_SPAN_RE.fullmatch(marker)
                or int(spans[0].get("color", 0)) != NOTE_BLUE_INT
            ):
                continue
            line_text = "".join(span.get("text", "") for span in spans[1:]).lstrip()
            if line_text.startswith("X:"):
                originals.add(int(marker))
    return originals


def reset_and_embolden_blue_footnote_markers_fitz(
    rect_shape,
    text_shape,
    text_dict: dict[str, object],
    *,
    fontname: str,
) -> int:
    if fitz is None:
        return 0

    count = 0
    xref_originals = xref_footnote_originals_fitz(text_dict)
    local_by_original: dict[int, int] = {}
    xref_by_original: dict[int, str] = {}
    next_local = 1
    next_xref = 1
    expected_original: int | None = None
    for block in text_dict.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                span_text = span.get("text", "").strip()
                if not FOOTNOTE_MARKER_SPAN_RE.fullmatch(span_text):
                    continue
                if int(span.get("color", 0)) != NOTE_BLUE_INT:
                    continue
                if "Bold" in span.get("font", ""):
                    continue
                size = float(span.get("size", 0))
                if size < 5.0 or size > 8.5:
                    continue
                originals, expected_original = split_marker_sequence(
                    span_text,
                    expected_original=expected_original,
                    local_by_original=local_by_original,
                )
                local_parts: list[str] = []
                for original in originals:
                    if original in xref_originals:
                        if original not in xref_by_original:
                            xref_by_original[original] = xref_letter(next_xref)
                            next_xref += 1
                        local_parts.append(xref_by_original[original])
                    else:
                        if original not in local_by_original:
                            local_by_original[original] = next_local
                            next_local += 1
                        local_parts.append(str(local_by_original[original]))
                local_text = "".join(local_parts)
                marker_color = (
                    NOTE_GREEN_RGB
                    if originals and all(original in xref_originals for original in originals)
                    else NOTE_BLUE_RGB
                )
                if originals and any(original in xref_originals for original in originals) and not all(
                    original in xref_originals for original in originals
                ):
                    marker_color = NOTE_GREEN_RGB
                origin = span.get("origin")
                rect = fitz.Rect(span["bbox"])
                if origin is None:
                    origin = (rect.x0, rect.y1 - 1.0)
                note_block_marker = size >= 7.0
                marker_right = float(rect.x1)
                rect.x0 -= 0.3
                rect.y0 -= 0.3
                rect.x1 += 0.0 if note_block_marker else 0.9
                rect.y1 += 0.9
                rect_shape.draw_rect(rect)
                insert_x = float(origin[0])
                if note_block_marker:
                    local_width = fitz.get_text_length(
                        local_text,
                        fontname="Times-Bold",
                        fontsize=size,
                    )
                    insert_x = marker_right - local_width - 2.0
                text_shape.insert_text(
                    (insert_x, float(origin[1])),
                    local_text,
                    fontsize=size,
                    fontname=fontname,
                    color=marker_color,
                )
                count += 1
    return count


def stamp_pdf(
    *,
    input_path: Path,
    output_path: Path,
    source_paths: list[Path],
    diagnostics_path: Path | None,
) -> dict[str, object]:
    book_order, chapter_bounds = load_chapter_bounds(source_paths)
    book_names = set(book_order)
    if fitz is not None:
        document = fitz.open(input_path)
        state = ParseState()
        page_headers: list[dict[str, object]] = []
        colored_chapter_headings = 0
        colored_verse_numbers = 0
        bold_blue_footnote_markers = 0
        for index, page in enumerate(document, start=1):
            text = page.get_text("text")
            text_dict = page.get_text("dict")
            refs = page_refs(
                text,
                state=state,
                book_names=book_names,
                chapter_bounds=chapter_bounds,
            )
            ref_range = format_ref_range(refs[0], refs[-1]) if refs else ""
            regular_font, bold_font = fitz_overlay_fonts(page)
            rect_shape = page.new_shape()
            text_shape = page.new_shape()
            stamp_page_header_fitz(text_shape, page, page_number=index, ref_range=ref_range, fontname=regular_font)
            rect_count = 0
            chapter_count = recolor_chapter_headings_fitz(
                rect_shape,
                text_shape,
                text_dict,
                fontname=bold_font,
            )
            rect_count += chapter_count
            colored_chapter_headings += chapter_count
            verse_count = recolor_verse_numbers_fitz(
                rect_shape,
                text_shape,
                text_dict,
                fontname=bold_font,
            )
            rect_count += verse_count
            colored_verse_numbers += verse_count
            footnote_marker_count = reset_and_embolden_blue_footnote_markers_fitz(
                rect_shape,
                text_shape,
                text_dict,
                fontname=bold_font,
            )
            rect_count += footnote_marker_count
            bold_blue_footnote_markers += footnote_marker_count
            if rect_count:
                rect_shape.finish(width=0, color=(1, 1, 1), fill=(1, 1, 1))
                rect_shape.commit(overlay=True)
            text_shape.commit(overlay=True)
            page_headers.append(
                {
                    "page": index,
                    "range": ref_range,
                    "first_ref": vars(refs[0]) if refs else None,
                    "last_ref": vars(refs[-1]) if refs else None,
                }
            )
        output_path.parent.mkdir(parents=True, exist_ok=True)
        same_path = input_path.resolve() == output_path.resolve()
        write_path = output_path.with_suffix(".stamped.tmp.pdf") if same_path else output_path
        document.save(write_path, garbage=1, deflate=True)
        document.close()
        if same_path:
            write_path.replace(output_path)
        diagnostics = {
            "input": str(input_path),
            "output": str(output_path),
            "page_count": len(page_headers),
            "headers_with_ranges": sum(1 for item in page_headers if item["range"]),
            "text_extractor": "pymupdf",
            "pdf_writer": "pymupdf",
            "header_font": str(EMBEDDED_HEADER_FONT) if EMBEDDED_HEADER_FONT.exists() else "Times-Roman",
            "header_ref_color": "#9B1C1C",
            "colored_chapter_headings": colored_chapter_headings,
            "colored_verse_numbers": colored_verse_numbers,
            "bold_blue_footnote_markers": bold_blue_footnote_markers,
            "reset_blue_footnote_markers": bold_blue_footnote_markers,
            "sources": [str(path) for path in source_paths],
            "page_headers": page_headers,
        }
        if diagnostics_path:
            diagnostics_path.parent.mkdir(parents=True, exist_ok=True)
            diagnostics_path.write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return diagnostics

    reader = PdfReader(str(input_path))
    writer = PdfWriter()
    state = ParseState()
    page_headers: list[dict[str, object]] = []
    for index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        refs = page_refs(
            text,
            state=state,
            book_names=book_names,
            chapter_bounds=chapter_bounds,
        )
        ref_range = format_ref_range(refs[0], refs[-1]) if refs else ""
        stamp_page_header(page, page_number=index, ref_range=ref_range, writer=writer)
        writer.add_page(page)
        page_headers.append(
            {
                "page": index,
                "range": ref_range,
                "first_ref": vars(refs[0]) if refs else None,
                "last_ref": vars(refs[-1]) if refs else None,
            }
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    same_path = input_path.resolve() == output_path.resolve()
    write_path = output_path.with_suffix(".stamped.tmp.pdf") if same_path else output_path
    with write_path.open("wb") as handle:
        writer.write(handle)
    if same_path:
        write_path.replace(output_path)

    diagnostics = {
        "input": str(input_path),
        "output": str(output_path),
        "page_count": len(reader.pages),
        "headers_with_ranges": sum(1 for item in page_headers if item["range"]),
        "text_extractor": "pypdf",
        "pdf_writer": "pypdf",
        "header_ref_color": "#9B1C1C",
        "colored_chapter_headings": 0,
        "colored_verse_numbers": 0,
        "bold_blue_footnote_markers": 0,
        "reset_blue_footnote_markers": 0,
        "sources": [str(path) for path in source_paths],
        "page_headers": page_headers,
    }
    if diagnostics_path:
        diagnostics_path.parent.mkdir(parents=True, exist_ok=True)
        diagnostics_path.write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return diagnostics


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--nt-source", type=Path, required=True)
    parser.add_argument("--diagnostics", type=Path)
    args = parser.parse_args()
    diagnostics = stamp_pdf(
        input_path=args.input,
        output_path=args.output,
        source_paths=[args.source, args.nt_source],
        diagnostics_path=args.diagnostics,
    )
    print(json.dumps({k: diagnostics[k] for k in ("output", "page_count", "headers_with_ranges")}, indent=2))


if __name__ == "__main__":
    main()
