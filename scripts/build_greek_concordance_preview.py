#!/usr/bin/env python3
"""Build a separate compact Greek-driven concordance preview.

The source rows do not yet carry full lemmatization or word-level alignment.
This preview therefore starts from a curated Greek form table, scans the LXX/TR
Greek source text, and groups each Greek-term hit by the English rendering seen
in the draft translation.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

import build_print_proof_bible as print_builder
import build_study_bible as study_builder


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TERMS = ROOT / "data" / "research" / "greek_concordance_terms.csv"
DEFAULT_OT = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
DEFAULT_NT = ROOT / "data" / "raw" / "tr_greek" / "nt_full.csv"
DEFAULT_OUTPUT = ROOT / "output" / "concordance" / "the_greek_heritage_study_bible_greek_concordance_preview.md"
DEFAULT_DIAGNOSTICS = (
    ROOT / "output" / "concordance" / "the_greek_heritage_study_bible_greek_concordance_preview_diagnostics.json"
)
BROAD_OUTPUT = ROOT / "output" / "concordance" / "the_greek_heritage_study_bible_greek_concordance_broad_preview.md"
BROAD_DIAGNOSTICS = (
    ROOT / "output" / "concordance" / "the_greek_heritage_study_bible_greek_concordance_broad_preview_diagnostics.json"
)

GREEK_TOKEN_RE = re.compile(r"[Ͱ-Ͽ]+")


@dataclass(frozen=True)
class Term:
    entry_id: str
    english_heading: str
    greek_lemma: str
    transliteration: str
    testament: str
    greek_forms: frozenset[str]
    greek_stems: frozenset[str]
    english_renderings: tuple[str, ...]
    priority: str
    note: str


@dataclass(frozen=True)
class VerseRow:
    ref: str
    book_code: str
    book_name: str
    chapter: int
    verse: int
    source_stream: str
    greek_text: str
    draft_translation: str


@dataclass(frozen=True)
class Match:
    ref: str
    verse: VerseRow
    bucket: str


def normalize_greek(value: str) -> str:
    decomposed = unicodedata.normalize("NFD", value.casefold())
    stripped = "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")
    return unicodedata.normalize("NFC", stripped).replace("ς", "σ")


def greek_tokens(value: str) -> set[str]:
    return {normalize_greek(match.group(0)) for match in GREEK_TOKEN_RE.finditer(value)}


def normalize_english(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip()


def load_terms(path: Path) -> list[Term]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    terms: list[Term] = []
    for row in rows:
        if row["include"].strip().lower() not in {"yes", "true", "1"}:
            continue
        forms = {
            normalize_greek(form.strip())
            for form in row["greek_forms"].split(";")
            if form.strip()
        }
        forms.add(normalize_greek(row["greek_lemma"]))
        renderings = tuple(
            rendering.strip()
            for rendering in row["english_renderings"].split(";")
            if rendering.strip()
        )
        terms.append(
            Term(
                entry_id=row["entry_id"].strip(),
                english_heading=row["english_heading"].strip(),
                greek_lemma=row["greek_lemma"].strip(),
                transliteration=row["transliteration"].strip(),
                testament=row["testament"].strip().lower() or "both",
                greek_forms=frozenset(forms),
                greek_stems=frozenset(),
                english_renderings=renderings,
                priority=row["priority"].strip(),
                note=row["note"].strip(),
            )
        )
    return terms


def broad_term(
    entry_id: str,
    heading: str,
    lemma: str,
    transliteration: str,
    stems: str,
    renderings: str,
    priority: str = "broad",
    testament: str = "both",
    note: str = "",
) -> Term:
    stem_values = frozenset(
        normalize_greek(stem.strip()) for stem in stems.split(";") if stem.strip()
    )
    return Term(
        entry_id=entry_id,
        english_heading=heading,
        greek_lemma=lemma,
        transliteration=transliteration,
        testament=testament,
        greek_forms=frozenset({normalize_greek(lemma)}),
        greek_stems=stem_values,
        english_renderings=tuple(
            rendering.strip() for rendering in renderings.split(";") if rendering.strip()
        ),
        priority=priority,
        note=note,
    )


BROAD_TERMS: tuple[Term, ...] = (
    broad_term("god", "God", "θεός", "theos", "θεο", "God;god", "core", note="Core divine title."),
    broad_term("lord", "Lord / Master", "κύριος", "kyrios", "κυρι", "Lord;lord;master", "core", note="Divine title and human lord/master term."),
    broad_term("jesus", "Jesus", "Ἰησοῦς", "Iesous", "ιησου", "Jesus", "core", testament="nt"),
    broad_term("christ", "Christ / Messiah", "χριστός", "christos", "χριστ", "Christ;Messiah;anointed", "core", testament="nt"),
    broad_term("spirit", "Spirit / Wind / Breath", "πνεῦμα", "pneuma", "πνευμα", "Spirit;spirit;wind;breath"),
    broad_term("soul", "Soul / Life", "ψυχή", "psyche", "ψυχ", "soul;life"),
    broad_term("life", "Life", "ζωή", "zoe", "ζω", "life;living"),
    broad_term("word", "Word / Saying", "λόγος", "logos", "λογ", "word;words;saying;sayings;matter;account"),
    broad_term("gospel", "Good News / Gospel", "εὐαγγέλιον", "euangelion", "ευαγγελ", "gospel;good news"),
    broad_term("love", "Love", "ἀγάπη", "agape", "αγαπ", "love;beloved"),
    broad_term("faith", "Faith / Trust", "πίστις", "pistis", "πιστ", "faith;trust;faithfulness;believe"),
    broad_term("righteousness", "Righteousness / Justice", "δικαιοσύνη", "dikaiosyne", "δικαιο", "righteousness;justice;righteous;just"),
    broad_term("law", "Law", "νόμος", "nomos", "νομ", "law;laws"),
    broad_term("grace", "Grace / Favor", "χάρις", "charis", "χαρι", "grace;favor;thanks"),
    broad_term("sin", "Sin", "ἁμαρτία", "hamartia", "αμαρτ", "sin;sins;sinned"),
    broad_term("repentance", "Repentance", "μετάνοια", "metanoia", "μετανοι", "repentance;repent"),
    broad_term("resurrection", "Resurrection / Rising", "ἀνάστασις", "anastasis", "αναστα", "resurrection;rising;rise"),
    broad_term("assembly", "Assembly / Church", "ἐκκλησία", "ekklesia", "εκκλησι", "assembly;church;churches"),
    broad_term("covenant", "Covenant / Testament", "διαθήκη", "diatheke", "διαθηκ", "covenant;testament"),
    broad_term("wisdom", "Wisdom", "σοφία", "sophia", "σοφι", "wisdom;wise"),
    broad_term("glory", "Glory / Honor", "δόξα", "doxa", "δοξ", "glory;honor"),
    broad_term("angel", "Angel / Messenger", "ἄγγελος", "angelos", "αγγελ", "angel;messenger"),
    broad_term("truth", "Truth", "ἀλήθεια", "aletheia", "αληθει", "truth;true"),
    broad_term("peace", "Peace", "εἰρήνη", "eirene", "ειρην", "peace"),
    broad_term("hope", "Hope", "ἐλπίς", "elpis", "ελπι", "hope"),
    broad_term("light", "Light", "φῶς", "phos", "φωσ;φωτ", "light"),
    broad_term("darkness", "Darkness", "σκότος", "skotos", "σκοτ", "darkness"),
    broad_term("salvation", "Salvation / Saving", "σωτηρία", "soteria", "σωτηρ", "salvation;saving;save;savior"),
    broad_term("flesh", "Flesh", "σάρξ", "sarx", "σαρκ", "flesh"),
    broad_term("mercy", "Mercy", "ἔλεος", "eleos", "ελεο;ελεου;ελεει;ελεη", "mercy"),
    broad_term("blood", "Blood", "αἷμα", "haima", "αιμα", "blood"),
    broad_term("kingdom", "Kingdom", "βασιλεία", "basileia", "βασιλει", "kingdom"),
    broad_term("king", "King", "βασιλεύς", "basileus", "βασιλευ;βασιλεω", "king;kings"),
    broad_term("priest", "Priest", "ἱερεύς", "hiereus", "ιερε;ιερευ", "priest;priests"),
    broad_term("temple", "Temple", "ναός", "naos", "ναο", "temple;sanctuary"),
    broad_term("altar", "Altar", "θυσιαστήριον", "thysiasterion", "θυσιαστηρ", "altar"),
    broad_term("sacrifice", "Sacrifice / Offering", "θυσία", "thysia", "θυσι;προσφορ", "sacrifice;offering;offerings"),
    broad_term("lamb", "Lamb", "ἀμνός", "amnos", "αμν", "lamb"),
    broad_term("sheep", "Sheep", "πρόβατον", "probaton", "προβατ", "sheep"),
    broad_term("shepherd", "Shepherd", "ποιμήν", "poimen", "ποιμ", "shepherd"),
    broad_term("servant", "Servant / Slave", "δοῦλος", "doulos", "δουλ", "servant;slave;bondservant"),
    broad_term("son", "Son", "υἱός", "huios", "υιο", "son;sons"),
    broad_term("father", "Father", "πατήρ", "pater", "πατερ;πατρ", "father;fathers"),
    broad_term("brother", "Brother", "ἀδελφός", "adelphos", "αδελφ", "brother;brothers"),
    broad_term("woman", "Woman / Wife", "γυνή", "gyne", "γυν", "woman;wife;women;wives"),
    broad_term("man", "Man / Human", "ἄνθρωπος", "anthropos", "ανθρωπ", "man;human;person"),
    broad_term("heart", "Heart", "καρδία", "kardia", "καρδι", "heart"),
    broad_term("mind", "Mind", "νοῦς", "nous", "νοο;νου", "mind;understanding"),
    broad_term("mouth", "Mouth", "στόμα", "stoma", "στομα", "mouth"),
    broad_term("hand", "Hand", "χείρ", "cheir", "χειρ", "hand;hands"),
    broad_term("face", "Face / Presence", "πρόσωπον", "prosopon", "προσωπ", "face;presence"),
    broad_term("name", "Name", "ὄνομα", "onoma", "ονομα", "name"),
    broad_term("holy", "Holy / Saint", "ἅγιος", "hagios", "αγι", "holy;saint;saints"),
    broad_term("clean", "Clean / Pure", "καθαρός", "katharos", "καθαρ", "clean;pure"),
    broad_term("unclean", "Unclean", "ἀκάθαρτος", "akathartos", "ακαθαρ", "unclean"),
    broad_term("evil", "Evil / Bad", "πονηρός", "poneros", "πονηρ;κακ", "evil;bad;wicked"),
    broad_term("good", "Good", "ἀγαθός", "agathos", "αγαθ", "good"),
    broad_term("death", "Death", "θάνατος", "thanatos", "θανατ", "death;dead"),
    broad_term("hades", "Hades", "ᾅδης", "hades", "αδη", "Hades;hell"),
    broad_term("fire", "Fire", "πῦρ", "pyr", "πυρ", "fire"),
    broad_term("water", "Water", "ὕδωρ", "hydor", "υδωρ;υδατ", "water;waters"),
    broad_term("bread", "Bread", "ἄρτος", "artos", "αρτ", "bread;loaf;loaves"),
    broad_term("wine", "Wine", "οἶνος", "oinos", "οιν", "wine"),
    broad_term("oil", "Oil", "ἔλαιον", "elaion", "ελαι", "oil"),
    broad_term("judge", "Judge / Judgment", "κρίνω", "krino", "κριν;κρισ", "judge;judgment;condemn"),
    broad_term("wrath", "Wrath / Anger", "ὀργή", "orge", "οργ;θυμ", "wrath;anger;fierce"),
    broad_term("fear", "Fear", "φόβος", "phobos", "φοβ", "fear;afraid"),
    broad_term("joy", "Joy / Rejoicing", "χαρά", "chara", "χαρα;χαιρ", "joy;rejoice"),
    broad_term("prayer", "Prayer", "προσευχή", "proseuche", "προσευχ", "prayer;pray"),
    broad_term("worship", "Worship", "προσκυνέω", "proskyneo", "προσκυν", "worship"),
    broad_term("praise", "Praise", "αἰνέω", "aineo", "αιν;υμν", "praise;hymn"),
    broad_term("blessing", "Blessing", "εὐλογία", "eulogia", "ευλογ", "blessing;blessed;bless"),
    broad_term("curse", "Curse", "κατάρα", "katara", "καταρ", "curse;cursed"),
    broad_term("commandment", "Commandment", "ἐντολή", "entole", "εντολ", "commandment;commandments;command"),
    broad_term("teaching", "Teaching / Doctrine", "διδαχή", "didache", "διδαχ", "teaching;doctrine;teach"),
    broad_term("disciple", "Disciple", "μαθητής", "mathetes", "μαθητ", "disciple;disciples"),
    broad_term("prophet", "Prophet", "προφήτης", "prophetes", "προφητ", "prophet;prophets"),
    broad_term("apostle", "Apostle", "ἀπόστολος", "apostolos", "αποστολ", "apostle;apostles"),
    broad_term("elder", "Elder", "πρεσβύτερος", "presbyteros", "πρεσβυτ", "elder;elders"),
    broad_term("mystery", "Mystery", "μυστήριον", "mysterion", "μυστηρι", "mystery"),
    broad_term("power", "Power / Mighty Work", "δύναμις", "dynamis", "δυναμ", "power;mighty;miracle"),
    broad_term("authority", "Authority", "ἐξουσία", "exousia", "εξουσι", "authority;power"),
    broad_term("sign", "Sign", "σημεῖον", "semeion", "σημει", "sign;signs"),
    broad_term("work", "Work", "ἔργον", "ergon", "εργ", "work;works"),
    broad_term("world", "World", "κόσμος", "kosmos", "κοσμ", "world"),
    broad_term("heaven", "Heaven", "οὐρανός", "ouranos", "ουραν", "heaven;heavens"),
    broad_term("earth", "Earth / Land", "γῆ", "ge", "γη;γαι", "earth;land"),
    broad_term("sea", "Sea", "θάλασσα", "thalassa", "θαλασσ", "sea"),
    broad_term("mountain", "Mountain", "ὄρος", "oros", "οροσ;ορου;ορει;ορη;ορεσι;ορεων", "mountain;mountains"),
    broad_term("wilderness", "Wilderness / Desert", "ἔρημος", "eremos", "ερημ", "wilderness;desert"),
    broad_term("city", "City", "πόλις", "polis", "πολι", "city;cities"),
    broad_term("jerusalem", "Jerusalem", "Ἰερουσαλήμ", "Ierousalem", "ιερουσαλημ", "Jerusalem"),
    broad_term("israel", "Israel", "Ἰσραήλ", "Israel", "ισραηλ", "Israel"),
    broad_term("judah", "Judah", "Ἰούδα", "Iouda", "ιουδα", "Judah"),
    broad_term("zion", "Zion", "Σιών", "Sion", "σιων", "Zion"),
    broad_term("egypt", "Egypt", "Αἴγυπτος", "Aigyptos", "αιγυπτ", "Egypt"),
    broad_term("babylon", "Babylon", "Βαβυλών", "Babylon", "βαβυλ", "Babylon"),
    broad_term("david", "David", "Δαυίδ", "Dauid", "δαυιδ", "David"),
    broad_term("moses", "Moses", "Μωυσῆς", "Moses", "μωυσ;μωυση", "Moses"),
    broad_term("abraham", "Abraham", "Ἀβραάμ", "Abraam", "αβρααμ", "Abraham"),
    broad_term("seed", "Seed", "σπέρμα", "sperma", "σπερμ", "seed"),
    broad_term("promise", "Promise", "ἐπαγγελία", "epangelia", "επαγγελ", "promise"),
    broad_term("inheritance", "Inheritance", "κληρονομία", "kleronomia", "κληρονομ", "inheritance;heir"),
    broad_term("beginning", "Beginning", "ἀρχή", "arche", "αρχη;αρχαι", "beginning;first"),
    broad_term("day", "Day", "ἡμέρα", "hemera", "ημερ", "day;days"),
    broad_term("night", "Night", "νύξ", "nyx", "νυκτ", "night;nights"),
    broad_term("morning", "Morning", "πρωΐ", "proi", "πρωι;ορθρ", "morning;dawn"),
    broad_term("evening", "Evening", "ἑσπέρα", "hespera", "εσπερ", "evening"),
    broad_term("sabbath", "Sabbath", "σάββατον", "sabbaton", "σαββατ", "Sabbath;sabbaths"),
    broad_term("passover", "Passover", "πάσχα", "pascha", "πασχ", "Passover"),
    broad_term("feast", "Feast", "ἑορτή", "heorte", "εορτ", "feast;festival"),
    broad_term("fasting", "Fasting", "νηστεία", "nesteia", "νηστ", "fast;fasting"),
    broad_term("baptism", "Baptism / Washing", "βάπτισμα", "baptisma", "βαπτισ;βαπτιζ", "baptism;baptize;baptized;washing"),
    broad_term("forgiveness", "Forgiveness / Release", "ἄφεσις", "aphesis", "αφεσ", "forgiveness;release;forgive"),
    broad_term("redemption", "Redemption / Ransom", "λύτρωσις", "lytrosis", "λυτρ", "redemption;ransom;redeem"),
    broad_term("atonement", "Atonement / Mercy Seat", "ἱλαστήριον", "hilasterion", "ιλαστηρ;ιλασμ", "atonement;mercy seat;propitiation"),
    broad_term("cross", "Cross", "σταυρός", "stauros", "σταυρ", "cross"),
    broad_term("crown", "Crown", "στέφανος", "stephanos", "στεφαν", "crown"),
    broad_term("throne", "Throne", "θρόνος", "thronos", "θρον", "throne"),
    broad_term("judgment-seat", "Judgment Seat", "βῆμα", "bema", "βημα", "judgment seat;tribunal"),
    broad_term("parable", "Parable", "παραβολή", "parabole", "παραβολ", "parable;parables"),
    broad_term("healing", "Healing", "θεραπεία", "therapeia", "θεραπευ;ιασ", "heal;healing;cure"),
    broad_term("sickness", "Sickness / Disease", "νόσος", "nosos", "νοσο;νοσου;νοσων;νοσοι", "sickness;disease"),
    broad_term("blind", "Blind", "τυφλός", "typhlos", "τυφλ", "blind"),
    broad_term("poor", "Poor", "πτωχός", "ptochos", "πτωχ", "poor"),
    broad_term("rich", "Rich", "πλούσιος", "plousios", "πλουσ", "rich;wealth"),
    broad_term("widow", "Widow", "χήρα", "chera", "χηρ", "widow;widows"),
    broad_term("orphan", "Orphan / Fatherless", "ὀρφανός", "orphanos", "ορφαν", "orphan;fatherless"),
    broad_term("stranger", "Stranger / Foreigner", "ξένος", "xenos", "ξενο;ξενω;ξενι;παροικ", "stranger;foreigner;sojourner"),
    broad_term("enemy", "Enemy", "ἐχθρός", "echthros", "εχθρ", "enemy;enemies"),
    broad_term("friend", "Friend", "φίλος", "philos", "φιλ", "friend;friends"),
    broad_term("bride", "Bride", "νύμφη", "nymphe", "νυμφη", "bride"),
    broad_term("bridegroom", "Bridegroom", "νυμφίος", "nymphios", "νυμφι", "bridegroom"),
    broad_term("marriage", "Marriage / Wedding", "γάμος", "gamos", "γαμ", "marriage;wedding"),
    broad_term("house", "House", "οἶκος", "oikos", "οικ", "house;household"),
    broad_term("child", "Child", "τέκνον", "teknon", "τεκν;παιδ", "child;children;little child"),
    broad_term("mother", "Mother", "μήτηρ", "meter", "μητερ;μητρ", "mother;mothers"),
    broad_term("daughter", "Daughter", "θυγάτηρ", "thygater", "θυγατρ", "daughter;daughters"),
    broad_term("virgin", "Virgin", "παρθένος", "parthenos", "παρθεν", "virgin;virgins"),
    broad_term("birth", "Birth / Begetting", "γέννησις", "gennesis", "γενν", "birth;beget;born"),
    broad_term("creation", "Creation / Creature", "κτίσις", "ktisis", "κτισ", "creation;creature;created"),
    broad_term("new", "New", "καινός", "kainos", "καιν", "new"),
    broad_term("old", "Old", "παλαιός", "palaios", "παλαι", "old"),
    broad_term("way", "Way / Path", "ὁδός", "hodos", "οδο", "way;path;road"),
    broad_term("gate", "Gate", "πύλη", "pyle", "πυλ", "gate;gates"),
    broad_term("rock", "Rock", "πέτρα", "petra", "πετρα;πετραι;πετρων", "rock"),
    broad_term("stone", "Stone", "λίθος", "lithos", "λιθ", "stone;stones"),
    broad_term("tree", "Tree / Wood", "ξύλον", "xylon", "ξυλ", "tree;wood"),
    broad_term("fruit", "Fruit", "καρπός", "karpos", "καρπ", "fruit"),
    broad_term("vine", "Vine / Vineyard", "ἄμπελος", "ampelos", "αμπελ", "vine;vineyard"),
    broad_term("harvest", "Harvest", "θερισμός", "therismos", "θερισ", "harvest"),
    broad_term("field", "Field", "ἀγρός", "agros", "αγρ", "field;fields"),
    broad_term("sword", "Sword", "μάχαιρα", "machaira", "μαχαιρ;ρομφ", "sword"),
    broad_term("shield", "Shield", "θυρεός", "thyreos", "θυρε;ασπιδ", "shield;shields"),
    broad_term("trumpet", "Trumpet", "σάλπιγξ", "salpinx", "σαλπιγ", "trumpet"),
    broad_term("book", "Book / Scroll", "βίβλος", "biblos", "βιβλ", "book;scroll"),
    broad_term("seal", "Seal", "σφραγίς", "sphragis", "σφραγ", "seal"),
    broad_term("star", "Star", "ἀστήρ", "aster", "αστερ", "star;stars"),
    broad_term("sun", "Sun", "ἥλιος", "helios", "ηλι", "sun"),
    broad_term("moon", "Moon", "σελήνη", "selene", "σελην", "moon"),
    broad_term("cloud", "Cloud", "νεφέλη", "nephele", "νεφελ", "cloud"),
    broad_term("rain", "Rain", "ὑετός", "hyetos", "υετ", "rain"),
    broad_term("river", "River", "ποταμός", "potamos", "ποταμ", "river"),
    broad_term("spring", "Spring / Fountain", "πηγή", "pege", "πηγ", "spring;fountain"),
    broad_term("well", "Well", "φρέαρ", "phrear", "φρεαρ", "well"),
    broad_term("prison", "Prison / Guard", "φυλακή", "phylake", "φυλακ", "prison;guard"),
    broad_term("tower", "Tower", "πύργος", "pyrgos", "πυργ", "tower"),
    broad_term("gold", "Gold", "χρυσός", "chrysos", "χρυσ", "gold"),
    broad_term("silver", "Silver", "ἄργυρος", "argyros", "αργυρ", "silver"),
    broad_term("idol", "Idol", "εἴδωλον", "eidolon", "ειδωλ", "idol;idols"),
    broad_term("image", "Image", "εἰκών", "eikon", "εικον", "image"),
    broad_term("demon", "Demon", "δαιμόνιον", "daimonion", "δαιμον", "demon;demons"),
    broad_term("devil", "Devil", "διάβολος", "diabolos", "διαβολ", "devil"),
    broad_term("satan", "Satan", "Σατανᾶς", "Satanas", "σαταν", "Satan"),
    broad_term("dragon", "Dragon", "δράκων", "drakon", "δρακ", "dragon"),
    broad_term("serpent", "Serpent", "ὄφις", "ophis", "οφι", "serpent;snake"),
    broad_term("beast", "Beast", "θηρίον", "therion", "θηρι", "beast"),
    broad_term("mark", "Mark", "χάραγμα", "charagma", "χαραγμ", "mark"),
    broad_term("number", "Number", "ἀριθμός", "arithmos", "αριθμ", "number"),
    broad_term("witness", "Witness", "μάρτυς", "martys", "μαρτυρ;μαρτυσ", "witness;testify;testified;testifies"),
    broad_term("testimony", "Testimony", "μαρτυρία", "martyria", "μαρτυρι", "testimony"),
    broad_term("knowledge", "Knowledge", "γνῶσις", "gnosis", "γνωσ", "knowledge;know;known"),
    broad_term("understanding", "Understanding", "σύνεσις", "synesis", "συνεσ;συνι", "understanding;understand"),
    broad_term("counsel", "Counsel / Plan", "βουλή", "boule", "βουλ", "counsel;plan;purpose"),
    broad_term("will", "Will / Desire", "θέλημα", "thelema", "θελη", "will;desire"),
    broad_term("chosen", "Chosen / Elect", "ἐκλεκτός", "eklektos", "εκλεκ", "chosen;elect;choice"),
    broad_term("calling", "Calling", "κλῆσις", "klesis", "κλησ", "calling;call;called"),
    broad_term("sanctification", "Sanctification", "ἁγιασμός", "hagiasmos", "αγιασμ", "sanctification;holiness"),
    broad_term("justification", "Justification", "δικαίωσις", "dikaiosis", "δικαιω", "justify;justified;justification"),
    broad_term("adoption", "Adoption", "υἱοθεσία", "huiothesia", "υιοθεσι", "adoption"),
    broad_term("fellowship", "Fellowship / Communion", "κοινωνία", "koinonia", "κοινων", "fellowship;communion;share"),
    broad_term("reconciliation", "Reconciliation", "καταλλαγή", "katallage", "καταλλαγ", "reconciliation;reconcile"),
    broad_term("temptation", "Temptation / Testing", "πειρασμός", "peirasmos", "πειρασ", "temptation;test;trial;tempt"),
    broad_term("endurance", "Endurance / Patience", "ὑπομονή", "hypomone", "υπομον", "endurance;patience;endure"),
    broad_term("longsuffering", "Longsuffering", "μακροθυμία", "makrothymia", "μακροθυμ", "longsuffering;patient"),
    broad_term("meekness", "Meekness / Gentleness", "πραΰτης", "prautes", "πραυ", "meek;meekness;gentle"),
    broad_term("humility", "Humility", "ταπεινοφροσύνη", "tapeinophrosyne", "ταπειν", "humble;humility;lowly"),
    broad_term("pride", "Pride", "ὑπερηφανία", "hyperphania", "υπερηφαν;αλαζον", "pride;proud;arrogant"),
    broad_term("self-control", "Self-Control", "ἐγκράτεια", "enkrateia", "εγκρατ", "self-control;temperance"),
    broad_term("drunkenness", "Drunkenness", "μέθη", "methe", "μεθ;μεθυσ", "drunk;drunken;drunkenness"),
    broad_term("envy", "Envy", "φθόνος", "phthonos", "φθον", "envy;envies"),
    broad_term("strife", "Strife / Contention", "ἔρις", "eris", "εριδ;εριζ", "strife;contention"),
    broad_term("hatred", "Hatred", "μῖσος", "misos", "μισ", "hate;hatred"),
    broad_term("desire", "Desire / Lust", "ἐπιθυμία", "epithymia", "επιθυμ", "desire;lust"),
    broad_term("fornication", "Fornication", "πορνεία", "porneia", "πορν", "fornication;sexual immorality;harlot"),
    broad_term("adultery", "Adultery", "μοιχεία", "moicheia", "μοιχ", "adultery;adulterer"),
    broad_term("murder", "Murder", "φόνος", "phonos", "φον", "murder;slaughter"),
    broad_term("theft", "Theft", "κλοπή", "klope", "κλεπτ;κλοπ", "theft;steal;thief"),
    broad_term("falsehood", "Lie / Falsehood", "ψεῦδος", "pseudos", "ψευδ", "lie;false;liar"),
    broad_term("deceit", "Deceit", "δόλος", "dolos", "δολ", "deceit;guile"),
    broad_term("hypocrisy", "Hypocrisy", "ὑπόκρισις", "hypokrisis", "υποκρι", "hypocrisy;hypocrite"),
    broad_term("blasphemy", "Blasphemy", "βλασφημία", "blasphemia", "βλασφημ", "blasphemy;blaspheme"),
    broad_term("scripture", "Scripture / Writing", "γραφή", "graphe", "γραφ", "scripture;written;writing"),
    broad_term("psalm", "Psalm / Song", "ψαλμός", "psalmos", "ψαλμ", "psalm;psalms;song"),
    broad_term("prophecy", "Prophecy", "προφητεία", "propheteia", "προφητει", "prophecy;prophesy"),
    broad_term("vision", "Vision", "ὅρασις", "horasis", "ορασ;οπτασ;οραμ", "vision;sight"),
    broad_term("dream", "Dream", "ἐνύπνιον", "enypnion", "ενυπν;ονειρ", "dream;dreams"),
    broad_term("oath", "Oath", "ὅρκος", "horkos", "ορκ", "oath;swear"),
    broad_term("vow", "Vow", "εὐχή", "euche", "ευχ", "vow;vows"),
    broad_term("tabernacle", "Tabernacle / Tent", "σκηνή", "skene", "σκην", "tabernacle;tent;dwelling"),
    broad_term("ark", "Ark", "κιβωτός", "kibotos", "κιβωτ", "ark"),
    broad_term("veil", "Veil", "καταπέτασμα", "katapetasma", "καταπετασ", "veil"),
    broad_term("incense", "Incense", "θυμίαμα", "thymiama", "θυμια", "incense"),
    broad_term("burnt-offering", "Burnt Offering", "ὁλοκαύτωμα", "holokautoma", "ολοκαυτ", "burnt offering;whole burnt offering"),
    broad_term("tithe", "Tithe / Tenth", "δεκάτη", "dekate", "δεκατ", "tithe;tenth"),
    broad_term("firstfruits", "Firstfruits", "ἀπαρχή", "aparche", "απαρχ", "firstfruits;first fruits"),
    broad_term("unleavened", "Unleavened", "ἄζυμος", "azymos", "αζυμ", "unleavened"),
    broad_term("circumcision", "Circumcision", "περιτομή", "peritome", "περιτομ", "circumcision;circumcise;circumcised"),
    broad_term("scepter", "Rod / Scepter / Staff", "ῥάβδος", "rhabdos", "ραβδ", "rod;scepter;staff"),
    broad_term("scribe", "Scribe", "γραμματεύς", "grammateus", "γραμματ", "scribe;scribes"),
    broad_term("pharisee", "Pharisee", "Φαρισαῖος", "Pharisaios", "φαρισ", "Pharisee;Pharisees"),
    broad_term("sadducee", "Sadducee", "Σαδδουκαῖος", "Saddoukaios", "σαδδουκ", "Sadducee;Sadducees"),
    broad_term("tax-collector", "Tax Collector / Publican", "τελώνης", "telones", "τελων", "tax collector;publican"),
    broad_term("centurion", "Centurion", "ἑκατόνταρχος", "hekatontarchos", "εκατονταρχ", "centurion"),
    broad_term("soldier", "Soldier", "στρατιώτης", "stratiotes", "στρατιωτ", "soldier;soldiers"),
    broad_term("governor", "Governor / Ruler", "ἡγεμών", "hegemon", "ηγεμον", "governor;ruler"),
    broad_term("caesar", "Caesar", "Καῖσαρ", "Kaisar", "καισαρ", "Caesar"),
    broad_term("queen", "Queen", "βασίλισσα", "basilissa", "βασιλισσ", "queen"),
    broad_term("tribe", "Tribe", "φυλή", "phyle", "φυλ", "tribe;tribes"),
    broad_term("people", "People", "λαός", "laos", "λαο", "people"),
    broad_term("nation", "Nation / Gentiles", "ἔθνος", "ethnos", "εθν", "nation;nations;Gentiles"),
    broad_term("rome", "Rome / Roman", "Ῥώμη", "Rhome", "ρωμ", "Rome;Roman;Romans"),
    broad_term("galilee", "Galilee", "Γαλιλαία", "Galilaia", "γαλιλαι", "Galilee"),
    broad_term("samaria", "Samaria / Samaritan", "Σαμάρεια", "Samareia", "σαμαρει;σαμαρ", "Samaria;Samaritan"),
    broad_term("jordan", "Jordan", "Ἰορδάνης", "Iordanes", "ιορδαν", "Jordan"),
    broad_term("bethlehem", "Bethlehem", "Βηθλεέμ", "Bethleem", "βηθλεεμ", "Bethlehem"),
    broad_term("nazareth", "Nazareth / Nazarene", "Ναζαρέτ", "Nazaret", "ναζαρ", "Nazareth;Nazarene"),
    broad_term("canaan", "Canaan", "Χαναάν", "Chanaan", "χανααν", "Canaan;Canaanite"),
    broad_term("assyria", "Assyria", "Ἀσσυρία", "Assyria", "ασσυρ", "Assyria;Assyrian"),
    broad_term("moab", "Moab", "Μωάβ", "Moab", "μωαβ", "Moab;Moabite"),
    broad_term("edom", "Edom", "Ἐδώμ", "Edom", "εδωμ", "Edom;Edomite"),
    broad_term("philistine", "Philistine", "Φυλιστιίμ", "Phylistiim", "φυλιστ", "Philistine;Philistines"),
    broad_term("greek", "Greek / Hellene", "Ἕλλην", "Hellen", "ελλην", "Greek;Greeks;Hellenist"),
    broad_term("damascus", "Damascus", "Δαμασκός", "Damaskos", "δαμασκ", "Damascus"),
    broad_term("nineveh", "Nineveh", "Νινευή", "Nineue", "νινευ", "Nineveh"),
    broad_term("sodom", "Sodom", "Σόδομα", "Sodoma", "σοδομ", "Sodom"),
    broad_term("gomorrah", "Gomorrah", "Γόμορρα", "Gomorra", "γομορ", "Gomorrah"),
    broad_term("animal", "Animal / Living Creature", "ζῷον", "zoon", "ζωο;κτηνο", "animal;living creature;cattle"),
    broad_term("bird", "Bird", "πετεινόν", "peteinon", "πετειν", "bird;birds;winged"),
    broad_term("fish", "Fish", "ἰχθύς", "ichthys", "ιχθυ", "fish"),
    broad_term("creeping-thing", "Creeping Thing", "ἑρπετόν", "herpeton", "ερπετ", "creeping thing;creeping"),
    broad_term("grass", "Grass / Herb", "χόρτος", "chortos", "χορτ", "grass;herb"),
    broad_term("flower", "Flower", "ἄνθος", "anthos", "ανθ", "flower"),
    broad_term("milk", "Milk", "γάλα", "gala", "γαλα", "milk"),
    broad_term("honey", "Honey", "μέλι", "meli", "μελι", "honey"),
    broad_term("salt", "Salt", "ἅλας", "halas", "αλασ;αλατ", "salt"),
    broad_term("leaven", "Leaven", "ζύμη", "zyme", "ζυμ", "leaven"),
    broad_term("cup", "Cup", "ποτήριον", "poterion", "ποτηρ", "cup"),
    broad_term("lamp", "Lamp", "λύχνος", "lychnos", "λυχν", "lamp"),
    broad_term("lampstand", "Lampstand", "λυχνία", "lychnia", "λυχνι", "lampstand;candlestick"),
    broad_term("garment", "Garment / Clothing", "ἱμάτιον", "himation", "ιματ;ενδυμ;χιτων", "garment;clothing;tunic"),
    broad_term("head", "Head", "κεφαλή", "kephale", "κεφαλ", "head"),
    broad_term("eye", "Eye", "ὀφθαλμός", "ophthalmos", "οφθαλμ", "eye;eyes"),
    broad_term("foot", "Foot / Feet", "πούς", "pous", "ποδ", "foot;feet"),
    broad_term("ear", "Ear", "οὖς", "ous", "ωτ", "ear;ears"),
    broad_term("voice", "Voice / Sound", "φωνή", "phone", "φων", "voice;sound"),
    broad_term("cry", "Cry / Shout", "κραυγή", "krauge", "κραυγ", "cry;crying;shout"),
    broad_term("song", "Song", "ᾠδή", "ode", "ωδη;ασμ", "song;songs"),
    broad_term("sleep", "Sleep", "ὕπνος", "hypnos", "υπν", "sleep"),
    broad_term("measure", "Measure", "μέτρον", "metron", "μετρ", "measure"),
    broad_term("weight", "Weight / Scale", "στάθμιον", "stathmion", "σταθμ", "weight;scale"),
    broad_term("war", "War / Battle", "πόλεμος", "polemos", "πολεμ", "war;battle"),
    broad_term("army", "Army / Host", "στρατιά", "stratia", "στρατι;στρατευ", "army;host"),
    broad_term("bow", "Bow", "τόξον", "toxon", "τοξ", "bow"),
    broad_term("spear", "Spear", "λόγχη", "lonche", "λογχ", "spear"),
    broad_term("chariot", "Chariot", "ἅρμα", "harma", "αρμα", "chariot"),
    broad_term("horse", "Horse", "ἵππος", "hippos", "ιππ", "horse"),
    broad_term("captivity", "Captivity / Captive", "αἰχμαλωσία", "aichmalosia", "αιχμαλωτ", "captivity;captive"),
    broad_term("famine", "Famine", "λιμός", "limos", "λιμ", "famine"),
    broad_term("plague", "Plague / Wound", "πληγή", "plege", "πληγ", "plague;wound"),
    broad_term("earthquake", "Earthquake", "σεισμός", "seismos", "σεισμ", "earthquake"),
    broad_term("abyss", "Abyss", "ἄβυσσος", "abyssos", "αβυσσ", "abyss"),
    broad_term("pit", "Pit", "λάκκος", "lakkos", "λακκ", "pit"),
    broad_term("lake", "Lake", "λίμνη", "limne", "λιμνη", "lake"),
    broad_term("destruction", "Destruction / Perdition", "ἀπώλεια", "apoleia", "απωλ", "destruction;perdition;destroy"),
    broad_term("vengeance", "Vengeance", "ἐκδίκησις", "ekdikesis", "εκδικ", "vengeance;avenge"),
    broad_term("bowl", "Bowl / Vial", "φιάλη", "phiale", "φιαλ", "bowl;vial"),
    broad_term("rider", "Rider / Horseman", "ἱππεύς", "hippeus", "ιππευ", "rider;horseman"),
    broad_term("horn", "Horn", "κέρας", "keras", "κερα", "horn"),
    broad_term("mediator", "Mediator", "μεσίτης", "mesites", "μεσιτ", "mediator"),
    broad_term("evangelist", "Evangelist", "εὐαγγελιστής", "euangelistes", "ευαγγελιστ", "evangelist"),
    broad_term("overseer", "Overseer / Bishop", "ἐπίσκοπος", "episkopos", "επισκοπ", "overseer;bishop;visitation"),
    broad_term("deacon", "Deacon / Minister", "διάκονος", "diakonos", "διακον", "deacon;minister;servant"),
    broad_term("minister", "Minister / Service", "λειτουργός", "leitourgos", "λειτουργ", "minister;service"),
    broad_term("steward", "Steward", "οἰκονόμος", "oikonomos", "οικονομ", "steward;stewardship"),
    broad_term("teacher", "Teacher", "διδάσκαλος", "didaskalos", "διδασκαλ", "teacher"),
    broad_term("rabbi", "Rabbi", "ῥαββί", "rhabbi", "ραββ", "Rabbi"),
    broad_term("synagogue", "Synagogue", "συναγωγή", "synagoge", "συναγωγ", "synagogue;assembly"),
    broad_term("neighbor", "Neighbor", "πλησίον", "plesion", "πλησιον", "neighbor"),
    broad_term("affliction", "Affliction / Tribulation", "θλῖψις", "thlipsis", "θλιψ", "affliction;tribulation"),
    broad_term("persecution", "Persecution", "διωγμός", "diogmos", "διωγ", "persecution;persecute"),
    broad_term("comfort", "Comfort / Exhortation", "παράκλησις", "paraklesis", "παρακλη", "comfort;encourage;exhort"),
    broad_term("compassion", "Compassion", "σπλάγχνον", "splagchnon", "σπλαγχν;οικτιρ", "compassion;bowels"),
    broad_term("alms", "Alms", "ἐλεημοσύνη", "eleemosyne", "ελεημοσυν", "alms"),
    broad_term("hospitality", "Hospitality", "φιλοξενία", "philoxenia", "φιλοξεν", "hospitality"),
    broad_term("body", "Body", "σῶμα", "soma", "σωμα", "body;bodies"),
    broad_term("year", "Year", "ἔτος", "etos", "ετο;ενιαυτ", "year;years"),
    broad_term("hour", "Hour / Time", "ὥρα", "hora", "ωρα", "hour;time"),
    broad_term("appointed-time", "Appointed Time / Season", "καιρός", "kairos", "καιρ", "time;season"),
    broad_term("duration-time", "Time / Duration", "χρόνος", "chronos", "χρον", "time;times"),
    broad_term("honor-price", "Honor / Price", "τιμή", "time", "τιμ", "honor;price;value"),
    broad_term("husband-man", "Man / Husband", "ἀνήρ", "aner", "ανδρ;ανηρ", "man;husband"),
    broad_term("infant", "Infant / Babe", "βρέφος", "brephos", "βρεφ", "infant;babe"),
    broad_term("young-man", "Young Man", "νεανίας", "neanias", "νεαν", "young man;youth"),
    broad_term("dog", "Dog", "κύων", "kyon", "κυνο;κυν", "dog;dogs"),
    broad_term("root", "Root", "ῥίζα", "rhiza", "ριζ", "root"),
    broad_term("wind", "Wind", "ἄνεμος", "anemos", "ανεμ", "wind;winds"),
    broad_term("shadow", "Shadow", "σκιά", "skia", "σκι", "shadow"),
    broad_term("door", "Door", "θύρα", "thyra", "θυρ", "door;doors"),
    broad_term("village", "Village", "κώμη", "kome", "κωμ", "village;villages"),
    broad_term("gift", "Gift / Offering", "δῶρον", "doron", "δωρ", "gift;offering"),
    broad_term("reward-wages", "Reward / Wages", "μισθός", "misthos", "μισθ", "reward;wages;hire"),
    broad_term("food", "Food / Nourishment", "τροφή", "trophe", "τροφ;βρωσ", "food;nourishment;meat"),
    broad_term("grain", "Grain / Wheat", "σῖτος", "sitos", "σιτ;σταχυ", "grain;wheat;corn"),
    broad_term("fig-tree", "Fig Tree", "συκῆ", "syke", "συκ", "fig tree;fig"),
    broad_term("lily", "Lily", "κρίνον", "krinon", "κριν", "lily;lilies"),
    broad_term("bed", "Bed / Couch", "κλίνη", "kline", "κλιν", "bed;couch"),
    broad_term("sackcloth", "Sackcloth", "σάκκος", "sakkos", "σακκ", "sackcloth;sack"),
    broad_term("sandal", "Sandal / Shoe", "σανδάλιον", "sandalion", "σανδαλ;υποδημ", "sandal;shoe"),
    broad_term("tongue", "Tongue / Language", "γλῶσσα", "glossa", "γλωσσ", "tongue;language"),
    broad_term("lip", "Lip", "χείλος", "cheilos", "χειλ", "lip;lips"),
    broad_term("hair", "Hair", "θρίξ", "thrix", "τριχ;θριξ", "hair"),
    broad_term("bone", "Bone", "ὀστοῦν", "ostoun", "οστ", "bone;bones"),
    broad_term("belly-womb", "Belly / Womb", "κοιλία", "koilia", "κοιλι", "belly;womb"),
    broad_term("finger", "Finger", "δάκτυλος", "daktylos", "δακτυλ", "finger"),
    broad_term("knee", "Knee", "γόνυ", "gony", "γον", "knee;knees"),
    broad_term("wing", "Wing", "πτέρυξ", "pteryx", "πτερυγ;πτερ", "wing;wings"),
    broad_term("conscience", "Conscience", "συνείδησις", "syneidesis", "συνειδη", "conscience"),
    broad_term("sorrow", "Sorrow / Grief", "λύπη", "lype", "λυπ", "sorrow;grief"),
    broad_term("trespass", "Trespass / Offense", "παράπτωμα", "paraptoma", "παραπτω", "trespass;offense"),
    broad_term("lawlessness", "Lawlessness / Iniquity", "ἀνομία", "anomia", "ανομ", "lawlessness;iniquity"),
    broad_term("wickedness", "Wickedness", "πονηρία", "poneria", "πονηρι", "wickedness;evil"),
    broad_term("unbelief", "Unbelief / Faithlessness", "ἀπιστία", "apistia", "απιστ", "unbelief;faithlessness"),
    broad_term("foolishness", "Foolishness", "μωρία", "moria", "μωρι;μωρο", "foolishness;foolish"),
    broad_term("stumbling-block", "Stumbling Block / Offense", "σκάνδαλον", "skandalon", "σκανδαλ", "stumbling block;offense;offence"),
    broad_term("covetousness", "Covetousness / Greed", "πλεονεξία", "pleonexia", "πλεονεξ", "covetousness;greed"),
    broad_term("zeal", "Zeal / Jealousy", "ζῆλος", "zelos", "ζηλ", "zeal;jealousy;envy"),
    broad_term("anxiety", "Care / Anxiety", "μέριμνα", "merimna", "μεριμν", "care;anxiety"),
    broad_term("spiritual", "Spiritual", "πνευματικός", "pneumatikos", "πνευματικ", "spiritual"),
    broad_term("liberty", "Liberty / Freedom", "ἐλευθερία", "eleutheria", "ελευθερ", "liberty;freedom"),
    broad_term("bondage", "Bondage / Slavery", "δουλεία", "douleia", "δουλει", "bondage;slavery"),
    broad_term("revelation", "Revelation / Unveiling", "ἀποκάλυψις", "apokalypsis", "αποκαλυψ", "revelation;unveiling"),
    broad_term("boldness", "Boldness", "παρρησία", "parresia", "παρρησι", "boldness"),
    broad_term("seek", "Seek", "ζητέω", "zeteo", "ζητε;ζητη", "seek;seeking"),
    broad_term("find", "Find", "εὑρίσκω", "heurisko", "ευρ", "find;found"),
    broad_term("hear", "Hear", "ἀκούω", "akouo", "ακου", "hear;heard;hearken"),
    broad_term("see", "See / Look", "βλέπω", "blepo", "βλεπ;ορα", "see;saw;look;behold"),
    broad_term("remember", "Remember", "μνημονεύω", "mnemoneuo", "μνημ", "remember;memory;memorial"),
    broad_term("forget", "Forget", "ἐπιλανθάνομαι", "epilanthanomai", "επιλανθ;λησμον", "forget;forgotten"),
    broad_term("ask", "Ask", "αἰτέω", "aiteo", "αιτε;ερωτ", "ask;asked;request"),
    broad_term("answer", "Answer", "ἀποκρίνομαι", "apokrinomai", "αποκρι", "answer;answered"),
    broad_term("confess", "Confess", "ὁμολογέω", "homologeo", "ομολογ", "confess;confession"),
    broad_term("preach", "Preach / Proclaim", "κηρύσσω", "kerysso", "κηρυσσ", "preach;proclaim"),
    broad_term("send", "Send", "ἀποστέλλω", "apostello", "αποστελλ;πεμπ", "send;sent"),
    broad_term("receive", "Receive / Take", "λαμβάνω", "lambano", "λαμβαν;λημψ;ληφ", "receive;take;took;taken"),
    broad_term("give", "Give", "δίδωμι", "didomi", "διδω;δωσ;εδωκ;δοθ", "give;gave;given"),
    broad_term("follow", "Follow", "ἀκολουθέω", "akoloutheo", "ακολουθ", "follow;followed"),
    broad_term("teach-verb", "Teach", "διδάσκω", "didasko", "διδασκ", "teach;taught"),
    broad_term("learn", "Learn", "μανθάνω", "manthano", "μανθαν", "learn;learned"),
    broad_term("obey", "Obey", "ὑπακούω", "hypakouo", "υπακου", "obey;obedience"),
    broad_term("disobey", "Disobey", "ἀπειθέω", "apeitheo", "απειθ", "disobey;disobedience;unbelief"),
    broad_term("keep-guard", "Keep / Guard", "τηρέω", "tereo", "τηρε;φυλασσ", "keep;kept;guard;watch"),
    broad_term("walk", "Walk", "περιπατέω", "peripateo", "περιπατ;πορευ", "walk;walked;go"),
    broad_term("dwell", "Dwell / Inhabit", "κατοικέω", "katoikeo", "κατοικ;οικε", "dwell;inhabit;live"),
    broad_term("rise", "Rise / Raise", "ἐγείρω", "egeiro", "εγειρ;αναστη", "rise;raised;arose"),
    broad_term("fall", "Fall", "πίπτω", "pipto", "πιπτ;πεσ", "fall;fell;fallen"),
    broad_term("eat", "Eat", "ἐσθίω", "esthio", "εσθι;φαγ", "eat;ate"),
    broad_term("drink", "Drink", "πίνω", "pino", "πιν;πιε", "drink;drank"),
    broad_term("wash", "Wash", "νίπτω", "nipto", "νιπτ;λου", "wash;washed"),
    broad_term("anoint", "Anoint", "χρίω", "chrio", "χριω;αλειφ", "anoint;anointed"),
    broad_term("write", "Write", "γράφω", "grapho", "γραφ", "write;written;wrote"),
    broad_term("read", "Read", "ἀναγινώσκω", "anaginosko", "αναγινωσκ", "read"),
    broad_term("open", "Open", "ἀνοίγω", "anoigo", "ανοιγ", "open;opened"),
    broad_term("shut", "Shut / Close", "κλείω", "kleio", "κλει", "shut;closed"),
    broad_term("build", "Build", "οἰκοδομέω", "oikodomeo", "οικοδομ", "build;built"),
    broad_term("destroy-verb", "Destroy", "ἀπόλλυμι", "apollymi", "απολλυ;ολεθρ", "destroy;destroyed;perish"),
    broad_term("save-verb", "Save", "σῴζω", "sozo", "σωζ", "save;saved"),
    broad_term("deliver-rescue", "Deliver / Rescue", "ῥύομαι", "rhyomai", "ρυσ;ρυο", "deliver;rescue"),
    broad_term("call", "Call", "καλέω", "kaleo", "καλε;κληθ", "call;called"),
    broad_term("turn", "Turn / Return", "στρέφω", "strepho", "στρεφ;επιστρεφ", "turn;turned;return"),
    broad_term("lead", "Lead / Bring", "ἄγω", "ago", "αγαγ;αγω;ηγαγ", "lead;brought;bring"),
    broad_term("bear-carry", "Bear / Carry", "φέρω", "phero", "φερ;ενεγκ", "bear;carry;brought"),
    broad_term("speak", "Speak", "λαλέω", "laleo", "λαλε", "speak;spoke"),
    broad_term("weep", "Weep", "κλαίω", "klaio", "κλαι;δακρυ", "weep;wept;tears"),
    broad_term("touch", "Touch", "ἅπτω", "hapto", "απτ;θιγ", "touch;touched"),
    broad_term("bind", "Bind", "δέω", "deo", "δεσμ;δεδε", "bind;bound"),
    broad_term("loose", "Loose / Release", "λύω", "lyo", "λυ;απολυ", "loose;release"),
    broad_term("tempt-test", "Test / Prove", "δοκιμάζω", "dokimazo", "δοκιμ", "test;prove;approved"),
    broad_term("pure-heart", "Pure", "ἁγνός", "hagnos", "αγν", "pure;chaste"),
    broad_term("kindness", "Kindness", "χρηστότης", "chrestotes", "χρηστ", "kindness;kind"),
    broad_term("thanksgiving", "Thanksgiving", "εὐχαριστία", "eucharistia", "ευχαριστ", "thank;thanksgiving"),
    broad_term("victory", "Victory / Overcome", "νίκη", "nike", "νικ", "victory;overcome;conquer"),
    broad_term("shame", "Shame", "αἰσχύνη", "aischyne", "αισχυν", "shame;ashamed"),
    broad_term("patriarch", "Patriarch", "πατριάρχης", "patriarches", "πατριαρχ", "patriarch"),
    broad_term("tomb", "Tomb / Grave", "μνημεῖον", "mnemeion", "μνημει;ταφ", "tomb;grave;sepulcher"),
    broad_term("crucify", "Crucify", "σταυρόω", "stauroo", "σταυρο", "crucify;crucified"),
    broad_term("Adam", "Adam", "Ἀδάμ", "Adam", "αδαμ", "Adam"),
    broad_term("Noah", "Noah", "Νῶε", "Noe", "νωε", "Noah"),
    broad_term("Isaac", "Isaac", "Ἰσαάκ", "Isaak", "ισαακ", "Isaac"),
    broad_term("Jacob", "Jacob", "Ἰακώβ", "Iakob", "ιακωβ", "Jacob"),
    broad_term("Joseph", "Joseph", "Ἰωσήφ", "Ioseph", "ιωσηφ", "Joseph"),
    broad_term("Aaron", "Aaron", "Ἀαρών", "Aaron", "ααρων", "Aaron"),
    broad_term("Joshua", "Joshua", "Ἰησοῦς", "Iesous", "ιησου", "Joshua", testament="ot"),
    broad_term("Sarah", "Sarah", "Σάρρα", "Sarra", "σαρρα", "Sarah"),
    broad_term("Rebekah", "Rebekah", "Ῥεβέκκα", "Rebekka", "ρεβεκ", "Rebekah;Rebecca"),
    broad_term("Rachel", "Rachel", "Ῥαχήλ", "Rachel", "ραχηλ", "Rachel"),
    broad_term("Samuel", "Samuel", "Σαμουήλ", "Samouel", "σαμουηλ", "Samuel"),
    broad_term("Saul", "Saul", "Σαούλ", "Saoul", "σαουλ", "Saul"),
    broad_term("Solomon", "Solomon", "Σαλωμών", "Salomon", "σαλωμων", "Solomon"),
    broad_term("Daniel", "Daniel", "Δανιήλ", "Daniel", "δανιηλ", "Daniel"),
    broad_term("Peter", "Peter", "Πέτρος", "Petros", "πετρ", "Peter", testament="nt"),
    broad_term("Paul", "Paul", "Παῦλος", "Paulos", "παυλ", "Paul", testament="nt"),
    broad_term("John", "John", "Ἰωάννης", "Ioannes", "ιωανν", "John", testament="nt"),
    broad_term("James", "James", "Ἰάκωβος", "Iakobos", "ιακωβ", "James", testament="nt"),
    broad_term("Mary", "Mary", "Μαρία", "Maria", "μαρι", "Mary", testament="nt"),
    broad_term("Pilate", "Pilate", "Πιλᾶτος", "Pilatos", "πιλατ", "Pilate", testament="nt"),
    broad_term("Herod", "Herod", "Ἡρῴδης", "Herodes", "ηρωδ", "Herod", testament="nt"),
)


def count_configured_terms(path: Path) -> tuple[int, int]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    included = sum(1 for row in rows if row["include"].strip().lower() in {"yes", "true", "1"})
    return len(rows), included


def load_source_rows(path: Path, source_stream: str) -> list[VerseRow]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = []
        for row in csv.DictReader(handle):
            greek_text = row["greek_text"].strip()
            if greek_text == "MT-only insertion; no LXX Greek row":
                continue
            rows.append(
                VerseRow(
                    ref=row["ref"],
                    book_code=row["book_code"],
                    book_name=row["book_name"],
                    chapter=int(row["chapter"]),
                    verse=int(row["verse"]),
                    source_stream=source_stream,
                    greek_text=greek_text,
                    draft_translation=row["draft_translation"],
                )
            )
    return rows


def term_applies(term: Term, source_stream: str) -> bool:
    return term.testament in {"both", source_stream}


def rendering_bucket(term: Term, draft_translation: str) -> str:
    normalized = normalize_english(draft_translation)
    for rendering in term.english_renderings:
        if re.search(rf"\b{re.escape(normalize_english(rendering))}\b", normalized):
            return rendering
    return "other rendering"


def term_matches_tokens(term: Term, tokens: set[str]) -> bool:
    if not tokens.isdisjoint(term.greek_forms):
        return True
    if term.greek_stems and any(
        token.startswith(stem) for token in tokens for stem in term.greek_stems
    ):
        return True
    return False


def format_refs(refs: list[str]) -> str:
    return "; ".join(print_builder.abbreviate_print_crossref(ref) for ref in refs)


SECTION_ORDER = {
    "torah": 0,
    "history": 1,
    "wisdom": 2,
    "prophets": 3,
    "gospels": 4,
    "acts": 5,
    "paul": 6,
    "general": 7,
    "revelation": 8,
}

SECTION_BY_BOOK_CODE = {
    **{code: "torah" for code in ["GEN", "EXO", "LEV", "NUM", "DEU"]},
    **{
        code: "history"
        for code in [
            "JOS",
            "JDG",
            "RUT",
            "1SA",
            "2SA",
            "1KI",
            "2KI",
            "1CH",
            "2CH",
            "EZR",
            "NEH",
            "EST",
            "ESG",
        ]
    },
    **{code: "wisdom" for code in ["JOB", "PSA", "PRO", "ECC", "SNG"]},
    **{
        code: "prophets"
        for code in [
            "ISA",
            "JER",
            "LAM",
            "EZK",
            "DAN",
            "DAG",
            "HOS",
            "JOL",
            "AMO",
            "OBA",
            "JON",
            "MIC",
            "NAM",
            "HAB",
            "ZEP",
            "HAG",
            "ZEC",
            "MAL",
        ]
    },
    **{code: "gospels" for code in ["MAT", "MRK", "LUK", "JHN"]},
    "ACT": "acts",
    **{code: "paul" for code in ["ROM", "1CO", "2CO", "GAL", "EPH", "PHP", "COL", "1TH", "2TH", "1TI", "2TI", "TIT", "PHM"]},
    **{code: "general" for code in ["HEB", "JAS", "1PE", "2PE", "1JN", "2JN", "3JN", "JUD"]},
    "REV": "revelation",
}

ANCHOR_REFS = {
    "god": {"Genesis 1:1", "John 1:1", "John 3:16"},
    "lord": {"Genesis 2:4", "Psalm 23:1", "Romans 10:9"},
    "jesus": {"Matthew 1:1", "John 1:17", "Acts 4:10"},
    "christ": {"Matthew 1:1", "John 20:31", "Romans 5:8"},
    "spirit": {"Genesis 1:2", "John 3:5", "Acts 2:4", "Romans 8:9"},
    "soul": {"Genesis 2:7", "Matthew 10:28", "1 Corinthians 15:45"},
    "life": {"John 1:4", "John 3:16", "John 14:6", "Revelation 22:1"},
    "word": {"John 1:1", "Hebrews 4:12", "Revelation 19:13"},
    "love": {"John 3:16", "1 Corinthians 13:4", "1 John 4:8"},
    "faith": {"Genesis 15:6", "Romans 1:17", "Hebrews 11:1"},
    "righteousness": {"Genesis 15:6", "Matthew 5:6", "Romans 3:22"},
    "law": {"Exodus 24:12", "Psalm 1:2", "Romans 3:20"},
    "grace": {"John 1:14", "Ephesians 2:8", "Titus 2:11"},
    "sin": {"Genesis 4:7", "Romans 3:23", "1 John 1:9"},
    "resurrection": {"Matthew 22:23", "John 11:25", "1 Corinthians 15:12"},
    "gospel": {"Mark 1:1", "Romans 1:16", "1 Corinthians 15:1"},
    "covenant": {"Genesis 9:9", "Jeremiah 38:31", "Hebrews 8:8"},
    "kingdom": {"Matthew 3:2", "John 3:3", "Romans 14:17"},
    "blood": {"Exodus 12:7", "Matthew 26:28", "Hebrews 9:14"},
}


def ref_sort_key(ref: str) -> tuple[int, int, int, str]:
    return study_builder.sort_cross_reference_key(ref)


def section_key(verse: VerseRow) -> str:
    return SECTION_BY_BOOK_CODE.get(verse.book_code, "general")


def match_score(term: Term, match: Match) -> tuple[int, tuple[int, int, int, str]]:
    score = 0
    normalized = normalize_english(match.verse.draft_translation)
    if match.bucket != "other rendering":
        score += 80
    if match.ref in ANCHOR_REFS.get(term.entry_id, set()):
        score += 120
    if match.verse.source_stream == "nt":
        score += 20
    if re.search(rf"\b{re.escape(normalize_english(term.english_heading.split('/')[0]))}\b", normalized):
        score += 10
    return -score, ref_sort_key(match.ref)


def select_ranked_matches(
    term: Term,
    matches: list[Match],
    *,
    max_refs: int,
) -> tuple[list[Match], int]:
    if len(matches) <= max_refs:
        return sorted(matches, key=lambda match: ref_sort_key(match.ref)), 0
    by_section: dict[str, list[Match]] = defaultdict(list)
    for match in matches:
        by_section[section_key(match.verse)].append(match)
    for key, values in by_section.items():
        by_section[key] = sorted(values, key=lambda match: match_score(term, match))
    selected: list[Match] = []
    seen: set[str] = set()
    anchor_refs = ANCHOR_REFS.get(term.entry_id, set())
    for match in sorted(matches, key=lambda match: (match.ref not in anchor_refs, ref_sort_key(match.ref))):
        if match.ref in anchor_refs and match.ref not in seen:
            selected.append(match)
            seen.add(match.ref)
            if len(selected) >= max_refs:
                break
    while len(selected) < max_refs:
        added = False
        for section in sorted(by_section, key=lambda key: SECTION_ORDER.get(key, 99)):
            while by_section[section] and by_section[section][0].ref in seen:
                by_section[section].pop(0)
            if not by_section[section]:
                continue
            match = by_section[section].pop(0)
            selected.append(match)
            seen.add(match.ref)
            added = True
            if len(selected) >= max_refs:
                break
        if not added:
            break
    return sorted(selected, key=lambda match: ref_sort_key(match.ref)), len(matches) - len(selected)


def build_broad_concordance(
    terms: list[Term],
    verses: list[VerseRow],
    *,
    max_refs_per_rendering: int,
    max_other_rendering_refs: int,
) -> tuple[str, dict[str, object]]:
    term_matches: dict[str, dict[str, list[Match]]] = {}
    term_totals: Counter[str] = Counter()
    rendering_totals: Counter[str] = Counter()
    omitted_by_rendering: Counter[str] = Counter()
    suppressed_other_rendering_hits: Counter[str] = Counter()
    rendered_terms = 0

    verse_tokens = [(verse, greek_tokens(verse.greek_text)) for verse in verses]
    for term in terms:
        groups: dict[str, list[Match]] = defaultdict(list)
        for verse, tokens in verse_tokens:
            if not term_applies(term, verse.source_stream):
                continue
            if not term_matches_tokens(term, tokens):
                continue
            bucket = rendering_bucket(term, verse.draft_translation)
            groups[bucket].append(Match(verse.ref, verse, bucket))
            term_totals[term.entry_id] += 1
            rendering_totals[f"{term.entry_id}:{bucket}"] += 1
        term_matches[term.entry_id] = dict(groups)

    lines = [
        "# Greek-Driven Concordance",
        "",
        "Selective concordance from curated Greek lemmas and stems. References are capped for print and ranked by anchor passages, visible rendering, canonical spread, New Testament use, and canonical order.",
        "",
    ]
    for term in terms:
        groups = term_matches[term.entry_id]
        if not groups:
            continue
        rendered_lines: list[str] = []
        for rendering in sorted(groups, key=lambda key: (key == "other rendering", key.casefold())):
            if rendering == "other rendering":
                suppressed_other_rendering_hits[term.entry_id] += len(groups[rendering])
                omitted_by_rendering[f"{term.entry_id}:{rendering}"] = len(groups[rendering])
                continue
            selected, omitted = select_ranked_matches(
                term,
                groups[rendering],
                max_refs=max_refs_per_rendering,
            )
            omitted_by_rendering[f"{term.entry_id}:{rendering}"] = omitted
            refs = [match.ref for match in selected]
            rendered_lines.append(f"**{rendering}:** {format_refs(refs)}")
        if not rendered_lines:
            continue
        rendered_terms += 1
        lines.extend(
            [
                f"## {term.english_heading} ({term.greek_lemma}, {term.transliteration})",
                "",
            ]
        )
        for rendered_line in rendered_lines:
            lines.append(rendered_line)
            lines.append("")

    markdown = "\n".join(lines).rstrip() + "\n"
    word_count = len(re.findall(r"\S+", markdown))
    diagnostics: dict[str, object] = {
        "profile": "broad-capped",
        "terms_configured": len(terms),
        "terms_with_matches": sum(1 for term in terms if term_matches[term.entry_id]),
        "source_rows_scanned": len(verses),
        "total_greek_term_hits": sum(term_totals.values()),
        "rough_word_count": word_count,
        "rough_page_estimate_at_450_words": round(word_count / 450, 1),
        "rough_compact_print_page_estimate_at_900_words": round(word_count / 900, 1),
        "page_budget_target": 30,
        "page_budget_estimate_field": "rough_compact_print_page_estimate_at_900_words",
        "max_refs_per_rendering": max_refs_per_rendering,
        "max_other_rendering_refs": max_other_rendering_refs,
        "total_omitted_refs": sum(omitted_by_rendering.values()),
        "terms_rendered": rendered_terms,
        "suppressed_other_rendering_hits": sum(suppressed_other_rendering_hits.values()),
        "term_hit_counts": dict(term_totals),
        "rendering_hit_counts": dict(rendering_totals),
        "omitted_by_rendering": dict(omitted_by_rendering),
        "suppressed_other_rendering_by_term": dict(suppressed_other_rendering_hits),
        "method": "curated Greek stems normalized for accents/final sigma, grouped by English rendering hints in draft_translation",
        "ranking": "anchor refs, visible rendering match, canonical section spread, NT usage, canonical order",
        "reference_format": "print book abbreviations via build_print_proof_bible.abbreviate_print_crossref",
    }
    return markdown, diagnostics


def build_concordance(terms: list[Term], verses: list[VerseRow]) -> tuple[str, dict[str, object]]:
    term_matches: dict[str, dict[str, list[str]]] = {}
    term_totals: Counter[str] = Counter()
    rendering_totals: Counter[str] = Counter()

    verse_tokens = [(verse, greek_tokens(verse.greek_text)) for verse in verses]

    for term in terms:
        groups: dict[str, list[str]] = defaultdict(list)
        for verse, tokens in verse_tokens:
            if not term_applies(term, verse.source_stream):
                continue
            if tokens.isdisjoint(term.greek_forms):
                continue
            bucket = rendering_bucket(term, verse.draft_translation)
            groups[bucket].append(verse.ref)
            term_totals[term.entry_id] += 1
            rendering_totals[f"{term.entry_id}:{bucket}"] += 1
        term_matches[term.entry_id] = dict(groups)

    lines = [
        "# Greek-Driven Concordance Preview",
        "",
        "Separate working preview for a possible compact print appendix. Entries are driven by curated Greek source forms, not by English surface words alone. Verse lists use the current project numbering.",
        "",
        "This is not wired into the print Bible yet. It is a sizing and usefulness draft.",
        "",
    ]

    for term in terms:
        groups = term_matches[term.entry_id]
        if not groups:
            continue
        lines.extend(
            [
                f"## {term.english_heading}",
                "",
                f"Greek: {term.greek_lemma} ({term.transliteration}). {term.note}",
                "",
            ]
        )
        for rendering in sorted(groups, key=lambda key: (key == "other rendering", key.casefold())):
            refs = groups[rendering]
            lines.extend(
                [
                    f"**{rendering}** ({len(refs)}): {format_refs(refs)}",
                    "",
                ]
            )

    markdown = "\n".join(lines).rstrip() + "\n"
    word_count = len(re.findall(r"\S+", markdown))
    diagnostics: dict[str, object] = {
        "terms_configured": len(terms),
        "terms_with_matches": sum(1 for term in terms if term_matches[term.entry_id]),
        "source_rows_scanned": len(verses),
        "total_greek_term_hits": sum(term_totals.values()),
        "rough_word_count": word_count,
        "rough_page_estimate_at_450_words": round(word_count / 450, 1),
        "page_budget_target": 30,
        "term_hit_counts": dict(term_totals),
        "rendering_hit_counts": dict(rendering_totals),
        "method": "curated Greek forms normalized for accents/final sigma, grouped by English rendering hints in draft_translation",
        "reference_format": "print book abbreviations via build_print_proof_bible.abbreviate_print_crossref",
    }
    return markdown, diagnostics


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=["focused", "broad"], default="focused")
    parser.add_argument("--terms", type=Path, default=DEFAULT_TERMS)
    parser.add_argument("--ot-source", type=Path, default=DEFAULT_OT)
    parser.add_argument("--nt-source", type=Path, default=DEFAULT_NT)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--diagnostics", type=Path, default=DEFAULT_DIAGNOSTICS)
    parser.add_argument("--max-refs-per-rendering", type=int, default=10)
    parser.add_argument("--max-other-rendering-refs", type=int, default=4)
    args = parser.parse_args()

    verses = load_source_rows(args.ot_source, "ot") + load_source_rows(args.nt_source, "nt")
    if args.profile == "broad":
        terms = list(BROAD_TERMS)
        if args.output_md == DEFAULT_OUTPUT:
            args.output_md = BROAD_OUTPUT
        if args.diagnostics == DEFAULT_DIAGNOSTICS:
            args.diagnostics = BROAD_DIAGNOSTICS
        markdown, diagnostics = build_broad_concordance(
            terms,
            verses,
            max_refs_per_rendering=args.max_refs_per_rendering,
            max_other_rendering_refs=args.max_other_rendering_refs,
        )
        diagnostics["terms_in_table"] = len(terms)
        diagnostics["terms_included"] = len(terms)
    else:
        configured_terms, included_terms = count_configured_terms(args.terms)
        terms = load_terms(args.terms)
        markdown, diagnostics = build_concordance(terms, verses)
        diagnostics["terms_configured"] = configured_terms
        diagnostics["terms_in_table"] = configured_terms
        diagnostics["terms_included"] = included_terms

    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.diagnostics.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.write_text(markdown, encoding="utf-8")
    args.diagnostics.write_text(json.dumps(diagnostics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(diagnostics, ensure_ascii=False))


if __name__ == "__main__":
    main()
