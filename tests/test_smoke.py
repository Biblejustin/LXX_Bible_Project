import csv
import hashlib
import importlib.util
import json
import re
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

for import_path in (ROOT, ROOT / "scripts"):
    import_path_text = str(import_path)
    if import_path_text not in sys.path:
        sys.path.insert(0, import_path_text)

from fresh_bible.book_scope import filter_rows_by_scope


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
    assert by_ref["Job 19:25"]["draft_translation"] == "For I know that eternal is the one who is about to free me upon earth."
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
    assert "from the mouth of prophets" in by_ref["Zechariah 8:9"]["draft_translation"]
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
    assert "the land behind them will be made desolate, with no one passing through or returning" in by_ref["Zechariah 7:14"]["draft_translation"]
    assert "they made the delightful land into destruction" in by_ref["Zechariah 7:14"]["draft_translation"]
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
    assert "called the border of lawlessness and a people against whom" in by_ref["Malachi 1:4"]["draft_translation"]
    assert "eat the strength of nations" in by_ref["Isaiah 61:6"]["draft_translation"]
    assert "bring to you the strength of nations" in by_ref["Isaiah 60:11"]["draft_translation"]
    assert "the one rescuing you, the God of Israel, will be called the God of all the earth" in by_ref["Isaiah 54:5"]["draft_translation"]
    assert "the one rescuing you, the Holy One of Israel" in by_ref["Isaiah 48:17"]["draft_translation"]
    assert "to find the way in which you should walk" in by_ref["Isaiah 48:17"]["draft_translation"]
    assert "the one rescuing you and upholding the strength of Jacob" in by_ref["Isaiah 49:26"]["draft_translation"]
    assert "said the Lord, the one rescuing you" in by_ref["Isaiah 54:8"]["draft_translation"]
    assert "The Lord stirred the spirit of the king of Medes" in by_ref["Jeremiah 28:11"]["draft_translation"]
    assert "beside the gates of rulers" in by_ref["Proverbs 1:21"]["draft_translation"]
    assert "by powers and by strengths of the field" in by_ref["Song of Solomon 2:7"]["draft_translation"]
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
    assert "Because the lips of a priest will guard knowledge, and the law they will seek" in by_ref["Malachi 2:7"]["draft_translation"]
    assert by_ref["Zechariah 14:5"]["draft_translation"].startswith("And the ravine of my mountains")
    assert "and the ravine of mountains" in by_ref["Zechariah 14:5"]["draft_translation"]
    assert "what the way of spirit is" in by_ref["Ecclesiastes 11:5"]["draft_translation"]
    assert "womb of a pregnant woman" in by_ref["Ecclesiastes 11:5"]["draft_translation"]
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
    assert "from the priests dwelling in Anathoth" in by_ref["Jeremiah 1:1"]["draft_translation"]
    assert "the judgment of a man before the face of the Most High" in by_ref["Lamentations 3:35"]["draft_translation"]
    assert by_ref["Ezekiel 1:1"]["draft_translation"].startswith("And it happened in the thirtieth year")
    assert "the heavens were opened" in by_ref["Ezekiel 1:1"]["draft_translation"]
    assert "mouth of the lions' den" in by_ref["Daniel 6:20"]["draft_translation"]
    assert by_ref["Hosea 14:10"]["draft_translation"].startswith("Who is wise")
    assert "Because the ways of the Lord are straight" in by_ref["Hosea 14:10"]["draft_translation"]
    assert "no high-sounding speech" in by_ref["1 Samuel 2:3"]["draft_translation"]
    assert "God of knowledge" in by_ref["1 Samuel 2:3"]["draft_translation"]
    assert "Those full of bread were brought low" in by_ref["1 Samuel 2:5"]["draft_translation"]
    assert "the men were cut to the heart" in by_ref["Genesis 34:7"]["draft_translation"]
    assert by_ref["Genesis 27:38"]["draft_translation"].startswith("But Esau said to his father")
    assert "when Isaac was cut to the heart" in by_ref["Genesis 27:38"]["draft_translation"]
    assert "Aaron was cut to the heart" in by_ref["Leviticus 10:3"]["draft_translation"]
    assert "the one with many children became weak" in by_ref["1 Samuel 2:5"]["draft_translation"]
    assert "each day's matter on its day" in by_ref["1 Kings 8:59"]["draft_translation"]
    assert "Ahab was cut to the heart before the Lord" in by_ref["1 Kings 20:27"]["draft_translation"]
    assert "Ahab was cut to the heart before me" in by_ref["1 Kings 20:29"]["draft_translation"]
    assert "a day's portion on its day" in by_ref["2 Kings 25:30"]["draft_translation"]
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
    assert "Will a plowman plow the whole earth all day" in by_ref["Isaiah 45:9"]["draft_translation"]
    assert "all beasts of the whole earth" in by_ref["Ezekiel 32:4"]["draft_translation"]
    assert by_ref["Ezekiel 35:14"]["draft_translation"].startswith("Thus says the Lord: In the joy of the whole earth")
    assert "the house of Jacob is in a snare" in by_ref["Isaiah 8:14"]["draft_translation"]
    assert "the house of Joseph a flame, and the house of Esau stubble" in by_ref["Obadiah 1:18"]["draft_translation"]
    assert by_ref["Micah 2:7"]["draft_translation"].startswith("O house of Jacob, saying, Has the spirit of the Lord")
    assert "like a lion ready for the hunt" in by_ref["Psalms 16:12"]["draft_translation"]
    assert "like a lion among beasts of the forest" in by_ref["Micah 5:7"]["draft_translation"]
    assert "like a lion-cub among flocks of sheep" in by_ref["Micah 5:7"]["draft_translation"]
    assert "like a lion for slaughter" in by_ref["Job 10:16"]["draft_translation"]
    assert "like a lion, while there is none" in by_ref["Psalms 7:3"]["draft_translation"]
    assert "like a lion in its den" in by_ref["Psalms 9:30"]["draft_translation"]
    assert "like a lion seizing and roaring" in by_ref["Psalms 21:14"]["draft_translation"]
    assert "righteous trusts like a lion" in by_ref["Proverbs 28:1"]["draft_translation"]
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
    assert "like a horse through wilderness" in by_ref["Isaiah 63:13"]["draft_translation"]
    assert "as a deer struck in liver" in by_ref["Proverbs 7:23"]["draft_translation"]
    assert "soar high like an eagle" in by_ref["Obadiah 1:4"]["draft_translation"]
    assert "fly like an eagle eager to eat" in by_ref["Habakkuk 1:8"]["draft_translation"]
    assert by_ref["Jeremiah 30:16"]["draft_translation"].startswith("Behold, like an eagle")
    assert "like an eagle against the house of the Lord" in by_ref["Hosea 8:1"]["draft_translation"]
    assert "as a young man dwelling with a virgin" in by_ref["Isaiah 62:5"]["draft_translation"]
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
    assert "like a torrent flooding glory" in by_ref["Isaiah 66:12"]["draft_translation"]
    assert "like a skin-bag, like a garment eaten by moth" in by_ref["Job 13:28"]["draft_translation"]
    assert "like a garment, and like a cloak" in by_ref["Psalms 101:27"]["draft_translation"]
    assert "my salvation like a cloud" in by_ref["Job 30:15"]["draft_translation"]
    assert "like a cloud he will come up" in by_ref["Jeremiah 4:13"]["draft_translation"]
    assert "become like a river and your righteousness like a wave of sea" in by_ref["Isaiah 48:18"]["draft_translation"]
    assert "rise like a river" in by_ref["Jeremiah 26:7"]["draft_translation"]
    assert "as a woman in labor" in by_ref["Isaiah 26:17"]["draft_translation"]
    assert "like a dead man" in by_ref["Psalms 30:13"]["draft_translation"]
    assert "like a ruined vessel" in by_ref["Psalms 30:13"]["draft_translation"]
    assert "as a house of sacrifice" in by_ref["2 Chronicles 7:12"]["draft_translation"]
    assert "pangs as of a woman giving birth" in by_ref["Psalms 47:7"]["draft_translation"]
    assert "as of a woman in labor" in by_ref["Jeremiah 4:31"]["draft_translation"]
    assert "as a fleeing gazelle" in by_ref["Isaiah 13:14"]["draft_translation"]
    assert "as with a weapon of favor" in by_ref["Psalms 5:13"]["draft_translation"]
    assert "as a flame burns mountains" in by_ref["Psalms 82:15"]["draft_translation"]
    assert "their faces will change as a flame" in by_ref["Isaiah 13:8"]["draft_translation"]
    assert by_ref["1 Chronicles 19:13"]["draft_translation"].startswith("Act like a man")
    assert "Be strong and act like a man and do" in by_ref["1 Chronicles 28:20"]["draft_translation"]
    assert "like a birthing woman" in by_ref["Micah 4:10"]["draft_translation"]
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
    assert "as a piece of pomegranate" in by_ref["Song of Solomon 4:3"]["draft_translation"]
    assert "Set me as a seal" in by_ref["Song of Solomon 8:6"]["draft_translation"]
    assert "as a tent in vineyard" in by_ref["Isaiah 1:8"]["draft_translation"]
    assert "as a city under siege" in by_ref["Isaiah 1:8"]["draft_translation"]
    assert "strong like an oak" in by_ref["Amos 2:9"]["draft_translation"]
    assert "as a flying bird" in by_ref["Isaiah 16:2"]["draft_translation"]
    assert "as an enemy" in by_ref["Isaiah 63:10"]["draft_translation"]
    assert "plowed like a field" in by_ref["Micah 3:12"]["draft_translation"]
    assert "as a shepherd snatches" in by_ref["Amos 3:12"]["draft_translation"]
    assert "like a flame of fire" in by_ref["Daniel 7:9"]["draft_translation"]
    assert "as the sound of thorns" in by_ref["Ecclesiastes 7:6"]["draft_translation"]
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
    assert "and a king speaking publicly among nation" in by_ref["Proverbs 30:31"][
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
    assert "because the mouth of sinner and the mouth of deceitful one" in by_ref[
        "Psalms 108:2"
    ]["draft_translation"]
    assert by_ref["Isaiah 11:3"]["draft_translation"].startswith("The spirit of fear of God")
    assert by_ref["Isaiah 19:3"]["draft_translation"].startswith("And the spirit of Egyptians")
    assert by_ref["Isaiah 61:1"]["draft_translation"].startswith("The Spirit of the Lord on me")
    assert by_ref["Jeremiah 4:12"]["draft_translation"].startswith("The spirit of fullness")
    assert by_ref["Ezekiel 11:5"]["draft_translation"].startswith("And the Spirit of the Lord fell")
    assert "but the word of our God remains" in by_ref["Isaiah 40:8"]["draft_translation"]
    assert by_ref["Proverbs 25:2"]["draft_translation"].startswith(
        "The glory of God hides a word"
    )
    assert by_ref["Isaiah 60:13"]["draft_translation"].startswith("The glory of Lebanon")
    assert by_ref["Isaiah 64:9"]["draft_translation"].startswith(
        "The city of your holy one became"
    )
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
    assert by_ref["Jonah 3:8"]["draft_translation"].startswith(
        "The people and cattle clothed themselves"
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
    assert "Many afflictions of the righteous ones" in by_ref["Psalms 33:20"]["draft_translation"]
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
    assert "The dwellers of rock will rejoice" in by_ref["Isaiah 42:11"]["draft_translation"]
    assert "The face of a prostitute became yours" in by_ref["Jeremiah 3:3"]["draft_translation"]
    assert by_ref["Hosea 9:7"]["draft_translation"].startswith(
        "The days of vengeance have come; the days of your repayment have come"
    )
    assert by_ref["Nahum 2:7"]["draft_translation"].startswith(
        "The gates of rivers were opened"
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
        "And the light of moon will be as the light of sun"
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
        "And the tract of sea will belong"
    )
    assert by_ref["Zechariah 9:12"]["draft_translation"].startswith(
        "You prisoners of the congregation will sit"
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
        "A voice from lips was heard"
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
    assert "it is a gift of God" in by_ref["Ecclesiastes 3:13"]["draft_translation"]
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
        "And this will be the downfall of horses"
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
    assert "where is the wrath of one afflicting you" in by_ref["Isaiah 51:13"]["draft_translation"]
    assert "Where is the multitude of your mercy" in by_ref["Isaiah 63:15"]["draft_translation"]
    assert "is the portion of Jacob" in by_ref["Jeremiah 10:16"]["draft_translation"]
    assert "it is a land of carved images" in by_ref["Jeremiah 27:38"]["draft_translation"]
    assert "there is a day of calling of defenders" in by_ref["Jeremiah 38:6"]["draft_translation"]
    assert by_ref["Ezekiel 43:12"]["draft_translation"].startswith("This is the law of the house")
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
    assert "She is the beginning of sin" in by_ref["Micah 1:13"]["draft_translation"]
    assert by_ref["Genesis 42:6"]["draft_translation"].startswith("And Joseph was the ruler")
    assert by_ref["Proverbs 9:1"]["draft_translation"].startswith(
        "Wisdom built a house for herself"
    )
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
    assert "upon the host of heaven and upon kings of the earth" in by_ref[
        "Isaiah 24:21"
    ]["draft_translation"]
    assert "if the foundation of the earth" in by_ref["Jeremiah 38:35"][
        "draft_translation"
    ]
    assert "all nations of the earth" in by_ref["Zechariah 12:3"]["draft_translation"]
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
    assert "under the sun, the number of days" in by_ref["Ecclesiastes 2:3"][
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
        "Wisdom will help the wise"
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
    assert "the valley of Achor for the rest of herds" in by_ref["Isaiah 65:10"]["draft_translation"]
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
    assert "where there was hope of help for him" in by_ref["Isaiah 30:32"]["draft_translation"]
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
    assert "All the words of God refined" in by_ref["Proverbs 30:5"]["draft_translation"]
    assert "The words of the wise in quiet" in by_ref["Ecclesiastes 9:17"]["draft_translation"]
    assert "The words of the wise are as goads" in by_ref["Ecclesiastes 12:11"]["draft_translation"]
    assert "all the words of the Lord which he answered" in by_ref["Jeremiah 43:4"]["draft_translation"]
    assert "read in the scroll the words of the Lord" in by_ref["Jeremiah 43:8"]["draft_translation"]
    assert "did not hear the words of the Lord" in by_ref["Jeremiah 44:2"]["draft_translation"]
    assert "like the appearance of a carbuncle stone" in by_ref["Ezekiel 10:9"]["draft_translation"]
    assert "like the fish of the great sea" in by_ref["Ezekiel 47:10"]["draft_translation"]
    assert "like the fish of the sea" in by_ref["Habakkuk 1:14"]["draft_translation"]
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
    assert by_ref["Isaiah 1:1"]["draft_translation"].startswith("The vision which Isaiah")
    assert by_ref["Isaiah 13:1"]["draft_translation"].startswith("The vision which Isaiah")
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
    assert "so the house of Israel proved faithless" in by_ref["Jeremiah 3:20"]["draft_translation"]
    assert "the house of Israel and the house of Judah acted faithlessly" in by_ref["Jeremiah 5:11"]["draft_translation"]
    assert "and the house of Judah broke my covenant" in by_ref["Jeremiah 11:10"]["draft_translation"]
    assert "brought up the house of Israel" in by_ref["Jeremiah 16:15"]["draft_translation"]
    assert "the remnant of Israel will no longer continue" in by_ref["Isaiah 10:20"]["draft_translation"]
    assert "people, the remnant of Israel" in by_ref["Jeremiah 38:7"]["draft_translation"]
    assert "the remnant of Judah perish" in by_ref["Jeremiah 47:15"]["draft_translation"]
    assert "wipe out the remnant of Israel" in by_ref["Ezekiel 9:8"]["draft_translation"]
    assert "bringing the remnant of Israel to an end" in by_ref["Ezekiel 11:13"]["draft_translation"]
    assert "receive the remnant of Israel" in by_ref["Micah 2:12"]["draft_translation"]
    assert "cloud of the glory of the Lord" in by_ref["2 Chronicles 5:13"]["draft_translation"]
    assert "and the glory of the Lord upon the house" in by_ref["2 Chronicles 7:3"]["draft_translation"]
    assert "Let the glory of the Lord be forever" in by_ref["Psalms 103:31"]["draft_translation"]
    assert "great is the glory of the Lord" in by_ref["Psalms 137:5"]["draft_translation"]
    assert "eclipse of the glory of Jacob" in by_ref["Isaiah 17:4"]["draft_translation"]
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
    assert "set your heart as the heart of a god" in by_ref["Ezekiel 28:2"]["draft_translation"]
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
    assert "to the top of cliff" in by_ref["2 Chronicles 25:12"]["draft_translation"]
    assert "from the top of Senir" in by_ref["Song of Solomon 4:8"]["draft_translation"]
    assert "at the corner of the court" in by_ref["Ezekiel 46:21"]["draft_translation"]
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
        "Who measured water with his hand and heaven with a span, and who set all the earth "
        "with a handful? Who set mountains with a scale and glens with a balance?"
    )
    assert "with a balance and with a bag of deceitful weights" in by_ref["Micah 6:11"]["draft_translation"]
    assert "the Lord stirred the spirit of Cyrus" in by_ref["Ezra 1:1"]["draft_translation"]
    assert "build for him a house in Jerusalem" in by_ref["2 Chronicles 36:23"]["draft_translation"]
    assert by_ref["Psalms 111:1"]["draft_translation"].startswith("Alleluia. Blessed is the man fearing the Lord")
    assert by_ref["Isaiah 31:9"]["draft_translation"].endswith(
        "Blessed is the one having seed in Zion and household in Jerusalem."
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
    assert "on the way of Horonaim" in by_ref["Isaiah 15:5"]["draft_translation"]
    assert "into the valley of Jehoshaphat" in by_ref["Joel 4:2"]["draft_translation"]
    assert "to the men of Judah" in by_ref["Jeremiah 4:3"]["draft_translation"]
    assert "after the thoughts of their evil heart" in by_ref["Jeremiah 3:17"]["draft_translation"]
    assert "with the wounded of sword" in by_ref["Ezekiel 31:18"]["draft_translation"]
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
    assert "from the king of the Assyrians" in by_ref["Isaiah 20:6"]["draft_translation"]
    assert "in the glory of the Lord" in by_ref["Isaiah 24:14"]["draft_translation"]
    assert "from the produce of your land" in by_ref["Isaiah 30:23"]["draft_translation"]
    assert "say to the cities of Judah" in by_ref["Isaiah 40:9"]["draft_translation"]
    assert "in the dark place of earth" in by_ref["Isaiah 45:19"]["draft_translation"]
    assert "to the generations of generations" in by_ref["Isaiah 51:8"]["draft_translation"]
    assert "by the strength of his arm" in by_ref["Isaiah 62:8"]["draft_translation"]
    assert "to whom the word of God came" in by_ref["Jeremiah 1:2"]["draft_translation"]
    assert "from the cities of Judah" in by_ref["Jeremiah 7:34"]["draft_translation"]
    assert "after the pleasures of their evil heart" in by_ref["Jeremiah 9:13"]["draft_translation"]
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
    assert "on the furrows of a field" in by_ref["Hosea 10:4"]["draft_translation"]
    assert "from the mount of Esau" in by_ref["Obadiah 1:8"]["draft_translation"]
    assert "at the right of lamp-bowl" in by_ref["Zechariah 4:3"]["draft_translation"]
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
    assert "for the rest of herds" in by_ref["Isaiah 65:10"]["draft_translation"]
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
    assert by_ref["Proverbs 10:21"]["draft_translation"].startswith("The lips of righteous know")
    assert by_ref["Proverbs 14:10"]["draft_translation"].startswith("The heart of perceptive man knows")
    assert by_ref["Ecclesiastes 7:4"]["draft_translation"].startswith("The heart of the wise")
    assert by_ref["1 Chronicles 2:29"]["draft_translation"].startswith(
        "And the name of the wife of Abishur"
    )
    assert by_ref["1 Chronicles 13:14"]["draft_translation"].startswith("And the ark of God stayed")
    assert by_ref["1 Chronicles 21:4"]["draft_translation"].startswith("But the word of the king prevailed")
    assert by_ref["2 Chronicles 9:1"]["draft_translation"].startswith("And the queen of Sheba heard")
    assert by_ref["Psalms 36:30"]["draft_translation"].startswith("The mouth of righteous man")
    assert "The river of God was filled" in by_ref["Psalms 64:10"]["draft_translation"]
    assert by_ref["Psalms 67:16"]["draft_translation"].startswith("The mountain of God")
    assert by_ref["Psalms 113:17"]["draft_translation"].startswith("The house of Israel hoped")
    assert by_ref["Isaiah 6:10"]["draft_translation"].startswith("For the heart of this people")
    assert by_ref["Isaiah 19:17"]["draft_translation"].startswith("And the land of Jews")
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
    assert "reported to him the words of Rabshakeh" in by_ref["Isaiah 36:22"]["draft_translation"]
    assert "tear apart the strength of kings" in by_ref["Isaiah 45:1"]["draft_translation"]
    assert "for the army of heaven" in by_ref["Jeremiah 7:18"]["draft_translation"]
    assert "Do not hear the words of prophets" in by_ref["Jeremiah 23:16"]["draft_translation"]
    assert "make the land of Babylon" in by_ref["Jeremiah 28:29"]["draft_translation"]
    assert "give them the land of Israel" in by_ref["Ezekiel 11:17"]["draft_translation"]
    assert "because of the blood of humans" in by_ref["Habakkuk 2:8"]["draft_translation"]
    assert by_ref["Isaiah 32:4"]["draft_translation"].startswith("And the heart of weak ones")
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
    assert "who will stand in his place" in by_ref["Ecclesiastes 4:15"]["draft_translation"]
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
    assert "wounded will be by the Lord" in by_ref["Isaiah 66:16"]["draft_translation"]
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
    assert by_ref["Ecclesiastes 7:4"]["draft_translation"].startswith("The heart of the wise")
    assert "and the heart of fools" in by_ref["Ecclesiastes 7:4"]["draft_translation"]
    assert "the heart of the king will perish and the heart of the rulers" in by_ref[
        "Jeremiah 4:9"
    ]["draft_translation"]
    assert "the voice of weeping and the voice of cry" in by_ref["Isaiah 65:19"]["draft_translation"]
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
    assert by_ref["Amos 9:12"]["draft_translation"].startswith("so that the remnant of men")
    assert "upon whom my name has been called may seek" in by_ref["Amos 9:12"]["draft_translation"]
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
