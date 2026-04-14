#!/usr/bin/env python3
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "book_intros_template.csv"

BOOKS = [
    ("GEN", "Genesis", "OT"),
    ("EXO", "Exodus", "OT"),
    ("LEV", "Leviticus", "OT"),
    ("NUM", "Numbers", "OT"),
    ("DEU", "Deuteronomy", "OT"),
    ("JOS", "Joshua", "OT"),
    ("JDG", "Judges", "OT"),
    ("RUT", "Ruth", "OT"),
    ("1SA", "1 Samuel", "OT"),
    ("2SA", "2 Samuel", "OT"),
    ("1KI", "1 Kings", "OT"),
    ("2KI", "2 Kings", "OT"),
    ("1CH", "1 Chronicles", "OT"),
    ("2CH", "2 Chronicles", "OT"),
    ("EZR", "Ezra", "OT"),
    ("NEH", "Nehemiah", "OT"),
    ("ESG", "Esther", "OT"),
    ("JOB", "Job", "OT"),
    ("PSA", "Psalms", "OT"),
    ("PRO", "Proverbs", "OT"),
    ("ECC", "Ecclesiastes", "OT"),
    ("SNG", "Song of Solomon", "OT"),
    ("ISA", "Isaiah", "OT"),
    ("JER", "Jeremiah", "OT"),
    ("LAM", "Lamentations", "OT"),
    ("EZK", "Ezekiel", "OT"),
    ("DAG", "Daniel", "OT"),
    ("HOS", "Hosea", "OT"),
    ("JOL", "Joel", "OT"),
    ("AMO", "Amos", "OT"),
    ("OBA", "Obadiah", "OT"),
    ("JON", "Jonah", "OT"),
    ("MIC", "Micah", "OT"),
    ("NAM", "Nahum", "OT"),
    ("HAB", "Habakkuk", "OT"),
    ("ZEP", "Zephaniah", "OT"),
    ("HAG", "Haggai", "OT"),
    ("ZEC", "Zechariah", "OT"),
    ("MAL", "Malachi", "OT"),
    ("MAT", "Matthew", "NT"),
    ("MRK", "Mark", "NT"),
    ("LUK", "Luke", "NT"),
    ("JHN", "John", "NT"),
    ("ACT", "Acts", "NT"),
    ("ROM", "Romans", "NT"),
    ("1CO", "1 Corinthians", "NT"),
    ("2CO", "2 Corinthians", "NT"),
    ("GAL", "Galatians", "NT"),
    ("EPH", "Ephesians", "NT"),
    ("PHP", "Philippians", "NT"),
    ("COL", "Colossians", "NT"),
    ("1TH", "1 Thessalonians", "NT"),
    ("2TH", "2 Thessalonians", "NT"),
    ("1TI", "1 Timothy", "NT"),
    ("2TI", "2 Timothy", "NT"),
    ("TIT", "Titus", "NT"),
    ("PHM", "Philemon", "NT"),
    ("HEB", "Hebrews", "NT"),
    ("JAS", "James", "NT"),
    ("1PE", "1 Peter", "NT"),
    ("2PE", "2 Peter", "NT"),
    ("1JN", "1 John", "NT"),
    ("2JN", "2 John", "NT"),
    ("3JN", "3 John", "NT"),
    ("JUD", "Jude", "NT"),
    ("REV", "Revelation", "NT"),
    ("TOB", "Tobit", "Apocrypha"),
    ("JDT", "Judith", "Apocrypha"),
    ("WIS", "Wisdom", "Apocrypha"),
    ("SIR", "Sirach", "Apocrypha"),
    ("BAR", "Baruch", "Apocrypha"),
    ("LJE", "Letter of Jeremiah", "Apocrypha"),
    ("SUS", "Susanna", "Apocrypha"),
    ("BEL", "Bel and the Dragon", "Apocrypha"),
    ("1MA", "1 Maccabees", "Apocrypha"),
    ("2MA", "2 Maccabees", "Apocrypha"),
    ("1ES", "1 Esdras", "Apocrypha"),
    ("MAN", "Prayer of Manasseh", "Apocrypha"),
    ("3MA", "3 Maccabees", "Apocrypha"),
    ("4MA", "4 Maccabees", "Apocrypha"),
]

FIELDNAMES = [
    "book_code",
    "book_name",
    "canonical_order",
    "section",
    "intro_title",
    "traditional_author",
    "authorship_basis",
    "jesus_or_nt_attribution",
    "composition_date",
    "mt_timeline",
    "lxx_timeline",
    "historical_setting",
    "purpose_theme",
    "key_themes",
    "outline",
    "oldest_fragment",
    "oldest_fragment_date",
    "oldest_substantial_manuscript",
    "oldest_substantial_date",
    "oldest_complete_hebrew",
    "oldest_complete_hebrew_date",
    "oldest_complete_greek",
    "oldest_complete_greek_date",
    "oldest_external_reference",
    "oldest_external_reference_author",
    "oldest_external_reference_date",
    "textual_notes",
    "conservative_notes",
    "source_notes",
    "status",
]


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        for idx, (book_code, book_name, section) in enumerate(BOOKS, start=1):
            writer.writerow(
                {
                    "book_code": book_code,
                    "book_name": book_name,
                    "canonical_order": idx,
                    "section": section,
                    "intro_title": book_name,
                    "status": "todo",
                }
            )


if __name__ == "__main__":
    main()
