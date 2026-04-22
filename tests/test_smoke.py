import csv
import hashlib
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


SOURCE_COLUMNS = {
    "ref",
    "book_code",
    "book_name",
    "chapter",
    "verse",
    "greek_text",
    "transliteration",
    "literal_gloss",
    "syntax_notes",
    "draft_translation",
}


PINNED_RAW_SHA256 = {
    "data/raw/eng-Brenton_usfm.zip": "b1380a21d81103a7c6a1a379e6f3734acf8dcb25bd345cb91eaaa1087aba5c4a",
    "data/raw/SF_2009-01-20_ENG_UKJV_(UPDATED KING JAMES VERSION).zip": "c4e998d53e595d317d60893accb0298ccef20f9a544ee8f7af85c84eca8987cf",
    "data/raw/TSK.zip": "53a94765a3b5a528249990a552aa639f00bb265548b84214343fb8de9db27557",
    "data/raw/cross-references.zip": "a4636893d50cae6191ca35a07bb65b2091a6d97990f61c169ee43d01af7b943c",
    "data/raw/hitchcock_bible_names.txt": "95d6eb253e4237ba198bb4ee92b4de9bccfab69fe7775eb82134444d44b2e850",
}


def csv_rows(relative_path: str) -> list[dict[str, str]]:
    with (ROOT / relative_path).open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256(relative_path: str) -> str:
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


def test_fresh_source_csv_shapes() -> None:
    ot_rows = csv_rows("data/raw/lxx_greek/ot_full.csv")
    nt_rows = csv_rows("data/raw/tr_greek/nt_full.csv")

    assert len(ot_rows) == 22896
    assert len(nt_rows) == 7957
    assert SOURCE_COLUMNS <= set(ot_rows[0])
    assert SOURCE_COLUMNS | {"ukjv_translation", "review_status", "review_notes"} <= set(nt_rows[0])
    assert ot_rows[0]["ref"] == "Genesis 1:1"
    assert nt_rows[0]["ref"] == "Matthew 1:1"


def test_tr_manifest_matches_imported_csv() -> None:
    manifest = json.loads((ROOT / "data/raw/tr_greek/source_manifest.json").read_text(encoding="utf-8"))
    nt_rows = csv_rows("data/raw/tr_greek/nt_full.csv")
    books = {row["book_code"] for row in nt_rows}

    assert manifest["upstream_commit"] == "6049a43b135ed870f843b83eb6a04764fc796678"
    assert manifest["diagnostics"]["rows"] == len(nt_rows)
    assert manifest["diagnostics"]["book_count"] == len(books)
    assert all(row["ukjv_translation"].strip() for row in nt_rows)


def test_proper_name_notes_have_meanings_and_expected_1_samuel_entries() -> None:
    rows = csv_rows("data/proper_name_transliteration_notes.csv")
    by_name = {row["name"]: row for row in rows}

    assert len(rows) == 3121
    assert not [row for row in rows if not row["name_meaning"].strip()]
    assert not [row for row in rows if "meaning uncertain" in row["name_meaning"].lower()]
    assert not [row for row in rows if row["equivalent_confidence"] == "fallback"]

    expected = {
        "Armathaim": ("Ramathaimzophim", "the two watch-towers"),
        "Siphā": ("Zophim", "watchers"),
        "Thoke": ("Tohu", "that lives; that declares"),
        "Anna": ("Hannah", "gracious; merciful; he that gives"),
        "Phennana": ("Peninnah", "pearl; precious stone; the face"),
        "Nasib": ("Zuph", "watcher; honeycomb"),
        "Iosedek": ("Jozadak", "Yahweh is righteous; justice of the Lord"),
        "Josedek": ("Josedech", "Yahweh is righteous; justice of the Lord"),
    }
    for source_name, (english_equivalent, meaning) in expected.items():
        assert by_name[source_name]["english_equivalent"] == english_equivalent
        assert by_name[source_name]["name_meaning"] == meaning


def test_pinned_raw_artifacts_are_unchanged() -> None:
    for relative_path, expected_hash in PINNED_RAW_SHA256.items():
        assert sha256(relative_path) == expected_hash


def test_generated_docx_files_are_valid_when_present() -> None:
    paths = [
        ROOT / "output/logos/fresh_translation_ot_logos_bible.docx",
        ROOT / "output/logos/fresh_translation_ot_logos_bible_mt_notes.docx",
        ROOT / "output/logos/fresh_translation_ot_proofreading.docx",
        ROOT / "output/logos_nt/fresh_translation_nt_tr_logos_bible.docx",
        ROOT / "output/logos_nt/fresh_translation_nt_tr_reference_notes.docx",
        ROOT / "output/logos_nt/fresh_translation_nt_tr_proofreading.docx",
    ]

    for path in paths:
        if not path.exists():
            continue
        with zipfile.ZipFile(path) as archive:
            assert archive.testzip() is None
            assert "word/document.xml" in archive.namelist()
