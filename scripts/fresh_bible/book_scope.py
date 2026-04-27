"""Shared book/chapter scope helpers for build scripts."""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from typing import TypeVar


Row = Mapping[str, str]
T = TypeVar("T")


def book_key(value: str | None) -> str:
    return (value or "").strip().casefold()


def row_matches_book(row: Row, book: str | None) -> bool:
    if not book:
        return True
    wanted = book_key(book)
    return wanted in {book_key(row.get("book_name")), book_key(row.get("book_code"))}


def filter_rows_by_scope(
    rows: Sequence[dict[str, str]],
    book: str | None,
    chapter: int | None,
    chapter_start: int | None,
    chapter_end: int | None,
) -> list[dict[str, str]]:
    filtered: list[dict[str, str]] = []
    for row in rows:
        if not row_matches_book(row, book):
            continue
        row_chapter = row.get("chapter", "").strip()
        if not row_chapter:
            continue
        chapter_value = int(row_chapter)
        if chapter is not None and chapter_value != chapter:
            continue
        if chapter_start is not None and chapter_value < chapter_start:
            continue
        if chapter_end is not None and chapter_value > chapter_end:
            continue
        filtered.append(row)
    return filtered


def item_matches_book(
    item: T,
    book: str | None,
    *,
    book_name: Callable[[T], str],
    book_code: Callable[[T], str],
) -> bool:
    if not book:
        return True
    wanted = book_key(book)
    return wanted in {book_key(book_name(item)), book_key(book_code(item))}


def filter_items_by_book(
    items: Sequence[T],
    book: str | None,
    *,
    book_name: Callable[[T], str],
    book_code: Callable[[T], str],
    item_label: str = "item",
) -> list[T]:
    selected = [
        item
        for item in items
        if item_matches_book(item, book, book_name=book_name, book_code=book_code)
    ]
    if book and not selected:
        available = ", ".join(dict.fromkeys(book_name(item) for item in items))
        raise SystemExit(f"No {item_label}s matched --book {book!r}. Available books: {available}")
    return selected
