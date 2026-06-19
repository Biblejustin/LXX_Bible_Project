import csv
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]

for import_path in (ROOT, ROOT / "scripts"):
    import_path_text = str(import_path)
    if import_path_text not in sys.path:
        sys.path.insert(0, import_path_text)

from fresh_bible.book_scope import filter_rows_by_scope
from fresh_bible.csv_shape import csv_shape_issues, format_csv_shape_issue


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
    "data/raw/lxx_deuterocanon/grclxx_usfm.zip": "ecb6be2ca5e31098f6699df538158f2ca05f557bb4e31cf6bf7ad5d8f4c7b7c8",
    "data/raw/lxx_deuterocanon/grcbrent_usfm.zip": "8fa575a5d1565ae2ceb0d7cabac251ff460242eab823f4ebd40d8eefdeaf6881",
    "data/raw/hitchcock_bible_names.txt": "95d6eb253e4237ba198bb4ee92b4de9bccfab69fe7775eb82134444d44b2e850",
}


def csv_rows(relative_path: str) -> list[dict[str, str]]:
    with (ROOT / relative_path).open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def csv_header(relative_path: str) -> list[str]:
    with (ROOT / relative_path).open("r", encoding="utf-8", newline="") as handle:
        return next(csv.reader(handle))


def ensure_nt_review_outputs() -> Path:
    output_dir = ROOT / "output" / "working" / "test_nt_review"
    review_csv = output_dir / "fresh_nt_tr_vs_ukjv_review.csv"
    diagnostics = output_dir / "fresh_nt_tr_vs_ukjv_review_diagnostics.json"
    if review_csv.exists() and diagnostics.exists():
        return output_dir
    subprocess.run(
        [
            sys.executable,
            "scripts/build_nt_tr_vs_ukjv_review.py",
            "--review-csv",
            str(review_csv),
            "--priority-csv",
            str(output_dir / "fresh_nt_tr_vs_ukjv_priority_review.csv"),
            "--priority-md",
            str(output_dir / "fresh_nt_tr_vs_ukjv_priority_review.md"),
            "--queue-csv",
            str(output_dir / "fresh_nt_tr_vs_ukjv_review_queue.csv"),
            "--queue-md",
            str(output_dir / "fresh_nt_tr_vs_ukjv_review_queue.md"),
            "--diagnostics",
            str(diagnostics),
        ],
        cwd=ROOT,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    return output_dir


def nt_review_rows() -> list[dict[str, str]]:
    path = ensure_nt_review_outputs() / "fresh_nt_tr_vs_ukjv_review.csv"
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def nt_review_diagnostics() -> dict[str, object]:
    path = ensure_nt_review_outputs() / "fresh_nt_tr_vs_ukjv_review_diagnostics.json"
    return json.loads(path.read_text(encoding="utf-8"))


def ensure_nt_literal_revision_outputs() -> Path:
    output_dir = ROOT / "output" / "working" / "test_nt_literal_revision"
    source_copy = output_dir / "nt_full.csv"
    diagnostics = output_dir / "nt_tr_literal_revision_pass1_diagnostics.json"
    review_queue = output_dir / "nt_tr_literal_revision_review_queue.csv"
    if source_copy.exists() and diagnostics.exists() and review_queue.exists():
        return output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "data" / "raw" / "tr_greek" / "nt_full.csv", source_copy)
    subprocess.run(
        [
            sys.executable,
            "scripts/apply_nt_tr_literal_revision.py",
            "--source",
            str(source_copy),
            "--report",
            str(diagnostics),
            "--review-queue",
            str(review_queue),
        ],
        cwd=ROOT,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    return output_dir


def nt_literal_revision_queue_refs() -> set[str]:
    path = ensure_nt_literal_revision_outputs() / "nt_tr_literal_revision_review_queue.csv"
    with path.open("r", encoding="utf-8", newline="") as handle:
        return {row["ref"] for row in csv.DictReader(handle)}


def sha256(relative_path: str) -> str:
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


def test_book_scope_filters_book_and_chapter_range() -> None:
    rows = [
        {"book_code": "MAT", "book_name": "Matthew", "chapter": "1", "verse": "1"},
        {"book_code": "MAT", "book_name": "Matthew", "chapter": "2", "verse": "1"},
        {"book_code": "MRK", "book_name": "Mark", "chapter": "1", "verse": "1"},
    ]

    scoped = filter_rows_by_scope(rows, "MAT", None, 2, None)
    assert [(row["book_code"], row["chapter"]) for row in scoped] == [("MAT", "2")]
    assert filter_rows_by_scope(rows, "Mark", 1, None, None) == [rows[2]]


def test_fresh_source_csv_shapes() -> None:
    ot_rows = csv_rows("data/raw/lxx_greek/ot_full.csv")
    nt_rows = csv_rows("data/raw/tr_greek/nt_full.csv")

    assert len(ot_rows) == 22909
    assert len(nt_rows) == 7957
    assert SOURCE_COLUMNS <= set(ot_rows[0])
    assert SOURCE_COLUMNS | {"ukjv_translation", "review_status", "review_notes"} <= set(nt_rows[0])
    assert ot_rows[0]["ref"] == "Genesis 1:1"
    assert nt_rows[0]["ref"] == "Matthew 1:1"
    assert not [row["ref"] for row in ot_rows if " = " in row["draft_translation"]]
    assert [row["ref"] for row in ot_rows if row["greek_text"] == "MT-only insertion; no LXX Greek row"] == [
        f"Jeremiah 40:{verse}" for verse in range(14, 27)
    ]


def test_crossref_target_overrides_convert_reversed_lxx_ranges() -> None:
    import build_fresh_logos_bible as logos_builder

    verses = logos_builder.load_verses(logos_builder.DEFAULT_SOURCE) + logos_builder.load_verses(
        logos_builder.DEFAULT_NT_SOURCE
    )
    valid_refs = logos_builder.valid_crossref_code_refs(verses)
    english_to_lxx = logos_builder.invert_versification_map(
        logos_builder.effective_versification_map(None)
    )

    cases = {
        "Exod 39:1-7": ("Exodus 36:8-14",),
        "Exodus 39:1-2": ("Exodus 36:8-9",),
        "Exodus 20:13-14": ("Exodus 20:13", "Exodus 20:15"),
        "Deuteronomy 5:17-18": ("Deuteronomy 5:17", "Deuteronomy 5:18"),
        "Jeremiah 39:1-10": ("Jeremiah 46:1-3",),
        "Jeremiah 39:2-4": ("Jeremiah 46:2-3",),
        "Jeremiah 48:1-49:22": ("Jeremiah 30:1-21", "Jeremiah 31:1-44"),
    }

    for source_ref, expected in cases.items():
        mapped_refs, counts = logos_builder.map_crossref_refs_to_lxx(
            (source_ref,),
            english_to_lxx_map=english_to_lxx,
            valid_code_refs=valid_refs,
        )
        assert mapped_refs == expected
        assert counts["manual_lxx_target_overrides"] == 1


def test_deuterocanon_source_workspace_is_separate_and_sourced() -> None:
    import build_fresh_logos_bible as logos_builder

    rows = csv_rows("data/raw/lxx_deuterocanon/deuterocanon_full.csv")
    manifest = json.loads((ROOT / "data/raw/lxx_deuterocanon/source_manifest.json").read_text(encoding="utf-8"))
    missing_sources = (ROOT / "docs/DEUTEROCANON_MISSING_SOURCES.md").read_text(encoding="utf-8")
    pending_decisions = (ROOT / "docs/DEUTEROCANON_PENDING_DECISIONS.md").read_text(encoding="utf-8")
    diagnostics = manifest["diagnostics"]
    by_ref = {row["ref"]: row for row in rows}
    drafted_refs = [row["ref"] for row in rows if row["draft_translation"].strip()]
    undrafted_refs = [row["ref"] for row in rows if not row["draft_translation"].strip()]
    codes = {row["book_code"] for row in rows}

    assert len(rows) == 6045
    assert SOURCE_COLUMNS <= set(rows[0])
    assert manifest["missing_source_candidates_doc"] == "docs/DEUTEROCANON_MISSING_SOURCES.md"
    assert manifest["pending_decisions_doc"] == "docs/DEUTEROCANON_PENDING_DECISIONS.md"
    assert manifest["validation_command"] == "make validate-deuterocanon"
    assert manifest["supplemental_archive_sha256"] == PINNED_RAW_SHA256[
        "data/raw/lxx_deuterocanon/grcbrent_usfm.zip"
    ]
    assert any(source["key"] == "grcbrent" for source in manifest["source_archives"])
    assert len(drafted_refs) == 6045
    assert len(undrafted_refs) == 0
    assert {row["book_code"] for row in rows if not row["draft_translation"].strip()} == set()
    assert not [
        row["ref"]
        for row in rows
        if re.search(r"Source (?:descriptor|footnote)|Draft translation:|Greek:", row["draft_translation"])
    ]
    assert not [row["ref"] for row in rows if re.search(r"\\[a-z0-9]+", row["draft_translation"])]
    assert not [row["ref"] for row in rows if re.search(r"[\u0370-\u03ff]", row["draft_translation"])]
    assert not [
        row["ref"]
        for row in rows
        if re.search(r"(?<!\[)\s\d+(?:[A-Za-zΑ-ωα-ω])?\s+", row["greek_text"])
    ]
    for relative_path in [
        "data/raw/lxx_deuterocanon/deuterocanon_full.csv",
        "data/raw/lxx_deuterocanon/source_manifest.json",
    ]:
        content = (ROOT / relative_path).read_bytes()
        assert b"\r" not in content, relative_path
    assert drafted_refs[:8] == [f"Tobit 1:{verse}" for verse in range(1, 9)]
    assert by_ref["Tobit 1:1"]["draft_translation"].startswith("Book of the words of Tobit")
    assert "ways of truth and righteousness" in by_ref["Tobit 1:2"]["draft_translation"]
    assert "Baal the heifer" in by_ref["Tobit 1:5"]["draft_translation"]
    assert "the third tithe" in by_ref["Tobit 1:8"]["draft_translation"]
    assert "[22]" in by_ref["Sirach 28:21"]["draft_translation"]
    assert by_ref["4 Maccabees 18:24"]["draft_translation"] == (
        "to whom be the glory into the ages of the ages. Amen."
    )
    assert "Source descriptor:" in by_ref["4 Maccabees 18:24"]["syntax_notes"]
    assert "ἀπόκρυφον" in by_ref["4 Maccabees 18:24"]["syntax_notes"]
    assert rows[0]["ref"] == "Tobit 1:1"
    assert "Source footnote:" in by_ref["Tobit 1:1"]["syntax_notes"]
    assert "ΚΑΤΑ ΤΟΥΣ ΚΩΔΙΚΕΣ" in by_ref["Tobit 1:1"]["syntax_notes"]
    assert "Psalms 151:1" in by_ref
    assert by_ref["Psalms 151:1"]["chapter"] == "151"
    assert by_ref["Psalms 151:7"]["verse"] == "7"
    assert "Source descriptor:" in by_ref["Psalms 151:1"]["syntax_notes"]
    assert "ἔξωθεν τοῦ ἀριθμοῦ" in by_ref["Psalms 151:1"]["syntax_notes"]
    assert by_ref["Greek Esther Additions 1:1α"]["draft_translation"] == by_ref["Greek Esther 1:1α"][
        "draft_translation"
    ]
    assert by_ref["Greek Esther 4:17"]["draft_translation"] == (
        "And Mordecai went and did whatever Esther commanded him."
    )
    assert by_ref["Greek Esther 4:17α"]["draft_translation"].startswith(
        "And he entreated the Lord"
    )
    assert by_ref["Greek Esther 9:21"]["draft_translation"].endswith(
        "the fifteenth of Adar."
    )
    assert by_ref["Greek Esther 9:22"]["draft_translation"].startswith(
        "For in these days the Jews rested"
    )
    assert "wrath of anger" not in by_ref["Sirach 10:18"]["draft_translation"]
    assert "fierce anger" in by_ref["Sirach 10:18"]["draft_translation"]
    assert "wrath of anger" not in by_ref["1 Maccabees 2:49"]["draft_translation"]
    assert "time of overthrow and fierce anger" in by_ref["1 Maccabees 2:49"]["draft_translation"]
    assert "angered with wrath" not in by_ref["1 Maccabees 3:27"]["draft_translation"]
    assert "his anger burned" in by_ref["1 Maccabees 3:27"]["draft_translation"]
    assert by_ref["1 Maccabees 8:29"]["draft_translation"] == (
        "According to these words the Romans established terms with the people of the Jews."
    )
    assert "angry with wrath" not in by_ref["1 Maccabees 9:69"]["draft_translation"]
    assert "his anger burned against the lawless men" in by_ref["1 Maccabees 9:69"]["draft_translation"]
    assert "did not again add to come" not in by_ref["1 Maccabees 9:72"]["draft_translation"]
    assert by_ref["1 Maccabees 9:72"]["draft_translation"].endswith(
        "did not come into their borders again."
    )
    assert by_ref["1 Esdras 8:62"]["draft_translation"].startswith(
        "And with him was Eleazar son of Phinehas"
    )
    assert by_ref["3 Maccabees 4:16"]["draft_translation"].startswith(
        "And the king, greatly and continually filled with joy"
    )
    assert by_ref["Greek Esther Additions 4:17α"]["draft_translation"].startswith(
        "And he entreated the Lord"
    )
    assert by_ref["Greek Esther Additions 4:17ω"]["draft_translation"].startswith(
        "O God, the one strong over all"
    )
    assert by_ref["Greek Esther Additions 5:1α"]["draft_translation"].startswith(
        "And having become splendid"
    )
    assert by_ref["Greek Esther Additions 5:2β"]["draft_translation"].startswith(
        "And while she was speaking"
    )
    assert by_ref["Greek Esther Additions 10:3α"]["draft_translation"] == (
        'And Mordecai said, "These things came from God.'
    )
    assert by_ref["Greek Esther Additions 10:3β"]["draft_translation"].startswith(
        "For I remembered the dream"
    )
    assert by_ref["Greek Esther Additions 10:3λ"]["draft_translation"] == by_ref["Greek Esther 10:3λ"][
        "draft_translation"
    ]
    assert by_ref["Prayer of Manasseh 1:1"]["greek_text"].startswith("ΚΥΡΙΕ παντοκράτωπ")
    assert by_ref["Prayer of Manasseh 1:15"]["draft_translation"].endswith("into the ages. Amen.")
    assert by_ref["2 Maccabees 1:1"]["greek_text"].startswith("ΤΟΙΣ ἀδελφοῖς")
    assert by_ref["2 Maccabees 1:1"]["draft_translation"].startswith("To the brothers")
    assert by_ref["2 Maccabees 2:32"]["draft_translation"].startswith("Therefore from here")
    assert by_ref["2 Maccabees 3:40"]["draft_translation"].endswith("proceeded in this way.")
    assert by_ref["2 Maccabees 4:50"]["draft_translation"].startswith("But Menelaus")
    assert by_ref["2 Maccabees 5:27"]["draft_translation"].startswith("But Judas Maccabeus")
    assert by_ref["2 Maccabees 6:31"]["draft_translation"].startswith("And therefore this one")
    assert by_ref["2 Maccabees 7:42"]["draft_translation"].startswith("Therefore let the things")
    assert by_ref["2 Maccabees 8:36"]["draft_translation"].startswith("And the one who had undertaken")
    assert by_ref["2 Maccabees 9:29"]["draft_translation"].startswith("And Philip")
    assert by_ref["2 Maccabees 10:38"]["draft_translation"].startswith("And having accomplished")
    assert by_ref["2 Maccabees 11:38"]["draft_translation"].startswith("Be healthy")
    assert by_ref["2 Maccabees 12:45"]["draft_translation"].startswith("then looking")
    assert by_ref["2 Maccabees 13:26"]["draft_translation"].startswith("Lysias went up")
    assert by_ref["2 Maccabees 14:46"]["draft_translation"].startswith("already having become")
    assert by_ref["2 Maccabees 15:39"]["draft_translation"].endswith("here will be the end.")
    assert by_ref["2 Esdras 1:1"]["greek_text"].startswith("ΚΑΙ ἐν τῷ πρώτῳ")
    assert by_ref["2 Esdras 1:1"]["draft_translation"].startswith("And in the first year of Cyrus")
    assert by_ref["2 Esdras 10:44"]["draft_translation"].startswith("All these took foreign women")
    assert "Genesis 1:1" not in by_ref
    assert {
        "TOB",
        "JDT",
        "ESG",
        "ESGA",
        "WIS",
        "SIR",
        "BAR",
        "LJE",
        "S3Y",
        "SUS",
        "BEL",
        "1MA",
        "2MA",
        "1ES",
        "2ES",
        "MAN",
        "3MA",
        "4MA",
        "PSA",
    } <= codes
    assert manifest["archive_sha256"] == PINNED_RAW_SHA256["data/raw/lxx_deuterocanon/grclxx_usfm.zip"]
    assert manifest["translation_policy"].startswith("Importer-created rows start with blank")
    assert manifest["diagnostics"]["draft_preservation"]["preserved_rows"] == len(drafted_refs)
    assert manifest["diagnostics"]["draft_preservation"]["preserved_canonical_overlap_rows"] == 280
    assert manifest["diagnostics"]["rows"] == len(rows)
    assert manifest["diagnostics"]["source_note_rows"] == 4
    assert manifest["diagnostics"]["plain_inline_verse_labels_split"] == 42
    assert manifest["diagnostics"]["esther_addition_inline_labels_selected"] == 33
    assert manifest["diagnostics"]["bracketed_source_text_rows"] == 23
    assert manifest["diagnostics"]["missing_targets"] == []
    assert "CrossWire LXX module" in missing_sources
    assert "CC-BY/open repo output" in missing_sources
    assert "eBible Brenton Greek" in missing_sources
    assert "Prayer of Manasseh and true 2 Maccabees" in pending_decisions
    assert "Greek Esther Scope" in pending_decisions
    assert "Greek Ezra B / 2 Esdras Scope" in pending_decisions
    assert manifest["diagnostics"]["source_validation"]["source_id_mismatches"] == []
    assert manifest["diagnostics"]["source_validation"]["source_title_mismatches"] == []
    assert manifest["diagnostics"]["books"]["2MA"]["source_key"] == "grcbrent"
    assert manifest["diagnostics"]["books"]["2MA"]["source_file"] == "53-2MAgrcbrent.usfm"
    assert manifest["diagnostics"]["books"]["MAN"]["source_key"] == "grcbrent"
    assert manifest["diagnostics"]["books"]["MAN"]["source_file"] == "55-MANgrcbrent.usfm"
    assert manifest["diagnostics"]["books"]["ESG"]["rows"] == 253
    assert manifest["diagnostics"]["books"]["ESG"]["plain_inline_verse_labels_split"] == 34
    assert manifest["diagnostics"]["books"]["ESGA"]["source_scope"] == "esther_additions"
    assert manifest["diagnostics"]["books"]["ESGA"]["rows"] == 88
    assert manifest["diagnostics"]["books"]["ESGA"]["esther_addition_inline_labels_selected"] == 33
    assert manifest["diagnostics"]["books"]["1MA"]["rows"] == 923
    assert manifest["diagnostics"]["books"]["1ES"]["rows"] == 431
    assert manifest["diagnostics"]["books"]["3MA"]["rows"] == 228
    assert manifest["diagnostics"]["books"]["SIR"]["bracketed_source_text_rows"] == 21
    assert manifest["diagnostics"]["books"]["S3Y"]["bracketed_source_text_rows"] == 2
    assert manifest["diagnostics"]["books"]["2ES"]["source_file"] == "58-2ESgrclxx.usfm"
    assert manifest["diagnostics"]["books"]["2ES"]["expected_title"] == "ΕΣΔΡΑΣ Β"
    assert manifest["diagnostics"]["books"]["2ES"]["rows"] == 280
    assert manifest["diagnostics"]["books"]["4MA"]["source_file"] == "53-2MAgrclxx.usfm"
    assert manifest["diagnostics"]["books"]["4MA"]["source_usfm_id"] == "2MA"
    assert manifest["diagnostics"]["books"]["4MA"]["expected_title"] == "ΜΑΚΚΑΒΑΙΩΝ Δ"
    assert "ΜΑΚΚΑΒΑΙΩΝ Δ" in manifest["diagnostics"]["books"]["4MA"]["note"]
    assert diagnostics["rows"] == len(rows)
    assert diagnostics["draft_preservation"]["preserved_rows"] == len(drafted_refs)
    deuterocanon_verses = logos_builder.load_verses(ROOT / "data/raw/lxx_deuterocanon/deuterocanon_full.csv")
    deuterocanon_by_ref = {verse.ref: verse for verse in deuterocanon_verses}
    assert deuterocanon_by_ref["Greek Esther 1:1α"].chapter == 1
    assert deuterocanon_by_ref["Greek Esther 1:1α"].verse == 1
    assert deuterocanon_by_ref["Greek Esther 1:1α"].display_verse == "1α"
    assert deuterocanon_by_ref["Greek Esther 1:1α"].logos_ref == "Esther 1:1"
    assert deuterocanon_by_ref["Greek Esther Additions 4:17ω"].logos_ref == "Esther 4:17"
    assert deuterocanon_by_ref["2 Esdras 1:1"].logos_ref == "2 Esdras 1:1"
    assert deuterocanon_by_ref["Letter of Jeremiah 1:1"].logos_ref == "Letter of Jeremiah 1:1"
    assert logos_builder.should_suppress_logos_bible_milestone(deuterocanon_by_ref["2 Esdras 1:1"])
    assert logos_builder.should_suppress_logos_bible_milestone(deuterocanon_by_ref["Tobit 6:19"])
    assert logos_builder.should_suppress_logos_bible_milestone(deuterocanon_by_ref["4 Maccabees 12:20"])
    assert not logos_builder.should_suppress_logos_bible_milestone(deuterocanon_by_ref["Tobit 1:1"])
    assert not logos_builder.should_suppress_logos_bible_milestone(deuterocanon_by_ref["Letter of Jeremiah 1:1"])
    assert logos_builder.TESTAMENT_CONFIG["deuterocanon"]["title_prefix"] == (
        "The Greek Heritage Study Bible Deuterocanon"
    )
    for book_code in sorted(codes):
        balance = 0
        quote_open = False
        for row in [row for row in rows if row["book_code"] == book_code]:
            for char in row["draft_translation"]:
                if char == "[":
                    balance += 1
                elif char == "]":
                    balance -= 1
                elif char == '"':
                    quote_open = not quote_open
                assert balance >= 0, row["ref"]
        assert balance == 0, book_code
        assert not quote_open, book_code


def test_1_enoch_witness_workspace_is_separate_and_labeled() -> None:
    rows = csv_rows("data/raw/1_enoch/1_enoch_charles_witness.csv")
    queue_rows = csv_rows("data/research/1_enoch_witness_comparison_queue.csv")
    greek_audit_rows = csv_rows("data/research/1_enoch_charles_1912_greek_ocr_audit.csv")
    greek_priority_rows = csv_rows("data/research/1_enoch_charles_1912_greek_ocr_priority.csv")
    greek_ref_review_rows = csv_rows("data/research/1_enoch_greek_fragment_ref_review.csv")
    greek_verified_rows = csv_rows("data/research/1_enoch_greek_fragment_verified.csv")
    manifest = json.loads((ROOT / "data/raw/1_enoch/source_manifest.json").read_text(encoding="utf-8"))
    status = (ROOT / "docs/1_ENOCH_SOURCE_STATUS.md").read_text(encoding="utf-8")
    deuterocanon_rows = csv_rows("data/raw/lxx_deuterocanon/deuterocanon_full.csv")
    by_ref = {row["ref"]: row for row in rows}
    queue_by_ref = {row["ref"]: row for row in queue_rows}
    greek_audit_by_line = {row["line_number"]: row for row in greek_audit_rows}

    assert len(rows) == 1056
    assert {row["book_code"] for row in rows} == {"ENO"}
    assert "ENO" not in {row["book_code"] for row in deuterocanon_rows}
    assert manifest["role"].startswith("separate witness/comparison workspace")
    assert manifest["validation_command"] == "make build-enoch-witness"
    assert manifest["candidate_public_domain_sources"][0]["local_file"] == "data/raw/1_enoch_charles_1912_djvu.txt"
    assert {item["siglum"] for item in manifest["comparison_witness_inventory"]["greek"]} >= {
        "Gizeh",
        "Syncellus",
        "Jude",
    }
    assert {item["siglum"] for item in manifest["comparison_witness_inventory"]["aramaic"]} >= {"4Q201", "4Q212"}
    assert {item["siglum"] for item in manifest["comparison_witness_inventory"]["latin"]} == {"Tertullian", "BL"}
    assert "expired" in manifest["comparison_source_pointer"]["access_policy"]["access_note"]
    assert "Syriac and Coptic fragments await encoding" in manifest["comparison_source_pointer"]["access_policy"]["coverage_note"]
    assert manifest["diagnostics"]["chapter_count"] == 108
    assert manifest["diagnostics"]["missing_chapters"] == []
    assert manifest["diagnostics"]["comparison_queue_rows"] == 351
    assert len(queue_rows) == 351
    assert len(greek_audit_rows) == 2440
    assert len(greek_priority_rows) == 320
    assert len(greek_ref_review_rows) == 42
    assert len(greek_verified_rows) >= 1
    assert greek_audit_rows[0]["source_file"] == "data/raw/1_enoch_charles_1912_djvu.txt"
    assert greek_audit_rows[0]["line_number"] == "307"
    assert "do not import as verse text" in greek_audit_rows[0]["next_review"]
    assert greek_priority_rows[0]["line_number"] == "34673"
    assert greek_priority_rows[0]["printed_page_hint"] == "272"
    assert greek_priority_rows[0]["pdf_page_hint"] == "389"
    assert greek_priority_rows[0]["heading_hint"].startswith("272 The Book of Enoch")
    assert greek_priority_rows[0]["section_hint"] == "greek fragment text"
    assert int(greek_priority_rows[0]["greek_char_count"]) >= 40
    assert greek_audit_by_line["34680"]["ref_hint"] == "1 Enoch 1:2"
    assert greek_audit_by_line["34799"]["ref_hint"] == "1 Enoch 1:9"
    assert greek_ref_review_rows[0]["ref_hint"] == "1 Enoch 1"
    assert greek_ref_review_rows[0]["charles_witness_refs"] == "1 Enoch 1:1-1:9"
    assert greek_ref_review_rows[0]["pdf_page_hints"] == "389"
    assert "Λόγος εὐλογίας" in greek_ref_review_rows[0]["greek_ocr_excerpt"]
    assert greek_verified_rows[0]["ref"] == "1 Enoch 1:1"
    assert greek_verified_rows[0]["pdf_page_hint"] == "389"
    assert "οἵτινες ἔσονται" in greek_verified_rows[0]["greek_text"]
    assert "OCR artifacts are not imported" in greek_verified_rows[0]["review_note"]
    assert queue_by_ref["1 Enoch 1:9"]["marker_types"] == "greek_absent_in_ethiopic"
    assert by_ref["1 Enoch 1:9"]["comparison_notes"].startswith("G^g has text absent from Ethiopic")
    assert "ten thousands of His holy ones" in by_ref["1 Enoch 1:9"]["draft_translation"]
    assert "Ethiopic has text absent from G^g/G^s" in by_ref["1 Enoch 3:1"]["comparison_notes"]
    assert by_ref["1 Enoch 4:1"]["draft_translation"].startswith("And again, observe ye")
    assert by_ref["1 Enoch 108:1"]["draft_translation"].startswith("Another book which Enoch wrote")
    assert "not in the Greek deuterocanon Logos Bible output" in status


def test_review_feedback_high_traffic_wording_stays_fixed() -> None:
    import build_fresh_logos_bible as logos_builder

    ot_by_ref = {row["ref"]: row for row in csv_rows("data/raw/lxx_greek/ot_full.csv")}
    nt_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    notes_by_ref = {
        (row["ref"], row["note_type"], row["trigger_phrase"]): row
        for row in csv_rows("data/research/translation_footnotes.csv")
    }

    assert "lie in wait for your head" in ot_by_ref["Genesis 3:15"]["draft_translation"]
    assert "nothing will be lacking to me" in ot_by_ref["Psalms 22:1"]["draft_translation"]
    assert '"Let light come to be."' in ot_by_ref["Genesis 1:3"]["draft_translation"]
    assert "'Let light come to be.'" not in ot_by_ref["Genesis 1:3"]["draft_translation"]
    assert '"Why is it that God said, \'You shall not eat from every tree of the garden\'?"' in (
        ot_by_ref["Genesis 3:1"]["draft_translation"]
    )
    assert nt_by_ref["Matthew 1:23"]["draft_translation"].count("Immanuel") == 1
    assert "Emmanuel" not in nt_by_ref["Matthew 1:23"]["draft_translation"]
    assert "The first man, Adam" in nt_by_ref["1 Corinthians 15:45"]["draft_translation"]
    assert "John 19:37 cites the pierced wording" in notes_by_ref[
        ("Zechariah 12:10", "textual", "because they mocked")
    ]["footnote_text"]
    assert "Jeremiah 38:31" in notes_by_ref[("Hebrews 8:8", "textual", "new covenant")][
        "footnote_text"
    ]
    assert "separate workstream" in (ROOT / "docs" / "CANON_POLICY.md").read_text(encoding="utf-8")

    psalm_22 = logos_builder.Verse(
        ref="Psalms 22:1",
        book_code="PSA",
        book_name="Psalms",
        chapter=22,
        verse=1,
        text=ot_by_ref["Psalms 22:1"]["draft_translation"],
    )
    assert logos_builder.split_psalm_superscription(psalm_22) == (
        "Psalm of David.",
        "The Lord shepherds me, and nothing will be lacking to me.",
    )


def test_review_csv_shapes() -> None:
    paths = [
        ROOT / "data" / "research" / "translation_footnotes.csv",
        ROOT / "data" / "research" / "translation_decisions.csv",
        ROOT / "data" / "research" / "reviewed_phrase_guards.csv",
    ]
    issues = [issue for path in paths for issue in csv_shape_issues(path)]
    assert not issues, "\n".join(format_csv_shape_issue(issue) for issue in issues[:10])

    decision_statuses = {row["status"] for row in csv_rows("data/research/translation_decisions.csv")}
    footnote_statuses = {row["status"] for row in csv_rows("data/research/translation_footnotes.csv")}
    assert decision_statuses <= {"", "accepted", "drafted", "reviewed", "todo"}
    assert footnote_statuses <= {"", "approved", "drafted", "reviewed", "todo"}


def test_reader_facing_translation_note_loader_suppresses_generic_process_notes() -> None:
    import build_fresh_logos_bible as logos_builder

    notes_by_ref, diagnostics = logos_builder.load_translation_notes(
        ROOT / "data" / "research" / "translation_footnotes.csv"
    )
    loaded_note_texts = [
        note.text
        for notes in notes_by_ref.values()
        for note in notes
    ]

    assert "Greek line matches current rendering closely here." not in loaded_note_texts
    assert (
        "Cross-reference review revised malformed literal wording while following the local Greek text at this verse numbering point."
        not in loaded_note_texts
    )
    assert not any(
        text.startswith("Cross-reference review revised malformed literal wording while following the local Greek")
        for text in loaded_note_texts
    )
    assert "Greek preserves its own proper-name form in this register. The translation follows it." not in loaded_note_texts
    assert diagnostics["skipped_generic_or_brenton_only"] >= 10092


def test_tracked_text_files_use_lf_line_endings() -> None:
    result = subprocess.run(
        ["git", "ls-files", "--eol"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    offenders = [
        line
        for line in result.stdout.splitlines()
        if " w/mixed " in line or " w/crlf " in line or line.startswith("i/mixed ")
    ]
    assert not offenders
    assert "*.csv text eol=lf" in (ROOT / ".gitattributes").read_text(encoding="utf-8")


def test_joshua_19_38_keeps_complete_lxx_name_list() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/lxx_greek/ot_full.csv")}
    decisions_by_ref = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_decisions.csv")
        if row["ref"] == "Joshua 19:38"
    }
    footnotes_by_ref = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_footnotes.csv")
        if row["ref"] == "Joshua 19:38"
    }
    expected = "and Iron and Migdalel, Horem and Baiththame and Thessamys."

    assert source_by_ref["Joshua 19:38"]["draft_translation"] == expected
    assert decisions_by_ref["Joshua 19:38"]["chosen_rendering"] == expected
    assert decisions_by_ref["Joshua 19:38"]["status"] == "reviewed"
    assert decisions_by_ref["Joshua 19:38"]["reviewer"] == "user"
    assert footnotes_by_ref["Joshua 19:38"]["trigger_phrase"] == expected
    assert footnotes_by_ref["Joshua 19:38"]["source_basis"] == "variant + witnesses"
    assert footnotes_by_ref["Joshua 19:38"]["status"] == "reviewed"


def test_joshua_7_wording_and_achan_policy() -> None:
    by_ref = {row["ref"]: row for row in csv_rows("data/raw/lxx_greek/ot_full.csv")}

    assert "Achan son of Carmi" in by_ref["Joshua 7:1"]["draft_translation"]
    assert "the Lord's anger burned" in by_ref["Joshua 7:1"]["draft_translation"]
    assert "Scout out Ai" in by_ref["Joshua 7:2"]["draft_translation"]
    assert "turned its back" in by_ref["Joshua 7:8"]["draft_translation"]
    assert "turn their backs" in by_ref["Joshua 7:12"]["draft_translation"]
    assert "I will no longer be with you" in by_ref["Joshua 7:12"]["draft_translation"]
    assert "no longer commit such evil" in by_ref["Deuteronomy 19:20"]["draft_translation"]
    assert "no longer add to do" not in by_ref["Deuteronomy 19:20"]["draft_translation"]
    assert "do not speak this word any more" in by_ref["Deuteronomy 3:26"]["draft_translation"]
    assert "do not add to speak" not in by_ref["Deuteronomy 3:26"]["draft_translation"]
    assert (
        "We shall not hear the voice of the Lord our God any more"
        in by_ref["Deuteronomy 18:16"]["draft_translation"]
    )
    assert "We shall not add to hear" not in by_ref["Deuteronomy 18:16"]["draft_translation"]
    assert "shall speak further to the people" in by_ref["Deuteronomy 20:8"]["draft_translation"]
    assert "shall add to speak" not in by_ref["Deuteronomy 20:8"]["draft_translation"]
    assert "You shall not see it again" in by_ref["Deuteronomy 28:68"]["draft_translation"]
    assert "You shall not add to see" not in by_ref["Deuteronomy 28:68"]["draft_translation"]
    assert "again did evil before the Lord" in by_ref["Judges 3:12"]["draft_translation"]
    assert "again added to do evil" not in by_ref["Judges 3:12"]["draft_translation"]
    assert "again did evil before the Lord" in by_ref["Judges 4:1"]["draft_translation"]
    assert "again did evil before the Lord" in by_ref["Judges 10:6"]["draft_translation"]
    assert "again did evil before the Lord" in by_ref["Judges 13:1"]["draft_translation"]
    assert "war came again against Saul" in by_ref["1 Samuel 19:8"]["draft_translation"]
    assert "war was added to be" not in by_ref["1 Samuel 19:8"]["draft_translation"]
    assert "Saul sent third messengers" in by_ref["1 Samuel 19:21"]["draft_translation"]
    assert "Saul added to send" not in by_ref["1 Samuel 19:21"]["draft_translation"]
    assert "foreigners came up again" in by_ref["2 Samuel 5:22"]["draft_translation"]
    assert "again added to go up" not in by_ref["2 Samuel 5:22"]["draft_translation"]
    assert by_ref["Judges 6:25"]["draft_translation"].startswith("That night the Lord said to him")
    assert "And it came to be that night that" not in by_ref["Judges 6:25"]["draft_translation"]
    assert "no longer went out from his land" in by_ref["2 Kings 24:7"]["draft_translation"]
    assert "no longer added to go out" not in by_ref["2 Kings 24:7"]["draft_translation"]
    assert "And the Lord spoke to me again" in by_ref["Isaiah 8:5"]["draft_translation"]
    assert "Lord added to speak" not in by_ref["Isaiah 8:5"]["draft_translation"]
    assert "did not return to him any longer" in by_ref["Genesis 8:12"]["draft_translation"]
    assert "did not add to return" not in by_ref["Genesis 8:12"]["draft_translation"]
    assert "You shall not return by this road any longer" in by_ref["Deuteronomy 17:16"]["draft_translation"]
    assert "You shall not add to return" not in by_ref["Deuteronomy 17:16"]["draft_translation"]
    assert "will no longer humble him" in by_ref["2 Samuel 7:10"]["draft_translation"]
    assert "no longer add to humble" not in by_ref["2 Samuel 7:10"]["draft_translation"]
    assert "may no longer boast greatly" in by_ref["Psalms 9:39"]["draft_translation"]
    assert "no longer add to acting great" not in by_ref["Psalms 9:39"]["draft_translation"]
    assert "will not harm him any longer" in by_ref["Psalms 88:23"]["draft_translation"]
    assert "will not add to harm" not in by_ref["Psalms 88:23"]["draft_translation"]
    assert "you will no longer boast greatly upon my holy mountain" in by_ref["Zephaniah 3:11"]["draft_translation"]
    assert "you will no longer add to boast" not in by_ref["Zephaniah 3:11"]["draft_translation"]
    assert "again she bore his brother Abel" in by_ref["Genesis 4:2"]["draft_translation"]
    assert "added to bear" not in by_ref["Genesis 4:2"]["draft_translation"]
    assert "do not deceive again, Pharaoh" in by_ref["Exodus 8:25"]["draft_translation"]
    assert "do not add again, Pharaoh" not in by_ref["Exodus 8:25"]["draft_translation"]
    assert "shall not again commit such evil" in by_ref["Deuteronomy 13:12"]["draft_translation"]
    assert "shall not add again to do" not in by_ref["Deuteronomy 13:12"]["draft_translation"]
    assert "the Lord called Samuel again" in by_ref["1 Samuel 3:8"]["draft_translation"]
    assert "Lord added to call" not in by_ref["1 Samuel 3:8"]["draft_translation"]
    assert "the Lord called again, Samuel, Samuel" in by_ref["1 Samuel 3:6"]["draft_translation"]
    assert "Lord added and called" not in by_ref["1 Samuel 3:6"]["draft_translation"]
    assert "Samuel did not see Saul again" in by_ref["1 Samuel 15:35"]["draft_translation"]
    assert "did not add again to see" not in by_ref["1 Samuel 15:35"]["draft_translation"]
    assert "he no longer sought him" in by_ref["1 Samuel 27:4"]["draft_translation"]
    assert "no longer added to seek" not in by_ref["1 Samuel 27:4"]["draft_translation"]
    assert "they fought no longer" in by_ref["2 Samuel 2:28"]["draft_translation"]
    assert "no longer added to fight" not in by_ref["2 Samuel 2:28"]["draft_translation"]
    assert "he will not touch him again" in by_ref["2 Samuel 14:10"]["draft_translation"]
    assert "will not add still to touch" not in by_ref["2 Samuel 14:10"]["draft_translation"]
    assert "not again shake the foot of Israel" in by_ref["2 Kings 21:8"]["draft_translation"]
    assert "not again add to shake" not in by_ref["2 Kings 21:8"]["draft_translation"]
    assert "he rebelled still further from the Lord" in by_ref["2 Chronicles 28:22"]["draft_translation"]
    assert "added to rebel further" not in by_ref["2 Chronicles 28:22"]["draft_translation"]
    assert "not again shake the foot of Israel" in by_ref["2 Chronicles 33:8"]["draft_translation"]
    assert "not again add to move" not in by_ref["2 Chronicles 33:8"]["draft_translation"]
    assert "Will not the one lying down rise again?" in by_ref["Psalms 40:9"]["draft_translation"]
    assert "add to rise again" not in by_ref["Psalms 40:9"]["draft_translation"]
    assert "he will receive more" in by_ref["Proverbs 9:9"]["draft_translation"]
    assert "add to receiving" not in by_ref["Proverbs 9:9"]["draft_translation"]
    assert "the Lord will again show his hand" in by_ref["Isaiah 11:11"]["draft_translation"]
    assert "will add to show" not in by_ref["Isaiah 11:11"]["draft_translation"]
    assert "I will proceed to move this people" in by_ref["Isaiah 29:14"]["draft_translation"]
    assert "I will add to move" not in by_ref["Isaiah 29:14"]["draft_translation"]
    assert "Shall I again look toward your holy temple?" in by_ref["Jonah 2:5"]["draft_translation"]
    assert "again add to look" not in by_ref["Jonah 2:5"]["draft_translation"]
    assert "will never happen again" in by_ref["Exodus 11:6"]["draft_translation"]
    assert "will never be added again" not in by_ref["Exodus 11:6"]["draft_translation"]
    assert "said again to Joab" in by_ref["2 Samuel 18:22"]["draft_translation"]
    assert "again added and said" not in by_ref["2 Samuel 18:22"]["draft_translation"]
    assert "the king sent again" in by_ref["2 Kings 1:11"]["draft_translation"]
    assert "king added and sent" not in by_ref["2 Kings 1:11"]["draft_translation"]
    assert "Esther spoke again to the king" in by_ref["Esther 8:3"]["draft_translation"]
    assert "Esther added and spoke" not in by_ref["Esther 8:3"]["draft_translation"]
    assert "Elihu continued and said" in by_ref["Job 36:1"]["draft_translation"]
    assert "Elihu still added" not in by_ref["Job 36:1"]["draft_translation"]
    assert "the Lord spoke again to Ahaz" in by_ref["Isaiah 7:10"]["draft_translation"]
    assert "Lord added again to speak" not in by_ref["Isaiah 7:10"]["draft_translation"]
    assert "continued speaking to him" in by_ref["Genesis 18:29"]["draft_translation"]
    assert "added still to speak" not in by_ref["Genesis 18:29"]["draft_translation"]
    assert "hated him still more" in by_ref["Genesis 37:8"]["draft_translation"]
    assert "added still more to hate" not in by_ref["Genesis 37:8"]["draft_translation"]
    assert "Saul was still more afraid of David" in by_ref["1 Samuel 18:29"]["draft_translation"]
    assert "added still more to stand in awe" not in by_ref["1 Samuel 18:29"]["draft_translation"]
    assert "Jonathan swore again to David" in by_ref["1 Samuel 20:17"]["draft_translation"]
    assert "Jonathan added still to swear" not in by_ref["1 Samuel 20:17"]["draft_translation"]
    assert "David inquired again through the Lord" in by_ref["1 Samuel 23:4"]["draft_translation"]
    assert "David added still to inquire" not in by_ref["1 Samuel 23:4"]["draft_translation"]
    assert "Abner said again to Asahel" in by_ref["2 Samuel 2:22"]["draft_translation"]
    assert "Abner added still" not in by_ref["2 Samuel 2:22"]["draft_translation"]
    assert "And again she bore a son" in by_ref["Genesis 38:5"]["draft_translation"]
    assert "And adding again" not in by_ref["Genesis 38:5"]["draft_translation"]
    assert "what more can David say to you" in by_ref["2 Samuel 7:20"]["draft_translation"]
    assert "what will David add still to speak" not in by_ref["2 Samuel 7:20"]["draft_translation"]
    assert "no longer take pleasure" in by_ref["Psalms 76:8"]["draft_translation"]
    assert "add no more to take pleasure" not in by_ref["Psalms 76:8"]["draft_translation"]
    assert "sinned still more against him" in by_ref["Psalms 77:17"]["draft_translation"]
    assert "added still to sin" not in by_ref["Psalms 77:17"]["draft_translation"]
    assert "I will do so no more" in by_ref["Job 34:32"]["draft_translation"]
    assert "I will add no more" not in by_ref["Job 34:32"]["draft_translation"]
    assert "hand of a mighty one" in by_ref["Psalms 126:4"]["draft_translation"]
    assert "hand of mighty one" not in by_ref["Psalms 126:4"]["draft_translation"]
    assert "Thus says the Lord God of Israel" in by_ref["Joshua 7:13"]["draft_translation"]
    assert "bring forward man by man" in by_ref["Joshua 7:14"]["draft_translation"]
    assert "committed a lawless deed in Israel" in by_ref["Joshua 7:15"]["draft_translation"]
    assert "the Lord turned from his fierce anger" in by_ref["Joshua 7:26"]["draft_translation"]
    assert "the Lord's anger burned against Moses" in by_ref["Exodus 4:14"]["draft_translation"]
    assert "his anger burned" in by_ref["Genesis 39:19"]["draft_translation"]
    assert "became angry with wrath" not in by_ref["Genesis 39:19"]["draft_translation"]
    assert "your God's anger burn" in by_ref["Deuteronomy 6:15"]["draft_translation"]
    assert "having become angry in wrath" not in by_ref["Deuteronomy 6:15"]["draft_translation"]
    assert "the Lord's anger will burn against you" in by_ref["Deuteronomy 7:4"]["draft_translation"]
    assert "the Lord's anger will burn against you" in by_ref["Deuteronomy 11:17"]["draft_translation"]
    assert "the Lord's anger burned against Israel" in by_ref["2 Kings 13:3"]["draft_translation"]
    assert "grew angry in wrath" not in by_ref["2 Kings 13:3"]["draft_translation"]
    assert "the Lord's anger burned against that land" in by_ref["Deuteronomy 29:26"]["draft_translation"]
    assert "my anger will burn against them" in by_ref["Deuteronomy 31:17"]["draft_translation"]
    for ref in ("Exodus 4:14", "Deuteronomy 7:4", "Deuteronomy 11:17", "Deuteronomy 29:26", "Deuteronomy 31:17"):
        assert "angered in wrath" not in by_ref[ref]["draft_translation"]
        assert "angered with wrath" not in by_ref[ref]["draft_translation"]
    assert "Did not Achan son of Zerah" in by_ref["Joshua 22:20"]["draft_translation"]
    assert "And sons of Carmi: Achar, the troubler of Israel" in by_ref["1 Chronicles 2:7"]["draft_translation"]

    add_to_notes = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_footnotes.csv")
        if row["source_basis"] == "add-to idiom"
    }
    for ref in (
        "Genesis 8:12",
        "Deuteronomy 17:16",
        "2 Samuel 7:10",
        "Psalms 9:39",
        "Psalms 88:23",
        "Zephaniah 3:11",
        "Genesis 4:2",
        "Exodus 8:25",
        "Deuteronomy 13:12",
        "1 Samuel 3:8",
        "1 Samuel 15:35",
        "1 Samuel 27:4",
        "2 Samuel 2:28",
        "2 Samuel 14:10",
        "2 Kings 21:8",
        "2 Chronicles 28:22",
        "2 Chronicles 33:8",
        "Psalms 40:9",
        "Proverbs 9:9",
        "Isaiah 11:11",
        "Isaiah 29:14",
        "Jonah 2:5",
        "Exodus 11:6",
        "1 Samuel 3:6",
        "2 Samuel 18:22",
        "2 Kings 1:11",
        "Esther 8:3",
        "Job 36:1",
        "Isaiah 7:10",
        "Genesis 18:29",
        "Genesis 37:8",
        "Genesis 38:5",
        "1 Samuel 18:29",
        "1 Samuel 20:17",
        "1 Samuel 23:4",
        "2 Samuel 2:22",
        "2 Samuel 7:20",
        "Psalms 76:8",
        "Psalms 77:17",
        "Job 34:32",
    ):
        assert "Greek literally" in add_to_notes[ref]["footnote_text"]

    anger_notes = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_footnotes.csv")
        if row["source_basis"] == "Greek anger idiom"
    }
    for ref in ("Exodus 4:14", "Deuteronomy 7:4", "Deuteronomy 11:17", "Deuteronomy 29:26", "Deuteronomy 31:17"):
        assert ref in anger_notes
        assert "Greek literally says" in anger_notes[ref]["footnote_text"]
        assert "doubled anger idiom" in anger_notes[ref]["footnote_text"]

    notes = csv_rows("data/proper_name_transliteration_notes.csv")
    achan_notes = [row for row in notes if row["name"] == "Achan" and row["source_form"] == "Achar"]
    assert {row["first_reference"] for row in achan_notes} >= {"Joshua 7:1", "Joshua 22:20"}
    assert any("MT distinguishes Achan in Joshua from Achar in 1 Chronicles 2:7" in row["footnote"] for row in achan_notes)

    narrative_notes = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_footnotes.csv")
        if row["source_basis"] == "narrative formula"
    }
    assert "Judges 6:25" in narrative_notes
    assert "Greek literally says and it came to be in that night" in narrative_notes["Judges 6:25"]["footnote_text"]


def test_genesis_31_41_wage_unit_note_matches_lxx_review() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/lxx_greek/ot_full.csv")}
    decisions_by_ref = {row["ref"]: row for row in csv_rows("data/research/translation_decisions.csv")}
    notes_by_ref = {row["ref"]: row for row in csv_rows("data/research/translation_footnotes.csv")}
    expected = (
        "These twenty years I have been in your house. I served you fourteen years for your "
        "two daughters and six years among your sheep, and you falsely reckoned my wages as "
        "ten ewe lambs."
    )

    assert source_by_ref["Genesis 31:41"]["draft_translation"] == expected
    assert decisions_by_ref["Genesis 31:41"]["chosen_rendering"] == (
        "you falsely reckoned my wages as ten ewe lambs"
    )
    assert "MT ten times" in decisions_by_ref["Genesis 31:41"]["rationale"]
    assert notes_by_ref["Genesis 31:41"]["trigger_phrase"] == expected
    assert "ten times" in notes_by_ref["Genesis 31:41"]["footnote_text"]
    assert "as ten ewe lambs" in notes_by_ref["Genesis 31:41"]["footnote_text"]


def test_greek_concordance_preview_is_greek_driven_and_compact() -> None:
    output_dir = ROOT / "output" / "working" / "test_greek_concordance"
    preview = output_dir / "greek_concordance_preview.md"
    diagnostics = output_dir / "greek_concordance_preview_diagnostics.json"
    result = subprocess.run(
        [
            sys.executable,
            "scripts/build_greek_concordance_preview.py",
            "--output-md",
            str(preview),
            "--diagnostics",
            str(diagnostics),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )

    diagnostic_data = json.loads(diagnostics.read_text(encoding="utf-8"))
    preview_text = preview.read_text(encoding="utf-8")
    terms = csv_rows("data/research/greek_concordance_terms.csv")

    assert json.loads(result.stdout)["rough_page_estimate_at_450_words"] <= 30
    assert diagnostic_data["terms_in_table"] == len(terms)
    assert diagnostic_data["terms_included"] < diagnostic_data["terms_in_table"]
    assert diagnostic_data["terms_with_matches"] == diagnostic_data["terms_included"]
    assert diagnostic_data["rough_page_estimate_at_450_words"] <= 30
    assert "curated Greek forms" in diagnostic_data["method"]
    assert "## Spirit / Wind / Breath" in preview_text
    assert "Greek: πνεῦμα (pneuma)" in preview_text
    assert "**Spirit**" in preview_text
    assert "**wind**" in preview_text
    assert "Jer 10:14" in preview_text
    assert "Jeremiah 10:14" not in preview_text
    assert "## Lord" not in preview_text
    spirit_line = next(line for line in preview_text.splitlines() if line.startswith("**Spirit**"))
    assert "; " not in spirit_line


def test_broad_greek_concordance_preview_is_capped_and_abbreviated() -> None:
    output_dir = ROOT / "output" / "working" / "test_greek_concordance"
    preview = output_dir / "greek_concordance_broad_preview.md"
    diagnostics = output_dir / "greek_concordance_broad_preview_diagnostics.json"
    result = subprocess.run(
        [
            sys.executable,
            "scripts/build_greek_concordance_preview.py",
            "--profile",
            "broad",
            "--output-md",
            str(preview),
            "--diagnostics",
            str(diagnostics),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )

    diagnostic_data = json.loads(diagnostics.read_text(encoding="utf-8"))
    preview_text = preview.read_text(encoding="utf-8")

    stdout_data = json.loads(result.stdout)
    budget_field = stdout_data["page_budget_estimate_field"]
    assert budget_field == "rough_compact_print_page_estimate_at_900_words"
    assert stdout_data[budget_field] <= stdout_data["page_budget_target"]
    assert diagnostic_data["profile"] == "broad-capped"
    assert diagnostic_data[diagnostic_data["page_budget_estimate_field"]] <= diagnostic_data["page_budget_target"]
    assert diagnostic_data["terms_in_table"] >= 430
    assert diagnostic_data["terms_rendered"] >= 430
    assert diagnostic_data["terms_with_matches"] >= diagnostic_data["terms_rendered"]
    assert diagnostic_data["total_omitted_refs"] > 0
    assert diagnostic_data["suppressed_other_rendering_hits"] > 0
    assert "anchor refs" in diagnostic_data["ranking"]
    assert "## God (θεός, theos)" in preview_text
    assert "## Faith / Trust (πίστις, pistis)" in preview_text
    assert "## Hospitality (φιλοξενία, philoxenia)" in preview_text
    assert "## Seek (ζητέω, zeteo)" in preview_text
    assert "## Hear (ἀκούω, akouo)" in preview_text
    assert "## Joshua (Ἰησοῦς, Iesous)" in preview_text
    assert "## Peter (Πέτρος, Petros)" in preview_text
    assert "Omitted for print space" not in preview_text
    assert "other rendering" not in preview_text
    assert re.search(r"^Greek:", preview_text, re.MULTILINE) is None
    assert "Gen 1:2" in preview_text
    assert "Genesis 1:2" not in preview_text
    headings = re.findall(r"^## (.+?) \(", preview_text, re.MULTILINE)
    heading_sort_key = lambda heading: re.sub(r"[^0-9a-z]+", " ", heading.casefold()).strip()
    assert headings
    assert headings == sorted(headings, key=heading_sort_key)
    ref_lines = [line for line in preview_text.splitlines() if line.startswith("**")]
    assert ref_lines
    assert not any("; " in line for line in ref_lines)


def test_safe_review_csv_append_quotes_commas(tmp_path: Path) -> None:
    target = tmp_path / "review.csv"
    target.write_text("ref,note\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "append_review_csv_rows.py"), str(target)],
        input="Jeremiah 1:1\tcomma, inside field\n",
        text=True,
        capture_output=True,
        check=True,
    )

    rows = list(csv.DictReader(target.open("r", encoding="utf-8", newline="")))
    assert rows == [{"ref": "Jeremiah 1:1", "note": "comma, inside field"}]
    assert not csv_shape_issues(target)
    assert "appended_rows" in result.stdout


def test_safe_csv_update_quotes_commas_and_preserves_unchanged_rows(tmp_path: Path) -> None:
    target = tmp_path / "source.csv"
    target.write_bytes(b"ref,draft_translation\r\nJeremiah 1:1,old\r\nJeremiah 1:2,keep\r\n")

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "update_csv_column_from_tsv.py"),
            str(target),
        ],
        input="Jeremiah 1:1\tnew, with comma\n",
        text=True,
        capture_output=True,
        check=True,
    )

    data = target.read_bytes()
    assert b"Jeremiah 1:2,keep\r\n" in data
    assert b'"new, with comma"' in data
    rows = list(csv.DictReader(target.open("r", encoding="utf-8", newline="")))
    assert rows == [
        {"ref": "Jeremiah 1:1", "draft_translation": "new, with comma"},
        {"ref": "Jeremiah 1:2", "draft_translation": "keep"},
    ]
    assert "updated_rows" in result.stdout


def test_tr_manifest_matches_imported_csv() -> None:
    manifest = json.loads((ROOT / "data/raw/tr_greek/source_manifest.json").read_text(encoding="utf-8"))
    nt_rows = csv_rows("data/raw/tr_greek/nt_full.csv")
    books = {row["book_code"] for row in nt_rows}

    assert manifest["upstream_commit"] == "6049a43b135ed870f843b83eb6a04764fc796678"
    assert manifest["diagnostics"]["rows"] == len(nt_rows)
    assert manifest["diagnostics"]["book_count"] == len(books)
    assert all(row["ukjv_translation"].strip() for row in nt_rows)


def test_jeremiah_33_mt_only_completeness_insertion_is_marked_and_mapped() -> None:
    ot_rows = csv_rows("data/raw/lxx_greek/ot_full.csv")
    mt_only_rows = [row for row in ot_rows if row["greek_text"] == "MT-only insertion; no LXX Greek row"]

    assert [row["ref"] for row in mt_only_rows] == [f"Jeremiah 40:{verse}" for verse in range(14, 27)]
    assert all(row["draft_translation"].startswith("[") and row["draft_translation"].endswith("]") for row in mt_only_rows)

    versification_map = json.loads(
        (ROOT / "data" / "versification" / "lxx_to_eng_map.json").read_text(encoding="utf-8")
    )["mapped_refs"]
    for verse in range(14, 27):
        assert versification_map[f"JER 40:{verse}"] == f"JER 33:{verse}"

    notes = csv_rows("data/research/translation_footnotes.csv")
    note = next(row for row in notes if row["ref"] == "Jeremiah 40:14" and row["note_type"] == "textual")
    assert "supplies MT Jeremiah 33:14-26" in note["footnote_text"]
    assert "absent from the LXX text used here" in note["footnote_text"]
    assert "not quoted in the New Testament" in note["footnote_text"]


def test_major_mt_lxx_gap_notes_are_specific() -> None:
    notes = csv_rows("data/research/translation_footnotes.csv")
    textual_notes = {
        row["ref"]: row["footnote_text"]
        for row in notes
        if row["note_type"] == "textual" and row["source_basis"] == "MT/LXX gap annotation"
    }

    expected_ranges = {
        "1 Samuel 17:32": "MT 1 Samuel 17:12-31",
        "1 Samuel 17:42": "MT 1 Samuel 17:41",
        "1 Samuel 17:51": "MT 1 Samuel 17:50",
        "1 Samuel 18:12": "MT 1 Samuel 17:55-18:11",
        "1 Kings 9:26": "MT 1 Kings 9:15-25",
        "1 Kings 14:21": "MT 1 Kings 14:1-20",
        "1 Chronicles 1:17": "MT 1 Chronicles 1:11-16",
        "1 Chronicles 1:24": "MT 1 Chronicles 1:18-23",
        "Proverbs 20:23": "MT Proverbs 20:14-22",
    }
    for ref, mt_range in expected_ranges.items():
        assert mt_range in textual_notes[ref]
        assert "LXX-numbered point" in textual_notes[ref] or "shorter Septuagint text" in textual_notes[ref]


def test_1_kings_20_21_lxx_ordering_is_present_and_mapped() -> None:
    ot_rows = csv_rows("data/raw/lxx_greek/ot_full.csv")
    by_ref = {row["ref"]: row for row in ot_rows}

    assert "Naboth" in by_ref["1 Kings 20:1"]["draft_translation"]
    assert "Ben-hadad" in by_ref["1 Kings 21:1"]["draft_translation"]

    versification_map = json.loads(
        (ROOT / "data" / "versification" / "lxx_to_eng_map.json").read_text(encoding="utf-8")
    )["mapped_refs"]
    assert versification_map["1KI 21:1"] == "1KI 20:1"
    assert versification_map["1KI 21:43"] == "1KI 20:43"


def test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes() -> None:
    ot_rows = csv_rows("data/raw/lxx_greek/ot_full.csv")
    by_ref = {row["ref"]: row for row in ot_rows}

    assert "cast a trance on Adam" in by_ref["Genesis 2:21"]["draft_translation"]
    assert "lie in wait for your head" in by_ref["Genesis 3:15"]["draft_translation"]
    assert by_ref["Job 19:25"]["draft_translation"] == "For I know that eternal is the one who is about to free me upon earth."
    assert "The gods who did not make" in by_ref["Jeremiah 10:11"]["draft_translation"]
    assert "The gods of nations" in by_ref["Daniel 4:37"]["draft_translation"]
    assert by_ref["Ecclesiastes 3:1"]["draft_translation"].startswith("For all things there is a time")
    assert "the Lord himself will give you a sign" in by_ref["Isaiah 7:14"]["draft_translation"]
    assert not [row["ref"] for row in ot_rows if "Gods " in row["draft_translation"]]
    assert not [row["ref"] for row in ot_rows if "These things says" in row["draft_translation"]]

    notes = csv_rows("data/research/translation_footnotes.csv")
    assert not [row["ref"] for row in notes if "Direct Logos export" in row["footnote_text"]]
    notes_by_ref = {(row["ref"], row["note_type"]): row for row in notes}
    assert "modern English connotations of ecstasy" in notes_by_ref[("Genesis 2:21", "translation")]["footnote_text"]
    assert "hostile force" in notes_by_ref[("Genesis 3:15", "translation")]["footnote_text"]
    assert "making the English sentence complete" in notes_by_ref[("Job 19:25", "translation")]["footnote_text"]
    assert "Psalm 22:16 with pierced language" in notes_by_ref[("Psalms 21:17", "translation")]["footnote_text"]
    assert "Ancient of Days" in notes_by_ref[("Daniel 7:13", "textual")]["footnote_text"]
    assert "τάσσω can mean arrange or set in order" in notes_by_ref[
        ("Song of Solomon 2:4", "translation")
    ]["footnote_text"]
    assert "compact comparisons" in notes_by_ref[
        ("Song of Solomon 8:6", "translation")
    ]["footnote_text"]


def test_known_release_blocker_fixes_stay_fixed() -> None:
    ot_rows = csv_rows("data/raw/lxx_greek/ot_full.csv")
    by_ref = {row["ref"]: row for row in ot_rows}

    gen5_refs = ("Genesis 5:21", "Genesis 5:22", "Genesis 5:25", "Genesis 5:26", "Genesis 5:27")
    for ref in gen5_refs:
        assert "Methuselah" in by_ref[ref]["draft_translation"]
        assert "Methusael" not in by_ref[ref]["draft_translation"]

    assert "Mehujael" in by_ref["Genesis 4:18"]["draft_translation"]
    assert "Mahalaleel" not in by_ref["Genesis 4:18"]["draft_translation"]
    assert "Methusael" in by_ref["Genesis 4:18"]["draft_translation"]
    assert "blameless in his generation" in by_ref["Genesis 6:9"]["draft_translation"]
    assert "blameless in his generations" not in by_ref["Genesis 6:9"]["draft_translation"]

    assert "God's" in by_ref["Deuteronomy 1:17"]["draft_translation"]
    assert "Gods" not in by_ref["Deuteronomy 1:17"]["draft_translation"]
    assert "father’s house" in by_ref["1 Samuel 9:20"]["draft_translation"]
    assert "father&#x2019;s" not in by_ref["1 Samuel 9:20"]["draft_translation"]

    searched_paths = (
        ROOT / "README.md",
        ROOT / "docs" / "ARCHITECTURE.md",
        ROOT / "docs" / "CANON_POLICY.md",
        ROOT / "data" / "book_intros_template.csv",
        ROOT / "data" / "research" / "translation_footnotes.csv",
    )
    for path in searched_paths:
        text = path.read_text(encoding="utf-8")
        assert "James 9:11" not in text
        assert "James 9:12" not in text


def test_book_intro_external_attestations_name_source_item() -> None:
    rows = csv_rows("data/book_intros_template.csv")
    by_code = {row["book_code"]: row for row in rows}

    assert by_code["2JN"]["oldest_external_reference"] == "Against Heresies 1.16.3"
    assert by_code["2JN"]["oldest_external_reference_author"] == "Irenaeus"
    assert by_code["REV"]["oldest_external_reference"] == "Dialogue with Trypho and Against Heresies"
    assert by_code["ROM"]["oldest_external_reference"] == "1 Clement"
    assert by_code["1PE"]["oldest_external_reference"] == "Polycarp to the Philippians"

    for row in rows:
        external = row["oldest_external_reference"].casefold()
        assert "likely attested by " not in external
        assert "likely echoed by " not in external
        assert "clear attestation in " not in external


def test_book_intro_earliest_witnesses_sort_oldest_to_newest() -> None:
    import build_fresh_logos_bible as logos_builder

    for row in csv_rows("data/book_intros_template.csv"):
        groups = dict(logos_builder.compact_intro_groups(row))
        witness_text = groups.get("Earliest Witnesses", "")
        if not witness_text:
            continue
        years = [logos_builder.intro_date_sort_year(item) for item in witness_text.split(" | ")]
        assert years == sorted(years), (row["book_code"], witness_text, years)


def test_book_intro_suppresses_not_applicable_timelines() -> None:
    import build_fresh_logos_bible as logos_builder

    by_code = {row["book_code"]: row for row in csv_rows("data/book_intros_template.csv")}

    for code in ("MAT", "MRK", "LUK", "JHN", "ROM", "1CO"):
        groups = dict(logos_builder.compact_intro_groups(by_code[code]))
        assert "MT Timeline" not in groups
        assert "LXX Timeline" not in groups

    wisdom_groups = dict(logos_builder.compact_intro_groups(by_code["WIS"]))
    assert "MT Timeline" not in wisdom_groups
    assert wisdom_groups["LXX Timeline"].startswith("Greek is the original language")

    genesis_groups = dict(logos_builder.compact_intro_groups(by_code["GEN"]))
    assert "MT Timeline" in genesis_groups
    assert "LXX Timeline" in genesis_groups


def test_book_intro_suppresses_negative_witness_placeholders() -> None:
    import build_fresh_logos_bible as logos_builder

    by_code = {row["book_code"]: row for row in csv_rows("data/book_intros_template.csv")}

    for code in ("MAT", "JHN", "ROM", "REV"):
        witnesses = dict(logos_builder.compact_intro_groups(by_code[code]))["Earliest Witnesses"]
        assert "Heb. No complete Hebrew original survives" not in witnesses

    wisdom_witnesses = dict(logos_builder.compact_intro_groups(by_code["WIS"]))[
        "Earliest Witnesses"
    ]
    assert "Frag. No Hebrew original is known" not in wisdom_witnesses
    assert "Gk. Codex Vaticanus and Alexandrinus" in wisdom_witnesses

    genesis_witnesses = dict(logos_builder.compact_intro_groups(by_code["GEN"]))[
        "Earliest Witnesses"
    ]
    assert "Heb. Leningrad Codex" in genesis_witnesses


def test_book_intro_source_has_no_render_placeholder_values() -> None:
    rows = csv_rows("data/book_intros_template.csv")
    placeholder_hits: list[tuple[str, str, str]] = []
    timeline_placeholder_prefixes = (
        "not applicable",
        "mt timeline not applicable",
        "lxx timeline not applicable",
        "not part of mt canon chronology",
        "not part of lxx canon chronology",
        "no secure full hebrew original survives",
    )
    negative_witness_prefixes = (
        "no complete hebrew",
        "no complete ancient hebrew",
        "no early hebrew original",
        "no early full hebrew witness",
        "no hebrew original",
        "no secure full hebrew",
    )
    for row in rows:
        for key, value in row.items():
            normalized = " ".join(value.casefold().split())
            if normalized in {"n/a", "not applicable"}:
                placeholder_hits.append((row["book_code"], key, value))
            if key in {"mt_timeline", "lxx_timeline"} and normalized.startswith(timeline_placeholder_prefixes):
                placeholder_hits.append((row["book_code"], key, value))
            if key in {"oldest_fragment", "oldest_complete_hebrew"} and normalized.startswith(
                negative_witness_prefixes
            ):
                placeholder_hits.append((row["book_code"], key, value))
    assert not placeholder_hits


def test_book_intro_witness_dates_name_artifact_ranges_not_broad_periods() -> None:
    rows = csv_rows("data/book_intros_template.csv")
    broad_period_hits: list[tuple[str, str, str]] = []
    generic_witness_hits: list[tuple[str, str, str]] = []
    broad_periods = {
        "Second Temple period",
        "Late Second Temple period",
        "Hasmonean period",
        "Herodian period",
        "Hasmonean-Herodian periods",
        "Hellenistic period",
        "Hellenistic and later",
        "Second Temple and medieval periods",
    }
    for row in rows:
        for key in ("oldest_fragment_date", "oldest_substantial_date", "oldest_complete_greek_date"):
            value = row.get(key, "").strip()
            if value in broad_periods:
                broad_period_hits.append((row["book_code"], key, value))
            if value.casefold() == "uncertain":
                broad_period_hits.append((row["book_code"], key, value))
        for key in ("oldest_fragment", "oldest_substantial_manuscript", "oldest_complete_greek"):
            value = " ".join(row.get(key, "").casefold().split())
            if any(
                phrase in value
                for phrase in (
                    "and related",
                    "early qumran",
                    "major uncials preserve",
                    "tradition is the principal",
                    "traditions preserve",
                    "greek text is the principal",
                    "greek text is primary",
                )
            ):
                generic_witness_hits.append((row["book_code"], key, row.get(key, "")))
    assert not broad_period_hits
    assert not generic_witness_hits


def test_genesis_chronology_comparison_preface_data() -> None:
    import build_fresh_logos_bible as logos_builder

    rows = logos_builder.load_genesis_chronology_comparison()
    by_patriarch = {row["patriarch"]: row for row in rows}

    assert by_patriarch["Adam -> Seth"]["lxx_age_at_son_birth"] == "230"
    assert by_patriarch["Adam -> Seth"]["mt_age_at_son_birth"] == "130"
    assert by_patriarch["Methuselah -> Lamech"]["lxx_age_at_son_birth"] == "167"
    assert by_patriarch["Methuselah -> Lamech"]["mt_age_at_son_birth"] == "187"
    assert by_patriarch["Arphaxad -> Cainan / Shelah"]["lxx_age_at_son_birth"] == "135 to Cainan"
    assert "MT omits Cainan" in by_patriarch["Arphaxad -> Cainan / Shelah"]["mt_age_at_son_birth"]


def test_genesis_chronology_comparison_renders_as_docx_table(tmp_path: Path) -> None:
    import build_fresh_logos_bible as logos_builder

    docx_path = tmp_path / "chronology.docx"
    doc = logos_builder.MinimalDocx("chronology", "chronology")
    logos_builder.add_genesis_chronology_comparison(doc)
    doc.save(docx_path)

    with zipfile.ZipFile(docx_path) as archive:
        document_xml = archive.read("word/document.xml").decode("utf-8")

    assert "<w:tbl>" in document_xml
    assert "Genesis Chronology Comparison" in document_xml
    assert "Patriarch | LXX age" not in document_xml
    assert "Methuselah -&gt; Lamech" in document_xml


def test_genesis_chronology_anchor_footnotes_present() -> None:
    rows = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_footnotes.csv")
        if row["ref"] in {"Genesis 5:3", "Genesis 11:10"}
    }

    assert rows["Genesis 5:3"]["source_basis"] == "MT/LXX chronology"
    assert "Methuselah inversion" in rows["Genesis 5:3"]["footnote_text"]
    assert rows["Genesis 11:10"]["source_basis"] == "MT/LXX chronology"
    assert "Luke 3:36" in rows["Genesis 11:10"]["footnote_text"]


def test_matthew_tr_critical_text_footnotes_present() -> None:
    source_rows = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    footnote_rows = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_footnotes.csv")
        if row["ref"] in {"Matthew 6:13", "Matthew 17:21", "Matthew 18:11", "Matthew 23:14"}
    }

    assert "οτι σου εστιν η βασιλεια" in source_rows["Matthew 6:13"]["greek_text"]
    assert "τουτο δε το γενος" in source_rows["Matthew 17:21"]["greek_text"]
    assert "ηλθεν γαρ ο υιος του ανθρωπου" in source_rows["Matthew 18:11"]["greek_text"]
    assert "κατεσθιετε τας οικιας των χηρων" in source_rows["Matthew 23:14"]["greek_text"]

    for ref in ("Matthew 6:13", "Matthew 17:21", "Matthew 18:11", "Matthew 23:14"):
        assert footnote_rows[ref]["note_type"] == "textual"
        assert "modern critical editions" in footnote_rows[ref]["footnote_text"]
        assert footnote_rows[ref]["status"] == "reviewed"


def test_mark_tr_critical_text_footnotes_present() -> None:
    source_rows = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    refs = {"Mark 7:16", "Mark 9:44", "Mark 9:46", "Mark 11:26", "Mark 15:28", "Mark 16:9"}
    footnote_rows = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_footnotes.csv")
        if row["ref"] in refs
    }

    assert "ει τις εχει ωτα" in source_rows["Mark 7:16"]["greek_text"]
    assert "ο σκωληξ αυτων" in source_rows["Mark 9:44"]["greek_text"]
    assert "ο σκωληξ αυτων" in source_rows["Mark 9:46"]["greek_text"]
    assert "ει δε υμεις ουκ αφιετε" in source_rows["Mark 11:26"]["greek_text"]
    assert "και μετα ανομων ελογισθη" in source_rows["Mark 15:28"]["greek_text"]
    assert "αναστας δε πρωι" in source_rows["Mark 16:9"]["greek_text"]

    for ref in refs:
        assert footnote_rows[ref]["note_type"] == "textual"
        assert "modern critical editions" in footnote_rows[ref]["footnote_text"]
        assert footnote_rows[ref]["status"] == "reviewed"
    assert "Mark 16:9-20" in footnote_rows["Mark 16:9"]["footnote_text"]


def test_luke_tr_critical_text_footnotes_present() -> None:
    source_rows = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    refs = {"Luke 2:14", "Luke 9:55", "Luke 17:36", "Luke 23:17"}
    footnote_rows = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_footnotes.csv")
        if row["ref"] in refs
    }

    assert "ευδοκια" in source_rows["Luke 2:14"]["greek_text"]
    assert "ουκ οιδατε οιου πνευματος" in source_rows["Luke 9:55"]["greek_text"]
    assert "ουκ ηλθεν ψυχας ανθρωπων απολεσαι" in source_rows["Luke 9:56"]["greek_text"]
    assert "δυο εσονται εν τω αγρω" in source_rows["Luke 17:36"]["greek_text"]
    assert "αναγκην δε ειχεν" in source_rows["Luke 23:17"]["greek_text"]

    for ref in refs:
        assert footnote_rows[ref]["note_type"] == "textual"
        assert "modern critical editions" in footnote_rows[ref]["footnote_text"]
        assert footnote_rows[ref]["status"] == "reviewed"
    assert "eudokia" in footnote_rows["Luke 2:14"]["footnote_text"]
    assert "Luke 9:55-56" in footnote_rows["Luke 9:55"]["footnote_text"]


def test_john_tr_critical_text_footnotes_present() -> None:
    source_rows = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    refs = {"John 5:3", "John 7:53"}
    footnote_rows = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_footnotes.csv")
        if row["ref"] in refs
    }

    assert "εκδεχομενων την του υδατος κινησιν" in source_rows["John 5:3"]["greek_text"]
    assert "αγγελος γαρ κατα καιρον" in source_rows["John 5:4"]["greek_text"]
    assert "και επορευθη εκαστος" in source_rows["John 7:53"]["greek_text"]
    assert "μηκετι αμαρτανε" in source_rows["John 8:11"]["greek_text"]

    for ref in refs:
        assert footnote_rows[ref]["note_type"] == "textual"
        assert "modern critical editions" in footnote_rows[ref]["footnote_text"]
        assert footnote_rows[ref]["status"] == "reviewed"
    assert "John 5:3b-4" in footnote_rows["John 5:3"]["footnote_text"]
    assert "John 7:53-8:11" in footnote_rows["John 7:53"]["footnote_text"]


def test_acts_tr_critical_text_footnotes_present() -> None:
    source_rows = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    refs = {"Acts 8:37", "Acts 15:34", "Acts 24:6", "Acts 28:29"}
    footnote_rows = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_footnotes.csv")
        if row["ref"] in refs
    }

    assert "ει πιστευεις εξ ολης της καρδιας" in source_rows["Acts 8:37"]["greek_text"]
    assert "εδοξεν δε τω σιλα" in source_rows["Acts 15:34"]["greek_text"]
    assert "κατα τον ημετερον νομον" in source_rows["Acts 24:6"]["greek_text"]
    assert "παρελθων δε λυσιας" in source_rows["Acts 24:7"]["greek_text"]
    assert "και ταυτα αυτου ειποντος" in source_rows["Acts 28:29"]["greek_text"]

    for ref in refs:
        assert footnote_rows[ref]["note_type"] == "textual"
        assert "modern critical editions" in footnote_rows[ref]["footnote_text"]
        assert footnote_rows[ref]["status"] == "reviewed"
    assert "Textus Receptus;" in footnote_rows["Acts 8:37"]["footnote_text"]
    assert "Acts 24:6b-8a" in footnote_rows["Acts 24:6"]["footnote_text"]


def test_romans_tr_critical_text_footnotes_present() -> None:
    source_rows = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    refs = {"Romans 8:1", "Romans 16:24"}
    footnote_rows = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_footnotes.csv")
        if row["ref"] in refs
    }

    assert "μη κατα σαρκα περιπατουσιν" in source_rows["Romans 8:1"]["greek_text"]
    assert "η χαρις του κυριου ημων" in source_rows["Romans 16:24"]["greek_text"]

    for ref in refs:
        assert footnote_rows[ref]["note_type"] == "textual"
        assert "modern critical editions" in footnote_rows[ref]["footnote_text"]
        assert footnote_rows[ref]["status"] == "reviewed"
    assert "shorter form" in footnote_rows["Romans 8:1"]["footnote_text"]


def test_first_timothy_tr_critical_text_footnote_present() -> None:
    source_rows = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    footnote_rows = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_footnotes.csv")
        if row["ref"] == "1 Timothy 3:16"
    }

    assert "θεος εφανερωθη εν σαρκι" in source_rows["1 Timothy 3:16"]["greek_text"]
    assert footnote_rows["1 Timothy 3:16"]["note_type"] == "textual"
    assert "God was manifest in the flesh" in footnote_rows["1 Timothy 3:16"]["footnote_text"]
    assert "modern critical editions" in footnote_rows["1 Timothy 3:16"]["footnote_text"]
    assert footnote_rows["1 Timothy 3:16"]["status"] == "reviewed"


def test_first_john_comma_johanneum_textual_note_present() -> None:
    source_rows = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    footnote_rows = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_footnotes.csv")
        if row["ref"] == "1 John 5:7"
    }

    assert "ο πατηρ ο λογος και το αγιον πνευμα" in source_rows["1 John 5:7"]["greek_text"]
    assert "το πνευμα και το υδωρ και το αιμα" in source_rows["1 John 5:8"]["greek_text"]
    assert footnote_rows["1 John 5:7"]["note_type"] == "textual"
    assert "Comma Johanneum" in footnote_rows["1 John 5:7"]["footnote_text"]
    assert "modern critical editions" in footnote_rows["1 John 5:7"]["footnote_text"]
    assert footnote_rows["1 John 5:7"]["status"] == "reviewed"


def test_revelation_tr_critical_text_footnotes_present() -> None:
    source_rows = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    refs = {"Revelation 22:14", "Revelation 22:19"}
    footnote_rows = {
        row["ref"]: row
        for row in csv_rows("data/research/translation_footnotes.csv")
        if row["ref"] in refs
    }

    assert "ποιουντες τας εντολας" in source_rows["Revelation 22:14"]["greek_text"]
    assert "βιβλου της ζωης" in source_rows["Revelation 22:19"]["greek_text"]

    for ref in refs:
        assert footnote_rows[ref]["note_type"] == "textual"
        assert "modern critical editions" in footnote_rows[ref]["footnote_text"]
        assert footnote_rows[ref]["status"] == "reviewed"
    assert "wash their robes" in footnote_rows["Revelation 22:14"]["footnote_text"]
    assert "tree of life" in footnote_rows["Revelation 22:19"]["footnote_text"]


def test_reviewed_phrase_guards_match_source() -> None:
    rows_by_testament = {
        "ot": {row["ref"]: row for row in csv_rows("data/raw/lxx_greek/ot_full.csv")},
        "nt": {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")},
    }

    guards = [
        row
        for row in csv_rows("data/research/reviewed_phrase_guards.csv")
        if row["status"] == "reviewed"
    ]

    for guard in guards:
        testament = guard["testament"].strip().lower()
        assert testament in rows_by_testament, guard
        source_row = rows_by_testament[testament][guard["ref"]]
        text = source_row["draft_translation"]
        phrase = guard["phrase"]
        mode = guard["mode"]

        if mode == "contains":
            assert phrase in text, guard
        elif mode == "startswith":
            assert text.startswith(phrase), guard
        elif mode == "equals":
            assert text == phrase, guard
        elif mode == "not_contains":
            assert phrase not in text, guard
        else:
            raise AssertionError(f"Unsupported reviewed phrase guard mode: {mode}")


def test_crossref_notes_use_fresh_language_and_drop_loose_single_word_links() -> None:
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_fresh_logos_bible as logos_builder

    verses = logos_builder.load_verses(ROOT / "data/raw/lxx_greek/ot_full.csv")
    hosea_1_2 = next(verse for verse in verses if verse.ref == "Hosea 1:2")
    crossrefs, _diag = logos_builder.build_crossrefs_for_verses(
        [hosea_1_2],
        "ot",
        enabled=True,
    )

    notes = crossrefs["Hosea 1:2"]
    display_text = "\n".join(note.display_text for note in notes)
    assert "Mark 1:1" not in display_text
    assert 'Cross-references for "beginning"' not in display_text
    assert 'Cross-references for "children": Hosea 2:6.' in display_text
    assert 'Cross-references for "children": Hos 2:4.' not in display_text
    assert "2Pet 2:14" not in display_text

    genesis_1_4 = next(verse for verse in verses if verse.ref == "Genesis 1:4")
    crossrefs, _diag = logos_builder.build_crossrefs_for_verses(
        [genesis_1_4],
        "ot",
        enabled=True,
    )
    assert not crossrefs.get("Genesis 1:4")

    nt_verses = logos_builder.load_verses(ROOT / "data/raw/tr_greek/nt_full.csv")
    matthew_4_4 = next(verse for verse in nt_verses if verse.ref == "Matthew 4:4")
    crossrefs, _diag = logos_builder.build_crossrefs_for_verses(
        [matthew_4_4],
        "nt",
        enabled=True,
    )
    display_text = "\n".join(note.display_text for note in crossrefs["Matthew 4:4"])
    assert 'Cross-references for "It is"' not in display_text


def test_crossref_phrase_anchors_match_fresh_text_and_broad_links_stay_local() -> None:
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_fresh_logos_bible as logos_builder

    def endpoint_code_ref(book_label: str, chapter: str, verse: str) -> str | None:
        parsed = logos_builder.parse_cross_reference(
            f"{book_label} {int(chapter)}:{int(verse)}"
        )
        if not parsed:
            return None
        code, _label, parsed_chapter, parsed_verse, _end, _raw = parsed
        if parsed_verse is None:
            return None
        return f"{logos_builder.validation_code(code)} {parsed_chapter}:{parsed_verse}"

    def crossref_endpoints(ref: str) -> list[str | None]:
        normalized = logos_builder.normalize_space(ref.strip())
        match = logos_builder.CROSSREF_FULL_RANGE_RE.match(normalized)
        if match:
            start_book, start_chapter, start_verse, end_book, end_chapter, end_verse = (
                match.groups()
            )
            return [
                endpoint_code_ref(start_book, start_chapter, start_verse),
                endpoint_code_ref(end_book, end_chapter, end_verse),
            ]
        match = logos_builder.CROSSREF_CHAPTER_RANGE_RE.match(normalized)
        if match:
            book, start_chapter, start_verse, end_chapter, end_verse = match.groups()
            return [
                endpoint_code_ref(book, start_chapter, start_verse),
                endpoint_code_ref(book, end_chapter, end_verse),
            ]
        match = logos_builder.CROSSREF_SAME_CHAPTER_RANGE_RE.match(normalized)
        if match:
            book, chapter, start_verse, end_verse = match.groups()
            return [
                endpoint_code_ref(book, chapter, start_verse),
                endpoint_code_ref(book, chapter, end_verse),
            ]
        parsed = logos_builder.parse_cross_reference(normalized)
        if not parsed:
            return [None]
        code, _label, chapter, verse, _end, _raw = parsed
        if verse is None:
            return [None]
        return [f"{logos_builder.validation_code(code)} {chapter}:{verse}"]

    sources = (
        ("ot", ROOT / "data/raw/lxx_greek/ot_full.csv"),
        ("nt", ROOT / "data/raw/tr_greek/nt_full.csv"),
    )
    for testament, path in sources:
        verses = logos_builder.load_verses(path)
        by_ref = {verse.ref: verse for verse in verses}
        valid_refs = logos_builder.valid_crossref_code_refs(verses)
        crossrefs, _diag = logos_builder.build_crossrefs_for_verses(
            verses,
            testament,
            enabled=True,
        )

        for ref, notes in crossrefs.items():
            verse = by_ref[ref]
            source_book = verse.tsk_key[0]
            for note in notes:
                phrase = note.display_phrase
                for crossref in note.refs:
                    assert not re.fullmatch(r"[HG]\d+", crossref), (testament, ref, crossref)
                    assert not re.search(r"\(\d+\)$", crossref), (testament, ref, crossref)
                    parsed = logos_builder.parse_cross_reference(crossref)
                    assert parsed and parsed[0], (testament, ref, crossref)
                    for endpoint in crossref_endpoints(crossref):
                        assert endpoint in valid_refs, (testament, ref, crossref, endpoint)
                if not phrase:
                    continue
                assert phrase in verse.text, (testament, ref, phrase)

                words = re.findall(r"[A-Za-z0-9]+", phrase.casefold())
                assert not logos_builder.uninformative_crossref_trigger(phrase), (
                    testament,
                    ref,
                    phrase,
                )
                if (
                    len(words) == 1
                    and words[0] in logos_builder.BROAD_SINGLE_WORD_CROSSREF_TRIGGERS
                ):
                    off_book = [
                        crossref
                        for crossref in note.refs
                        if logos_builder.crossref_book_code(crossref) != source_book
                    ]
                    assert off_book == [], (testament, ref, phrase, off_book)


def test_release_hardening_ignores_reviewed_cognate_repetitions() -> None:
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_release_hardening_report as hardening

    decisions = hardening.load_csv(hardening.TRANSLATION_DECISIONS)
    reviewed_repeated_words = hardening.reviewed_repeated_word_allowlist(decisions)
    assert ("Ezekiel 38:12", "plunder") in reviewed_repeated_words

    raw_rows = hardening.load_csv(hardening.RAW_OT)
    _blocking_hits, repeated = hardening.scan_translation_text(
        raw_rows,
        reviewed_repeated_words,
    )
    assert not any(
        row["ref"] == "Ezekiel 38:12" and row["word"].casefold() == "plunder"
        for row in repeated
    )


def test_common_lord_article_formulas_are_normalized() -> None:
    ot_rows = csv_rows("data/raw/lxx_greek/ot_full.csv")
    formulas = (
        "says Lord",
        "Hear word of the Lord",
        "of Lord",
        "word of Lord",
        "day of Lord",
        "to Lord",
        "before Lord",
        "from Lord",
        "against Lord",
        "in Lord",
        "on Lord",
        "for Lord",
        "by Lord",
        "Blessed Lord",
        "Bless Lord",
        "blessed Lord",
        "praise Lord",
        "Praise Lord",
        "praised Lord",
        "praising Lord",
        "seek Lord God",
        "return upon Lord God",
        "reproach Lord God",
        "as Lord God",
        "worship King, Lord Almighty",
        "worship Lord",
        "worship Lord God",
        "forsook Lord God",
        "sought Lord God",
        "serve Lord your God",
        "serve Lord our God",
        "serve Lord their God",
        "with Lord our God",
        "through Lord our God salvation",
        "toward Lord God",
        "let Lord your God announce",
        "has Lord called",
        "Unless Lord of hosts",
        "Master Lord of hosts",
        "I = Lord",
        "with us = Lord",
        "whose Lord their God",
        "I am Lord",
        "I Lord ",
        "Where is Lord",
        "whose God is Lord",
        "my name is Lord",
        "Good and upright is Lord",
        "Righteous is Lord",
        "Blessed is Lord God",
        "at beginning is Lord",
        "establish forever, Lord Almighty",
        "Let them say, Lord, Lord Almighty",
        "called upon me, Lord Almighty",
        "said, Lord Almighty, how long",
        "Save us, God of our salvation",
        "God of our salvations will make straight way",
        "Turn us back, God of our salvations",
        "Save us, Lord our God",
        "gather us from nations",
        "to hear prayer which",
        "Lord God, to hear petition",
        "Jerusalem spirit of grace",
        "Please, Lord God of heaven",
        "restore judgment in gates",
        "set aside command of the king",
        "face of whole earth",
        "house of living God",
        "bless living God",
        "because of sins of",
        "from herbs of the earth",
        "Latter glory",
        "greater than first",
        "forgot law of your God",
        "all army of heaven",
        "honors father",
        "If I am father",
        "lips of priest",
        "and law they will seek",
        "And ravine of my mountains",
        "and ravine of mountains",
        "what way of spirit",
        "womb of pregnant woman",
        "And soul sinning will die",
        "son will not bear injustice",
        "father bear injustice",
        "Righteousness of righteous one",
        "lawlessness of lawless one",
        "set decree",
        "not doing law of your God",
        "and law of the king",
        "beginning, Lord my God",
        "not die. Lord, you appointed",
        "profane covenant",
        "fruit of my womb for sin",
        "He is Lord our God",
        "Are you not Lord who",
        "Is it not Lord who",
        "bless Lord who",
        "Sanctify Lord himself",
        "Lord of hosts with us",
        "Who is this king of glory? Lord of hosts",
        "praise name of the Lord",
        "Let name of the Lord",
        "in name of the Lord",
        "For cloud was upon the tent",
        "name of the Lord great to you",
        "place to you will be rivers",
        "nor will vessel go through",
        "from mouth of the Lord",
        "from mouth of Jeremiah",
        "from mouth of God",
        "by mouth of Jeremiah",
        "by hand of",
        "in days of",
        "In days of",
        "in land of",
        "In land of",
        "in whole land of Babylon",
        "from land of",
        "From land of",
        "into land of",
        "Into land of",
        "to land of",
        "To land of",
        "onto land of",
        "Onto land of",
        "from land which",
        "From land which",
        "into land which",
        "Into land which",
        "to land which",
        "To land which",
        "into land that",
        "Into land that",
        "into land where",
        "Into land where",
        "into land about",
        "Into land about",
        "into land concerning",
        "Into land concerning",
        "into land dark",
        "Into land dark",
        "into land like",
        "Into land like",
        "into land whose",
        "Into land whose",
        "in city of",
        "In city of",
        "from city of",
        "From city of",
        "into city of",
        "Into city of",
        "to city of",
        "To city of",
        "in mountain of",
        "In mountain of",
        "from mountain of",
        "From mountain of",
        "into mountain of",
        "Into mountain of",
        "to mountain of",
        "To mountain of",
        "before temple of",
        "Before temple of",
        "from temple of",
        "From temple of",
        "toward temple of",
        "Toward temple of",
        "in temple of",
        "In temple of",
        "upon altar of",
        "Upon altar of",
        "on altar of",
        "On altar of",
        "before altar of",
        "Before altar of",
        "to altar of",
        "To altar of",
        "before ark of",
        "Before ark of",
        "from tribe of",
        "From tribe of",
        "before face of",
        "Before face of",
        "in house of the Lord",
        "In house of the Lord",
        "from man even to woman",
        "Word of the Lord",
        "Word of God",
        "Words of the Lord",
        "in midst of",
        "In midst of",
        "from midst of",
        "From midst of",
        "into midst of",
        "Into midst of",
        "through midst of",
        "before eyes of",
        "from day when",
        "From day when",
        "from day they",
        "until day he",
        "until day of",
        "on day you",
        "On day you",
        "on day when",
        "On day when",
        "on day of",
        "On day of",
        "in day of",
        "In day of",
        "in time of",
        "In time of",
        "from beginning",
        "people of land",
        "People of land",
        "inhabitants of land",
        "sons of land",
        "Whole land",
        "all the whole land",
        "together with freewill of",
        "from streets of Jerusalem",
        "full end I will not make",
        "make no full end",
        "make you into full end",
        "will be desolation",
        "smell of perfume and light of lamp",
        "to house of",
        "into house of",
        "from house of",
        "in house of",
        "before house of",
        "against house of",
        "over house of",
        "for house of",
        "concerning house of",
        "of house of",
        "inside house of",
        "Inside house of",
        "in houses of",
        "In houses of",
        "in heart of",
        "heart of sea",
        "set your heart as heart of god",
        "from face of",
        "on face of",
        "upon face of",
        "uncover face of",
        "over face of",
        "Over face of",
        "to face of your God",
        "in wall of",
        "In wall of",
        "from wall of",
        "From wall of",
        "to wall of",
        "To wall of",
        "on wall of",
        "On wall of",
        "width of wall",
        "upon head of",
        "Upon head of",
        "over head of",
        "Over head of",
        "on head of",
        "On head of",
        "on seat of",
        "On seat of",
        "upon seat of",
        "Upon seat of",
        "in seat of",
        "In seat of",
        "before tent of",
        "Before tent of",
        "from tent of",
        "From tent of",
        "in tent of",
        "In tent of",
        "in eyes of",
        "In eyes of",
        "in ears of",
        "In ears of",
        "into ears of",
        "Into ears of",
        "from root of",
        "From root of",
        "to top of",
        "To top of",
        "from top of",
        "From top of",
        "at corner of",
        "At corner of",
        "from corner of",
        "From corner of",
        "corner of house",
        "in middle of",
        "In middle of",
        "through middle of",
        "Through middle of",
        "middle of tent",
        "middle of portion",
        "from entrance of",
        "From entrance of",
        "in entrance of",
        "In entrance of",
        "at entrance of",
        "At entrance of",
        "entrance of new gate",
        "entrance of sea",
        "to door of",
        "To door of",
        "from door of",
        "From door of",
        "door of furnace",
        "from hand of",
        "From hand of",
        "in hand of",
        "In hand of",
        "Over hand of",
        "over hand of",
        "against hand of",
        "Against hand of",
        "upon heart of",
        "Upon heart of",
        "to heart of",
        "To heart of",
        "into heart of",
        "Into heart of",
        "by gate of",
        "By gate of",
        "from gate of",
        "From gate of",
        "to gate of",
        "To gate of",
        "through gate of",
        "Through gate of",
        "in gate of",
        "In gate of",
        "gate of city",
        "in court of",
        "In court of",
        "from court of",
        "From court of",
        "to court of",
        "To court of",
        "into court of",
        "Into court of",
        "court of prison",
        "in courts of",
        "In courts of",
        "on throne of",
        "On throne of",
        "upon throne of",
        "Upon throne of",
        "in mouth of",
        "In mouth of",
        "on mouth of",
        "On mouth of",
        "to mouth of",
        "To mouth of",
        "into mouth of",
        "Into mouth of",
        "mouth of den",
        "mouth of eater",
        "ends of earth",
        "end of earth",
        "face of earth",
        "surface of earth",
        "from end of the earth",
        "from ends of the earth",
        "to end of the earth",
        "to ends of the earth",
        "from face of the earth",
        "In first year",
        "in second year",
        "in third year",
        "in fourth year",
        "in eighth year",
        "in twelfth year",
        "in sixth month",
        "of first month",
        "on first day",
        "from first day",
        "until last day",
        "the Lord stirred spirit of Cyrus",
        "all earth",
        "All earth",
        "Sound of",
        "and sound of",
        "from sound of",
        "at sound of",
        "hates sound of security",
        "heard in sea",
        "from breast",
        "from breasts of",
        "in upper court",
        "in fire of",
        "in streets of",
        "in book of",
        "upon book of",
        "in words of",
        "to words of",
        "in way of",
        "in ways of",
        "in sight of",
        "in multitude of",
        "In multitude of",
        "to multitude of",
        "by command of",
        "according to command of",
        "to command of",
        "in assembly of",
        "in plain of",
        "at beginning of",
        "in reign of",
        "on mountains of",
        "upon mountains of",
        "Upon mountains of",
        "over land of",
        "upon land of",
        "land of north",
        "land of life",
        "face of sword",
        "into hands of",
        "Into hands of",
        "in hands of",
        "In hands of",
        "from hands of",
        "From hands of",
        "by hands of",
        "By hands of",
        "into hand of",
        "Into hand of",
        "from days of",
        "From days of",
        "on mountain of",
        "On mountain of",
        "into temple of",
        "Into temple of",
        "at gate of",
        "At gate of",
        "From sound of",
        "At sound of",
        "from seed of",
        "from elders of",
        "from voice of",
        "from fruits of",
        "From fruits of",
        "from abundance of",
        "from springs of",
        "from captivity of",
        "in law of",
        " in works of",
        "in strength of",
        "in gates of",
        "in shelter of",
        "in light of",
        "in name of",
        "in vision of",
        "at end of",
        "at gates of",
        "at completion of",
        "at time of",
        "at head of",
        "to voice of",
        "to number of",
        "to birds of",
        "to beasts of",
        "to remnant of",
        "to forecourt of",
        "to chiefs of",
        "to prayer of",
        "to counsel of",
        "according to number of",
        "according to works of",
        "according to word of",
        "according to writing of",
        "according to counsel of",
        "upon prayer of",
        "by spirit of",
        "from tower of",
        "over works of",
        "over treasuries of",
        "over crushing of",
        "into depth of",
        "into chamber of",
        "on walls of",
        "Upon walls of",
        "on wings of",
        "upon wings of",
        "upon valley of",
        "through gates of",
        "to word of",
        "in writing of",
        "from sons of",
        "From sons of",
        "to sons of",
        "To sons of",
        "before sons of",
        "Before sons of",
        "from daughters of",
        "From daughters of",
        "to daughters of",
        "To daughters of",
        "in cities of",
        "In cities of",
        "to king of",
        "To king of",
        "in valley of",
        "In valley of",
        "to man of God",
        "To man of God",
        "by houses of",
        "By houses of",
        "according to houses of",
        "upon house of",
        "Upon house of",
        "from people of",
        "from peoples of",
        "upon sons of",
        "over sons of",
        "to all sons of",
        "to all people of",
        "to all house of",
        "to queen of",
        "against king of",
        "from all cities of",
        "against cities of",
        " on land of",
        "at threshing floor of",
        "from all tribes of",
        "in feast of",
        "in eighteenth year of",
        "in thirty-eighth year of",
        "on first of",
        "on thirteenth of",
        "on fourteenth of",
        "from multitude of",
        "on tops of",
        "at voice of",
        "in year of",
        "In year of",
        "said to Levites",
        "rulers of Levites",
        "contributed to Levites",
        "placed holy ark",
        "King said",
        "built, The king said",
        "God and king",
        "people and king",
        "son, and king",
        "because king desired",
        "and king speaking publicly",
        "and king asked",
        "and king honored",
        "and king sealed",
        "that king might",
        "that king did not",
        "answered king saying",
        "because mouth of sinner",
        "Spirit of fear of God",
        "And spirit of Egyptians",
        "Spirit of fullness",
        "And spirit of the Lord fell",
        "but word of our God remains",
        "Glory of God hides word",
        "Glory of Lebanon",
        "City of your holy one became",
        "And city came into siege",
        "And city was broken through",
        "Land mourned",
        "And land acted lawlessly",
        "And land will be watered",
        "and land that was desolated",
        "And land will mourn",
        "People will fall",
        "People walking in darkness",
        "People and cattle clothed themselves",
        "Birth-pangs of death",
        "Pangs of death",
        "Pangs of Hades",
        "Kings of earth",
        "Swords of enemy",
        "Desire of poor men",
        "Desire of his soul",
        "Desire of righteous",
        "Law of the Lord blameless",
        "testimony of the Lord faithful",
        "Ordinances of the Lord straight",
        "command of the Lord radiant",
        "Eyes of the Lord upon",
        "Eyes of the Lord preserve",
        "Death of sinners evil",
        "Words of his mouth",
        "Law of his God in his heart",
        "Sacrifice of praise",
        "Words of lawless men",
        "Kings of Tarshish",
        "Trees of the plain",
        "Idols of nations",
        "Heaven of heaven belongs",
        "Cup of salvation",
        "Way of truth",
        "Way of your commandments",
        "Ropes of sinners",
        "Disclosure of your words",
        "Streams of waters",
        "Beginning of your words truth",
        "Labors of your fruits",
        "Daughter of Babylon",
        "Head of their encirclement",
        "Eyes of all hope in you",
        "Praise of the Lord my mouth",
        "Exaltations of God",
        "Beginning of wisdom fear of God",
        "Beginning of the word of the Lord",
        "Works of righteous",
        "Words of ungodly",
        "Law of wise fountain of life",
        "Beginning of good way =",
        "Way of righteousness",
        "Way of evil",
        "Words of whisperers",
        "Eyes of wise man",
        "Words of mouth of wise",
        "Beginning of words of his mouth =",
        "Daughter of Zion",
        "Way of godly",
        "Daughter of my people",
        "Daughter of Egypt",
        "Words of sons of Jonadab",
        "Law of truth",
        "Sacrifice of Judah",
        "The kings of earth",
        "The swords of enemy",
        "The desire of righteous",
        "The works of righteous",
        "The words of ungodly",
        "The law of wise",
        "The words of the mouth of wise",
        "The way of godly",
        "carry anything on shoulders",
        "for continual whole burnt offering",
        "and words I put",
        "Great his rule",
        "Zeal of the Lord of hosts",
        "so that remnant of men",
        "was called upon them may seek",
        "bring third through fire",
        "he will say, the Lord is my God",
        "this one is God of gods",
        "he is God of gods",
        "your God is God of gods",
        "against God of gods",
        "servants of God of gods",
        "servants of God of heaven",
        "provoked God of heaven",
        "before God of heaven",
        "prayed to God of heaven",
        "prayed to God of gods",
        "serve God of heaven",
        "speaks against God of heaven",
        "to God of heaven",
        "of God of heaven",
        "to God of gods",
        "Give thanks to God of gods",
        "Give thanks to God of heaven",
        "shelter of God of heaven",
        "removing kingdom from kings",
        "All days of my kingdom",
        "as sweet smell to the Lord",
        "offer sacrifice and offering",
        "to seed of",
        "against inhabitants of",
        "to repair house of",
        "to build house of",
        "according to purity of",
        "to all army of",
        "in chambers of",
        "from edge of",
        "from rising of",
        "on fifth of",
        "on tenth of",
        "to rulers of",
        "into kingdom of",
        "in kingdom of",
        "through broad place of",
        "from womb of",
        "from belly of",
        "to hear voice of",
        "in hidden place of",
        "in blood of",
        "into depths of",
        "in tents of",
        "from fat of",
        "to all beasts of",
        "from fruit of",
        "upon ways of",
        "from wages of",
        "from way of",
        "in places of",
        "from glory of",
        "from east of",
        "by sword of",
        "on road of",
        "to daughter of",
        "at last of",
        "At last of",
        "at forecourt of",
        "to servant of",
        "from possession of",
        "to celebrate feast of",
        "on borders of",
        "With arrow and bow",
        "will be wasteland",
        "all foundations of earth",
        "light of ungodly will be quenched",
        "called city of righteousness",
        "speaking language of Canaan",
        "Land with ruin will be ruined",
        "man supported in trustworthy place",
        "because no man lays it to heart",
        "shut house so as not to enter",
        "from anyone passing through or returning",
        "made delightful land into destruction",
        "will grow, sitting",
        "became lion",
        "became reproach",
        "for all beasts of field",
        "Merchants from nations",
        "among nations will shudder",
        "God to family of Israel",
        "number of sons of Israel",
        "sand of sea",
        "sand of seas",
        "sand of seashore",
        "mother of young man",
        "sons of living God",
        "called house of prayer",
        "called city of the Lord",
        "called city of truth",
        "called border of lawlessness",
        "the Lord stirred spirit of the king",
        "find way in which",
        "beside gates of",
        "strengths of field",
        "in vineyards of wine",
        "In region of Jordan king",
        "in thickness of earth",
        "with force of mighty warriors",
        "concerning houses of this city",
        "in fury of wrath",
        "for pasture of camels",
        "for pasture of sheep",
        "from Syriac book",
        "Taking Arabian wife",
        "he fathered son whose name",
        "one of sons of Esau",
        "from mother Bozrah",
        "king of sons of Esau from Temanites",
        "tyrant of Sauchites",
        "king of Naamathites",
        "see limbs of men",
        "will be spectacle to all flesh",
        "And ration for him was given",
        "Words of Amos",
        "Vision of Obadiah",
        "message to nations",
        "inherit mount of Esau",
        "inherit mount of Ephraim",
        "and plain of Samaria",
        "from mount Zion",
        "avenge mount of Esau",
        "and kingdom will belong",
        "Nineveh, great city",
        "because cry of its evil",
        "according to former proclamation",
        "Book of vision of Nahum",
        "and sons of Ammon as Gomorrah",
        "like heap of threshing-floor",
        "forever; remnant of my people will plunder",
        "for boast among all peoples of earth",
        "there will no longer be Canaanite",
        "whatever foreigner calls upon you for",
        "all peoples of earth",
        "fear you as your people Israel and know",
        "become den of robbers",
        "on mount Zion",
        "called on Lord",
        "Upon heights set me",
        "from line of sons of Israel",
        "Song of songs",
        "Vision which Isaiah",
        "because great is day of Jezreel",
        "stand amazed at Lord",
        "in last days",
        "he their helper and defender",
        "I your servant",
        "whole day it my meditation",
        "you my firm place",
        "you my endurance",
        "you my protector",
        "But we your people",
        "Those trusting in the Lord like Mount Zion",
        "Blessed all fearing Lord",
        "Out of depths",
        "Lord, my heart not exalted",
        "what good or what pleasant",
        "last days mountain of the Lord",
        "upon whole earth",
        "did to whole earth",
        "plow whole earth",
        "all beasts of whole earth",
        "In joy of whole earth",
        "house of Jacob in snare",
        "and house of Esau stubble",
        "Has spirit of the Lord",
        "like lion among",
        "like lion-cub among",
        "like lion for",
        "like lion in",
        "like lion seizing",
        "trusts like lion",
        "Behold, like lion",
        "lodging like lion",
        "as lion,",
        "as lion's",
        "as beast",
        "face of great sword",
        "like sparrow ",
        "like bird ",
        "like dog ",
        "like gazelle ",
        "like calf ",
        "like dove ",
        "like horse through",
        "like bear ",
        "as deer ",
        "like eagle,",
        "like eagle.",
        "like eagle he",
        "like eagle against",
        "like eagle eager",
        "soar high like eagle",
        "widen your widowhood like eagle",
        "as young man dwelling with virgin",
        "as bridegroom rejoices over bride",
        " as ruler over",
        " as leader over",
        " as leader,",
        " as prophet to",
        " as prophet of",
        "faithful as prophet",
        "like drunkard",
        "like tree ",
        "like spider",
        "like moth",
        "like giant",
        "like wineskin",
        "like wheel within wheel",
        "as wheel within wheel",
        "like storm",
        "like torrent ",
        "like river of peace",
        "like garment",
        "like cloak",
        "like skin-bag",
        "like cloud ",
        "like cloud.",
        "like river ",
        "like wave",
        "as woman",
        "like dead man",
        "like ruined vessel",
        "as house of sacrifice",
        "as of woman",
        "as fleeing gazelle",
        "as with weapon of favor",
        "as flame burns",
        "as flame.",
        "Act like man",
        "act like man",
        "like birthing woman",
        "like son of man",
        "like sleeping man",
        "like broken man",
        "like wounded man",
        "like man;",
        "like man and",
        "like man unable",
        "like man not",
        "like man overcome",
        "like desert ",
        "like desert;",
        "like morning star",
        "like morning cloud",
        "like fruitful",
        "like vine ",
        "like vine,",
        "like vine;",
        "like blossom ",
        "like bad traveler",
        "like bad runner",
        "like good runner",
        "like fountain",
        "Like sound of",
        "like sound of",
        "like voice of",
        "like oven",
        "like bronze pot",
        "like perfume-vessel",
        "like shadow",
        "Like flower",
        "like flower",
        "like sword",
        "like stone cube",
        "like beam of",
        "like heap of",
        "like ripe threshing-floor",
        "like hired man",
        "like furnace",
        "like deaf man",
        "like deaf asp",
        "like flock",
        "like palm tree",
        "like cedar ",
        "like herd of",
        "as piece of",
        "as seal",
        "as tent",
        "as city",
        "like oak",
        "as flying bird",
        "as enemy",
        "like field",
        "as shepherd ",
        "like flame of fire",
        "as sound of",
        "as watchman",
        "as iron wall",
        "like dead of",
        "like passing shadow",
        "like passing flower",
        "like roaring of lion",
        "like force of God",
        "like breaking of waters",
        "like name of",
        "like rim of cup",
        "like funeral of",
        "as leper",
        "as stumbling-block",
        "as laughingstock",
        "Like appearance of",
        "like appearance of",
        " as appearance of",
        "like sight of",
        "like work of",
        "like likeness of",
        "like fish of the great sea",
        "like fish of the sea",
        "as eyes of servants",
        "as eyes of maidservant",
        "I was eye of blind",
        "and foot of lame",
        "This was appearance of likeness of",
        "heard voice speaking",
        "heard voice of",
        "hear sound of",
        "heard sound of",
        "endure sound of",
        ", sound of festival-keepers",
        ", sound of its waves",
        "set sound of",
        "With sound of",
        ", sound of his wheels",
        "by sound of",
        "because of sound of",
        "Remove from me sound of",
        "to sound of instruments",
        "with them was book of the law",
        "found book of the law",
        "bring book of the law",
        "toward book of the law",
        "when king heard words of law",
        "all words of the law",
        "I found book of law",
        "gave book to",
        "taught people",
        "praising king",
        "entered to king",
        "announced to king all words",
        "when king heard",
        "heard words of the law",
        "; words of the Lord refined",
        "provoked words of God",
        "All words of God",
        "words of wise",
        "all words of the Lord",
        "scroll words of the Lord",
        "hear words of the Lord",
        "like woman",
        "like vessel",
        "like hammer",
        "like arrow",
        "like dragon,",
        "like adversary",
        "like enemy",
        "like barber",
        "like bride",
        "like firebrand",
        "like torch",
        "like angel",
        "vine will give its fruit, land will give",
        "Fast of fourth",
        "forming spirit of human",
        "with commander of the king",
        "And commander of the king",
        "behold, commander of Greeks",
        "one of first rulers",
        "king of Assyrians",
        "king of Persians",
        "king of north",
        "as house of Ahab",
        "let house of David",
        "like house of David",
        "gathered house of Judah",
        "In Israel going out from Egypt, house of Jacob",
        "of law of God",
        "to law of God",
        "from law of God",
        "heed law of God",
        "recount glory of God",
        "and glory of God will",
        "gladdens heart of man",
        "strengthens heart of man",
        "brighten face with oil",
        "glorify remnant of Israel",
        "toward mountains of Israel",
        "over mountains of Israel",
        "to mountains of Israel",
        "in sound of trumpet",
        "charges of tent of testimony",
        "charges of sons of Aaron",
        "dedicated house of God",
        "destroy house of David",
        "like house of Ahab",
        "avenged house of Ahab",
        "pulled down house of God",
        "honored the people and house of God",
        "opposite house of God",
        "above house of David",
        "Why was house of God forsaken",
        "as far as house of God",
        "he blessed house of Israel",
        "he blessed house of Aaron",
        "Let house of Israel say",
        "Let house of Aaron say",
        "so house of Israel proved faithless",
        "Because in faithlessness house of Israel",
        "and house of Judah broke",
        "of the house of Israel and house of Judah",
        "brought up house of Israel",
        "people, remnant of Israel",
        "wipe out remnant of Israel",
        "bringing remnant of Israel to an end",
        "receive remnant of Israel",
        "cloud of glory of the Lord",
        "and glory of the Lord upon",
        "Let glory of the Lord",
        "because great glory of the Lord",
        "eclipse of glory of Jacob",
        "see glory of the Lord",
        "and glory of the Lord has risen",
        "earth glory of Israel",
        "of likeness of glory of the Lord",
        "Blessed glory of the Lord",
        "there glory of the Lord stood",
        "there was glory of the Lord",
        "brightness of glory of the Lord",
        "full of glory of the Lord",
        "know glory of the Lord",
        "where ark of the Lord entered",
        "book of law of Moses",
        "hear law of God",
        "Remember law of Moses",
        "this is City of David",
        "called it City of David",
        "to City of David",
        "into City of David",
        "in City of David",
        "from City of David",
        "as far as City of David",
        "beside City of David",
        "with City of David",
        "of City of David",
        "toward south of City of David",
        "supporting-wall of City of David",
        "wall outside City of David",
        "over tribes of Israel",
        "made tribes of Israel dwell",
        "and tribes of Israel attached",
        "strike tribes of Israel",
        "year of reign of",
        "out of land of Egypt",
        "enter land of Egypt",
        "entered land of Egypt",
        "strike land of Egypt",
        "destroy land of Egypt",
        "midst of land of Egypt",
        "wilderness of land of Egypt",
        "make land of Egypt",
        "give land of Egypt",
        "gave him land of Egypt",
        "Hear sound of trumpet",
        "hearing sound of trumpet",
        "heard sound of trumpet",
        "hears sound of trumpet",
        "with sound of trumpet",
        "voice of trumpet",
        "works of hands of men",
        "weakens hands of men fighting",
        "In good heart of man",
        "Let heart of man",
        "Before crushing heart of man",
        "restore heart of father to son and heart of man",
        "as good hand of God",
        "of hand of God",
        "For ways of man",
        "reproving ways of man",
        "grows tree of life",
        "good desire tree of life",
        "Healing tongue tree of life",
        "as days of tree of life",
        "judge city of bloods",
        "lest house of Joseph",
        "and house of Joseph I will",
        "fruit of womb",
        "give land of Canaan",
        "May name of God",
        "praise name of God",
        "gladden city of God",
        "behind whole house of Judah",
        "made whole house of Israel",
        "the house of Israel and house of Judah",
        "Perhaps house of Judah",
        "Jerusalem and house of Judah",
        "his flock, house of Judah",
        "answering words of truth",
        "uprightness, words of truth",
        "was City of Letters",
        "and City of Letters",
        "was City of Arba",
        "and City of Arba",
        "above Gate of Ephraim",
        "year of kingdom of",
        "Remember days of old",
        "remembered days of old",
        "Jericho, city of palms",
        "patriarchs of tribes of Israel",
        "went through cities of Judah",
        "attacked cities of Judah",
        "upon cities of Judah",
        "make cities of Judah",
        "give desolate cities of Judah",
        "and cities of Judah I will",
        "And cities of Judah",
        "know heart of sons of men",
        "right hand of poor man",
        "right hand right hand of injustice",
        "Ways of ungodly",
        "But ways of ungodly",
        "Ways of righteous",
        "guards ways of righteous life",
        "Words of wise",
        "see way of Egypt",
        "reported to him words of Rabshakeh",
        "tear apart strength of kings",
        "for army of heaven",
        "Do not hear words of prophets",
        "make land of Babylon",
        "give them land of Israel",
        "because of blood of humans",
        "And heart of weak ones",
        "And hand of man",
        "And gate of inner court faced gate of north",
        "by way of gate between",
        "by way of gate of the court",
        "for remnant of his inheritance",
        "before remnant of this people",
        "And sons of the exile",
        "And sons of the singers",
        "And export of horses",
        "And anger of the Lord",
        "And arrogance of Israel",
        "And eyes of God",
        "And force of Pharaoh",
        "And force of Chaldeans",
        "And force of the king of Babylon",
        "And he burned house of the Lord",
        "all houses of the city",
        "And he measured width of",
        "And he measured length of",
        "And one of seraphim",
        "broke down wall of Jerusalem",
        "entered house of",
        "saw wisdom of Solomon and house which he built",
        "heard name of Solomon",
        "then answer was sent",
        "according to blow of Midian",
        "in way by sea",
        "in way toward Egypt",
        "beasts of earth",
        "face of field",
        "cloud filled house",
        "and court was filled",
        "stood upon mountain opposite",
        "And all elders of Israel",
        "all Levites took ark",
        "And all leaders of force",
        "that king of Babylon",
        "And dead bodies of",
        "be example upon",
        "And eyes of Zedekiah",
        "and king of Babylon led",
        "And the name of wife of Abishur",
        "and name of their sister",
        "holy is place where",
        "And all men of Judah and Benjamin",
        "bring ark of our God",
        "served as priest in place of him",
        "reigned in place of him",
        "reign in place of him",
        "would reign in place of him",
        "who will stand in place of him",
        "Who will give my death in place of you? I, in place of you",
        "made bronze arms in place of them",
        "put satraps in place of them",
        "make in place of them iron yokes",
        "in place of every firstborn",
        "beasts of field",
        "fish of sea",
        "reptiles of earth",
        "creeping things creeping on earth",
        "in wilderness",
        "In wilderness",
        "from wilderness",
        "into wilderness",
        "to wilderness",
        "of wilderness",
        "with sons of",
        "with voice of",
        "with words of",
        "with weapons of",
        "with instruments of",
        "with beasts of",
        "with rulers of",
        "with house of",
        "with servants of",
        "with peoples of",
        "with oil of",
        "with strength of",
        "with shame of",
        "with assembly of",
        "with fat of",
        "to bring up ark of",
        "to carry ark of",
        "to enter house of",
        "to strengthen house of",
        "to turn kingdom of",
        "to valley of",
        "to ordinance of",
        "to judgment of",
        "to sins of",
        "to destroy race of",
        "from half tribe of",
        "from mountains of",
        "from brothers of",
        "from borders of",
        "from chiefs of",
        "from country of",
        "from depths of",
        "from height of",
        "in holy things of",
        "in clouds of",
        "in uprightness of",
        "in commandments of",
        "in broad place of",
        "in heat of",
        "in pillar of",
        "in path of",
        "in counsel of",
        "in mercy of",
        "in shadow of",
        "in depths of",
        "in innocence of",
        "on house of",
        "on ascent of",
        "Upon ascent of",
        "on beasts of",
        "on way of",
        "over men of",
        "by number of",
        "by words of",
        "upon words of",
        "upon kingdom of",
        "under hand of",
        "into holy of",
        "into wilderness of",
        "into torrent of",
        "into treasury of",
        "into pit of",
        "into valley of",
        "against kingdom of",
        "after end of",
        "after death of",
        "after wife of",
        "after thoughts of",
        "after pleasures of",
        "before king of",
        "to men of",
        "to abundance of",
        "to elders of",
        "to people of",
        "to ruler of",
        "to cities of",
        "to generations of",
        "to measures of",
        "to length of",
        "to whom word of",
        "from affliction of",
        "from snare of",
        "from produce of",
        "from king of",
        "from cities of",
        "from islands of",
        "from wrath of",
        "in acts of",
        "in abundance of",
        "in gathering of",
        "in council of",
        "in ways of",
        "in womb of",
        "in dark place of",
        "in glory of",
        "in prophets of",
        "in paradise of",
        "with wounded of",
        "with beauty of",
        "with fullness of",
        "with wife of",
        "with vengeance of",
        "according to matter of",
        "according to abundance of",
        "according to likeness of",
        "according to anger of",
        "according to measures of",
        "on breadth of",
        "on corner of",
        "on bank of",
        "by command of",
        "By command of",
        "by decree of",
        "by name of",
        "by king of",
        "by strength of",
        "by works of",
        "upon bed of",
        "upon inhabitants of",
        "through generations of",
        "into cities of",
        "into storerooms of",
        "into foundations of",
        "into bosom of",
        "against land of",
        "on fifteenth of",
        "at water of",
        "from dust of",
        "from mount of",
        "from sight of",
        "from men of",
        "in desires of",
        " in sons of",
        "in scroll words of",
        "to end of",
        "with blood of",
        "with blessing of",
        "with produce of",
        "with leaders of",
        "with scarcity of",
        "with water of",
        "In way of",
        "on furrows of",
        "under yoke of",
        "over affairs of",
        "over to souls of",
        "against sons of",
        "And king said",
        "And king commanded",
        "And king cried",
        "Then king issued",
        "Because king hopes",
        "But king will",
        "Because king of",
        "And king and",
        "the King ",
        "at right of",
        "upon son of",
        "for sons of",
        "For sons of",
        "for sacrifice of",
        "for service of",
        "for day of",
        "for mouth of",
        "For command of",
        "for life of",
        "for seed of",
        "for time of",
        "for light of",
        "for people of",
        "for salvation of",
        "for bread of",
        "for half tribe of",
        "for works of",
        "on twenty-fourth day of",
        "On twenty-fourth day of",
        "concerning sons of",
        "concerning words of",
        "concerning favor of",
        "into treasury-room of",
        "over third part of",
        "toward land of",
        "to drink water of",
        "in anger of",
        "for length of",
        "For length of",
        "for authority of",
        "for words of",
        "for days of",
        "for rest of",
        "toward hands of",
        "when chiefs of",
        "is breath of life",
        "is spirit of life",
        "to give inheritance of",
        "keeping charge of",
        "from end of",
        "into tribe of",
        "from hill of",
        "to bring ark of",
        "to bless house of",
        "for ark of",
        "for cities of",
        "for nails of",
        "for fine flour of",
        "for remaining sons of",
        "For divisions of",
        "by word of",
        "on servants of",
        "over cleansing of",
        "after gods of",
        "at hearing of",
        "from families of",
        "to borders of sons of",
        "into cave of",
        "from there ark of",
        "in ark of",
        "for sake of",
        "For sake of",
        "And rest of",
        "And beside border of",
        "And servants of",
        "And angel of",
        "And men of",
        "And people of",
        "And all people of",
        "And queen of",
        "And name of",
        "And ark of",
        "And word of",
        "But word of",
        "But hand of",
        "For heart of",
        "And land of",
        "And house of Israel",
        "But house of Israel",
        "House of Israel hoped",
        "House of Aaron hoped",
        "House of Levi, bless",
        "House of Jacob",
        "House of Joseph",
        "Because voice of",
        "Voice of your",
        "Voice of many",
        "Voice of one",
        "Voice of ones",
        "Voice of my",
        "Voice of cry",
        "Voice of report",
        "Voice of fear",
        "Voice of criers",
        "Voice of daughter",
        "Mouth of",
        "Hand of our God",
        "River of God",
        "Mountain of God",
        "King of Babylon heard",
        "People of the land, oppressing",
        "Remnant of Israel will",
        "And rulers of",
        "And remnant of",
        "And glory of",
        "Because of multitude of",
        "Voice of the Lord upon waters",
        "Voice of the Lord",
        "Voice of exultation",
        "voice of the Lord in magnificence",
        "Fear of the Lord pure",
        "Fear of the Lord",
        "Beginning of wisdom the fear",
        "Works of his hands",
        "Heart of",
        "Lips of",
        "Right hand of the Lord",
        "Hand of choice ones",
        "And spirit of God clothed",
        "And Spirit of God will rest",
        "in Spirit of God",
        "above people and said",
        "transgress commandments of the Lord",
        "Because you forsake Lord",
        "And king of",
        "Who measured water with hand",
        "heaven with span",
        "by handful",
        "with scale",
        "with balance",
        "all kingdoms of earth",
        "build for him house in Jerusalem",
        "Blessed man fearing Lord",
        "Blessed one having",
        "Blessed God,",
        "Blessed be Lord",
        "Blessed is one remaining",
        "Blessed soul, every simple one",
        "Blessing of one perishing came",
        "mouth of widow blessed me",
        "Curse of God in the houses of ungodly",
        "dwellings of righteous are blessed",
        "Blessing of the Lord upon the head of righteous",
        "Memory of righteous with praises",
        "name of ungodly is quenched",
        "Fountain of life in the hand of righteous",
        "Righteousness of blameless cuts",
        "Righteousness of upright rescues",
        "Wisdom of shrewd will know",
        "folly of fools in wandering",
        "Command of the Lord fountain",
        "Fear of God discipline",
        "Light of the Lord = breath",
        "Joy of righteous =",
        "Joy of our heart ceased",
        "Tongue of wise knows",
        "but mouth of fools",
        "Face of understanding man",
        "eyes of fool to the ends",
        "Tongue of nursing child",
        "Hands of compassionate women",
        "Face of the Lord is their portion",
        "Foot of man will not pass",
        "and foot of beast will not pass",
        "Face of man toward",
        "face of lion toward",
        "Hands of Zerubbabel founded",
        "Rulers of peoples gathered",
        "mighty ones of earth belong",
        "Enemies of the Lord lied",
        "Houses of lawless",
        "houses of righteous acceptable",
        "Houses of ungodly",
        "Princes of Zoan failed, and princes of Memphis",
        "Rulers of Judah became",
        "righteous with ungodly",
        "hope of ungodly",
        "overthrow of ungodly,",
        "gift of ungodly",
        "dwelling of ungodly",
        "hands of ungodly",
        "counsel of ungodly?",
        "eyes of ungodly",
        "life of ungodly",
        "witness of ungodly",
        "gladness of ungodly",
        "vengeance of ungodly",
        "afflictions of righteous ones",
        "salvation of righteous ones",
        "horns of righteous one",
        "soul of righteous man",
        "lot of righteous",
        "cry of poor upon",
        "counsel of poor man",
        "petition of poor man",
        "judgment of poor one and justice of needy",
        "Sinner provoked Lord",
        "Lawless man says",
        "Sinner will watch righteous man",
        "Sinner borrows and will not repay, but righteous man",
        "Sinner watches righteous man",
        "Fool said in his heart",
        "Righteous one will rejoice",
        "Righteous one will flower",
        "Sinner will see and be angry",
        "Wise son gladdens father",
        "but foolish son grief",
        "Ungodly one does unjust works",
        "Fool same day announces",
        "Wise man, fearing,",
        "but fool, trusting himself",
        "Fool sneers discipline of father",
        "Lawless man tests friends",
        "Wise servant calms anger of man",
        "Righteous man accuses himself",
        "Wise king winnows ungodly",
        "Lawless man = purging-scrap",
        "Wise man scaled strong cities",
        "Ungodly man stands shameless",
        "Fool dies in sins",
        "Wise man will judge nations",
        "Fool folded his hands",
        "Fool was given",
        "judgments of the Lord true",
        "word of the Lord straight",
        "salvation of man vain",
        "Precious before the Lord death",
        "The ways of righteous like",
        "The memory of the righteous with praises",
        "desire of righteous acceptable",
        "The desire of the righteous altogether good",
        "The fear of the Lord fortress",
        "The mouth of righteous drips",
        "The words of the ungodly deceitful",
        "Hearts of righteous meditate",
        "The ways of righteous men acceptable",
        "God far from ungodly",
        "prayers of righteous he hears",
        "Ways of Hades her house",
        "Ways of fools right before",
        "Ways of idle paved",
        "Ways of mindless man",
        "Ways of life thoughts",
        "counsel of holy ones understanding",
        "but tongue of unjust",
        "but mouth of upright",
        "In every place eyes of the Lord",
        "All the time eyes of evil",
        "foot of lawless man perish",
        "and way of godly prepared",
        "See how righteous man perished",
        "injustice righteous man is taken away",
        "Wrath of anger will be sent",
        "Pebbles of torrent were sweet",
        "Pillars of heaven were spread",
        "Drops of rain are counted",
        "Soul of ungodly will not be pitied",
        "Toil of fools will weary",
        "Dwellers of rock will rejoice",
        "Face of prostitute became",
        "Days of vengeance have come",
        "; days of your repayment have come",
        "Gates of rivers were opened",
        "And wings of cheroubim were",
        "And wings of cheroubim spread",
        "many of assembly had",
        "For wrath of anger is",
        "defile wife of man",
        "And fountains of waters were",
        "foundations of inhabited world",
        "There workers of lawlessness",
        "Lord steps of man",
        "The ways of ungodly",
        "But the ways of ungodly",
        "wealth of ungodly",
        "And light of moon",
        "as light of sun",
        "in day when the Lord heals",
        "And works of righteousness will be",
        "Seed of disobedient became",
        "Then eyes of blind",
        "ears of deaf will hear",
        "Because customs of nations are",
        "foot of beast will not pass",
        "And altars of laughter will be",
        "and rites of Israel will be",
        "And tract of sea will belong",
        "prisoners of congregation will",
        "And gathering of peoples will",
        "Wise in heart will",
        "but wise listens",
        "that Lord of all hearts knows",
        "And dwellers in this island",
        "those from west will",
        "those from sunrise his",
        "Voice from lips was",
        "And remnants of peace",
        "And reproach of nations",
        "Arrogance of your heart",
        "And seers of dreams",
        "Strength of the enemies was",
        "Beauties of the wilderness will",
        "Quarter of you will be",
        "and quarter of you finished",
        "and quarter I will",
        "and quarter will fall",
        "Wise will inherit",
        "Wise hide perception",
        "Wise women of her princesses",
        "Wise men were ashamed",
        "Because thought of man will",
        "will be crown of hope",
        "will be end of all who forget",
        "Good ones will be inhabitants of earth",
        "straight ones will settle in earth",
        "will be camp of sirens",
        "will be spring of water",
        "There joy of birds",
        "You will be crown of beauty",
        "will be pasture of flocks",
        "This will be sin of Egypt",
        "This is house of the Lord God",
        "this is place of those not knowing",
        "This is portion of ungodly man",
        "what is place of darkness",
        "it is gift of God",
        "Near is day of Moab",
        "That day is day of wrath",
        "he is messenger of the Lord",
        "he was man of war",
        "there was oversized man",
        "he was descendant of giants",
        "there was prophet of the Lord",
        "righteous and blameless man became object",
        "Stone which builders rejected",
        "became torment of their injustices",
        "will be downfall of horses",
        "which is city of Scythians",
        "She is mother of Onam",
        "in which is covenant",
        "It is king of Israel",
        "He is son of Jehoshaphat",
        "this is copy of decree",
        "hand is soul of every",
        "Where is house of ruler",
        "where is shelter of tents",
        "Who is father of rain",
        "is arm of yours",
        "it is king of all things",
        "where is wrath of one",
        "Where is multitude of your mercy",
        "is portion of Jacob",
        "it is land of carved images",
        "there is day of calling",
        "This is law of the house",
        "This is height of the altar",
        "This is interpretation of the writing",
        "is king of Medes",
        "is king of Greeks",
        "is first king",
        "When then is completion",
        "what is solution of this word",
        "it is sanctuary of the king",
        "What is impiety of Jacob",
        "what is sin of the house",
        "Where is dwelling of lions",
        "He was priest of God",
        "Timnah was concubine",
        "it was days of wheat",
        "he was chief of a band",
        "He was ruler of the Reubenites",
        "was gatekeeper of the door",
        "this was number of mighty",
        "Asaph from the beginning was chief",
        "this was lawlessness of Sodom",
        "became grass of field",
        "This is beginning of the Lord",
        "time is completion of release-hands",
        "She is beginning of sin",
        "Joseph was ruler of the land",
        "Wisdom built a house for and",
        "Wisdom good with inheritance",
        "Wisdom good above weapons",
        "Death and life in the hand of tongue",
        "Folly of man ruins",
        "Glory to man to turn",
        "Folly fastened to",
        "Wisdom will help wise",
        "Wisdom and good understanding at",
        "Lawless men set city",
        "Fear and pit and snare upon",
        "whose king son of nobles",
        "This one is father of the Moabites",
        "This one is father of the Ammonites",
        "he is father of Jesse",
        "he is king of glory",
        "He was father of those",
        "Ham was father of Canaan",
        "was servant of your father",
        "there became sons of Belah",
        "became servants of David",
        "portions of foxes",
        "folds of flocks",
        "just as house of Israel was ashamed",
        "until time of completion",
        "Light turned to darkness",
        "Righteous men seeing",
        "Wisdom hymns",
        "Righteous escapes from trap",
        "Joy lingers for righteous",
        "Righteous forever will",
        "Righteous pities souls",
        "Righteous openly displays",
        "Righteous hates unjust word",
        "Light for righteous always",
        "Righteous son is born",
        "Ungodly is carried",
        "but ungodly will not inhabit earth",
        "Ungodly all day",
        "Ungodly flees",
        "Death swallowed after",
        "Lawless one failed",
        "Lawless in Zion",
        "There will be joy of birds",
        "where was hope of help",
        "I was father of weak",
        "This one was father of Ziph",
        "Maon was father of Bethzur",
        "This one was father of Eshton",
        "Death is rest to a man",
        "until moon is removed",
        "set his footsteps in way",
        "Light arose for righteous one",
        "Glory and wealth in his house",
        "Righteous ones cried out",
        "Righteous will instruct",
        "oil of sinner",
        "Righteous lips acceptable",
        "Righteous will make many years",
        "Righteous eating fills",
        "Righteous understands",
        "Righteous father rears",
        "Righteous king raises",
        "Righteous knows how",
        "sinner one will destroy",
        "Fear and anger became",
        "Judah knew them before God",
        "trusting on them",
        "brother to her father",
        "so was standing of brightness",
        "Ungodly is one saying",
        "Wise and understanding men they call",
        "Morning they did not tread",
        "he was son of Rebekah",
        "Amasa was son of a man",
        "this one was son of Isabia",
        "overseer of the Levites was son",
        "he himself was son of Zerah",
        "he was chief of three",
        "Ioudias was chief of Hebronites",
        "Ahithophel was counselor of the king",
        "Cushi was first friend",
        "was overseer of men of war",
    )
    non_possessive_lord = r"(?<![Tt]he )(?<!my )(?<!your )(?<!our )(?<!his )(?<!their )\bLord "
    bare_subject_pattern = re.compile(
        non_possessive_lord +
        r"(?:will|has|is|was|sent|said|spoke|gave|gives|heard|chose|chooses|loved|humbled|"
        r"stopped|swore|turned|testified|came|comes|sits|destroys|destroyed|saved|saves|"
        r"answered|guards|guarded|increased|blessed|became|awoke|thundered|reign|reigns|"
        r"dwells|dwelt|delights|made|makes|struck|strengthened|listened|magnified|raised|"
        r"directed|brought|did|does|took|opened|shields|speaks|revealed|appeared|went|"
        r"arose|looked|passes|passed|helps|cares|commands|commanded)\b"
    )
    bare_title_pattern = re.compile(
        non_possessive_lord + r"(?:God|Almighty|God Almighty|God of Israel|Most High)\b"
        r"(?= (?:has|was|will|is|sent|answered|his|may|with|touching|gave|chose|loved|said|"
        r"spoke|comes|came|sits|destroys|destroyed|blow|shield|visit|name|fearful|kind|high|"
        r"gives|heard|swore|turned|testified|became|awoke|thundered|reign|reigns|dwells|"
        r"dwelt|delights|made|makes|struck|strengthened|listened|magnified|raised|directed|"
        r"brought|did|does|took|opened|speaks|revealed|appeared|went|arose|looked|passes|"
        r"passed|helps|cares|commands|commanded)\b)"
    )
    bare_phrase_patterns = (
        re.compile(r"\bking [A-Z][A-Za-z-]+"),
        re.compile(r"\b(to|before|with|from|against|for) king\b"),
        re.compile(r"\band king of\b"),
        re.compile(r"\band king were\b"),
        re.compile(r"\band king put\b"),
        re.compile(r"^Spirit of the Lord on me\b"),
        re.compile(r"(?<![Tt]he )\bLord God of heaven gave me\b"),
        re.compile(r"(?<![Tt]he )\bLord our God will save\b"),
        re.compile(r"(?<![Tt]he )\bLord your God spoke\b"),
        re.compile(r"(?<![Tt]he )\bLord your God in you,"),
        re.compile(r"(?<![Tt]he )\bLord who gathers\b"),
        re.compile(r"(?<![Tt]he )\bLord called your name\b"),
        re.compile(r"(?<![Tt]he )\bword of the Lord came\b"),
        re.compile(r"(?<![Tt]he )(?<![Tt]he great )\bday of the Lord is near\b"),
        re.compile(r"(?<![Tt]he )\bLord of hosts (?:has|counseled|commanded|will)\b"),
        re.compile(r"(?<![Tt]he )\bLord lives\b"),
        re.compile(r"\bExalt Lord our God\b"),
        re.compile(r"\bWho like Lord our God\b"),
        re.compile(r"\btoward Lord our God\b"),
        re.compile(r"\bHoly, holy, holy, Lord of hosts\b"),
        re.compile(r"\bking Lord of hosts\b"),
        re.compile(r"(?<![Tt]he )\bGod of heaven will set up\b"),
        re.compile(r"(?<![Tt]he )\bGod of heaven has authority\b"),
        re.compile(r"(?<![Tt]he )\bGod of heaven did in me\b"),
        re.compile(r"(?<![Tt]he )\bGod of heaven, he will\b"),
        re.compile(r"(?<![Tt]he )\bGod of gods, Lord, spoke\b"),
        re.compile(r"(?<![Tt]he )\bGod of gods will be seen\b"),
        re.compile(r"\bof month\b"),
        re.compile(r"\bhouse of king\b"),
        re.compile(r"\bof king\b"),
        re.compile(r"\bof people\b"),
        re.compile(r"\bof city\b"),
        re.compile(r"\bof house\b"),
        re.compile(r"\bof temple\b"),
        re.compile(r"\band house of the king\b"),
        re.compile(r"(?<![Tt]he )\bheart of the king will perish\b"),
        re.compile(r"\ball people\b"),
        re.compile(r"\ball assembly\b"),
        re.compile(r"\ball land\b"),
            re.compile(r"\bfrom breath of\b"),
            re.compile(r"\bfrom presence of\b"),
            re.compile(r"\bin wilderness of\b"),
            re.compile(r"\bin plain\b"),
            re.compile(r"\bIn plain\b"),
            re.compile(r"\binto plain\b"),
            re.compile(r"\bfrom plain\b"),
            re.compile(r"\bof plain\b"),
            re.compile(r"\bin forest\b"),
            re.compile(r"\bIn forest\b"),
            re.compile(r"\bfrom forest\b"),
            re.compile(r"\bto forest\b"),
            re.compile(r"\bof forest\b"),
            re.compile(r"\b(?:to|upon|from|in|into|of|by) river\b"),
            re.compile(r"\bLet not king speak thus\b"),
            re.compile(r"\bexcept king of Israel only\b"),
            re.compile(r"\bwhom king of Babylon appointed\b"),
            re.compile(r"\band name of (?=(?:his|her|their|the|[A-Z]))"),
            re.compile(r"\bAnd name of (?=(?:his|her|their|the|[A-Z]))"),
            re.compile(r"\bCall name of Pharaoh\b"),
            re.compile(r"\bLet name of the great the Lord\b"),
            re.compile(r"\bLet the name of the great the Lord\b"),
            re.compile(r"\bpraise name of your boasting\b"),
            re.compile(r"\bbless name of your glory\b"),
            re.compile(r"\bprofane name of their God\b"),
            re.compile(r"(?<!the )\bname of Israel will\b"),
            re.compile(r"\bfears Lord\b"),
            re.compile(r"\bhear voice of his servant\b"),
            re.compile(r"(?<!the )\bname of the city is\b"),
            re.compile(r"(?<!the )\bland will be cleansed\b"),
            re.compile(r"(?<!a )\bhouse of refuge\b"),
            re.compile(r"\bhouse of kingdom\b"),
            re.compile(r"\bhouse of lawless one\b"),
            re.compile(r"\benter house of thief\b"),
            re.compile(r"\band house of one swearing falsely\b"),
            re.compile(r"\bThe heart of wise\b"),
            re.compile(r"\bThe heart of fool\b"),
            re.compile(r"(?<!the )\bheart of fools\b"),
            re.compile(r"\bbut heart of fools\b"),
            re.compile(r"\band heart of rulers\b"),
            re.compile(r"(?<!the )\bvoice of weeping and voice of cry\b"),
            re.compile(r"(?<!the )\bsound of shout of joy\b"),
            re.compile(r"(?<!the )\bsound of wings\b"),
            re.compile(r"(?<!the )\bsound of harmony\b"),
            re.compile(r"(?<!the )\bsound of cry\b"),
            re.compile(r"\bin gladness of\b"),
        re.compile(r"\bin wandering of\b"),
        re.compile(r"\bat dedication of\b"),
        re.compile(r"\bat mouth of\b"),
        re.compile(r"\baccording to ways of\b"),
        re.compile(r"\baccording to completion of\b"),
        re.compile(r"\bby gates of\b"),
        re.compile(r"\bfor wall of\b"),
        re.compile(r"\bfor throne of\b"),
        re.compile(r"\bfor work of\b"),
        re.compile(r"\bwith elders of\b"),
        re.compile(r"\bover faithlessness of\b"),
        re.compile(r"\binto height of\b"),
        re.compile(r"\bbefore temple\b"),
        re.compile(r"\bin temple\b"),
        re.compile(r"\bfrom temple\b"),
        re.compile(r"\btoward temple\b"),
        re.compile(r"\bentered temple\b"),
        re.compile(r"\b(?:build(?:ing)?|built|build up) house\b"),
        re.compile(r"\bto son of man\b"),
        re.compile(r"\b(?:came into|entered|from|through|in|into|to) city\b"),
        re.compile(r"\bopposite city\b"),
        re.compile(r"\bhappen to city\b"),
        re.compile(r"\badorn city\b"),
        re.compile(r"(?<!the )\bcity will be taken\b"),
        re.compile(r"\bdwelt in land\b"),
        re.compile(r"\bdwelling in land\b"),
        re.compile(r"\bdwell in land\b"),
        re.compile(r"\breigned over land\b"),
        re.compile(r"\bimposed tribute on land\b"),
        re.compile(r"\bcame into land\b"),
        re.compile(r"\bcame up against land\b"),
        re.compile(r"\b(in|on|upon|over|from|to|into|through|against) land\b(?! of)"),
        re.compile(r"\bcover land\b"),
        re.compile(r"\bcovering land\b"),
        re.compile(r"\bcurse will eat land\b"),
        re.compile(r"\bFlowers appeared in land\b"),
        re.compile(r"\b(?:the the|a a|a the|the a)\b", re.IGNORECASE),
        re.compile(r"\bbefore ark\b"),
        re.compile(r"\bin ark\b"),
        re.compile(r"\bbefore altar\b"),
        re.compile(r"\bon altar\b"),
        re.compile(r"\bupon altar\b"),
        re.compile(r"\bto altar\b"),
        re.compile(r"\bfrom altar\b"),
        re.compile(r"^(?:And|But|Because|For|Then)? ?people\b"),
        re.compile(r"\bdwelt in house from\b"),
        re.compile(r"\bbefore house\b"),
        re.compile(r"\bupon house\b"),
        re.compile(r"\binto house which\b"),
        re.compile(r"\binto house\b"),
        re.compile(r"\bstrengthen house\b"),
        re.compile(r"\bholy ark in house\b"),
        re.compile(r"\bstand in house\b"),
        re.compile(r"\bin house (?:her|over|on)"),
        re.compile(r"\bfrom house where\b"),
        re.compile(r"\binside house\b"),
        re.compile(r"\bsat in house\b"),
        re.compile(r"^(?:And |Because |For |But |Then )?voice of\b"),
        re.compile(r"^Voice of exultation\b"),
        re.compile(r"^Hand of choice ones\b"),
        re.compile(r"(^|[.;:] )right hand of\b", re.IGNORECASE),
        re.compile(r"(?<![Tt]he )\bwhole land\b"),
        re.compile(r"\bdid mighty deed\b"),
        re.compile(r"\bfreewill of\b"),
        re.compile(r"(?<!a )\bfull end\b"),
        re.compile(r"\bwill be desolation\b"),
        re.compile(r"\bWith arrow and bow\b"),
        re.compile(r"\bwill be wasteland\b"),
        re.compile(r"(?<!the )\bcities of Judah will be built\b", re.IGNORECASE),
        re.compile(r"(?<![Tt]he )\bways of ungodly\b"),
        re.compile(r"(?<![Tt]he )\bways of righteous\b"),
        re.compile(r"(?<![Tt]he )\bwords of wise\b"),
        re.compile(r"(?<!the )\bheight of men will\b"),
        re.compile(r"(?<!the )\bcity was quiet\b"),
        re.compile(r"(?<!the )\bundertaking of his heart\b"),
        re.compile(r"(?<!the )\bshadow of death\b"),
        re.compile(r"(?<!the )\bin field\b"),
        re.compile(r"\ball foundations of earth\b"),
        re.compile(r"\blight of ungodly will be quenched\b"),
        re.compile(r"\bcalled city of righteousness\b"),
        re.compile(r"\bspeaking language of Canaan\b"),
        re.compile(r"\bLand with ruin will be ruined\b"),
        re.compile(r"\bman supported in trustworthy place\b"),
        re.compile(r"(?<!the )\bglory upon him will be removed\b", re.IGNORECASE),
        re.compile(r"(?<!a )\bpursuing horse\b"),
        re.compile(r"(?<!a )\bjolting chariot\b"),
        re.compile(r"\bbecause no man lays it to heart\b"),
        re.compile(r"\bshut house so as not to enter\b"),
        re.compile(r"(?<!the )\bland behind them\b", re.IGNORECASE),
        re.compile(r"\bfrom anyone passing through or returning\b"),
        re.compile(r"\bmade delightful land into destruction\b"),
        re.compile(r"(?<!a )\bman being judged\b"),
        re.compile(r"\bwill grow, sitting\b"),
        re.compile(r"(?<!a )\bbecame lion\b"),
        re.compile(r"(?<!a )\bbecame reproach\b"),
        re.compile(r"\bfor all beasts of field\b"),
        re.compile(r"\bMerchants from nations\b"),
        re.compile(r"\bamong nations will shudder\b"),
        re.compile(r"\bGod to family of Israel\b"),
        re.compile(r"\bnumber of sons of Israel\b"),
        re.compile(r"\bsand of sea\b"),
        re.compile(r"\bsand of seas\b"),
        re.compile(r"\bsand of seashore\b"),
        re.compile(r"(?<!the )\bpeople Israel become\b"),
        re.compile(r"(?<!the )\bremnant of them will be saved\b"),
        re.compile(r"\bmother of young man\b"),
        re.compile(r"\bsons of living God\b"),
        re.compile(r"\bcalled house of prayer\b"),
        re.compile(r"\bcalled city of the Lord\b"),
        re.compile(r"\bcalled city of truth\b"),
        re.compile(r"\bcalled border of lawlessness\b"),
        re.compile(r"(?<!a )\bpeople against whom\b"),
        re.compile(r"(?<!the )\bone rescuing you\b"),
        re.compile(r"\bhe God of Israel\b"),
        re.compile(r"\bHoly One of Israel: I am your God\. I showed you to find way\b"),
        re.compile(r"\bto find way in which\b"),
        re.compile(r"\bcalled God of all the earth\b"),
        re.compile(r"\bthe Lord stirred spirit of the king\b"),
        re.compile(r"(?<!the )\bstrength of nations\b", re.IGNORECASE),
        re.compile(r"(?<!the )\bcommander of Greeks\b"),
        re.compile(r"(?<![Tt]he )\bhouse of Jacob will inherit\b"),
        re.compile(r"(?<![Tt]he )\bhouse of God will be manifest\b"),
        re.compile(r"(?<![Tt]he )\bhouse of Jacob in snare\b"),
        re.compile(r"(?<![Tt]he )\bhouse of Judah will come\b"),
        re.compile(r"(?<![Tt]he )\bremnant of Israel will\b"),
        re.compile(r"(?<![Tt]he )\bremnant of Judah perish\b"),
        re.compile(r"(?<!the )\bark of God\b"),
        re.compile(r"(?<!the )\bark of covenant\b"),
        re.compile(r"(?<![Tt]he )\bglory of God of Israel\b"),
        re.compile(r"(?<!the )\bmouth of ungodly\b"),
        re.compile(r"(?<!the )\bcamp of Philistines\b"),
        re.compile(r"(?<!the )\bspirit of life\b"),
        re.compile(r"(?<!the )\btrees of forest\b"),
        re.compile(r"(?<!the )\btent of testimony\b"),
            re.compile(r"(?<![Tt]he )\bgates of Jerusalem\b"),
        re.compile(r"(?<!the )\bgates of death\b"),
        re.compile(r"(?<![Tt]he )\bway of righteous men\b"),
        re.compile(r"(?<![Tt]he )\bway of ungodly(?: men)?\b"),
        re.compile(r"(?<!the )\bday of Sabbaths\b"),
        re.compile(r"(?<!the )\bwater of sea\b"),
        re.compile(r"(?<![Tt]he )\bmountains of Israel will be desolated\b"),
        re.compile(r"(?<![Tt]he )\bhouse of Joseph flame\b"),
        re.compile(r"(?<!the )\bwhole house of Judah\b"),
        re.compile(r"(?<!the )\bwhole house of Israel\b"),
        re.compile(r"(?<!the )\bwords of truth are\b"),
        re.compile(r"\bfrom streets of\b"),
        re.compile(r"\bsmell of perfume and light of lamp\b"),
        re.compile(r"\blight of lamp\b"),
        re.compile(r"(^|[.;:] )sound of\b", re.IGNORECASE),
        re.compile(r"(?<![Tt]he )\bhouse of the Lord was full\b"),
        re.compile(r"(?<![Tt]he )\bglory of the Lord filled house\b"),
        re.compile(r"(?<![Tt]he )\bremnant of Israel were\b"),
        re.compile(r"\bby river\b"),
    )

    for row in ot_rows:
        text = row["draft_translation"]
        assert not any(formula in text for formula in formulas), row["ref"]
        assert not any(pattern.search(text) for pattern in bare_phrase_patterns), row["ref"]
        assert not bare_subject_pattern.search(text), row["ref"]
        assert not bare_title_pattern.search(text), row["ref"]
        assert not re.search(r"(?<![Tt]he )\bLord himself will\b", text), row["ref"]
        assert "Thus said Lord" not in text, row["ref"]
        assert "said Lord" not in text, row["ref"]

    by_ref = {row["ref"]: row for row in ot_rows}
    assert "The Lord shepherds me" in by_ref["Psalms 22:1"]["draft_translation"]
    assert "nothing will be lacking to me" in by_ref["Psalms 22:1"]["draft_translation"]
    assert "The Lord said to my Lord" in by_ref["Psalms 109:1"]["draft_translation"]
    assert "forsook the Lord God of their fathers" in by_ref["2 Chronicles 7:22"]["draft_translation"]
    assert "The Lord God of heaven gave me" in by_ref["2 Chronicles 36:23"]["draft_translation"]
    assert "The Lord of hosts has commanded" in by_ref["Isaiah 13:4"]["draft_translation"]
    assert "the voice of kings and nations" in by_ref["Isaiah 13:4"]["draft_translation"]
    assert "As the Lord lives" in by_ref["Jeremiah 23:7"]["draft_translation"]
    assert "Exalt the Lord our God" in by_ref["Psalms 98:5"]["draft_translation"]
    assert by_ref["Zephaniah 3:17"]["draft_translation"].startswith("The Lord your God is in you")
    assert "by the word of the Lord" in by_ref["Numbers 33:2"]["draft_translation"]
    assert by_ref["1 Kings 17:2"]["draft_translation"].startswith("And the word of the Lord came")
    assert "Hear the word of the Lord" in by_ref["2 Kings 20:16"]["draft_translation"]
    assert "praise the name of the Lord" in by_ref["Psalms 112:1"]["draft_translation"]
    assert "for the day of the Lord is near" in by_ref["Isaiah 13:6"]["draft_translation"]
    assert "to destroy the whole inhabited world" in by_ref["Isaiah 13:5"][
        "draft_translation"
    ]
    assert "Let the name of the Lord be blessed" in by_ref["Job 1:21"]["draft_translation"]
    assert "sought the face of the Lord" in by_ref["2 Chronicles 33:12"]["draft_translation"]
    assert by_ref["Psalms 117:18"]["draft_translation"].startswith("The Lord disciplined me")
    assert by_ref["Proverbs 15:25"]["draft_translation"].startswith("The Lord tears down")
    assert "which the Lord planted" in by_ref["Isaiah 44:14"]["draft_translation"]
    assert "the Lord of heaven has authority" in by_ref["Daniel 4:17"]["draft_translation"]
    assert "relied upon the Lord saying" in by_ref["Micah 3:11"]["draft_translation"]
    assert by_ref["Exodus 40:38"]["draft_translation"] == (
        "For the cloud was upon the tent by day, and fire upon it by night, "
        "before all Israel in all their journeys."
    )
    assert by_ref["Psalms 1:1"]["draft_translation"].startswith("Blessed is the man who")
    assert by_ref["Psalms 83:5"]["draft_translation"].startswith("Blessed are those")
    assert by_ref["Psalms 145:5"]["draft_translation"].startswith("Blessed is he whose helper is the God of Jacob")
    assert "Blessed are you by the Lord" in by_ref["Psalms 113:23"]["draft_translation"]
    assert "the name of the Lord is great to you" in by_ref["Isaiah 33:21"]["draft_translation"]
    assert "from the mouth of Jeremiah" in by_ref["Ezra 1:1"]["draft_translation"]
    assert "by the mouth of Jeremiah" in by_ref["2 Chronicles 36:22"]["draft_translation"]
    assert "from the mouth of God" in by_ref["2 Chronicles 35:22"]["draft_translation"]
    assert "from the mouth of the prophets" in by_ref["Zechariah 8:9"]["draft_translation"]
    assert "by the hand of Samuel" in by_ref["1 Chronicles 11:3"]["draft_translation"]
    assert "in the days of Artaxerxes" in by_ref["Esther 1:1"]["draft_translation"]
    assert "in the land of Benjamin" in by_ref["Jeremiah 1:1"]["draft_translation"]
    assert "from the land of Egypt" in by_ref["2 Chronicles 5:10"]["draft_translation"]
    assert "into the land of sons of Ammon" in by_ref["1 Chronicles 19:2"]["draft_translation"]
    assert "to the land of enemies" in by_ref["2 Chronicles 6:36"]["draft_translation"]
    assert "onto the land of Israel" in by_ref["Ezekiel 38:8"]["draft_translation"]
    assert "return them to the land which you gave" in by_ref["2 Chronicles 6:25"]["draft_translation"]
    assert "into the land that I prepared" in by_ref["Ezekiel 20:6"]["draft_translation"]
    assert "into a dark and gloomy land" in by_ref["Job 10:21"]["draft_translation"]
    assert "into a land like your land" in by_ref["Isaiah 36:17"]["draft_translation"]
    assert "into a land whose bars" in by_ref["Jonah 2:7"]["draft_translation"]
    assert "from the city of Kirjathjearim" in by_ref["1 Chronicles 13:5"]["draft_translation"]
    assert "in the city of David" in by_ref["2 Chronicles 9:31"]["draft_translation"]
    assert "to the mountain of the Lord" in by_ref["Isaiah 2:3"]["draft_translation"]
    assert "from the mountain of Ephraim" in by_ref["Jeremiah 4:15"]["draft_translation"]
    assert "before the temple of the Lord" in by_ref["2 Chronicles 15:8"]["draft_translation"]
    assert "toward the temple of the Lord" in by_ref["Ezekiel 8:16"]["draft_translation"]
    assert "upon the altar of the Lord" in by_ref["2 Chronicles 29:21"]["draft_translation"]
    assert "before the altar of the Lord" in by_ref["2 Chronicles 6:12"]["draft_translation"]
    assert "before the ark of God" in by_ref["1 Chronicles 15:24"]["draft_translation"]
    assert by_ref["Psalms 117:15"]["draft_translation"].startswith("The voice of exultation")
    assert "the right hand of the Lord did a mighty deed" in by_ref["Psalms 117:15"]["draft_translation"]
    assert by_ref["Psalms 117:16"]["draft_translation"].startswith("The right hand of the Lord")
    assert by_ref["Proverbs 12:24"]["draft_translation"].startswith("The hand of choice ones")
    assert "the whole land of Babylon" in by_ref["Ezra 7:16"]["draft_translation"]
    assert "together with the freewill offering of the people" in by_ref["Ezra 7:16"]["draft_translation"]
    assert "With an arrow and bow" in by_ref["Isaiah 7:24"]["draft_translation"]
    assert "because the whole land will be a wasteland and thorn" in by_ref["Isaiah 7:24"]["draft_translation"]
    assert "the cities of Judah will be built" in by_ref["Psalms 68:36"]["draft_translation"]
    assert "all foundations of the earth will be shaken" in by_ref["Psalms 81:5"]["draft_translation"]
    assert by_ref["Job 18:5"]["draft_translation"].startswith("But the light of the ungodly will be quenched")
    assert "called the city of righteousness" in by_ref["Isaiah 1:26"]["draft_translation"]
    assert "speaking the language of Canaan" in by_ref["Isaiah 19:18"]["draft_translation"]
    assert "called the City of Righteousness" in by_ref["Isaiah 19:18"]["draft_translation"]
    assert by_ref["Isaiah 24:3"]["draft_translation"].startswith("The land will be ruined with ruin")
    assert "the man supported in a trustworthy place will be shaken" in by_ref["Isaiah 22:25"]["draft_translation"]
    assert "the glory upon him will be removed" in by_ref["Isaiah 22:25"]["draft_translation"]
    assert by_ref["Jeremiah 4:27"]["draft_translation"].startswith("Thus says the Lord: The whole land")
    assert "yet I will not make a full end" in by_ref["Jeremiah 4:27"]["draft_translation"]
    assert "do not make a full end" in by_ref["Jeremiah 5:10"]["draft_translation"]
    assert "I will not make a full end of you" in by_ref["Jeremiah 5:18"]["draft_translation"]
    assert "will be a desolation" in by_ref["Ezekiel 35:15"]["draft_translation"]
    assert "Greece and all the land" in by_ref["Ezekiel 27:13"]["draft_translation"]
    assert "from the streets of Jerusalem" in by_ref["Jeremiah 7:34"]["draft_translation"]
    assert "the voice of rejoicing and the voice of gladness" in by_ref["Jeremiah 7:34"]["draft_translation"]
    assert "the voice of joy and the voice of gladness" in by_ref["Jeremiah 25:10"]["draft_translation"]
    assert "the smell of perfume and the light of a lamp" in by_ref["Jeremiah 25:10"]["draft_translation"]
    assert by_ref["Jeremiah 27:22"]["draft_translation"].startswith("The sound of war")
    assert "and the sound of rattling wheels" in by_ref["Nahum 3:2"]["draft_translation"]
    assert "a pursuing horse and a jolting chariot" in by_ref["Nahum 3:2"]["draft_translation"]
    assert "the sound of lions roaring" in by_ref["Zechariah 11:3"]["draft_translation"]
    assert by_ref["Jeremiah 40:11"]["draft_translation"].startswith("The voice of gladness and the voice of joy")
    assert "because no one lays it to heart" in by_ref["Jeremiah 12:11"]["draft_translation"]
    assert "shut a house so as not to enter" in by_ref["Isaiah 24:10"]["draft_translation"]
    assert "the land behind them will be made a disappearance, with no one passing through or returning" in by_ref["Zechariah 7:14"]["draft_translation"]
    assert "they made the chosen land into disappearance" in by_ref["Zechariah 7:14"]["draft_translation"]
    assert "mother, that you bore me, a man being judged" in by_ref["Jeremiah 15:10"]["draft_translation"]
    assert "from his seed will grow up to sit" in by_ref["Jeremiah 22:30"]["draft_translation"]
    assert "became a lion" in by_ref["Ezekiel 19:3"]["draft_translation"]
    assert "became a lion" in by_ref["Ezekiel 19:6"]["draft_translation"]
    assert "became a reproach" in by_ref["Psalms 30:12"]["draft_translation"]
    assert "became food for all the beasts of the field" in by_ref["Ezekiel 34:5"]["draft_translation"]
    assert by_ref["Ezekiel 27:36"]["draft_translation"].startswith("Merchants from the nations")
    assert "among the nations will shudder" in by_ref["Ezekiel 28:19"]["draft_translation"]
    assert "God to the family of Israel" in by_ref["Jeremiah 38:1"]["draft_translation"]
    assert by_ref["Hosea 2:1"]["draft_translation"].startswith("And the number of the sons of Israel was like the sand of the sea")
    assert "than the sand of the seashore" in by_ref["Job 6:3"]["draft_translation"]
    assert "like the sand of the seas" in by_ref["Psalms 77:27"]["draft_translation"]
    assert "the people Israel become as the sand of the sea, the remnant of them will be saved" in by_ref["Isaiah 10:22"]["draft_translation"]
    assert "beyond the sand of the sea" in by_ref["Jeremiah 15:8"]["draft_translation"]
    assert "against the mother of a young man, misery at noon" in by_ref["Jeremiah 15:8"]["draft_translation"]
    assert "called sons of the living God" in by_ref["Hosea 2:1"]["draft_translation"]
    assert "called a house of prayer" in by_ref["Isaiah 56:7"]["draft_translation"]
    assert "called the city of the Lord, Zion of the Holy One of Israel" in by_ref["Isaiah 60:14"]["draft_translation"]
    assert "called the city of truth and the mountain of the Lord Almighty, a holy mountain" in by_ref["Zechariah 8:3"]["draft_translation"]
    assert "called borders of lawlessness and a people against whom" in by_ref["Malachi 1:4"]["draft_translation"]
    assert "eat the strength of nations" in by_ref["Isaiah 61:6"]["draft_translation"]
    assert "bring to you the strength of nations" in by_ref["Isaiah 60:11"]["draft_translation"]
    assert "the one rescuing you, the God of Israel, will be called the God of all the earth" in by_ref["Isaiah 54:5"]["draft_translation"]
    assert "the one rescuing you, the Holy One of Israel" in by_ref["Isaiah 48:17"]["draft_translation"]
    assert "to find the way in which you will walk" in by_ref["Isaiah 48:17"]["draft_translation"]
    assert "the one rescuing you and upholding the strength of Jacob" in by_ref["Isaiah 49:26"]["draft_translation"]
    assert "said the Lord, the one rescuing you" in by_ref["Isaiah 54:8"]["draft_translation"]
    assert "The Lord stirred the spirit of the king of Medes" in by_ref["Jeremiah 28:11"]["draft_translation"]
    assert "beside the gates of rulers" in by_ref["Proverbs 1:21"]["draft_translation"]
    assert "by the powers and by the strengths of the field" in by_ref["Song of Solomon 2:7"]["draft_translation"]
    assert "in the vineyards of wine" in by_ref["1 Chronicles 27:27"]["draft_translation"]
    assert by_ref["2 Chronicles 4:17"]["draft_translation"].startswith("In the region of Jordan the king cast them in the thickness of the earth")
    assert "with a force of mighty warriors" in by_ref["2 Chronicles 13:3"]["draft_translation"]
    assert "concerning the houses of this city" in by_ref["Jeremiah 40:4"]["draft_translation"]
    assert "in a fury of wrath" in by_ref["Ezekiel 23:25"]["draft_translation"]
    assert "establish forever, O Lord Almighty, God of Israel" in by_ref["2 Samuel 7:25"]["draft_translation"]
    assert "Let them say, O Lord, Lord Almighty, God of Israel" in by_ref["1 Chronicles 17:24"]["draft_translation"]
    assert "Save us, O God of our salvation, and deliver us from the nations" in by_ref["1 Chronicles 16:35"]["draft_translation"]
    assert "O Lord God, to hear the petition and the prayer which your servant prays" in by_ref["2 Chronicles 6:19"]["draft_translation"]
    assert "to hear the prayer which your servant prays" in by_ref["2 Chronicles 6:20"]["draft_translation"]
    assert "the God of our salvations will make a straight way for us" in by_ref["Psalms 67:20"]["draft_translation"]
    assert "Turn us back, O God of our salvations" in by_ref["Psalms 84:5"]["draft_translation"]
    assert "Save us, O Lord our God, and gather us from the nations" in by_ref["Psalms 105:47"]["draft_translation"]
    assert "your name is called upon me, O Lord Almighty" in by_ref["Jeremiah 15:16"]["draft_translation"]
    assert "said, O Lord Almighty, how long" in by_ref["Zechariah 1:12"]["draft_translation"]
    assert "Jerusalem a spirit of grace and compassion" in by_ref["Zechariah 12:10"]["draft_translation"]
    assert "for a pasture for camels" in by_ref["Ezekiel 25:5"]["draft_translation"]
    assert "for a pasture for sheep" in by_ref["Ezekiel 25:5"]["draft_translation"]
    assert "Please, O Lord God of heaven" in by_ref["Nehemiah 1:5"]["draft_translation"]
    assert "restore judgment in the gates" in by_ref["Amos 5:15"]["draft_translation"]
    assert "set aside the command of the king" in by_ref["Daniel 3:28"]["draft_translation"]
    assert "face of the whole earth" in by_ref["Daniel 4:22"]["draft_translation"]
    assert "laid waste the house of the living God because of the sins" in by_ref["Daniel 4:22"]["draft_translation"]
    assert "vessels of the house of the living God" in by_ref["Daniel 5:23"]["draft_translation"]
    assert "you did not bless the living God" in by_ref["Daniel 5:23"]["draft_translation"]
    assert "from the herbs of the earth" in by_ref["Daniel 4:33"]["draft_translation"]
    assert "the time of my release came" in by_ref["Daniel 4:34"]["draft_translation"]
    assert "to the God of gods, the great one" in by_ref["Daniel 4:34"]["draft_translation"]
    assert "the kingdom of your nation is restored" in by_ref["Daniel 4:34"]["draft_translation"]
    assert by_ref["Haggai 2:9"]["draft_translation"].startswith("The latter glory of this house")
    assert "greater than the first" in by_ref["Haggai 2:9"]["draft_translation"]
    assert "you forgot the law of your God" in by_ref["Hosea 4:6"]["draft_translation"]
    assert "created all the army of heaven" in by_ref["Hosea 13:4"]["draft_translation"]
    assert "A son honors a father" in by_ref["Malachi 1:6"]["draft_translation"]
    assert by_ref["Proverbs 28:7"]["draft_translation"].startswith("An understanding son keeps the law")
    assert "dishonors his father" in by_ref["Proverbs 28:7"]["draft_translation"]
    assert "a son dishonors his father" in by_ref["Micah 7:6"]["draft_translation"]
    assert "If I am a father" in by_ref["Malachi 1:6"]["draft_translation"]
    assert "Because the lips of a priest will guard knowledge, and they will seek the law" in by_ref["Malachi 2:7"]["draft_translation"]
    assert by_ref["Zechariah 14:5"]["draft_translation"].startswith("And the ravine of my mountains")
    assert "and the ravine of mountains" in by_ref["Zechariah 14:5"]["draft_translation"]
    assert "the face of the water" in by_ref["Ecclesiastes 11:1"]["draft_translation"]
    assert "upon the earth" in by_ref["Ecclesiastes 11:2"]["draft_translation"]
    assert "what the way of spirit is" in by_ref["Ecclesiastes 11:5"]["draft_translation"]
    assert "womb of a pregnant woman" in by_ref["Ecclesiastes 11:5"]["draft_translation"]
    assert "the works of God" in by_ref["Ecclesiastes 11:5"]["draft_translation"]
    assert "the light is sweet" in by_ref["Ecclesiastes 11:7"]["draft_translation"]
    assert "youth and folly are vanity" in by_ref["Ecclesiastes 11:10"][
        "draft_translation"
    ]
    assert by_ref["Ezekiel 18:20"]["draft_translation"].startswith("And the soul sinning will die")
    assert "a son will not bear the injustice of his father" in by_ref["Ezekiel 18:20"]["draft_translation"]
    assert "The righteousness of a righteous one" in by_ref["Ezekiel 18:20"]["draft_translation"]
    assert "The righteousness of a righteous one will not rescue him" in by_ref["Ezekiel 33:12"]["draft_translation"]
    assert "the lawlessness of an impious one will not hurt him" in by_ref["Ezekiel 33:12"]["draft_translation"]
    assert "set a decree for you" in by_ref["Ezra 5:3"]["draft_translation"]
    assert "King Darius set a decree" in by_ref["Ezra 6:1"]["draft_translation"]
    assert "Cyrus the king set a decree" in by_ref["Ezra 6:3"]["draft_translation"]
    assert "I, Darius, set a decree" in by_ref["Ezra 6:12"]["draft_translation"]
    assert "set a decree to all the treasuries" in by_ref["Ezra 7:21"]["draft_translation"]
    assert "not doing the law of your God and the law of the king" in by_ref["Ezra 7:26"]["draft_translation"]
    assert "Are you not from the beginning, O Lord my God" in by_ref["Habakkuk 1:12"]["draft_translation"]
    assert "O Lord, you appointed him for judgment" in by_ref["Habakkuk 1:12"]["draft_translation"]
    assert "profane the covenant of your fathers" in by_ref["Malachi 2:10"]["draft_translation"]
    assert "the fruit of my womb for the sin of my soul" in by_ref["Micah 6:7"]["draft_translation"]
    assert by_ref["Nehemiah 1:1"]["draft_translation"].startswith("The words of Nehemiah son of Hachaliah")
    assert "in the month of Chisleu, in the twentieth year" in by_ref["Nehemiah 1:1"]["draft_translation"]
    assert by_ref["Nehemiah 7:3"]["draft_translation"].startswith("and I said to them, The gates of Jerusalem")
    assert "from the inhabitants of Jerusalem" in by_ref["Nehemiah 7:3"]["draft_translation"]
    assert "everyone who could understand what they heard" in by_ref["Nehemiah 8:2"]["draft_translation"]
    assert by_ref["Nehemiah 13:31"]["draft_translation"].startswith("and the gift of the wood-bearers")
    assert "year by year, and in the firstfruits" in by_ref["Nehemiah 13:31"]["draft_translation"]
    assert "Remember me, O our God, for goodness" in by_ref["Nehemiah 13:31"]["draft_translation"]
    assert "all Judah and the inhabitants of Jerusalem" in by_ref["2 Chronicles 20:18"]["draft_translation"]
    assert "with his face to the ground" in by_ref["2 Chronicles 20:18"]["draft_translation"]
    assert "rose early in the morning" in by_ref["2 Chronicles 20:20"]["draft_translation"]
    assert "Judah and the inhabitants of Jerusalem" in by_ref["2 Chronicles 20:20"]["draft_translation"]
    assert by_ref["Job 22:15"]["draft_translation"].startswith("Will you keep the ancient path")
    assert by_ref["Proverbs 16:14"]["draft_translation"].startswith("The wrath of the king is a messenger of death")
    assert "but a wise man will appease him" in by_ref["Proverbs 16:14"]["draft_translation"]
    assert "be praised in the gates" in by_ref["Proverbs 31:31"]["draft_translation"]
    assert by_ref["Ecclesiastes 1:1"]["draft_translation"].startswith("The words of Ecclesiastes")
    assert "all the woods of Lebanon" in by_ref["Song of Solomon 4:14"]["draft_translation"]
    assert "all the first perfumes" in by_ref["Song of Solomon 4:14"]["draft_translation"]
    assert "like a gazelle or a fawn of deer" in by_ref["Song of Solomon 8:14"]["draft_translation"]
    assert "from the priests, who dwelt in Anathoth" in by_ref["Jeremiah 1:1"]["draft_translation"]
    assert "the judgment of a man before the face of the Most High" in by_ref["Lamentations 3:35"]["draft_translation"]
    assert by_ref["Ezekiel 1:1"]["draft_translation"].startswith("And it happened in the thirtieth year")
    assert "the heavens were opened" in by_ref["Ezekiel 1:1"]["draft_translation"]
    assert "mouth of the lions' den" in by_ref["Daniel 6:20"]["draft_translation"]
    assert by_ref["Hosea 14:10"]["draft_translation"].startswith("Who is wise")
    assert "Because the ways of the Lord are straight" in by_ref["Hosea 14:10"]["draft_translation"]
    assert "no high-sounding speech" in by_ref["1 Samuel 2:3"]["draft_translation"]
    assert "God of knowledge" in by_ref["1 Samuel 2:3"]["draft_translation"]
    assert "Those full of bread were brought low" in by_ref["1 Samuel 2:5"]["draft_translation"]
    assert "Please, lord, as your soul lives" in by_ref["1 Samuel 1:26"]["draft_translation"]
    assert "the men were cut to the heart" in by_ref["Genesis 34:7"]["draft_translation"]
    assert by_ref["Genesis 27:38"]["draft_translation"].startswith("But Esau said to his father")
    assert "when Isaac was cut to the heart" in by_ref["Genesis 27:38"]["draft_translation"]
    assert "Aaron was cut to the heart" in by_ref["Leviticus 10:3"]["draft_translation"]
    assert "the one with many children became weak" in by_ref["1 Samuel 2:5"]["draft_translation"]
    assert "each day's matter on its day" in by_ref["1 Kings 8:59"]["draft_translation"]
    assert "Ahab was cut to the heart before the Lord" in by_ref["1 Kings 20:27"]["draft_translation"]
    assert "Ahab was cut to the heart before me" in by_ref["1 Kings 20:29"]["draft_translation"]
    assert "a day's portion on its day" in by_ref["2 Kings 25:30"]["draft_translation"]
    assert "built the city all around" in by_ref["1 Chronicles 11:8"]["draft_translation"]
    assert "passed through every border of Israel" in by_ref["1 Chronicles 21:4"]["draft_translation"]
    assert "set the sea from the corner" in by_ref["2 Chronicles 4:10"]["draft_translation"]
    assert "over the place of the ark" in by_ref["2 Chronicles 5:8"]["draft_translation"]
    assert "from the day the house was founded" in by_ref["2 Chronicles 8:16"]["draft_translation"]
    assert "each day's matter on its day" in by_ref["2 Chronicles 8:14"]["draft_translation"]
    assert "the one who is about to free me" in by_ref["Job 19:25"]["draft_translation"]
    assert by_ref["Proverbs 23:27"]["draft_translation"].startswith("For a foreign house is a pierced jar")
    assert "works are works of lawlessness" in by_ref["Isaiah 59:6"]["draft_translation"]
    assert "the one who is about to eat their eggs" in by_ref["Isaiah 59:5"]["draft_translation"]
    assert "there is no judgment in their ways" in by_ref["Isaiah 59:8"]["draft_translation"]
    assert by_ref["Joel 2:17"]["draft_translation"].startswith("At the base of the altar")
    assert "Spare, O Lord, your people" in by_ref["Joel 2:17"]["draft_translation"]
    assert "say among the nations" in by_ref["Joel 2:17"]["draft_translation"]
    assert "did not know the thought of the Lord" in by_ref["Micah 4:12"]["draft_translation"]
    assert "like sheaves of the threshing floor" in by_ref["Micah 4:12"]["draft_translation"]
    assert "clap their hands over you" in by_ref["Nahum 3:19"]["draft_translation"]
    assert "Habakkuk the prophet saw" in by_ref["Habakkuk 1:1"]["draft_translation"]
    assert "one building a city in bloodshed and preparing a city" in by_ref["Habakkuk 2:12"]["draft_translation"]
    assert "around the king" in by_ref["2 Chronicles 23:10"]["draft_translation"]
    assert "the king stood at his station" in by_ref["2 Chronicles 23:13"]["draft_translation"]
    assert "through the horse gate" in by_ref["2 Chronicles 23:15"]["draft_translation"]
    assert "take the scroll" in by_ref["Jeremiah 43:21"]["draft_translation"]
    assert "from the fold, from behind the sheep" in by_ref["1 Chronicles 17:7"]["draft_translation"]
    assert by_ref["Psalms 46:3"]["draft_translation"].startswith("Because the Lord Most High is fearsome")
    assert "because the mouth of the Lord Almighty spoke these things" in by_ref["Micah 4:4"]["draft_translation"]
    assert "the spirit of the remnant of all the people" in by_ref["Haggai 1:14"]["draft_translation"]
    assert "the angel speaking with me" in by_ref["Zechariah 1:9"]["draft_translation"]
    assert "the angel speaking with me" in by_ref["Zechariah 1:13"]["draft_translation"]
    assert "the angel speaking with me" in by_ref["Zechariah 6:5"]["draft_translation"]
    assert "touching the pupil of his eye" in by_ref["Zechariah 2:12"]["draft_translation"]
    assert "carrying away the measure" in by_ref["Zechariah 5:10"]["draft_translation"]
    assert "perish from a righteous way" in by_ref["Psalms 2:12"]["draft_translation"]
    assert "Blessed are all who trust in him" in by_ref["Psalms 2:12"]["draft_translation"]
    assert by_ref["Psalms 21:29"]["draft_translation"].startswith("Because the kingdom belongs to the Lord")
    assert "rules over the nations" in by_ref["Psalms 21:29"]["draft_translation"]
    assert "the mouth of a sinner and the mouth of a deceitful one" in by_ref["Psalms 108:2"]["draft_translation"]
    assert "with a deceitful tongue" in by_ref["Psalms 108:2"]["draft_translation"]
    assert "from a deceitful tongue" in by_ref["Psalms 119:2"]["draft_translation"]
    assert "against a deceitful tongue" in by_ref["Psalms 119:3"]["draft_translation"]
    assert "a deceitful tongue" in by_ref["Psalms 51:6"]["draft_translation"]
    assert "with all my heart" in by_ref["Psalms 85:12"]["draft_translation"]
    assert "with all my heart" in by_ref["Psalms 110:1"]["draft_translation"]
    assert "with all their heart they will seek him" in by_ref["Psalms 118:2"]["draft_translation"]
    assert by_ref["Psalms 118:10"]["draft_translation"].startswith("With all my heart")
    assert "keep it with all my heart" in by_ref["Psalms 118:34"]["draft_translation"]
    assert "with all my heart" in by_ref["Psalms 118:58"]["draft_translation"]
    assert "with all my heart" in by_ref["Psalms 118:69"]["draft_translation"]
    assert "with all my heart" in by_ref["Psalms 118:145"]["draft_translation"]
    assert "with all my heart" in by_ref["Psalms 137:1"]["draft_translation"]
    assert "with all your heart" in by_ref["Proverbs 3:5"]["draft_translation"]
    assert "with all her heart" in by_ref["Jeremiah 3:10"]["draft_translation"]
    assert "with all their heart" in by_ref["2 Chronicles 6:14"]["draft_translation"]
    assert "with all my heart" in by_ref["Psalms 9:2"]["draft_translation"]
    assert "with all his heart" in by_ref["2 Chronicles 22:9"]["draft_translation"]
    assert "strong enough for the kingdom" in by_ref["2 Chronicles 22:9"]["draft_translation"]
    assert "for the kingdom and for holy things and for Israel" in by_ref["2 Chronicles 29:21"][
        "draft_translation"
    ]
    assert "You sat upon a throne, judging righteousness" in by_ref["Psalms 9:5"]["draft_translation"]
    assert "the ungodly man perished" in by_ref["Psalms 9:6"]["draft_translation"]
    assert "a refuge for the poor man" in by_ref["Psalms 9:10"]["draft_translation"]
    assert "the cry of poor men" in by_ref["Psalms 9:13"]["draft_translation"]
    assert "the sinner was caught" in by_ref["Psalms 9:17"]["draft_translation"]
    assert "the poor man will not be forgotten to the end" in by_ref["Psalms 9:19"][
        "draft_translation"
    ]
    assert "When the ungodly man acts proudly, the poor man" in by_ref["Psalms 9:23"][
        "draft_translation"
    ]
    assert "the sinner is praised" in by_ref["Psalms 9:24"]["draft_translation"]
    assert "an innocent man" in by_ref["Psalms 9:29"]["draft_translation"]
    assert "in a hidden place" in by_ref["Psalms 9:30"]["draft_translation"]
    assert "the ungodly man provoke God" in by_ref["Psalms 9:34"]["draft_translation"]
    assert "the poor man is left" in by_ref["Psalms 9:35"]["draft_translation"]
    assert "Break the arm of the sinner and evil man" in by_ref["Psalms 9:36"][
        "draft_translation"
    ]
    assert by_ref["Psalms 9:38"]["draft_translation"].startswith("The Lord heard")
    assert "an orphan and a lowly man" in by_ref["Psalms 9:39"]["draft_translation"]
    assert "For what hope is there for an ungodly man" in by_ref["Job 27:8"]["draft_translation"]
    assert "keep an ungodly man alive" in by_ref["Job 36:6"]["draft_translation"]
    assert "examines the righteous man and the ungodly man" in by_ref["Psalms 10:5"][
        "draft_translation"
    ]
    assert "I saw an ungodly man" in by_ref["Psalms 36:35"]["draft_translation"]
    assert "the upright man himself understands" in by_ref["Proverbs 21:29"]["draft_translation"]
    assert "against the ungodly man" in by_ref["Proverbs 21:30"]["draft_translation"]
    assert "partner of an ungodly man" in by_ref["Proverbs 28:24"]["draft_translation"]
    assert "Who knows a wise man" in by_ref["Ecclesiastes 8:1"]["draft_translation"]
    assert "Keep the king's mouth" in by_ref["Ecclesiastes 8:2"]["draft_translation"]
    assert "The one keeping a command" in by_ref["Ecclesiastes 8:5"][
        "draft_translation"
    ]
    assert "for the ungodly man" in by_ref["Ecclesiastes 8:13"]["draft_translation"]
    assert "this too is vanity" in by_ref["Ecclesiastes 8:14"]["draft_translation"]
    assert "all the works of God" in by_ref["Ecclesiastes 8:17"]["draft_translation"]
    assert "the righteous and the wise" in by_ref["Ecclesiastes 9:1"][
        "draft_translation"
    ]
    assert "for the righteous and the ungodly" in by_ref["Ecclesiastes 9:2"][
        "draft_translation"
    ]
    assert "the heart of the sons of man" in by_ref["Ecclesiastes 9:3"][
        "draft_translation"
    ]
    assert "a living dog is better than a dead lion" in by_ref["Ecclesiastes 9:4"][
        "draft_translation"
    ]
    assert "See life with a woman" in by_ref["Ecclesiastes 9:9"][
        "draft_translation"
    ]
    assert "Let the ungodly man leave his ways and the lawless man" in by_ref["Isaiah 55:7"][
        "draft_translation"
    ]
    assert "rescued a poor man from the hand of a mighty man" in by_ref["Job 29:12"][
        "draft_translation"
    ]
    assert "look toward the poor man" in by_ref["Psalms 10:4"]["draft_translation"]
    assert "rescuing a poor man" in by_ref["Psalms 34:10"]["draft_translation"]
    assert "for the poor one" in by_ref["Psalms 67:11"]["draft_translation"]
    assert "rescued a poor man from the hand of a ruler" in by_ref["Psalms 71:12"][
        "draft_translation"
    ]
    assert "Judge an orphan and a poor one" in by_ref["Psalms 81:3"]["draft_translation"]
    assert "Rescue a needy one and a poor one" in by_ref["Psalms 81:4"]["draft_translation"]
    assert "Prayer for the poor man" in by_ref["Psalms 101:1"]["draft_translation"]
    assert "helped a poor man out of poverty" in by_ref["Psalms 106:41"]["draft_translation"]
    assert "the poor man is deserted even by the friend he has" in by_ref["Proverbs 19:4"][
        "draft_translation"
    ]
    assert "Better a poor man walking in truth than a rich liar" in by_ref["Proverbs 28:6"][
        "draft_translation"
    ]
    assert "for a poor man there is no discerning mind" in by_ref["Proverbs 29:7"][
        "draft_translation"
    ]
    assert "slander of a poor man" in by_ref["Ecclesiastes 5:7"]["draft_translation"]
    assert "in a province" in by_ref["Ecclesiastes 5:7"]["draft_translation"]
    assert "for the wise man over the fool" in by_ref["Ecclesiastes 6:8"]["draft_translation"]
    assert "Because the poor man knows" in by_ref["Ecclesiastes 6:8"]["draft_translation"]
    assert "a poor wise man" in by_ref["Ecclesiastes 9:15"]["draft_translation"]
    assert "the wisdom of the poor man is despised" in by_ref["Ecclesiastes 9:16"][
        "draft_translation"
    ]
    assert "soul of a poor man" in by_ref["Jeremiah 20:13"]["draft_translation"]
    assert "sold a righteous one for silver and a poor one" in by_ref["Amos 2:6"][
        "draft_translation"
    ]
    assert "eating a poor one secretly" in by_ref["Habakkuk 3:14"]["draft_translation"]
    assert "a righteous man would rise up against a lawless one" in by_ref["Job 17:8"][
        "draft_translation"
    ]
    assert "from a righteous man, and with kings on a throne" in by_ref["Job 36:7"][
        "draft_translation"
    ]
    assert "hear the righteous man" in by_ref["Job 36:10"]["draft_translation"]
    assert "bless a righteous man" in by_ref["Psalms 5:13"]["draft_translation"]
    assert "set a righteous man straight" in by_ref["Psalms 7:10"]["draft_translation"]
    assert "but the righteous man, what did he do" in by_ref["Psalms 10:3"][
        "draft_translation"
    ]
    assert "against the righteous man in pride" in by_ref["Psalms 30:19"][
        "draft_translation"
    ]
    assert "hating the righteous man" in by_ref["Psalms 33:22"]["draft_translation"]
    assert "Better a little thing to the righteous man" in by_ref["Psalms 36:16"][
        "draft_translation"
    ]
    assert "did not see a righteous man forsaken" in by_ref["Psalms 36:25"][
        "draft_translation"
    ]
    assert "The mouth of a righteous man" in by_ref["Psalms 36:30"]["draft_translation"]
    assert "hide in earth a righteous man unjustly" in by_ref["Proverbs 1:11"][
        "draft_translation"
    ]
    assert "make a righteous man know" in by_ref["Proverbs 9:9"]["draft_translation"]
    assert "When a righteous man dies" in by_ref["Proverbs 11:7"]["draft_translation"]
    assert "the heart of a righteous man" in by_ref["Proverbs 12:25"][
        "draft_translation"
    ]
    assert "a righteous man does not heed lying lips" in by_ref["Proverbs 17:4"][
        "draft_translation"
    ]
    assert "lying lips a righteous man" in by_ref["Proverbs 17:7"]["draft_translation"]
    assert "To fine a righteous man is not good" in by_ref["Proverbs 17:26"][
        "draft_translation"
    ]
    assert "there is not a righteous man on earth" in by_ref["Ecclesiastes 7:20"][
        "draft_translation"
    ]
    assert "Many are the afflictions of the righteous ones" in by_ref["Psalms 33:20"][
        "draft_translation"
    ]
    assert "salvation of the righteous ones is from the Lord" in by_ref["Psalms 36:39"][
        "draft_translation"
    ]
    assert "the horns of the righteous one will be exalted" in by_ref["Psalms 74:11"][
        "draft_translation"
    ]
    assert "upon the lot of the righteous" in by_ref["Psalms 124:3"]["draft_translation"]
    assert "lest the righteous stretch out their hands" in by_ref["Psalms 124:3"][
        "draft_translation"
    ]
    assert "Yet the righteous will give thanks" in by_ref["Psalms 139:14"][
        "draft_translation"
    ]
    assert "The lips of the righteous know high things" in by_ref["Proverbs 10:21"][
        "draft_translation"
    ]
    assert "perception of the righteous is a good way" in by_ref["Proverbs 11:9"][
        "draft_translation"
    ]
    assert "In good things of the righteous, a city prospered" in by_ref["Proverbs 11:10"][
        "draft_translation"
    ]
    assert "one helping the righteous will spring up" in by_ref["Proverbs 11:28"][
        "draft_translation"
    ]
    assert "roots of the righteous will not be pulled up" in by_ref["Proverbs 12:3"][
        "draft_translation"
    ]
    assert "A discerning righteous one will be his own friend" in by_ref["Proverbs 12:26"][
        "draft_translation"
    ]
    assert "seven times the righteous will fall and rise" in by_ref["Proverbs 24:16"][
        "draft_translation"
    ]
    assert "the righteous groan" in by_ref["Proverbs 28:28"]["draft_translation"]
    assert "the righteous will multiply" in by_ref["Proverbs 28:28"]["draft_translation"]
    assert "sinful man is a great snare" in by_ref["Proverbs 29:6"]["draft_translation"]
    assert "the righteous will be in joy" in by_ref["Proverbs 29:6"]["draft_translation"]
    assert "the ungodly will despise wisdom and discipline" in by_ref["Proverbs 1:7"][
        "draft_translation"
    ]
    assert "assaults of the ungodly" in by_ref["Proverbs 3:25"]["draft_translation"]
    assert "the ways of the ungodly" in by_ref["Proverbs 4:14"]["draft_translation"]
    assert "rebuking the ungodly man" in by_ref["Proverbs 9:7"]["draft_translation"]
    assert "poverty is ruin of the ungodly" in by_ref["Proverbs 10:15"][
        "draft_translation"
    ]
    assert "fruits of the ungodly produce sins" in by_ref["Proverbs 10:16"][
        "draft_translation"
    ]
    assert "The tongue of the righteous is refined silver" in by_ref["Proverbs 10:20"][
        "draft_translation"
    ]
    assert "the heart of the ungodly will fail" in by_ref["Proverbs 10:20"][
        "draft_translation"
    ]
    assert "years of the ungodly will be shortened" in by_ref["Proverbs 10:27"][
        "draft_translation"
    ]
    assert "destruction of the ungodly comes" in by_ref["Proverbs 11:3"][
        "draft_translation"
    ]
    assert "boast of the ungodly perishes" in by_ref["Proverbs 11:7"][
        "draft_translation"
    ]
    assert "the ungodly one is handed over" in by_ref["Proverbs 11:8"][
        "draft_translation"
    ]
    assert "mouth of the ungodly is a snare" in by_ref["Proverbs 11:9"][
        "draft_translation"
    ]
    assert "by the mouths of the ungodly" in by_ref["Proverbs 11:11"][
        "draft_translation"
    ]
    assert "pursuit of the ungodly is for death" in by_ref["Proverbs 11:19"][
        "draft_translation"
    ]
    assert "inward parts of the ungodly are pitiless" in by_ref["Proverbs 12:10"][
        "draft_translation"
    ]
    assert "Desires of the ungodly are evil" in by_ref["Proverbs 12:12"][
        "draft_translation"
    ]
    assert "roots of the pious are in strongholds" in by_ref["Proverbs 12:12"][
        "draft_translation"
    ]
    assert "Nothing unjust will please the righteous" in by_ref["Proverbs 12:21"][
        "draft_translation"
    ]
    assert "the ungodly will be filled with evils" in by_ref["Proverbs 12:21"][
        "draft_translation"
    ]
    assert "counsels of the ungodly are harsh" in by_ref["Proverbs 12:26"][
        "draft_translation"
    ]
    assert "the way of the ungodly will mislead them" in by_ref["Proverbs 12:26"][
        "draft_translation"
    ]
    assert "the dwelling of the ungodly will not be" in by_ref["Job 8:22"][
        "draft_translation"
    ]
    assert "the righteous are laughed to scorn" in by_ref["Job 9:23"][
        "draft_translation"
    ]
    assert "knows the works of lawless men" in by_ref["Job 11:11"][
        "draft_translation"
    ]
    assert "the eyes of the ungodly will melt" in by_ref["Job 11:20"][
        "draft_translation"
    ]
    assert "For an appointed time was prepared" in by_ref["Job 12:5"][
        "draft_translation"
    ]
    assert "All the life of the ungodly" in by_ref["Job 15:20"]["draft_translation"]
    assert "given to a tyrant" in by_ref["Job 15:20"]["draft_translation"]
    assert "the witness of the ungodly is death" in by_ref["Job 15:34"][
        "draft_translation"
    ]
    assert "hands of an unjust one" in by_ref["Job 16:11"]["draft_translation"]
    assert "their flame will not blaze forth" in by_ref["Job 18:5"][
        "draft_translation"
    ]
    assert "the gladness of the ungodly is a sudden fall" in by_ref["Job 20:5"][
        "draft_translation"
    ]
    assert "the joy of lawless men is destruction" in by_ref["Job 20:5"][
        "draft_translation"
    ]
    assert "the works of ungodly men" in by_ref["Job 21:16"]["draft_translation"]
    assert "the lamp of ungodly men will be quenched" in by_ref["Job 21:17"][
        "draft_translation"
    ]
    assert "the shelter of the tents of ungodly men" in by_ref["Job 21:28"][
        "draft_translation"
    ]
    assert "the counsel of ungodly men is far from him" in by_ref["Job 22:18"][
        "draft_translation"
    ]
    assert "Before the right time they reaped a field" in by_ref["Job 24:6"][
        "draft_translation"
    ]
    assert "worked the vineyards of ungodly men" in by_ref["Job 24:6"][
        "draft_translation"
    ]
    assert "as the overthrow of ungodly men" in by_ref["Job 27:7"][
        "draft_translation"
    ]
    assert "as the destruction of lawless men" in by_ref["Job 27:7"][
        "draft_translation"
    ]
    assert "from the righteous" in by_ref["Job 36:17"]["draft_translation"]
    assert "wrath will be upon the ungodly" in by_ref["Job 36:18"][
        "draft_translation"
    ]
    assert "because of the ungodliness of gifts" in by_ref["Job 36:18"][
        "draft_translation"
    ]
    assert "took the light from ungodly men" in by_ref["Job 38:15"][
        "draft_translation"
    ]
    assert "shattered the arm of proud men" in by_ref["Job 38:15"][
        "draft_translation"
    ]
    assert "the teeth of sinners you shattered" in by_ref["Psalms 3:8"][
        "draft_translation"
    ]
    assert "Let the evil of sinners come to an end" in by_ref["Psalms 7:10"][
        "draft_translation"
    ]
    assert "the portion of their cup" in by_ref["Psalms 10:6"]["draft_translation"]
    assert "Let the foot of pride not come to me" in by_ref["Psalms 35:12"][
        "draft_translation"
    ]
    assert "the hand of sinners not shake me" in by_ref["Psalms 35:12"][
        "draft_translation"
    ]
    assert "the arms of sinners will be broken" in by_ref["Psalms 36:17"][
        "draft_translation"
    ]
    assert "the seed of ungodly men will be utterly destroyed" in by_ref[
        "Psalms 36:28"
    ]["draft_translation"]
    assert "the remnants of ungodly men will be utterly destroyed" in by_ref[
        "Psalms 36:38"
    ]["draft_translation"]
    assert "to a righteous one forever" in by_ref["Psalms 54:23"][
        "draft_translation"
    ]
    assert "from the book of the living" in by_ref["Psalms 68:29"][
        "draft_translation"
    ]
    assert "with the righteous let them not be written" in by_ref["Psalms 68:29"][
        "draft_translation"
    ]
    assert "seeing the peace of sinners" in by_ref["Psalms 72:3"][
        "draft_translation"
    ]
    assert "one day in your courts is better" in by_ref["Psalms 83:11"][
        "draft_translation"
    ]
    assert "see the repayment of sinners" in by_ref["Psalms 90:8"][
        "draft_translation"
    ]
    assert "You who love the Lord" in by_ref["Psalms 96:10"]["draft_translation"]
    assert "guards the souls of his holy ones" in by_ref["Psalms 96:10"][
        "draft_translation"
    ]
    assert "the desire of sinners will perish" in by_ref["Psalms 111:10"][
        "draft_translation"
    ]
    assert "The righteous will wait for me" in by_ref["Psalms 141:8"][
        "draft_translation"
    ]
    assert "but the ungodly will be shamed" in by_ref["Proverbs 13:5"][
        "draft_translation"
    ]
    assert "Desires of the godly sweeten the soul" in by_ref["Proverbs 13:19"][
        "draft_translation"
    ]
    assert "works of the ungodly are far from knowledge" in by_ref[
        "Proverbs 13:19"
    ]["draft_translation"]
    assert "the houses of the righteous are acceptable" in by_ref[
        "Proverbs 14:9"
    ]["draft_translation"]
    assert "the tents of those setting straight will stand" in by_ref[
        "Proverbs 14:11"
    ]["draft_translation"]
    assert "the ungodly will serve at the doors of the righteous" in by_ref[
        "Proverbs 14:19"
    ]["draft_translation"]
    assert "In his evil the ungodly will be driven away" in by_ref[
        "Proverbs 14:32"
    ]["draft_translation"]
    assert "one trusting in his own holiness is righteous" in by_ref[
        "Proverbs 14:32"
    ]["draft_translation"]
    assert "but he loves those pursuing righteousness" in by_ref["Proverbs 15:9"][
        "draft_translation"
    ]
    assert "justifying the unjust and condemning the righteous" in by_ref["Proverbs 17:15"][
        "draft_translation"
    ]
    assert "the lamp of the ungodly is sin" in by_ref["Proverbs 21:4"]["draft_translation"]
    assert "a holy man is unclean among evildoers" in by_ref["Proverbs 21:15"]["draft_translation"]
    assert "a lawless one is one remembering wrongs" in by_ref["Proverbs 21:24"]["draft_translation"]
    assert "A deep pit is the mouth of a lawless man" in by_ref["Proverbs 22:14"]["draft_translation"]
    assert "before a man" in by_ref["Proverbs 22:14"]["draft_translation"]
    assert "from a crooked and evil way" in by_ref["Proverbs 22:14"]["draft_translation"]
    assert "the ungodly will grow weak in evils" in by_ref["Proverbs 24:16"]["draft_translation"]
    assert "the lamp of the ungodly will be quenched" in by_ref["Proverbs 24:20"]["draft_translation"]
    assert "but the glory of the king honors matters" in by_ref["Proverbs 25:2"]["draft_translation"]
    assert by_ref["Proverbs 25:3"]["draft_translation"].startswith("Heaven is high")
    assert "the heart of the king is unsearchable" in by_ref["Proverbs 25:3"]["draft_translation"]
    assert by_ref["Proverbs 25:11"]["draft_translation"].startswith("A golden apple")
    assert "a wise word to a listening ear" in by_ref["Proverbs 25:12"]["draft_translation"]
    assert "a faithful messenger benefits" in by_ref["Proverbs 25:13"]["draft_translation"]
    assert "benefits the souls" in by_ref["Proverbs 25:13"]["draft_translation"]
    assert "so also a man testifying" in by_ref["Proverbs 25:18"]["draft_translation"]
    assert "perish in an evil day" in by_ref["Proverbs 25:19"]["draft_translation"]
    assert "falling upon the body grieves the heart" in by_ref["Proverbs 25:20"]["draft_translation"]
    assert "As a moth in a garment" in by_ref["Proverbs 25:20"]["draft_translation"]
    assert "corner of a roof" in by_ref["Proverbs 25:24"]["draft_translation"]
    assert "with a scolding woman in a common house" in by_ref["Proverbs 25:24"]["draft_translation"]
    assert "cool water is pleasant to a thirsty soul" in by_ref["Proverbs 25:25"]["draft_translation"]
    assert "a good message from a far land" in by_ref["Proverbs 25:25"]["draft_translation"]
    assert "stop up a spring and spoil a water outlet" in by_ref["Proverbs 25:26"]["draft_translation"]
    assert "for a righteous man to fall before an ungodly man" in by_ref["Proverbs 25:26"]["draft_translation"]
    assert by_ref["Proverbs 25:28"]["draft_translation"].startswith("Like a city")
    assert "so a man who does anything without counsel" in by_ref["Proverbs 25:28"]["draft_translation"]
    assert "honor is not for a fool" in by_ref["Proverbs 26:1"]["draft_translation"]
    assert by_ref["Proverbs 26:11"]["draft_translation"].startswith("As a dog")
    assert "so a fool" in by_ref["Proverbs 26:11"]["draft_translation"]
    assert "There is shame that brings sin" in by_ref["Proverbs 26:11"]["draft_translation"]
    assert "I saw a man seeming wise to himself" in by_ref["Proverbs 26:12"]["draft_translation"]
    assert "yet a fool had more hope" in by_ref["Proverbs 26:12"]["draft_translation"]
    assert "The words of whisperers are soft" in by_ref["Proverbs 26:22"]["draft_translation"]
    assert by_ref["Proverbs 26:28"]["draft_translation"].startswith("A lying tongue")
    assert "an unchecked mouth makes disorders" in by_ref["Proverbs 26:28"]["draft_translation"]
    assert "what the next day will bring forth" in by_ref["Proverbs 27:1"]["draft_translation"]
    assert by_ref["Proverbs 27:2"]["draft_translation"].startswith("Let a neighbor")
    assert "a stranger, not your own lips" in by_ref["Proverbs 27:2"]["draft_translation"]
    assert by_ref["Proverbs 27:3"]["draft_translation"].startswith("A heavy stone")
    assert "the anger of a fool is heavier" in by_ref["Proverbs 27:3"]["draft_translation"]
    assert "Wounds of a friend are more trustworthy" in by_ref["Proverbs 27:6"]["draft_translation"]
    assert "kisses of an enemy" in by_ref["Proverbs 27:6"]["draft_translation"]
    assert by_ref["Proverbs 27:7"]["draft_translation"].startswith("A soul")
    assert "to a needy soul" in by_ref["Proverbs 27:7"]["draft_translation"]
    assert "when a bird flies down" in by_ref["Proverbs 27:8"]["draft_translation"]
    assert "so a man enslaves himself" in by_ref["Proverbs 27:8"]["draft_translation"]
    assert "the heart delights" in by_ref["Proverbs 27:9"]["draft_translation"]
    assert "the soul is torn apart" in by_ref["Proverbs 27:9"]["draft_translation"]
    assert "enter the house of your brother" in by_ref["Proverbs 27:10"]["draft_translation"]
    assert "Better a nearby friend" in by_ref["Proverbs 27:10"]["draft_translation"]
    assert by_ref["Proverbs 27:12"]["draft_translation"].startswith("A shrewd man")
    assert "an insolent man passed by" in by_ref["Proverbs 27:13"]["draft_translation"]
    assert "blesses a friend early in the morning with a loud voice" in by_ref["Proverbs 27:14"]["draft_translation"]
    assert "Drops drive a man" in by_ref["Proverbs 27:15"]["draft_translation"]
    assert "on a winter day" in by_ref["Proverbs 27:15"]["draft_translation"]
    assert "a scolding woman" in by_ref["Proverbs 27:15"]["draft_translation"]
    assert by_ref["Proverbs 27:16"]["draft_translation"].startswith("A north wind is a hard wind")
    assert "a man sharpens the face of a companion" in by_ref["Proverbs 27:17"]["draft_translation"]
    assert "One planting a fig tree" in by_ref["Proverbs 27:18"]["draft_translation"]
    assert "so neither are the thoughts of men" in by_ref["Proverbs 27:19"]["draft_translation"]
    assert "the eyes of men are insatiable" in by_ref["Proverbs 27:20"]["draft_translation"]
    assert "fixing an eye is an abomination" in by_ref["Proverbs 27:20"]["draft_translation"]
    assert "undisciplined men are unrestrained" in by_ref["Proverbs 27:20"]["draft_translation"]
    assert "a man is tested through the mouth" in by_ref["Proverbs 27:21"]["draft_translation"]
    assert "The heart of a lawless man" in by_ref["Proverbs 27:21"]["draft_translation"]
    assert "an upright heart seeks knowledge" in by_ref["Proverbs 27:21"]["draft_translation"]
    assert "scourge a fool" in by_ref["Proverbs 27:22"]["draft_translation"]
    assert "Know well the souls of your flock" in by_ref["Proverbs 27:23"]["draft_translation"]
    assert "strength and power are not forever for a man" in by_ref["Proverbs 27:24"]["draft_translation"]
    assert "honor the field" in by_ref["Proverbs 27:26"]["draft_translation"]
    assert "a righteous one trusts like a lion" in by_ref["Proverbs 28:1"]["draft_translation"]
    assert "sins of the ungodly" in by_ref["Proverbs 28:2"]["draft_translation"]
    assert "a shrewd man will quench" in by_ref["Proverbs 28:2"]["draft_translation"]
    assert by_ref["Proverbs 28:3"]["draft_translation"].startswith("A strong man")
    assert "slanders the poor" in by_ref["Proverbs 28:3"]["draft_translation"]
    assert "he is like sweeping and useless rain" in by_ref["Proverbs 28:3"]["draft_translation"]
    assert "Those forsaking the law" in by_ref["Proverbs 28:4"]["draft_translation"]
    assert "those loving the law wrap a wall" in by_ref["Proverbs 28:4"]["draft_translation"]
    assert "mercy to the poor" in by_ref["Proverbs 28:8"]["draft_translation"]
    assert "hearing the law" in by_ref["Proverbs 28:9"]["draft_translation"]
    assert "leading the upright astray in an evil way" in by_ref["Proverbs 28:10"]["draft_translation"]
    assert "the lawless will pass by" in by_ref["Proverbs 28:10"]["draft_translation"]
    assert by_ref["Proverbs 28:11"]["draft_translation"].startswith("A rich man is wise")
    assert "a poor understanding man" in by_ref["Proverbs 28:11"]["draft_translation"]
    assert "Through help of the righteous" in by_ref["Proverbs 28:12"]["draft_translation"]
    assert "places of the ungodly" in by_ref["Proverbs 28:12"]["draft_translation"]
    assert "one hardening the heart" in by_ref["Proverbs 28:14"]["draft_translation"]
    assert by_ref["Proverbs 28:15"]["draft_translation"].startswith("A hungry lion")
    assert "a thirsty wolf is a tyrant" in by_ref["Proverbs 28:15"]["draft_translation"]
    assert "over a needy people" in by_ref["Proverbs 28:15"]["draft_translation"]
    assert by_ref["Proverbs 28:16"]["draft_translation"].startswith("A king")
    assert "a great slanderer" in by_ref["Proverbs 28:16"]["draft_translation"]
    assert "live a long time" in by_ref["Proverbs 28:16"]["draft_translation"]
    assert "guaranteeing a man guilty of murder" in by_ref["Proverbs 28:17"]["draft_translation"]
    assert "will be a fugitive" in by_ref["Proverbs 28:17"]["draft_translation"]
    assert "a lawless nation" in by_ref["Proverbs 28:17"]["draft_translation"]
    assert by_ref["Proverbs 28:20"]["draft_translation"].startswith("A faithful man")
    assert "an evil man will not go unpunished" in by_ref["Proverbs 28:20"]["draft_translation"]
    assert "faces of the righteous" in by_ref["Proverbs 28:21"]["draft_translation"]
    assert "such a man will be sold for a morsel of bread" in by_ref["Proverbs 28:21"]["draft_translation"]
    assert by_ref["Proverbs 28:22"]["draft_translation"].startswith("An envious man")
    assert "a merciful man will master him" in by_ref["Proverbs 28:22"]["draft_translation"]
    assert "ways of a man" in by_ref["Proverbs 28:23"]["draft_translation"]
    assert "with the tongue" in by_ref["Proverbs 28:23"]["draft_translation"]
    assert "is a partner of an ungodly man" in by_ref["Proverbs 28:24"]["draft_translation"]
    assert by_ref["Proverbs 28:25"]["draft_translation"].startswith("A faithless man")
    assert "in a bold heart" in by_ref["Proverbs 28:26"]["draft_translation"]
    assert "that man is a fool" in by_ref["Proverbs 28:26"]["draft_translation"]
    assert "giving to the poor" in by_ref["Proverbs 28:27"]["draft_translation"]
    assert "places of the ungodly" in by_ref["Proverbs 28:28"]["draft_translation"]
    assert by_ref["Proverbs 29:1"]["draft_translation"].startswith("A man who rebukes")
    assert "than a stiff-necked man" in by_ref["Proverbs 29:1"]["draft_translation"]
    assert "When the righteous are praised" in by_ref["Proverbs 29:2"]["draft_translation"]
    assert "when the ungodly rule" in by_ref["Proverbs 29:2"]["draft_translation"]
    assert by_ref["Proverbs 29:3"]["draft_translation"].startswith("When a man loves wisdom")
    assert "a lawless man digs it down" in by_ref["Proverbs 29:4"]["draft_translation"]
    assert "preparing a net before his own friend" in by_ref["Proverbs 29:5"]["draft_translation"]
    assert by_ref["Proverbs 29:6"]["draft_translation"].startswith("For a sinful man")
    assert "judge for the poor" in by_ref["Proverbs 29:7"]["draft_translation"]
    assert "the ungodly one does not understand" in by_ref["Proverbs 29:7"]["draft_translation"]
    assert "but a base man" in by_ref["Proverbs 29:9"]["draft_translation"]
    assert "hate a holy man" in by_ref["Proverbs 29:10"]["draft_translation"]
    assert "the upright will seek" in by_ref["Proverbs 29:10"]["draft_translation"]
    assert by_ref["Proverbs 29:13"]["draft_translation"].startswith("When a lender")
    assert "judges the poor" in by_ref["Proverbs 29:14"]["draft_translation"]
    assert by_ref["Proverbs 29:16"]["draft_translation"].startswith("When the ungodly are many")
    assert "the righteous are put in fear" in by_ref["Proverbs 29:16"]["draft_translation"]
    assert "faces of the leaders" in by_ref["Proverbs 29:26"]["draft_translation"]
    assert "abomination to the righteous" in by_ref["Proverbs 29:27"]["draft_translation"]
    assert "Thus says the man" in by_ref["Proverbs 30:1"]["draft_translation"]
    assert "knowledge of the holy ones" in by_ref["Proverbs 30:3"]["draft_translation"]
    assert "winds in a bosom" in by_ref["Proverbs 30:4"]["draft_translation"]
    assert "water in a garment" in by_ref["Proverbs 30:4"]["draft_translation"]
    assert "all the ends of the earth" in by_ref["Proverbs 30:4"]["draft_translation"]
    assert "What is his name" in by_ref["Proverbs 30:4"]["draft_translation"]
    assert "what is the name of his children" in by_ref["Proverbs 30:4"]["draft_translation"]
    assert "words of God are refined" in by_ref["Proverbs 30:5"]["draft_translation"]
    assert "become a liar" in by_ref["Proverbs 30:6"]["draft_translation"]
    assert "Make a vain word and a lie" in by_ref["Proverbs 30:8"]["draft_translation"]
    assert "the necessary and self-sufficient things" in by_ref["Proverbs 30:8"]["draft_translation"]
    assert "being filled I become a liar" in by_ref["Proverbs 30:9"]["draft_translation"]
    assert "hand a servant over into the hands of his master" in by_ref["Proverbs 30:10"]["draft_translation"]
    assert by_ref["Proverbs 30:11"]["draft_translation"].startswith("An evil offspring")
    assert "its father" in by_ref["Proverbs 30:11"]["draft_translation"]
    assert "its mother" in by_ref["Proverbs 30:11"]["draft_translation"]
    assert by_ref["Proverbs 30:12"]["draft_translation"].startswith("An evil offspring")
    assert by_ref["Proverbs 30:13"]["draft_translation"].startswith("An evil offspring")
    assert by_ref["Proverbs 30:14"]["draft_translation"].startswith("An evil offspring")
    assert "consume the humble from the earth" in by_ref["Proverbs 30:14"]["draft_translation"]
    assert "the poor among men" in by_ref["Proverbs 30:14"]["draft_translation"]
    assert by_ref["Proverbs 30:15"]["draft_translation"].startswith("The leech")
    assert "the fourth was not satisfied" in by_ref["Proverbs 30:15"]["draft_translation"]
    assert "the desire of a woman" in by_ref["Proverbs 30:16"]["draft_translation"]
    assert by_ref["Proverbs 30:17"]["draft_translation"].startswith("An eye mocking a father")
    assert "the old age of a mother" in by_ref["Proverbs 30:17"]["draft_translation"]
    assert "and a fourth I do not know" in by_ref["Proverbs 30:18"]["draft_translation"]
    assert "the tracks of an eagle flying" in by_ref["Proverbs 30:19"]["draft_translation"]
    assert "the ways of a serpent on a rock" in by_ref["Proverbs 30:19"]["draft_translation"]
    assert "the paths of a ship voyaging at sea" in by_ref["Proverbs 30:19"]["draft_translation"]
    assert by_ref["Proverbs 30:20"]["draft_translation"].startswith("Such is the way of an adulterous woman")
    assert "the earth is shaken" in by_ref["Proverbs 30:21"]["draft_translation"]
    assert "a fourth it cannot bear" in by_ref["Proverbs 30:21"]["draft_translation"]
    assert "if a servant reigns" in by_ref["Proverbs 30:22"]["draft_translation"]
    assert "a fool is filled" in by_ref["Proverbs 30:22"]["draft_translation"]
    assert "a maidservant throws out her mistress" in by_ref["Proverbs 30:23"]["draft_translation"]
    assert "a hated woman happens upon a good husband" in by_ref["Proverbs 30:23"]["draft_translation"]
    assert by_ref["Proverbs 30:24"]["draft_translation"].startswith("Four things on the earth are very little")
    assert "wiser than the wise" in by_ref["Proverbs 30:24"]["draft_translation"]
    assert by_ref["Proverbs 30:25"]["draft_translation"].startswith("The ants")
    assert by_ref["Proverbs 30:26"]["draft_translation"].startswith("and the rock-badgers")
    assert "a nation not strong" in by_ref["Proverbs 30:26"]["draft_translation"]
    assert "in the rocks" in by_ref["Proverbs 30:26"]["draft_translation"]
    assert by_ref["Proverbs 30:27"]["draft_translation"].startswith("The locust")
    assert by_ref["Proverbs 30:28"]["draft_translation"].startswith("and a lizard")
    assert "with its hands" in by_ref["Proverbs 30:28"]["draft_translation"]
    assert "in the fortresses of the king" in by_ref["Proverbs 30:28"]["draft_translation"]
    assert "and a fourth walks well" in by_ref["Proverbs 30:29"]["draft_translation"]
    assert by_ref["Proverbs 30:30"]["draft_translation"].startswith("A lion's cub is strongest")
    assert "shrink from a beast" in by_ref["Proverbs 30:30"]["draft_translation"]
    assert by_ref["Proverbs 30:31"]["draft_translation"].startswith("and a rooster")
    assert "a goat leading a flock" in by_ref["Proverbs 30:31"]["draft_translation"]
    assert "among a nation" in by_ref["Proverbs 30:31"]["draft_translation"]
    assert by_ref["Proverbs 30:33"]["draft_translation"].startswith("When milk is pressed")
    assert "an oracle of a king" in by_ref["Proverbs 31:1"]["draft_translation"]
    assert "the rulers drink wine" in by_ref["Proverbs 31:4"]["draft_translation"]
    assert "judge the weak rightly" in by_ref["Proverbs 31:5"]["draft_translation"]
    assert "forget their poverty" in by_ref["Proverbs 31:7"]["draft_translation"]
    assert "remember their troubles" in by_ref["Proverbs 31:7"]["draft_translation"]
    assert "for the word of God" in by_ref["Proverbs 31:8"]["draft_translation"]
    assert "for the poor and weak" in by_ref["Proverbs 31:9"]["draft_translation"]
    assert by_ref["Proverbs 31:10"]["draft_translation"].startswith("Who will find a brave wife")
    assert "Such a woman is more precious" in by_ref["Proverbs 31:10"]["draft_translation"]
    assert "such a woman will not lack" in by_ref["Proverbs 31:11"]["draft_translation"]
    assert "all her life" in by_ref["Proverbs 31:12"]["draft_translation"]
    assert by_ref["Proverbs 31:13"]["draft_translation"].startswith("She works wool and flax")
    assert "like a merchant ship" in by_ref["Proverbs 31:14"]["draft_translation"]
    assert "rises by night" in by_ref["Proverbs 31:15"]["draft_translation"]
    assert "tasks to the maidservants" in by_ref["Proverbs 31:15"]["draft_translation"]
    assert by_ref["Proverbs 31:16"]["draft_translation"].startswith("Having considered a field")
    assert "planted a possession" in by_ref["Proverbs 31:16"]["draft_translation"]
    assert "the whole night" in by_ref["Proverbs 31:18"]["draft_translation"]
    assert "to the useful things" in by_ref["Proverbs 31:19"]["draft_translation"]
    assert "to the spindle" in by_ref["Proverbs 31:19"]["draft_translation"]
    assert "hands to the poor" in by_ref["Proverbs 31:20"]["draft_translation"]
    assert "her wrist to the needy" in by_ref["Proverbs 31:20"]["draft_translation"]
    assert "all who are from her are clothed" in by_ref["Proverbs 31:21"]["draft_translation"]
    assert "conspicuous in the gates" in by_ref["Proverbs 31:23"]["draft_translation"]
    assert "belts to the Canaanites" in by_ref["Proverbs 31:24"]["draft_translation"]
    assert "in the latter days" in by_ref["Proverbs 31:26"]["draft_translation"]
    assert "vain is beauty of a woman" in by_ref["Proverbs 31:30"]["draft_translation"]
    assert "for a prudent woman is blessed" in by_ref["Proverbs 31:30"]["draft_translation"]
    assert by_ref["Ecclesiastes 1:2"]["draft_translation"].endswith("all things are vanity.")
    assert by_ref["Ecclesiastes 1:3"]["draft_translation"].startswith("What surplus is there for a man")
    assert by_ref["Ecclesiastes 1:4"]["draft_translation"].startswith("A generation goes")
    assert "the earth stands into the age" in by_ref["Ecclesiastes 1:4"]["draft_translation"]
    assert by_ref["Ecclesiastes 1:5"]["draft_translation"].startswith("And the sun rises")
    assert "toward the south" in by_ref["Ecclesiastes 1:6"]["draft_translation"]
    assert "toward the north" in by_ref["Ecclesiastes 1:6"]["draft_translation"]
    assert "into the sea" in by_ref["Ecclesiastes 1:7"]["draft_translation"]
    assert "to the place where the torrents go" in by_ref["Ecclesiastes 1:7"]["draft_translation"]
    assert "a man will not be able to speak" in by_ref["Ecclesiastes 1:8"]["draft_translation"]
    assert "the eye will not be filled" in by_ref["Ecclesiastes 1:8"]["draft_translation"]
    assert "the ear filled from hearing" in by_ref["Ecclesiastes 1:8"]["draft_translation"]
    assert "this is what will happen" in by_ref["Ecclesiastes 1:9"]["draft_translation"]
    assert "this is what will be done" in by_ref["Ecclesiastes 1:9"]["draft_translation"]
    assert "in the ages that came before us" in by_ref["Ecclesiastes 1:10"]["draft_translation"]
    assert "memory for the first things" in by_ref["Ecclesiastes 1:11"]["draft_translation"]
    assert "with the things yet to be at the end" in by_ref["Ecclesiastes 1:11"]["draft_translation"]
    assert "because God gave evil distraction" in by_ref["Ecclesiastes 1:13"]["draft_translation"]
    assert "look, all is vanity" in by_ref["Ecclesiastes 1:14"]["draft_translation"]
    assert "in much wisdom is much knowledge" in by_ref["Ecclesiastes 1:18"]["draft_translation"]
    assert "the one adding knowledge" in by_ref["Ecclesiastes 1:18"]["draft_translation"]
    assert by_ref["Ecclesiastes 2:1"]["draft_translation"].endswith("this too is vanity.")
    assert "what good there is for the sons of man" in by_ref["Ecclesiastes 2:3"]["draft_translation"]
    assert "for the number of days" in by_ref["Ecclesiastes 2:3"]["draft_translation"]
    assert "a forest sprouting trees" in by_ref["Ecclesiastes 2:6"]["draft_translation"]
    assert "beyond all who were before me" in by_ref["Ecclesiastes 2:7"]["draft_translation"]
    assert "treasures of kings and of the provinces" in by_ref["Ecclesiastes 2:8"]["draft_translation"]
    assert "delights of the sons of man" in by_ref["Ecclesiastes 2:8"]["draft_translation"]
    assert "a cupbearer and cupbearers" in by_ref["Ecclesiastes 2:8"]["draft_translation"]
    assert "all that my eyes asked" in by_ref["Ecclesiastes 2:10"]["draft_translation"]
    assert "look, all is vanity" in by_ref["Ecclesiastes 2:11"]["draft_translation"]
    assert "as the surplus of light over darkness" in by_ref["Ecclesiastes 2:13"]["draft_translation"]
    assert "wise man are in his head" in by_ref["Ecclesiastes 2:14"]["draft_translation"]
    assert "the fool walks in darkness" in by_ref["Ecclesiastes 2:14"]["draft_translation"]
    assert "As the meeting of the fool" in by_ref["Ecclesiastes 2:15"]["draft_translation"]
    assert "this too is vanity" in by_ref["Ecclesiastes 2:15"]["draft_translation"]
    assert "a fool speaks from surplus" in by_ref["Ecclesiastes 2:15"]["draft_translation"]
    assert "memory of the wise man with the fool" in by_ref["Ecclesiastes 2:16"]["draft_translation"]
    assert "the days that are coming" in by_ref["Ecclesiastes 2:16"]["draft_translation"]
    assert "all is vanity and choice of spirit" in by_ref["Ecclesiastes 2:17"]["draft_translation"]
    assert "the man coming after me" in by_ref["Ecclesiastes 2:18"]["draft_translation"]
    assert "wise or a fool" in by_ref["Ecclesiastes 2:19"]["draft_translation"]
    assert by_ref["Ecclesiastes 2:19"]["draft_translation"].endswith("this too is vanity.")
    assert "all the toil in which I toiled" in by_ref["Ecclesiastes 2:20"]["draft_translation"]
    assert "there is a man whose toil" in by_ref["Ecclesiastes 2:21"]["draft_translation"]
    assert "to a man who did not toil" in by_ref["Ecclesiastes 2:21"]["draft_translation"]
    assert "this too is vanity and a great evil" in by_ref["Ecclesiastes 2:21"]["draft_translation"]
    assert "what comes to a man" in by_ref["Ecclesiastes 2:22"]["draft_translation"]
    assert "in the choice of his heart" in by_ref["Ecclesiastes 2:22"]["draft_translation"]
    assert "his distraction is wrath" in by_ref["Ecclesiastes 2:23"]["draft_translation"]
    assert "even in the night" in by_ref["Ecclesiastes 2:23"]["draft_translation"]
    assert by_ref["Haggai 1:1"]["draft_translation"].startswith("In the second year of Darius the king")
    assert "Haggai the prophet" in by_ref["Haggai 1:1"]["draft_translation"]
    assert "the high priest" in by_ref["Haggai 1:1"]["draft_translation"]
    assert by_ref["Zechariah 1:1"]["draft_translation"].startswith("In the eighth month of the second year of Darius")
    assert "between you and the wife of your youth" in by_ref["Malachi 2:14"]["draft_translation"]
    assert "and the wife of your covenant" in by_ref["Malachi 2:14"]["draft_translation"]
    assert "from the Syriac book" in by_ref["Job 42:17"]["draft_translation"]
    assert "Taking an Arabian wife" in by_ref["Job 42:17"]["draft_translation"]
    assert "he fathered a son whose name was Ennon" in by_ref["Job 42:17"]["draft_translation"]
    assert "one of the sons of Esau" in by_ref["Job 42:17"]["draft_translation"]
    assert "from his mother Bozrah" in by_ref["Job 42:17"]["draft_translation"]
    assert "Eliphaz king of the sons of Esau from the Temanites" in by_ref["Job 42:17"]["draft_translation"]
    assert "Bildad tyrant of the Sauchites" in by_ref["Job 42:17"]["draft_translation"]
    assert "Zophar king of the Naamathites" in by_ref["Job 42:17"]["draft_translation"]
    assert "see the limbs of the men" in by_ref["Isaiah 66:24"]["draft_translation"]
    assert "will be a spectacle to all flesh" in by_ref["Isaiah 66:24"]["draft_translation"]
    assert by_ref["Jeremiah 52:34"]["draft_translation"].startswith("And the ration for him")
    assert by_ref["Amos 1:1"]["draft_translation"].startswith("The words of Amos")
    assert by_ref["Obadiah 1:1"]["draft_translation"].startswith("The vision of Obadiah")
    assert "message to the nations" in by_ref["Obadiah 1:1"]["draft_translation"]
    assert "inherit the mount of Esau" in by_ref["Obadiah 1:19"]["draft_translation"]
    assert "inherit the mount of Ephraim" in by_ref["Obadiah 1:19"]["draft_translation"]
    assert "the plain of Samaria" in by_ref["Obadiah 1:19"]["draft_translation"]
    assert "from Mount Zion to avenge the mount of Esau" in by_ref["Obadiah 1:21"]["draft_translation"]
    assert "and the kingdom will belong to the Lord" in by_ref["Obadiah 1:21"]["draft_translation"]
    assert "Nineveh, the great city" in by_ref["Jonah 1:2"]["draft_translation"]
    assert "because the cry of its evil" in by_ref["Jonah 1:2"]["draft_translation"]
    assert "according to the former proclamation" in by_ref["Jonah 3:2"]["draft_translation"]
    assert "Nineveh, the great city" in by_ref["Jonah 4:11"]["draft_translation"]
    assert by_ref["Nahum 1:1"]["draft_translation"].endswith("Book of the vision of Nahum the Elkoshite.")
    assert "the sons of Ammon as Gomorrah" in by_ref["Zephaniah 2:9"]["draft_translation"]
    assert "like a heap of the threshing-floor" in by_ref["Zephaniah 2:9"]["draft_translation"]
    assert "the remnant of my people" in by_ref["Zephaniah 2:9"]["draft_translation"]
    assert "for a boast among all the peoples of the earth" in by_ref["Zephaniah 3:20"]["draft_translation"]
    assert "there will no longer be a Canaanite" in by_ref["Zechariah 14:21"]["draft_translation"]
    assert "whatever a foreigner calls upon you for" in by_ref["2 Chronicles 6:33"]["draft_translation"]
    assert "so that all the peoples of the earth may know" in by_ref["2 Chronicles 6:33"]["draft_translation"]
    assert "fear you as your people Israel do, and know" in by_ref["2 Chronicles 6:33"]["draft_translation"]
    assert by_ref["Jeremiah 7:11"]["draft_translation"].startswith("Has my house")
    assert "become a den of robbers" in by_ref["Jeremiah 7:11"]["draft_translation"]
    assert "on Mount Zion and in Jerusalem" in by_ref["Joel 3:5"]["draft_translation"]
    assert by_ref["Obadiah 1:17"]["draft_translation"].startswith("But on Mount Zion")
    assert "they called on the Lord, and he heard them" in by_ref["Psalms 98:6"]["draft_translation"]
    assert "He mounts me upon heights, to conquer in his song" in by_ref["Habakkuk 3:19"]["draft_translation"]
    assert "from the line of the sons of Israel" in by_ref["Daniel 1:6"]["draft_translation"]
    assert "hoped on the Lord" in by_ref["Psalms 113:17"]["draft_translation"]
    assert "hoped on the Lord" in by_ref["Psalms 113:18"]["draft_translation"]
    assert "he is their helper and defender" in by_ref["Psalms 113:17"]["draft_translation"]
    assert "he is their helper and defender" in by_ref["Psalms 113:18"]["draft_translation"]
    assert "he is their helper and defender" in by_ref["Psalms 113:19"]["draft_translation"]
    assert "I am your servant, I am your servant" in by_ref["Psalms 115:7"]["draft_translation"]
    assert "the whole day it is my meditation" in by_ref["Psalms 118:97"]["draft_translation"]
    assert by_ref["Psalms 118:125"]["draft_translation"].startswith("I am your servant")
    assert "But I, your servant, did not see" in by_ref["1 Samuel 25:25"]["draft_translation"]
    assert "because I am your servant" in by_ref["Psalms 142:12"]["draft_translation"]
    assert "because you are my firm place and refuge" in by_ref["Psalms 70:3"]["draft_translation"]
    assert by_ref["Psalms 70:5"]["draft_translation"].startswith("Because you are my endurance")
    assert "you are my protector" in by_ref["Psalms 70:6"]["draft_translation"]
    assert by_ref["Psalms 78:13"]["draft_translation"].startswith("But we are your people")
    assert by_ref["Psalms 124:1"]["draft_translation"].startswith("Song of ascents. Those trusting in the Lord are like Mount Zion")
    assert by_ref["Psalms 127:1"]["draft_translation"].startswith("Song of ascents. Blessed are all fearing the Lord")
    assert by_ref["Psalms 129:1"]["draft_translation"].startswith("Song of ascents. Out of the depths")
    assert "Lord, my heart is not exalted" in by_ref["Psalms 130:1"]["draft_translation"]
    assert "what is good or what is pleasant" in by_ref["Psalms 132:1"]["draft_translation"]
    assert by_ref["Isaiah 2:2"]["draft_translation"].startswith("Because in the last days the mountain of the Lord")
    assert "upon the whole earth" in by_ref["Isaiah 28:22"]["draft_translation"]
    assert "what the kings of the Assyrians did to the whole earth" in by_ref["Isaiah 37:11"]["draft_translation"]
    assert "Will the plowman plow the whole earth all day" in by_ref["Isaiah 45:9"]["draft_translation"]
    assert "all the beasts of the whole earth" in by_ref["Ezekiel 32:4"]["draft_translation"]
    assert by_ref["Ezekiel 35:14"]["draft_translation"].startswith("Thus says the Lord: In the joy of the whole earth")
    assert "the house of Jacob is in a snare" in by_ref["Isaiah 8:14"]["draft_translation"]
    assert "the house of Joseph a flame, and the house of Esau for stubble" in by_ref[
        "Obadiah 1:18"
    ]["draft_translation"]
    assert by_ref["Micah 2:7"]["draft_translation"].startswith(
        "You who say, Has the house of Jacob provoked the spirit of the Lord"
    )
    assert "like a lion ready for the hunt" in by_ref["Psalms 16:12"]["draft_translation"]
    assert "like a lion among beasts of the forest" in by_ref["Micah 5:7"]["draft_translation"]
    assert "like a lion-cub among flocks of sheep" in by_ref["Micah 5:7"]["draft_translation"]
    assert "like a lion for slaughter" in by_ref["Job 10:16"]["draft_translation"]
    assert "like a lion, while there is none" in by_ref["Psalms 7:3"]["draft_translation"]
    assert "like a lion in its den" in by_ref["Psalms 9:30"]["draft_translation"]
    assert "like a lion seizing and roaring" in by_ref["Psalms 21:14"]["draft_translation"]
    assert "as a lion's whelp" in by_ref["Isaiah 5:29"]["draft_translation"]
    assert "as a beast and cast out" in by_ref["Isaiah 5:29"]["draft_translation"]
    assert "as a lion, thus he crushed my bones" in by_ref["Isaiah 38:13"]["draft_translation"]
    assert "like a lion in the forest" in by_ref["Jeremiah 12:8"]["draft_translation"]
    assert by_ref["Jeremiah 27:44"]["draft_translation"].startswith("Behold, like a lion")
    assert by_ref["Jeremiah 30:13"]["draft_translation"].startswith("Behold, like a lion")
    assert "his lodging like a lion" in by_ref["Jeremiah 32:38"]["draft_translation"]
    assert "from the face of the great sword" in by_ref["Jeremiah 32:38"]["draft_translation"]
    assert "became like a sparrow solitary" in by_ref["Psalms 101:8"]["draft_translation"]
    assert "like a gazelle from snares and like a bird from trap" in by_ref["Proverbs 6:5"]["draft_translation"]
    assert "hunger like a dog" in by_ref["Psalms 58:7"]["draft_translation"]
    assert "like a calf not taught" in by_ref["Jeremiah 38:18"]["draft_translation"]
    assert "Like a bear and like a dove" in by_ref["Isaiah 59:11"]["draft_translation"]
    assert "like a horse through a wilderness" in by_ref["Isaiah 63:13"]["draft_translation"]
    assert "as a deer struck in liver" in by_ref["Proverbs 7:23"]["draft_translation"]
    assert "soar high like an eagle" in by_ref["Obadiah 1:4"]["draft_translation"]
    assert "fly as an eagle eager to eat" in by_ref["Habakkuk 1:8"]["draft_translation"]
    assert by_ref["Jeremiah 30:16"]["draft_translation"].startswith("Behold, like an eagle")
    assert "like an eagle against the house of the Lord" in by_ref["Hosea 8:1"]["draft_translation"]
    assert "as a young man lives with a virgin" in by_ref["Isaiah 62:5"]["draft_translation"]
    assert "as a bridegroom rejoices over a bride" in by_ref["Isaiah 62:5"]["draft_translation"]
    assert "anoint him as a ruler over my people Israel" in by_ref["1 Samuel 9:16"]["draft_translation"]
    assert "faithful as a prophet to the Lord" in by_ref["1 Samuel 3:20"]["draft_translation"]
    assert "be for us as a leader" in by_ref["Judges 11:6"]["draft_translation"]
    assert "wander like a drunkard" in by_ref["Job 12:25"]["draft_translation"]
    assert "like a tree planted" in by_ref["Psalms 1:3"]["draft_translation"]
    assert "like a moth, and like a spider" in by_ref["Job 27:18"]["draft_translation"]
    assert "like a giant to run his course" in by_ref["Psalms 18:6"]["draft_translation"]
    assert "like a wineskin" in by_ref["Psalms 32:7"]["draft_translation"]
    assert "like a wheel" in by_ref["Psalms 82:14"]["draft_translation"]
    assert "comes like a storm" in by_ref["Proverbs 1:27"]["draft_translation"]
    assert "like a river of peace" in by_ref["Isaiah 66:12"]["draft_translation"]
    assert "like a torrent flooding the glory" in by_ref["Isaiah 66:12"]["draft_translation"]
    assert "like a skin-bag, like a garment eaten by moth" in by_ref["Job 13:28"]["draft_translation"]
    assert "like a garment, and like a cloak" in by_ref["Psalms 101:27"]["draft_translation"]
    assert "my salvation like a cloud" in by_ref["Job 30:15"]["draft_translation"]
    assert "like a cloud he will come up" in by_ref["Jeremiah 4:13"]["draft_translation"]
    assert "become like a river and your righteousness like a wave of the sea" in by_ref["Isaiah 48:18"]["draft_translation"]
    assert "rise like a river" in by_ref["Jeremiah 26:7"]["draft_translation"]
    assert "as a woman in labor" in by_ref["Isaiah 26:17"]["draft_translation"]
    assert "like a dead man" in by_ref["Psalms 30:13"]["draft_translation"]
    assert "like a ruined vessel" in by_ref["Psalms 30:13"]["draft_translation"]
    assert "as a house of sacrifice" in by_ref["2 Chronicles 7:12"]["draft_translation"]
    assert "pangs as of a woman giving birth" in by_ref["Psalms 47:7"]["draft_translation"]
    assert "as of a woman in labor" in by_ref["Jeremiah 4:31"]["draft_translation"]
    assert "as a fleeing gazelle" in by_ref["Isaiah 13:14"]["draft_translation"]
    assert "as a wandering sheep" in by_ref["Isaiah 13:14"]["draft_translation"]
    assert "as with a weapon of favor" in by_ref["Psalms 5:13"]["draft_translation"]
    assert "as a flame burns mountains" in by_ref["Psalms 82:15"]["draft_translation"]
    assert "their faces will change as a flame" in by_ref["Isaiah 13:8"]["draft_translation"]
    assert by_ref["1 Chronicles 19:13"]["draft_translation"].startswith("Act like a man")
    assert "Be strong and act like a man and do" in by_ref["1 Chronicles 28:20"]["draft_translation"]
    assert "like a woman giving birth" in by_ref["Micah 4:10"]["draft_translation"]
    assert "one like a son of man" in by_ref["Daniel 7:13"]["draft_translation"]
    assert "Gird your loins like a man" in by_ref["Job 38:3"]["draft_translation"]
    assert "like a sleeping man or like a man unable to save" in by_ref["Jeremiah 14:9"]["draft_translation"]
    assert "like a broken man and like a man overcome by wine" in by_ref["Jeremiah 23:9"]["draft_translation"]
    assert "like a desert donkey" in by_ref["Job 11:12"]["draft_translation"]
    assert "like a desert pelican" in by_ref["Psalms 101:7"]["draft_translation"]
    assert "Zion became like a desert" in by_ref["Isaiah 64:9"]["draft_translation"]
    assert "like a morning star" in by_ref["Job 11:17"]["draft_translation"]
    assert "like a morning cloud" in by_ref["Hosea 6:4"]["draft_translation"]
    assert "like a fruitful olive tree" in by_ref["Psalms 51:10"]["draft_translation"]
    assert "like a fruitful tree" in by_ref["Jeremiah 38:12"]["draft_translation"]
    assert "Your wife like a vine" in by_ref["Psalms 127:3"]["draft_translation"]
    assert "like a vine, like a blossom" in by_ref["Ezekiel 19:10"]["draft_translation"]
    assert "like a bad traveler" in by_ref["Proverbs 6:11"]["draft_translation"]
    assert "like a good runner" in by_ref["Proverbs 6:11"]["draft_translation"]
    assert "like a fountain" in by_ref["Proverbs 6:11"]["draft_translation"]
    assert "like the sound of much water" in by_ref["Ezekiel 1:24"]["draft_translation"]
    assert "like the voice of God Almighty" in by_ref["Ezekiel 10:5"]["draft_translation"]
    assert "like an oven" in by_ref["Lamentations 5:10"]["draft_translation"]
    assert "like a bronze pot" in by_ref["Job 41:23"]["draft_translation"]
    assert "like a perfume-vessel" in by_ref["Job 41:23"]["draft_translation"]
    assert "like a shadow" in by_ref["1 Chronicles 29:15"]["draft_translation"]
    assert by_ref["Job 14:2"]["draft_translation"].startswith("Like a flower")
    assert "tongues like a sword" in by_ref["Psalms 63:4"]["draft_translation"]
    assert "like a stone cube" in by_ref["Job 38:38"]["draft_translation"]
    assert "spear like a beam of weavers" in by_ref["1 Chronicles 11:23"]["draft_translation"]
    assert "like a heap of threshing floor" in by_ref["Job 5:26"]["draft_translation"]
    assert "like a ripe threshing-floor" in by_ref["Jeremiah 28:33"]["draft_translation"]
    assert "like a hired man" in by_ref["Job 7:2"]["draft_translation"]
    assert "like a furnace of fire" in by_ref["Psalms 20:10"]["draft_translation"]
    assert "like a deaf man" in by_ref["Psalms 37:14"]["draft_translation"]
    assert "like a deaf asp" in by_ref["Psalms 57:5"]["draft_translation"]
    assert "led them like a flock" in by_ref["Psalms 77:52"]["draft_translation"]
    assert "like a palm tree" in by_ref["Psalms 91:13"]["draft_translation"]
    assert "like a cedar in Lebanon" in by_ref["Psalms 91:13"]["draft_translation"]
    assert "like a herd of shorn sheep" in by_ref["Song of Solomon 4:2"]["draft_translation"]
    assert "is like a piece of pomegranate" in by_ref["Song of Solomon 4:3"]["draft_translation"]
    assert "Set me as a seal" in by_ref["Song of Solomon 8:6"]["draft_translation"]
    assert "as a tent in a vineyard" in by_ref["Isaiah 1:8"]["draft_translation"]
    assert "as a city under siege" in by_ref["Isaiah 1:8"]["draft_translation"]
    assert "strong like an oak" in by_ref["Amos 2:9"]["draft_translation"]
    assert "as a flying bird" in by_ref["Isaiah 16:2"]["draft_translation"]
    assert "a chick taken away" in by_ref["Isaiah 16:2"]["draft_translation"]
    assert "as an enemy" in by_ref["Isaiah 63:10"]["draft_translation"]
    assert "plowed like a field" in by_ref["Micah 3:12"]["draft_translation"]
    assert "as a shepherd snatches" in by_ref["Amos 3:12"]["draft_translation"]
    assert "like a flame of fire" in by_ref["Daniel 7:9"]["draft_translation"]
    assert "as the sound of thorns under the cauldron" in by_ref["Ecclesiastes 7:6"]["draft_translation"]
    assert "as a watchman" in by_ref["Ezekiel 3:17"]["draft_translation"]
    assert "as an iron wall" in by_ref["Ezekiel 4:3"]["draft_translation"]
    assert "like the dead of long ago" in by_ref["Lamentations 3:6"]["draft_translation"]
    assert "like a passing shadow" in by_ref["Psalms 143:4"]["draft_translation"]
    assert "like a passing flower" in by_ref["Zephaniah 2:2"]["draft_translation"]
    assert "like the roaring of a lion" in by_ref["Proverbs 19:12"]["draft_translation"]
    assert "like the force of God" in by_ref["1 Chronicles 12:23"]["draft_translation"]
    assert "like the breaking of waters" in by_ref["1 Chronicles 14:11"]["draft_translation"]
    assert "like the name of great ones" in by_ref["1 Chronicles 17:8"]["draft_translation"]
    assert "like the rim of a cup" in by_ref["2 Chronicles 4:5"]["draft_translation"]
    assert "like the funeral of his fathers" in by_ref["2 Chronicles 21:19"]["draft_translation"]
    assert "as a leper" in by_ref["2 Chronicles 26:21"]["draft_translation"]
    assert "as a stumbling-block" in by_ref["2 Chronicles 28:23"]["draft_translation"]
    assert "as a laughingstock" in by_ref["2 Chronicles 30:10"]["draft_translation"]
    assert "like the work of sapphire brick" in by_ref["Exodus 24:10"]["draft_translation"]
    assert "I was the eye of the blind and foot of the lame" in by_ref["Job 29:15"]["draft_translation"]
    assert "as the eyes of servants" in by_ref["Psalms 122:2"]["draft_translation"]
    assert "as the eyes of a maidservant" in by_ref["Psalms 122:2"]["draft_translation"]
    assert "like the likeness of the temple" in by_ref["Psalms 143:12"]["draft_translation"]
    assert "like the appearance of electrum" in by_ref["Ezekiel 1:4"]["draft_translation"]
    assert "like the sight of lamps" in by_ref["Ezekiel 1:13"]["draft_translation"]
    assert "Like the appearance of a sapphire stone" in by_ref["Ezekiel 1:26"]["draft_translation"]
    assert "as the appearance of a man" in by_ref["Ezekiel 1:26"]["draft_translation"]
    assert "Like the appearance of a bow when it is in a cloud" in by_ref["Ezekiel 1:28"]["draft_translation"]
    assert "This was the appearance of the likeness of the glory" in by_ref["Ezekiel 1:28"]["draft_translation"]
    assert "heard a voice speaking" in by_ref["Ezekiel 1:28"]["draft_translation"]
    assert "I heard the voice of your words" in by_ref["Job 33:8"]["draft_translation"]
    assert "the Lord heard the voice of my weeping" in by_ref["Psalms 6:9"]["draft_translation"]
    assert "he heard the voice of my petition" in by_ref["Psalms 27:6"]["draft_translation"]
    assert "you heard the voice of my petition" in by_ref["Psalms 30:23"]["draft_translation"]
    assert "I heard the voice of the Lord saying" in by_ref["Isaiah 6:8"]["draft_translation"]
    assert "I heard the voice of your prayer" in by_ref["Isaiah 38:5"]["draft_translation"]
    assert "heard the voice of a trumpet" in by_ref["Jeremiah 4:19"]["draft_translation"]
    assert "I heard the voice of your blasphemies" in by_ref["Ezekiel 35:12"]["draft_translation"]
    assert "I heard the voice of a man" in by_ref["Daniel 8:16"]["draft_translation"]
    assert "hear the sound of shaking" in by_ref["1 Chronicles 14:15"]["draft_translation"]
    assert "heard the sound of the people" in by_ref["2 Chronicles 23:12"]["draft_translation"]
    assert "hear the sound of the horn" in by_ref["Nehemiah 4:14"]["draft_translation"]
    assert "endure the sound of your speech" in by_ref["Job 6:26"]["draft_translation"]
    assert "the sound of festival-keepers" in by_ref["Psalms 41:5"]["draft_translation"]
    assert "the sound of its waves" in by_ref["Psalms 64:8"]["draft_translation"]
    assert "set the sound of waters" in by_ref["Jeremiah 28:16"]["draft_translation"]
    assert "With the sound of its waves" in by_ref["Jeremiah 28:42"]["draft_translation"]
    assert "the sound of his wheels" in by_ref["Jeremiah 29:3"]["draft_translation"]
    assert "by the sound of his roar" in by_ref["Ezekiel 19:7"]["draft_translation"]
    assert "because of the sound of great words" in by_ref["Daniel 7:11"]["draft_translation"]
    assert "Remove from me the sound of your songs" in by_ref["Amos 5:23"]["draft_translation"]
    assert "to the sound of instruments" in by_ref["Amos 6:5"]["draft_translation"]
    assert "hates the sound of security" in by_ref["Proverbs 11:15"]["draft_translation"]
    assert "came to the king in Hebron" in by_ref["1 Chronicles 11:3"]["draft_translation"]
    assert "before the king and rulers" in by_ref["1 Chronicles 24:6"]["draft_translation"]
    assert "with the king in Jerusalem" in by_ref["2 Chronicles 1:14"]["draft_translation"]
    assert "gave to the king one hundred twenty talents" in by_ref["2 Chronicles 9:9"][
        "draft_translation"
    ]
    assert "and the king put them in the house" in by_ref["2 Chronicles 9:16"][
        "draft_translation"
    ]
    assert "ships went for the king to Tarshish" in by_ref["2 Chronicles 9:21"][
        "draft_translation"
    ]
    assert "ships came from Tarshish to the king full of gold" in by_ref[
        "2 Chronicles 9:21"
    ]["draft_translation"]
    assert "rulers of Israel and the king were put to shame" in by_ref["2 Chronicles 12:6"][
        "draft_translation"
    ]
    assert "He blessed God and the king" in by_ref["1 Kings 20:10"]["draft_translation"]
    assert "between himself and people and the king" in by_ref["2 Chronicles 23:16"][
        "draft_translation"
    ]
    assert "because the king desired your beauty" in by_ref["Psalms 44:12"]["draft_translation"]
    assert "My son, fear God and the king" in by_ref["Proverbs 24:21"]["draft_translation"]
    assert "and a king speaking publicly among a nation" in by_ref["Proverbs 30:31"][
        "draft_translation"
    ]
    assert "and the king asked him secretly" in by_ref["Jeremiah 44:17"]["draft_translation"]
    assert "and the king honored them" in by_ref["Daniel 1:20"]["draft_translation"]
    assert "and the king sealed it" in by_ref["Daniel 6:18"]["draft_translation"]
    assert "that the king might not pull him up" in by_ref["Daniel 6:18"]["draft_translation"]
    assert "that the king did not listen to them" in by_ref["2 Chronicles 10:16"][
        "draft_translation"
    ]
    assert "people answered the king saying" in by_ref["2 Chronicles 10:16"][
        "draft_translation"
    ]
    assert "because the mouth of a sinner and the mouth of a deceitful one" in by_ref[
        "Psalms 108:2"
    ]["draft_translation"]
    assert by_ref["Isaiah 11:3"]["draft_translation"].startswith("The spirit of fear of God")
    assert "a rod will come out from the root of Jesse" in by_ref["Isaiah 11:1"][
        "draft_translation"
    ]
    assert "a wolf will graze together with a lamb" in by_ref["Isaiah 11:6"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 19:3"]["draft_translation"].startswith(
        "And the spirit of the Egyptians"
    )
    assert by_ref["Isaiah 61:1"]["draft_translation"].startswith("The Spirit of the Lord is on me")
    assert by_ref["Jeremiah 4:12"]["draft_translation"].startswith("A spirit of fullness")
    assert by_ref["Ezekiel 11:5"]["draft_translation"].startswith("And the Spirit of the Lord fell")
    assert "but the word of our God remains" in by_ref["Isaiah 40:8"]["draft_translation"]
    assert by_ref["Proverbs 25:2"]["draft_translation"].startswith(
        "The glory of God hides a word"
    )
    assert by_ref["Isaiah 60:13"]["draft_translation"].startswith("The glory of Lebanon")
    assert by_ref["Isaiah 64:9"]["draft_translation"].startswith("Your holy city became")
    assert by_ref["Jeremiah 52:5"]["draft_translation"].startswith(
        "And the city came into siege"
    )
    assert by_ref["Jeremiah 52:7"]["draft_translation"].startswith(
        "And the city was broken through"
    )
    assert by_ref["Isaiah 24:4"]["draft_translation"].startswith("The land mourned")
    assert by_ref["Isaiah 24:5"]["draft_translation"].startswith(
        "And the land acted lawlessly"
    )
    assert by_ref["Ezekiel 32:6"]["draft_translation"].startswith(
        "And the land will be watered"
    )
    assert "and the land that was desolated will be worked" in by_ref["Ezekiel 36:34"][
        "draft_translation"
    ]
    assert by_ref["Zechariah 12:12"]["draft_translation"].startswith("And the land will mourn")
    assert by_ref["Isaiah 3:5"]["draft_translation"].startswith("The people will fall")
    assert by_ref["Isaiah 9:1"]["draft_translation"].startswith(
        "The people walking in darkness"
    )
    assert "see a great light" in by_ref["Isaiah 9:1"]["draft_translation"]
    assert by_ref["Jonah 3:8"]["draft_translation"].startswith(
        "The people and the cattle clothed themselves"
    )
    assert by_ref["Psalms 18:8"]["draft_translation"].startswith(
        "The law of the Lord is blameless"
    )
    assert by_ref["Psalms 33:16"]["draft_translation"].startswith(
        "The eyes of the Lord are upon"
    )
    assert by_ref["Psalms 118:160"]["draft_translation"].startswith(
        "The beginning of your words is truth"
    )
    assert by_ref["Proverbs 1:7"]["draft_translation"].startswith(
        "The beginning of wisdom is fear of God"
    )
    assert by_ref["Proverbs 22:12"]["draft_translation"].startswith(
        "The eyes of the Lord preserve"
    )
    assert by_ref["Hosea 1:2"]["draft_translation"].startswith(
        "The beginning of the word of the Lord"
    )
    assert by_ref["Isaiah 1:8"]["draft_translation"].startswith("The daughter of Zion")
    assert by_ref["Malachi 2:6"]["draft_translation"].startswith("The law of truth")
    assert by_ref["Psalms 2:2"]["draft_translation"].startswith("The kings of the earth")
    assert by_ref["Psalms 9:7"]["draft_translation"].startswith("The swords of the enemy")
    assert by_ref["Proverbs 11:23"]["draft_translation"].startswith(
        "The desire of the righteous"
    )
    assert by_ref["Proverbs 10:16"]["draft_translation"].startswith(
        "The works of the righteous"
    )
    assert by_ref["Proverbs 12:6"]["draft_translation"].startswith(
        "The words of the ungodly"
    )
    assert by_ref["Proverbs 13:14"]["draft_translation"].startswith(
        "The law of the wise is a fountain of life"
    )
    assert "the heart of a fool is at his left" in by_ref["Ecclesiastes 10:2"][
        "draft_translation"
    ]
    assert "the spirit of the ruler" in by_ref["Ecclesiastes 10:4"][
        "draft_translation"
    ]
    assert by_ref["Ecclesiastes 10:8"]["draft_translation"].startswith(
        "The one digging a pit"
    )
    assert by_ref["Ecclesiastes 10:12"]["draft_translation"].startswith(
        "The words of the mouth of the wise"
    )
    assert by_ref["Isaiah 26:7"]["draft_translation"].startswith("The way of the godly")
    assert by_ref["Job 29:13"]["draft_translation"].startswith(
        "The blessing of one perishing came upon me"
    )
    assert by_ref["Proverbs 3:33"]["draft_translation"].startswith(
        "The curse of God in the houses of the ungodly"
    )
    assert by_ref["Proverbs 10:7"]["draft_translation"].startswith(
        "The memory of the righteous"
    )
    assert by_ref["Proverbs 10:11"]["draft_translation"].startswith(
        "A fountain of life is in the hand of the righteous"
    )
    assert by_ref["Proverbs 14:27"]["draft_translation"].startswith(
        "The command of the Lord is a fountain of life"
    )
    assert by_ref["Proverbs 15:33"]["draft_translation"].startswith(
        "The fear of God is discipline and wisdom"
    )
    assert by_ref["Proverbs 15:2"]["draft_translation"].startswith(
        "The tongue of the wise knows good things"
    )
    assert by_ref["Lamentations 4:10"]["draft_translation"].startswith(
        "The hands of compassionate women"
    )
    assert by_ref["Zechariah 4:9"]["draft_translation"].startswith(
        "The hands of Zerubbabel founded this house"
    )
    assert by_ref["Proverbs 14:9"]["draft_translation"].startswith(
        "The houses of the lawless will owe cleansing"
    )
    assert "sweep away the righteous with the ungodly" in by_ref["Genesis 18:23"]["draft_translation"]
    assert "hope of the ungodly will perish" in by_ref["Job 8:13"]["draft_translation"]
    assert "hands of the ungodly" in by_ref["Job 9:24"]["draft_translation"]
    assert "gladness of the ungodly" in by_ref["Job 20:5"]["draft_translation"]
    assert "Many are the afflictions of the righteous ones" in by_ref["Psalms 33:20"][
        "draft_translation"
    ]
    assert "horns of the righteous one will be exalted" in by_ref["Psalms 74:11"]["draft_translation"]
    assert "lot of the righteous" in by_ref["Psalms 124:3"]["draft_translation"]
    assert "cry of the poor upon him" in by_ref["Job 34:28"]["draft_translation"]
    assert "petition of a poor man" in by_ref["Psalms 21:25"]["draft_translation"]
    assert by_ref["Psalms 52:2"]["draft_translation"].startswith(
        "The fool said in his heart"
    )
    assert by_ref["Psalms 57:11"]["draft_translation"].startswith(
        "The righteous one will rejoice"
    )
    assert by_ref["Proverbs 10:1"]["draft_translation"].startswith(
        "A wise son gladdens a father"
    )
    assert by_ref["Proverbs 14:16"]["draft_translation"].startswith(
        "A wise man, fearing"
    )
    assert by_ref["Proverbs 18:14"]["draft_translation"].startswith(
        "A wise servant calms the anger of a man"
    )
    assert by_ref["Proverbs 21:18"]["draft_translation"].startswith(
        "A lawless man is purging-scrap for the righteous"
    )
    assert by_ref["Ecclesiastes 4:5"]["draft_translation"].startswith(
        "A fool folded his hands"
    )
    assert "all the slanders happening under the sun" in by_ref["Ecclesiastes 4:1"]["draft_translation"]
    assert "this too is vanity" in by_ref["Ecclesiastes 4:4"]["draft_translation"]
    assert "There is one and there is no second" in by_ref["Ecclesiastes 4:8"]["draft_translation"]
    assert by_ref["Ecclesiastes 4:13"]["draft_translation"].startswith(
        "Better a poor and wise child"
    )
    assert "judgments of the Lord are true" in by_ref["Psalms 18:10"]["draft_translation"]
    assert by_ref["Psalms 32:4"]["draft_translation"].startswith(
        "Because the word of the Lord is straight"
    )
    assert "salvation of man is vain" in by_ref["Psalms 59:13"]["draft_translation"]
    assert by_ref["Psalms 115:6"]["draft_translation"].startswith(
        "Precious before the Lord is the death"
    )
    assert by_ref["Proverbs 4:18"]["draft_translation"].startswith(
        "The ways of the righteous are like shining light"
    )
    assert by_ref["Proverbs 10:7"]["draft_translation"].startswith(
        "The memory of the righteous is with praises"
    )
    assert "the desire of the righteous is acceptable" in by_ref["Proverbs 10:24"]["draft_translation"]
    assert by_ref["Proverbs 12:6"]["draft_translation"].startswith(
        "The words of the ungodly are deceitful"
    )
    assert by_ref["Proverbs 15:29"]["draft_translation"].startswith(
        "God is far from the ungodly"
    )
    assert by_ref["Proverbs 7:27"]["draft_translation"].startswith(
        "The ways of Hades are her house"
    )
    assert by_ref["Proverbs 15:19"]["draft_translation"].startswith(
        "The ways of the idle are paved"
    )
    assert by_ref["Proverbs 9:10"]["draft_translation"].startswith(
        "The beginning of wisdom is the fear of the Lord, and the counsel"
    )
    assert by_ref["Proverbs 15:3"]["draft_translation"].startswith(
        "In every place the eyes of the Lord"
    )
    assert by_ref["Proverbs 25:19"]["draft_translation"].startswith(
        "The way of evil and the foot of a lawless man"
    )
    assert "the way of the godly is prepared" in by_ref["Isaiah 26:7"]["draft_translation"]
    assert by_ref["Isaiah 57:1"]["draft_translation"].startswith(
        "See how a righteous man perished"
    )
    assert by_ref["Job 20:23"]["draft_translation"].startswith(
        "The wrath of anger will be sent upon him"
    )
    assert by_ref["Job 21:33"]["draft_translation"].startswith(
        "The pebbles of a torrent were sweet to him"
    )
    assert by_ref["Job 26:11"]["draft_translation"].startswith(
        "The pillars of heaven were spread out"
    )
    assert by_ref["Job 36:27"]["draft_translation"].startswith(
        "The drops of rain are counted for him"
    )
    assert by_ref["Proverbs 21:10"]["draft_translation"].startswith(
        "The soul of the ungodly will not be pitied"
    )
    assert by_ref["Ecclesiastes 10:15"]["draft_translation"].startswith(
        "The toil of fools will weary them"
    )
    assert "whose king is young" in by_ref["Ecclesiastes 10:16"]["draft_translation"]
    assert "do not curse a king" in by_ref["Ecclesiastes 10:20"][
        "draft_translation"
    ]
    assert "The dwellers of the rock will rejoice" in by_ref["Isaiah 42:11"][
        "draft_translation"
    ]
    assert "The face of a prostitute became yours" in by_ref["Jeremiah 3:3"]["draft_translation"]
    assert by_ref["Hosea 9:7"]["draft_translation"].startswith(
        "The days of vengeance have come; the days of your repayment have come"
    )
    assert by_ref["Nahum 2:7"]["draft_translation"].startswith(
        "The gates of the rivers were opened"
    )
    assert by_ref["2 Chronicles 3:11"]["draft_translation"].startswith(
        "And the wings of cheroubim were"
    )
    assert by_ref["2 Chronicles 3:13"]["draft_translation"].startswith(
        "And the wings of cheroubim spread out"
    )
    assert by_ref["2 Chronicles 30:17"]["draft_translation"].startswith(
        "Because many of the assembly had not sanctified themselves"
    )
    assert by_ref["Job 31:11"]["draft_translation"].startswith(
        "For the wrath of anger is unrestrainable"
    )
    assert "to defile the wife of a man" in by_ref["Job 31:11"]["draft_translation"]
    assert by_ref["Psalms 17:16"]["draft_translation"].startswith(
        "And the fountains of waters were seen"
    )
    assert "the foundations of the inhabited world were uncovered" in by_ref["Psalms 17:16"]["draft_translation"]
    assert by_ref["Psalms 35:13"]["draft_translation"].startswith(
        "There the workers of lawlessness fell"
    )
    assert by_ref["Psalms 36:23"]["draft_translation"].startswith(
        "From the Lord the steps of a man are directed straight"
    )
    assert by_ref["Proverbs 20:24"]["draft_translation"].startswith(
        "From the Lord the steps of a man are made straight"
    )
    assert by_ref["Proverbs 2:22"]["draft_translation"].startswith(
        "The ways of the ungodly will perish"
    )
    assert by_ref["Proverbs 15:9"]["draft_translation"].startswith(
        "The ways of the ungodly are an abomination"
    )
    assert "the wealth of the ungodly is stored up for the righteous" in by_ref["Proverbs 13:22"]["draft_translation"]
    assert by_ref["Isaiah 29:5"]["draft_translation"].startswith(
        "And the wealth of the ungodly will be"
    )
    assert by_ref["Isaiah 24:8"]["draft_translation"].startswith(
        "The gladness of drums ceased"
    )
    assert "the wealth of the ungodly ceased" in by_ref["Isaiah 24:8"]["draft_translation"]
    assert by_ref["Isaiah 30:26"]["draft_translation"].startswith(
        "And the light of the moon will be as the light of the sun"
    )
    assert by_ref["Isaiah 32:17"]["draft_translation"].startswith(
        "And the works of righteousness will be peace"
    )
    assert "The seed of the disobedient became for destruction" in by_ref["Isaiah 33:2"]["draft_translation"]
    assert by_ref["Isaiah 35:5"]["draft_translation"].startswith(
        "Then the eyes of the blind will be opened"
    )
    assert by_ref["Jeremiah 10:3"]["draft_translation"].startswith(
        "Because the customs of nations are vain"
    )
    assert by_ref["Ezekiel 29:11"]["draft_translation"].startswith(
        "The foot of a man will not pass through it"
    )
    assert by_ref["Amos 7:9"]["draft_translation"].startswith(
        "And the altars of laughter will be destroyed"
    )
    assert by_ref["Zephaniah 2:7"]["draft_translation"].startswith(
        "And the measuring-line of the sea will belong"
    )
    assert by_ref["Zechariah 9:12"]["draft_translation"].startswith(
        "You will sit in a stronghold"
    )
    assert by_ref["Psalms 7:8"]["draft_translation"].startswith(
        "And a gathering of peoples will encircle you"
    )
    assert by_ref["Proverbs 10:8"]["draft_translation"].startswith(
        "The wise in heart will receive commands"
    )
    assert "but a wise one listens to counsels" in by_ref["Proverbs 12:15"]["draft_translation"]
    assert "the Lord of all hearts knows" in by_ref["Proverbs 24:12"]["draft_translation"]
    assert by_ref["Isaiah 20:6"]["draft_translation"].startswith(
        "And the dwellers in this island will say"
    )
    assert by_ref["Isaiah 59:19"]["draft_translation"].startswith(
        "And those from the west will fear"
    )
    assert by_ref["Jeremiah 3:21"]["draft_translation"].startswith(
        "A voice was heard from lips"
    )
    assert by_ref["Jeremiah 32:37"]["draft_translation"].startswith(
        "And the remnants of peace will cease"
    )
    assert by_ref["Ezekiel 36:15"]["draft_translation"].startswith(
        "And the reproach of nations will no longer be heard"
    )
    assert by_ref["Obadiah 1:3"]["draft_translation"].startswith(
        "The arrogance of your heart lifted you up"
    )
    assert by_ref["Micah 3:7"]["draft_translation"].startswith(
        "And the seers of dreams will be put to shame"
    )
    assert "The strength of the enemies was crushed" in by_ref["Nehemiah 4:4"]["draft_translation"]
    assert by_ref["Psalms 64:13"]["draft_translation"].startswith(
        "The beauties of the wilderness will grow fat"
    )
    assert by_ref["Ezekiel 5:12"]["draft_translation"].startswith(
        "A quarter of you will be consumed"
    )
    assert by_ref["Proverbs 3:35"]["draft_translation"].startswith(
        "The wise will inherit glory"
    )
    assert by_ref["Proverbs 10:14"]["draft_translation"].startswith(
        "The wise hide perception"
    )
    assert by_ref["Judges 5:29"]["draft_translation"].startswith(
        "The wise women of her princesses answered"
    )
    assert by_ref["Jeremiah 8:9"]["draft_translation"].startswith(
        "The wise men were ashamed"
    )
    assert by_ref["Psalms 75:11"]["draft_translation"].startswith(
        "Because the thought of man will confess"
    )
    assert "the Lord of hosts will be a crown of hope" in by_ref["Isaiah 28:5"]["draft_translation"]
    assert by_ref["Job 8:13"]["draft_translation"].startswith(
        "So then will be the end of all who forget the Lord"
    )
    assert "The good ones will inhabit the earth" in by_ref["Proverbs 2:21"]["draft_translation"]
    assert "it will be a camp of sirens" in by_ref["Isaiah 34:13"]["draft_translation"]
    assert "there will be a spring of water" in by_ref["Isaiah 35:7"]["draft_translation"]
    assert by_ref["Isaiah 62:3"]["draft_translation"].startswith(
        "You will be a crown of beauty"
    )
    assert by_ref["Zephaniah 2:6"]["draft_translation"].startswith(
        "And Crete will be a pasture of flocks"
    )
    assert by_ref["Zechariah 14:19"]["draft_translation"].startswith(
        "This will be the sin of Egypt"
    )
    assert by_ref["1 Chronicles 22:1"]["draft_translation"].startswith(
        "And David said, This is the house of the Lord God"
    )
    assert by_ref["Job 18:21"]["draft_translation"].endswith(
        "this is the place of those not knowing the Lord."
    )
    assert by_ref["Job 20:29"]["draft_translation"].startswith(
        "This is the portion of an ungodly man"
    )
    assert "what is the place of darkness" in by_ref["Job 38:19"]["draft_translation"]
    assert by_ref["Ecclesiastes 3:2"]["draft_translation"].startswith(
        "A time to bear and a time to die"
    )
    assert "What surplus is there to the doer" in by_ref["Ecclesiastes 3:9"]["draft_translation"]
    assert "the work that God made" in by_ref["Ecclesiastes 3:11"]["draft_translation"]
    assert "it is a gift of God" in by_ref["Ecclesiastes 3:13"]["draft_translation"]
    assert "there is a season for every matter" in by_ref["Ecclesiastes 3:17"]["draft_translation"]
    assert "this is his portion" in by_ref["Ecclesiastes 3:22"]["draft_translation"]
    assert "bring out a word before the face of God" in by_ref["Ecclesiastes 5:1"]["draft_translation"]
    assert by_ref["Ecclesiastes 5:2"]["draft_translation"].startswith("Because a dream comes")
    assert "the works of your hands" in by_ref["Ecclesiastes 5:5"]["draft_translation"]
    assert "This too is vanity" in by_ref["Ecclesiastes 5:9"]["draft_translation"]
    assert "this is his portion" in by_ref["Ecclesiastes 5:17"]["draft_translation"]
    assert by_ref["Ecclesiastes 5:18"]["draft_translation"].endswith("this is a gift of God.")
    assert by_ref["Ecclesiastes 6:1"]["draft_translation"].startswith("There is an evil")
    assert "the stillborn is better" in by_ref["Ecclesiastes 6:3"]["draft_translation"]
    assert "All the toil of man is for his mouth" in by_ref["Ecclesiastes 6:7"]["draft_translation"]
    assert "what surplus is there to man" in by_ref["Ecclesiastes 6:11"]["draft_translation"]
    assert by_ref["Jeremiah 31:16"]["draft_translation"].startswith("Near is the day of Moab")
    assert by_ref["Zephaniah 1:15"]["draft_translation"].startswith("That day is a day of wrath")
    assert "he is a messenger of the Lord Almighty" in by_ref["Malachi 2:7"]["draft_translation"]
    assert "Hadarezer was a man of war" in by_ref["1 Chronicles 18:10"]["draft_translation"]
    assert "there was an oversized man" in by_ref["1 Chronicles 20:6"]["draft_translation"]
    assert "he was a descendant of giants" in by_ref["1 Chronicles 20:6"]["draft_translation"]
    assert "there was a prophet of the Lord there" in by_ref["2 Chronicles 28:9"]["draft_translation"]
    assert by_ref["Job 12:4"]["draft_translation"].startswith(
        "For a righteous and blameless man became an object of mockery"
    )
    assert by_ref["Psalms 117:22"]["draft_translation"].startswith(
        "The stone which builders rejected"
    )
    assert "became a torment of their injustices" in by_ref["Ezekiel 7:19"]["draft_translation"]
    assert by_ref["Zechariah 14:15"]["draft_translation"].startswith(
        "And this will be the downfall of the horses"
    )
    assert "which is a city of Scythians" in by_ref["Judges 1:27"]["draft_translation"]
    assert "She is the mother of Onam" in by_ref["1 Chronicles 2:26"]["draft_translation"]
    assert "in which is the covenant of the Lord" in by_ref["2 Chronicles 6:11"]["draft_translation"]
    assert "It is the king of Israel" in by_ref["2 Chronicles 18:31"]["draft_translation"]
    assert "He is a son of Jehoshaphat" in by_ref["2 Chronicles 22:9"]["draft_translation"]
    assert "this is a copy of the decree" in by_ref["Ezra 7:11"]["draft_translation"]
    assert "in his hand is the soul of every living thing" in by_ref["Job 12:10"]["draft_translation"]
    assert by_ref["Job 21:28"]["draft_translation"].startswith("For you will say, Where is the house")
    assert by_ref["Job 38:28"]["draft_translation"].startswith("Who is the father of rain")
    assert by_ref["Job 40:9"]["draft_translation"].startswith("Or is your arm against the Lord")
    assert "it is the king of all things in waters" in by_ref["Job 41:26"]["draft_translation"]
    assert "where is the wrath of the one afflicting you" in by_ref["Isaiah 51:13"]["draft_translation"]
    assert "Where is the multitude of your mercy" in by_ref["Isaiah 63:15"]["draft_translation"]
    assert "is the portion of Jacob" in by_ref["Jeremiah 10:16"]["draft_translation"]
    assert "it is a land of carved images" in by_ref["Jeremiah 27:38"]["draft_translation"]
    assert "there is a day of calling of defenders" in by_ref["Jeremiah 38:6"]["draft_translation"]
    assert by_ref["Ezekiel 43:12"]["draft_translation"].startswith("And show the plan of the house")
    assert by_ref["Ezekiel 43:13"]["draft_translation"].endswith("This is the height of the altar.")
    assert by_ref["Daniel 5:26"]["draft_translation"].startswith(
        "This is the interpretation of the writing"
    )
    assert "is the king of Medes and Persians" in by_ref["Daniel 8:20"]["draft_translation"]
    assert "is the king of Greeks" in by_ref["Daniel 8:21"]["draft_translation"]
    assert "is the first king" in by_ref["Daniel 8:21"]["draft_translation"]
    assert "When then is the completion of these wonders" in by_ref["Daniel 12:6"]["draft_translation"]
    assert "what is the solution of this word" in by_ref["Daniel 12:8"]["draft_translation"]
    assert "it is the sanctuary of the king and the house of the kingdom" in by_ref["Amos 7:13"]["draft_translation"]
    assert "What is the impiety of Jacob" in by_ref["Micah 1:5"]["draft_translation"]
    assert "what is the sin of the house of Judah" in by_ref["Micah 1:5"]["draft_translation"]
    assert by_ref["Nahum 2:12"]["draft_translation"].startswith("Where is the dwelling of lions")
    assert "He was a priest of God Most High" in by_ref["Genesis 14:18"]["draft_translation"]
    assert "Timnah was a concubine of Eliphaz" in by_ref["Genesis 36:12"]["draft_translation"]
    assert by_ref["2 Samuel 24:15"]["draft_translation"].startswith(
        "And it was the days of wheat harvest"
    )
    assert "he was the chief of a band" in by_ref["1 Kings 11:14"]["draft_translation"]
    assert by_ref["1 Chronicles 5:6"]["draft_translation"].startswith(
        "his son Beerah, whom Tilgathpilneser king of Assyria deported. He was the ruler"
    )
    assert by_ref["1 Chronicles 9:21"]["draft_translation"].startswith(
        "Zechariah son of Meshelemiah was the gatekeeper"
    )
    assert "this was the number of mighty men of David" in by_ref["1 Chronicles 11:11"]["draft_translation"]
    assert "Asaph from the beginning was the chief of the singers" in by_ref["Nehemiah 12:46"]["draft_translation"]
    assert "this was the lawlessness of Sodom your sister" in by_ref["Ezekiel 16:49"]["draft_translation"]
    assert "They became like grass of the field" in by_ref["2 Kings 19:26"]["draft_translation"]
    assert by_ref["Job 40:19"]["draft_translation"].startswith("This is the beginning")
    assert "is the completion of release-hands" in by_ref["Daniel 12:7"]["draft_translation"]
    assert "She is the leader of sin" in by_ref["Micah 1:13"]["draft_translation"]
    assert by_ref["Genesis 42:6"]["draft_translation"].startswith("And Joseph was the ruler")
    assert by_ref["Proverbs 9:1"]["draft_translation"].startswith(
        "Wisdom built a house for herself"
    )
    assert by_ref["Ecclesiastes 7:1"]["draft_translation"].startswith("A good name is")
    assert "this is the end of every man" in by_ref["Ecclesiastes 7:2"]["draft_translation"]
    assert by_ref["Ecclesiastes 7:11"]["draft_translation"].startswith("Wisdom is good")
    assert by_ref["Ecclesiastes 9:18"]["draft_translation"].startswith("Wisdom is good")
    assert by_ref["Proverbs 18:21"]["draft_translation"].startswith(
        "Death and life are in the hand of the tongue"
    )
    assert by_ref["Proverbs 19:3"]["draft_translation"].startswith(
        "The folly of a man ruins"
    )
    assert by_ref["Proverbs 20:3"]["draft_translation"].startswith("It is glory for a man")
    assert by_ref["Proverbs 22:15"]["draft_translation"].startswith("Folly is fastened")
    assert "the rod and discipline are far from him" in by_ref["Proverbs 22:15"]["draft_translation"]
    assert by_ref["Proverbs 2:21"]["draft_translation"].startswith("The good ones will inhabit")
    assert "Ioudias was the chief of the Hebronites" in by_ref["1 Chronicles 26:31"]["draft_translation"]
    assert "In the fortieth year" in by_ref["1 Chronicles 26:31"]["draft_translation"]
    assert "and the Holy One" in by_ref["Habakkuk 3:3"]["draft_translation"]
    assert "covered the heavens" in by_ref["Habakkuk 3:3"]["draft_translation"]
    assert "O Holy One of Israel" in by_ref["Psalms 70:22"]["draft_translation"]
    assert "provoked the Holy One of Israel" in by_ref["Psalms 77:41"]["draft_translation"]
    assert "to the Holy One of Israel" in by_ref["Psalms 88:19"]["draft_translation"]
    assert "You abandoned the Lord and provoked the Holy One of Israel" in by_ref[
        "Isaiah 1:4"
    ]["draft_translation"]
    assert "said the Holy One" in by_ref["Isaiah 40:25"]["draft_translation"]
    assert "God, the Holy One of Israel" in by_ref["Isaiah 43:3"]["draft_translation"]
    assert "your Holy One" in by_ref["Isaiah 43:15"]["draft_translation"]
    assert "my Holy One" in by_ref["Habakkuk 1:12"]["draft_translation"]
    assert "those seeing the sun" in by_ref["Ecclesiastes 7:11"]["draft_translation"]
    assert by_ref["Jeremiah 12:1"]["draft_translation"].startswith("You are righteous")
    assert "way of the ungodly" in by_ref["Jeremiah 12:1"]["draft_translation"]
    assert by_ref["Lamentations 1:18"]["draft_translation"].startswith("The Lord is righteous")
    assert by_ref["Isaiah 1:28"]["draft_translation"].startswith("The lawless and sinners")
    assert "dwellers on the earth" in by_ref["Isaiah 24:17"]["draft_translation"]
    assert by_ref["Proverbs 13:9"]["draft_translation"].startswith("There is light")
    assert by_ref["Proverbs 24:21"]["draft_translation"].startswith("My son, fear God")
    assert "all kings of the earth were seeking the face of Solomon" in by_ref[
        "2 Chronicles 9:23"
    ]["draft_translation"]
    assert by_ref["Job 9:24"]["draft_translation"].startswith("For the earth is given")
    assert "the earth is a house for every mortal" in by_ref["Job 30:23"]["draft_translation"]
    assert "the heavens were made firm" in by_ref["Psalms 32:6"]["draft_translation"]
    assert "kings of the earth" in by_ref["Psalms 75:13"]["draft_translation"]
    assert "foundations of the earth" in by_ref["Isaiah 24:18"]["draft_translation"]
    assert "upon the host of heaven and upon the kings of the earth" in by_ref[
        "Isaiah 24:21"
    ]["draft_translation"]
    assert "if the foundation of the earth" in by_ref["Jeremiah 38:35"][
        "draft_translation"
    ]
    assert "all the nations of the earth" in by_ref["Zechariah 12:3"]["draft_translation"]
    assert by_ref["Psalms 10:4"]["draft_translation"].startswith(
        "The Lord is in his holy temple; the Lord's throne is in heaven."
    )
    assert "The Lord in his anger will trouble them" in by_ref["Psalms 20:10"][
        "draft_translation"
    ]
    assert by_ref["Psalms 95:9"]["draft_translation"].startswith(
        "Worship the Lord in his holy court"
    )
    assert by_ref["Psalms 144:13"]["draft_translation"].endswith(
        "Faithful is the Lord in his words and holy in all his works."
    )
    assert "the earth shook" in by_ref["Judges 5:4"]["draft_translation"]
    assert "upon the earth?" in by_ref["2 Chronicles 6:18"]["draft_translation"]
    assert "dust of the earth" in by_ref["2 Chronicles 1:9"]["draft_translation"]
    assert "dust of the earth" in by_ref["Job 14:19"]["draft_translation"]
    assert "but the earth he gave" in by_ref["Psalms 113:24"]["draft_translation"]
    assert "crushing of the daughter of my kin" in by_ref["Isaiah 22:4"][
        "draft_translation"
    ]
    assert "from the heads of father-houses" in by_ref["Ezra 2:68"][
        "draft_translation"
    ]
    assert "forecourt of the gate of the house" in by_ref["Ezekiel 8:14"][
        "draft_translation"
    ]
    assert "porch of the gate" in by_ref["Ezekiel 40:9"]["draft_translation"]
    assert "throne of the kingdom of the Lord" in by_ref["1 Chronicles 28:5"][
        "draft_translation"
    ]
    assert "spirit of the courts of the house" in by_ref["1 Chronicles 28:12"][
        "draft_translation"
    ]
    assert "made the house of the holy of holies" in by_ref["2 Chronicles 3:8"][
        "draft_translation"
    ]
    assert "for the judgment of the Lord" in by_ref["2 Chronicles 19:8"][
        "draft_translation"
    ]
    assert "not in the tombs of kings" in by_ref["2 Chronicles 21:20"][
        "draft_translation"
    ]
    assert "according to the covenant of the law of the Lord" in by_ref[
        "2 Chronicles 25:4"
    ]["draft_translation"]
    assert "according to the abominations of nations" in by_ref["2 Chronicles 28:3"][
        "draft_translation"
    ]
    assert "gods of the nations of the earth" in by_ref["2 Chronicles 32:17"][
        "draft_translation"
    ]
    assert "commanders of the force of the king" in by_ref["2 Chronicles 33:11"][
        "draft_translation"
    ]
    assert "rulers of the earth" in by_ref["Job 12:24"]["draft_translation"]
    assert "under the sun" in by_ref["Ecclesiastes 1:3"]["draft_translation"]
    assert "the daughter of my people" in by_ref["Jeremiah 4:11"][
        "draft_translation"
    ]
    assert by_ref["Ezra 1:5"]["draft_translation"].startswith(
        "Then the heads of father-houses"
    )
    assert "chiefs of the houses of fathers" in by_ref["1 Chronicles 7:7"][
        "draft_translation"
    ]
    assert "chiefs of the father-houses of priests" in by_ref[
        "1 Chronicles 24:6"
    ]["draft_translation"]
    assert "house of the tombs of my fathers" in by_ref["Nehemiah 2:3"][
        "draft_translation"
    ]
    assert "of the words of the king" in by_ref["Nehemiah 2:18"][
        "draft_translation"
    ]
    assert "the hand of the peoples of the land" in by_ref["Nehemiah 9:30"][
        "draft_translation"
    ]
    assert "the judgments of your righteousness" in by_ref["Psalms 118:7"][
        "draft_translation"
    ]
    assert "from the day of your fall" in by_ref["Ezekiel 26:18"][
        "draft_translation"
    ]
    assert "Lord's anger" in by_ref["Numbers 32:14"]["draft_translation"]
    assert "from the strength of your hand" in by_ref["Psalms 38:11"][
        "draft_translation"
    ]
    assert "by the multitude of his strength" in by_ref["Psalms 32:16"][
        "draft_translation"
    ]
    assert "breath of the spirit of your wrath" in by_ref["Psalms 17:16"][
        "draft_translation"
    ]
    assert "under the sun for the number of days" in by_ref["Ecclesiastes 2:3"][
        "draft_translation"
    ]
    assert "for the number of days" in by_ref["Ezekiel 4:5"]["draft_translation"]
    assert "with the sun and before the moon" in by_ref["Psalms 71:5"][
        "draft_translation"
    ]
    assert "Seven times a day" in by_ref["Psalms 118:164"]["draft_translation"]
    assert "on the day when the Lord rescued him" in by_ref["Psalms 17:1"][
        "draft_translation"
    ]
    assert "by day and by night" in by_ref["Ecclesiastes 8:16"][
        "draft_translation"
    ]
    assert "as on the day of Midian" in by_ref["Isaiah 9:3"]["draft_translation"]
    assert "the yoke lying on them and the rod on their neck" in by_ref["Isaiah 9:3"][
        "draft_translation"
    ]
    assert "the race is not to the swift" in by_ref["Ecclesiastes 9:11"][
        "draft_translation"
    ]
    assert "did not hear the voice of tax-collector" in by_ref["Job 3:18"]["draft_translation"]
    assert by_ref["Job 4:10"]["draft_translation"].startswith("The strength of a lion")
    assert "the Lord with the voice of a trumpet" in by_ref["Psalms 46:6"]["draft_translation"]
    assert "will not hear the voice of charmers" in by_ref["Psalms 57:6"]["draft_translation"]
    assert "the Lord will hear the voice of my supplication" in by_ref[
        "Psalms 114:1"
    ]["draft_translation"]
    assert "the voice of a turtledove was heard" in by_ref[
        "Song of Solomon 2:12"
    ]["draft_translation"]
    assert "by the voice of the Lord" in by_ref["Isaiah 30:31"]["draft_translation"]
    assert by_ref["Isaiah 66:6"]["draft_translation"].startswith(
        "The voice of a cry from the city"
    )
    assert "did not obey the voice of the Lord" in by_ref["Jeremiah 3:25"][
        "draft_translation"
    ]
    assert by_ref["Jeremiah 49:6"]["draft_translation"].startswith(
        "Whether good or evil, the voice of the Lord"
    )
    assert by_ref["Ecclesiastes 7:19"]["draft_translation"].startswith(
        "Wisdom will help the wise man"
    )
    assert by_ref["Proverbs 24:7"]["draft_translation"].startswith(
        "Wisdom and good understanding are at"
    )
    assert by_ref["Proverbs 29:8"]["draft_translation"].startswith(
        "Lawless men set a city on fire"
    )
    assert by_ref["Isaiah 24:17"]["draft_translation"].startswith(
        "Fear and pit and snare are upon you"
    )
    assert "This one is the father of the Moabites" in by_ref["Genesis 19:37"]["draft_translation"]
    assert "This one is the father of the Ammonites" in by_ref["Genesis 19:38"]["draft_translation"]
    assert "he is the father of Jesse, the father of David" in by_ref["Ruth 4:17"]["draft_translation"]
    assert "he is the king of glory" in by_ref["Psalms 23:10"]["draft_translation"]
    assert by_ref["Genesis 4:20"]["draft_translation"].startswith(
        "And Adah bore Jabal. He was the father"
    )
    assert "Ham was the father of Canaan" in by_ref["Genesis 9:18"]["draft_translation"]
    assert "then I was your father's servant" in by_ref["2 Samuel 15:34"]["draft_translation"]
    assert "And the sons of Belah were: Gera" in by_ref["Genesis 46:21"]["draft_translation"]
    assert "all Edomites became David's servants" in by_ref["1 Chronicles 18:13"]["draft_translation"]
    assert "they will be portions for foxes" in by_ref["Psalms 62:11"]["draft_translation"]
    assert "there will be folds for flocks" in by_ref["Isaiah 65:10"]["draft_translation"]
    assert "the valley of Achor as a resting place for herds" in by_ref[
        "Isaiah 65:10"
    ]["draft_translation"]
    assert "the house of Israel was ashamed of Bethel" in by_ref["Jeremiah 31:13"]["draft_translation"]
    assert "until the time of completion" in by_ref["Daniel 9:26"]["draft_translation"]
    assert "until the time of the completion of war" in by_ref["Daniel 9:27"]["draft_translation"]
    assert "until the time of completion" in by_ref["Daniel 11:35"]["draft_translation"]
    assert by_ref["Job 22:11"]["draft_translation"].startswith("The light turned to darkness")
    assert by_ref["Job 22:19"]["draft_translation"].startswith("Righteous men saw and laughed")
    assert by_ref["Proverbs 1:20"]["draft_translation"].startswith("Wisdom is hymned")
    assert by_ref["Proverbs 11:8"]["draft_translation"].startswith("A righteous one escapes")
    assert "Joy lingers for the righteous" in by_ref["Proverbs 10:28"]["draft_translation"]
    assert by_ref["Proverbs 10:30"]["draft_translation"].startswith("The righteous forever")
    assert by_ref["Proverbs 12:10"]["draft_translation"].startswith("A righteous one pities")
    assert by_ref["Proverbs 12:17"]["draft_translation"].startswith("A righteous one openly")
    assert by_ref["Proverbs 13:5"]["draft_translation"].startswith("A righteous one hates")
    assert by_ref["Proverbs 13:9"]["draft_translation"].startswith("There is light for the righteous always")
    assert by_ref["Proverbs 11:19"]["draft_translation"].startswith("A righteous son")
    assert by_ref["Proverbs 10:24"]["draft_translation"].startswith("An ungodly one")
    assert "the ungodly will not inhabit the earth" in by_ref["Proverbs 10:30"]["draft_translation"]
    assert by_ref["Proverbs 21:26"]["draft_translation"].startswith("An ungodly one")
    assert by_ref["Proverbs 28:1"]["draft_translation"].startswith("An ungodly one")
    assert by_ref["Isaiah 25:8"]["draft_translation"].startswith("Death was swallowed")
    assert by_ref["Isaiah 29:20"]["draft_translation"].startswith("The lawless one failed")
    assert by_ref["Isaiah 33:14"]["draft_translation"].startswith("The lawless in Zion")
    assert "There will be the joy of birds" in by_ref["Isaiah 35:7"]["draft_translation"]
    assert "where there was the hope of help for him" in by_ref["Isaiah 30:32"]["draft_translation"]
    assert by_ref["Job 29:16"]["draft_translation"].startswith("I was a father to weak men")
    assert "This one was the father of Ziph" in by_ref["1 Chronicles 2:42"]["draft_translation"]
    assert "Maon was the father of Bethzur" in by_ref["1 Chronicles 2:45"]["draft_translation"]
    assert "This one was the father of Eshton" in by_ref["1 Chronicles 4:11"]["draft_translation"]
    assert by_ref["Job 3:23"]["draft_translation"].startswith("Death is rest for a man")
    assert "until the moon is removed" in by_ref["Psalms 71:7"]["draft_translation"]
    assert "set his footsteps in the way" in by_ref["Psalms 84:14"]["draft_translation"]
    assert by_ref["Psalms 96:11"]["draft_translation"].startswith("Light arose for a righteous one")
    assert by_ref["Psalms 111:3"]["draft_translation"].startswith("Glory and wealth are in his house")
    assert by_ref["Psalms 33:18"]["draft_translation"].startswith("The righteous cried out")
    assert by_ref["Psalms 140:5"]["draft_translation"].startswith("A righteous one will instruct")
    assert "oil of a sinner" in by_ref["Psalms 140:5"]["draft_translation"]
    assert by_ref["Proverbs 16:13"]["draft_translation"].startswith("Righteous lips are acceptable")
    assert by_ref["Proverbs 13:23"]["draft_translation"].startswith("A righteous one will make")
    assert by_ref["Proverbs 13:25"]["draft_translation"].startswith("A righteous one eats")
    assert by_ref["Proverbs 21:12"]["draft_translation"].startswith("A righteous one understands")
    assert by_ref["Proverbs 23:24"]["draft_translation"].startswith("A righteous father")
    assert by_ref["Proverbs 29:4"]["draft_translation"].startswith("A righteous king")
    assert by_ref["Proverbs 29:7"]["draft_translation"].startswith("A righteous one knows")
    assert "one sinner will destroy much good" in by_ref["Ecclesiastes 9:18"]["draft_translation"]
    assert by_ref["Lamentations 3:47"]["draft_translation"].startswith("Fear and anger came upon us")
    assert "God knows them" in by_ref["Hosea 12:1"]["draft_translation"]
    assert "God's holy people" in by_ref["Hosea 12:1"]["draft_translation"]
    assert "trusting in them" in by_ref["Jeremiah 31:13"]["draft_translation"]
    assert "he was a relative of her father" in by_ref["Genesis 29:12"]["draft_translation"]
    assert "so was the appearance of brightness around" in by_ref["Ezekiel 1:28"]["draft_translation"]
    assert by_ref["Job 34:18"]["draft_translation"].startswith("He is ungodly who says")
    assert by_ref["Proverbs 16:21"]["draft_translation"].startswith("Men call the wise")
    assert by_ref["Jeremiah 31:33"]["draft_translation"].startswith(
        "Joy and gladness were utterly swept"
    )
    assert "he was the son of Rebekah" in by_ref["Genesis 29:12"]["draft_translation"]
    assert "Amasa was the son of a man" in by_ref["2 Samuel 17:25"]["draft_translation"]
    assert "this one was the son of Isabia" in by_ref["1 Chronicles 4:35"]["draft_translation"]
    assert by_ref["Nehemiah 11:22"]["draft_translation"].startswith(
        "And the overseer of the Levites"
    )
    assert "he himself was the son of Zerah" in by_ref["Job 42:17"]["draft_translation"]
    assert "he was chief of the three" in by_ref["1 Chronicles 11:20"]["draft_translation"]
    assert "Ioudias was the chief of the Hebronites" in by_ref["1 Chronicles 26:31"]["draft_translation"]
    assert "Ahithophel was counselor to the king" in by_ref["1 Chronicles 27:33"]["draft_translation"]
    assert "Cushi was the first friend of the king" in by_ref["1 Chronicles 27:33"]["draft_translation"]
    assert "who was overseer over the men of war" in by_ref["Jeremiah 52:25"]["draft_translation"]
    assert "with them was the book of the law of the Lord" in by_ref["2 Chronicles 17:9"]["draft_translation"]
    assert "found the book of the law of the Lord" in by_ref["2 Chronicles 34:14"]["draft_translation"]
    assert "when the king heard the words of the law" in by_ref["2 Chronicles 34:19"]["draft_translation"]
    assert "bring the book of the law of Moses" in by_ref["Nehemiah 8:1"]["draft_translation"]
    assert "toward the book of the law" in by_ref["Nehemiah 8:3"]["draft_translation"]
    assert "all the words of the law" in by_ref["Nehemiah 8:13"]["draft_translation"]
    assert "I found the book of the law" in by_ref["2 Chronicles 34:15"]["draft_translation"]
    assert "gave the book to Shaphan" in by_ref["2 Chronicles 34:15"]["draft_translation"]
    assert "taught the people" in by_ref["2 Chronicles 17:9"]["draft_translation"]
    assert "praising the king and entered to the king" in by_ref["2 Chronicles 23:12"]["draft_translation"]
    assert "announced to the king all the words" in by_ref["Jeremiah 43:20"]["draft_translation"]
    assert "when the king heard them singing" in by_ref["Daniel 3:24"]["draft_translation"]
    assert "heard the words of the law" in by_ref["Nehemiah 8:9"]["draft_translation"]
    assert "the words of the Lord refined" in by_ref["Psalms 17:31"]["draft_translation"]
    assert "provoked the words of God" in by_ref["Psalms 106:11"]["draft_translation"]
    assert "All the words of God are refined" in by_ref["Proverbs 30:5"]["draft_translation"]
    assert "The words of the wise in quiet" in by_ref["Ecclesiastes 9:17"]["draft_translation"]
    assert "The words of the wise are as goads" in by_ref["Ecclesiastes 12:11"]["draft_translation"]
    assert "all the words of the Lord which he had declared" in by_ref["Jeremiah 43:4"]["draft_translation"]
    assert "read in the scroll the words of the Lord" in by_ref["Jeremiah 43:8"]["draft_translation"]
    assert "did not hear the words of the Lord" in by_ref["Jeremiah 44:2"]["draft_translation"]
    assert "like the appearance of a carbuncle stone" in by_ref["Ezekiel 10:9"]["draft_translation"]
    assert "like the fish of the great sea" in by_ref["Ezekiel 47:10"]["draft_translation"]
    assert "as the fish of the sea" in by_ref["Habakkuk 1:14"]["draft_translation"]
    assert "like the likeness of an angel" in by_ref["Daniel 3:25"]["draft_translation"]
    assert "like a woman giving birth" in by_ref["Jeremiah 13:21"]["draft_translation"]
    assert "like a vessel of no use" in by_ref["Jeremiah 22:28"]["draft_translation"]
    assert "like a hammer breaking rock" in by_ref["Jeremiah 23:29"]["draft_translation"]
    assert "like an arrow of wise warrior" in by_ref["Jeremiah 27:9"]["draft_translation"]
    assert "swallowed me like a dragon" in by_ref["Jeremiah 28:34"]["draft_translation"]
    assert "like an enemy" in by_ref["Lamentations 2:4"]["draft_translation"]
    assert "like an adversary" in by_ref["Lamentations 2:4"]["draft_translation"]
    assert "like a barber's razor" in by_ref["Ezekiel 5:1"]["draft_translation"]
    assert "Lament to me like a bride" in by_ref["Joel 1:8"]["draft_translation"]
    assert "like a firebrand in wood" in by_ref["Zechariah 12:6"]["draft_translation"]
    assert "like a torch of fire" in by_ref["Zechariah 12:6"]["draft_translation"]
    assert "like an angel of the Lord" in by_ref["Zechariah 12:8"]["draft_translation"]
    assert "the vine will give its fruit, the land will give its produce" in by_ref["Zechariah 8:12"]["draft_translation"]
    assert by_ref["Zechariah 8:19"]["draft_translation"].startswith("Thus says the Lord Almighty: The fast of the fourth")
    assert "forming the spirit of a human within him" in by_ref["Zechariah 12:1"]["draft_translation"]
    assert by_ref["Proverbs 1:1"]["draft_translation"].startswith("The Proverbs of Solomon")
    assert "hope may be on the Lord" in by_ref["Proverbs 22:19"]["draft_translation"]
    assert by_ref["Song of Solomon 1:1"]["draft_translation"].startswith("The Song of Songs")
    assert "the scent of your perfumes is above all spices" in by_ref[
        "Song of Solomon 1:3"
    ]["draft_translation"]
    assert "The king brought me into his chamber" in by_ref["Song of Solomon 1:4"][
        "draft_translation"
    ]
    assert "the sun looked past me" in by_ref["Song of Solomon 1:6"][
        "draft_translation"
    ]
    assert "go out on the heels of the flocks" in by_ref["Song of Solomon 1:8"][
        "draft_translation"
    ]
    assert "your eyes are doves" in by_ref["Song of Solomon 1:15"][
        "draft_translation"
    ]
    assert "As a lily in the midst of thorns" in by_ref["Song of Solomon 2:2"][
        "draft_translation"
    ]
    assert "among the trees of the grove" in by_ref["Song of Solomon 2:3"][
        "draft_translation"
    ]
    assert "the winter passed, the rain departed" in by_ref[
        "Song of Solomon 2:11"
    ]["draft_translation"]
    assert "your voice is sweet and your face is beautiful" in by_ref[
        "Song of Solomon 2:14"
    ]["draft_translation"]
    assert "among the lilies" in by_ref["Song of Solomon 2:16"][
        "draft_translation"
    ]
    assert "in the markets and in the squares" in by_ref["Song of Solomon 3:2"][
        "draft_translation"
    ]
    assert "Did you see the one my soul loved" in by_ref["Song of Solomon 3:3"][
        "draft_translation"
    ]
    assert "by the powers and by the strengths of the field" in by_ref[
        "Song of Solomon 3:5"
    ]["draft_translation"]
    assert "All holding a sword" in by_ref["Song of Solomon 3:8"][
        "draft_translation"
    ]
    assert "made for himself a litter" in by_ref["Song of Solomon 3:9"][
        "draft_translation"
    ]
    assert "your eyes are doves behind your veil" in by_ref["Song of Solomon 4:1"][
        "draft_translation"
    ]
    assert "Your neck is like the tower of David" in by_ref[
        "Song of Solomon 4:4"
    ]["draft_translation"]
    assert "Until the day breathes and the shadows move" in by_ref[
        "Song of Solomon 4:6"
    ]["draft_translation"]
    assert "You are wholly beautiful" in by_ref["Song of Solomon 4:7"][
        "draft_translation"
    ]
    assert "the scent of your garments is above all spices" in by_ref[
        "Song of Solomon 4:10"
    ]["draft_translation"]
    assert "A garden shut" in by_ref["Song of Solomon 4:12"]["draft_translation"]
    assert "knocks at the door" in by_ref["Song of Solomon 5:2"][
        "draft_translation"
    ]
    assert "my fingers were full of myrrh" in by_ref["Song of Solomon 5:5"][
        "draft_translation"
    ]
    assert "by the powers and by the strengths of the field" in by_ref[
        "Song of Solomon 5:8"
    ]["draft_translation"]
    assert "My beloved is white and ruddy" in by_ref["Song of Solomon 5:10"][
        "draft_translation"
    ]
    assert "His cheeks are like bowls of spice" in by_ref[
        "Song of Solomon 5:13"
    ]["draft_translation"]
    assert "His throat is sweetness" in by_ref["Song of Solomon 5:16"][
        "draft_translation"
    ]
    assert "I am to my beloved" in by_ref["Song of Solomon 6:3"][
        "draft_translation"
    ]
    assert "awe-inspiring as battle-lines" in by_ref["Song of Solomon 6:4"][
        "draft_translation"
    ]
    assert "Your lips are like a scarlet cord" in by_ref[
        "Song of Solomon 6:7"
    ]["draft_translation"]
    assert "beautiful as the moon, chosen as the sun" in by_ref[
        "Song of Solomon 6:10"
    ]["draft_translation"]
    assert "Into a garden of walnut trees" in by_ref["Song of Solomon 6:11"][
        "draft_translation"
    ]
    assert "The curves of your thighs are like necklaces" in by_ref[
        "Song of Solomon 7:2"
    ]["draft_translation"]
    assert "Your neck is like an ivory tower" in by_ref[
        "Song of Solomon 7:5"
    ]["draft_translation"]
    assert "This stature of yours was likened to a palm tree" in by_ref[
        "Song of Solomon 7:8"
    ]["draft_translation"]
    assert "I am to my beloved, and his turning is upon me" in by_ref[
        "Song of Solomon 7:11"
    ]["draft_translation"]
    assert "The mandrakes gave scent" in by_ref["Song of Solomon 7:14"][
        "draft_translation"
    ]
    assert "His left is under my head" in by_ref["Song of Solomon 8:3"][
        "draft_translation"
    ]
    assert "by the powers and by the strengths of the field" in by_ref[
        "Song of Solomon 8:4"
    ]["draft_translation"]
    assert "love is as strong as death" in by_ref["Song of Solomon 8:6"][
        "draft_translation"
    ]
    assert "I am a wall, and my breasts are like towers" in by_ref[
        "Song of Solomon 8:10"
    ]["draft_translation"]
    assert "My vineyard is mine before me" in by_ref["Song of Solomon 8:12"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 1:1"]["draft_translation"].startswith("The vision which Isaiah")
    assert "The ox knew the one acquiring it" in by_ref["Isaiah 1:3"][
        "draft_translation"
    ]
    assert "because your hands are full of blood" in by_ref["Isaiah 1:15"][
        "draft_translation"
    ]
    assert "the good things of the land you will eat" in by_ref["Isaiah 1:19"][
        "draft_translation"
    ]
    assert "Your silver is unapproved" in by_ref["Isaiah 1:22"][
        "draft_translation"
    ]
    assert "as a terebinth" in by_ref["Isaiah 1:30"]["draft_translation"]
    assert "For from Zion the law will come out" in by_ref["Isaiah 2:3"][
        "draft_translation"
    ]
    assert "Their land was filled with silver and gold" in by_ref["Isaiah 2:7"][
        "draft_translation"
    ]
    assert "For the eyes of the Lord are high" in by_ref["Isaiah 2:11"][
        "draft_translation"
    ]
    assert "the day of the Lord of hosts is upon" in by_ref["Isaiah 2:12"][
        "draft_translation"
    ]
    assert "a giant and a strong man and a man of war" in by_ref["Isaiah 3:2"][
        "draft_translation"
    ]
    assert "a child will strike against an elder" in by_ref["Isaiah 3:5"][
        "draft_translation"
    ]
    assert "the righteous one" in by_ref["Isaiah 3:10"]["draft_translation"]
    assert "the path of your feet" in by_ref["Isaiah 3:12"]["draft_translation"]
    assert "shame the face of the poor" in by_ref["Isaiah 3:15"][
        "draft_translation"
    ]
    assert "the glory of their clothing" in by_ref["Isaiah 3:18"][
        "draft_translation"
    ]
    assert "instead of a sweet smell there will be dust" in by_ref["Isaiah 3:24"][
        "draft_translation"
    ]
    assert "the one left in Zion" in by_ref["Isaiah 4:3"]["draft_translation"]
    assert "wash the filth of the sons and daughters of Zion" in by_ref[
        "Isaiah 4:4"
    ]["draft_translation"]
    assert "A vineyard came to my beloved on a hilltop" in by_ref["Isaiah 5:1"][
        "draft_translation"
    ]
    assert "the vineyard of the Lord of hosts is the house of Israel" in by_ref[
        "Isaiah 5:7"
    ]["draft_translation"]
    assert "Woe to those saying evil is good and good is evil" in by_ref[
        "Isaiah 5:20"
    ]["draft_translation"]
    assert "the right of the righteous" in by_ref["Isaiah 5:23"][
        "draft_translation"
    ]
    assert "his hand is still high" in by_ref["Isaiah 5:25"]["draft_translation"]
    assert "there will not be one rescuing them" in by_ref["Isaiah 5:29"][
        "draft_translation"
    ]
    assert "the house was full of his glory" in by_ref["Isaiah 6:1"][
        "draft_translation"
    ]
    assert "with two they covered the face" in by_ref["Isaiah 6:2"][
        "draft_translation"
    ]
    assert "in his hand he had a coal" in by_ref["Isaiah 6:6"][
        "draft_translation"
    ]
    assert "understand with the heart" in by_ref["Isaiah 6:10"][
        "draft_translation"
    ]
    assert "to the pool of the upper road of the fuller's field" in by_ref[
        "Isaiah 7:3"
    ]["draft_translation"]
    assert "the kingdom of Ephraim will cease from being a people" in by_ref[
        "Isaiah 7:8"
    ]["draft_translation"]
    assert "the virgin will have a child in the womb" in by_ref["Isaiah 7:14"][
        "draft_translation"
    ]
    assert "since the day Ephraim was taken away from Judah" in by_ref[
        "Isaiah 7:17"
    ]["draft_translation"]
    assert "with a razor, the great and drunken one" in by_ref["Isaiah 7:20"][
        "draft_translation"
    ]
    assert "for the grazing of sheep and the trampling of ox" in by_ref[
        "Isaiah 7:25"
    ]["draft_translation"]
    assert "the water of Siloam going quietly" in by_ref["Isaiah 8:6"][
        "draft_translation"
    ]
    assert "the water of the river, strong and abundant" in by_ref[
        "Isaiah 8:7"
    ]["draft_translation"]
    assert "whatever word you speak" in by_ref["Isaiah 8:10"]["draft_translation"]
    assert "as a stumbling stone" in by_ref["Isaiah 8:14"]["draft_translation"]
    assert "Then those sealing the law" in by_ref["Isaiah 8:16"][
        "draft_translation"
    ]
    assert "the way of the sea" in by_ref["Isaiah 8:23"]["draft_translation"]
    assert by_ref["Isaiah 13:1"]["draft_translation"].startswith("The vision which Isaiah")
    assert "the stars of heaven" in by_ref["Isaiah 13:10"]["draft_translation"]
    assert "great is the day of Jezreel" in by_ref["Hosea 2:2"]["draft_translation"]
    assert "stand amazed at the Lord" in by_ref["Hosea 3:5"]["draft_translation"]
    assert "in the last days" in by_ref["Hosea 3:5"]["draft_translation"]
    assert by_ref["Daniel 10:13"]["draft_translation"].startswith("And the commander of the king of the Persians")
    assert "with the commander of the king of the Persians" in by_ref["Daniel 10:13"]["draft_translation"]
    assert "one of the first rulers" in by_ref["Daniel 10:13"]["draft_translation"]
    assert "behold, the commander of Greeks" in by_ref["Daniel 10:20"]["draft_translation"]
    assert "Sennacherib king of the Assyrians" in by_ref["2 Chronicles 32:1"]["draft_translation"]
    assert "Cyrus king of the Persians" in by_ref["2 Chronicles 36:22"]["draft_translation"]
    assert "king of the north will come" in by_ref["Daniel 11:7"]["draft_translation"]
    assert "as the house of Ahab did" in by_ref["2 Chronicles 21:6"]["draft_translation"]
    assert "let the house of David your servant be established" in by_ref["1 Chronicles 17:24"]["draft_translation"]
    assert "like the house of David, and the house of David like the house of God" in by_ref["Zechariah 12:8"]["draft_translation"]
    assert "Amaziah gathered the house of Judah" in by_ref["2 Chronicles 25:5"]["draft_translation"]
    assert by_ref["Psalms 113:1"]["draft_translation"].startswith("Alleluia. When Israel went out from Egypt")
    assert "the house of Jacob will inherit" in by_ref["Obadiah 1:17"]["draft_translation"]
    assert "placed the ark of God" in by_ref["1 Chronicles 13:7"]["draft_translation"]
    assert "carrying the ark of the covenant of the Lord" in by_ref["1 Chronicles 15:26"]["draft_translation"]
    assert "scribe of the law of the God of heaven" in by_ref["Ezra 7:12"]["draft_translation"]
    assert "in the book of the law of God" in by_ref["Nehemiah 8:8"]["draft_translation"]
    assert "heed the law of God" in by_ref["Isaiah 1:10"]["draft_translation"]
    assert "recount the glory of God" in by_ref["Psalms 18:2"]["draft_translation"]
    assert by_ref["Ezekiel 9:3"]["draft_translation"].startswith("And the glory of God of Israel")
    assert "wine gladdens the heart of man" in by_ref["Psalms 103:15"]["draft_translation"]
    assert "bread strengthens the heart of man" in by_ref["Psalms 103:15"]["draft_translation"]
    assert "to brighten the face with oil" in by_ref["Psalms 103:15"]["draft_translation"]
    assert "glorify the remnant of Israel" in by_ref["Isaiah 4:2"]["draft_translation"]
    assert "toward the mountains of Israel" in by_ref["Ezekiel 6:2"]["draft_translation"]
    assert "with the sound of a trumpet" in by_ref["Psalms 150:3"]["draft_translation"]
    assert "the mouth of the ungodly" in by_ref["Proverbs 10:6"]["draft_translation"]
    assert "the camp of the Philistines" in by_ref["1 Chronicles 11:15"]["draft_translation"]
    assert "charges of the tent of testimony" in by_ref["1 Chronicles 23:32"]["draft_translation"]
    assert "dedicated the house of God" in by_ref["2 Chronicles 7:5"]["draft_translation"]
    assert "destroy the house of David" in by_ref["2 Chronicles 21:7"]["draft_translation"]
    assert "like the house of Ahab" in by_ref["2 Chronicles 22:4"]["draft_translation"]
    assert "avenged the house of Ahab" in by_ref["2 Chronicles 22:8"]["draft_translation"]
    assert "pulled down the house of God" in by_ref["2 Chronicles 24:7"]["draft_translation"]
    assert "honored the people and the house of God" in by_ref["Ezra 8:36"]["draft_translation"]
    assert "opposite the house of God" in by_ref["Nehemiah 11:11"]["draft_translation"]
    assert "above the house of David" in by_ref["Nehemiah 12:37"]["draft_translation"]
    assert "Why was the house of God forsaken" in by_ref["Nehemiah 13:11"]["draft_translation"]
    assert "as far as the house of God" in by_ref["Psalms 41:5"]["draft_translation"]
    assert "he blessed the house of Israel" in by_ref["Psalms 113:20"]["draft_translation"]
    assert "Let the house of Israel say" in by_ref["Psalms 117:2"]["draft_translation"]
    assert "the house of God will be manifest" in by_ref["Isaiah 2:2"]["draft_translation"]
    assert "the house of Jacob is in a snare" in by_ref["Isaiah 8:14"]["draft_translation"]
    assert "the house of Judah will come" in by_ref["Jeremiah 3:18"]["draft_translation"]
    assert "so the house of Israel acted faithlessly" in by_ref["Jeremiah 3:20"]["draft_translation"]
    assert "the house of Israel and the house of Judah acted faithlessly" in by_ref["Jeremiah 5:11"]["draft_translation"]
    assert "and the house of Judah broke my covenant" in by_ref["Jeremiah 11:10"]["draft_translation"]
    assert "brought up the house of Israel" in by_ref["Jeremiah 16:15"]["draft_translation"]
    assert "the remnant of Israel and those saved of Jacob will no longer keep trusting" in by_ref[
        "Isaiah 10:20"
    ]["draft_translation"]
    assert "people, the remnant of Israel" in by_ref["Jeremiah 38:7"]["draft_translation"]
    assert "the remnant of Judah perish" in by_ref["Jeremiah 47:15"]["draft_translation"]
    assert "wipe out the remnant of Israel" in by_ref["Ezekiel 9:8"]["draft_translation"]
    assert "bringing the remnant of Israel to an end" in by_ref["Ezekiel 11:13"]["draft_translation"]
    assert "receive the remnant of Israel" in by_ref["Micah 2:12"]["draft_translation"]
    assert "cloud of the glory of the Lord" in by_ref["2 Chronicles 5:13"]["draft_translation"]
    assert "and the glory of the Lord upon the house" in by_ref["2 Chronicles 7:3"]["draft_translation"]
    assert "Let the glory of the Lord be forever" in by_ref["Psalms 103:31"]["draft_translation"]
    assert "great is the glory of the Lord" in by_ref["Psalms 137:5"]["draft_translation"]
    assert "a fading of the glory of Jacob" in by_ref["Isaiah 17:4"]["draft_translation"]
    assert "see the glory of the Lord" in by_ref["Isaiah 26:10"]["draft_translation"]
    assert "the glory of the Lord has risen" in by_ref["Isaiah 60:1"]["draft_translation"]
    assert "to earth the glory of Israel" in by_ref["Lamentations 2:1"]["draft_translation"]
    assert "likeness of the glory of the Lord" in by_ref["Ezekiel 1:28"]["draft_translation"]
    assert "Blessed be the glory of the Lord" in by_ref["Ezekiel 3:12"]["draft_translation"]
    assert "there the glory of the Lord stood" in by_ref["Ezekiel 3:23"]["draft_translation"]
    assert "there was the glory of the Lord God of Israel" in by_ref["Ezekiel 8:4"]["draft_translation"]
    assert "brightness of the glory of the Lord" in by_ref["Ezekiel 10:4"]["draft_translation"]
    assert "full of the glory of the Lord" in by_ref["Ezekiel 43:5"]["draft_translation"]
    assert "know the glory of the Lord" in by_ref["Habakkuk 2:14"]["draft_translation"]
    assert "where the ark of the Lord entered" in by_ref["2 Chronicles 8:11"]["draft_translation"]
    assert "book of the law of Moses" in by_ref["Nehemiah 8:1"]["draft_translation"]
    assert "hear the law of God" in by_ref["Isaiah 30:9"]["draft_translation"]
    assert "Remember the law of Moses" in by_ref["Malachi 3:24"]["draft_translation"]
    assert by_ref["2 Chronicles 24:20"]["draft_translation"].startswith("And the Spirit of God clothed")
    assert "above the people and said" in by_ref["2 Chronicles 24:20"]["draft_translation"]
    assert "transgress the commandments of the Lord" in by_ref["2 Chronicles 24:20"]["draft_translation"]
    assert "Because you forsake the Lord" in by_ref["2 Chronicles 24:20"]["draft_translation"]
    assert by_ref["Isaiah 11:2"]["draft_translation"].startswith("And the Spirit of God will rest")
    assert "a spirit of counsel and strength" in by_ref["Isaiah 11:2"]["draft_translation"]
    assert "in the Spirit of God" in by_ref["Ezekiel 11:24"]["draft_translation"]
    assert "from the tribe of Judah" in by_ref["Haggai 1:1"]["draft_translation"]
    assert "before the face of the Most High" in by_ref["Lamentations 3:35"]["draft_translation"]
    assert "in the house of the Lord" in by_ref["2 Chronicles 20:5"]["draft_translation"]
    assert "from man to woman" in by_ref["Nehemiah 8:2"]["draft_translation"]
    assert by_ref["Jeremiah 1:1"]["draft_translation"].startswith("The word of God")
    assert by_ref["Hosea 1:1"]["draft_translation"].startswith("The word of the Lord")
    assert by_ref["Psalms 11:7"]["draft_translation"].startswith("The words of the Lord")
    assert "in the midst of their brothers" in by_ref["1 Chronicles 9:38"]["draft_translation"]
    assert "from the midst of the king’s sons" in by_ref["2 Chronicles 22:11"]["draft_translation"]
    assert "God is in the midst of her" in by_ref["Psalms 45:6"]["draft_translation"]
    assert "before the eyes of God" in by_ref["Proverbs 5:21"]["draft_translation"]
    assert "from the day when I brought up Israel" in by_ref["1 Chronicles 17:5"]["draft_translation"]
    assert "until the day he died" in by_ref["Jeremiah 52:34"]["draft_translation"]
    assert "on the day you were born" in by_ref["Ezekiel 16:4"]["draft_translation"]
    assert "in the day of destruction" in by_ref["Job 21:30"]["draft_translation"]
    assert "in the time of their affliction" in by_ref["Nehemiah 9:27"]["draft_translation"]
    assert "from the beginning" in by_ref["Psalms 73:2"]["draft_translation"]
    assert "people of the land" in by_ref["2 Chronicles 23:13"]["draft_translation"]
    assert "inhabitants of the land" in by_ref["1 Chronicles 22:18"]["draft_translation"]
    assert "to the house of the Lord" in by_ref["2 Chronicles 20:28"]["draft_translation"]
    assert "into the house of Obededom" in by_ref["1 Chronicles 13:13"]["draft_translation"]
    assert "from the house of Obededom" in by_ref["1 Chronicles 15:25"]["draft_translation"]
    assert "in the house of Dagon" in by_ref["1 Chronicles 10:10"]["draft_translation"]
    assert "before the house of God" in by_ref["Ezra 10:1"]["draft_translation"]
    assert "against the house of Ahab" in by_ref["2 Chronicles 22:7"]["draft_translation"]
    assert "over the house of David" in by_ref["Psalms 121:5"]["draft_translation"]
    assert "for the house of the Lord" in by_ref["1 Chronicles 22:14"]["draft_translation"]
    assert "concerning the house of David" in by_ref["2 Chronicles 23:3"]["draft_translation"]
    assert "ruler of the house of God" in by_ref["1 Chronicles 9:11"]["draft_translation"]
    assert "service of the house of God" in by_ref["1 Chronicles 28:21"]["draft_translation"]
    assert "house of the king" in by_ref["2 Chronicles 7:11"]["draft_translation"]
    assert "inside the house of the Lord" in by_ref["2 Chronicles 29:16"]["draft_translation"]
    assert "in the houses of their fathers" in by_ref["1 Chronicles 4:38"]["draft_translation"]
    assert "by the river Chebar" in by_ref["Ezekiel 1:1"]["draft_translation"]
    assert "in the heart of the sea" in by_ref["Ezekiel 27:25"]["draft_translation"]
    assert "into the heart of the sea" in by_ref["Jonah 2:4"]["draft_translation"]
    assert "set your heart as the heart of God" in by_ref["Ezekiel 28:2"]["draft_translation"]
    assert "from the face of Absalom" in by_ref["Psalms 3:1"]["draft_translation"]
    assert "upon the face of land" in by_ref["2 Chronicles 6:31"]["draft_translation"]
    assert "on the face of water" in by_ref["Hosea 10:7"]["draft_translation"]
    assert "uncover the face of its clothing" in by_ref["Job 41:5"]["draft_translation"]
    assert "over the face of all the earth" in by_ref["Ezekiel 34:6"]["draft_translation"]
    assert "before the face of your God" in by_ref["Malachi 1:9"]["draft_translation"]
    assert "from the wall of Jerusalem" in by_ref["2 Chronicles 25:23"]["draft_translation"]
    assert "in the wall of Ophel" in by_ref["2 Chronicles 27:3"]["draft_translation"]
    assert "on the wall of his house" in by_ref["Daniel 5:0"]["draft_translation"]
    assert "width of the wall of the side room" in by_ref["Ezekiel 41:9"]["draft_translation"]
    assert "upon the head of David" in by_ref["1 Chronicles 20:2"]["draft_translation"]
    assert "over the head of the living beings" in by_ref["Ezekiel 1:22"]["draft_translation"]
    assert "on the head of Joshua" in by_ref["Zechariah 6:11"]["draft_translation"]
    assert "upon the seat of pestilent men" in by_ref["Psalms 1:1"]["draft_translation"]
    assert "in the seat of elders" in by_ref["Psalms 106:32"]["draft_translation"]
    assert "before the tent of the Lord" in by_ref["1 Chronicles 16:39"]["draft_translation"]
    assert "from the tent of the Lord" in by_ref["2 Chronicles 29:6"]["draft_translation"]
    assert "in the eyes of all the people" in by_ref["1 Chronicles 13:4"]["draft_translation"]
    assert "in the ears of all the people" in by_ref["Jeremiah 43:10"]["draft_translation"]
    assert "into the ears of all the people" in by_ref["Jeremiah 35:7"]["draft_translation"]
    assert "from the root of Jesse" in by_ref["Isaiah 11:1"]["draft_translation"]
    assert "a flower from the root" in by_ref["Isaiah 11:1"]["draft_translation"]
    assert "the whole world was filled to know the Lord" in by_ref["Isaiah 11:9"][
        "draft_translation"
    ]
    assert "sing a hymn to the Lord" in by_ref["Isaiah 12:4"]["draft_translation"]
    assert "to the top of cliff" in by_ref["2 Chronicles 25:12"]["draft_translation"]
    assert "from the top of Senir" in by_ref["Song of Solomon 4:8"]["draft_translation"]
    assert "at the side of the court" in by_ref["Ezekiel 46:21"]["draft_translation"]
    assert "from the corner of the house" in by_ref["2 Chronicles 4:10"]["draft_translation"]
    assert "in the middle of the portion" in by_ref["1 Chronicles 11:14"]["draft_translation"]
    assert "in the middle of the tent" in by_ref["1 Chronicles 16:1"]["draft_translation"]
    assert "through the middle of the sea" in by_ref["Nehemiah 9:11"]["draft_translation"]
    assert "from the entrance of Hamath" in by_ref["2 Chronicles 7:8"]["draft_translation"]
    assert "in the entrance of the new gate" in by_ref["Jeremiah 33:10"]["draft_translation"]
    assert "at the entrance of the sea" in by_ref["Ezekiel 27:3"]["draft_translation"]
    assert "to the door of the furnace" in by_ref["Daniel 3:26"]["draft_translation"]
    assert "to the door of the house of Eliashib" in by_ref["Nehemiah 3:20"]["draft_translation"]
    assert "from the door of the house of Eliashib" in by_ref["Nehemiah 3:21"]["draft_translation"]
    assert "in the hand of Egyptian" in by_ref["1 Chronicles 11:23"]["draft_translation"]
    assert "from the hand of Egyptian" in by_ref["1 Chronicles 11:23"]["draft_translation"]
    assert "from the hand of Sennacherib" in by_ref["2 Chronicles 32:22"]["draft_translation"]
    assert "upon the heart of David" in by_ref["2 Chronicles 6:7"]["draft_translation"]
    assert "to the heart of Jerusalem" in by_ref["Isaiah 40:2"]["draft_translation"]
    assert "into the heart of the king" in by_ref["Ezra 7:27"]["draft_translation"]
    assert "by the gate of the city" in by_ref["1 Chronicles 19:9"]["draft_translation"]
    assert "through the gate of Goleila" in by_ref["Nehemiah 2:13"]["draft_translation"]
    assert "in the gate of Benjamin" in by_ref["Jeremiah 45:7"]["draft_translation"]
    assert "in the court of the house of the Lord" in by_ref["2 Chronicles 24:21"]["draft_translation"]
    assert "into the court of the house of the Lord" in by_ref["2 Chronicles 29:16"]["draft_translation"]
    assert "from the court of the prison" in by_ref["Jeremiah 46:14"]["draft_translation"]
    assert "in the courts of the house of the Lord" in by_ref["2 Chronicles 23:5"]["draft_translation"]
    assert "on the throne of David" in by_ref["1 Chronicles 29:23"]["draft_translation"]
    assert "upon the throne of Israel" in by_ref["2 Chronicles 6:10"]["draft_translation"]
    assert "in the mouth of all these prophets" in by_ref["2 Chronicles 18:22"]["draft_translation"]
    assert "on the mouth of the den" in by_ref["Daniel 6:18"]["draft_translation"]
    assert "into the mouth of the eater" in by_ref["Nahum 3:12"]["draft_translation"]
    assert "with all his heart and with all his soul" in by_ref["2 Kings 23:3"]["draft_translation"]
    assert "with all their strength" in by_ref["1 Chronicles 13:8"]["draft_translation"]
    assert "with all their heart and all their soul" in by_ref["2 Chronicles 6:38"]["draft_translation"]
    assert "with all their soul they swore" in by_ref["2 Chronicles 15:15"]["draft_translation"]
    assert "with all their desire sought him" in by_ref["2 Chronicles 15:15"]["draft_translation"]
    assert "with all his heart and with all his soul" in by_ref["2 Chronicles 34:31"]["draft_translation"]
    assert "Sing to the Lord, all the earth" in by_ref["1 Chronicles 16:23"]["draft_translation"]
    assert "king over all the earth" in by_ref["Zechariah 14:9"]["draft_translation"]
    assert "their fall, earth was shaken" in by_ref["Jeremiah 30:15"]["draft_translation"]
    assert "from the sound of their fall, earth was shaken" in by_ref["Jeremiah 30:15"]["draft_translation"]
    assert "at the sound of song" in by_ref["Job 21:12"]["draft_translation"]
    assert "heard in the sea" in by_ref["Jeremiah 30:15"]["draft_translation"]
    assert "from the breast of her comfort" in by_ref["Isaiah 66:11"]["draft_translation"]
    assert "from the breasts of my mother" in by_ref["Psalms 21:10"]["draft_translation"]
    assert "in the upper court" in by_ref["Jeremiah 43:10"]["draft_translation"]
    assert "in the fire of my wrath" in by_ref["Ezekiel 21:36"]["draft_translation"]
    assert "in the streets of Jerusalem" in by_ref["Jeremiah 5:1"]["draft_translation"]
    assert "written in the book of kings" in by_ref["2 Chronicles 16:11"]["draft_translation"]
    assert "written upon the book of kings" in by_ref["2 Chronicles 25:26"]["draft_translation"]
    assert "in the words of Samuel" in by_ref["1 Chronicles 29:29"]["draft_translation"]
    assert "to the words of my mouth" in by_ref["Psalms 53:4"]["draft_translation"]
    assert "walked in the way of kings" in by_ref["2 Chronicles 21:6"]["draft_translation"]
    assert "walked in the ways of David" in by_ref["2 Chronicles 11:17"]["draft_translation"]
    assert "upright in the sight of the Lord" in by_ref["2 Chronicles 14:1"]["draft_translation"]
    assert "in the multitude of your mercy" in by_ref["Psalms 5:8"]["draft_translation"]
    assert "to the multitude of their ungodliness" in by_ref["Psalms 5:11"]["draft_translation"]
    assert "by the command of the Lord" in by_ref["Numbers 33:38"]["draft_translation"]
    assert "according to the command of the king" in by_ref["2 Chronicles 35:10"]["draft_translation"]
    assert "in the assembly of Judah" in by_ref["2 Chronicles 20:5"]["draft_translation"]
    assert "in the plain of Megiddo" in by_ref["2 Chronicles 35:22"]["draft_translation"]
    assert "at the beginning of his reign" in by_ref["Ezra 4:6"]["draft_translation"]
    assert "in the reign of Ahasuerus" in by_ref["Ezra 4:6"]["draft_translation"]
    assert "on the mountains of Bethel" in by_ref["Song of Solomon 2:9"]["draft_translation"]
    assert "upon the mountains of Zion" in by_ref["Psalms 132:3"]["draft_translation"]
    assert by_ref["Ezekiel 39:4"]["draft_translation"].startswith("Upon the mountains of Israel")
    assert "over the land of Israel" in by_ref["Ezekiel 25:3"]["draft_translation"]
    assert "upon the land of Israel" in by_ref["Ezekiel 12:19"]["draft_translation"]
    assert "from the land of the north" in by_ref["Jeremiah 3:18"]["draft_translation"]
    assert "upon the land of the living" in by_ref["Ezekiel 26:20"]["draft_translation"]
    assert "from the face of the sword" in by_ref["Isaiah 31:8"]["draft_translation"]
    assert by_ref["Isaiah 40:12"]["draft_translation"] == (
        "Who measured the water with his hand and heaven with a span, and who set all the earth "
        "with a handful? Who set the mountains with a scale and the glens with a balance?"
    )
    assert "with a balance and with a bag of deceitful weights" in by_ref["Micah 6:11"]["draft_translation"]
    assert "the Lord stirred the spirit of Cyrus" in by_ref["Ezra 1:1"]["draft_translation"]
    assert "build for him a house in Jerusalem" in by_ref["2 Chronicles 36:23"]["draft_translation"]
    assert by_ref["Psalms 111:1"]["draft_translation"].startswith("Alleluia. Blessed is the man fearing the Lord")
    assert by_ref["Psalms 150:6"]["draft_translation"].endswith("Alleluia.")
    assert by_ref["Isaiah 31:9"]["draft_translation"].endswith(
        "Blessed is the one having seed in Zion and a household in Jerusalem."
    )
    assert by_ref["Psalms 65:20"]["draft_translation"].startswith("Blessed be God,")
    assert by_ref["Psalms 67:36"]["draft_translation"].endswith("Blessed be God.")
    assert "Blessed be the Lord" in by_ref["Zechariah 11:5"]["draft_translation"]
    assert by_ref["Proverbs 11:25"]["draft_translation"] == (
        "Every simple soul is blessed, but a hot-tempered man is unseemly."
    )
    assert "whose king is a son of nobles" in by_ref["Ecclesiastes 10:17"]["draft_translation"]
    assert by_ref["Daniel 12:12"]["draft_translation"].startswith("Blessed is the one remaining")
    assert "face of the earth" in by_ref["Psalms 1:4"]["draft_translation"]
    assert "ends of the earth" in by_ref["Psalms 2:8"]["draft_translation"]
    assert "from the end of the earth" in by_ref["Isaiah 5:26"]["draft_translation"]
    assert "From the ends of the earth" in by_ref["Psalms 60:3"]["draft_translation"]
    assert "from the face of the earth" in by_ref["Zephaniah 1:2"]["draft_translation"]
    assert "In the first year of Cyrus" in by_ref["2 Chronicles 36:22"]["draft_translation"]
    assert "in the second year of their coming" in by_ref["Ezra 3:8"]["draft_translation"]
    assert by_ref["Daniel 1:1"]["draft_translation"].startswith("In the third year")
    assert "on the first day of the seventh month" in by_ref["Nehemiah 8:2"]["draft_translation"]
    assert "from the first day until the last day" in by_ref["Nehemiah 8:18"]["draft_translation"]
    assert "in the sixth month, on the first day of the month" in by_ref["Haggai 1:1"]["draft_translation"]
    assert "from the days of Saul" in by_ref["1 Chronicles 13:3"]["draft_translation"]
    assert "into the hands of the Lord" in by_ref["1 Chronicles 21:13"]["draft_translation"]
    assert "into the hand of the king of Syria" in by_ref["2 Chronicles 28:5"]["draft_translation"]
    assert "in the law of Moses" in by_ref["2 Chronicles 23:18"]["draft_translation"]
    assert "according to the counsel of the rulers" in by_ref["Ezra 10:8"]["draft_translation"]
    assert "Attend to the voice of my petition" in by_ref["Psalms 5:3"]["draft_translation"]
    assert "as on the wings of eagles" in by_ref["Exodus 19:4"]["draft_translation"]
    assert "at the completion of these words" in by_ref["Daniel 4:28"]["draft_translation"]
    assert "in the name of God of Israel" in by_ref["Ezra 5:1"]["draft_translation"]
    assert "according to the number of tribes of Israel" in by_ref["Ezra 6:17"]["draft_translation"]
    assert "by the spirit of his mouth" in by_ref["Psalms 32:6"]["draft_translation"]
    assert "through the gates of Jerusalem" in by_ref["Lamentations 4:12"]["draft_translation"]
    assert "from the sons of Ham" in by_ref["1 Chronicles 4:40"]["draft_translation"]
    assert "to the sons of Shimei" in by_ref["1 Chronicles 23:10"]["draft_translation"]
    assert "from the daughters of the Canaanites" in by_ref["Genesis 24:3"]["draft_translation"]
    assert "in the cities of chariots" in by_ref["2 Chronicles 1:14"]["draft_translation"]
    assert "to the king of Achshaph" in by_ref["Joshua 11:1"]["draft_translation"]
    assert "in the valley of giants" in by_ref["1 Chronicles 11:15"]["draft_translation"]
    assert "to the man of God" in by_ref["1 Samuel 9:7"]["draft_translation"]
    assert "by the houses of their fathers" in by_ref["1 Chronicles 7:4"]["draft_translation"]
    assert "upon the house of your father" in by_ref["Isaiah 7:17"]["draft_translation"]
    assert "from the peoples of the lands" in by_ref["Ezra 3:3"]["draft_translation"]
    assert "upon the sons of men" in by_ref["Psalms 13:2"]["draft_translation"]
    assert "gave to the queen of Sheba" in by_ref["2 Chronicles 9:12"]["draft_translation"]
    assert "on the land of God" in by_ref["Isaiah 14:2"]["draft_translation"]
    assert "over the king of Babylon" in by_ref["Isaiah 14:4"]["draft_translation"]
    assert "according to the houses of their fathers" in by_ref["1 Chronicles 5:13"]["draft_translation"]
    assert "at the threshing floor of Araunah" in by_ref["1 Chronicles 21:15"]["draft_translation"]
    assert "from all the tribes of Israel" in by_ref["2 Chronicles 6:5"]["draft_translation"]
    assert "in the feast of unleavened bread" in by_ref["2 Chronicles 8:13"]["draft_translation"]
    assert by_ref["2 Chronicles 13:1"]["draft_translation"].startswith("In the eighteenth year")
    assert "priests from the people of the land" in by_ref["2 Chronicles 13:9"]["draft_translation"]
    assert "against the king of sons of Ammon" in by_ref["2 Chronicles 27:5"]["draft_translation"]
    assert "on the fourteenth of the second month" in by_ref["2 Chronicles 30:15"]["draft_translation"]
    assert "from the multitude of workers" in by_ref["Psalms 63:3"]["draft_translation"]
    assert "on the tops of mountains" in by_ref["Psalms 71:16"]["draft_translation"]
    assert "At the voice of one" in by_ref["Isaiah 30:17"]["draft_translation"]
    assert "from all the cities of Judah" in by_ref["2 Chronicles 14:4"]["draft_translation"]
    assert "against the cities of Israel" in by_ref["2 Chronicles 16:4"]["draft_translation"]
    assert "gave it to the seed of Abraham" in by_ref["2 Chronicles 20:7"]["draft_translation"]
    assert "against the inhabitants of Judah and Jerusalem" in by_ref["Ezra 4:6"]["draft_translation"]
    assert "to repair the house of the Lord" in by_ref["2 Chronicles 24:4"]["draft_translation"]
    assert "according to the purity of my hands" in by_ref["Psalms 17:21"]["draft_translation"]
    assert "from the edge of heaven" in by_ref["Nehemiah 1:9"]["draft_translation"]
    assert "from the rising of sun" in by_ref["Psalms 49:1"]["draft_translation"]
    assert "on the fifth of the month" in by_ref["Ezekiel 1:1"]["draft_translation"]
    assert "in the kingdom of Artaxerxes" in by_ref["Esther 9:20"]["draft_translation"]
    assert "through the broad place of the city" in by_ref["Esther 4:1"]["draft_translation"]
    assert "from the womb of my mother" in by_ref["Job 1:21"]["draft_translation"]
    assert "from the belly of my mother" in by_ref["Psalms 21:11"]["draft_translation"]
    assert "to hear the voice of praise" in by_ref["Psalms 25:7"]["draft_translation"]
    assert "in the hidden place of his tent" in by_ref["Psalms 26:5"]["draft_translation"]
    assert "into the depths of sea" in by_ref["Psalms 68:3"]["draft_translation"]
    assert "from the fat of wheat" in by_ref["Psalms 80:17"]["draft_translation"]
    assert "to all the beasts of the field" in by_ref["Psalms 103:11"]["draft_translation"]
    assert "from the fruit of your works" in by_ref["Psalms 103:13"]["draft_translation"]
    assert "from the wages of prostitute" in by_ref["Proverbs 19:13"]["draft_translation"]
    assert "from the glory of his strength" in by_ref["Isaiah 2:10"]["draft_translation"]
    assert "by the sword of man" in by_ref["Isaiah 31:8"]["draft_translation"]
    assert "on the road of fuller's field" in by_ref["Isaiah 36:2"]["draft_translation"]
    assert "Say to the daughter of Zion" in by_ref["Isaiah 62:11"]["draft_translation"]
    assert "At the last of days" in by_ref["Jeremiah 23:20"]["draft_translation"]
    assert "at the forecourt of the temple" in by_ref["Ezekiel 8:16"]["draft_translation"]
    assert "with the sons of the king" in by_ref["1 Chronicles 27:32"]["draft_translation"]
    assert "with the voice of gladness" in by_ref["1 Chronicles 15:16"]["draft_translation"]
    assert "with the words of peace" in by_ref["Numbers 21:21"]["draft_translation"]
    assert "with the weapons of war" in by_ref["Judges 18:11"]["draft_translation"]
    assert "to bring up the ark of the Lord" in by_ref["1 Chronicles 15:3"]["draft_translation"]
    assert "to carry the ark of God" in by_ref["1 Chronicles 15:2"]["draft_translation"]
    assert "from the half tribe of Manasseh" in by_ref["1 Chronicles 6:46"]["draft_translation"]
    assert "over the men of Israel" in by_ref["2 Chronicles 10:17"]["draft_translation"]
    assert "with the house of David" in by_ref["2 Chronicles 10:19"]["draft_translation"]
    assert "by the number of names" in by_ref["Numbers 26:53"]["draft_translation"]
    assert "from the brothers of Saul" in by_ref["1 Chronicles 12:2"]["draft_translation"]
    assert "to turn the kingdom of Saul" in by_ref["1 Chronicles 12:24"]["draft_translation"]
    assert "from the borders of Egypt" in by_ref["1 Chronicles 13:5"]["draft_translation"]
    assert "to enter the house of the Lord" in by_ref["1 Chronicles 24:19"]["draft_translation"]
    assert "into the holy of holies" in by_ref["2 Chronicles 4:22"]["draft_translation"]
    assert "against the kingdom of the Lord" in by_ref["2 Chronicles 13:8"]["draft_translation"]
    assert "in the commandments of his father" in by_ref["2 Chronicles 17:4"]["draft_translation"]
    assert "after the end of years" in by_ref["2 Chronicles 18:2"]["draft_translation"]
    assert "in the broad place of gate of Samaria" in by_ref["2 Chronicles 18:9"]["draft_translation"]
    assert "into the wilderness of Tekoa" in by_ref["2 Chronicles 20:20"]["draft_translation"]
    assert "to the valley of blessing" in by_ref["2 Chronicles 20:26"]["draft_translation"]
    assert "to strengthen the house of the Lord" in by_ref["2 Chronicles 24:5"]["draft_translation"]
    assert "after the death of Jehoiada" in by_ref["2 Chronicles 24:17"]["draft_translation"]
    assert "in the heat of anger" in by_ref["2 Chronicles 25:10"]["draft_translation"]
    assert "with the strength of power" in by_ref["2 Chronicles 26:13"]["draft_translation"]
    assert "into the torrent of Kidron" in by_ref["2 Chronicles 29:16"]["draft_translation"]
    assert "upon the words of Hezekiah" in by_ref["2 Chronicles 32:8"]["draft_translation"]
    assert "with the shame of face" in by_ref["2 Chronicles 32:21"]["draft_translation"]
    assert "from the height of his heart" in by_ref["2 Chronicles 32:26"]["draft_translation"]
    assert "before the king of Judah" in by_ref["2 Chronicles 34:24"]["draft_translation"]
    assert "into the treasury of the work" in by_ref["Ezra 2:69"]["draft_translation"]
    assert "upon the kingdom of the king" in by_ref["Ezra 7:23"]["draft_translation"]
    assert "from the chiefs of the priests" in by_ref["Ezra 8:24"]["draft_translation"]
    assert "with the peoples of the lands" in by_ref["Ezra 9:2"]["draft_translation"]
    assert "in the pillar of cloud" in by_ref["Nehemiah 9:12"]["draft_translation"]
    assert "under the hand of Hegai" in by_ref["Esther 2:8"]["draft_translation"]
    assert "with the oil of myrrh" in by_ref["Esther 2:12"]["draft_translation"]
    assert "to destroy the race of Mordecai" in by_ref["Esther 3:7"]["draft_translation"]
    assert "at the doors of inferiors" in by_ref["Job 5:4"]["draft_translation"]
    assert "by the words of your mouth" in by_ref["Job 15:5"]["draft_translation"]
    assert "from the country of Uz" in by_ref["Job 32:2"]["draft_translation"]
    assert "in the path of man" in by_ref["Job 34:11"]["draft_translation"]
    assert "in the counsel of ungodly men" in by_ref["Psalms 1:1"]["draft_translation"]
    assert "in the mercy of Most High" in by_ref["Psalms 20:8"]["draft_translation"]
    assert "with the assembly of vanity" in by_ref["Psalms 25:4"]["draft_translation"]
    assert "into the pit of corruption" in by_ref["Psalms 54:24"]["draft_translation"]
    assert "in the shadow of your wings" in by_ref["Psalms 56:2"]["draft_translation"]
    assert "from the depths of earth" in by_ref["Psalms 70:20"]["draft_translation"]
    assert "in the innocence of his heart" in by_ref["Psalms 77:72"]["draft_translation"]
    assert "Upon the ascent of Luhith" in by_ref["Isaiah 15:5"]["draft_translation"]
    assert "for a heifer is three years old" in by_ref["Isaiah 15:5"][
        "draft_translation"
    ]
    assert "on the way of Horonaim" in by_ref["Isaiah 15:5"]["draft_translation"]
    assert by_ref["Isaiah 15:1"]["draft_translation"].startswith(
        "The word against the Moabite land"
    )
    assert "The water of Rimmon" in by_ref["Isaiah 15:9"]["draft_translation"]
    assert "The fugitives of Moab" in by_ref["Isaiah 16:4"]["draft_translation"]
    assert "a throne will be set right" in by_ref["Isaiah 16:5"]["draft_translation"]
    assert "The fields of Heshbon" in by_ref["Isaiah 16:8"]["draft_translation"]
    assert "years of a hired worker" in by_ref["Isaiah 16:14"]["draft_translation"]
    assert by_ref["Isaiah 17:1"]["draft_translation"].startswith(
        "The word against Damascus"
    )
    assert "a fortress for Ephraim" in by_ref["Isaiah 17:3"]["draft_translation"]
    assert "a standing harvest" in by_ref["Isaiah 17:5"]["draft_translation"]
    assert "berries of an olive tree" in by_ref["Isaiah 17:6"]["draft_translation"]
    assert "the Amorites and the Hivites" in by_ref["Isaiah 17:9"][
        "draft_translation"
    ]
    assert "This is the portion" in by_ref["Isaiah 17:14"]["draft_translation"]
    assert "beyond the rivers of Ethiopia" in by_ref["Isaiah 18:1"][
        "draft_translation"
    ]
    assert "on the water" in by_ref["Isaiah 18:2"]["draft_translation"]
    assert "the light of noonday heat" in by_ref["Isaiah 18:4"][
        "draft_translation"
    ]
    assert "the birds of heaven and the beasts of the earth" in by_ref[
        "Isaiah 18:6"
    ]["draft_translation"]
    assert by_ref["Isaiah 19:1"]["draft_translation"].startswith(
        "A vision of Egypt"
    )
    assert "on a swift cloud" in by_ref["Isaiah 19:1"]["draft_translation"]
    assert "the spirit of the Egyptians" in by_ref["Isaiah 19:3"][
        "draft_translation"
    ]
    assert "water from the sea" in by_ref["Isaiah 19:5"]["draft_translation"]
    assert "the green rush" in by_ref["Isaiah 19:7"]["draft_translation"]
    assert "the princes of Zoan" in by_ref["Isaiah 19:11"]["draft_translation"]
    assert "a spirit of wandering" in by_ref["Isaiah 19:14"][
        "draft_translation"
    ]
    assert "the land of the Jews" in by_ref["Isaiah 19:17"]["draft_translation"]
    assert "an altar to the Lord" in by_ref["Isaiah 19:19"]["draft_translation"]
    assert "the Egyptians will know the Lord" in by_ref["Isaiah 19:21"][
        "draft_translation"
    ]
    assert "a way from Egypt to the Assyrians" in by_ref["Isaiah 19:23"][
        "draft_translation"
    ]
    assert "Blessed is my people" in by_ref["Isaiah 19:25"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 20:1"]["draft_translation"].startswith("In the year")
    assert "sent by Sargon king of the Assyrians" in by_ref["Isaiah 20:1"][
        "draft_translation"
    ]
    assert "the sackcloth off your waist" in by_ref["Isaiah 20:2"][
        "draft_translation"
    ]
    assert "the king of the Assyrians will lead the captivity" in by_ref[
        "Isaiah 20:4"
    ]["draft_translation"]
    assert by_ref["Isaiah 21:1"]["draft_translation"].startswith(
        "The vision of the wilderness"
    )
    assert "the envoys of the Persians" in by_ref["Isaiah 21:2"][
        "draft_translation"
    ]
    assert "set a watchman" in by_ref["Isaiah 21:6"]["draft_translation"]
    assert "a rider of a donkey" in by_ref["Isaiah 21:7"]["draft_translation"]
    assert "The vision of Edom" in by_ref["Isaiah 21:11"]["draft_translation"]
    assert "the glory of the sons of Kedar" in by_ref["Isaiah 21:16"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 22:1"]["draft_translation"].startswith(
        "The word of the valley of Zion"
    )
    assert "The city is full of shouting" in by_ref["Isaiah 22:2"][
        "draft_translation"
    ]
    assert "there is a day of trouble" in by_ref["Isaiah 22:5"][
        "draft_translation"
    ]
    assert "the hidden things of the houses" in by_ref["Isaiah 22:9"][
        "draft_translation"
    ]
    assert "Shebna the steward" in by_ref["Isaiah 22:15"]["draft_translation"]
    assert "a memorial in a high place" in by_ref["Isaiah 22:16"][
        "draft_translation"
    ]
    assert "as a father to the dwellers" in by_ref["Isaiah 22:21"][
        "draft_translation"
    ]
    assert "the glory of David" in by_ref["Isaiah 22:22"]["draft_translation"]
    assert by_ref["Isaiah 23:1"]["draft_translation"].startswith(
        "The vision of Tyre"
    )
    assert "the dwellers on the island" in by_ref["Isaiah 23:2"][
        "draft_translation"
    ]
    assert "the seed of traders as a harvest" in by_ref["Isaiah 23:3"][
        "draft_translation"
    ]
    assert "the land of the Chaldeans" in by_ref["Isaiah 23:13"][
        "draft_translation"
    ]
    assert "as the song of a prostitute" in by_ref["Isaiah 23:15"][
        "draft_translation"
    ]
    assert "all the kingdoms of the inhabited world" in by_ref["Isaiah 23:17"][
        "draft_translation"
    ]
    assert "destroys the inhabited world" in by_ref["Isaiah 24:1"][
        "draft_translation"
    ]
    assert "the buyer will be as the seller" in by_ref["Isaiah 24:2"][
        "draft_translation"
    ]
    assert "the everlasting covenant" in by_ref["Isaiah 24:5"][
        "draft_translation"
    ]
    assert "a curse will eat the land" in by_ref["Isaiah 24:6"][
        "draft_translation"
    ]
    assert "the glory of the Lord will be in the islands of the sea" in by_ref[
        "Isaiah 24:15"
    ]["draft_translation"]
    assert "O Lord, the God of Israel" in by_ref["Isaiah 24:15"][
        "draft_translation"
    ]
    assert "the one fleeing the fear" in by_ref["Isaiah 24:18"][
        "draft_translation"
    ]
    assert "like a fruit-watch hut" in by_ref["Isaiah 24:20"]["draft_translation"]
    assert "into a stronghold and into a prison" in by_ref["Isaiah 24:22"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 25:1"]["draft_translation"].startswith(
        "O Lord my God"
    )
    assert "the city of the ungodly" in by_ref["Isaiah 25:2"][
        "draft_translation"
    ]
    assert "the poor people will bless you" in by_ref["Isaiah 25:3"][
        "draft_translation"
    ]
    assert "a shelter for the thirsty ones" in by_ref["Isaiah 25:4"][
        "draft_translation"
    ]
    assert "all the nations on this mountain" in by_ref["Isaiah 25:6"][
        "draft_translation"
    ]
    assert "the reproach of the people" in by_ref["Isaiah 25:8"][
        "draft_translation"
    ]
    assert "the Moabite land" in by_ref["Isaiah 25:10"]["draft_translation"]
    assert "to the ground" in by_ref["Isaiah 25:12"]["draft_translation"]
    assert "Behold, a strong city" in by_ref["Isaiah 26:1"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 26:2"]["draft_translation"].startswith(
        "Open the gates"
    )
    assert "O Lord, forever, the great eternal God" in by_ref["Isaiah 26:4"][
        "draft_translation"
    ]
    assert "those dwelling on the heights" in by_ref["Isaiah 26:5"][
        "draft_translation"
    ]
    assert "upon the earth" in by_ref["Isaiah 26:9"]["draft_translation"]
    assert "For the ungodly ceased" in by_ref["Isaiah 26:10"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 26:11"]["draft_translation"].startswith("O Lord")
    assert "the dead certainly will not see life" in by_ref["Isaiah 26:14"][
        "draft_translation"
    ]
    assert "all the glorious ones of the earth" in by_ref["Isaiah 26:15"][
        "draft_translation"
    ]
    assert "In the womb we conceived" in by_ref["Isaiah 26:18"][
        "draft_translation"
    ]
    assert "those in the tombs" in by_ref["Isaiah 26:19"]["draft_translation"]
    assert "until the anger of the Lord passes" in by_ref["Isaiah 26:20"][
        "draft_translation"
    ]
    assert "the holy and great and strong sword" in by_ref["Isaiah 27:1"][
        "draft_translation"
    ]
    assert "the dragon, the fleeing serpent" in by_ref["Isaiah 27:1"][
        "draft_translation"
    ]
    assert "a beautiful vineyard" in by_ref["Isaiah 27:2"]["draft_translation"]
    assert "I, a strong city" in by_ref["Isaiah 27:3"]["draft_translation"]
    assert "the inhabited world will be filled" in by_ref["Isaiah 27:6"][
        "draft_translation"
    ]
    assert "the one plotting with the harsh spirit" in by_ref["Isaiah 27:8"][
        "draft_translation"
    ]
    assert "the lawlessness of Jacob" in by_ref["Isaiah 27:9"][
        "draft_translation"
    ]
    assert "all the stones of the altars" in by_ref["Isaiah 27:9"][
        "draft_translation"
    ]
    assert "as an abandoned flock" in by_ref["Isaiah 27:10"][
        "draft_translation"
    ]
    assert "not a people having understanding" in by_ref["Isaiah 27:11"][
        "draft_translation"
    ]
    assert "from the channel of the river" in by_ref["Isaiah 27:12"][
        "draft_translation"
    ]
    assert "with the great trumpet" in by_ref["Isaiah 27:13"][
        "draft_translation"
    ]
    assert "on the holy mountain in Jerusalem" in by_ref["Isaiah 27:13"][
        "draft_translation"
    ]
    assert "the crown of insolence" in by_ref["Isaiah 28:1"][
        "draft_translation"
    ]
    assert "the hired drinkers of Ephraim" in by_ref["Isaiah 28:1"][
        "draft_translation"
    ]
    assert "a force rushing down" in by_ref["Isaiah 28:2"]["draft_translation"]
    assert "will be trampled" in by_ref["Isaiah 28:3"]["draft_translation"]
    assert "the fallen flower" in by_ref["Isaiah 28:4"]["draft_translation"]
    assert "like an early fig" in by_ref["Isaiah 28:4"]["draft_translation"]
    assert "upon a spirit of judgment" in by_ref["Isaiah 28:6"][
        "draft_translation"
    ]
    assert "the priest and the prophet" in by_ref["Isaiah 28:7"][
        "draft_translation"
    ]
    assert "This is a vision" in by_ref["Isaiah 28:7"]["draft_translation"]
    assert "announce a message" in by_ref["Isaiah 28:9"]["draft_translation"]
    assert "The ones weaned from milk" in by_ref["Isaiah 28:9"][
        "draft_translation"
    ]
    assert "This rest to a hungry one" in by_ref["Isaiah 28:12"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 28:13"]["draft_translation"].startswith(
        "And the oracle of the Lord God"
    )
    assert "you afflicted men and rulers" in by_ref["Isaiah 28:14"][
        "draft_translation"
    ]
    assert "We made a covenant with Hades" in by_ref["Isaiah 28:15"][
        "draft_translation"
    ]
    assert "by a lie we will be covered" in by_ref["Isaiah 28:15"][
        "draft_translation"
    ]
    assert "a costly, chosen, precious cornerstone" in by_ref["Isaiah 28:16"][
        "draft_translation"
    ]
    assert "the one believing on him" in by_ref["Isaiah 28:16"][
        "draft_translation"
    ]
    assert "a storm certainly will not pass you by" in by_ref["Isaiah 28:17"][
        "draft_translation"
    ]
    assert "the covenant of death" in by_ref["Isaiah 28:18"][
        "draft_translation"
    ]
    assert "The hope will be evil" in by_ref["Isaiah 28:19"][
        "draft_translation"
    ]
    assert "a mountain of the ungodly" in by_ref["Isaiah 28:21"][
        "draft_translation"
    ]
    assert "a work of bitterness" in by_ref["Isaiah 28:21"][
        "draft_translation"
    ]
    assert "the completed and cut-short things" in by_ref["Isaiah 28:22"][
        "draft_translation"
    ]
    assert "Will the plowman plow the whole day" in by_ref["Isaiah 28:24"][
        "draft_translation"
    ]
    assert "with the judgment of your God" in by_ref["Isaiah 28:26"][
        "draft_translation"
    ]
    assert "For the black cumin" in by_ref["Isaiah 28:27"]["draft_translation"]
    assert "the voice of my bitterness" in by_ref["Isaiah 28:28"][
        "draft_translation"
    ]
    assert "from the Lord of hosts: the wonders" in by_ref["Isaiah 28:29"][
        "draft_translation"
    ]
    assert "its strength and its wealth" in by_ref["Isaiah 29:2"][
        "draft_translation"
    ]
    assert "throw a palisade around you" in by_ref["Isaiah 29:3"][
        "draft_translation"
    ]
    assert "humbled to the earth" in by_ref["Isaiah 29:4"]["draft_translation"]
    assert "dust from a wheel" in by_ref["Isaiah 29:5"]["draft_translation"]
    assert "there will be a visitation" in by_ref["Isaiah 29:6"][
        "draft_translation"
    ]
    assert "a storm carried along" in by_ref["Isaiah 29:6"][
        "draft_translation"
    ]
    assert "the wealth of all nations" in by_ref["Isaiah 29:7"][
        "draft_translation"
    ]
    assert "as a thirsty man dreams" in by_ref["Isaiah 29:8"][
        "draft_translation"
    ]
    assert "by a spirit of stupor" in by_ref["Isaiah 29:10"][
        "draft_translation"
    ]
    assert "as the words of this sealed book" in by_ref["Isaiah 29:11"][
        "draft_translation"
    ]
    assert "to a man knowing letters" in by_ref["Isaiah 29:11"][
        "draft_translation"
    ]
    assert "the hands of a man not knowing letters" in by_ref["Isaiah 29:12"][
        "draft_translation"
    ]
    assert "draws near to me with their lips" in by_ref["Isaiah 29:13"][
        "draft_translation"
    ]
    assert "the wisdom of the wise" in by_ref["Isaiah 29:14"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 29:15"]["draft_translation"].startswith(
        "Woe to those making counsel deep"
    )
    assert "the clay of the potter" in by_ref["Isaiah 29:16"][
        "draft_translation"
    ]
    assert "the thing formed say to the one forming" in by_ref["Isaiah 29:16"][
        "draft_translation"
    ]
    assert "as the mountain of Carmel" in by_ref["Isaiah 29:17"][
        "draft_translation"
    ]
    assert "the deaf will hear words of a book" in by_ref["Isaiah 29:18"][
        "draft_translation"
    ]
    assert "the poor will exult" in by_ref["Isaiah 29:19"][
        "draft_translation"
    ]
    assert "setting a stumbling block" in by_ref["Isaiah 29:21"][
        "draft_translation"
    ]
    assert "in the gates" in by_ref["Isaiah 29:21"]["draft_translation"]
    assert "change the face" in by_ref["Isaiah 29:22"]["draft_translation"]
    assert "the God of Israel" in by_ref["Isaiah 29:23"]["draft_translation"]
    assert "the stammering tongues" in by_ref["Isaiah 29:24"][
        "draft_translation"
    ]
    assert "sheltered under the Egyptians" in by_ref["Isaiah 30:2"][
        "draft_translation"
    ]
    assert "the shelter of Pharaoh" in by_ref["Isaiah 30:3"][
        "draft_translation"
    ]
    assert "leaders in Zoan" in by_ref["Isaiah 30:4"]["draft_translation"]
    assert "Toward a people" in by_ref["Isaiah 30:5"]["draft_translation"]
    assert by_ref["Isaiah 30:6"]["draft_translation"].startswith(
        "The vision of four-footed beasts"
    )
    assert "a lion and a lion's cub" in by_ref["Isaiah 30:6"][
        "draft_translation"
    ]
    assert "to a nation that will not benefit them" in by_ref["Isaiah 30:6"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 30:7"]["draft_translation"].startswith(
        "The Egyptians"
    )
    assert "in a book" in by_ref["Isaiah 30:8"]["draft_translation"]
    assert "this people is disobedient" in by_ref["Isaiah 30:9"][
        "draft_translation"
    ]
    assert "who say to the prophets" in by_ref["Isaiah 30:10"][
        "draft_translation"
    ]
    assert "vainly and emptily" in by_ref["Isaiah 30:7"]["draft_translation"]
    assert "as a wall falling suddenly" in by_ref["Isaiah 30:13"][
        "draft_translation"
    ]
    assert "of a strong city captured" in by_ref["Isaiah 30:13"][
        "draft_translation"
    ]
    assert "as the shattering of an earthen vessel" in by_ref["Isaiah 30:14"][
        "draft_translation"
    ]
    assert "one does not find a shard" in by_ref["Isaiah 30:14"][
        "draft_translation"
    ]
    assert "riders on the swift ones" in by_ref["Isaiah 30:16"][
        "draft_translation"
    ]
    assert "a thousand will flee" in by_ref["Isaiah 30:17"][
        "draft_translation"
    ]
    assert "as a mast on a mountain" in by_ref["Isaiah 30:17"][
        "draft_translation"
    ]
    assert "Blessed are the ones staying" in by_ref["Isaiah 30:18"][
        "draft_translation"
    ]
    assert "Because a holy people" in by_ref["Isaiah 30:19"][
        "draft_translation"
    ]
    assert "the ones leading you astray" in by_ref["Isaiah 30:20"][
        "draft_translation"
    ]
    assert "your ears will hear the words" in by_ref["Isaiah 30:21"][
        "draft_translation"
    ]
    assert "in a rich and spacious place" in by_ref["Isaiah 30:23"][
        "draft_translation"
    ]
    assert "the oxen working the land" in by_ref["Isaiah 30:24"][
        "draft_translation"
    ]
    assert "mixed with barley" in by_ref["Isaiah 30:24"]["draft_translation"]
    assert "water passing through" in by_ref["Isaiah 30:25"][
        "draft_translation"
    ]
    assert "the crushing of his people" in by_ref["Isaiah 30:26"][
        "draft_translation"
    ]
    assert "the pain of your blow" in by_ref["Isaiah 30:26"][
        "draft_translation"
    ]
    assert "his wrath is burning with glory" in by_ref["Isaiah 30:27"][
        "draft_translation"
    ]
    assert "The oracle of his lips" in by_ref["Isaiah 30:27"][
        "draft_translation"
    ]
    assert "in a ravine" in by_ref["Isaiah 30:28"]["draft_translation"]
    assert "up to the neck" in by_ref["Isaiah 30:28"]["draft_translation"]
    assert "trouble the nations" in by_ref["Isaiah 30:28"][
        "draft_translation"
    ]
    assert "with a flute" in by_ref["Isaiah 30:29"]["draft_translation"]
    assert "to the God of Israel" in by_ref["Isaiah 30:29"][
        "draft_translation"
    ]
    assert "the glory of his voice" in by_ref["Isaiah 30:30"][
        "draft_translation"
    ]
    assert "the wrath of his arm" in by_ref["Isaiah 30:30"][
        "draft_translation"
    ]
    assert "the Assyrians will be defeated by the blow" in by_ref[
        "Isaiah 30:31"
    ]["draft_translation"]
    assert "a deep ravine was prepared" in by_ref["Isaiah 30:33"][
        "draft_translation"
    ]
    assert "the wrath of the Lord is as a ravine" in by_ref["Isaiah 30:33"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 31:1"]["draft_translation"].startswith(
        "Woe to those going down"
    )
    assert "trusting in horses and in chariots" in by_ref["Isaiah 31:1"][
        "draft_translation"
    ]
    assert "against the houses of evil men" in by_ref["Isaiah 31:2"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 31:3"]["draft_translation"].startswith(
        "An Egyptian is a man and not God"
    )
    assert "horses are flesh" in by_ref["Isaiah 31:3"]["draft_translation"]
    assert "the helpers will tire" in by_ref["Isaiah 31:3"][
        "draft_translation"
    ]
    assert "As a lion or a lion's cub" in by_ref["Isaiah 31:4"][
        "draft_translation"
    ]
    assert "over the prey it took" in by_ref["Isaiah 31:4"][
        "draft_translation"
    ]
    assert "the mountains are filled" in by_ref["Isaiah 31:4"][
        "draft_translation"
    ]
    assert "the multitude of wrath is terrified" in by_ref["Isaiah 31:4"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 31:5"]["draft_translation"].startswith(
        "As flying birds"
    )
    assert "you who are counseling" in by_ref["Isaiah 31:6"][
        "draft_translation"
    ]
    assert "the men will reject their handmade things of silver and gold" in by_ref[
        "Isaiah 31:7"
    ]["draft_translation"]
    assert "nor will the sword of a human devour him" in by_ref["Isaiah 31:8"][
        "draft_translation"
    ]
    assert "the young men will be for defeat" in by_ref["Isaiah 31:8"][
        "draft_translation"
    ]
    assert "as by a trench around a rock" in by_ref["Isaiah 31:9"][
        "draft_translation"
    ]
    assert "but the one fleeing will be caught" in by_ref["Isaiah 31:9"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 32:1"]["draft_translation"].startswith(
        "For behold, a righteous king"
    )
    assert "as a glorious flowing river in a thirsty land" in by_ref[
        "Isaiah 32:2"
    ]["draft_translation"]
    assert "give their ears to hear" in by_ref["Isaiah 32:3"][
        "draft_translation"
    ]
    assert "the stammering tongues" in by_ref["Isaiah 32:4"][
        "draft_translation"
    ]
    assert "say to the fool" in by_ref["Isaiah 32:5"]["draft_translation"]
    assert by_ref["Isaiah 32:6"]["draft_translation"].startswith(
        "For the fool"
    )
    assert "make the thirsty souls empty" in by_ref["Isaiah 32:6"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 32:7"]["draft_translation"].startswith(
        "For the counsel of evil men"
    )
    assert "destroy the humble" in by_ref["Isaiah 32:7"]["draft_translation"]
    assert "words of the humble" in by_ref["Isaiah 32:7"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 32:8"]["draft_translation"].startswith(
        "But the godly men"
    )
    assert "days of a year" in by_ref["Isaiah 32:10"]["draft_translation"]
    assert "the vintage is spent, the seed ceased" in by_ref["Isaiah 32:10"][
        "draft_translation"
    ]
    assert "gird your loins with sackcloths" in by_ref["Isaiah 32:11"][
        "draft_translation"
    ]
    assert "on your breasts for a desired field" in by_ref["Isaiah 32:12"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 32:13"]["draft_translation"].endswith(
        "the rich city."
    )
    assert by_ref["Isaiah 32:14"]["draft_translation"].startswith(
        "The abandoned houses"
    )
    assert "the villages will be caves forever" in by_ref["Isaiah 32:14"][
        "draft_translation"
    ]
    assert "the joy of wild donkeys" in by_ref["Isaiah 32:14"][
        "draft_translation"
    ]
    assert "until a spirit from on high" in by_ref["Isaiah 32:15"][
        "draft_translation"
    ]
    assert "as a forest" in by_ref["Isaiah 32:15"]["draft_translation"]
    assert "if the hail comes down" in by_ref["Isaiah 32:19"][
        "draft_translation"
    ]
    assert "dwelling in the forests" in by_ref["Isaiah 32:19"][
        "draft_translation"
    ]
    assert "where an ox and a donkey do not tread" in by_ref["Isaiah 32:20"][
        "draft_translation"
    ]
    assert "as a moth on a garment" in by_ref["Isaiah 33:1"][
        "draft_translation"
    ]
    assert "from your fear the nations were scattered" in by_ref["Isaiah 33:3"][
        "draft_translation"
    ]
    assert "dwelling in the heights" in by_ref["Isaiah 33:5"][
        "draft_translation"
    ]
    assert "There are wisdom and knowledge and piety" in by_ref["Isaiah 33:6"][
        "draft_translation"
    ]
    assert "the fear of nations ceased" in by_ref["Isaiah 33:8"][
        "draft_translation"
    ]
    assert "the covenant with these is removed" in by_ref["Isaiah 33:8"][
        "draft_translation"
    ]
    assert "Sharon became a marsh" in by_ref["Isaiah 33:9"][
        "draft_translation"
    ]
    assert "The strength of your spirit" in by_ref["Isaiah 33:11"][
        "draft_translation"
    ]
    assert "a fire will devour you" in by_ref["Isaiah 33:11"][
        "draft_translation"
    ]
    assert "the nations will be burned as a thorn" in by_ref["Isaiah 33:12"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 33:13"]["draft_translation"].startswith(
        "The ones far away"
    )
    assert "the ones near will know my strength" in by_ref["Isaiah 33:13"][
        "draft_translation"
    ]
    assert "will seize the ungodly" in by_ref["Isaiah 33:14"][
        "draft_translation"
    ]
    assert "that a fire burns" in by_ref["Isaiah 33:14"]["draft_translation"]
    assert "speaking a straight way" in by_ref["Isaiah 33:15"][
        "draft_translation"
    ]
    assert "shaking his hands from gifts" in by_ref["Isaiah 33:15"][
        "draft_translation"
    ]
    assert "stopping his ears" in by_ref["Isaiah 33:15"][
        "draft_translation"
    ]
    assert "a cave of a strong rock" in by_ref["Isaiah 33:16"][
        "draft_translation"
    ]
    assert "his water will be faithful" in by_ref["Isaiah 33:16"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 33:17"]["draft_translation"].startswith(
        "You will see a king"
    )
    assert "see a land from far away" in by_ref["Isaiah 33:17"][
        "draft_translation"
    ]
    assert "meditate on fear" in by_ref["Isaiah 33:18"][
        "draft_translation"
    ]
    assert "Where are the scribes" in by_ref["Isaiah 33:18"][
        "draft_translation"
    ]
    assert "Where is the one counting" in by_ref["Isaiah 33:18"][
        "draft_translation"
    ]
    assert "a people despised" in by_ref["Isaiah 33:19"][
        "draft_translation"
    ]
    assert "to the listener" in by_ref["Isaiah 33:19"]["draft_translation"]
    assert "Zion, the city of our salvation" in by_ref["Isaiah 33:20"][
        "draft_translation"
    ]
    assert "Jerusalem, a rich city" in by_ref["Isaiah 33:20"][
        "draft_translation"
    ]
    assert "the pegs of her tent" in by_ref["Isaiah 33:20"][
        "draft_translation"
    ]
    assert "A ship under oars will not travel this way" in by_ref[
        "Isaiah 33:21"
    ]["draft_translation"]
    assert "loosen the sails" in by_ref["Isaiah 33:23"]["draft_translation"]
    assert "lift a signal" in by_ref["Isaiah 33:23"]["draft_translation"]
    assert "many lame ones" in by_ref["Isaiah 33:23"]["draft_translation"]
    assert "Let the earth and those in it hear" in by_ref["Isaiah 34:1"][
        "draft_translation"
    ]
    assert "the inhabited world and the people in it" in by_ref["Isaiah 34:1"][
        "draft_translation"
    ]
    assert "wrath of the Lord is upon all the nations" in by_ref["Isaiah 34:2"][
        "draft_translation"
    ]
    assert "the mountains will be soaked" in by_ref["Isaiah 34:3"][
        "draft_translation"
    ]
    assert "rolled like a book" in by_ref["Isaiah 34:4"][
        "draft_translation"
    ]
    assert "all the stars will fall" in by_ref["Isaiah 34:4"][
        "draft_translation"
    ]
    assert "from a fig tree" in by_ref["Isaiah 34:4"]["draft_translation"]
    assert "upon Edom it will come down" in by_ref["Isaiah 34:5"][
        "draft_translation"
    ]
    assert "upon the people of destruction" in by_ref["Isaiah 34:5"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 34:6"]["draft_translation"].startswith(
        "The sword of the Lord"
    )
    assert "in Bozrah and a great slaughter in Edom" in by_ref["Isaiah 34:6"][
        "draft_translation"
    ]
    assert "the mighty ones will fall" in by_ref["Isaiah 34:7"][
        "draft_translation"
    ]
    assert "the rams and the bulls" in by_ref["Isaiah 34:7"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 34:8"]["draft_translation"].startswith(
        "For it is the day"
    )
    assert "a measuring cord of desert" in by_ref["Isaiah 34:11"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 34:15"]["draft_translation"].startswith(
        "There a hedgehog"
    )
    assert "the earth kept her children" in by_ref["Isaiah 34:15"][
        "draft_translation"
    ]
    assert "let the wilderness exult and bloom as a lily" in by_ref[
        "Isaiah 35:1"
    ]["draft_translation"]
    assert "the deserts of the Jordan" in by_ref["Isaiah 35:2"][
        "draft_translation"
    ]
    assert "the height of God" in by_ref["Isaiah 35:2"]["draft_translation"]
    assert "Strengthen the loosened hands" in by_ref["Isaiah 35:3"][
        "draft_translation"
    ]
    assert "the ears of the deaf" in by_ref["Isaiah 35:5"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 35:6"]["draft_translation"].startswith(
        "Then the lame one"
    )
    assert "the tongue of stammerers" in by_ref["Isaiah 35:6"][
        "draft_translation"
    ]
    assert "a ravine in a thirsty land" in by_ref["Isaiah 35:6"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 35:7"]["draft_translation"].startswith(
        "And the dry place"
    )
    assert "in the thirsty land" in by_ref["Isaiah 35:7"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 35:8"]["draft_translation"].startswith(
        "There will be a pure way"
    )
    assert "called a holy way" in by_ref["Isaiah 35:8"]["draft_translation"]
    assert "an unclean one" in by_ref["Isaiah 35:8"]["draft_translation"]
    assert "the scattered ones" in by_ref["Isaiah 35:8"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 35:9"]["draft_translation"].startswith(
        "And a lion"
    )
    assert "any of the evil beasts" in by_ref["Isaiah 35:9"][
        "draft_translation"
    ]
    assert "eternal gladness will be over their heads" in by_ref[
        "Isaiah 35:10"
    ]["draft_translation"]
    assert "in the fourteenth year of the reign of Hezekiah" in by_ref[
        "Isaiah 36:1"
    ]["draft_translation"]
    assert "against the fortified cities of Judah" in by_ref["Isaiah 36:1"][
        "draft_translation"
    ]
    assert "with a great force" in by_ref["Isaiah 36:2"][
        "draft_translation"
    ]
    assert "by the conduit of the upper pool" in by_ref["Isaiah 36:2"][
        "draft_translation"
    ]
    assert "Shebna the scribe" in by_ref["Isaiah 36:3"]["draft_translation"]
    assert "Thus says the great king" in by_ref["Isaiah 36:4"][
        "draft_translation"
    ]
    assert "Is a battle-line made" in by_ref["Isaiah 36:5"][
        "draft_translation"
    ]
    assert "all those trusting on him" in by_ref["Isaiah 36:6"][
        "draft_translation"
    ]
    assert "make a bargain with my lord" in by_ref["Isaiah 36:8"][
        "draft_translation"
    ]
    assert "the king of the Assyrians" in by_ref["Isaiah 36:8"][
        "draft_translation"
    ]
    assert "turn away the face of one governor" in by_ref["Isaiah 36:9"][
        "draft_translation"
    ]
    assert "The ones trusting in the Egyptians" in by_ref["Isaiah 36:9"][
        "draft_translation"
    ]
    assert "ears of the men on the wall" in by_ref["Isaiah 36:11"][
        "draft_translation"
    ]
    assert "to the men sitting on the wall" in by_ref["Isaiah 36:12"][
        "draft_translation"
    ]
    assert "with a great voice" in by_ref["Isaiah 36:13"][
        "draft_translation"
    ]
    assert "Hear the words of the great king" in by_ref["Isaiah 36:13"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 36:14"]["draft_translation"].startswith(
        "Thus says the king"
    )
    assert "Thus says the king of the Assyrians" in by_ref["Isaiah 36:16"][
        "draft_translation"
    ]
    assert "eat each one his vine and his figs" in by_ref["Isaiah 36:16"][
        "draft_translation"
    ]
    assert "a land of grain and wine" in by_ref["Isaiah 36:17"][
        "draft_translation"
    ]
    assert "the gods of the nations" in by_ref["Isaiah 36:18"][
        "draft_translation"
    ]
    assert "the god of Hamath and Arpad" in by_ref["Isaiah 36:19"][
        "draft_translation"
    ]
    assert "the god of the city of Sepharvaim" in by_ref["Isaiah 36:19"][
        "draft_translation"
    ]
    assert "all the gods of these nations" in by_ref["Isaiah 36:20"][
        "draft_translation"
    ]
    assert "the God of Jerusalem" in by_ref["Isaiah 36:20"][
        "draft_translation"
    ]
    assert "answered him a word" in by_ref["Isaiah 36:21"][
        "draft_translation"
    ]
    assert "Shebna the scribe of force" in by_ref["Isaiah 36:22"][
        "draft_translation"
    ]
    assert "tearing their tunics" in by_ref["Isaiah 36:22"][
        "draft_translation"
    ]
    assert "tore his garments" in by_ref["Isaiah 37:1"]["draft_translation"]
    assert "the elders of the priests" in by_ref["Isaiah 37:2"][
        "draft_translation"
    ]
    assert "hear the words of Rabshakeh" in by_ref["Isaiah 37:4"][
        "draft_translation"
    ]
    assert "the living God" in by_ref["Isaiah 37:4"]["draft_translation"]
    assert "the envoys of the king of the Assyrians" in by_ref[
        "Isaiah 37:6"
    ]["draft_translation"]
    assert "I cast a spirit into him" in by_ref["Isaiah 37:7"][
        "draft_translation"
    ]
    assert "hearing a report" in by_ref["Isaiah 37:7"]["draft_translation"]
    assert "found the king besieging Libnah" in by_ref["Isaiah 37:8"][
        "draft_translation"
    ]
    assert "Tirhakah king of the Ethiopians" in by_ref["Isaiah 37:9"][
        "draft_translation"
    ]
    assert "how they destroyed it" in by_ref["Isaiah 37:11"][
        "draft_translation"
    ]
    assert "the gods of the nations" in by_ref["Isaiah 37:12"][
        "draft_translation"
    ]
    assert "Rezeph which are in the land of Theemath" in by_ref[
        "Isaiah 37:12"
    ]["draft_translation"]
    assert "the kings of Hamath and Arpad" in by_ref["Isaiah 37:13"][
        "draft_translation"
    ]
    assert "the city of Sepharvaim, Hena, Ivvah" in by_ref[
        "Isaiah 37:13"
    ]["draft_translation"]
    assert "took the book from the messengers" in by_ref["Isaiah 37:14"][
        "draft_translation"
    ]
    assert "the one sitting upon the cherubim" in by_ref["Isaiah 37:16"][
        "draft_translation"
    ]
    assert "every kingdom of the inhabited world" in by_ref["Isaiah 37:16"][
        "draft_translation"
    ]
    assert "see the words which Sennacherib sent" in by_ref[
        "Isaiah 37:17"
    ]["draft_translation"]
    assert "the kings of the Assyrians made the whole inhabited world" in by_ref[
        "Isaiah 37:18"
    ]["draft_translation"]
    assert "into the fire" in by_ref["Isaiah 37:19"]["draft_translation"]
    assert "every kingdom of the earth" in by_ref["Isaiah 37:20"][
        "draft_translation"
    ]
    assert "The virgin daughter Zion" in by_ref["Isaiah 37:22"][
        "draft_translation"
    ]
    assert "the daughter Jerusalem shook her head" in by_ref[
        "Isaiah 37:22"
    ]["draft_translation"]
    assert "you reproached the Lord" in by_ref["Isaiah 37:24"][
        "draft_translation"
    ]
    assert "the far parts of Lebanon" in by_ref["Isaiah 37:24"][
        "draft_translation"
    ]
    assert "I set a bridge" in by_ref["Isaiah 37:25"]["draft_translation"]
    assert "lay the nations waste" in by_ref["Isaiah 37:26"][
        "draft_translation"
    ]
    assert "the dwellers in fortified cities" in by_ref["Isaiah 37:26"][
        "draft_translation"
    ]
    assert "I let go the hands" in by_ref["Isaiah 37:27"][
        "draft_translation"
    ]
    assert "put a hook into your nose and a bridle" in by_ref[
        "Isaiah 37:29"
    ]["draft_translation"]
    assert "this is the sign to you" in by_ref["Isaiah 37:30"][
        "draft_translation"
    ]
    assert "in the second year the remnant" in by_ref["Isaiah 37:30"][
        "draft_translation"
    ]
    assert "put forth a root down" in by_ref["Isaiah 37:31"][
        "draft_translation"
    ]
    assert "the ones left will go out" in by_ref["Isaiah 37:32"][
        "draft_translation"
    ]
    assert "concerning the king of the Assyrians" in by_ref[
        "Isaiah 37:33"
    ]["draft_translation"]
    assert "cast an arrow" in by_ref["Isaiah 37:33"]["draft_translation"]
    assert "bring a shield" in by_ref["Isaiah 37:33"]["draft_translation"]
    assert "circle a palisade" in by_ref["Isaiah 37:33"]["draft_translation"]
    assert by_ref["Isaiah 37:34"]["draft_translation"].startswith(
        "But by the way"
    )
    assert "from the camp of the Assyrians" in by_ref["Isaiah 37:36"][
        "draft_translation"
    ]
    assert "all the bodies dead" in by_ref["Isaiah 37:36"][
        "draft_translation"
    ]
    assert "Nisroch his ancestral god" in by_ref["Isaiah 37:38"][
        "draft_translation"
    ]
    assert "Adrammelech and Sharezer" in by_ref["Isaiah 37:38"][
        "draft_translation"
    ]
    assert "happened at that time" in by_ref["Isaiah 38:1"][
        "draft_translation"
    ]
    assert "toward the wall" in by_ref["Isaiah 38:2"]["draft_translation"]
    assert "in a true heart" in by_ref["Isaiah 38:3"]["draft_translation"]
    assert "the pleasing things" in by_ref["Isaiah 38:3"][
        "draft_translation"
    ]
    assert "this is the sign to you" in by_ref["Isaiah 38:7"][
        "draft_translation"
    ]
    assert "the shadow of the stair-steps" in by_ref["Isaiah 38:8"][
        "draft_translation"
    ]
    assert "the sun went up the ten steps" in by_ref["Isaiah 38:8"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 38:9"]["draft_translation"].startswith(
        "A prayer of Hezekiah"
    )
    assert "In the height of my days" in by_ref["Isaiah 38:10"][
        "draft_translation"
    ]
    assert "the remaining years" in by_ref["Isaiah 38:10"][
        "draft_translation"
    ]
    assert "the salvation of God on the earth" in by_ref["Isaiah 38:11"][
        "draft_translation"
    ]
    assert "see a man" in by_ref["Isaiah 38:11"]["draft_translation"]
    assert "the remnant of my life" in by_ref["Isaiah 38:12"][
        "draft_translation"
    ]
    assert "as one striking a tent" in by_ref["Isaiah 38:12"][
        "draft_translation"
    ]
    assert "as a weaver's web" in by_ref["Isaiah 38:12"][
        "draft_translation"
    ]
    assert "from the day until the night" in by_ref["Isaiah 38:13"][
        "draft_translation"
    ]
    assert "As a swallow" in by_ref["Isaiah 38:14"]["draft_translation"]
    assert "as a dove" in by_ref["Isaiah 38:14"]["draft_translation"]
    assert "the pain of my soul" in by_ref["Isaiah 38:15"][
        "draft_translation"
    ]
    assert "nor will the dead bless you" in by_ref["Isaiah 38:18"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 38:19"]["draft_translation"].startswith(
        "The living ones"
    )
    assert "with a psaltery all the days of my life" in by_ref[
        "Isaiah 38:20"
    ]["draft_translation"]
    assert "Take a cake of figs" in by_ref["Isaiah 38:21"][
        "draft_translation"
    ]
    assert "This is the sign" in by_ref["Isaiah 38:22"]["draft_translation"]
    assert "he heard that he grew weak" in by_ref["Isaiah 39:1"][
        "draft_translation"
    ]
    assert "the house of perfumes" in by_ref["Isaiah 39:2"][
        "draft_translation"
    ]
    assert "all the houses of the vessels of the treasury" in by_ref[
        "Isaiah 39:2"
    ]["draft_translation"]
    assert "From a far land" in by_ref["Isaiah 39:3"]["draft_translation"]
    assert "all the things in my house" in by_ref["Isaiah 39:4"][
        "draft_translation"
    ]
    assert "the things in my treasures" in by_ref["Isaiah 39:4"][
        "draft_translation"
    ]
    assert "the days are coming" in by_ref["Isaiah 39:6"][
        "draft_translation"
    ]
    assert "all the things in your house" in by_ref["Isaiah 39:6"][
        "draft_translation"
    ]
    assert "the king of the Babylonians" in by_ref["Isaiah 39:7"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 39:8"]["draft_translation"].startswith(
        "And Hezekiah said to Isaiah, The word of the Lord"
    )
    assert "make straight the paths of our God" in by_ref["Isaiah 40:3"][
        "draft_translation"
    ]
    assert "all the crooked things will become straight" in by_ref[
        "Isaiah 40:4"
    ]["draft_translation"]
    assert "the rough things into plains" in by_ref["Isaiah 40:4"][
        "draft_translation"
    ]
    assert "the salvation of God" in by_ref["Isaiah 40:5"][
        "draft_translation"
    ]
    assert "all the glory of man is as a flower of grass" in by_ref[
        "Isaiah 40:6"
    ]["draft_translation"]
    assert "The grass dried up and the flower fell" in by_ref[
        "Isaiah 40:7"
    ]["draft_translation"]
    assert by_ref["Isaiah 40:9"]["draft_translation"].startswith(
        "Go up on a high mountain"
    )
    assert "the one bringing good news to Zion" in by_ref["Isaiah 40:9"][
        "draft_translation"
    ]
    assert "his wage is with him and his work before him" in by_ref[
        "Isaiah 40:10"
    ]["draft_translation"]
    assert by_ref["Isaiah 40:11"]["draft_translation"].startswith(
        "As a shepherd"
    )
    assert "those carrying in the womb" in by_ref["Isaiah 40:11"][
        "draft_translation"
    ]
    assert "Who measured the water" in by_ref["Isaiah 40:12"][
        "draft_translation"
    ]
    assert "Who set the mountains" in by_ref["Isaiah 40:12"][
        "draft_translation"
    ]
    assert "the mind of the Lord" in by_ref["Isaiah 40:13"][
        "draft_translation"
    ]
    assert "the way of understanding" in by_ref["Isaiah 40:14"][
        "draft_translation"
    ]
    assert "all the nations were reckoned as a drop from a bucket" in by_ref[
        "Isaiah 40:15"
    ]["draft_translation"]
    assert "Lebanon is not enough for burning" in by_ref["Isaiah 40:16"][
        "draft_translation"
    ]
    assert "all the four-footed animals" in by_ref["Isaiah 40:16"][
        "draft_translation"
    ]
    assert "a whole burnt offering" in by_ref["Isaiah 40:16"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 40:17"]["draft_translation"].startswith(
        "And all the nations"
    )
    assert "liken the Lord" in by_ref["Isaiah 40:18"]["draft_translation"]
    assert "a craftsman make an image" in by_ref["Isaiah 40:19"][
        "draft_translation"
    ]
    assert "construct a likeness" in by_ref["Isaiah 40:19"][
        "draft_translation"
    ]
    assert "a craftsman wisely seeks" in by_ref["Isaiah 40:20"][
        "draft_translation"
    ]
    assert "the foundations of the earth" in by_ref["Isaiah 40:21"][
        "draft_translation"
    ]
    assert "The one holding the circuit of the earth" in by_ref[
        "Isaiah 40:22"
    ]["draft_translation"]
    assert "heaven as a vault" in by_ref["Isaiah 40:22"][
        "draft_translation"
    ]
    assert "made the earth as nothing" in by_ref["Isaiah 40:23"][
        "draft_translation"
    ]
    assert "take root in the earth" in by_ref["Isaiah 40:24"][
        "draft_translation"
    ]
    assert "a storm will take them up" in by_ref["Isaiah 40:24"][
        "draft_translation"
    ]
    assert "Lift your eyes on high" in by_ref["Isaiah 40:26"][
        "draft_translation"
    ]
    assert "the one bringing out his array" in by_ref["Isaiah 40:26"][
        "draft_translation"
    ]
    assert "The eternal God" in by_ref["Isaiah 40:28"][
        "draft_translation"
    ]
    assert "the God who prepared the ends of the earth" in by_ref[
        "Isaiah 40:28"
    ]["draft_translation"]
    assert "the hungry ones" in by_ref["Isaiah 40:29"]["draft_translation"]
    assert "the young men will hunger" in by_ref["Isaiah 40:30"][
        "draft_translation"
    ]
    assert "the chosen youths" in by_ref["Isaiah 40:30"][
        "draft_translation"
    ]
    assert "grow wings like eagles" in by_ref["Isaiah 40:31"][
        "draft_translation"
    ]
    assert "for the rulers will change strength" in by_ref["Isaiah 41:1"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 41:2"]["draft_translation"].startswith(
        "Who raised righteousness from the east"
    )
    assert "their swords into the earth" in by_ref["Isaiah 41:2"][
        "draft_translation"
    ]
    assert "the way of his feet" in by_ref["Isaiah 41:3"][
        "draft_translation"
    ]
    assert "from the generations of beginning" in by_ref["Isaiah 41:4"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 41:5"]["draft_translation"].startswith(
        "The nations saw"
    )
    assert "the ends of the earth" in by_ref["Isaiah 41:5"][
        "draft_translation"
    ]
    assert "Each one judging for his neighbor" in by_ref["Isaiah 41:6"][
        "draft_translation"
    ]
    assert "saying to his brother" in by_ref["Isaiah 41:6"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 41:7"]["draft_translation"].startswith(
        "A craftsman"
    )
    assert "with a hammer" in by_ref["Isaiah 41:7"]["draft_translation"]
    assert "The joint is good" in by_ref["Isaiah 41:7"]["draft_translation"]
    assert "the seed of Abraham" in by_ref["Isaiah 41:8"][
        "draft_translation"
    ]
    assert "from the edges of the earth" in by_ref["Isaiah 41:9"][
        "draft_translation"
    ]
    assert "the one strengthening you" in by_ref["Isaiah 41:10"][
        "draft_translation"
    ]
    assert "all those opposing you" in by_ref["Isaiah 41:11"][
        "draft_translation"
    ]
    assert "the men who rage against you" in by_ref["Isaiah 41:12"][
        "draft_translation"
    ]
    assert "the ones fighting against you" in by_ref["Isaiah 41:12"][
        "draft_translation"
    ]
    assert "the one holding your right hand" in by_ref["Isaiah 41:13"][
        "draft_translation"
    ]
    assert "wheels of a wagon" in by_ref["Isaiah 41:15"][
        "draft_translation"
    ]
    assert "thresh the mountains" in by_ref["Isaiah 41:15"][
        "draft_translation"
    ]
    assert "make the hills fine" in by_ref["Isaiah 41:15"][
        "draft_translation"
    ]
    assert "a wind will take them and a storm" in by_ref["Isaiah 41:16"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 41:17"]["draft_translation"].startswith(
        "For the poor and the needy"
    )
    assert "the God of Israel" in by_ref["Isaiah 41:17"]["draft_translation"]
    assert "on the mountains" in by_ref["Isaiah 41:18"]["draft_translation"]
    assert "the wilderness into marshes" in by_ref["Isaiah 41:18"][
        "draft_translation"
    ]
    assert "the thirsty land into aqueducts" in by_ref["Isaiah 41:18"][
        "draft_translation"
    ]
    assert "a cedar and a box tree" in by_ref["Isaiah 41:19"][
        "draft_translation"
    ]
    assert "in the dry land" in by_ref["Isaiah 41:19"]["draft_translation"]
    assert "the hand of the Lord" in by_ref["Isaiah 41:20"][
        "draft_translation"
    ]
    assert "the king of Jacob" in by_ref["Isaiah 41:21"][
        "draft_translation"
    ]
    assert "what the former things were" in by_ref["Isaiah 41:22"][
        "draft_translation"
    ]
    assert "what the last things are" in by_ref["Isaiah 41:22"][
        "draft_translation"
    ]
    assert "the things coming" in by_ref["Isaiah 41:22"][
        "draft_translation"
    ]
    assert "the things coming at the end" in by_ref["Isaiah 41:23"][
        "draft_translation"
    ]
    assert "from where is your work" in by_ref["Isaiah 41:24"][
        "draft_translation"
    ]
    assert "as an abomination" in by_ref["Isaiah 41:24"][
        "draft_translation"
    ]
    assert "from the north" in by_ref["Isaiah 41:25"]["draft_translation"]
    assert "from the east of the sun" in by_ref["Isaiah 41:25"][
        "draft_translation"
    ]
    assert "Let the rulers come" in by_ref["Isaiah 41:25"][
        "draft_translation"
    ]
    assert "a potter treading the clay" in by_ref["Isaiah 41:25"][
        "draft_translation"
    ]
    assert "the things from the beginning" in by_ref["Isaiah 41:26"][
        "draft_translation"
    ]
    assert "the things before" in by_ref["Isaiah 41:26"][
        "draft_translation"
    ]
    assert "a beginning to Zion" in by_ref["Isaiah 41:27"][
        "draft_translation"
    ]
    assert "for the way" in by_ref["Isaiah 41:27"]["draft_translation"]
    assert by_ref["Isaiah 41:28"]["draft_translation"].startswith(
        "For from the nations"
    )
    assert "from where they are" in by_ref["Isaiah 41:28"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 41:29"]["draft_translation"].startswith(
        "For the ones making you"
    )
    assert "the ones leading you astray" in by_ref["Isaiah 41:29"][
        "draft_translation"
    ]
    assert "judgment to the nations" in by_ref["Isaiah 42:1"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 42:3"]["draft_translation"].startswith(
        "A crushed reed"
    )
    assert "in truth he will bring judgment" in by_ref["Isaiah 42:3"][
        "draft_translation"
    ]
    assert "upon the earth" in by_ref["Isaiah 42:4"]["draft_translation"]
    assert "the nations will hope in his name" in by_ref["Isaiah 42:4"][
        "draft_translation"
    ]
    assert "the one making heaven" in by_ref["Isaiah 42:5"][
        "draft_translation"
    ]
    assert "the one establishing the earth" in by_ref["Isaiah 42:5"][
        "draft_translation"
    ]
    assert "the things in it" in by_ref["Isaiah 42:5"]["draft_translation"]
    assert "breath to the people" in by_ref["Isaiah 42:5"][
        "draft_translation"
    ]
    assert "into a covenant of a race" in by_ref["Isaiah 42:6"][
        "draft_translation"
    ]
    assert "into a light of nations" in by_ref["Isaiah 42:6"][
        "draft_translation"
    ]
    assert "open the eyes of the blind" in by_ref["Isaiah 42:7"][
        "draft_translation"
    ]
    assert "out of a prison house" in by_ref["Isaiah 42:7"][
        "draft_translation"
    ]
    assert "this is my name" in by_ref["Isaiah 42:8"]["draft_translation"]
    assert "to the carved things" in by_ref["Isaiah 42:8"][
        "draft_translation"
    ]
    assert "the former things came" in by_ref["Isaiah 42:9"][
        "draft_translation"
    ]
    assert "the new things" in by_ref["Isaiah 42:9"]["draft_translation"]
    assert "a new hymn" in by_ref["Isaiah 42:10"]["draft_translation"]
    assert "into the sea" in by_ref["Isaiah 42:10"]["draft_translation"]
    assert "the islands and those dwelling in them" in by_ref["Isaiah 42:10"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 42:11"]["draft_translation"].startswith(
        "Rejoice, the wilderness"
    )
    assert "the dwellers in Kedar" in by_ref["Isaiah 42:11"][
        "draft_translation"
    ]
    assert "from the tops of the mountains" in by_ref["Isaiah 42:11"][
        "draft_translation"
    ]
    assert "in the islands" in by_ref["Isaiah 42:12"]["draft_translation"]
    assert "As a woman giving birth" in by_ref["Isaiah 42:14"][
        "draft_translation"
    ]
    assert "dry up marshes" in by_ref["Isaiah 42:15"]["draft_translation"]
    assert "the darkness for them into light" in by_ref["Isaiah 42:16"][
        "draft_translation"
    ]
    assert "the crooked things into straight things" in by_ref["Isaiah 42:16"][
        "draft_translation"
    ]
    assert "the ones trusting in the carved things" in by_ref["Isaiah 42:17"][
        "draft_translation"
    ]
    assert "the ones saying to the molten images" in by_ref["Isaiah 42:17"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 42:18"]["draft_translation"].startswith(
        "The deaf ones"
    )
    assert "the blind ones" in by_ref["Isaiah 42:18"]["draft_translation"]
    assert "who is blind" in by_ref["Isaiah 42:19"]["draft_translation"]
    assert "the ones ruling them" in by_ref["Isaiah 42:19"][
        "draft_translation"
    ]
    assert "the ears were opened" in by_ref["Isaiah 42:20"][
        "draft_translation"
    ]
    assert "wanted him to be justified" in by_ref["Isaiah 42:21"][
        "draft_translation"
    ]
    assert "the snare was in the storerooms" in by_ref["Isaiah 42:22"][
        "draft_translation"
    ]
    assert "there was no one rescuing" in by_ref["Isaiah 42:22"][
        "draft_translation"
    ]
    assert "no one saying, Give back" in by_ref["Isaiah 42:22"][
        "draft_translation"
    ]
    assert "the things coming" in by_ref["Isaiah 42:23"][
        "draft_translation"
    ]
    assert "the ones spoiling him" in by_ref["Isaiah 42:24"][
        "draft_translation"
    ]
    assert "the anger of his wrath" in by_ref["Isaiah 42:25"][
        "draft_translation"
    ]
    assert "the ones burning them around" in by_ref["Isaiah 42:25"][
        "draft_translation"
    ]
    assert "each of them" in by_ref["Isaiah 42:25"]["draft_translation"]
    assert "his soul" in by_ref["Isaiah 42:25"]["draft_translation"]
    assert "the one making you" in by_ref["Isaiah 43:1"][
        "draft_translation"
    ]
    assert "the one forming you" in by_ref["Isaiah 43:1"][
        "draft_translation"
    ]
    assert "a flame will not burn you" in by_ref["Isaiah 43:2"][
        "draft_translation"
    ]
    assert "the one saving you" in by_ref["Isaiah 43:3"][
        "draft_translation"
    ]
    assert "From the east" in by_ref["Isaiah 43:5"]["draft_translation"]
    assert "from the west" in by_ref["Isaiah 43:5"]["draft_translation"]
    assert "to the north" in by_ref["Isaiah 43:6"]["draft_translation"]
    assert "to the south" in by_ref["Isaiah 43:6"]["draft_translation"]
    assert "from a far land" in by_ref["Isaiah 43:6"]["draft_translation"]
    assert "a blind people" in by_ref["Isaiah 43:8"]["draft_translation"]
    assert "deaf ones having ears" in by_ref["Isaiah 43:8"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 43:9"]["draft_translation"].startswith(
        "All the nations"
    )
    assert "the things from the beginning" in by_ref["Isaiah 43:9"][
        "draft_translation"
    ]
    assert "say true things" in by_ref["Isaiah 43:9"]["draft_translation"]
    assert "the servant whom I chose" in by_ref["Isaiah 43:10"][
        "draft_translation"
    ]
    assert "no one rescuing" in by_ref["Isaiah 43:13"]["draft_translation"]
    assert "the one redeeming you" in by_ref["Isaiah 43:14"][
        "draft_translation"
    ]
    assert "all the fugitives" in by_ref["Isaiah 43:14"][
        "draft_translation"
    ]
    assert "the Chaldeans" in by_ref["Isaiah 43:14"]["draft_translation"]
    assert "the one showing Israel" in by_ref["Isaiah 43:15"][
        "draft_translation"
    ]
    assert "the one giving a way in the sea" in by_ref["Isaiah 43:16"][
        "draft_translation"
    ]
    assert "a path in strong water" in by_ref["Isaiah 43:16"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 43:17"]["draft_translation"].startswith(
        "the one bringing out chariots"
    )
    assert "a strong crowd" in by_ref["Isaiah 43:17"]["draft_translation"]
    assert "the former things" in by_ref["Isaiah 43:18"][
        "draft_translation"
    ]
    assert "the ancient things" in by_ref["Isaiah 43:18"][
        "draft_translation"
    ]
    assert "the new things" in by_ref["Isaiah 43:19"]["draft_translation"]
    assert "in the dry land rivers" in by_ref["Isaiah 43:19"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 43:20"]["draft_translation"].startswith(
        "The beasts of the field"
    )
    assert "rivers in the dry land" in by_ref["Isaiah 43:20"][
        "draft_translation"
    ]
    assert "your burnt offering" in by_ref["Isaiah 43:23"][
        "draft_translation"
    ]
    assert "the fat of your sacrifices" in by_ref["Isaiah 43:24"][
        "draft_translation"
    ]
    assert "the one wiping out your lawlessnesses" in by_ref["Isaiah 43:25"][
        "draft_translation"
    ]
    assert by_ref["Isaiah 43:28"]["draft_translation"].startswith(
        "And the rulers"
    )
    assert "the one making you" in by_ref["Isaiah 44:2"][
        "draft_translation"
    ]
    assert "the one forming you from the womb" in by_ref["Isaiah 44:2"][
        "draft_translation"
    ]
    assert "to the ones going in dry land" in by_ref["Isaiah 44:3"][
        "draft_translation"
    ]
    assert "like a willow" in by_ref["Isaiah 44:4"]["draft_translation"]
    assert "the king of Israel" in by_ref["Isaiah 44:6"][
        "draft_translation"
    ]
    assert "the one rescuing him" in by_ref["Isaiah 44:6"][
        "draft_translation"
    ]
    assert "I am first" in by_ref["Isaiah 44:6"]["draft_translation"]
    assert by_ref["Isaiah 44:7"]["draft_translation"].startswith(
        "Who is like me"
    )
    assert "from the time" in by_ref["Isaiah 44:7"]["draft_translation"]
    assert "the things coming" in by_ref["Isaiah 44:7"][
        "draft_translation"
    ]
    assert "a god besides me" in by_ref["Isaiah 44:8"]["draft_translation"]
    assert by_ref["Isaiah 44:9"]["draft_translation"].startswith(
        "The ones shaping and carving"
    )
    assert by_ref["Isaiah 44:10"]["draft_translation"].startswith(
        "All the ones who shape a god"
    )
    assert by_ref["Isaiah 44:12"]["draft_translation"].startswith(
        "For a craftsman"
    )
    assert "with an axe" in by_ref["Isaiah 44:12"]["draft_translation"]
    assert "with a drill" in by_ref["Isaiah 44:12"]["draft_translation"]
    assert "into the valley of Jehoshaphat" in by_ref["Joel 4:2"]["draft_translation"]
    assert "to the men of Judah" in by_ref["Jeremiah 4:3"]["draft_translation"]
    assert "after the thoughts of their evil heart" in by_ref["Jeremiah 3:17"]["draft_translation"]
    assert "with the wounded by the sword" in by_ref["Ezekiel 31:18"]["draft_translation"]
    assert "By the command of God" in by_ref["Joshua 19:50"]["draft_translation"]
    assert "according to the matter of each day" in by_ref["2 Chronicles 8:13"]["draft_translation"]
    assert "into the cities of Judah" in by_ref["2 Chronicles 24:5"]["draft_translation"]
    assert "by the decree of God of Israel" in by_ref["Ezra 6:14"]["draft_translation"]
    assert "according to the abundance of your mercy" in by_ref["Nehemiah 13:22"]["draft_translation"]
    assert "with the beauty of eyes" in by_ref["1 Samuel 16:12"]["draft_translation"]
    assert "in the acts of power" in by_ref["Psalms 19:7"]["draft_translation"]
    assert "to the length of days" in by_ref["Psalms 22:6"]["draft_translation"]
    assert "in the abundance of peace" in by_ref["Psalms 36:11"]["draft_translation"]
    assert "upon the bed of his pain" in by_ref["Psalms 40:4"]["draft_translation"]
    assert "from the affliction of sinner" in by_ref["Psalms 54:4"]["draft_translation"]
    assert "according to the likeness of serpent" in by_ref["Psalms 57:5"]["draft_translation"]
    assert "at the water of contradiction" in by_ref["Psalms 80:8"]["draft_translation"]
    assert "in the gathering of gods" in by_ref["Psalms 81:1"]["draft_translation"]
    assert "in the council of holy ones" in by_ref["Psalms 88:8"]["draft_translation"]
    assert "from the snare of hunters" in by_ref["Psalms 90:3"]["draft_translation"]
    assert "through the generations of generations" in by_ref["Psalms 101:25"]["draft_translation"]
    assert "with the fullness of grain" in by_ref["Proverbs 3:10"]["draft_translation"]
    assert "with the wife of your youth" in by_ref["Proverbs 5:18"]["draft_translation"]
    assert "on the breadth of your heart" in by_ref["Proverbs 7:3"]["draft_translation"]
    assert "into the storerooms of belly" in by_ref["Proverbs 20:30"]["draft_translation"]
    assert "on the corner of open roof" in by_ref["Proverbs 21:9"]["draft_translation"]
    assert "by the name of God" in by_ref["Proverbs 30:9"]["draft_translation"]
    assert "in the womb of a pregnant woman" in by_ref["Ecclesiastes 11:5"]["draft_translation"]
    assert "by the king of the Assyrians" in by_ref["Isaiah 7:20"]["draft_translation"]
    assert "into the foundations of the earth" in by_ref["Isaiah 14:15"]["draft_translation"]
    assert "How the morning-star fell from heaven" in by_ref["Isaiah 14:12"][
        "draft_translation"
    ]
    assert "I will be like the Most High" in by_ref["Isaiah 14:14"]["draft_translation"]
    assert "to destroy the Assyrians from my land" in by_ref["Isaiah 14:25"][
        "draft_translation"
    ]
    assert "the yoke of the one striking you" in by_ref["Isaiah 14:29"][
        "draft_translation"
    ]
    assert "the kings of nations answer" in by_ref["Isaiah 14:32"]["draft_translation"]
    assert "from the king of the Assyrians" in by_ref["Isaiah 20:6"]["draft_translation"]
    assert "in the glory of the Lord" in by_ref["Isaiah 24:14"]["draft_translation"]
    assert "from the produce of your land" in by_ref["Isaiah 30:23"]["draft_translation"]
    assert "say to the cities of Judah" in by_ref["Isaiah 40:9"]["draft_translation"]
    assert "in a dark place of the earth" in by_ref["Isaiah 45:19"]["draft_translation"]
    assert "to the generations of generations" in by_ref["Isaiah 51:8"]["draft_translation"]
    assert "by the strength of his arm" in by_ref["Isaiah 62:8"]["draft_translation"]
    assert "to whom the word of God came" in by_ref["Jeremiah 1:2"]["draft_translation"]
    assert "from the cities of Judah" in by_ref["Jeremiah 7:34"]["draft_translation"]
    assert "after the things pleasing to their evil heart" in by_ref["Jeremiah 9:13"]["draft_translation"]
    assert "upon the inhabitants of Anathoth" in by_ref["Jeremiah 11:23"]["draft_translation"]
    assert "in the prophets of Samaria" in by_ref["Jeremiah 23:13"]["draft_translation"]
    assert "by the works of your hands" in by_ref["Jeremiah 25:6"]["draft_translation"]
    assert "according to the anger of my wrath" in by_ref["Jeremiah 25:17"]["draft_translation"]
    assert "to the elders of exile" in by_ref["Jeremiah 36:1"]["draft_translation"]
    assert "into the bosom of their children" in by_ref["Jeremiah 39:18"]["draft_translation"]
    assert "say to the people of the land" in by_ref["Ezekiel 12:19"]["draft_translation"]
    assert "with the vengeance of adulteress" in by_ref["Ezekiel 16:38"]["draft_translation"]
    assert "against the land of Israel" in by_ref["Ezekiel 21:7"]["draft_translation"]
    assert "from the islands of Kittim" in by_ref["Ezekiel 27:6"]["draft_translation"]
    assert "say to the ruler of Tyre" in by_ref["Ezekiel 28:2"]["draft_translation"]
    assert "in the paradise of God" in by_ref["Ezekiel 31:8"]["draft_translation"]
    assert "on the fifteenth of the month" in by_ref["Ezekiel 32:17"]["draft_translation"]
    assert "according to the measures of gate facing east" in by_ref["Ezekiel 40:21"]["draft_translation"]
    assert "on the bank of the river" in by_ref["Ezekiel 47:7"]["draft_translation"]
    assert "from the dust of the earth" in by_ref["Genesis 2:7"]["draft_translation"]
    assert "with the blood of life" in by_ref["Genesis 9:4"]["draft_translation"]
    assert "with the blessing of heaven" in by_ref["Genesis 49:25"]["draft_translation"]
    assert "with the scarcity of breads" in by_ref["Leviticus 26:26"]["draft_translation"]
    assert "with the water of purification" in by_ref["Numbers 8:7"]["draft_translation"]
    assert "with the produce of fields" in by_ref["Deuteronomy 32:13"]["draft_translation"]
    assert "with the leaders of peoples" in by_ref["Deuteronomy 33:21"]["draft_translation"]
    assert "to the end of Sabbath" in by_ref["2 Chronicles 23:8"]["draft_translation"]
    assert "from the men of bloods" in by_ref["Psalms 58:3"]["draft_translation"]
    assert "upon the son of man" in by_ref["Psalms 79:16"]["draft_translation"]
    assert "In the way of your testimonies" in by_ref["Psalms 118:14"]["draft_translation"]
    assert "in the sons of men" in by_ref["Psalms 145:3"]["draft_translation"]
    assert "under the yoke of the king of Babylon" in by_ref["Jeremiah 34:8"]["draft_translation"]
    assert "in the scroll the words of the Lord" in by_ref["Jeremiah 43:8"]["draft_translation"]
    assert "from the sight of loins" in by_ref["Ezekiel 1:27"]["draft_translation"]
    assert "over the affairs of Babylon" in by_ref["Daniel 2:48"]["draft_translation"]
    assert "against the sons of your people" in by_ref["Daniel 8:19"]["draft_translation"]
    assert "on the fallow ground of a field" in by_ref["Hosea 10:4"]["draft_translation"]
    assert "from the mount of Esau" in by_ref["Obadiah 1:8"]["draft_translation"]
    assert "at the right of the lamp-bowl" in by_ref["Zechariah 4:3"]["draft_translation"]
    assert "And for the sons of Aaron" in by_ref["1 Chronicles 24:1"]["draft_translation"]
    assert "for the sacrifice of salvation" in by_ref["Numbers 7:17"]["draft_translation"]
    assert "for the service of God" in by_ref["Ezra 6:18"]["draft_translation"]
    assert "for the day of war" in by_ref["Job 38:23"]["draft_translation"]
    assert "for the mouth of the Lord spoke" in by_ref["Isaiah 1:20"]["draft_translation"]
    assert "On the twenty-fourth day" in by_ref["Haggai 2:10"]["draft_translation"]
    assert "For the command of the king" in by_ref["Nehemiah 11:23"]["draft_translation"]
    assert "for the life of the king" in by_ref["Ezra 6:10"]["draft_translation"]
    assert "for the seed of righteous ones" in by_ref["Proverbs 11:18"]["draft_translation"]
    assert "for the time of healing" in by_ref["Jeremiah 8:15"]["draft_translation"]
    assert "for the light of day" in by_ref["Jeremiah 38:36"]["draft_translation"]
    assert "for the people of the land" in by_ref["Jeremiah 52:6"]["draft_translation"]
    assert "for the salvation of the Lord" in by_ref["Lamentations 3:26"]["draft_translation"]
    assert "for the bread of presentation" in by_ref["1 Chronicles 23:29"]["draft_translation"]
    assert "for the half tribe of Manasseh" in by_ref["1 Chronicles 27:20"]["draft_translation"]
    assert "for the works of the house" in by_ref["1 Chronicles 29:7"]["draft_translation"]
    assert "concerning the sons of Israel" in by_ref["Nehemiah 1:6"]["draft_translation"]
    assert "concerning the words of book found" in by_ref["2 Chronicles 34:21"]["draft_translation"]
    assert "concerning the favor of Mordecai" in by_ref["Esther 2:23"]["draft_translation"]
    assert "into the treasury-room of Johanan" in by_ref["Ezra 10:6"]["draft_translation"]
    assert "over the third part of my kingdom" in by_ref["Daniel 5:16"]["draft_translation"]
    assert "toward the land of Egypt" in by_ref["Jeremiah 49:17"]["draft_translation"]
    assert "to drink the water of Gihon" in by_ref["Jeremiah 2:18"]["draft_translation"]
    assert "in the anger of wrath" in by_ref["1 Samuel 20:34"]["draft_translation"]
    assert "for the length of days" in by_ref["Psalms 92:5"]["draft_translation"]
    assert "For the length of life" in by_ref["Proverbs 3:2"]["draft_translation"]
    assert "Sun for the authority of day" in by_ref["Psalms 135:8"]["draft_translation"]
    assert "for the words of songs" in by_ref["Psalms 136:3"]["draft_translation"]
    assert "for the days of times" in by_ref["Isaiah 30:8"]["draft_translation"]
    assert "as a resting place for herds" in by_ref["Isaiah 65:10"]["draft_translation"]
    assert "toward the hands of their masters" in by_ref["Psalms 122:2"]["draft_translation"]
    assert "when the chiefs of chariots saw" in by_ref["2 Chronicles 18:31"]["draft_translation"]
    assert "in which is the breath of life" in by_ref["Genesis 6:17"]["draft_translation"]
    assert "in which is the spirit of life" in by_ref["Genesis 7:15"]["draft_translation"]
    assert "to give the inheritance of Zelophehad" in by_ref["Numbers 36:2"]["draft_translation"]
    assert "keeping the charge of the house" in by_ref["Ezekiel 40:45"]["draft_translation"]
    assert "keeping the charge of the altar" in by_ref["Ezekiel 40:46"]["draft_translation"]
    assert "from the end of the land" in by_ref["1 Samuel 3:21"]["draft_translation"]
    assert "after the gods of the peoples" in by_ref["1 Chronicles 5:25"]["draft_translation"]
    assert "from the families of the half tribe" in by_ref["1 Chronicles 6:56"]["draft_translation"]
    assert "to the borders of the sons of Manasseh" in by_ref["1 Chronicles 7:29"]["draft_translation"]
    assert "from the hill of Benjamin" in by_ref["1 Chronicles 11:31"]["draft_translation"]
    assert "into the cave of Adullam" in by_ref["1 Chronicles 11:15"]["draft_translation"]
    assert "to bring the ark of God" in by_ref["1 Chronicles 13:5"]["draft_translation"]
    assert "from there the ark of God" in by_ref["1 Chronicles 13:6"]["draft_translation"]
    assert "by the word of God" in by_ref["1 Chronicles 15:15"]["draft_translation"]
    assert "brought in the ark of God" in by_ref["1 Chronicles 16:1"]["draft_translation"]
    assert "to bless the house of your servant" in by_ref["1 Chronicles 17:27"]["draft_translation"]
    assert "on the servants of Hadarezer" in by_ref["1 Chronicles 18:7"]["draft_translation"]
    assert "For the divisions of gates" in by_ref["1 Chronicles 26:1"]["draft_translation"]
    assert "for the ark of God" in by_ref["1 Chronicles 15:1"]["draft_translation"]
    assert "for the cities of our God" in by_ref["1 Chronicles 19:13"]["draft_translation"]
    assert "for the nails of doors" in by_ref["1 Chronicles 22:3"]["draft_translation"]
    assert "for the fine flour of offering" in by_ref["1 Chronicles 23:29"]["draft_translation"]
    assert "for the remaining sons of Levi" in by_ref["1 Chronicles 24:20"]["draft_translation"]
    assert "over the cleansing of all holy things" in by_ref["1 Chronicles 23:28"]["draft_translation"]
    assert "at the hearing of the ear" in by_ref["2 Samuel 22:45"]["draft_translation"]
    assert by_ref["Psalms 24:11"]["draft_translation"].startswith("For the sake of your name")
    assert by_ref["1 Chronicles 19:11"]["draft_translation"].startswith("And the rest of the people")
    assert by_ref["Ezekiel 48:2"]["draft_translation"].startswith("And beside the border of Dan")
    assert "And the servants of David came" in by_ref["1 Chronicles 19:2"]["draft_translation"]
    assert by_ref["2 Kings 1:3"]["draft_translation"].startswith("And the angel of the Lord spoke")
    assert by_ref["1 Samuel 7:11"]["draft_translation"].startswith("And the men of Israel went out")
    assert by_ref["2 Chronicles 33:25"]["draft_translation"].startswith("And the people of the land struck")
    assert by_ref["2 Chronicles 23:17"]["draft_translation"].startswith("And all the people of the land entered")
    assert by_ref["1 Chronicles 19:3"]["draft_translation"].startswith("And the rulers of Ammon said")
    assert by_ref["Isaiah 10:21"]["draft_translation"].startswith("And the remnant of Jacob")
    assert by_ref["Isaiah 40:5"]["draft_translation"].startswith("And the glory of the Lord")
    assert by_ref["Psalms 28:3"]["draft_translation"].startswith("The voice of the Lord is upon waters")
    assert by_ref["Psalms 18:10"]["draft_translation"].startswith("The fear of the Lord is pure")
    assert by_ref["Psalms 110:10"]["draft_translation"].startswith("The beginning of wisdom is the fear")
    assert "The works of his hands you blessed" in by_ref["Job 1:10"]["draft_translation"]
    assert "Because of the multitude of your injustice" in by_ref["Jeremiah 13:22"]["draft_translation"]
    assert "the house of the Lord was full of glory" in by_ref["Ezekiel 44:4"]["draft_translation"]
    assert by_ref["2 Chronicles 18:5"]["draft_translation"].startswith("And the king of Israel gathered")
    assert by_ref["Isaiah 36:2"]["draft_translation"].startswith("And the king of the Assyrians sent")
    assert by_ref["Jeremiah 52:10"]["draft_translation"].startswith("And the king of Babylon slaughtered")
    assert "the glory of the Lord filled the house of God" in by_ref["2 Chronicles 5:14"]["draft_translation"]
    assert "the glory of the Lord filled the house" in by_ref["2 Chronicles 7:1"]["draft_translation"]
    assert "the remnant of Israel were one soul" in by_ref["1 Chronicles 12:39"]["draft_translation"]
    assert by_ref["Psalms 28:4"]["draft_translation"].startswith("The voice of the Lord is in strength")
    assert by_ref["Psalms 28:5"]["draft_translation"].startswith("The voice of the Lord shattering")
    assert by_ref["Proverbs 8:13"]["draft_translation"].startswith("The fear of the Lord hates")
    assert by_ref["Proverbs 10:21"]["draft_translation"].startswith("The lips of the righteous know")
    assert by_ref["Proverbs 14:10"]["draft_translation"].startswith("The heart of perceptive man knows")
    assert by_ref["Ecclesiastes 7:4"]["draft_translation"].startswith("The heart of the wise is")
    assert by_ref["1 Chronicles 2:29"]["draft_translation"].startswith(
        "And the name of the wife of Abishur"
    )
    assert by_ref["1 Chronicles 13:14"]["draft_translation"].startswith("And the ark of God stayed")
    assert by_ref["1 Chronicles 21:4"]["draft_translation"].startswith("But the word of the king prevailed")
    assert by_ref["2 Chronicles 9:1"]["draft_translation"].startswith("And the queen of Sheba heard")
    assert by_ref["Psalms 36:30"]["draft_translation"].startswith("The mouth of a righteous man")
    assert "The river of God was filled" in by_ref["Psalms 64:10"]["draft_translation"]
    assert by_ref["Psalms 67:16"]["draft_translation"].startswith("The mountain of God")
    assert by_ref["Psalms 113:17"]["draft_translation"].startswith("The house of Israel hoped")
    assert by_ref["Isaiah 6:10"]["draft_translation"].startswith("For the heart of this people")
    assert by_ref["Isaiah 19:17"]["draft_translation"].startswith(
        "And the land of the Jews"
    )
    assert by_ref["Isaiah 52:8"]["draft_translation"].startswith("Because the voice of your watchmen")
    assert by_ref["Jeremiah 27:43"]["draft_translation"].startswith("The king of Babylon heard")
    assert by_ref["Jeremiah 33:24"]["draft_translation"].startswith("But the hand of Ahikam")
    assert by_ref["Ezekiel 3:7"]["draft_translation"].startswith("But the house of Israel")
    assert by_ref["Ezekiel 18:29"]["draft_translation"].startswith("And the house of Israel")
    assert by_ref["Ezekiel 22:29"]["draft_translation"].startswith("The people of the land")
    assert by_ref["Zephaniah 3:13"]["draft_translation"].startswith("The remnant of Israel")
    assert by_ref["2 Samuel 7:18"]["draft_translation"].startswith("And King David entered")
    assert by_ref["1 Kings 9:26"]["draft_translation"].startswith("And King Solomon made")
    assert "King David's spears" in by_ref["2 Kings 11:10"]["draft_translation"]
    assert "And the king said, Sit in Jericho" in by_ref["1 Chronicles 19:5"]["draft_translation"]
    assert by_ref["2 Chronicles 7:4"]["draft_translation"].startswith("And the king and all the people")
    assert by_ref["Psalms 20:8"]["draft_translation"].startswith("Because the king hopes")
    assert by_ref["Psalms 62:12"]["draft_translation"].startswith("But the king will rejoice")
    assert by_ref["Ezekiel 21:26"]["draft_translation"].startswith("Because the king of Babylon")
    assert "Then the king issued decree" in by_ref["Daniel 5:7"]["draft_translation"]
    assert "death of all the people" in by_ref["Numbers 16:29"]["draft_translation"]
    assert by_ref["1 Chronicles 16:36"]["draft_translation"].startswith("Blessed is the Lord God of Israel")
    assert "And all the people shall say, Amen" in by_ref["1 Chronicles 16:36"]["draft_translation"]
    assert by_ref["1 Chronicles 21:4"]["draft_translation"].startswith("But the word of the king prevailed")
    assert "matter of the king" in by_ref["1 Chronicles 26:32"]["draft_translation"]
    assert "Let all the people in my kingdom worship" in by_ref["Daniel 6:27"]["draft_translation"]
    assert "to all the assembly of Israel" in by_ref["1 Chronicles 13:2"]["draft_translation"]
    assert "in all the land of Israel" in by_ref["1 Chronicles 13:2"]["draft_translation"]
    assert by_ref["1 Chronicles 13:4"]["draft_translation"].startswith("And all the assembly said")
    assert "spoils of the city" in by_ref["1 Chronicles 20:2"]["draft_translation"]
    assert "breadth of the house" in by_ref["2 Chronicles 3:4"]["draft_translation"]
    assert "face of the temple of the Lord" in by_ref["Jeremiah 24:1"]["draft_translation"]
    assert "set pillars before the temple" in by_ref["2 Chronicles 3:17"]["draft_translation"]
    assert "set them in the temple" in by_ref["2 Chronicles 4:7"]["draft_translation"]
    assert "burn incense in the temple" in by_ref["2 Chronicles 26:19"]["draft_translation"]
    assert "entered the temple of the Lord" in by_ref["2 Chronicles 29:17"]["draft_translation"]
    assert "voice from the temple" in by_ref["Isaiah 66:6"]["draft_translation"]
    assert "the Lord will build a house for you" in by_ref["1 Chronicles 17:10"]["draft_translation"]
    assert "to build a house for God" in by_ref["1 Chronicles 22:2"]["draft_translation"]
    assert "building the house of the Lord" in by_ref["2 Chronicles 3:1"]["draft_translation"]
    assert "build the house, and I will take pleasure" in by_ref["Haggai 1:8"]["draft_translation"]
    assert "will build the house of the Lord" in by_ref["Zechariah 6:12"]["draft_translation"]
    assert "your righteousness to a son of man" in by_ref["Job 35:8"]["draft_translation"]
    assert "came into the city" in by_ref["1 Chronicles 19:15"]["draft_translation"]
    assert "from one city to another" in by_ref["2 Chronicles 30:10"]["draft_translation"]
    assert "in each city and province" in by_ref["Esther 8:17"]["draft_translation"]
    assert "opposite the city" in by_ref["Jonah 4:5"]["draft_translation"]
    assert "the city will be taken" in by_ref["Zechariah 14:2"]["draft_translation"]
    assert "Jebusites dwelling in the land" in by_ref["1 Chronicles 11:4"]["draft_translation"]
    assert "death in the land" in by_ref["1 Chronicles 21:12"]["draft_translation"]
    assert "Athaliah reigned over the land" in by_ref["2 Chronicles 22:12"]["draft_translation"]
    assert "dwelt in the land of Uz" in by_ref["Job 42:17"]["draft_translation"]
    assert "in a desert and trackless and waterless land" in by_ref["Psalms 62:2"]["draft_translation"]
    assert "came into the land" in by_ref["2 Chronicles 36:5"]["draft_translation"]
    assert "against a land thrown open" in by_ref["Ezekiel 38:11"]["draft_translation"]
    assert "before the ark continually" in by_ref["1 Chronicles 16:37"]["draft_translation"]
    assert "There was nothing in the ark" in by_ref["2 Chronicles 5:10"]["draft_translation"]
    assert "swears before the altar" in by_ref["2 Chronicles 6:22"]["draft_translation"]
    assert "poured blood upon the altar" in by_ref["2 Chronicles 29:22"]["draft_translation"]
    assert "And the people rejoiced" in by_ref["1 Chronicles 29:9"]["draft_translation"]
    assert "dwelt in a house from the day" in by_ref["1 Chronicles 17:5"]["draft_translation"]
    assert "vestibule before the house" in by_ref["2 Chronicles 3:4"]["draft_translation"]
    assert "glory of the Lord upon the house" in by_ref["2 Chronicles 7:3"]["draft_translation"]
    assert "holy ark in the house" in by_ref["2 Chronicles 35:3"]["draft_translation"]
    assert "inside the house like death" in by_ref["Lamentations 1:20"]["draft_translation"]
    assert "from the breath of Mighty One" in by_ref["Job 37:10"]["draft_translation"]
    assert "from the presence of the king" in by_ref["Ezra 7:14"]["draft_translation"]
    assert "in the wilderness of Judah" in by_ref["Psalms 62:1"]["draft_translation"]
    assert "in the gladness of your nation" in by_ref["Psalms 105:5"]["draft_translation"]
    assert "in the wandering of his heart" in by_ref["Jeremiah 23:17"]["draft_translation"]
    assert "at the dedication of the house of God" in by_ref["Ezra 6:17"]["draft_translation"]
    assert "at the mouth of pit" in by_ref["Jeremiah 31:28"]["draft_translation"]
    assert "according to the ways of kings" in by_ref["2 Chronicles 28:2"]["draft_translation"]
    assert "according to the completion of days" in by_ref["Ezekiel 5:2"]["draft_translation"]
    assert "by the gates of Jerusalem" in by_ref["Jeremiah 17:21"]["draft_translation"]
    assert "for the wall of the city" in by_ref["Nehemiah 2:8"]["draft_translation"]
    assert "for the throne of rule" in by_ref["Proverbs 16:12"]["draft_translation"]
    assert "for the work of the house of the Lord" in by_ref["2 Chronicles 24:12"]["draft_translation"]
    assert "with the elders of the land" in by_ref["Proverbs 31:23"]["draft_translation"]
    assert "over the faithlessness of the exile" in by_ref["Ezra 9:4"]["draft_translation"]
    assert "into the height of mountains" in by_ref["Isaiah 37:24"]["draft_translation"]
    assert "this is the City of David" in by_ref["1 Chronicles 11:5"]["draft_translation"]
    assert "went up to the City of David" in by_ref["1 Chronicles 13:6"]["draft_translation"]
    assert by_ref["1 Chronicles 27:16"]["draft_translation"].startswith("And over the tribes of Israel")
    assert "in the fifth year of the reign of Rehoboam" in by_ref["2 Chronicles 12:2"]["draft_translation"]
    assert "out of the land of Egypt" in by_ref["2 Chronicles 6:5"]["draft_translation"]
    assert "Hear the sound of a trumpet" in by_ref["Jeremiah 6:17"]["draft_translation"]
    assert "works of the hands of men" in by_ref["2 Chronicles 32:19"]["draft_translation"]
    assert by_ref["Proverbs 14:33"]["draft_translation"].startswith("In the good heart of man")
    assert "the spirit of life was in the wheels" in by_ref["Ezekiel 1:20"]["draft_translation"]
    assert by_ref["1 Chronicles 16:33"]["draft_translation"].startswith("Then trees of the forest")
    assert "there was the tent of testimony of God" in by_ref["2 Chronicles 1:3"]["draft_translation"]
    assert "as the good hand of God was upon me" in by_ref["Ezra 7:28"]["draft_translation"]
    assert by_ref["Nehemiah 13:19"]["draft_translation"].startswith("And it came to be when the gates of Jerusalem")
    assert by_ref["Job 38:17"]["draft_translation"].startswith("And are the gates of death")
    assert "the way of righteous men" in by_ref["Psalms 1:6"]["draft_translation"]
    assert by_ref["Proverbs 5:21"]["draft_translation"].startswith("For the ways of man")
    assert "grows the tree of life" in by_ref["Proverbs 11:30"]["draft_translation"]
    assert "Sanctify the day of Sabbaths" in by_ref["Jeremiah 17:22"]["draft_translation"]
    assert "judge the city of bloods" in by_ref["Ezekiel 22:2"]["draft_translation"]
    assert "the mountains of Israel will be desolated" in by_ref["Ezekiel 33:28"]["draft_translation"]
    assert by_ref["Amos 5:6"]["draft_translation"].startswith("Seek the Lord and live, lest the house of Joseph")
    assert "fruit of the womb" in by_ref["Genesis 30:2"]["draft_translation"]
    assert "give the land of Canaan" in by_ref["1 Chronicles 16:18"]["draft_translation"]
    assert "may the name of God of Jacob" in by_ref["Psalms 19:2"]["draft_translation"]
    assert "gladden the city of God" in by_ref["Psalms 45:5"]["draft_translation"]
    assert by_ref["Psalms 46:6"]["draft_translation"].endswith(
        "the Lord with the voice of a trumpet."
    )
    assert by_ref["Isaiah 24:14"]["draft_translation"].endswith("the water of the sea will be troubled.")
    assert "behind the whole house of Judah" in by_ref["Nehemiah 4:10"]["draft_translation"]
    assert "the house of Israel and the house of Judah" in by_ref["Jeremiah 38:31"]["draft_translation"]
    assert by_ref["Jeremiah 43:3"]["draft_translation"].startswith("Perhaps the house of Judah")
    assert "Jerusalem and the house of Judah proclaimed fast" in by_ref["Jeremiah 43:9"]["draft_translation"]
    assert "his flock, the house of Judah" in by_ref["Zechariah 10:3"]["draft_translation"]
    assert by_ref["Job 6:25"]["draft_translation"].startswith("As it seems, the words of truth")
    assert "answering the words of truth" in by_ref["Proverbs 22:21"]["draft_translation"]
    assert "remember the one who created you" in by_ref["Ecclesiastes 12:1"][
        "draft_translation"
    ]
    assert "the dust returns upon the earth" in by_ref["Ecclesiastes 12:7"][
        "draft_translation"
    ]
    assert "all is vanity" in by_ref["Ecclesiastes 12:8"]["draft_translation"]
    assert "the City of Letters" in by_ref["Joshua 15:15"]["draft_translation"]
    assert "the City of Arba" in by_ref["Joshua 14:15"]["draft_translation"]
    assert "above the Gate of Ephraim" in by_ref["Nehemiah 12:39"]["draft_translation"]
    assert "in the fifteenth year of the kingdom of Asa" in by_ref["2 Chronicles 15:10"]["draft_translation"]
    assert by_ref["Deuteronomy 32:7"]["draft_translation"].startswith("Remember the days of old")
    assert "Jericho, the city of palms" in by_ref["Deuteronomy 34:3"]["draft_translation"]
    assert "patriarchs of the tribes of Israel" in by_ref["1 Chronicles 27:22"]["draft_translation"]
    assert "went through the cities of Judah" in by_ref["2 Chronicles 17:9"]["draft_translation"]
    assert "attacked the cities of Judah" in by_ref["2 Chronicles 25:13"]["draft_translation"]
    assert "know the heart of sons of men" in by_ref["2 Chronicles 6:30"]["draft_translation"]
    assert "the right hand of a poor man" in by_ref["Psalms 108:31"]["draft_translation"]
    assert "right hand, the right hand of injustice" in by_ref["Psalms 143:8"]["draft_translation"]
    assert by_ref["Proverbs 2:22"]["draft_translation"].startswith("The ways of the ungodly")
    assert by_ref["Proverbs 4:18"]["draft_translation"].startswith(
        "The ways of the righteous are like"
    )
    assert by_ref["Proverbs 4:19"]["draft_translation"].startswith("But the ways of the ungodly are dark")
    assert "guards the ways of righteous life" in by_ref["Proverbs 10:17"]["draft_translation"]
    assert by_ref["Ecclesiastes 9:17"]["draft_translation"].startswith("The words of the wise")
    assert "the height of men will be humbled" in by_ref["Isaiah 2:11"]["draft_translation"]
    assert "see the way of Egypt" in by_ref["Isaiah 10:24"]["draft_translation"]
    assert "from the Assyrians, because with a rod" in by_ref["Isaiah 10:24"][
        "draft_translation"
    ]
    assert "reported to him the words of Rabshakeh" in by_ref["Isaiah 36:22"]["draft_translation"]
    assert "tear apart the strength of kings" in by_ref["Isaiah 45:1"]["draft_translation"]
    assert "for the host of heaven" in by_ref["Jeremiah 7:18"]["draft_translation"]
    assert "Do not hear the words of prophets" in by_ref["Jeremiah 23:16"]["draft_translation"]
    assert "make the land of Babylon" in by_ref["Jeremiah 28:29"]["draft_translation"]
    assert "give them the land of Israel" in by_ref["Ezekiel 11:17"]["draft_translation"]
    assert "because of the blood of humans" in by_ref["Habakkuk 2:8"]["draft_translation"]
    assert by_ref["Isaiah 32:4"]["draft_translation"].startswith(
        "And the heart of the weak ones"
    )
    assert by_ref["Ezekiel 1:8"]["draft_translation"].startswith("And the hand of man")
    assert by_ref["Ezekiel 40:23"]["draft_translation"].startswith(
        "And the gate of the inner court faced the gate of the north"
    )
    assert "by way of the gate between" in by_ref["Jeremiah 52:7"]["draft_translation"]
    assert "by way of the gate of the court" in by_ref["Ezekiel 47:2"]["draft_translation"]
    assert "for the remnant of his inheritance" in by_ref["Micah 7:18"]["draft_translation"]
    assert "before the remnant of this people" in by_ref["Zechariah 8:6"]["draft_translation"]
    assert by_ref["Ezra 6:19"]["draft_translation"].startswith("And the sons of the exile")
    assert by_ref["Nehemiah 12:28"]["draft_translation"].startswith("And the sons of the singers")
    assert by_ref["2 Chronicles 1:16"]["draft_translation"].startswith("And the export of horses")
    assert by_ref["2 Chronicles 25:15"]["draft_translation"].startswith("And the anger of the Lord")
    assert by_ref["Hosea 5:5"]["draft_translation"].startswith("And the arrogance of Israel")
    assert by_ref["Ezra 5:5"]["draft_translation"].startswith("And the eyes of God")
    assert by_ref["Jeremiah 44:5"]["draft_translation"].startswith("And the force of Pharaoh")
    assert by_ref["Jeremiah 52:8"]["draft_translation"].startswith("And the force of Chaldeans")
    assert by_ref["Jeremiah 39:2"]["draft_translation"].startswith("And the force of the king of Babylon")
    assert by_ref["2 Chronicles 36:19"]["draft_translation"].startswith(
        "And he burned the house of the Lord"
    )
    assert "and the house of the king and all the houses of the city" in by_ref["Jeremiah 52:13"][
        "draft_translation"
    ]
    assert by_ref["Ezekiel 40:11"]["draft_translation"].startswith("And he measured the width of")
    assert by_ref["Ezekiel 41:4"]["draft_translation"].startswith("And he measured the length of")
    assert by_ref["Isaiah 6:6"]["draft_translation"].startswith("And one of the seraphim")
    assert "broke down the wall of Jerusalem" in by_ref["2 Chronicles 36:19"]["draft_translation"]
    assert "and the city was quiet" in by_ref["2 Chronicles 23:21"]["draft_translation"]
    assert "entered the house of Baal" in by_ref["2 Chronicles 23:17"]["draft_translation"]
    assert "saw the wisdom of Solomon and the house which he built" in by_ref["2 Chronicles 9:3"][
        "draft_translation"
    ]
    assert "heard the name of Solomon" in by_ref["2 Chronicles 9:1"]["draft_translation"]
    assert "then an answer was sent" in by_ref["Ezra 5:5"]["draft_translation"]
    assert "from the undertaking of his heart" in by_ref["Jeremiah 23:20"]["draft_translation"]
    assert "establishes the undertaking of his heart" in by_ref["Jeremiah 37:24"]["draft_translation"]
    assert "according to the blow of Midian" in by_ref["Isaiah 10:26"]["draft_translation"]
    assert "in the place of affliction" in by_ref["Isaiah 10:26"]["draft_translation"]
    assert "in the way by sea, in the way toward Egypt" in by_ref["Isaiah 10:26"]["draft_translation"]
    assert "midst of the shadow of death" in by_ref["Psalms 22:4"]["draft_translation"]
    assert "beasts of the earth" in by_ref["Jeremiah 7:33"]["draft_translation"]
    assert "face of the field" in by_ref["Jeremiah 9:21"]["draft_translation"]
    assert "cloud filled the house, and the court was filled" in by_ref["Ezekiel 10:4"][
        "draft_translation"
    ]
    assert "stood upon the mountain opposite the city" in by_ref["Ezekiel 11:23"]["draft_translation"]
    assert by_ref["1 Chronicles 11:3"]["draft_translation"].startswith("And all the elders of Israel")
    assert "all the Levites took the ark" in by_ref["2 Chronicles 5:4"]["draft_translation"]
    assert by_ref["Jeremiah 47:7"]["draft_translation"].startswith("And all the leaders of the force")
    assert "in the field" in by_ref["Jeremiah 47:7"]["draft_translation"]
    assert "that the king of Babylon appointed" in by_ref["Jeremiah 47:7"]["draft_translation"]
    assert by_ref["Jeremiah 7:33"]["draft_translation"].startswith("And the dead bodies of this people")
    assert "be an example upon" in by_ref["Jeremiah 9:21"]["draft_translation"]
    assert by_ref["Jeremiah 52:11"]["draft_translation"].startswith("And the eyes of Zedekiah")
    assert "and the king of Babylon led him" in by_ref["Jeremiah 52:11"]["draft_translation"]
    assert by_ref["1 Chronicles 2:29"]["draft_translation"].startswith(
        "And the name of the wife of Abishur"
    )
    assert "and the name of their sister" in by_ref["1 Chronicles 4:3"]["draft_translation"]
    assert "holy is the place where" in by_ref["2 Chronicles 8:11"]["draft_translation"]
    assert by_ref["Ezra 10:9"]["draft_translation"].startswith("And all the men of Judah and Benjamin")
    assert "bring the ark of our God" in by_ref["1 Chronicles 13:3"]["draft_translation"]
    assert "served as priest in his place" in by_ref["Deuteronomy 10:6"]["draft_translation"]
    assert "reigned in his place" in by_ref["1 Kings 14:31"]["draft_translation"]
    assert "would reign in his place" in by_ref["2 Kings 3:27"]["draft_translation"]
    assert "the second young man who will stand in his place" in by_ref["Ecclesiastes 4:15"]["draft_translation"]
    assert "Who will give my death instead of you? I, instead of you" in by_ref["2 Samuel 19:1"]["draft_translation"]
    assert "made bronze arms in their place" in by_ref["1 Kings 14:27"]["draft_translation"]
    assert "put satraps in their place" in by_ref["1 Kings 21:24"]["draft_translation"]
    assert "make iron yokes in their place" in by_ref["Jeremiah 35:13"]["draft_translation"]
    assert "instead of every firstborn" in by_ref["Numbers 3:12"]["draft_translation"]
    assert "beasts of the field" in by_ref["Psalms 8:8"]["draft_translation"]
    assert "all the beasts of the field" in by_ref["Ezekiel 31:6"]["draft_translation"]
    assert "fish of the sea will recount to you" in by_ref["Job 12:8"]["draft_translation"]
    assert "creeping things creeping on the earth" in by_ref["Ezekiel 38:20"]["draft_translation"]
    assert "reptiles of the earth" in by_ref["Hosea 2:20"]["draft_translation"]
    assert "In the wilderness they lay in wait for us" in by_ref["Lamentations 4:19"]["draft_translation"]
    assert "made in the wilderness" in by_ref["1 Chronicles 21:29"]["draft_translation"]
    assert "from the wilderness" in by_ref["1 Chronicles 12:9"]["draft_translation"]
    assert "into the wilderness" in by_ref["Jeremiah 13:24"]["draft_translation"]
    assert "to the wilderness" in by_ref["Hosea 2:16"]["draft_translation"]
    assert "river of the wilderness Jeruel" in by_ref["2 Chronicles 20:16"]["draft_translation"]
    assert "camped by themselves in the plain" in by_ref["1 Chronicles 19:9"]["draft_translation"]
    assert "went out into the plain" in by_ref["Ezekiel 3:23"]["draft_translation"]
    assert "entering city from the plain" in by_ref["Ezekiel 26:10"]["draft_translation"]
    assert "face of the plain" in by_ref["Ezekiel 16:5"]["draft_translation"]
    assert "house of the forest of Lebanon" in by_ref["2 Chronicles 9:16"]["draft_translation"]
    assert "Boar from the forest ravaged her" in by_ref["Psalms 79:14"]["draft_translation"]
    assert "In the forest at evening" in by_ref["Isaiah 21:13"]["draft_translation"]
    assert "say to the forest of Negeb" in by_ref["Ezekiel 21:3"]["draft_translation"]
    assert "to the river Gozan" in by_ref["1 Chronicles 5:26"]["draft_translation"]
    assert "upon the river Euphrates" in by_ref["1 Chronicles 18:3"]["draft_translation"]
    assert "from the river Ahava" in by_ref["Ezra 8:31"]["draft_translation"]
    assert "Rushings of the river" in by_ref["Psalms 45:5"]["draft_translation"]
    assert "into the river will groan" in by_ref["Isaiah 19:8"]["draft_translation"]
    assert "Let not the king speak thus" in by_ref["2 Chronicles 18:7"]["draft_translation"]
    assert "except the king of Israel only" in by_ref["2 Chronicles 18:30"]["draft_translation"]
    assert "whom the king of Babylon appointed" in by_ref["Jeremiah 47:5"]["draft_translation"]
    assert "and the name of his city was Dinhabah" in by_ref["1 Chronicles 1:43"]["draft_translation"]
    assert "and the name of his city was Gittaim" in by_ref["1 Chronicles 1:46"]["draft_translation"]
    assert "and the name of his mother was Maachah" in by_ref["2 Chronicles 13:2"]["draft_translation"]
    assert "and the name of his sister was Maachah" in by_ref["1 Chronicles 7:15"]["draft_translation"]
    assert "and the name of the second was Zelophehad" in by_ref["1 Chronicles 7:15"]["draft_translation"]
    assert "Call the name of Pharaoh Neco" in by_ref["Jeremiah 26:17"]["draft_translation"]
    assert "Let the name of the great Lord be blessed" in by_ref["Daniel 2:20"]["draft_translation"]
    assert "praise the name of your boasting" in by_ref["1 Chronicles 29:13"]["draft_translation"]
    assert "bless the name of your glory" in by_ref["Nehemiah 9:5"]["draft_translation"]
    assert "profane the name of their God" in by_ref["Amos 2:7"]["draft_translation"]
    assert "the name of Israel will not be remembered" in by_ref["Psalms 82:5"]["draft_translation"]
    assert "one hated by the Lord" in by_ref["2 Chronicles 19:2"]["draft_translation"]
    assert "fears the Lord" in by_ref["Proverbs 14:2"]["draft_translation"]
    assert "hearts chosen by the Lord" in by_ref["Proverbs 17:3"]["draft_translation"]
    assert "hear the voice of his servant" in by_ref["Isaiah 50:10"]["draft_translation"]
    assert "Redeemed by the Lord" in by_ref["Isaiah 62:12"]["draft_translation"]
    assert "many will be wounded by the Lord" in by_ref["Isaiah 66:16"]["draft_translation"]
    assert "slain by the Lord" in by_ref["Jeremiah 32:33"]["draft_translation"]
    assert "the name of the city is Burial Place, and the land will be cleansed" in by_ref[
        "Ezekiel 39:16"
    ]["draft_translation"]
    assert "swearing by the Lord" in by_ref["Zephaniah 1:5"]["draft_translation"]
    assert "God defender and a house of refuge" in by_ref["Psalms 30:3"]["draft_translation"]
    assert "house of the kingdom" in by_ref["Amos 7:13"]["draft_translation"]
    assert "house of a lawless one" in by_ref["Micah 6:10"]["draft_translation"]
    assert "enter the house of the thief and the house of the one swearing falsely" in by_ref[
        "Zechariah 5:4"
    ]["draft_translation"]
    assert by_ref["Proverbs 17:21"]["draft_translation"].startswith("The heart of a fool")
    assert "but the heart of fools" in by_ref["Proverbs 12:23"]["draft_translation"]
    assert by_ref["Ecclesiastes 7:4"]["draft_translation"].startswith("The heart of the wise is")
    assert "and the heart of fools is" in by_ref["Ecclesiastes 7:4"]["draft_translation"]
    assert "the one fearing God" in by_ref["Ecclesiastes 7:18"]["draft_translation"]
    assert "the good one before the face of God" in by_ref["Ecclesiastes 7:26"]["draft_translation"]
    assert "one man among a thousand" in by_ref["Ecclesiastes 7:28"]["draft_translation"]
    assert "the heart of the king will perish and the heart of the rulers" in by_ref[
        "Jeremiah 4:9"
    ]["draft_translation"]
    assert "a voice of weeping and a voice of crying" in by_ref["Isaiah 65:19"]["draft_translation"]
    assert "the sound of a shout of joy" in by_ref["Ezra 3:13"]["draft_translation"]
    assert "the sound of wings of living beings" in by_ref["Ezekiel 3:13"]["draft_translation"]
    assert "the sound of wings of cherubim" in by_ref["Ezekiel 10:5"]["draft_translation"]
    assert "the sound of harmony" in by_ref["Ezekiel 23:42"]["draft_translation"]
    assert "the sound of a cry from the gate" in by_ref["Zephaniah 1:10"]["draft_translation"]
    assert "said to the Levites" in by_ref["2 Chronicles 35:3"]["draft_translation"]
    assert "placed the holy ark" in by_ref["2 Chronicles 35:3"]["draft_translation"]
    assert "built, and the king said" in by_ref["2 Chronicles 35:3"]["draft_translation"]
    assert "anything on your shoulders" in by_ref["2 Chronicles 35:3"]["draft_translation"]
    assert "rulers of the Levites, contributed to the Levites" in by_ref["2 Chronicles 35:9"][
        "draft_translation"
    ]
    assert "for the continual whole burnt offering of the Sabbaths" in by_ref["Nehemiah 10:34"][
        "draft_translation"
    ]
    assert "and the words I put in your mouth" in by_ref["Isaiah 59:21"]["draft_translation"]
    assert by_ref["Isaiah 9:6"]["draft_translation"].startswith("Great is his rule")
    assert "The zeal of the Lord of hosts will do these things" in by_ref["Isaiah 9:6"][
        "draft_translation"
    ]
    assert "but his hand is still high" in by_ref["Isaiah 9:20"]["draft_translation"]
    assert by_ref["Amos 9:12"]["draft_translation"].startswith("so that the remnant of men")
    assert "upon whom my name has been called upon them may seek" in by_ref["Amos 9:12"][
        "draft_translation"
    ]
    assert "bring the third through fire" in by_ref["Zechariah 13:9"]["draft_translation"]
    assert "he will say, The Lord is my God" in by_ref["Zechariah 13:9"]["draft_translation"]
    assert "this one is the God of gods" in by_ref["Deuteronomy 10:17"]["draft_translation"]
    assert by_ref["Psalms 49:1"]["draft_translation"].startswith(
        "Psalm of Asaph. The God of gods, the Lord, spoke"
    )
    assert "Give thanks to the God of gods" in by_ref["Psalms 135:2"]["draft_translation"]
    assert "Give thanks to the God of heaven" in by_ref["Psalms 135:26"]["draft_translation"]
    assert by_ref["Daniel 2:44"]["draft_translation"].startswith("And in the days of those kings the God of heaven")
    assert "your God is the God of gods" in by_ref["Daniel 2:47"]["draft_translation"]
    assert "servants of the God of gods" in by_ref["Daniel 3:26"]["draft_translation"]
    assert "he is the God of gods" in by_ref["Daniel 4:37"]["draft_translation"]
    assert "removing a kingdom from kings" in by_ref["Daniel 4:37"]["draft_translation"]
    assert "All the days of my kingdom" in by_ref["Daniel 4:37"]["draft_translation"]
    assert "as a sweet smell to the Lord" in by_ref["Daniel 4:37"]["draft_translation"]
    assert "as the God of heaven did in me" in by_ref["Daniel 4:37"]["draft_translation"]
    assert "speaks against the God of heaven" in by_ref["Daniel 4:37"]["draft_translation"]
    assert "offer a sacrifice and an offering" in by_ref["Daniel 4:37"]["draft_translation"]
    assert "against the God of gods" in by_ref["Daniel 11:36"]["draft_translation"]


def test_lexham_textual_export_is_not_enabled_from_user_desktop_by_default() -> None:
    script_path = ROOT / "scripts" / "build_fresh_logos_bible.py"
    spec = importlib.util.spec_from_file_location("build_fresh_logos_bible", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    default_path = module.DEFAULT_TEXTUAL_NOTES_HTML
    assert default_path == ROOT / "data" / "research" / "textual_notes_export.html"
    assert "Desktop" not in str(default_path)
    assert module.reader_facing_note_text(
        "Main note. Equivalent source: internal debug source. Direct Logos export shows witness detail."
    ) == "Main note."


def test_proper_name_notes_have_meanings_and_expected_1_samuel_entries() -> None:
    rows = csv_rows("data/proper_name_transliteration_notes.csv")
    by_name = {row["name"]: row for row in rows}

    assert len(rows) >= 2300
    assert not [row for row in rows if not row["name_meaning"].strip()]
    assert not [row for row in rows if "meaning uncertain" in row["name_meaning"].lower()]
    assert not [row for row in rows if row["equivalent_confidence"] == "fallback"]
    assert not [row for row in rows if row["name"] == "Gods" or row["greek_form"] == "επιγνωση"]

    expected = {
        "Ramathaim-Zophim": ("Ramathaim-Zophim", "the two watch-towers"),
        "Dizahab": ("Dizahab", "where much gold is"),
        "Tohu": ("Tohu", "that lives; that declares"),
        "Hannah": ("Hannah", "gracious; merciful; he that gives"),
        "Peninnah": ("Peninnah", "pearl; precious stone; the face"),
        "Zuph": ("Zuph", "watcher; honeycomb"),
        "Kue": ("Kue", "Cilician region"),
        "Jozadak": ("Jozadak", "Yahweh is righteous; justice of the Lord"),
        "Josedech": ("Josedech", "Yahweh is righteous; justice of the Lord"),
        "Ieddouran": ("Joram", "to cast; elevated"),
    }
    for source_name, (english_equivalent, meaning) in expected.items():
        assert by_name[source_name]["english_equivalent"] == english_equivalent
        assert by_name[source_name]["name_meaning"] == meaning


def test_nt_proper_name_notes_have_no_placeholder_meanings() -> None:
    rows = csv_rows("data/proper_name_transliteration_notes.csv")
    nt_rows = [row for row in rows if row["source"] == "nt"]
    placeholder_rows = [
        row
        for row in nt_rows
        if any(
            marker in row["name_meaning"].lower()
            for marker in ("same as", "possibly", "uncertain", "unknown")
        )
    ]

    assert not placeholder_rows


def test_ot_proper_name_notes_only_have_known_residual_weak_meanings() -> None:
    rows = csv_rows("data/proper_name_transliteration_notes.csv")
    ot_rows = [row for row in rows if row["source"] == "ot"]
    placeholder_rows = [
        row
        for row in ot_rows
        if any(
            marker in row["name_meaning"].lower()
            for marker in ("same as", "possibly", "uncertain", "unknown", "the same as")
        )
    ]

    residual = {
        (row["first_reference"], row["name"], row["name_meaning"])
        for row in placeholder_rows
    }
    assert residual == set()


def test_nt_review_priority_queue_is_empty() -> None:
    diagnostics = nt_review_diagnostics()

    assert diagnostics["priority_rows"] == 0
    assert diagnostics["queue_rows"] == 0


def test_nt_literal_revision_queue_excludes_reviewed_pass_refs() -> None:
    script_path = ROOT / "scripts" / "apply_nt_tr_literal_revision.py"
    spec = importlib.util.spec_from_file_location("apply_nt_tr_literal_revision", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    latest_statuses = module.load_latest_review_statuses()
    source_rows = csv_rows("data/raw/tr_greek/nt_full.csv")
    needs_review_refs = {row["ref"] for row in source_rows if row["review_status"] == "needs_focused_tr_review"}
    synced_review_rows = [
        row for row in source_rows if row["review_notes"].startswith("focused TR review resolved as ")
    ]

    assert latest_statuses["Matthew 2:3"] == "keep"
    assert "Matthew 2:3" not in needs_review_refs
    assert needs_review_refs == set()
    assert len(synced_review_rows) >= 600


def test_nt_review_metadata_cleanup_has_no_stale_queue_markers() -> None:
    source_rows = csv_rows("data/raw/tr_greek/nt_full.csv")
    review_rows = nt_review_rows()
    review_diagnostics = nt_review_diagnostics()

    assert not [row["ref"] for row in source_rows if row["review_status"] == "needs_focused_tr_review"]
    assert not [row["ref"] for row in review_rows if not row["latest_review_status"]]
    assert len([row for row in source_rows if row["review_notes"].startswith("focused TR review resolved as keep")]) >= 600
    assert "unreviewed" not in review_diagnostics["latest_review_status_counts"]


def test_nt_old_revised_pass_rows_match_source_text() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}

    expected = {
        "Acts 7:19": "This one dealt craftily with our kindred, and mistreated our fathers, by making them expose their infants, so that they might not be kept alive.",
        "1 Timothy 3:14": "I write these things to you, hoping to come to you shortly:",
    }
    for ref, draft_translation in expected.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"


def test_nt_second_corinthians_5_focused_queue_revisions_stay_reviewed() -> None:
    by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}

    expected = {
        "2 Corinthians 5:2": "For also in this we groan, longing to be clothed over with our dwelling which is from heaven:",
        "2 Corinthians 5:4": "For also we who are in this tent groan, being burdened, because we do not wish to be unclothed, but to be clothed over, so that the mortal may be swallowed up by life.",
        "2 Corinthians 5:7": "For we walk by faith, not by appearance.",
        "2 Corinthians 5:18": "But all things are from God, who reconciled us to himself through Jesus Christ, and gave to us the ministry of reconciliation;",
        "2 Corinthians 5:21": "For he made the one who did not know sin to be sin for us, so that we might become righteousness of God in him.",
    }
    for ref, draft_translation in expected.items():
        assert by_ref[ref]["draft_translation"] == draft_translation
        assert by_ref[ref]["review_status"] == "tr_literal_manual"
        assert by_ref[ref]["review_notes"] == "manual TR literal override"


def test_nt_second_corinthians_6_to_8_queue_revisions_and_keeps_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "2 Corinthians 6:4": "But in everything commending ourselves as servants of God, in much endurance, in afflictions, in necessities, in distresses,",
        "2 Corinthians 7:6": "But God, who comforts the lowly, comforted us by the presence of Titus;",
        "2 Corinthians 7:8": "For even if I grieved you with the letter, I do not regret it, though I did regret it: for I see that that letter grieved you, even if for a short time.",
        "2 Corinthians 7:10": "For sorrow according to God works repentance to salvation without regret, but the sorrow of the world works death.",
        "2 Corinthians 8:13": "For it is not that others have relief and you affliction, but by equality; at the present time your abundance is for their lack,",
        "2 Corinthians 8:14": "so that also their abundance may be for your lack, so that there may be equality:",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_146.md"
        assert ref not in queue_refs

    for ref in ("2 Corinthians 6:10", "2 Corinthians 7:16"):
        assert review_by_ref[ref]["latest_review_status"] == "keep"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_146.md"
        assert ref not in queue_refs


def test_nt_second_corinthians_8_to_9_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected = {
        "2 Corinthians 8:22": "And we sent with them our brother, whom we often proved in many things to be diligent, but now much more diligent by great confidence toward you.",
        "2 Corinthians 9:2": "For I know your readiness, for which I boast about you to Macedonians, that Achaia has been ready since last year; and your zeal stirred up the majority.",
        "2 Corinthians 9:7": "Let each one give as he purposes in the heart, not from sorrow or from necessity: for God loves a cheerful giver.",
        "2 Corinthians 9:14": "and in their prayer for you, longing for you because of the surpassing grace of God upon you.",
    }
    for ref, draft_translation in expected.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_147.md"
        assert ref not in queue_refs


def test_nt_second_corinthians_10_queue_revisions_and_keep_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "2 Corinthians 10:1": "Now I Paul myself plead with you through the meekness and gentleness of Christ, who in person am lowly among you, but being absent am bold toward you:",
        "2 Corinthians 10:3": "For though we walk in flesh, we do not wage war according to flesh:",
        "2 Corinthians 10:4": "For the weapons of our warfare are not fleshly, but powerful by God for pulling down strongholds;",
        "2 Corinthians 10:5": "casting down reasonings, and every high thing lifted up against the knowledge of God, and taking every thought captive to the obedience of Christ;",
        "2 Corinthians 10:6": "and being ready to avenge all disobedience, when your obedience is completed.",
        "2 Corinthians 10:12": "For we do not dare to class or compare ourselves with some who commend themselves; but they, measuring themselves by themselves, and comparing themselves with themselves, do not understand.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_148.md"
        assert ref not in queue_refs

    assert review_by_ref["2 Corinthians 10:9"]["latest_review_status"] == "keep"
    assert review_by_ref["2 Corinthians 10:9"]["latest_review_pass"] == "nt_review_pass_148.md"
    assert "2 Corinthians 10:9" not in queue_refs


def test_nt_second_corinthians_11_queue_revisions_and_keep_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "2 Corinthians 11:2": "For I am jealous for you with God's jealousy: for I joined you to one husband, to present a pure virgin to Christ.",
        "2 Corinthians 11:13": "For such ones are false apostles, deceitful workers, transforming themselves into apostles of Christ.",
        "2 Corinthians 11:14": "And no wonder; for Satan himself transforms himself into an angel of light.",
        "2 Corinthians 11:15": "Therefore it is no great thing if his servants also transform themselves as servants of righteousness; whose end shall be according to their works.",
        "2 Corinthians 11:21": "I speak according to dishonor, as though we had been weak. But in whatever anyone is bold, I speak in foolishness, I also am bold.",
        "2 Corinthians 11:24": "By Jews five times I received forty stripes minus one.",
        "2 Corinthians 11:25": "Three times I was beaten with rods; once I was stoned; three times I was shipwrecked; I have spent a night and a day in the deep;",
        "2 Corinthians 11:27": "In labor and hardship, in watchings often, in hunger and thirst, in fastings often, in cold and nakedness.",
        "2 Corinthians 11:32": "In Damascus, the governor under Aretas the king guarded the city of the Damascenes, wanting to seize me:",
        "2 Corinthians 11:33": "and through a window I was let down in a basket through the wall, and escaped his hands.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_149.md"
        assert ref not in queue_refs

    assert review_by_ref["2 Corinthians 11:22"]["latest_review_status"] == "keep"
    assert review_by_ref["2 Corinthians 11:22"]["latest_review_pass"] == "nt_review_pass_149.md"
    assert "2 Corinthians 11:22" not in queue_refs


def test_nt_second_corinthians_12_to_13_queue_revisions_and_keeps_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "2 Corinthians 12:7": "And by the surpassing greatness of the revelations, lest I should be exalted above measure, a thorn in the flesh was given to me, a messenger of Satan, that he might buffet me, lest I should be exalted above measure.",
        "2 Corinthians 12:10": "Therefore I take pleasure in weaknesses, in reproaches, in necessities, in persecutions, in distresses for Christ: for when I am weak, then I am strong.",
        "2 Corinthians 12:15": "And I will very gladly spend and be fully spent for your souls; though the more abundantly I love you, the less I am loved.",
        "2 Corinthians 12:16": "But be it so, I did not burden you: but, being crafty, I took you by deceit.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_150.md"
        assert ref not in queue_refs

    for ref in ("2 Corinthians 12:3", "2 Corinthians 13:4", "2 Corinthians 13:8"):
        assert review_by_ref[ref]["latest_review_status"] == "keep"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_150.md"
        assert ref not in queue_refs


def test_nt_galatians_1_queue_revisions_and_keeps_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Galatians 1:4": "Who gave himself for our sins, that he might deliver us out of this present evil age, according to the will of our God and Father:",
        "Galatians 1:12": "For I neither received it from man, nor was I taught it, but by revelation of Jesus Christ.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_151.md"
        assert ref not in queue_refs

    for ref in ("Galatians 1:15", "Galatians 1:21", "Galatians 1:24"):
        assert review_by_ref[ref]["latest_review_status"] == "keep"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_151.md"
        assert ref not in queue_refs


def test_nt_galatians_2_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Galatians 2:1": "Then after fourteen years I went up again to Jerusalem with Barnabas, taking Titus also with me.",
        "Galatians 2:3": "But not even Titus, who was with me, being Greek, was compelled to be circumcised:",
        "Galatians 2:10": "Only that we should remember the poor, the very thing I also was eager to do.",
        "Galatians 2:18": "For if I build again the things that I destroyed, I establish myself as a transgressor.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_152.md"
        assert ref not in queue_refs


def test_nt_galatians_3_queue_revisions_and_keep_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Galatians 3:6": "Just as Abraham believed God, and it was reckoned to him for righteousness.",
        "Galatians 3:10": "For as many as are from works of law are under a curse: for it is written, Cursed is everyone who does not continue in all things written in the book of the law, to do them.",
        "Galatians 3:12": "And the law is not from faith: but, The man who does them shall live in them.",
        "Galatians 3:13": "Christ redeemed us from the curse of the law, having become a curse for us: for it is written, Cursed is everyone who hangs on a tree:",
        "Galatians 3:18": "For if the inheritance is from law, it is no longer from promise: but God has graciously granted it to Abraham through promise.",
        "Galatians 3:20": "Now a mediator is not of one, but God is one.",
        "Galatians 3:25": "But after faith came, we are no longer under a schoolmaster.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_153.md"
        assert ref not in queue_refs

    assert review_by_ref["Galatians 3:27"]["latest_review_status"] == "keep"
    assert review_by_ref["Galatians 3:27"]["latest_review_pass"] == "nt_review_pass_153.md"
    assert "Galatians 3:27" not in queue_refs


def test_nt_galatians_4_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Galatians 4:2": "But he is under guardians and stewards until the time appointed by the father.",
        "Galatians 4:3": "So also we, when we were children, were enslaved under the elements of the world:",
        "Galatians 4:16": "So then, have I become your enemy by telling you the truth?",
        "Galatians 4:18": "But it is good to be zealous always in a good thing, and not only when I am present with you.",
        "Galatians 4:19": "My little children, for whom I travail in birth again until Christ is formed in you,",
        "Galatians 4:20": "I desired to be present with you now, and to change my voice; for I am perplexed about you.",
        "Galatians 4:22": "For it is written, that Abraham had two sons, one from the bondwoman and one from the freewoman.",
        "Galatians 4:23": "But the one from the bondwoman was born according to flesh; but the one from the freewoman through promise.",
        "Galatians 4:26": "But the Jerusalem above is free, which is mother of us all.",
        "Galatians 4:30": "But what does the scripture say? Cast out the bondwoman and her son: for the son of the bondwoman shall not inherit with the son of the freewoman.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_154.md"
        assert ref not in queue_refs


def test_nt_galatians_5_to_6_queue_revisions_and_keep_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Galatians 5:3": "And I testify again to every man who is circumcised, that he is a debtor to do the whole law.",
        "Galatians 5:12": "I wish those who unsettle you would even cut themselves off.",
        "Galatians 5:23": "Meekness, self-control: against such there is no law.",
        "Galatians 5:26": "Let us not become vain-glorious, provoking one another, envying one another.",
        "Galatians 6:3": "For if anyone thinks himself to be something, being nothing, he deceives himself.",
        "Galatians 6:4": "But let each one prove his own work, and then he shall have boasting in himself alone, and not in another.",
        "Galatians 6:5": "For each one shall bear his own load.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_155.md"
        assert ref not in queue_refs

    assert review_by_ref["Galatians 5:9"]["latest_review_status"] == "keep"
    assert review_by_ref["Galatians 5:9"]["latest_review_pass"] == "nt_review_pass_155.md"
    assert "Galatians 5:9" not in queue_refs


def test_nt_ephesians_1_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Ephesians 1:10": "For the dispensation of the fullness of the times, to sum up all things in Christ, the things in the heavens and the things on the earth, in him:",
        "Ephesians 1:11": "In whom also we obtained an inheritance, being predestined according to the purpose of him who works all things according to the counsel of his will:",
        "Ephesians 1:12": "that we should be to the praise of his glory, we who first hoped in Christ.",
        "Ephesians 1:16": "I do not cease giving thanks for you, making mention of you in my prayers;",
        "Ephesians 1:19": "And what is the surpassing greatness of his power toward us who believe, according to the working of the might of his strength,",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_156.md"
        assert ref not in queue_refs


def test_nt_ephesians_2_to_3_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Ephesians 2:14": "For he himself is our peace, who made both one, and broke down the middle wall of the partition;",
        "Ephesians 2:20": "And are built upon the foundation of the apostles and prophets, Christ Jesus himself being the chief cornerstone;",
        "Ephesians 3:9": "And to make all see what is the fellowship of the mystery, which from the ages has been hidden in God, who created all things through Jesus Christ:",
        "Ephesians 3:12": "In whom we have boldness and access with confidence through his faith.",
        "Ephesians 3:15": "From whom every family in the heavens and on earth is named,",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_157.md"
        assert ref not in queue_refs


def test_nt_ephesians_4_queue_revisions_and_keep_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Ephesians 4:6": "One God and Father of all, who is over all, and through all, and in you all.",
        "Ephesians 4:9": "(Now this, he ascended, what is it except that he also first descended into the lower parts of the earth?",
        "Ephesians 4:11": "And he himself gave some as apostles, and some as prophets, and some as evangelists, and some as pastors and teachers;",
        "Ephesians 4:18": "being darkened in understanding, being alienated from the life of God because of the ignorance that is in them, because of the hardness of their heart:",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_158.md"
        assert ref not in queue_refs

    assert review_by_ref["Ephesians 4:27"]["latest_review_status"] == "keep"
    assert review_by_ref["Ephesians 4:27"]["latest_review_pass"] == "nt_review_pass_158.md"
    assert "Ephesians 4:27" not in queue_refs


def test_nt_ephesians_5_to_6_queue_revisions_and_keeps_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Ephesians 5:4": "And filthiness, and foolish talking, or jesting, which are not fitting: but rather thanksgiving.",
        "Ephesians 5:11": "And do not have fellowship with the unfruitful works of darkness, but rather even reprove them.",
        "Ephesians 5:12": "For the secret things being done by them are shameful even to speak of.",
        "Ephesians 5:21": "Submitting to one another in the fear of God.",
        "Ephesians 5:33": "Nevertheless also you, each one, let each love his own wife in this way as himself; and let the wife reverence her husband.",
        "Ephesians 6:14": "Stand therefore, having girded your loins with truth, and having put on the breastplate of righteousness;",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_159.md"
        assert ref not in queue_refs

    for ref in ("Ephesians 5:16", "Ephesians 5:30", "Ephesians 6:3"):
        assert review_by_ref[ref]["latest_review_status"] == "keep"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_159.md"
        assert ref not in queue_refs


def test_nt_philippians_1_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Philippians 1:3": "I thank my God at every remembrance of you,",
        "Philippians 1:4": "always in every prayer of mine for you all, making my prayer with joy,",
        "Philippians 1:13": "so that my bonds became manifest in Christ in the whole praetorium, and to all the rest;",
        "Philippians 1:15": "Some indeed also preach Christ through envy and strife, but some also through good will:",
        "Philippians 1:16": "Those from selfish ambition proclaim Christ, not sincerely, supposing to add affliction to my bonds:",
        "Philippians 1:21": "For to me to live is Christ, and to die is gain.",
        "Philippians 1:24": "But to remain in the flesh is more necessary for you.",
        "Philippians 1:25": "And being confident of this, I know that I shall remain and continue with you all for your progress and joy of the faith;",
        "Philippians 1:26": "that your boasting may abound in Christ Jesus in me through my presence with you again.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_160.md"
        assert ref not in queue_refs


def test_nt_philippians_2_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Philippians 2:4": "Let each not look to his own things, but each also to the things of others.",
        "Philippians 2:5": "For let this mind be in you, which was also in Christ Jesus:",
        "Philippians 2:6": "who, existing in the form of God, did not consider being equal with God a thing to be seized:",
        "Philippians 2:14": "Do all things without grumblings and reasonings:",
        "Philippians 2:21": "For all seek their own things, not the things of Christ Jesus.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_161.md"
        assert ref not in queue_refs


def test_nt_philippians_3_to_4_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Philippians 3:2": "Beware of dogs, beware of evil workers, beware of the mutilation.",
        "Philippians 3:7": "But whatever things were gains to me, these I have counted loss because of Christ.",
        "Philippians 3:12": "Not that I already obtained, or have already been perfected: but I press on, if also I may lay hold of that for which also I was laid hold of by Christ Jesus.",
        "Philippians 3:14": "I press toward the goal for the prize of the upward calling of God in Christ Jesus.",
        "Philippians 3:16": "Nevertheless, to what we have attained, let us walk by the same rule, let us mind the same thing.",
        "Philippians 3:18": "(For many walk, of whom I told you often, and now also tell you weeping, as enemies of the cross of Christ:",
        "Philippians 4:18": "But I have all things, and abound: I am full, having received from Epaphroditus the things from you, an aroma of sweet smell, an acceptable sacrifice, well-pleasing to God.",
        "Philippians 4:19": "But my God shall fill every need of yours according to his riches in glory in Christ Jesus.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_162.md"
        assert ref not in queue_refs

    assert review_by_ref["Philippians 3:19"]["latest_review_status"] == "keep"
    assert review_by_ref["Philippians 3:19"]["latest_review_pass"] == "nt_review_pass_162.md"
    assert "Philippians 3:19" not in queue_refs


def test_nt_colossians_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Colossians 1:15": "Who is the image of the invisible God, the firstborn of all creation:",
        "Colossians 1:17": "And he is before all things, and all things hold together in him.",
        "Colossians 1:19": "For in him all the fullness was pleased to dwell;",
        "Colossians 1:21": "And you, once being alienated and enemies in mind in wicked works, yet now he has reconciled",
        "Colossians 1:28": "Whom we proclaim, admonishing every man, and teaching every man in all wisdom; that we may present every man complete in Christ Jesus:",
        "Colossians 2:3": "In whom all the treasures of wisdom and knowledge are hidden.",
        "Colossians 2:9": "For in him dwells all the fullness of the Deity bodily.",
        "Colossians 2:14": "Having blotted out the handwriting in ordinances that was against us, which was contrary to us, and he has taken it out of the midst, nailing it to the cross;",
        "Colossians 2:15": "And having stripped off principalities and powers, he made a public show of them, triumphing over them in it.",
        "Colossians 2:22": "which all are for corruption with use), according to the commandments and teachings of men?",
        "Colossians 3:2": "Mind the things above, not the things on the earth.",
        "Colossians 3:6": "Because of these things the wrath of God comes upon the children of disobedience:",
        "Colossians 3:21": "Fathers, do not provoke your children, lest they be discouraged.",
        "Colossians 4:2": "Continue steadfastly in prayer, watching in it with thanksgiving;",
        "Colossians 4:18": "The greeting by my hand, Paul. Remember my bonds. Grace be with you. Amen.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_163.md"
        assert ref not in queue_refs

    for ref in ("Colossians 2:17", "Colossians 4:4", "Colossians 4:14"):
        assert review_by_ref[ref]["latest_review_status"] == "keep"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_163.md"
        assert ref not in queue_refs


def test_nt_first_thessalonians_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "1 Thessalonians 2:3": "For our exhortation was not from error, nor from uncleanness, nor in deceit:",
        "1 Thessalonians 2:6": "Nor seeking glory from men, neither from you nor from others, though we could be burdensome as apostles of Christ.",
        "1 Thessalonians 2:7": "But we were gentle among you, as a nursing mother cherishes her own children:",
        "1 Thessalonians 3:10": "Night and day praying exceedingly to see your face, and to complete the things lacking in your faith?",
        "1 Thessalonians 5:3": "For when they say, Peace and safety; then sudden destruction comes upon them, as birth pains upon a pregnant woman; and they shall not escape.",
        "1 Thessalonians 5:6": "Therefore let us not sleep, as the rest do; but let us watch and be sober.",
        "1 Thessalonians 5:10": "Who died for us, that, whether we watch or sleep, we should live together with him.",
        "1 Thessalonians 5:16": "Rejoice always.",
        "1 Thessalonians 5:20": "Do not despise prophecies.",
        "1 Thessalonians 5:21": "Test all things; hold fast the good.",
        "1 Thessalonians 5:22": "Abstain from every form of evil.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_164.md"
        assert ref not in queue_refs

    for ref in ("1 Thessalonians 1:2", "1 Thessalonians 5:17"):
        assert review_by_ref[ref]["latest_review_status"] == "keep"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_164.md"
        assert ref not in queue_refs


def test_nt_second_thessalonians_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "2 Thessalonians 2:7": "For the mystery of iniquity already works: only there is the one restraining now, until he comes out of the midst.",
        "2 Thessalonians 2:9": "whose coming is according to the working of Satan with all power and signs and wonders of falsehood,",
        "2 Thessalonians 2:11": "And because of this God shall send them a working of error, that they should believe the lie:",
        "2 Thessalonians 3:2": "And that we may be delivered from unreasonable and evil men: for the faith is not of all.",
        "2 Thessalonians 3:10": "For even when we were with you, this we commanded you, that if anyone is not willing to work, neither let him eat.",
        "2 Thessalonians 3:11": "For we hear that some walk among you disorderly, not working at all, but being busybodies.",
        "2 Thessalonians 3:15": "And do not regard him as an enemy, but admonish him as a brother.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_165.md"
        assert ref not in queue_refs


def test_nt_first_timothy_1_to_2_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "1 Timothy 1:8": "But we know that the law is good, if anyone uses it lawfully;",
        "1 Timothy 1:9": "Knowing this, that law is not laid down for a righteous one, but for lawless and unruly, for ungodly and sinners, for unholy and profane, for father-killers and mother-killers, for murderers,",
        "1 Timothy 1:13": "I who was formerly a blasphemer, and a persecutor, and an insolent man: but I obtained mercy, because being ignorant I acted in unbelief.",
        "1 Timothy 2:1": "I exhort therefore, first of all, that supplications, prayers, intercessions, and thanksgivings be made for all men;",
        "1 Timothy 2:2": "For kings, and for all who are in authority; that we may lead a quiet and tranquil life in all godliness and dignity.",
        "1 Timothy 2:6": "Who gave himself a ransom for all, the testimony in its own times.",
        "1 Timothy 2:10": "but with what befits women professing godliness, through good works.",
        "1 Timothy 2:11": "Let a woman learn in quietness with all submission.",
        "1 Timothy 2:12": "But I do not permit a woman to teach, nor to exercise authority over a man, but to be in quietness.",
        "1 Timothy 2:14": "And Adam was not deceived, but the woman, having been deceived, came to be in transgression.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_166.md"
        assert ref not in queue_refs

    for ref in ("1 Timothy 2:5", "1 Timothy 2:13"):
        assert review_by_ref[ref]["latest_review_status"] == "keep"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_166.md"
        assert ref not in queue_refs


def test_nt_first_timothy_3_to_4_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "1 Timothy 3:3": "not given to wine, not a striker, not greedy for shameful gain; but gentle, peaceable, not loving money;",
        "1 Timothy 3:4": "One ruling well his own house, having his children in submission with all dignity;",
        "1 Timothy 3:11": "Women likewise must be dignified, not slanderers, sober, faithful in all things.",
        "1 Timothy 4:2": "In hypocrisy of liars, having their own conscience seared;",
        "1 Timothy 4:4": "For every creature of God is good, and nothing is to be rejected, being received with thanksgiving:",
        "1 Timothy 4:11": "Command and teach these things.",
        "1 Timothy 4:13": "Until I come, give attention to reading, to exhortation, to teaching.",
        "1 Timothy 4:14": "Do not neglect the gift that is in you, which was given to you through prophecy, with laying on of the hands of the presbytery.",
        "1 Timothy 4:15": "Practice these things; be in them; that your progress may be manifest to all.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_167.md"
        assert ref not in queue_refs

    assert review_by_ref["1 Timothy 3:9"]["latest_review_status"] == "keep"
    assert review_by_ref["1 Timothy 3:9"]["latest_review_pass"] == "nt_review_pass_167.md"
    assert "1 Timothy 3:9" not in queue_refs


def test_nt_first_timothy_5_to_6_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "1 Timothy 5:4": "But if any widow has children or grandchildren, let them learn first to show piety toward their own house, and to give recompense to their parents: for this is good and acceptable before God.",
        "1 Timothy 5:5": "Now she who is truly a widow, and left alone, has set her hope on God, and continues in supplications and prayers night and day.",
        "1 Timothy 5:6": "But she who lives in self-indulgence is dead while she lives.",
        "1 Timothy 5:7": "And command these things, that they may be blameless.",
        "1 Timothy 5:8": "But if anyone does not provide for his own, and especially for those of his own household, he has denied the faith, and is worse than an unbeliever.",
        "1 Timothy 5:9": "Let a widow be enrolled not less than sixty years old, having been the wife of one man,",
        "1 Timothy 5:11": "But refuse younger widows: for when they grow wanton against Christ, they desire to marry;",
        "1 Timothy 5:13": "And at the same time they also learn to be idle, going about the houses; and not only idle, but also gossips and busybodies, speaking things which they ought not.",
        "1 Timothy 5:14": "Therefore I will that younger women marry, bear children, rule the house, give no occasion to the adversary for reproach.",
        "1 Timothy 5:19": "Do not receive an accusation against an elder except upon two or three witnesses.",
        "1 Timothy 5:24": "Some men's sins are manifest beforehand, going before to judgment; and some also follow after.",
        "1 Timothy 6:1": "Let as many slaves as are under the yoke count their own masters worthy of all honor, that the name of God and the teaching may not be blasphemed.",
        "1 Timothy 6:5": "constant disputes of men corrupted in mind and deprived of the truth, supposing godliness to be gain: from such withdraw yourself.",
        "1 Timothy 6:7": "For we brought nothing into the world, and it is clear that we can carry nothing out.",
        "1 Timothy 6:10": "For the love of money is a root of all the evils: which some reaching after were led astray from the faith, and pierced themselves through with many pains.",
        "1 Timothy 6:17": "Charge those who are rich in the present age not to be high-minded, nor to have hope in uncertain riches, but in the living God, who gives us richly all things to enjoy;",
        "1 Timothy 6:18": "That they do good, that they be rich in good works, ready to share, generous;",
        "1 Timothy 6:19": "storing up for themselves a good foundation for the future, that they may lay hold on eternal life.",
        "1 Timothy 6:20": "O Timothy, guard the deposit, turning away from profane empty babblings and oppositions of falsely named knowledge:",
        "1 Timothy 6:21": "which some professing have missed the mark concerning the faith. Grace be with you. Amen.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_168.md"
        assert ref not in queue_refs

    for ref in ("1 Timothy 5:2", "1 Timothy 5:15", "1 Timothy 6:6"):
        assert review_by_ref[ref]["latest_review_status"] == "keep"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_168.md"
        assert ref not in queue_refs


def test_nt_second_timothy_1_to_2_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "2 Timothy 1:4": "longing to see you, remembering your tears, that I may be filled with joy;",
        "2 Timothy 1:5": "being reminded of the sincere faith in you, which dwelt first in your grandmother Lois and your mother Eunice; and I am persuaded that it is also in you.",
        "2 Timothy 1:17": "but when he came to Rome, he sought me very diligently, and found me.",
        "2 Timothy 2:2": "And the things that you heard from me among many witnesses, entrust these to faithful men, who shall be able to teach others also.",
        "2 Timothy 2:3": "You therefore endure hardship as a good soldier of Jesus Christ.",
        "2 Timothy 2:5": "And if anyone also competes, he is not crowned unless he competes lawfully.",
        "2 Timothy 2:12": "If we endure, we shall also reign with him: if we deny him, he also will deny us:",
        "2 Timothy 2:18": "who concerning the truth have missed the mark, saying that the resurrection has already happened, and overthrow the faith of some.",
        "2 Timothy 2:23": "But refuse foolish and uninstructed questions, knowing that they beget strifes.",
        "2 Timothy 2:25": "in meekness instructing those who oppose, if perhaps God may give them repentance to the knowledge of the truth;",
        "2 Timothy 2:26": "and they may come to themselves out of the devil's snare, having been taken captive by him to his will.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_169.md"
        assert ref not in queue_refs

    assert review_by_ref["2 Timothy 1:3"]["latest_review_status"] == "keep"
    assert review_by_ref["2 Timothy 1:3"]["latest_review_pass"] == "nt_review_pass_169.md"
    assert "2 Timothy 1:3" not in queue_refs


def test_nt_second_timothy_3_to_4_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "2 Timothy 3:1": "But know this, that in the last days difficult times shall come.",
        "2 Timothy 3:2": "For men shall be lovers of themselves, lovers of money, boasters, proud, blasphemers, disobedient to parents, unthankful, unholy,",
        "2 Timothy 3:3": "without natural affection, implacable, slanderers, without self-control, savage, not lovers of good,",
        "2 Timothy 3:4": "traitors, reckless, puffed up, lovers of pleasure rather than lovers of God;",
        "2 Timothy 3:7": "always learning, and never able to come to the knowledge of the truth.",
        "2 Timothy 3:8": "Now in the same way that Jannes and Jambres resisted Moses, so these also resist the truth: men corrupted in mind, unapproved concerning the faith.",
        "2 Timothy 3:13": "But evil men and impostors will advance to worse, deceiving and being deceived.",
        "2 Timothy 3:14": "But you continue in the things which you learned and were assured of, knowing from whom you learned them;",
        "2 Timothy 3:16": "All scripture is God-breathed and profitable for teaching, for reproof, for correction, for instruction in righteousness:",
        "2 Timothy 4:3": "For the time will come when they will not endure sound teaching; but according to their own lusts they shall heap up teachers to themselves, having itching ears;",
        "2 Timothy 4:5": "But you be sober in all things, endure hardship, do the work of an evangelist, fulfill your ministry.",
        "2 Timothy 4:6": "For I am already being poured out, and the time of my departure has come.",
        "2 Timothy 4:7": "I have fought the good fight, I have finished the course, I have kept the faith:",
        "2 Timothy 4:11": "Only Luke is with me. Take Mark, and bring him with you: for he is useful to me for ministry.",
        "2 Timothy 4:12": "But Tychicus I sent to Ephesus.",
        "2 Timothy 4:19": "Greet Prisca and Aquila, and the household of Onesiphorus.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_170.md"
        assert ref not in queue_refs


def test_nt_titus_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Titus 1:2": "in hope of eternal life, which God, who cannot lie, promised before eternal times;",
        "Titus 1:5": "For this cause I left you in Crete, that you should set in order the things that are lacking, and appoint elders in every city, as I directed you:",
        "Titus 1:6": "if anyone is blameless, the husband of one wife, having faithful children not accused of dissipation or insubordination.",
        "Titus 1:8": "but hospitable, a lover of good, sober-minded, just, holy, self-controlled;",
        "Titus 1:10": "For there are many unruly men, vain talkers and deceivers, especially those of the circumcision:",
        "Titus 1:11": "whose mouths must be stopped, who overturn whole houses, teaching things which they ought not, for shameful gain's sake.",
        "Titus 1:12": "One of themselves, a prophet of their own, said, Cretans are always liars, evil beasts, idle bellies.",
        "Titus 1:14": "not giving heed to Jewish fables, and commandments of men who turn away from the truth.",
        "Titus 2:1": "But speak the things which befit sound teaching:",
        "Titus 2:4": "that they may train the young women to love their husbands, to love their children,",
        "Titus 2:6": "The younger men likewise exhort to be sober-minded.",
        "Titus 2:7": "in all things showing yourself a pattern of good works: in teaching, incorruptness, dignity, sincerity,",
        "Titus 2:11": "For the saving grace of God has appeared to all men,",
        "Titus 2:12": "teaching us that, denying ungodliness and worldly lusts, we should live soberly, righteously, and godly in the present age;",
        "Titus 3:1": "Remind them to be subject to rulers and authorities, to obey, to be ready for every good work,",
        "Titus 3:9": "But avoid foolish questions, and genealogies, and contentions, and fights about the law; for they are unprofitable and vain.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_171.md"
        assert ref not in queue_refs


def test_nt_philemon_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Philemon 1:4": "I thank my God, always making mention of you in my prayers,",
        "Philemon 1:6": "that the fellowship of your faith may become effective in the knowledge of every good thing which is in you toward Christ Jesus.",
        "Philemon 1:10": "I plead with you concerning my child Onesimus, whom I begot in my bonds:",
        "Philemon 1:11": "who once was useless to you, but now useful to you and to me:",
        "Philemon 1:14": "But without your consent I wished to do nothing; that your good might not be as by necessity, but willingly.",
        "Philemon 1:17": "If therefore you have me as a partner, receive him as me.",
        "Philemon 1:23": "Epaphras, my fellow-prisoner in Christ Jesus, greets you;",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_172.md"
        assert ref not in queue_refs


def test_nt_hebrews_1_to_2_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Hebrews 1:4": "having become so much better than the angels, as he has inherited a more excellent name than they.",
        "Hebrews 1:6": "And again, when he brings the firstborn into the inhabited world, he says, And let all the angels of God worship him.",
        "Hebrews 1:9": "You have loved righteousness, and hated lawlessness; because of this God, your God, has anointed you with the oil of gladness beyond your companions.",
        "Hebrews 1:12": "And as a mantle you shall roll them up, and they shall be changed: but you are the same, and your years shall not fail.",
        "Hebrews 2:6": "But someone somewhere testified, saying, What is man, that you are mindful of him? or the son of man, that you visit him?",
        "Hebrews 2:8": "You subjected all things under his feet. For in subjecting all things to him, he left nothing unsubjected to him. But now we do not yet see all things subjected to him.",
        "Hebrews 2:15": "and deliver those who through fear of death were all their life subject to slavery.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_173.md"
        assert ref not in queue_refs


def test_nt_hebrews_3_to_4_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Hebrews 3:8": "Do not harden your hearts, as in the provocation, in the day of testing in the wilderness:",
        "Hebrews 3:9": "where your fathers tested me, proved me, and saw my works forty years.",
        "Hebrews 3:16": "For who, when they heard, provoked? was it not all who came out of Egypt by Moses?",
        "Hebrews 3:18": "And to whom did he swear that they should not enter into his rest, but to those who disobeyed?",
        "Hebrews 3:19": "And we see that they could not enter because of unbelief.",
        "Hebrews 4:1": "Let us therefore fear, lest, a promise remaining of entering into his rest, any of you should seem to have come short.",
        "Hebrews 4:3": "For we who have believed enter into the rest, as he said, As I swore in my wrath, They shall not enter into my rest: although the works were finished from the foundation of the world.",
        "Hebrews 4:4": "For he spoke somewhere concerning the seventh day in this way, And God rested on the seventh day from all his works.",
        "Hebrews 4:5": "And in this place again, They shall not enter into my rest.",
        "Hebrews 4:8": "For if Joshua had given them rest, he would not afterward have spoken of another day.",
        "Hebrews 4:9": "There remains therefore a Sabbath rest for the people of God.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_174.md"
        assert ref not in queue_refs

    assert review_by_ref["Hebrews 3:11"]["latest_review_status"] == "keep"
    assert review_by_ref["Hebrews 3:11"]["latest_review_pass"] == "nt_review_pass_174.md"
    assert "Hebrews 3:11" not in queue_refs


def test_nt_hebrews_5_to_6_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Hebrews 5:1": "For every high priest taken from among men is appointed on behalf of men in things pertaining to God, that he may offer both gifts and sacrifices for sins:",
        "Hebrews 5:8": "Though he was a Son, he learned obedience from the things which he suffered;",
        "Hebrews 6:2": "of teaching about baptisms, and of laying on of hands, and of resurrection of the dead, and of eternal judgment.",
        "Hebrews 6:3": "And this we will do, if God permits.",
        "Hebrews 6:9": "But, beloved, we are persuaded concerning you of better things, and things belonging to salvation, though we speak thus.",
        "Hebrews 6:13": "For when God promised Abraham, because he had no greater by whom to swear, he swore by himself,",
        "Hebrews 6:15": "And so, having patiently endured, he obtained the promise.",
        "Hebrews 6:18": "that by two immutable things, in which it is impossible for God to lie, we who have fled for refuge might have strong encouragement to lay hold of the hope set before us:",
        "Hebrews 6:19": "which we have as an anchor of the soul, both sure and steadfast, and entering into the inner side of the veil;",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_175.md"
        assert ref not in queue_refs

    assert review_by_ref["Hebrews 6:14"]["latest_review_status"] == "keep"
    assert review_by_ref["Hebrews 6:14"]["latest_review_pass"] == "nt_review_pass_175.md"
    assert "Hebrews 6:14" not in queue_refs


def test_nt_hebrews_7_to_8_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Hebrews 7:1": "For this Melchisedec, king of Salem, priest of the Most High God, who met Abraham returning from the slaughter of the kings, and blessed him;",
        "Hebrews 7:7": "And without any dispute the lesser is blessed by the better.",
        "Hebrews 7:8": "And here dying men receive tithes; but there one receives them, of whom it is witnessed that he lives.",
        "Hebrews 7:9": "And, so to speak, through Abraham Levi also, who receives tithes, has paid tithes.",
        "Hebrews 7:10": "For he was still in the loins of his father when Melchisedec met him.",
        "Hebrews 7:11": "If therefore perfection was through the Levitical priesthood, (for upon it the people received the law,) what further need was there for another priest to arise according to the order of Melchisedec, and not be called according to the order of Aaron?",
        "Hebrews 7:12": "For when the priesthood is changed, of necessity a change of the law also takes place.",
        "Hebrews 7:16": "who has become, not according to the law of a fleshly commandment, but according to the power of an indestructible life.",
        "Hebrews 7:20": "And inasmuch as it was not without oath-taking:",
        "Hebrews 7:24": "But he, because he remains forever, has the unchangeable priesthood.",
        "Hebrews 7:27": "who does not have daily need, as those high priests, first to offer sacrifices for his own sins, then for the people's: for this he did once for all, having offered up himself.",
        "Hebrews 8:4": "For if he were on earth, he would not be a priest, there being priests who offer gifts according to the law:",
        "Hebrews 8:6": "But now he has obtained a more excellent ministry, by as much as he is mediator of a better covenant, which has been enacted upon better promises.",
        "Hebrews 8:7": "For if that first had been faultless, no place would have been sought for a second.",
        "Hebrews 8:12": "For I will be merciful to their unrighteousness, and their sins and their lawless deeds I will remember no more.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_176.md"
        assert ref not in queue_refs


def test_nt_hebrews_9_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Hebrews 9:3": "And after the second veil, the tabernacle which is called Holy of Holies;",
        "Hebrews 9:5": "And over it the cherubim of glory overshadowing the mercy seat; concerning which we cannot now speak in detail.",
        "Hebrews 9:6": "Now these things having been thus prepared, the priests always enter into the first tabernacle, performing the services.",
        "Hebrews 9:7": "But into the second the high priest alone enters once every year, not without blood, which he offers for himself, and for the ignorances of the people:",
        "Hebrews 9:12": "nor by blood of goats and calves, but by his own blood he entered once for all into the holy places, having obtained eternal redemption.",
        "Hebrews 9:19": "For when every commandment had been spoken by Moses to all the people according to the law, he took the blood of calves and goats, with water, and scarlet wool, and hyssop, and sprinkled both the book itself, and all the people,",
        "Hebrews 9:20": "saying, This is the blood of the covenant which God commanded to you.",
        "Hebrews 9:21": "Moreover he sprinkled with the blood both the tabernacle, and all the vessels of the service.",
        "Hebrews 9:23": "It was therefore necessary that the copies of the things in the heavens be purified with these; but the heavenly things themselves with better sacrifices than these.",
        "Hebrews 9:24": "For Christ did not enter into holy places made with hands, copies of the true, but into heaven itself, now to appear before the face of God for us:",
        "Hebrews 9:25": "Nor yet that he should offer himself often, as the high priest enters into the holy places every year with another's blood;",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_177.md"
        assert ref not in queue_refs


def test_nt_hebrews_10_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Hebrews 10:3": "But in them there is a remembrance of sins every year.",
        "Hebrews 10:4": "For it is impossible for blood of bulls and goats to take away sins.",
        "Hebrews 10:6": "In burnt offerings and offerings for sin you had no pleasure.",
        "Hebrews 10:11": "And every priest stands daily ministering and often offering the same sacrifices, which can never take away sins:",
        "Hebrews 10:17": "And their sins and their lawless deeds I will remember no more.",
        "Hebrews 10:20": "by a new and living way, which he inaugurated for us, through the veil, that is, his flesh;",
        "Hebrews 10:22": "Let us draw near with a true heart in full assurance of faith, having our hearts sprinkled from an evil conscience, and our body washed with pure water.",
        "Hebrews 10:26": "For if we sin willingly after receiving the knowledge of the truth, there remains no more sacrifice for sins,",
        "Hebrews 10:27": "But a certain fearful expectation of judgment and fiery zeal, about to devour the adversaries.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_178.md"
        assert ref not in queue_refs

    assert review_by_ref["Hebrews 10:31"]["latest_review_status"] == "keep"
    assert review_by_ref["Hebrews 10:31"]["latest_review_pass"] == "nt_review_pass_178.md"
    assert "Hebrews 10:31" not in queue_refs


def test_nt_hebrews_11_1_to_18_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Hebrews 11:2": "For by it the elders obtained testimony.",
        "Hebrews 11:5": "By faith Enoch was translated so that he should not see death; and was not found, because God had translated him: for before his translation he had testimony that he pleased God.",
        "Hebrews 11:7": "By faith Noah, being warned of God concerning things not yet seen, moved with fear, prepared an ark for the salvation of his house; through which he condemned the world, and became heir of the righteousness which is by faith.",
        "Hebrews 11:8": "By faith Abraham, when called, obeyed to go out to the place which he was about to receive for an inheritance; and he went out, not knowing where he was going.",
        "Hebrews 11:9": "By faith he sojourned in the land of promise, as in a foreign land, dwelling in tents with Isaac and Jacob, co-heirs of the same promise:",
        "Hebrews 11:10": "For he waited for the city which has foundations, whose builder and maker is God.",
        "Hebrews 11:12": "Therefore also from one, and him as good as dead, were begotten as many as the stars of heaven in multitude, and as the sand which is by the seashore innumerable.",
        "Hebrews 11:13": "These all died according to faith, not having received the promises, but having seen them afar off, and been persuaded, and greeted them, and confessed that they were strangers and pilgrims on the earth.",
        "Hebrews 11:18": "to whom it was said, In Isaac shall your seed be called:",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_179.md"
        assert ref not in queue_refs

    assert review_by_ref["Hebrews 11:1"]["latest_review_status"] == "keep"
    assert review_by_ref["Hebrews 11:1"]["latest_review_pass"] == "nt_review_pass_179.md"
    assert "Hebrews 11:1" not in queue_refs


def test_nt_hebrews_11_20_to_40_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Hebrews 11:22": "By faith Joseph, when dying, made mention concerning the exodus of the children of Israel; and gave command concerning his bones.",
        "Hebrews 11:23": "By faith Moses, when he was born, was hidden three months by his parents, because they saw he was a beautiful child; and they were not afraid of the king's decree.",
        "Hebrews 11:25": "choosing rather to suffer affliction with the people of God than to have temporary enjoyment of sin;",
        "Hebrews 11:27": "By faith he left Egypt, not fearing the wrath of the king: for he endured, as seeing him who is invisible.",
        "Hebrews 11:29": "By faith they passed through the Red Sea as through dry land: which the Egyptians, attempting, were swallowed.",
        "Hebrews 11:30": "By faith the walls of Jericho fell, having been encircled for seven days.",
        "Hebrews 11:35": "Women received their dead by resurrection: and others were tortured, not accepting release; that they might obtain a better resurrection:",
        "Hebrews 11:38": "of whom the world was not worthy, wandering in deserts, and mountains, and caves, and holes of the earth.",
        "Hebrews 11:40": "God having provided something better concerning us, that they should not be made perfect without us.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_180.md"
        assert ref not in queue_refs

    assert review_by_ref["Hebrews 11:20"]["latest_review_status"] == "keep"
    assert review_by_ref["Hebrews 11:20"]["latest_review_pass"] == "nt_review_pass_180.md"
    assert "Hebrews 11:20" not in queue_refs


def test_nt_hebrews_12_to_13_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Hebrews 12:21": "And so fearful was the appearance that Moses said, I am terrified and trembling:)",
        "Hebrews 12:27": "And this, Yet once more, signifies the removal of the things being shaken, as of things made, that the things not being shaken may remain.",
        "Hebrews 13:11": "For the bodies of those animals whose blood is brought into the holy places by the high priest for sin are burned outside the camp.",
        "Hebrews 13:14": "For here we have no continuing city, but we seek the one to come.",
        "Hebrews 13:15": "Through him therefore let us offer the sacrifice of praise to God continually, that is, the fruit of our lips confessing his name.",
        "Hebrews 13:16": "But do not forget doing good and sharing: for with such sacrifices God is well pleased.",
        "Hebrews 13:18": "Pray for us: for we are persuaded that we have a good conscience, desiring in all things to conduct ourselves well.",
        "Hebrews 13:19": "But I more earnestly plead that you do this, that I may be restored to you sooner.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_181.md"
        assert ref not in queue_refs

    expected_keep = {
        "Hebrews 12:13",
        "Hebrews 12:20",
        "Hebrews 12:26",
        "Hebrews 12:29",
        "Hebrews 13:1",
        "Hebrews 13:25",
    }
    for ref in expected_keep:
        assert review_by_ref[ref]["latest_review_status"] == "keep"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_181.md"
        assert ref not in queue_refs


def test_nt_james_1_to_2_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "James 1:3": "Knowing that the testing of your faith works endurance.",
        "James 1:5": "But if any of you lacks wisdom, let him ask from God, who gives to all generously and does not reproach; and it shall be given to him.",
        "James 1:8": "A double-minded man is unstable in all his ways.",
        "James 1:9": "But let the lowly brother boast in his exaltation:",
        "James 1:10": "But the rich in his humiliation, because as a flower of grass he shall pass away.",
        "James 1:14": "But each one is tempted by his own desire, being drawn away and enticed.",
        "James 1:17": "Every good giving and every perfect gift is from above, coming down from the Father of lights, with whom there is no variation or shadow of turning.",
        "James 1:20": "For the wrath of man does not work the righteousness of God.",
        "James 1:24": "For he observed himself, and has gone away, and immediately forgot what kind he was.",
        "James 1:27": "Pure and undefiled religion before God and the Father is this, to visit orphans and widows in their affliction, to keep oneself unstained from the world.",
        "James 2:13": "For judgment is without mercy to the one who has done no mercy; and mercy boasts over judgment.",
        "James 2:15": "If a brother or sister is naked, and lacking daily food,",
        "James 2:17": "So also faith, if it does not have works, is dead by itself.",
        "James 2:20": "But do you want to know, O empty man, that faith without works is dead?",
        "James 2:21": "Was not Abraham our father justified by works, having offered Isaac his son upon the altar?",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_182.md"
        assert ref not in queue_refs


def test_nt_james_3_to_5_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "James 3:7": "For every kind of beasts and birds, of reptiles and sea creatures, is tamed and has been tamed by human nature:",
        "James 3:11": "Does a spring pour forth from the same opening the sweet and the bitter?",
        "James 3:15": "This wisdom is not coming down from above, but is earthly, natural, demonic.",
        "James 3:16": "For where jealousy and strife are, there is disorder and every evil practice.",
        "James 3:17": "But the wisdom from above is first pure, then peaceable, gentle, easily entreated, full of mercy and good fruits, impartial and without hypocrisy.",
        "James 4:9": "Be afflicted, and mourn, and weep: let your laughter be turned to mourning, and your joy to dejection.",
        "James 5:13": "Is anyone among you suffering? let him pray. Is anyone cheerful? let him sing praise.",
        "James 5:17": "Elijah was a man of like nature with us, and he prayed earnestly that it might not rain: and it did not rain on the earth for three years and six months.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_183.md"
        assert ref not in queue_refs

    for ref in {"James 4:7", "James 4:12"}:
        assert review_by_ref[ref]["latest_review_status"] == "keep"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_183.md"
        assert ref not in queue_refs


def test_nt_1_peter_1_to_2_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "1 Peter 1:4": "To an incorruptible and undefiled and unfading inheritance, reserved in the heavens for you,",
        "1 Peter 1:9": "receiving the end of your faith, the salvation of your souls.",
        "1 Peter 1:14": "As children of obedience, not conforming yourselves to the former desires in your ignorance:",
        "1 Peter 1:19": "but with precious blood, as of a lamb without blemish and without spot, of Christ:",
        "1 Peter 2:10": "who once were not a people, but now are the people of God: who had not obtained mercy, but now have obtained mercy.",
        "1 Peter 2:11": "Beloved, I exhort you as strangers and pilgrims to abstain from fleshly desires, which war against the soul;",
        "1 Peter 2:18": "Household servants, be subject in all fear to your masters; not only to the good and gentle, but also to the perverse.",
        "1 Peter 2:19": "For this is grace, if because of conscience toward God someone endures griefs, suffering unjustly.",
        "1 Peter 2:22": "who did no sin, neither was deceit found in his mouth:",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_184.md"
        assert ref not in queue_refs


def test_nt_1_peter_3_to_5_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "1 Peter 3:3": "whose adornment let it not be outward, in braiding hair and wearing gold, or putting on garments;",
        "1 Peter 3:11": "Let him turn away from evil, and do good; let him seek peace, and pursue it.",
        "1 Peter 4:2": "so that he no longer should live the remaining time in the flesh to the desires of men, but to the will of God.",
        "1 Peter 4:9": "Be hospitable to one another without grumblings.",
        "1 Peter 4:15": "But let none of you suffer as a murderer, or thief, or evildoer, or as a meddler in others' matters.",
        "1 Peter 4:18": "And if the righteous is saved with difficulty, where shall the ungodly and sinner appear?",
        "1 Peter 5:3": "not as lording it over the allotted portions, but becoming examples to the flock.",
        "1 Peter 5:7": "Casting all your anxiety upon him; for he cares for you.",
        "1 Peter 5:8": "Be sober, watch; because your adversary the devil walks about as a roaring lion, seeking whom he may devour:",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_185.md"
        assert ref not in queue_refs

    assert review_by_ref["1 Peter 5:6"]["latest_review_status"] == "keep"
    assert review_by_ref["1 Peter 5:6"]["latest_review_pass"] == "nt_review_pass_185.md"
    assert "1 Peter 5:6" not in queue_refs


def test_nt_2_peter_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "2 Peter 1:5": "And for this very thing, bringing in all diligence, supply virtue in your faith; and in virtue knowledge;",
        "2 Peter 1:6": "and in knowledge self-control; and in self-control endurance; and in endurance godliness;",
        "2 Peter 1:18": "And we heard this voice brought from heaven, being with him on the holy mountain.",
        "2 Peter 1:20": "Knowing this first, that no prophecy of Scripture comes from one's own interpretation.",
        "2 Peter 2:2": "And many shall follow their destructive ways; because of whom the way of truth shall be blasphemed.",
        "2 Peter 2:5": "And he did not spare the ancient world, but preserved Noah, the eighth, a preacher of righteousness, having brought a flood upon the world of the ungodly;",
        "2 Peter 2:12": "But these, as irrational natural animals, born for capture and corruption, blaspheming in things they are ignorant of, shall be utterly corrupted in their own corruption;",
        "2 Peter 2:15": "having left the straight way, they went astray, following the way of Balaam the son of Bosor, who loved the wage of unrighteousness;",
        "2 Peter 3:3": "Knowing this first, that in the last days scoffers shall come, walking according to their own desires,",
        "2 Peter 3:4": "and saying, Where is the promise of his coming? for since the fathers fell asleep, all things continue thus from the beginning of creation.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_186.md"
        assert ref not in queue_refs


def test_nt_1_john_1_to_3_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "1 John 1:6": "If we say that we have fellowship with him, and walk in darkness, we lie, and do not practice the truth:",
        "1 John 2:16": "For everything in the world, the desire of the flesh, and the desire of the eyes, and the pride of life, is not from the Father, but is from the world.",
        "1 John 2:25": "And this is the promise which he promised us, the eternal life.",
        "1 John 2:28": "And now, little children, remain in him; that, when he is manifested, we may have confidence, and not be ashamed before him at his coming.",
        "1 John 3:2": "Beloved, now we are children of God, and it has not yet been manifested what we shall be: but we know that, when he is manifested, we shall be like him; for we shall see him as he is.",
        "1 John 3:3": "And everyone who has this hope set on him purifies himself, even as he is pure.",
        "1 John 3:20": "For if our heart condemns us, God is greater than our heart, and knows all things.",
        "1 John 3:21": "Beloved, if our heart does not condemn us, we have confidence toward God.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_187.md"
        assert ref not in queue_refs

    for ref in {"1 John 1:8", "1 John 1:9"}:
        assert review_by_ref[ref]["latest_review_status"] == "keep"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_187.md"
        assert ref not in queue_refs


def test_nt_1_john_4_to_5_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "1 John 4:5": "They are from the world: therefore they speak from the world, and the world hears them.",
        "1 John 4:21": "And this commandment we have from him, That he who loves God love his brother also.",
        "1 John 5:11": "And this is the testimony, that God has given to us eternal life, and this life is in his Son.",
        "1 John 5:19": "And we know that we are from God, and the whole world lies in the evil one.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_188.md"
        assert ref not in queue_refs

    for ref in {"1 John 4:11", "1 John 4:19", "1 John 5:2", "1 John 5:21"}:
        assert review_by_ref[ref]["latest_review_status"] == "keep"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_188.md"
        assert ref not in queue_refs


def test_nt_2_john_and_3_john_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "2 John 1:4": "I rejoiced greatly because I have found some of your children walking in truth, as we received commandment from the Father.",
        "3 John 1:2": "Beloved, concerning all things I pray that you prosper and be in health, just as your soul prospers.",
        "3 John 1:4": "I have no greater joy than these things, that I hear my children walking in truth.",
        "3 John 1:8": "We therefore ought to receive such, that we may become fellow-workers with the truth.",
        "3 John 1:14": "But I hope to see you shortly, and we shall speak mouth to mouth. Peace to you. The friends greet you. Greet the friends by name.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_189.md"
        assert ref not in queue_refs

    assert review_by_ref["2 John 1:13"]["latest_review_status"] == "keep"
    assert review_by_ref["2 John 1:13"]["latest_review_pass"] == "nt_review_pass_189.md"
    assert "2 John 1:13" not in queue_refs


def test_nt_jude_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Jude 1:8": "Likewise nevertheless these also, dreaming, defile the flesh, reject lordship, and blaspheme glories.",
        "Jude 1:15": "to execute judgment against all, and to convict all the ungodly among them concerning all their works of ungodliness which they have ungodly committed, and concerning all the harsh things which ungodly sinners have spoken against him.",
        "Jude 1:16": "These are murmurers, complainers, walking according to their own desires; and their mouth speaks swelling things, admiring persons for advantage.",
        "Jude 1:18": "that they told you, In the last time there shall be mockers, walking according to their own ungodly desires.",
        "Jude 1:22": "And on some have mercy, making a distinction:",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_190.md"
        assert ref not in queue_refs


def test_nt_jude_living_creature_cleanup_stays_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    assert (
        source_by_ref["Jude 1:10"]["draft_translation"]
        == "But these speak evil of as many things as they do not know: but what things they understand naturally, as irrational living creatures, in these things they corrupt themselves."
    )
    assert source_by_ref["Jude 1:10"]["review_status"] == "tr_literal_manual"
    assert source_by_ref["Jude 1:10"]["review_notes"] == "manual TR literal override"
    assert review_by_ref["Jude 1:10"]["latest_review_status"] == "revised"
    assert review_by_ref["Jude 1:10"]["latest_review_pass"] == "nt_review_pass_202.md"
    assert "Jude 1:10" not in queue_refs


def test_nt_revelation_1_to_3_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Revelation 1:12": "And I turned to see the voice which spoke with me. And having turned, I saw seven golden lampstands;",
        "Revelation 1:16": "And having in his right hand seven stars: and out of his mouth a sharp two-edged sword proceeding: and his appearance was as the sun shines in its strength.",
        "Revelation 1:19": "Write the things which you saw, and the things which are, and the things which are about to happen after these things;",
        "Revelation 2:6": "But this you have, that you hate the works of the Nicolaitanes, which I also hate.",
        "Revelation 2:27": "And he shall shepherd them with a rod of iron; as the vessels of a potter are broken to pieces: as I also have received from my Father.",
        "Revelation 3:2": "Become watchful, and strengthen the remaining things which are about to die: for I have not found your works fulfilled before God.",
        "Revelation 3:3": "Remember therefore how you have received and heard, and keep, and repent. If therefore you shall not watch, I will come upon you as a thief, and you shall by no means know what hour I will come upon you.",
        "Revelation 3:15": "I know your works, that you are neither cold nor hot: I wish you were cold or hot.",
        "Revelation 3:16": "So then because you are lukewarm, and neither cold nor hot, I am about to vomit you out of my mouth.",
        "Revelation 3:19": "As many as I love, I reprove and discipline: be zealous therefore, and repent.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_191.md"
        assert ref not in queue_refs

    for ref in {"Revelation 1:14", "Revelation 2:28"}:
        assert review_by_ref[ref]["latest_review_status"] == "keep"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_191.md"
        assert ref not in queue_refs


def test_nt_revelation_4_to_6_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Revelation 4:7": "And the first living creature was like a lion, and the second living creature like a calf, and the third living creature having the face as a man, and the fourth living creature like a flying eagle.",
        "Revelation 5:11": "And I saw, and I heard a voice of many angels around the throne and the living creatures and the elders: and their number was myriads of myriads, and thousands of thousands;",
        "Revelation 6:1": "And I saw when the Lamb opened one of the seals, and I heard one of the four living creatures saying, as with a voice of thunder, Come and see.",
        "Revelation 6:3": "And when he opened the second seal, I heard the second living creature saying, Come and see.",
        "Revelation 6:7": "And when he opened the fourth seal, I heard a voice of the fourth living creature saying, Come and see.",
        "Revelation 6:14": "And the heaven was separated as a scroll being rolled up; and every mountain and island were moved out of their places.",
        "Revelation 6:15": "And the kings of the earth, and the great ones, and the rich, and the commanders of thousands, and the mighty, and every slave, and every free man, hid themselves in the caves and in the rocks of the mountains;",
        "Revelation 6:17": "For the great day of his wrath has come; and who is able to stand?",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_192.md"
        assert ref not in queue_refs


def test_nt_revelation_zoon_rows_use_living_creature_language() -> None:
    zoon_re = re.compile(r"(?<!\S)ζω(?:ον|ου|α|ων)(?!\S)")
    offenders = {
        row["ref"]: row["draft_translation"]
        for row in csv_rows("data/raw/tr_greek/nt_full.csv")
        if row["book_name"] == "Revelation"
        and zoon_re.search(row["greek_text"])
        and re.search(r"\bbeasts?\b", row["draft_translation"], re.I)
    }

    assert offenders == {}


def test_nt_revelation_7_to_8_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Revelation 7:1": "And after these things I saw four angels standing on the four corners of the earth, holding the four winds of the earth, that no wind should blow on the earth, nor on the sea, nor on any tree.",
        "Revelation 7:2": "And I saw another angel ascending from the rising of the sun, having the seal of the living God: and he cried with a great voice to the four angels, to whom it was given to harm the earth and the sea,",
        "Revelation 7:16": "They shall hunger no more, neither thirst anymore; neither shall the sun fall upon them, nor any burning heat.",
        "Revelation 8:1": "And when he opened the seventh seal, there was silence in heaven about half an hour.",
        "Revelation 8:5": "And the angel took the censer, and filled it from the fire of the altar, and cast it to the earth: and there were voices, and thunders, and lightnings, and an earthquake.",
        "Revelation 8:9": "And the third of the creatures in the sea, those having life, died; and the third of the ships were destroyed.",
        "Revelation 8:10": "And the third angel sounded, and a great star fell from heaven, burning as a lamp, and it fell upon the third of the rivers, and upon the springs of waters;",
        "Revelation 8:11": "And the name of the star is called Wormwood: and the third of the waters became wormwood; and many of men died from the waters, because they were made bitter.",
        "Revelation 8:12": "And the fourth angel sounded, and the third of the sun was struck, and the third of the moon, and the third of the stars; so that the third of them might be darkened, and the day might not shine for a third of it, and the night likewise.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_193.md"
        assert ref not in queue_refs

    assert review_by_ref["Revelation 7:7"]["latest_review_status"] == "keep"
    assert review_by_ref["Revelation 7:7"]["latest_review_pass"] == "nt_review_pass_193.md"
    assert "Revelation 7:7" not in queue_refs


def test_nt_revelation_9_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Revelation 9:2": "And he opened the pit of the abyss; and smoke arose out of the pit, as smoke of a great furnace; and the sun and the air were darkened from the smoke of the pit.",
        "Revelation 9:5": "And it was given to them that they should not kill them, but that they should be tormented five months: and their torment was as the torment of a scorpion, when it strikes a man.",
        "Revelation 9:6": "And in those days men shall seek death, and shall not find it; and they shall desire to die, and death shall flee from them.",
        "Revelation 9:8": "And they had hair like women's hair, and their teeth were as lions' teeth.",
        "Revelation 9:9": "And they had breastplates as breastplates of iron; and the sound of their wings was as the sound of chariots of many horses running to war.",
        "Revelation 9:11": "And they have over them a king, the angel of the abyss; his name in Hebrew is Abaddon, and in Greek he has the name Apollyon.",
        "Revelation 9:13": "And the sixth angel sounded, and I heard one voice from the four horns of the golden altar before God,",
        "Revelation 9:16": "And the number of the armies of the cavalry was two myriads of myriads: and I heard their number.",
        "Revelation 9:18": "By these three the third of men were killed, by the fire, and by the smoke, and by the brimstone, which proceeded out of their mouths.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_194.md"
        assert ref not in queue_refs


def test_nt_revelation_10_to_11_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Revelation 10:1": "And I saw another mighty angel coming down from heaven, clothed with a cloud: and a rainbow was upon his head, and his face was as the sun, and his feet as pillars of fire:",
        "Revelation 10:2": "And he had in his hand a little scroll opened: and he set his right foot upon the sea, and the left upon the earth,",
        "Revelation 10:3": "And he cried with a great voice, as a lion roars: and when he cried, the seven thunders spoke their own voices.",
        "Revelation 10:10": "And I took the little scroll out of the angel's hand, and ate it; and it was in my mouth sweet as honey: and when I had eaten it, my belly was made bitter.",
        "Revelation 11:4": "These are the two olive trees, and the two lampstands standing before the God of the earth.",
        "Revelation 11:6": "These have authority to shut heaven, that no rain should rain in the days of their prophecy: and they have authority over the waters to turn them to blood, and to strike the earth with every plague, as often as they wish.",
        "Revelation 11:7": "And when they finish their testimony, the beast that ascends out of the abyss shall make war with them, and shall overcome them, and kill them.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_195.md"
        assert ref not in queue_refs


def test_nt_revelation_12_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Revelation 12:1": "And a great sign was seen in heaven; a woman clothed with the sun, and the moon underneath her feet, and upon her head a crown of twelve stars:",
        "Revelation 12:2": "And having in the womb, she cries, being in labor and being tormented to give birth.",
        "Revelation 12:6": "And the woman fled into the wilderness, where she has a place prepared from God, that they should nourish her there a thousand two hundred sixty days.",
        "Revelation 12:7": "And there was war in heaven: Michael and his angels fought against the dragon; and the dragon fought, and his angels,",
        "Revelation 12:9": "And the great dragon was cast down, the ancient serpent, called Devil and Satan, who deceives the whole inhabited world: he was cast down to the earth, and his angels were cast down with him.",
        "Revelation 12:14": "And to the woman were given the two wings of the great eagle, that she might fly into the wilderness, to her place, where she is nourished there for a time, and times, and half a time, from the face of the serpent.",
        "Revelation 12:15": "And the serpent cast out of his mouth water as a river after the woman, that he might make her carried away by the river.",
        "Revelation 12:16": "And the earth helped the woman, and the earth opened its mouth, and swallowed the river which the dragon cast out of his mouth.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_196.md"
        assert ref not in queue_refs


def test_nt_revelation_13_to_14_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Revelation 13:1": "And I stood upon the sand of the sea, and saw a beast ascending out of the sea, having seven heads and ten horns, and upon his horns ten diadems, and upon his heads a name of blasphemy.",
        "Revelation 13:3": "And I saw one of his heads as having been slain to death; and the wound of his death was healed: and the whole earth marveled after the beast.",
        "Revelation 13:11": "And I saw another beast ascending out of the earth; and he had two horns like a lamb, and he spoke as a dragon.",
        "Revelation 13:13": "And he does great signs, so that he even makes fire come down from heaven to the earth before men,",
        "Revelation 14:2": "And I heard a voice from heaven, as a voice of many waters, and as a voice of great thunder: and I heard a voice of harpists playing on their harps:",
        "Revelation 14:5": "And in their mouth no deceit was found: for they are blameless before the throne of God.",
        "Revelation 14:17": "And another angel came out of the temple which is in heaven, he also having a sharp sickle.",
        "Revelation 14:19": "And the angel cast his sickle into the earth, and harvested the vine of the earth, and cast it into the great winepress of the wrath of God.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_197.md"
        assert ref not in queue_refs


def test_nt_revelation_15_to_17_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Revelation 15:6": "And the seven angels having the seven plagues came out of the temple, clothed in pure and bright linen, and girded around the breasts with golden belts.",
        "Revelation 16:16": "And he gathered them together into the place called in Hebrew Armageddon.",
        "Revelation 16:18": "And there were voices, and thunders, and lightnings; and there was a great earthquake, such as had not happened since men came to be upon the earth, so great an earthquake, so mighty.",
        "Revelation 17:9": "Here is the mind which has wisdom. The seven heads are seven mountains, where the woman sits upon them.",
        "Revelation 17:10": "And there are seven kings: five have fallen, and one is, the other has not yet come; and when he comes, he must remain a short time.",
        "Revelation 17:12": "And the ten horns which you saw are ten kings, who have not yet received a kingdom; but receive authority as kings for one hour with the beast.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_198.md"
        assert ref not in queue_refs

    assert review_by_ref["Revelation 16:20"]["latest_review_status"] == "keep"
    assert review_by_ref["Revelation 16:20"]["latest_review_pass"] == "nt_review_pass_198.md"
    assert "Revelation 16:20" not in queue_refs


def test_nt_revelation_18_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Revelation 18:1": "And after these things I saw another angel coming down from heaven, having great authority; and the earth was illuminated from his glory.",
        "Revelation 18:7": "As much as she glorified herself, and lived luxuriously, so much torment and mourning give her: for she says in her heart, I sit as a queen, and am not a widow, and shall by no means see mourning.",
        "Revelation 18:10": "standing far off because of the fear of her torment, saying, Woe, woe, the great city Babylon, the mighty city! for in one hour your judgment has come.",
        "Revelation 18:12": "cargo of gold, and silver, and precious stone, and pearls, and fine linen, and purple, and silk, and scarlet, and every thyine wood, and every ivory vessel, and every vessel of most precious wood, and of bronze, and iron, and marble,",
        "Revelation 18:13": "and cinnamon, and incense, and myrrh, and frankincense, and wine, and oil, and fine flour, and wheat, and cattle, and sheep, and horses, and wagons, and bodies, and souls of men.",
        "Revelation 18:15": "The merchants of these things, who were made rich from her, shall stand far off because of the fear of her torment, weeping and mourning,",
        "Revelation 18:16": "and saying, Woe, woe, the great city, clothed in fine linen, and purple, and scarlet, and adorned with gold, and precious stone, and pearls!",
        "Revelation 18:17": "For in one hour such great wealth was made desolate. And every ship captain, and all the company on the ships, and sailors, and as many as work the sea, stood far off,",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_199.md"
        assert ref not in queue_refs


def test_nt_revelation_19_to_20_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Revelation 19:14": "And the armies which were in heaven followed him on white horses, clothed in fine linen, white and clean.",
        "Revelation 19:15": "And out of his mouth goes a sharp sword, that with it he should strike the nations: and he shall shepherd them with a rod of iron: and he treads the winepress of the wine of the fury and wrath of God Almighty.",
        "Revelation 20:1": "And I saw an angel coming down from heaven, having the key of the abyss and a great chain in his hand.",
        "Revelation 20:2": "And he laid hold of the dragon, the ancient serpent, who is Devil and Satan, and bound him a thousand years,",
        "Revelation 20:3": "And cast him into the abyss, and shut him up, and sealed over him, that he should deceive the nations no longer, until the thousand years should be fulfilled: and after these things he must be loosed a little time.",
        "Revelation 20:7": "And when the thousand years are fulfilled, Satan shall be loosed out of his prison,",
        "Revelation 20:12": "And I saw the dead, small and great, standing before God; and books were opened: and another book was opened, which is the book of life: and the dead were judged from the things written in the books, according to their works.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_200.md"
        assert ref not in queue_refs


def test_nt_revelation_21_to_22_queue_revisions_stay_reviewed() -> None:
    source_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    review_by_ref = {row["ref"]: row for row in nt_review_rows()}
    queue_refs = nt_literal_revision_queue_refs()

    expected_manual = {
        "Revelation 21:1": "And I saw a new heaven and a new earth: for the first heaven and the first earth had passed away; and the sea is no more.",
        "Revelation 21:2": "And I John saw the holy city, new Jerusalem, coming down from God out of heaven, prepared as a bride adorned for her husband.",
        "Revelation 21:12": "having a great and high wall, having twelve gates, and at the gates twelve angels, and names written on them, which are the names of the twelve tribes of the sons of Israel:",
        "Revelation 21:13": "From the east three gates; from the north three gates; from the south three gates; and from the west three gates.",
        "Revelation 21:14": "And the wall of the city had twelve foundations, and in them the names of the twelve apostles of the Lamb.",
        "Revelation 21:16": "And the city lies square, and its length is as much as the breadth: and he measured the city with the reed at twelve thousand stadia. Its length and breadth and height are equal.",
        "Revelation 21:19": "And the foundations of the wall of the city were adorned with every precious stone. The first foundation was jasper; the second, sapphire; the third, chalcedony; the fourth, emerald;",
        "Revelation 21:20": "The fifth, sardonyx; the sixth, sardius; the seventh, chrysolyte; the eighth, beryl; the ninth, topaz; the tenth, chrysoprase; the eleventh, jacinth; the twelfth, amethyst.",
        "Revelation 21:25": "And its gates shall by no means be shut by day: for night shall not be there.",
        "Revelation 22:1": "And he showed me a pure river of water of life, bright as crystal, proceeding out of the throne of God and of the Lamb.",
        "Revelation 22:4": "And they shall see his face; and his name shall be on their foreheads.",
        "Revelation 22:13": "I am the Alpha and the Omega, beginning and end, the first and the last.",
    }
    for ref, draft_translation in expected_manual.items():
        assert source_by_ref[ref]["draft_translation"] == draft_translation
        assert source_by_ref[ref]["review_status"] == "tr_literal_manual"
        assert source_by_ref[ref]["review_notes"] == "manual TR literal override"
        assert review_by_ref[ref]["latest_review_status"] == "revised"
        assert review_by_ref[ref]["latest_review_pass"] == "nt_review_pass_201.md"
        assert ref not in queue_refs


def test_high_confidence_review_typos_are_corrected_at_source() -> None:
    from build_fresh_logos_bible import find_trigger_span

    ot_by_ref = {row["ref"]: row for row in csv_rows("data/raw/lxx_greek/ot_full.csv")}
    nt_by_ref = {row["ref"]: row for row in csv_rows("data/raw/tr_greek/nt_full.csv")}
    notes_by_ref = {row["ref"]: row for row in csv_rows("data/research/translation_footnotes.csv")}

    assert "neither shall there be any more pain" in nt_by_ref["Revelation 21:4"][
        "draft_translation"
    ]
    assert "neither shall there is any more pain" not in nt_by_ref["Revelation 21:4"][
        "draft_translation"
    ]
    assert "Alleluia. And her smoke" in nt_by_ref["Revelation 19:3"]["draft_translation"]
    assert "Alleluia And her smoke" not in nt_by_ref["Revelation 19:3"]["draft_translation"]
    assert "Thus says the one who holds" in nt_by_ref["Revelation 2:1"]["draft_translation"]
    assert not [row["ref"] for row in nt_by_ref.values() if "These things says" in row["draft_translation"]]
    assert "many are those who enter through it" in nt_by_ref["Matthew 7:13"][
        "draft_translation"
    ]
    assert "few are those who find it" in nt_by_ref["Matthew 7:14"]["draft_translation"]
    assert ot_by_ref["Song of Solomon 1:1"]["draft_translation"] == (
        "The Song of Songs, which is Solomon's."
    )
    assert ot_by_ref["Job 38:4"]["draft_translation"].startswith(
        "Where were you when I founded the earth?"
    )
    assert notes_by_ref["Job 38:4"]["trigger_phrase"].startswith(
        "Where were you when I founded the earth?"
    )
    for ref in ("Psalms 101:26", "Psalms 103:5", "Psalms 118:90", "Proverbs 3:19"):
        assert "founded the earth" in ot_by_ref[ref]["draft_translation"]
        assert "founded earth" not in ot_by_ref[ref]["draft_translation"]
        assert "founded the earth" in notes_by_ref[ref]["trigger_phrase"]
    possessive_span = find_trigger_span("The Song of Songs, which is Solomon's.", "Solomon")
    assert possessive_span is not None
    assert "The Song of Songs, which is Solomon's."[possessive_span[0] : possessive_span[1]] == "Solomon's"


def test_inscription_style_all_caps_rows_use_normalized_equivalents() -> None:
    rows = csv_rows("data/proper_name_transliteration_notes.csv")
    by_name = {(row["name"], row["first_reference"]): row for row in rows}

    expected = {
        ("JESUS", "Matthew 1:21"): "Jesus",
        ("NAZARETH", "John 19:19"): "Nazareth",
        ("BABYLON", "Revelation 17:5"): "Babylon",
    }
    for key, equivalent in expected.items():
        assert by_name[key]["english_equivalent"] == equivalent
    assert ("GOD", "Acts 17:23") not in by_name


def test_residual_ego_greek_form_mislabels_are_removed() -> None:
    rows = csv_rows("data/proper_name_transliteration_notes.csv")
    by_name = {(row["name"], row["first_reference"]): row for row in rows}

    assert by_name[("Nebo", "Numbers 27:12")]["greek_form"] == "ναβαυ"
    assert by_name[("Omega", "Revelation 1:8")]["greek_form"] == "ω"
    assert by_name[("Baal-peor", "Numbers 25:3")]["greek_form"] == "βεελφεγωρ"
    assert not [
        (row["name"], row["first_reference"])
        for row in rows
        if row["greek_form"] == "εγω"
    ]


def test_no_raw_logos_bibleknowledgebase_markup_in_key_outputs() -> None:
    paths = [
        ROOT / "data" / "research" / "translation_decisions.csv",
        ROOT / "data" / "research" / "translation_footnotes.csv",
        ROOT / "output" / "logos_greek_heritage" / "the_greek_heritage_study_bible_preview.md",
        ROOT / "output" / "logos_deuterocanon" / "the_greek_heritage_study_bible_deuterocanon_preview.md",
    ]

    for path in paths:
        text = path.read_text(encoding="utf-8", errors="ignore")
        assert "[[" not in text or "BibleKnowledgebase@" not in text


def test_logos_docx_hebrew_runs_are_language_tagged_without_custom_class() -> None:
    docx_path = (
        ROOT
        / "output"
        / "logos_greek_heritage"
        / "the_greek_heritage_study_bible_reference_notes.docx"
    )
    with zipfile.ZipFile(docx_path) as zf:
        footnotes_xml = zf.read("word/footnotes.xml").decode("utf-8")
        document_xml = zf.read("word/document.xml").decode("utf-8")
        styles_xml = zf.read("word/styles.xml").decode("utf-8")

    combined_xml = footnotes_xml + document_xml + styles_xml
    assert "HebrewText" not in combined_xml
    assert "אֱלֹהִים" in footnotes_xml

    hebrew_runs = [
        match.group(0)
        for match in re.finditer(r"<w:r>.*?</w:r>", combined_xml, flags=re.DOTALL)
        if re.search(r"[\u0590-\u05ff]", match.group(0))
    ]
    assert hebrew_runs
    assert not [
        run_xml
        for run_xml in hebrew_runs
        if 'w:lang w:val="he-IL" w:bidi="he-IL"' not in run_xml
    ]


def test_mt_bridge_docx_has_no_consecutive_duplicate_bible_milestones() -> None:
    docx_path = (
        ROOT
        / "output"
        / "logos_greek_heritage"
        / "the_greek_heritage_study_bible_reference_notes.docx"
    )
    with zipfile.ZipFile(docx_path) as zf:
        document_xml = zf.read("word/document.xml").decode("utf-8")

    milestones = re.findall(r"\[\[@Bible:([^]]+)\]\]", document_xml)
    duplicates = [
        (left, right)
        for left, right in zip(milestones, milestones[1:])
        if left == right
    ]
    assert not duplicates


def test_lulu_print_proof_pdf_profile_includes_prefaces() -> None:
    output_dir = ROOT / "output" / "print"
    docx_path = output_dir / "the_greek_heritage_study_bible_lulu_print_proof.docx"
    diagnostics = json.loads(
        (output_dir / "the_greek_heritage_study_bible_lulu_print_proof_diagnostics.json").read_text(
            encoding="utf-8"
        )
    )
    pandoc_pdf_path = output_dir / "the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf"
    readme = (output_dir / "README_lulu.md").read_text(encoding="utf-8")
    with zipfile.ZipFile(docx_path) as zf:
        document_xml = zf.read("word/document.xml").decode("utf-8")
        settings_xml = zf.read("word/settings.xml").decode("utf-8")
        styles_xml = zf.read("word/styles.xml").decode("utf-8")
        footnotes_xml = zf.read("word/footnotes.xml").decode("utf-8")

    assert pandoc_pdf_path.exists()
    assert diagnostics["print_profile"]["book_prefaces"] == "included"
    assert diagnostics["print_profile"]["margin_profile"] == "lulu_pod_safe"
    assert diagnostics["print_profile"]["type_profile"] == "docx_9_5pt; pandoc_pdf_8_75pt"
    assert "inside 0.75 in" in diagnostics["print_profile"]["margins"]
    assert "outside 0.5 in" in diagnostics["print_profile"]["margins"]
    assert diagnostics["print_profile"]["verse_layout"] == "chapter-continuous run-in paragraphs"
    assert diagnostics["book_prefaces"]["included"] is True
    assert diagnostics["print_docx"]["book_preface_pages"] >= 66
    assert diagnostics["print_docx"]["run_in_verse_paragraphs"] is True
    assert diagnostics["print_docx"]["run_in_group_size"] == 0
    assert diagnostics["print_docx"]["footnote_columns"] == 2
    assert diagnostics["reader_facing_translation_note_filter"]["skipped_mechanical_review_notes"] == 319
    assert 2900 <= diagnostics["print_docx"]["pericope_heading_count"] <= 3100
    assert 2900 <= diagnostics["pericope_headings"]["included"] <= 3100
    assert diagnostics["print_profile"]["layout"] == "compact_single_column"
    footnote_layout = diagnostics["print_profile"]["footnote_layout"]
    assert footnote_layout.startswith("active Pandoc PDF uses two-column footnotes")
    assert "verse-number-keyed cross-references in red via manyfoot two-stream LaTeX" in footnote_layout
    assert "green cross-reference letters" not in footnote_layout
    assert "Pandoc/XeLaTeX is the active full-size print proof renderer" in diagnostics["print_profile"][
        "alternate_pdf_renderer"
    ]
    assert "BSB-placement original headings included" in diagnostics["print_profile"]["pericope_headings"]
    assert "Why This Draft Exists" in document_xml
    assert "Rough Methodology" in document_xml
    assert "ordinary English articles" in document_xml
    assert "the land of Judah" in document_xml
    assert diagnostics["print_profile"]["name_note_labels"] == "compact"
    assert diagnostics["print_profile"]["generated_crossrefs"] == "openbible_top_n"
    assert diagnostics["minimal_crossrefs"]["profile"] == "openbible_top_n_print"
    assert diagnostics["minimal_crossrefs"]["max_refs_per_note"] == 4
    assert diagnostics["print_docx"]["crossref_footnotes"] > 27000
    assert diagnostics["print_docx"]["verse_anchored_crossref_notes"] == diagnostics["print_docx"]["crossref_footnotes"]
    assert "Creation of Heaven and Earth" in document_xml
    assert "Confession of Love" in document_xml
    assert "Flower of the Plain" in document_xml
    assert "Search in the Night" in document_xml
    assert "Bride Confesses Her Love" not in document_xml
    assert "Bride's Admiration" not in document_xml
    assert "Bride's Dream" not in document_xml
    assert "PericopeHeading" in styles_xml
    assert 'w15:footnoteColumns w15:val="2"' in document_xml
    assert 'w:left="1080"' in document_xml
    assert 'w:right="720"' in document_xml
    assert 'w:top="720"' in document_xml
    assert 'w:bottom="720"' in document_xml
    assert "<w:mirrorMargins/>" in settings_xml
    assert '<w:spacing w:before="0" w:after="0" w:line="200" w:lineRule="auto"/>' in styles_xml
    assert '<w:vertAlign w:val="superscript"/><w:b/><w:color w:val="1F4E79"/><w:sz w:val="17"/><w:szCs w:val="17"/>' in styles_xml
    assert '<w:b/><w:color w:val="9B1C1C"/><w:sz w:val="21"/>' in styles_xml
    assert '<w:vertAlign w:val="baseline"/><w:b/><w:color w:val="1F4E79"/><w:sz w:val="15"/><w:szCs w:val="13"/>' in footnotes_xml
    assert '<w:b/><w:color w:val="9B1C1C"/>' in document_xml
    assert '<w:szCs w:val="13"/>' in styles_xml
    assert "—" not in footnotes_xml
    assert "Article review supplied" not in footnotes_xml
    assert "Article cleanup:" not in footnotes_xml
    assert "Article/readability policy" in document_xml
    assert "Std: Gomer. Src: Gomer." not in footnotes_xml
    assert "Lulu-safe mirrored POD margins" in readme
    assert "Default Lulu PDF target stamps page numbers and chapter/verse ranges" in readme
    assert "preferred stamp-free proof target uses native LaTeX marks" in readme
    assert "the_greek_heritage_study_bible_lulu_print_proof_pandoc_pdf_headers.json" in readme
    assert "the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf" in readme
    assert "active full-size Pandoc/XeLaTeX proof PDF with two-column footnotes" in readme
    assert "`the_greek_heritage_study_bible_lulu_print_proof.pdf`" not in readme
    assert "make build-print-proof-lulu-pdf" not in readme
    assert "make build-print-proof-lulu-pandoc-pdf" in readme
    assert "make build-print-proof-lulu-pandoc-pdf-native-headers-with-backmatter" in readme
    assert "Book preface pages included." in readme


PANDOC_FOOTNOTE_PREFIXES = "T|Txt|MT/LXX|Heb|Gk|Tr|Std|Src|Nm|Pn|Pl|Ppl|Div|Eng"
PANDOC_NUMERIC_FOOTNOTE_RE = re.compile(rf"^(\d+)\s+(?:{PANDOC_FOOTNOTE_PREFIXES}):")
PANDOC_BLUE = 0x1F4E79
PANDOC_RED = 0x9B1C1C


def pandoc_pdf_output_dir() -> Path:
    return ROOT / "output" / "print"


def pandoc_pdf_sample_pages() -> list[int]:
    header_path = (
        pandoc_pdf_output_dir() / "the_greek_heritage_study_bible_lulu_print_proof_pandoc_pdf_headers.json"
    )
    diagnostics = json.loads(header_path.read_text(encoding="utf-8"))

    def overlaps(item: dict[str, object], book: str, chapter: int) -> bool:
        first = item.get("first_ref")
        last = item.get("last_ref")
        if not isinstance(first, dict) or not isinstance(last, dict):
            return False
        if first.get("book") != book or last.get("book") != book:
            return False
        return int(first["chapter"]) <= chapter <= int(last["chapter"])

    pages: list[int] = []
    for book, chapter in (("Joshua", 6), ("Joshua", 7), ("Psalms", 22), ("Romans", 8)):
        for item in diagnostics["page_headers"]:
            if overlaps(item, book, chapter):
                pages.append(int(item["page"]) - 1)
                break
    return pages


def pandoc_pdf_lines(page) -> list[str]:
    lines: list[str] = []
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            text = "".join(span.get("text", "") for span in line.get("spans", [])).strip()
            if text:
                lines.append(text)
    return lines


def pandoc_pdf_lines_with_y(page) -> list[tuple[float, str]]:
    lines: list[tuple[float, str]] = []
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            text = "".join(span.get("text", "") for span in line.get("spans", [])).strip()
            if text:
                lines.append((float(line["bbox"][1]), text))
    return lines


def pandoc_pdf_marker_spans(page, *, color: int) -> list[str]:
    markers: list[str] = []
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = span.get("text", "").strip()
                size = float(span.get("size", 0.0))
                if span.get("color") == color and 7.0 <= size <= 7.9 and text:
                    markers.append(text)
    return markers


def assert_contiguous_sequence(values: list[int]) -> None:
    if not values:
        return
    unique_values = sorted(set(values))
    assert unique_values == list(range(1, unique_values[-1] + 1))


def test_lulu_pandoc_pdf_footnote_numeric_sequence_is_contiguous() -> None:
    output_dir = ROOT / "output" / "print"
    pdf_path = output_dir / "the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf"
    diagnostics = json.loads(
        (output_dir / "the_greek_heritage_study_bible_lulu_print_proof_diagnostics.json").read_text(
            encoding="utf-8"
        )
    )

    document = fitz.open(pdf_path)
    for page_index in pandoc_pdf_sample_pages():
        markers = [int(text) for text in pandoc_pdf_marker_spans(document[page_index], color=PANDOC_BLUE)]
        assert_contiguous_sequence(markers)
    assert diagnostics["print_docx"]["crossref_footnotes"] > 27000


def test_lulu_pandoc_pdf_crossrefs_use_red_verse_number_labels() -> None:
    pdf_path = pandoc_pdf_output_dir() / "the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf"
    document = fitz.open(pdf_path)
    red_markers: list[str] = []
    for page_index in [1, *pandoc_pdf_sample_pages()]:
        lines = pandoc_pdf_lines(document[page_index])
        assert not any(re.match(r"^[a-z]+\s+X:", line) for line in lines)
        assert not any(re.match(r"^\d+\s+X:", line) for line in lines)
        red_markers.extend(pandoc_pdf_marker_spans(document[page_index], color=PANDOC_RED))
    assert red_markers
    assert all(marker.isdigit() for marker in red_markers)


def test_lulu_pandoc_pdf_crossrefs_use_abbreviated_book_names() -> None:
    pdf_path = pandoc_pdf_output_dir() / "the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf"
    document = fitz.open(pdf_path)
    xref_text = ""
    for page_index in range(min(12, len(document))):
        page = document[page_index]
        candidate = "\n".join(
            line for y, line in pandoc_pdf_lines_with_y(page) if y > page.rect.height * 0.85
        )
        if "Heb 11:3" in candidate:
            xref_text = candidate
            break
    assert "Heb 11:3" in xref_text
    assert "Isa 45:18" in xref_text
    assert "Rev 4:11" in xref_text
    assert "Ps 103:30" in xref_text
    assert "Ps 104:30" not in xref_text
    assert "Hebrews 11:3" not in xref_text
    assert "Isaiah 45:18" not in xref_text
    assert "Revelation 4:11" not in xref_text
    assert "Psalms 103:30" not in xref_text
    assert "Psalms 104:30" not in xref_text


def test_compact_print_crossrefs_drop_semicolons_and_terminal_period() -> None:
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_fresh_logos_bible as logos_builder

    note = 'Cross-references: John 1:1-3; Heb 11:3; Isa 45:18; Rev 4:11.'
    assert (
        logos_builder.compact_print_footnote_text(note)
        == "X: John 1:1-3 Heb 11:3 Isa 45:18 Rev 4:11"
    )


def test_lulu_pandoc_pdf_no_overlapping_markers() -> None:
    pdf_path = pandoc_pdf_output_dir() / "the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf"
    document = fitz.open(pdf_path)
    bad_lines: list[str] = []
    for page_index in pandoc_pdf_sample_pages():
        page = document[page_index]
        for color in (PANDOC_BLUE, PANDOC_RED):
            for marker in pandoc_pdf_marker_spans(page, color=color):
                if not marker.isdigit():
                    bad_lines.append(marker)
    assert bad_lines == []


def test_root_readme_reflects_complete_fresh_workspace() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
    translation_rules = (ROOT / "data" / "research" / "translation_rules.md").read_text(encoding="utf-8")
    research_readme = (ROOT / "data" / "research" / "README.md").read_text(encoding="utf-8")
    architecture = (ROOT / "docs" / "ARCHITECTURE.md").read_text(encoding="utf-8")
    architecture_flat = " ".join(architecture.split())

    assert "Fresh translation workspace for Greek-to-English OT/NT polish" in readme
    assert "## Fresh Translation Workspace" in readme
    assert "`data/raw/lxx_greek/ot_full.csv`" in readme
    assert "`data/raw/tr_greek/nt_full.csv`" in readme
    assert "`output/logos_greek_heritage/the_greek_heritage_study_bible_logos_bible.docx`" in readme
    assert "`output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_logos_bible.docx`" in readme
    assert "`output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf`" in readme
    assert "`output/print/cover/ghsb_draft_lulu_jacket_cover_26_5x11_75.pdf`" in readme
    assert "`release/greek-heritage-study-bible-rc1/MANIFEST.md`" in readme
    assert "They are ignored unless a" in readme
    assert "future release explicitly promotes them back to reader-facing artifacts" in readme
    assert "make build-fresh" in readme
    assert "make build-combined" in readme
    assert "make build-combined-logos" in readme
    assert "make release-combined" in readme
    assert "Existing OT release-candidate package" in readme
    for stale_phrase in (
        "Fresh Translation Pilot",
        "pilot workspace",
        "Build pilot worksheet",
        "`data/raw/lxx_greek/genesis_1_3_pilot.csv`",
        "`data/research/genesis_1_3_workflow.md`",
    ):
        assert stale_phrase not in readme
        assert stale_phrase not in translation_rules
        assert stale_phrase not in research_readme
    assert not (ROOT / "data" / "raw" / "lxx_greek" / "genesis_1_3_pilot.csv").exists()
    assert not (ROOT / "data" / "research" / "genesis_1_3_workflow.md").exists()
    assert "Treat fresh output as draft until phrase-level decisions are reviewed." in translation_rules
    assert "base Greek edition" not in translation_rules
    assert "Suggested pilot" not in research_readme
    assert "complete NT Scrivener TR source workspace" in research_readme
    assert "Phrase and verse decisions used by the fresh output pipeline" in architecture
    assert "not aggregate output rebuilds" in architecture_flat
    assert "`make build-nt` before NT release-facing commits" in architecture_flat
    assert "`make build-combined` refreshes the single-file OT/NT Markdown outputs" in architecture_flat
    assert "build-fresh: build-ot build-nt release-combined" in makefile
    assert "release-combined: build-combined build-combined-logos" in makefile
    assert "PYTHON ?= python" in makefile
    assert "python3" not in readme
    assert "python3" not in contributing


def test_data_dictionary_matches_current_editable_schemas() -> None:
    dictionary = (ROOT / "docs" / "DATA_DICTIONARY.md").read_text(encoding="utf-8")
    expected_paths = [
        "data/research/translation_footnotes.csv",
        "data/research/translation_decisions.csv",
        "data/research/variant_notes.csv",
        "data/research/reviewed_phrase_guards.csv",
        "data/proper_name_transliteration_notes.csv",
        "data/research/contextual_proper_name_decisions.csv",
    ]

    for relative_path in expected_paths:
        assert f"`{relative_path}`" in dictionary
        for column in csv_header(relative_path):
            assert f"`{column}`" in dictionary

    for stale_phrase in (
        "`anchor`",
        "`variant_type`",
        "`note` | Public note text",
        "`source` | Witness or review source used for the note",
        "`scope` | Testament/book scope for the note",
    ):
        assert stale_phrase not in dictionary


def test_fresh_translation_research_stack_is_scope_specific() -> None:
    stack_text = (ROOT / "data" / "research" / "logos_translation_stack.json").read_text(encoding="utf-8")
    stack = json.loads(stack_text)
    resources = stack["preferred_resources"]
    source_resources = {
        (resource["testament"], resource["role"], resource["resource_id"])
        for resource in resources
    }

    assert "pilot_scope" not in stack
    assert "Genesis pilot" not in stack_text
    assert ("ot", "source_workspace", "data/raw/lxx_greek/ot_full.csv") in source_resources
    assert ("nt", "source_workspace", "data/raw/tr_greek/nt_full.csv") in source_resources
    assert all(
        resource["testament"] == "ot"
        for resource in resources
        if resource["resource_id"] == "LLS:LOGOSLXX"
    )


def test_release_status_distinguishes_ot_rc_from_complete_nt_workspace() -> None:
    status = (ROOT / "RELEASE_STATUS.md").read_text(encoding="utf-8")
    pending_variant_refs = [
        row["ref"] for row in csv_rows("data/research/variant_notes.csv") if row["status"] == "pending"
    ]

    assert "Release candidate: `fresh-translation-ot-rc1`" in status
    assert "the NT TR fresh draft is complete" in status
    assert "`output/logos_greek_heritage/the_greek_heritage_study_bible_logos_bible.docx`" in status
    assert "`output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_logos_bible.docx`" in status
    assert "`output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf`" in status
    assert "`output/print/cover/ghsb_draft_lulu_jacket_cover_26_5x11_75.pdf`" in status
    assert "`release/greek-heritage-study-bible-rc1/`" in status
    assert "`release/fresh-translation-ot-rc1/MANIFEST.md`" in status
    assert "packaged combined release bundle has not been cut" not in status
    assert f"`{len(pending_variant_refs)}` non-blocking pending" in status
    assert "apparatus rows." in status
    assert "python3" not in status


def test_combined_logos_reader_output_suppresses_mechanical_review_notes() -> None:
    output_dir = ROOT / "output" / "logos_greek_heritage"
    diagnostics = json.loads(
        (output_dir / "the_greek_heritage_study_bible_diagnostics.json").read_text(
            encoding="utf-8"
        )
    )
    with zipfile.ZipFile(output_dir / "the_greek_heritage_study_bible_logos_bible.docx") as zf:
        logos_footnotes = zf.read("word/footnotes.xml").decode("utf-8")
        logos_document = zf.read("word/document.xml").decode("utf-8")
    with zipfile.ZipFile(output_dir / "the_greek_heritage_study_bible_reference_notes.docx") as zf:
        reference_footnotes = zf.read("word/footnotes.xml").decode("utf-8")
    with zipfile.ZipFile(output_dir / "the_greek_heritage_study_bible_proofreading.docx") as zf:
        proof_footnotes = zf.read("word/footnotes.xml").decode("utf-8")

    assert diagnostics["reader_facing_translation_note_filter"]["skipped_mechanical_review_notes"] == 319
    assert "Article review supplied" not in logos_footnotes
    assert "Article cleanup:" not in logos_footnotes
    assert "ordinary English articles" in logos_document
    assert "the land of Judah" in logos_document
    assert "Article review supplied" in reference_footnotes
    assert "Article review supplied" in proof_footnotes


def test_combined_release_manifest_and_checksums_cover_outputs() -> None:
    manifest = (ROOT / "release/greek-heritage-study-bible-rc1/MANIFEST.md").read_text(encoding="utf-8")
    checksum_lines = (
        ROOT / "release/greek-heritage-study-bible-rc1/CHECKSUMS.sha256"
    ).read_text(encoding="utf-8").splitlines()
    checksums = {line.split("  ", 1)[1]: line.split("  ", 1)[0] for line in checksum_lines}
    expected_paths = [
        "output/logos_greek_heritage/the_greek_heritage_study_bible_logos_bible.docx",
        "output/logos_greek_heritage/the_greek_heritage_study_bible_reference_notes.docx",
        "output/logos_greek_heritage/the_greek_heritage_study_bible_proofreading.docx",
        "output/logos_greek_heritage/README.md",
        "output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_logos_bible.docx",
        "output/logos_deuterocanon/README.md",
        "output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf",
        "output/print/cover/ghsb_draft_lulu_jacket_cover_26_5x11_75.pdf",
    ]

    assert "Release candidate: `greek-heritage-study-bible-rc1`" in manifest
    assert "make build-combined-logos" in manifest
    assert "make build-deuterocanon-logos" in manifest
    assert "make build-print-proof-lulu-pandoc-pdf" in manifest
    assert "python3" not in manifest
    for relative_path in expected_paths:
        assert f"`{relative_path}`" in manifest
        assert relative_path in checksums
        assert checksums[relative_path] == sha256(relative_path)

    cover_pdf = ROOT / "output/print/cover/ghsb_draft_lulu_jacket_cover_26_5x11_75.pdf"
    with fitz.open(cover_pdf) as document:
        page = document[0]
        assert round(page.rect.width / 72, 3) == 26.5
        assert round(page.rect.height / 72, 3) == 11.75


def test_no_known_fixed_ot_name_leaks_in_outputs_or_support_tables() -> None:
    paths = [
        ROOT / "output" / "logos_greek_heritage" / "the_greek_heritage_study_bible_preview.md",
        ROOT / "data" / "research" / "translation_footnotes.csv",
    ]
    forbidden = [
        "Jeminite",
        "Jeminaian",
        "Ouai Ichabod",
        "Geththaite",
        "Geththaites",
        "Eththi",
        "Elioun",
        "Shilom",
        "Pheleththi",
        "Chereththi",
        "Chetti",
        "Sabee",
        "Aoronite",
        "Ioanas",
        "Adroi",
        "Iethri",
        "Ieddouran",
        "Iethiraean",
        "Thabason",
        "Benor",
        "Souphi",
        "Ougaua",
        "Chabasin",
        "Tochos",
        "Assourieim",
        "Othom",
        "Nambran",
        "Beelmeon",
        "Botanin",
        "Sokchotha",
        "Addamin",
        "Aptalim",
        "Macho",
        "Maatarothorech",
        "Barek",
        "Maragella",
        "Katasem",
        "Easakem",
        "Chalamak",
        "Baithanan",
        "Sira",
        "Eleasa",
        "Iturea",
        "Tharach",
        "Eliazai",
        "Baalia",
        "Zacharian",
        "Zachri",
        "Asas",
        "Marodach",
        "Kittians",
        "Rehoboth-city",
        "Sared",
        "Saredite",
        "Mithkah",
        "Thebes",
        "Aiin",
        "Iephthae",
        "Beelphegor",
        "Gai-Benaiah-Hinnom",
        "Moabitis",
        "Baalpeor",
        "Chasbi",
        "Sourin",
        "Rokom",
        "Robok",
        "Eui",
        "Abelbethmaachah",
        "Chezrath",
        "Keneroth",
        "Chenereth",
        "son of Hadad",
        "Elkana",
        "Achaab",
        "Nabouthai",
        "Ioas",
        "Ioachas",
        "Iosaphat",
        "Phakee",
        "Thaglathphellasar",
        "Thalgathphellasar",
        "Bersabee",
        "Phinees",
        "Badekar",
        "Jezraelite",
        "Regma",
        "Seboim",
        "Segor",
        "Balla",
        "Zare",
        "Moze",
        "Balaennon",
        "Gesem",
        "Salpaad",
        "Nabau",
        "Jassa",
        "Misor",
        "Sekelak",
        "Mageddo",
        "Saraa",
        "Jabis",
        "Sadok",
        "Remmoth",
        "Ailath",
        "Asaia",
        "Nechao",
        "Sechenia",
        "Taphnas",
        "Gergesites",
        "Ochozath",
        "Asar",
        "Gola",
        "Petephres",
        "Phua",
        "Bale",
        "Barsa",
        "Symobor",
        "Etebatha",
        "Jarin",
        "Tholmi",
        "Golathmain",
        "Sikimois",
        "Sikimoi",
        "Maacha",
        "Aoda",
        "Thoada",
        "Abisou",
        "Bokkai",
        "Mariel",
        "Melchisoue",
        "Sobochai",
        "Galaaditis",
        "Zathoua",
        "Esam",
        "Gesam",
        "Amadathos",
        "Ausitis",
        "Sauchite",
        "City of Jearim",
        "Kariathiarin",
        "Kariatharbok",
        "Kariatharboksepher",
        "Gasein",
        "Sothiba",
        "Araa",
        "Ammanith",
        "Emospheos",
        "Aithalim",
        "Miphithim",
        "Esamathim",
        "Amasaraim",
        "Sarathaians",
        "Esthaolaians",
        "Esel",
        "Gamariah",
        "Ergab",
        "Minaeans",
        "Minaian",
        "Sabatha",
        "Eliphaleit",
        "Baaltham",
        "Rhos",
        "Orech",
        "Taam",
        "Chebratha",
        "Golam",
        "Manachath",
        "Gaibel",
        "Sutalaam",
        "Suthala",
        "Manthanain",
        "Pikriai",
        "Sapher",
        "Gesiongaber",
        "Maala",
        "Chorraean",
        "Aziph",
        "Napheddor",
        "Onom",
        "Baithmaacha",
        "Machemas",
        "Esebon",
        "Ganebath",
        "Thekemina",
        "Apheka",
        "Cheleb",
        "Asordan",
        "Mesollam",
        "Osar",
        "Sagaph",
        "Nage",
        "Assathon",
        "Balaa",
        "Mophaath",
        "Iaous",
        "Sosek",
        "Iediou",
        "Abdias",
        "Geththite",
        "Ouni",
        "Zethom",
        "Godollathi",
        "Psonthomphanech",
        "Caphtorieim",
        "Oupheir",
        "Eveila",
        "Masek",
        "Sabek",
        "Soie",
        "Latousieim",
        "Laomeim",
        "Douma",
        "Beoch",
        "Gader",
        "Aie",
        "Jamein",
        "Amada",
        "Metebeel",
        "Matraith",
        "Helas",
        "Mazar",
        "Iasub",
        "Zambram",
        "Thasoban",
        "Aedeis",
        "Aroedeis",
        "Merra",
        "Sami",
        "Samite",
        "Ommin",
        "Esephin",
        "Zarai",
        "Zakkou",
        "Telmon",
        "Tabaoth",
        "Rason",
        "Bakbouk",
        "Basaloth",
        "Barkous",
        "Abdeselma",
        "Atharsatha",
        "Apharsachaeans",
        "Sechenias",
        "Argyriou",
        "Aoue",
        "Asana",
        "Azour",
        "Ariph",
        "Bougaian",
        "Godoliah",
        "Pathures",
        "Auranitis",
        "Ainan",
        "Dase",
        "Loudieim",
        "Enemetieim",
        "Labieim",
        "Nephthalieim",
        "Pathrosonieim",
        "Oul",
        "Saleth",
        "Sarmoth",
        "Jarach",
        "Odorra",
        "Aibel",
        "Decla",
        "Eual",
        "Saby",
        "Exeleketh",
        "Baithok",
        "Keaph",
        "Messara",
        "Rasim",
        "Masphar",
        "Maspharath",
        "Netopha",
        "Maeleth",
        "Kiradas",
        "Jezoniah",
        "Jeremin",
        "Habazziniah",
        "Ophi",
        "Mochathi",
        "Phoinikon",
        "Marimoth",
        "Mane",
        "Thekel",
    ]

    for path in paths:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for term in forbidden:
            pattern = rf"(?<![A-Za-z]){re.escape(term)}(?![A-Za-z])"
            assert not re.search(pattern, text), f"{term} leaked in {path}"


def test_sync_ot_support_text_helper_strips_logos_markup() -> None:
    script_path = ROOT / "scripts" / "sync_ot_support_text.py"
    assert script_path.exists()

    spec = importlib.util.spec_from_file_location("sync_ot_support_text", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    sample = "And they came to [[Shiloh >> BibleKnowledgebase@Shiloh]] and [[Ophni >> BibleKnowledgebase@Ophni]]."
    assert module.strip_logos_links(sample) == "And they came to Shiloh and Ophni."


def test_pinned_raw_artifacts_are_unchanged() -> None:
    for relative_path, expected_hash in PINNED_RAW_SHA256.items():
        assert sha256(relative_path) == expected_hash


def test_generated_docx_files_are_valid_when_present() -> None:
    paths = [
        ROOT / "output/logos_greek_heritage/the_greek_heritage_study_bible_logos_bible.docx",
        ROOT / "output/logos_greek_heritage/the_greek_heritage_study_bible_reference_notes.docx",
        ROOT / "output/logos_greek_heritage/the_greek_heritage_study_bible_proofreading.docx",
        ROOT / "output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_logos_bible.docx",
    ]

    for path in paths:
        if not path.exists():
            continue
        with zipfile.ZipFile(path) as archive:
            assert archive.testzip() is None
            assert "word/document.xml" in archive.namelist()


def test_study_helps_appendix_omits_reading_plan_and_resolves_refs() -> None:
    script_path = ROOT / "scripts" / "build_study_helps_appendix.py"
    assert script_path.exists()

    spec = importlib.util.spec_from_file_location("build_study_helps_appendix", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    markdown, diagnostics = module.render_markdown()
    assert diagnostics == []
    assert "DAILY READING PLAN" not in markdown
    assert "SECTION 1" not in markdown
    assert "This separate appendix draft is adapted from the supplied insert" not in markdown
    assert "Largest OT section" not in markdown
    assert "missing local verse text" not in markdown
    assert "**Kingdom of Heaven**" in markdown
    assert "**Kingdom of God**" in markdown
    assert "**Day of the Lord**" in markdown
    assert "**Day of Christ**" in markdown
    assert "Ps 22:1 (English Ps 23:1)" in markdown
    assert "Psalms 22:1 (English Psalm 23:1)" not in markdown
    assert "Key reference: Deut 6:4." in markdown
    assert "**Isa 26:3-4.** 3 upholding truth and keeping peace, because upon you 4 they hoped" in markdown
    assert "**2Chr 7:13-14.** 13 If I shut heaven and rain does not come" in markdown
    assert "**2Chr 7:14.** and my people" not in markdown
