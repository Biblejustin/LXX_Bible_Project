#!/usr/bin/env python3
import csv
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
PROPER_NAMES = ROOT / "data" / "proper_names.csv"
LOGOS_ALL = ROOT / "data" / "research" / "local" / "logos_scan" / "logos_resources_all.csv"
LOCAL_DIR = ROOT / "data" / "research" / "local" / "proper_name_review"
OUT_PRIVATE_CSV = LOCAL_DIR / "proper_name_candidates.csv"
OUT_PRIVATE_README = LOCAL_DIR / "README.md"
OUT_MD = ROOT / "output" / "fresh_ot_proper_name_watch.md"
OUT_CSV = ROOT / "output" / "fresh_ot_proper_name_watch.csv"
OUT_DIAGNOSTICS = ROOT / "output" / "fresh_ot_proper_name_watch_diagnostics.json"

TOKEN_RE = re.compile(r"\b[A-ZĀĒĪŌŪ][A-Za-zĀĒĪŌŪāēīōū'-]+\b")

# Seed list only. Review can expand this.
NAME_MAP = {
    "Ierousalem": {"preferred": "Jerusalem", "kind": "place"},
    "Iouda": {"preferred": "Judah", "kind": "people/place"},
    "Dauid": {"preferred": "David", "kind": "person"},
    "Saoul": {"preferred": "Saul", "kind": "person"},
    "Salomon": {"preferred": "Solomon", "kind": "person"},
    "Roboam": {"preferred": "Rehoboam", "kind": "person"},
    "Ieroboam": {"preferred": "Jeroboam", "kind": "person"},
    "Ioab": {"preferred": "Joab", "kind": "person"},
    "Achaab": {"preferred": "Ahab", "kind": "person"},
    "Achab": {"preferred": "Ahab", "kind": "person"},
    "Achaz": {"preferred": "Ahaz", "kind": "person"},
    "Ezekias": {"preferred": "Hezekiah", "kind": "person"},
    "Elisaie": {"preferred": "Elisha", "kind": "person"},
    "Esaias": {"preferred": "Isaiah", "kind": "person"},
    "Nabouchodonosor": {"preferred": "Nebuchadnezzar", "kind": "person"},
    "Pharao": {"preferred": "Pharaoh", "kind": "title/name"},
    "Noomma": {"preferred": "Naamah", "kind": "person"},
    "Iericho": {"preferred": "Jericho", "kind": "place"},
    "Iesse": {"preferred": "Jesse", "kind": "person"},
    "Iotham": {"preferred": "Jotham", "kind": "person"},
    "Ioel": {"preferred": "Joel", "kind": "person"},
    "Osee": {"preferred": "Hosea", "kind": "person"},
    "Abessalom": {"preferred": "Absalom", "kind": "person"},
    "Azael": {"preferred": "Hazael", "kind": "person"},
    "Ozias": {"preferred": "Uzziah", "kind": "person"},
    "Amasias": {"preferred": "Amaziah", "kind": "person"},
    "Joatham": {"preferred": "Jotham", "kind": "person"},
    # Common macronized variants produced by the draft pass.
    "Samouēl": {"preferred": "Samuel", "kind": "person"},
    "Iōnathan": {"preferred": "Jonathan", "kind": "person"},
    "Abessalōm": {"preferred": "Absalom", "kind": "person"},
    "Iōab": {"preferred": "Joab", "kind": "person"},
    "Iōb": {"preferred": "Job", "kind": "person"},
    "Abennēr": {"preferred": "Abner", "kind": "person"},
    "Iōsaphat": {"preferred": "Jehoshaphat", "kind": "person"},
    "Sampsōn": {"preferred": "Samson", "kind": "person"},
    "Iōsias": {"preferred": "Josiah", "kind": "person"},
    "Chebrōn": {"preferred": "Hebron", "kind": "place"},
    "Amnōn": {"preferred": "Amnon", "kind": "person"},
    "Baithēl": {"preferred": "Bethel", "kind": "place"},
    "Manassēs": {"preferred": "Manasseh", "kind": "person"},
    "Ierousalēm": {"preferred": "Jerusalem", "kind": "place"},
    "Manōe": {"preferred": "Manoah", "kind": "person"},
    "Amalēk": {"preferred": "Amalek", "kind": "people/place"},
    "Nēr": {"preferred": "Ner", "kind": "person"},
    "Thēmar": {"preferred": "Tamar", "kind": "person"},
    "Oziēl": {"preferred": "Uzziel", "kind": "person"},
    "Iōatham": {"preferred": "Jotham", "kind": "person"},
    "Asaēl": {"preferred": "Asahel", "kind": "person"},
    "Debbōra": {"preferred": "Deborah", "kind": "person"},
    "Zēbee": {"preferred": "Zebah", "kind": "person"},
    "Massēpha": {"preferred": "Mizpah", "kind": "place"},
    "Massēphath": {"preferred": "Mizpah", "kind": "place"},
    "Iezraēlite": {"preferred": "Jezreelite", "kind": "people/place"},
    "Salōmōn": {"preferred": "Solomon", "kind": "person"},
    "Aōd": {"preferred": "Ehud", "kind": "person"},
    "Amōn": {"preferred": "Amon", "kind": "person"},
    "Mōab": {"preferred": "Moab", "kind": "people/place"},
    "Sennachērim": {"preferred": "Sennacherib", "kind": "person"},
    "Babylōn": {"preferred": "Babylon", "kind": "place"},
    "Shilōm": {"preferred": "Shiloh", "kind": "place"},
    "Manaēm": {"preferred": "Menahem", "kind": "person"},
    "Rapsakēs": {"preferred": "Rabshakeh", "kind": "title/name"},
    "Ioēl": {"preferred": "Joel", "kind": "person"},
    "Gabaōn": {"preferred": "Gibeon", "kind": "place"},
    "Ierichō": {"preferred": "Jericho", "kind": "place"},
    "Saddōk": {"preferred": "Zadok", "kind": "person"},
    "Ramōth": {"preferred": "Ramoth", "kind": "place"},
    "Jaēl": {"preferred": "Jael", "kind": "person"},
    "Bēthleem": {"preferred": "Bethlehem", "kind": "place"},
    "Iakōb": {"preferred": "Jacob", "kind": "person"},
    "Achitōb": {"preferred": "Ahitub", "kind": "person"},
    "Karmēl": {"preferred": "Carmel", "kind": "place"},
    "Ismaēl": {"preferred": "Ishmael", "kind": "person"},
    "Eliēl": {"preferred": "Eliel", "kind": "person"},
    "Sēir": {"preferred": "Seir", "kind": "place"},
    "Michaēl": {"preferred": "Michael", "kind": "person"},
    "Nathanaēl": {"preferred": "Nathanael", "kind": "person"},
    "Iōsēph": {"preferred": "Joseph", "kind": "person"},
    "Mōusēs": {"preferred": "Moses", "kind": "person"},
    "Aarōn": {"preferred": "Aaron", "kind": "person"},
    "Siōn": {"preferred": "Zion", "kind": "place"},
    "Edōm": {"preferred": "Edom", "kind": "people/place"},
    "Amōs": {"preferred": "Amoz", "kind": "person"},
}

CONTEXT_DEPENDENT_NAME_FORMS = {
    "Kedrōn": {
        "kind": "place",
        "note": "Context-dependent: usually Kidron in Jerusalem-wadi contexts, but Kitron at Judges 1:30.",
    },
    "Iōas": {
        "kind": "person",
        "note": "Context-dependent: Joash and Jehoash vary by king/person context.",
    },
    "Jōas": {
        "kind": "person",
        "note": "Context-dependent: Joash and Jehoash vary by king/person context.",
    },
    "Iōram": {
        "kind": "person",
        "note": "Context-dependent: Joram and Jehoram vary by king/person context.",
    },
    "Iōdae": {
        "kind": "person",
        "note": "Context-dependent: often Jehoiada, but Jedaiah in some priest-list contexts.",
    },
    "Sokchōth": {
        "kind": "place",
        "note": "Context-dependent: Succoth in Judges 8, but Socoh/Socchoh in 1 Samuel 17.",
    },
    "Bērsabee": {
        "kind": "place/person",
        "note": "Context-dependent: Beersheba as place, Bathsheba as person in David/Solomon contexts.",
    },
    "Iōanan": {
        "kind": "person",
        "note": "Context-dependent: Johanan and Jehohanan vary by person context.",
    },
    "Iōakim": {
        "kind": "person",
        "note": "Context-dependent: Jehoiakim as king, Joiakim in Nehemiah priestly contexts.",
    },
    "Iiēl": {
        "kind": "person",
        "note": "Context-dependent: Jeiel, Jeuel, or Jehiel by genealogy context.",
    },
}

RESOURCE_HINTS = [
    "LLS:EXDCTBIBNM",
    "LLS:HITCHCOCK01",
    "LLS:9781607426288",
    "LLS:9781628364507",
    "LLS:ANCPLCNAMES",
    "LLS:CARTAONOMASTICON",
]


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def load_name_meanings(path: Path) -> dict[str, dict[str, str]]:
    out = {}
    for row in load_csv(path):
        name = (row.get("name") or "").strip()
        if name:
            out[name] = row
    return out


def resource_labels(path: Path) -> list[str]:
    by_id = {row.get("resource_id", ""): row for row in load_csv(path)}
    labels = []
    for rid in RESOURCE_HINTS:
        row = by_id.get(rid)
        if not row:
            continue
        title = row.get("title") or row.get("short_title") or rid
        labels.append(f"{title} [{rid}]")
    return labels


def gather_name_hits(name_map: dict[str, dict[str, str]]) -> dict[str, dict[str, object]]:
    hits: dict[str, dict[str, object]] = {}
    for current_form, meta in name_map.items():
        hits[current_form] = {
            "preferred": meta.get("preferred", ""),
            "kind": meta["kind"],
            "note": meta.get("note", ""),
            "count": 0,
            "sample_refs": [],
        }

    for row in load_csv(RAW):
        ref = row.get("ref", "")
        text = row.get("draft_translation", "")
        tokens = TOKEN_RE.findall(text)
        seen_this_ref = set()
        for token in tokens:
            if token not in hits:
                continue
            hits[token]["count"] += 1
            if token not in seen_this_ref and len(hits[token]["sample_refs"]) < 8:
                hits[token]["sample_refs"].append(ref)
                seen_this_ref.add(token)
    return hits


def main() -> None:
    prior_rows = {row["current_form"]: row for row in load_csv(OUT_PRIVATE_CSV) if row.get("current_form")}
    meanings = load_name_meanings(PROPER_NAMES)
    resources = resource_labels(LOGOS_ALL)
    hits = gather_name_hits(NAME_MAP)
    context_hits = gather_name_hits(CONTEXT_DEPENDENT_NAME_FORMS)

    public_rows = []
    private_rows = []
    context_rows = []
    for current_form, data in sorted(hits.items(), key=lambda item: (-int(item[1]["count"]), item[0])):
        count = int(data["count"])
        if count == 0:
            continue
        preferred = str(data["preferred"])
        meaning_row = meanings.get(preferred, {})
        prior = prior_rows.get(current_form, {})
        sample_refs = ", ".join(data["sample_refs"])
        public_rows.append(
            {
                "current_form": current_form,
                "preferred_form": preferred,
                "kind": str(data["kind"]),
                "occurrences": str(count),
                "sample_refs": sample_refs,
                "meaning": meaning_row.get("meaning", ""),
                "status": prior.get("status", ""),
            }
        )
        private_rows.append(
            {
                "current_form": current_form,
                "preferred_form": prior.get("preferred_form", preferred),
                "kind": str(data["kind"]),
                "occurrences": str(count),
                "sample_refs": sample_refs,
                "meaning": meaning_row.get("meaning", ""),
                "footnote": meaning_row.get("footnote", ""),
                "resource_1": resources[0] if len(resources) > 0 else "",
                "resource_2": resources[1] if len(resources) > 1 else "",
                "resource_3": resources[2] if len(resources) > 2 else "",
                "status": prior.get("status", ""),
                "notes": prior.get("notes", ""),
            }
        )

    for current_form, data in sorted(context_hits.items(), key=lambda item: (-int(item[1]["count"]), item[0])):
        count = int(data["count"])
        if count == 0:
            continue
        context_rows.append(
            {
                "current_form": current_form,
                "kind": str(data["kind"]),
                "occurrences": str(count),
                "sample_refs": ", ".join(data["sample_refs"]),
                "note": str(data["note"]),
            }
        )

    write_csv(
        OUT_CSV,
        public_rows,
        ["current_form", "preferred_form", "kind", "occurrences", "sample_refs", "meaning", "status"],
    )
    write_csv(
        OUT_PRIVATE_CSV,
        private_rows,
        [
            "current_form",
            "preferred_form",
            "kind",
            "occurrences",
            "sample_refs",
            "meaning",
            "footnote",
            "resource_1",
            "resource_2",
            "resource_3",
            "status",
            "notes",
        ],
    )

    lines = [
        "# Fresh OT Proper Name Watch",
        "",
        f"Rows: {len(public_rows)}",
        "",
        "Default policy:",
        "- use familiar MT-based English name forms in main text when Greek is simply transliterating the same referent",
        "- do not force raw Greekized spellings into main text when English has a stable familiar biblical form",
        "- preserve name meaning in notes when that meaning matters contextually or the text plays on it",
        "",
    ]
    for row in public_rows:
        lines.extend(
            [
                f"## {row['current_form']} → {row['preferred_form']}",
                f"- kind: `{row['kind']}`",
                f"- occurrences: `{row['occurrences']}`",
                f"- sample refs: {row['sample_refs']}",
                f"- meaning: {row['meaning'] or '[none]'}",
                f"- status: `{row['status'] or 'open'}`",
                "",
            ]
        )
    lines.extend(
        [
            "## Context-Dependent Forms Excluded from Auto-Apply",
            "",
            "These forms remain visible for manual contextual review. They are intentionally not written to the private apply worksheet.",
            "",
        ]
    )
    if not context_rows:
        lines.extend(["[none]", ""])
    for row in context_rows:
        lines.extend(
            [
                f"### {row['current_form']}",
                f"- kind: `{row['kind']}`",
                f"- occurrences: `{row['occurrences']}`",
                f"- sample refs: {row['sample_refs']}",
                f"- note: {row['note']}",
                "",
            ]
        )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    OUT_PRIVATE_README.write_text(
        "\n".join(
            [
                "# Proper Name Review",
                "",
                "Private worksheet.",
                "Use Logos onomastic and place-name resources here.",
                "",
                "Policy target:",
                "1. Main text should normally use familiar MT-based English forms for shared biblical names.",
                "2. Keep raw Greekized spellings only if there is a strong textual/editorial reason.",
                "3. Preserve meaning-level significance in notes, not by forcing unusual spellings.",
                "",
                "Suggested statuses:",
                "- `open`",
                "- `keep-current`",
                "- `revise-main-text`",
                "- `needs-logos`",
                "- `done`",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    diagnostics = {
        "rows": len(public_rows),
        "top_rows": public_rows[:10],
        "context_dependent_rows": len(context_rows),
        "context_dependent_top_rows": context_rows[:10],
        "public_md": str(OUT_MD),
        "public_csv": str(OUT_CSV),
        "private_csv": str(OUT_PRIVATE_CSV),
    }
    OUT_DIAGNOSTICS.write_text(json.dumps(diagnostics, indent=2), encoding="utf-8")
    print(json.dumps(diagnostics, indent=2))


if __name__ == "__main__":
    main()
