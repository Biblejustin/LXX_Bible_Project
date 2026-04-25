import csv
import hashlib
import importlib.util
import json
import re
import sys
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

    assert len(ot_rows) == 22909
    assert len(nt_rows) == 7957
    assert SOURCE_COLUMNS <= set(ot_rows[0])
    assert SOURCE_COLUMNS | {"ukjv_translation", "review_status", "review_notes"} <= set(nt_rows[0])
    assert ot_rows[0]["ref"] == "Genesis 1:1"
    assert nt_rows[0]["ref"] == "Matthew 1:1"
    assert [row["ref"] for row in ot_rows if row["greek_text"] == "MT-only insertion; no LXX Greek row"] == [
        f"Jeremiah 40:{verse}" for verse in range(14, 27)
    ]


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
    assert "keep watch for your head" in by_ref["Genesis 3:15"]["draft_translation"]
    assert by_ref["Job 19:25"]["draft_translation"] == "For I know that eternal is the one about to free me upon earth."
    assert "The gods who did not make" in by_ref["Jeremiah 10:11"]["draft_translation"]
    assert "The gods of nations" in by_ref["Daniel 4:37"]["draft_translation"]
    assert by_ref["Ecclesiastes 3:1"]["draft_translation"].startswith("For all things there is a time")
    assert "the Lord himself will give you a sign" in by_ref["Isaiah 7:14"]["draft_translation"]
    assert not [row["ref"] for row in ot_rows if "Gods " in row["draft_translation"]]

    notes = csv_rows("data/research/translation_footnotes.csv")
    assert not [row["ref"] for row in notes if "Direct Logos export" in row["footnote_text"]]
    notes_by_ref = {(row["ref"], row["note_type"]): row for row in notes}
    assert "modern English connotations of ecstasy" in notes_by_ref[("Genesis 2:21", "translation")]["footnote_text"]
    assert "watch/guard language" in notes_by_ref[("Genesis 3:15", "translation")]["footnote_text"]
    assert "making the English sentence complete" in notes_by_ref[("Job 19:25", "translation")]["footnote_text"]
    assert "Psalm 22:16 with pierced language" in notes_by_ref[("Psalms 21:17", "translation")]["footnote_text"]
    assert "Ancient of Days" in notes_by_ref[("Daniel 7:13", "textual")]["footnote_text"]


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
        "for Lord",
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
    assert "The Lord said to my Lord" in by_ref["Psalms 109:1"]["draft_translation"]
    assert "forsook the Lord God of their fathers" in by_ref["2 Chronicles 7:22"]["draft_translation"]
    assert "The Lord God of heaven gave me" in by_ref["2 Chronicles 36:23"]["draft_translation"]
    assert "The Lord of hosts has commanded" in by_ref["Isaiah 13:4"]["draft_translation"]
    assert "As the Lord lives" in by_ref["Jeremiah 23:7"]["draft_translation"]
    assert "Exalt the Lord our God" in by_ref["Psalms 98:5"]["draft_translation"]
    assert by_ref["Zephaniah 3:17"]["draft_translation"].startswith("The Lord your God is in you")
    assert "by the word of the Lord" in by_ref["Numbers 33:2"]["draft_translation"]
    assert by_ref["1 Kings 17:2"]["draft_translation"].startswith("And the word of the Lord came")
    assert "Hear the word of the Lord" in by_ref["2 Kings 20:16"]["draft_translation"]
    assert "praise the name of the Lord" in by_ref["Psalms 112:1"]["draft_translation"]
    assert "for the day of the Lord is near" in by_ref["Isaiah 13:6"]["draft_translation"]
    assert "Let the name of the Lord be blessed" in by_ref["Job 1:21"]["draft_translation"]
    assert "sought the face of the Lord" in by_ref["2 Chronicles 33:12"]["draft_translation"]
    assert by_ref["Psalms 117:18"]["draft_translation"].startswith("The Lord disciplined me")
    assert by_ref["Proverbs 15:25"]["draft_translation"].startswith("The Lord tears down")
    assert "which the Lord planted" in by_ref["Isaiah 44:14"]["draft_translation"]
    assert "the Lord of heaven has authority" in by_ref["Daniel 4:17"]["draft_translation"]
    assert "relied on the Lord saying" in by_ref["Micah 3:11"]["draft_translation"]


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
    diagnostics = json.loads(
        (ROOT / "output/fresh_nt_tr_vs_ukjv_review_diagnostics.json").read_text(encoding="utf-8")
    )

    assert diagnostics["priority_rows"] == 0
    assert diagnostics["queue_rows"] == 0


def test_inscription_style_all_caps_rows_use_normalized_equivalents() -> None:
    rows = csv_rows("data/proper_name_transliteration_notes.csv")
    by_name = {(row["name"], row["first_reference"]): row for row in rows}

    expected = {
        ("JESUS", "Matthew 1:21"): "Jesus",
        ("NAZARETH", "John 19:19"): "Nazareth",
        ("GOD", "Acts 17:23"): "God",
        ("BABYLON", "Revelation 17:5"): "Babylon",
    }
    for key, equivalent in expected.items():
        assert by_name[key]["english_equivalent"] == equivalent


def test_no_raw_logos_bibleknowledgebase_markup_in_key_outputs() -> None:
    paths = [
        ROOT / "data" / "research" / "translation_decisions.csv",
        ROOT / "data" / "research" / "translation_footnotes.csv",
        ROOT / "output" / "fresh_translation_ot_full_translation_only.md",
        ROOT / "output" / "fresh_translation_nt_tr_translation_only.md",
        ROOT / "output" / "logos" / "fresh_translation_ot_logos_bible_preview.md",
        ROOT / "output" / "logos_nt" / "fresh_translation_nt_tr_preview.md",
    ]

    for path in paths:
        text = path.read_text(encoding="utf-8", errors="ignore")
        assert "[[" not in text or "BibleKnowledgebase@" not in text


def test_no_known_fixed_ot_name_leaks_in_outputs_or_support_tables() -> None:
    paths = [
        ROOT / "output" / "fresh_translation_ot_full_translation_only.md",
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
