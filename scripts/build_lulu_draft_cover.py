#!/usr/bin/env python3
"""Build a Lulu draft cover PDF."""

from __future__ import annotations

import argparse
import math
import shutil
import tempfile
from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = ROOT / "output" / "print" / "cover"
DEFAULT_PICTURES_DIR = Path.home() / "Pictures"
DEFAULT_STEM = "ghsb_draft_lulu_jacket_cover_26_5x11_75"

PAGE_WIDTH_IN = 26.5
PAGE_HEIGHT_IN = 11.75
OUTER_BLEED_IN = 0.625
TOP_BLEED_IN = 0.375
TRIM_WIDTH_IN = 8.5
TRIM_HEIGHT_IN = 11.0
SPINE_WIDTH_IN = 1.75
FLAP_WIDTH_IN = 3.25
FLAP_FOLD_WIDTH_IN = 0.25
PANEL_WIDTH_IN = TRIM_WIDTH_IN
DPI = 300

LEFT_FLAP_X_IN = OUTER_BLEED_IN
BACK_X_IN = LEFT_FLAP_X_IN + FLAP_WIDTH_IN
SPINE_X_IN = BACK_X_IN + PANEL_WIDTH_IN
FRONT_X_IN = SPINE_X_IN + SPINE_WIDTH_IN
RIGHT_FLAP_X_IN = FRONT_X_IN + PANEL_WIDTH_IN
PANEL_Y_IN = TOP_BLEED_IN

FONT_DIR = Path("/System/Library/Fonts/Supplemental")
FONTS = {
    "times": FONT_DIR / "Times New Roman.ttf",
    "times_bold": FONT_DIR / "Times New Roman Bold.ttf",
    "times_italic": FONT_DIR / "Times New Roman Italic.ttf",
    "optima": Path("/System/Library/Fonts/Optima.ttc"),
}

NAVY_TOP = "#1a2a47"
NAVY_MID = "#16243d"
NAVY_BOTTOM = "#0e1a2e"
GOLD = "#c9a961"
GOLD_LIGHT = "#e8cd7d"
GOLD_DARK = "#a0823f"
CREAM = "#f4ede0"
MUTED_GOLD = "#d4c5a8"
BLUE_GRAY = "#9eb0c9"
BLACKISH = "#08111f"

BACK_COPY = [
    (
        "The Greek Heritage Study Bible is a working draft of a fresh English "
        "translation prepared from the Greek textual heritage of the Church: the "
        "Old Testament from the Septuagint tradition and the New Testament from "
        "the Scrivener 1894 Textus Receptus."
    ),
    (
        "The goal is to make a Bible that gives careful attention to the Greek "
        "Old Testament text used and quoted by the New Testament authors, so "
        "readers can hear the Scriptures in the form that shaped the apostolic "
        "witness."
    ),
    (
        "This draft is a work in progress. It will contain mistakes "
        "and rough areas that can be improved. That is the purpose of this "
        "copy: to be read, marked, tested, and corrected before final "
        "publication."
    ),
    (
        "Notes identify translation decisions, textual differences, divine "
        "names, proper-name meanings, and places where Greek and Hebrew "
        "traditions need explanation. Cross-references and larger study-note "
        "layers have been minimized so the focus stays on proofreading the "
        "biblical text itself."
    ),
]


def pt(inches: float) -> float:
    return inches * 72


def px(inches: float) -> int:
    return round(inches * DPI)


def rgb(hex_color: str) -> tuple[float, float, float]:
    value = hex_color.lstrip("#")
    return tuple(int(value[i : i + 2], 16) / 255 for i in (0, 2, 4))


def rgb255(hex_color: str) -> tuple[int, int, int]:
    value = hex_color.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def mix(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    return tuple(round(a[i] * (1 - t) + b[i] * t) for i in range(3))


def require_fonts() -> None:
    missing = [str(path) for path in FONTS.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing cover fonts: " + ", ".join(missing))


def make_background(path: Path) -> None:
    width = px(PAGE_WIDTH_IN)
    height = px(PAGE_HEIGHT_IN)
    top = rgb255(NAVY_TOP)
    mid = rgb255(NAVY_MID)
    bottom = rgb255(NAVY_BOTTOM)
    image = Image.new("RGB", (width, height), top)
    draw = ImageDraw.Draw(image)

    for y in range(height):
        t = y / max(height - 1, 1)
        color = mix(top, mid, t * 2) if t < 0.5 else mix(mid, bottom, (t - 0.5) * 2)
        draw.line((0, y, width, y), fill=color)

    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)

    spine_x = px(SPINE_X_IN)
    spine_w = px(SPINE_WIDTH_IN)
    overlay_draw.rectangle((spine_x, 0, spine_x + spine_w, height), fill=(4, 10, 19, 105))
    for spine_edge_x in (SPINE_X_IN, FRONT_X_IN):
        x = px(spine_edge_x)
        overlay_draw.rectangle((x - 2, 0, x + 2, height), fill=(0, 0, 0, 85))

    vignette_small = Image.new("L", (max(width // 10, 1), max(height // 10, 1)), 0)
    pixels = vignette_small.load()
    cx = vignette_small.width * 0.55
    cy = vignette_small.height * 0.42
    max_dist = math.hypot(max(cx, vignette_small.width - cx), max(cy, vignette_small.height - cy))
    for y in range(vignette_small.height):
        for x in range(vignette_small.width):
            dist = math.hypot(x - cx, y - cy)
            pixels[x, y] = round(max(0, (dist / max_dist) - 0.45) * 170)
    vignette = vignette_small.resize(image.size, Image.Resampling.BILINEAR)
    vignette_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    vignette_layer.putalpha(vignette)
    overlay = Image.alpha_composite(overlay, vignette_layer)

    pattern = Image.new("RGBA", (px(3.55), px(1.65)), (0, 0, 0, 0))
    pattern_draw = ImageDraw.Draw(pattern)
    pattern_font = ImageFont.truetype(str(FONTS["times"]), 26)
    pattern_english_font = ImageFont.truetype(str(FONTS["times_italic"]), 15)
    pattern_fill = (232, 215, 163, 42)
    pattern_english_fill = (158, 176, 201, 36)
    pattern_lines = [
        ("ΕΝ ΑΡΧΗ ΕΠΟΙΗΣΕΝ Ο ΘΕΟΣ", "In the beginning God made", 0.00, 0.12),
        ("ΤΟΝ ΟΥΡΑΝΟΝ ΚΑΙ ΤΗΝ ΓΗΝ", "Heaven and earth", 0.25, 0.62),
        ("ΕΝ ΑΡΧΗ ΗΝ Ο ΛΟΓΟΣ", "In the beginning was the Word", 0.05, 1.12),
    ]
    for greek, english, x_in, y_in in pattern_lines:
        x = px(x_in)
        y = px(y_in)
        pattern_draw.text((x, y), greek, font=pattern_font, fill=pattern_fill)
        pattern_draw.text((x + px(0.02), y + px(0.18)), english, font=pattern_english_font, fill=pattern_english_fill)
    pattern = pattern.rotate(-4, expand=True, resample=Image.Resampling.BICUBIC)
    for y in range(-pattern.height, height + pattern.height, pattern.height):
        for x in range(-pattern.width, width + pattern.width, pattern.width):
            overlay.alpha_composite(pattern, (x, y))

    image = Image.alpha_composite(image.convert("RGBA"), overlay).convert("RGB")
    image.save(path, quality=94, optimize=True)


def register_fonts(page: fitz.Page) -> None:
    page.insert_font(fontname="TimesNewRoman", fontfile=str(FONTS["times"]))
    page.insert_font(fontname="TimesNewRomanBold", fontfile=str(FONTS["times_bold"]))
    page.insert_font(fontname="TimesNewRomanItalic", fontfile=str(FONTS["times_italic"]))
    page.insert_font(fontname="Optima", fontfile=str(FONTS["optima"]))


def text_width(text: str, font_path: Path, font_size: float) -> float:
    font = ImageFont.truetype(str(font_path), round(font_size))
    return font.getlength(text)


def wrap_text(text: str, font_path: Path, font_size: float, max_width_pt: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if text_width(candidate, font_path, font_size) <= max_width_pt or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_line_text(
    page: fitz.Page,
    text: str,
    *,
    x: float,
    y: float,
    fontname: str,
    font_path: Path,
    size: float,
    color: str,
    align: str = "left",
) -> None:
    line_width = text_width(text, font_path, size)
    if align == "center":
        x -= line_width / 2
    elif align == "right":
        x -= line_width
    page.insert_text(
        fitz.Point(x, y),
        text,
        fontname=fontname,
        fontsize=size,
        color=rgb(color),
    )


def draw_multiline(
    page: fitz.Page,
    lines: list[str],
    *,
    x: float,
    y: float,
    leading: float,
    fontname: str,
    font_path: Path,
    size: float,
    color: str,
    align: str = "left",
) -> float:
    for index, line in enumerate(lines):
        draw_line_text(
            page,
            line,
            x=x,
            y=y + leading * index,
            fontname=fontname,
            font_path=font_path,
            size=size,
            color=color,
            align=align,
        )
    return y + leading * len(lines)


def panel_border(page: fitz.Page, x_in: float, y_in: float, w_in: float, h_in: float) -> None:
    inset = pt(0.35)
    x = pt(x_in) + inset
    y = pt(y_in) + inset
    w = pt(w_in) - 2 * inset
    h = pt(h_in) - 2 * inset
    page.draw_rect(fitz.Rect(x, y, x + w, y + h), color=rgb(GOLD), width=1.2)
    page.draw_rect(fitz.Rect(x + 8, y + 8, x + w - 8, y + h - 8), color=rgb(GOLD), width=0.35)
    corner = pt(0.42)
    for sx, sy in ((x, y), (x + w, y), (x, y + h), (x + w, y + h)):
        sign_x = 1 if sx == x else -1
        sign_y = 1 if sy == y else -1
        page.draw_line(fitz.Point(sx, sy), fitz.Point(sx + sign_x * corner, sy), color=rgb(GOLD), width=2.2)
        page.draw_line(fitz.Point(sx, sy), fitz.Point(sx, sy + sign_y * corner), color=rgb(GOLD), width=2.2)


def draw_front(page: fitz.Page) -> None:
    cx = pt(FRONT_X_IN + PANEL_WIDTH_IN / 2)
    top = pt(1.48)
    title_font = FONTS["optima"]
    body_font = FONTS["times"]
    italic_font = FONTS["times_italic"]

    draw_line_text(page, "□", x=cx, y=top, fontname="Optima", font_path=title_font, size=18, color=GOLD, align="center")
    draw_line_text(page, "THE", x=cx, y=pt(2.08), fontname="Optima", font_path=title_font, size=21, color=GOLD_LIGHT, align="center")
    draw_line_text(page, "GREEK", x=cx, y=pt(2.92), fontname="Optima", font_path=title_font, size=48, color=GOLD_LIGHT, align="center")
    draw_line_text(page, "HERITAGE", x=cx, y=pt(3.62), fontname="Optima", font_path=title_font, size=48, color=GOLD_LIGHT, align="center")
    draw_line_text(page, "Study Bible", x=cx, y=pt(4.38), fontname="Optima", font_path=title_font, size=38, color=CREAM, align="center")

    page.draw_line(fitz.Point(cx - pt(1.45), pt(4.85)), fitz.Point(cx - pt(0.34), pt(4.85)), color=rgb(GOLD_DARK), width=0.5)
    page.draw_line(fitz.Point(cx + pt(0.34), pt(4.85)), fitz.Point(cx + pt(1.45), pt(4.85)), color=rgb(GOLD_DARK), width=0.5)
    draw_line_text(page, "□", x=cx, y=pt(4.92), fontname="Optima", font_path=title_font, size=13, color=GOLD, align="center")
    draw_line_text(page, "Draft Proof", x=cx, y=pt(5.54), fontname="Optima", font_path=title_font, size=24, color=GOLD_LIGHT, align="center")
    draw_line_text(page, "Ἐν ἀρχῇ ἦν ὁ λόγος", x=cx, y=pt(6.38), fontname="TimesNewRomanItalic", font_path=italic_font, size=20, color=MUTED_GOLD, align="center")
    draw_line_text(page, "In the beginning was the Word", x=cx, y=pt(6.68), fontname="TimesNewRomanItalic", font_path=italic_font, size=10, color=BLUE_GRAY, align="center")

    page.draw_line(fitz.Point(cx - pt(1.48), pt(7.55)), fitz.Point(cx + pt(1.48), pt(7.55)), color=rgb(GOLD_DARK), width=0.45)
    lines = ["A Fresh English Translation", "from the Septuagint", "and the Textus Receptus"]
    draw_multiline(
        page,
        lines,
        x=cx,
        y=pt(8.05),
        leading=pt(0.32),
        fontname="TimesNewRoman",
        font_path=body_font,
        size=15,
        color=MUTED_GOLD,
        align="center",
    )
    page.draw_line(fitz.Point(cx - pt(1.48), pt(9.0)), fitz.Point(cx + pt(1.48), pt(9.0)), color=rgb(GOLD_DARK), width=0.45)
    draw_line_text(page, "□", x=cx, y=pt(9.85), fontname="Optima", font_path=title_font, size=13, color=GOLD, align="center")
    draw_line_text(page, "LXX AND TR BASED", x=cx, y=pt(10.42), fontname="Optima", font_path=title_font, size=12, color=GOLD, align="center")


def draw_back(page: fitz.Page) -> None:
    cx = pt(BACK_X_IN + PANEL_WIDTH_IN / 2)
    left = pt(BACK_X_IN + 1.02)
    max_width = pt(PANEL_WIDTH_IN - 2.04)
    title_font = FONTS["optima"]
    body_font = FONTS["times"]

    draw_line_text(page, "□", x=cx, y=pt(1.48), fontname="Optima", font_path=title_font, size=18, color=GOLD, align="center")
    draw_line_text(page, "Draft Proof Copy", x=cx, y=pt(2.05), fontname="Optima", font_path=title_font, size=22, color=GOLD_LIGHT, align="center")

    y = pt(2.75)
    for paragraph in BACK_COPY:
        lines = wrap_text(paragraph, body_font, 12.8, max_width)
        y = draw_multiline(
            page,
            lines,
            x=cx,
            y=y,
            leading=16.4,
            fontname="TimesNewRoman",
            font_path=body_font,
            size=12.8,
            color=CREAM,
            align="center",
        )
        y += pt(0.38)

    page.draw_line(fitz.Point(left, pt(9.95)), fitz.Point(left + max_width, pt(9.95)), color=rgb(GOLD_DARK), width=0.5)
    draw_line_text(
        page,
        "Not final text. Prepared for proofreading and correction.",
        x=cx,
        y=pt(10.35),
        fontname="TimesNewRomanItalic",
        font_path=FONTS["times_italic"],
        size=12,
        color=BLUE_GRAY,
        align="center",
    )


def draw_spine(page: fitz.Page) -> None:
    rect = fitz.Rect(
        pt(SPINE_X_IN + 0.18),
        pt(PANEL_Y_IN + 0.18),
        pt(SPINE_X_IN + SPINE_WIDTH_IN - 0.18),
        pt(PAGE_HEIGHT_IN - TOP_BLEED_IN - 0.18),
    )
    page.insert_textbox(
        rect,
        "THE GREEK HERITAGE STUDY BIBLE - DRAFT PROOF",
        fontname="Optima",
        fontsize=16,
        color=rgb(GOLD_LIGHT),
        align=fitz.TEXT_ALIGN_CENTER,
        rotate=270,
    )


def build_pdf(pdf_path: Path, preview_path: Path) -> None:
    require_fonts()
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmpdir:
        bg_path = Path(tmpdir) / "cover_background.jpg"
        make_background(bg_path)

        doc = fitz.open()
        page = doc.new_page(width=pt(PAGE_WIDTH_IN), height=pt(PAGE_HEIGHT_IN))
        page.insert_image(page.rect, filename=str(bg_path))
        register_fonts(page)

        panel_border(page, BACK_X_IN, PANEL_Y_IN, PANEL_WIDTH_IN, TRIM_HEIGHT_IN)
        panel_border(page, FRONT_X_IN, PANEL_Y_IN, PANEL_WIDTH_IN, TRIM_HEIGHT_IN)
        draw_back(page)
        draw_front(page)
        draw_spine(page)

        doc.save(pdf_path, garbage=4, deflate=True)
        doc.close()

    with fitz.open(pdf_path) as doc:
        page = doc[0]
        scale = 2400 / page.rect.width
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
        pix.save(preview_path)


def remove_stale_files(output_dir: Path, pictures_dir: Path) -> None:
    stale_stems = [
        "ghsb_draft_lulu_letter_598p_cover",
        "ghsb_draft_lulu_jacket_598p_cover",
        "ghsb_draft_lulu_cover_20_375x12_75",
        "ghsb_draft_lulu_jacket_cover_26_625x11_75",
    ]
    for directory in (output_dir, pictures_dir):
        for stem in stale_stems:
            for suffix in (".svg", ".pdf", ".png"):
                stale = directory / f"{stem}{suffix}"
                if stale.exists():
                    stale.unlink()
            for suffix in ("_raw.pdf", "_preview.png"):
                stale = directory / f"{stem}{suffix}"
                if stale.exists():
                    stale.unlink()


def write_outputs(output_dir: Path, pictures_dir: Path, stem: str) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    pictures_dir.mkdir(parents=True, exist_ok=True)
    remove_stale_files(output_dir, pictures_dir)

    pdf_path = output_dir / f"{stem}.pdf"
    preview_path = output_dir / f"{stem}_preview.png"
    build_pdf(pdf_path, preview_path)

    picture_pdf = pictures_dir / pdf_path.name
    picture_preview = pictures_dir / preview_path.name
    shutil.copy2(pdf_path, picture_pdf)
    shutil.copy2(preview_path, picture_preview)
    return {
        "pdf": pdf_path,
        "preview": preview_path,
        "pictures_pdf": picture_pdf,
        "pictures_preview": picture_preview,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--pictures-dir", type=Path, default=DEFAULT_PICTURES_DIR)
    parser.add_argument("--stem", default=DEFAULT_STEM)
    args = parser.parse_args()
    outputs = write_outputs(args.output_dir, args.pictures_dir, args.stem)
    for key, path in outputs.items():
        print(f"{key}: {path}")


if __name__ == "__main__":
    main()
