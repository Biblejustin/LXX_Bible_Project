#!/usr/bin/env python3
import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

from build_idiom_consistency_review import FAMILIES
from build_crossref_clue_review import OPENBIBLE_BOOK_MAP, STANDARD_BOOK_NAMES, load_openbible_crossrefs, parse_openbible_ref


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RAW = DATA / "raw"
RESEARCH = DATA / "research"
DEFAULT_SOURCE = ROOT / "output" / "fresh_vs_brenton_ot_drafted.csv"
DEFAULT_OT_SOURCE = RAW / "lxx_greek" / "ot_full.csv"
DEFAULT_NT_IDIOMS = RESEARCH / "nt_idiom_parallels.csv"
DEFAULT_NT_ENGLISH_WITNESS = RESEARCH / "local" / "witness_review" / "nt_english_witness_observations.csv"
DEFAULT_ENGLISH_WITNESS = RESEARCH / "local" / "witness_review" / "english_witness_observations.csv"
DEFAULT_LOGOS_LOCAL = RESEARCH / "local" / "witness_review" / "logos_local_observations.csv"
DEFAULT_OUTPUT = ROOT / "output" / "fresh_vs_brenton_ot_priority_review.md"
DEFAULT_CSV = ROOT / "output" / "fresh_vs_brenton_ot_priority_review.csv"
DEFAULT_DIAGNOSTICS = ROOT / "output" / "fresh_vs_brenton_ot_priority_review_diagnostics.json"

IMPORTANCE_SCORE = {"none": 0, "low": 1, "medium": 2, "high": 4}
KEYWORD_RE = re.compile(
    r"\b("
    r"spirit|wind|soul|being|covenant|mercy|truth|righteous|righteousness|justice|law|altar|priest|"
    r"sacrifice|sin|forgive|salvation|savior|holy|holiness|lord|god|name|glory|king|anointed|"
    r"firstborn|shepherd|faith|grace|compassion|beloved|virgin|servant|messenger|angel|day one|"
    r"firm span|hades|abyss|seed|offspring|image|created|create|resurrection|repent|peace|judgment"
    r")\b",
    re.IGNORECASE,
)


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_by_ref(path: Path) -> dict[str, dict[str, str]]:
    return {row["ref"]: row for row in load_rows(path)}


def load_nt_parallels(path: Path) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in load_rows(path):
        grouped[row["family"]].append(row)
    return grouped


def load_nt_english_witness(path: Path) -> dict[tuple[str, str], dict[str, str]]:
    if not path.exists():
        return {}
    out: dict[tuple[str, str], dict[str, str]] = {}
    for row in load_rows(path):
        family = (row.get("family") or "").strip()
        nt_ref = (row.get("nt_ref") or "").strip()
        if family and nt_ref:
            out[(family, nt_ref)] = row
    return out


def load_english_witness(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    return {row["ref"]: row for row in load_rows(path) if row.get("ref")}


def load_logos_local(path: Path) -> dict[str, dict[str, list[dict[str, str]]]]:
    out = {"ref": defaultdict(list), "family": defaultdict(list)}
    if not path.exists():
        return out
    for row in load_rows(path):
        scope_type = (row.get("scope_type") or "").strip()
        scope_key = (row.get("scope_key") or "").strip()
        if scope_type in out and scope_key:
            out[scope_type][scope_key].append(row)
    return out


def family_map(source_by_ref: dict[str, dict[str, str]]) -> dict[str, set[str]]:
    mapped: dict[str, set[str]] = {}
    for ref, row in source_by_ref.items():
        greek = row.get("greek_text", "") or ""
        mapped[ref] = {family["name"] for family in FAMILIES if family["match"](greek)}
    return mapped


def nt_parallel_info(row: dict[str, str], source_by_ref: dict[str, dict[str, str]], nt_map: dict[str, list[dict[str, str]]]) -> tuple[int, list[str], list[str]]:
    source_row = source_by_ref.get(row["ref"])
    if not source_row:
        return 0, [], []
    greek = source_row.get("greek_text", "") or ""
    families = [family["name"] for family in FAMILIES if family["name"] in nt_map and family["match"](greek)]
    if not families:
        return 0, [], []
    refs: list[str] = []
    weights: list[int] = []
    for family_name in families:
        for nt_row in nt_map[family_name]:
            refs.append(nt_row["nt_ref"])
            weights.append(int(nt_row["weight"]))
    deduped_refs = list(dict.fromkeys(refs))
    return (max(weights) if weights else 0), families, deduped_refs


def crossref_info(
    row: dict[str, str],
    source_by_ref: dict[str, dict[str, str]],
    families_by_ref: dict[str, set[str]],
    crossrefs_by_ref: dict[str, list[dict[str, str]]],
) -> tuple[int, int, int, int]:
    top_vote = 0
    nt_count = 0
    shared_family_hits = 0
    targets = crossrefs_by_ref.get(row["ref"], [])
    source_families = families_by_ref.get(row["ref"], set())
    for target in targets:
        parsed = parse_openbible_ref(target["target_raw"])
        if not parsed:
            continue
        code, chapter, verse, _ = parsed
        votes = int(target["votes"])
        top_vote = max(top_vote, votes)
        if code not in source_by_ref and code in {
            "MAT", "MRK", "LUK", "JHN", "ACT", "ROM", "1CO", "2CO", "GAL", "EPH", "PHP",
            "COL", "1TH", "2TH", "1TI", "2TI", "TIT", "PHM", "HEB", "JAS", "1PE", "2PE",
            "1JN", "2JN", "3JN", "JUD", "REV",
        }:
            nt_count += 1
            continue
        target_ref = f"{STANDARD_BOOK_NAMES[code]} {chapter}:{verse}"
        target_families = families_by_ref.get(target_ref, set())
        if source_families and target_families and source_families & target_families:
            shared_family_hits += 1

    bonus = 0
    if top_vote >= 100:
        bonus += 3
    elif top_vote >= 50:
        bonus += 2
    elif top_vote >= 20:
        bonus += 1
    if nt_count:
        bonus += 1
    if shared_family_hits >= 2:
        bonus += 2
    elif shared_family_hits == 1:
        bonus += 1
    return bonus, top_vote, nt_count, shared_family_hits


def english_witness_info(row: dict[str, str], english_map: dict[str, dict[str, str]]) -> tuple[int, dict[str, str]]:
    witness_row = english_map.get(row["ref"])
    if not witness_row:
        return 0, {
            "english_witness_checked": "0",
            "english_witness_fresh_support": "0",
            "english_witness_brenton_support": "0",
            "english_witness_mt_support": "0",
            "english_witness_differs_all": "0",
            "english_witness_split_or_mixed": "0",
            "english_witness_signals": "",
            "english_witness_recommendation": "",
        }

    alignments = []
    for key in ("les_alignment", "nets_alignment", "saas_alignment"):
        value = (witness_row.get(key) or "").strip()
        if value and value != "not_checked":
            alignments.append(value)

    signals = []
    for key in ("les_signal", "nets_signal", "saas_signal"):
        value = (witness_row.get(key) or "").strip()
        if value and value != "no_issue":
            signals.append(value)

    checked = len(alignments)
    fresh_support = sum(1 for value in alignments if value == "agrees_fresh")
    brenton_support = sum(1 for value in alignments if value == "agrees_brenton")
    mt_support = sum(1 for value in alignments if value == "agrees_mt")
    differs_all = sum(1 for value in alignments if value == "differs_all")
    split_or_mixed = sum(1 for value in alignments if value == "split_or_mixed")
    recommendation = (witness_row.get("consensus_recommendation") or "").strip()

    bonus = 0
    if recommendation == "revise":
        bonus += 4
    elif recommendation == "needs_logos":
        bonus += 3
    elif recommendation == "defer":
        bonus += 2
    if checked and fresh_support == 0 and (brenton_support > 0 or mt_support > 0 or differs_all > 0):
        bonus += 2
    if differs_all:
        bonus += min(differs_all, 2)
    if split_or_mixed:
        bonus += 1
    if any(signal in {"textual_issue", "verse_map"} for signal in signals):
        bonus += 2
    elif signals:
        bonus += 1

    return bonus, {
        "english_witness_checked": str(checked),
        "english_witness_fresh_support": str(fresh_support),
        "english_witness_brenton_support": str(brenton_support),
        "english_witness_mt_support": str(mt_support),
        "english_witness_differs_all": str(differs_all),
        "english_witness_split_or_mixed": str(split_or_mixed),
        "english_witness_signals": ", ".join(sorted(dict.fromkeys(signals))),
        "english_witness_recommendation": recommendation,
    }


def nt_english_witness_info(
    families: list[str],
    nt_refs: list[str],
    nt_english_map: dict[tuple[str, str], dict[str, str]],
) -> tuple[int, dict[str, str]]:
    rows = [
        nt_english_map[(family, nt_ref)]
        for family in families
        for nt_ref in nt_refs
        if (family, nt_ref) in nt_english_map
    ]
    if not rows:
        return 0, {
            "nt_english_checked": "0",
            "nt_english_support_family": "0",
            "nt_english_softens_family": "0",
            "nt_english_mixed": "0",
            "nt_english_signals": "",
            "nt_english_recommendation": "",
        }

    alignments = []
    signals = []
    recommendations = []
    for witness_row in rows:
        for key in ("lsb_alignment", "esv_alignment", "kjv_alignment"):
            value = (witness_row.get(key) or "").strip()
            if value and value != "not_checked":
                alignments.append(value)
        for key in ("lsb_signal", "esv_signal", "kjv_signal"):
            value = (witness_row.get(key) or "").strip()
            if value and value != "no_issue":
                signals.append(value)
        recommendation = (witness_row.get("consensus_recommendation") or "").strip()
        if recommendation:
            recommendations.append(recommendation)

    checked = len(alignments)
    support_family = sum(1 for value in alignments if value == "supports_greek_family")
    softens_family = sum(1 for value in alignments if value == "softens_greek_family")
    mixed = sum(1 for value in alignments if value == "mixed")

    recommendation = ""
    for candidate in ("revise", "needs_logos", "defer", "keep"):
        if candidate in recommendations:
            recommendation = candidate
            break

    bonus = 0
    if recommendation == "revise":
        bonus += 3
    elif recommendation == "needs_logos":
        bonus += 2
    elif recommendation == "defer":
        bonus += 1
    if checked and support_family == 0 and (softens_family > 0 or mixed > 0):
        bonus += 1
    if mixed:
        bonus += 1
    if any(signal in {"smoothing", "unclear"} for signal in signals):
        bonus += 1

    return bonus, {
        "nt_english_checked": str(checked),
        "nt_english_support_family": str(support_family),
        "nt_english_softens_family": str(softens_family),
        "nt_english_mixed": str(mixed),
        "nt_english_signals": ", ".join(sorted(dict.fromkeys(signals))),
        "nt_english_recommendation": recommendation,
    }


def logos_local_info(
    row: dict[str, str],
    families_by_ref: dict[str, set[str]],
    logos_local_map: dict[str, dict[str, list[dict[str, str]]]],
) -> tuple[int, dict[str, str]]:
    matched = []
    matched.extend(logos_local_map["ref"].get(row["ref"], []))
    for family_name in families_by_ref.get(row["ref"], set()):
        matched.extend(logos_local_map["family"].get(family_name, []))
    if not matched:
        return 0, {
            "logos_local_checked": "0",
            "logos_local_scopes": "",
            "logos_local_source_tools": "",
            "logos_local_signals": "",
            "logos_local_supports": "",
            "logos_local_confidence": "",
            "logos_local_recommendation": "",
        }

    scopes = sorted({item.get("scope_key", "").strip() for item in matched if item.get("scope_key", "").strip()})
    source_tools = sorted({item.get("source_tools", "").strip() for item in matched if item.get("source_tools", "").strip()})
    signals = sorted({item.get("signal_type", "").strip() for item in matched if item.get("signal_type", "").strip()})
    supports = sorted({item.get("supports", "").strip() for item in matched if item.get("supports", "").strip()})
    recommendations = [item.get("recommendation", "").strip() for item in matched if item.get("recommendation", "").strip()]
    confidences = [item.get("confidence", "").strip() for item in matched if item.get("confidence", "").strip()]

    recommendation = ""
    for candidate in ("revise", "needs_logos", "defer", "keep"):
        if candidate in recommendations:
            recommendation = candidate
            break

    confidence = ""
    for candidate in ("high", "medium", "low"):
        if candidate in confidences:
            confidence = candidate
            break

    bonus = 0
    if recommendation == "revise":
        bonus += 3
    elif recommendation == "needs_logos":
        bonus += 2
    elif recommendation == "defer":
        bonus += 1
    if "unclear" in signals:
        bonus += 1

    return bonus, {
        "logos_local_checked": str(len(matched)),
        "logos_local_scopes": ", ".join(scopes),
        "logos_local_source_tools": " | ".join(source_tools),
        "logos_local_signals": ", ".join(signals),
        "logos_local_supports": ", ".join(supports),
        "logos_local_confidence": confidence,
        "logos_local_recommendation": recommendation,
    }


def consensus_recommendation(*recommendations: str) -> str:
    values = [(value or "").strip() for value in recommendations if (value or "").strip()]
    for candidate in ("revise", "needs_logos", "defer", "keep"):
        if candidate in values:
            return candidate
    return ""


def score_row(
    row: dict[str, str],
    source_by_ref: dict[str, dict[str, str]],
    nt_map: dict[str, list[dict[str, str]]],
    families_by_ref: dict[str, set[str]],
    crossrefs_by_ref: dict[str, list[dict[str, str]]],
    english_map: dict[str, dict[str, str]],
    nt_english_map: dict[tuple[str, str], dict[str, str]],
    logos_local_map: dict[str, dict[str, list[dict[str, str]]]],
) -> tuple[int, list[str], list[str], int, list[str], int, int, int, dict[str, str], dict[str, str], dict[str, str], str]:
    text = f"{row.get('fresh_translation', '')} {row.get('brenton_translation', '')}"
    keyword_hits = sorted({match.group(0).lower() for match in KEYWORD_RE.finditer(text)})
    decision_count = int(row.get("decision_count", "0") or "0")
    footnote_count = int(row.get("footnote_count", "0") or "0")
    importance = row.get("importance", "none")
    nt_weight, nt_families, nt_refs = nt_parallel_info(row, source_by_ref, nt_map)
    crossref_bonus, crossref_top_vote, crossref_nt_count, crossref_shared_family_hits = crossref_info(
        row, source_by_ref, families_by_ref, crossrefs_by_ref
    )
    english_bonus, english_meta = english_witness_info(row, english_map)
    nt_english_bonus, nt_english_meta = nt_english_witness_info(nt_families, nt_refs, nt_english_map)
    logos_local_bonus, logos_local_meta = logos_local_info(row, families_by_ref, logos_local_map)

    score = 0
    score += IMPORTANCE_SCORE.get(importance, 0)
    score += min(decision_count, 2) * 3
    score += min(footnote_count, 2) * 2
    score += len(keyword_hits) * 2
    score += nt_weight
    score += crossref_bonus
    score += english_bonus
    score += nt_english_bonus
    score += logos_local_bonus
    score += 0 if row.get("same_normalized", "") == "yes" else 1

    reasons: list[str] = []
    if decision_count:
        reasons.append(f"decisions={decision_count}")
    if footnote_count:
        reasons.append(f"footnotes={footnote_count}")
    if importance != "none":
        reasons.append(f"importance={importance}")
    if keyword_hits:
        reasons.append("keywords=" + ", ".join(keyword_hits[:6]))
    if nt_refs:
        reasons.append("nt=" + ", ".join(nt_refs[:4]))
    if crossref_top_vote:
        reasons.append(f"crossref_top_vote={crossref_top_vote}")
    if crossref_shared_family_hits:
        reasons.append(f"crossref_shared_family={crossref_shared_family_hits}")
    if english_meta["english_witness_checked"] != "0":
        reasons.append(
            "eng="
            + "/".join(
                [
                    f"fresh:{english_meta['english_witness_fresh_support']}",
                    f"brenton:{english_meta['english_witness_brenton_support']}",
                    f"mt:{english_meta['english_witness_mt_support']}",
                ]
            )
        )
    if english_meta["english_witness_recommendation"]:
        reasons.append(f"eng_reco={english_meta['english_witness_recommendation']}")
    if english_meta["english_witness_signals"]:
        reasons.append("eng_flags=" + english_meta["english_witness_signals"])
    if nt_english_meta["nt_english_checked"] != "0":
        reasons.append(
            "nt_eng="
            + "/".join(
                [
                    f"support:{nt_english_meta['nt_english_support_family']}",
                    f"soften:{nt_english_meta['nt_english_softens_family']}",
                    f"mixed:{nt_english_meta['nt_english_mixed']}",
                ]
            )
        )
    if nt_english_meta["nt_english_recommendation"]:
        reasons.append(f"nt_eng_reco={nt_english_meta['nt_english_recommendation']}")
    if nt_english_meta["nt_english_signals"]:
        reasons.append("nt_eng_flags=" + nt_english_meta["nt_english_signals"])
    if logos_local_meta["logos_local_checked"] != "0":
        reasons.append(f"logos={logos_local_meta['logos_local_checked']}")
    if logos_local_meta["logos_local_recommendation"]:
        reasons.append(f"logos_reco={logos_local_meta['logos_local_recommendation']}")
    if logos_local_meta["logos_local_signals"]:
        reasons.append("logos_flags=" + logos_local_meta["logos_local_signals"])
    if logos_local_meta["logos_local_supports"]:
        reasons.append("logos_support=" + logos_local_meta["logos_local_supports"])

    overall_recommendation = consensus_recommendation(
        english_meta.get("english_witness_recommendation", ""),
        nt_english_meta.get("nt_english_recommendation", ""),
        logos_local_meta.get("logos_local_recommendation", ""),
    )
    if overall_recommendation:
        reasons.append(f"reco={overall_recommendation}")

    return (
        score,
        keyword_hits,
        reasons,
        nt_weight,
        nt_refs,
        crossref_top_vote,
        crossref_nt_count,
        crossref_shared_family_hits,
        english_meta,
        nt_english_meta,
        logos_local_meta,
        overall_recommendation,
    )


def build_priority_rows(
    rows: list[dict[str, str]],
    per_book_limit: int,
    min_score: int,
    source_by_ref: dict[str, dict[str, str]],
    nt_map: dict[str, list[dict[str, str]]],
    families_by_ref: dict[str, set[str]],
    crossrefs_by_ref: dict[str, list[dict[str, str]]],
    english_map: dict[str, dict[str, str]],
    nt_english_map: dict[tuple[str, str], dict[str, str]],
    logos_local_map: dict[str, dict[str, list[dict[str, str]]]],
) -> list[dict[str, str]]:
    grouped: dict[str, list[tuple[int, int, dict[str, str], list[str], list[str]]]] = defaultdict(list)
    for index, row in enumerate(rows):
        (
            score,
            keyword_hits,
            reasons,
            nt_weight,
            nt_refs,
            crossref_top_vote,
            crossref_nt_count,
            crossref_shared_family_hits,
            english_meta,
            nt_english_meta,
            logos_local_meta,
            overall_recommendation,
        ) = score_row(
            row,
            source_by_ref,
            nt_map,
            families_by_ref,
            crossrefs_by_ref,
            english_map,
            nt_english_map,
            logos_local_map,
        )
        if score < min_score:
            continue
        enriched = dict(row)
        enriched["nt_parallel_weight"] = str(nt_weight)
        enriched["nt_parallel_count"] = str(len(nt_refs))
        enriched["nt_parallel_refs"] = ", ".join(nt_refs)
        enriched["crossref_top_vote"] = str(crossref_top_vote)
        enriched["crossref_nt_count"] = str(crossref_nt_count)
        enriched["crossref_shared_family_hits"] = str(crossref_shared_family_hits)
        enriched.update(english_meta)
        enriched.update(nt_english_meta)
        enriched.update(logos_local_meta)
        grouped[row["book_name"]].append((score, index, enriched, keyword_hits, reasons))

    selected: list[tuple[int, dict[str, str], list[str], list[str]]] = []
    for book_rows in grouped.values():
        ranked = sorted(book_rows, key=lambda item: (-item[0], item[1]))[:per_book_limit]
        selected.extend((item[1], item[2], item[3], item[4]) for item in ranked)

    selected.sort(key=lambda item: item[0])
    out_rows: list[dict[str, str]] = []
    for _, row, keyword_hits, reasons in selected:
        (
            score,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            english_meta,
            nt_english_meta,
            logos_local_meta,
            overall_recommendation,
        ) = score_row(
            row,
            source_by_ref,
            nt_map,
            families_by_ref,
            crossrefs_by_ref,
            english_map,
            nt_english_map,
            logos_local_map,
        )
        out_rows.append(
            {
                "ref": row["ref"],
                "book_name": row["book_name"],
                "chapter": row["chapter"],
                "verse": row["verse"],
                "importance": row["importance"],
                "priority_score": str(score),
                "decision_count": row["decision_count"],
                "footnote_count": row["footnote_count"],
                "nt_parallel_count": row.get("nt_parallel_count", "0"),
                "nt_parallel_weight": row.get("nt_parallel_weight", "0"),
                "nt_parallel_refs": row.get("nt_parallel_refs", ""),
                "crossref_top_vote": row.get("crossref_top_vote", "0"),
                "crossref_nt_count": row.get("crossref_nt_count", "0"),
                "crossref_shared_family_hits": row.get("crossref_shared_family_hits", "0"),
                "english_witness_checked": english_meta.get("english_witness_checked", "0"),
                "english_witness_fresh_support": english_meta.get("english_witness_fresh_support", "0"),
                "english_witness_brenton_support": english_meta.get("english_witness_brenton_support", "0"),
                "english_witness_mt_support": english_meta.get("english_witness_mt_support", "0"),
                "english_witness_differs_all": english_meta.get("english_witness_differs_all", "0"),
                "english_witness_split_or_mixed": english_meta.get("english_witness_split_or_mixed", "0"),
                "english_witness_signals": english_meta.get("english_witness_signals", ""),
                "english_witness_recommendation": english_meta.get("english_witness_recommendation", ""),
                "nt_english_checked": nt_english_meta.get("nt_english_checked", "0"),
                "nt_english_support_family": nt_english_meta.get("nt_english_support_family", "0"),
                "nt_english_softens_family": nt_english_meta.get("nt_english_softens_family", "0"),
                "nt_english_mixed": nt_english_meta.get("nt_english_mixed", "0"),
                "nt_english_signals": nt_english_meta.get("nt_english_signals", ""),
                "nt_english_recommendation": nt_english_meta.get("nt_english_recommendation", ""),
                "logos_local_checked": logos_local_meta.get("logos_local_checked", "0"),
                "logos_local_scopes": logos_local_meta.get("logos_local_scopes", ""),
                "logos_local_source_tools": logos_local_meta.get("logos_local_source_tools", ""),
                "logos_local_signals": logos_local_meta.get("logos_local_signals", ""),
                "logos_local_supports": logos_local_meta.get("logos_local_supports", ""),
                "logos_local_confidence": logos_local_meta.get("logos_local_confidence", ""),
                "logos_local_recommendation": logos_local_meta.get("logos_local_recommendation", ""),
                "consensus_recommendation": overall_recommendation,
                "keyword_hits": ", ".join(keyword_hits),
                "reasons": "; ".join(reasons),
                "fresh_translation": row["fresh_translation"],
                "brenton_translation": row["brenton_translation"],
            }
        )
    return out_rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_markdown(rows: list[dict[str, str]], per_book_limit: int, min_score: int) -> str:
    by_book: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_book[row["book_name"]].append(row)

    lines = [
        "# OT Priority Difference Review",
        "",
        f"Per-book limit: {per_book_limit}",
        f"Minimum score: {min_score}",
        f"Selected verses: {len(rows)}",
        "",
        "Use:",
        "- review verses most likely to matter for theology or core language choices",
        "- not exhaustive",
        "",
        "## By Book",
    ]
    for book, book_rows in by_book.items():
        lines.append(f"- {book}: {len(book_rows)}")

    for book, book_rows in by_book.items():
        lines.append("")
        lines.append(f"## {book}")
        for row in book_rows:
            lines.append("")
            lines.append(f"### {row['ref']}")
            lines.append(f"- score: {row['priority_score']}")
            lines.append(f"- reasons: {row['reasons']}")
            if row.get("nt_parallel_refs"):
                lines.append(f"- nt refs: {row['nt_parallel_refs']}")
            if row.get("nt_english_checked") not in {"", "0"}:
                lines.append(
                    "- nt english witnesses: "
                    f"checked {row['nt_english_checked']}, "
                    f"support {row.get('nt_english_support_family', '0')}, "
                    f"soften {row.get('nt_english_softens_family', '0')}, "
                    f"mixed {row.get('nt_english_mixed', '0')}"
                )
            if row.get("nt_english_recommendation"):
                lines.append(f"- nt english recommendation: {row['nt_english_recommendation']}")
            if row.get("nt_english_signals"):
                lines.append(f"- nt english signals: {row['nt_english_signals']}")
            if row.get("logos_local_checked") not in {"", "0"}:
                lines.append(
                    "- logos local: "
                    f"checked {row['logos_local_checked']}, "
                    f"supports {row.get('logos_local_supports', '[none]') or '[none]'}, "
                    f"confidence {row.get('logos_local_confidence', 'none') or 'none'}"
                )
            if row.get("logos_local_recommendation"):
                lines.append(f"- logos local recommendation: {row['logos_local_recommendation']}")
            if row.get("logos_local_signals"):
                lines.append(f"- logos local signals: {row['logos_local_signals']}")
            if row.get("crossref_top_vote") not in {"", "0"}:
                lines.append(f"- crossref top vote: {row['crossref_top_vote']}")
            if row.get("crossref_shared_family_hits") not in {"", "0"}:
                lines.append(f"- crossref shared-family hits: {row['crossref_shared_family_hits']}")
            if row.get("english_witness_checked") not in {"", "0"}:
                lines.append(
                    "- english witnesses: "
                    f"checked {row['english_witness_checked']}, "
                    f"fresh {row.get('english_witness_fresh_support', '0')}, "
                    f"brenton {row.get('english_witness_brenton_support', '0')}, "
                    f"mt {row.get('english_witness_mt_support', '0')}, "
                    f"differs all {row.get('english_witness_differs_all', '0')}"
                )
            if row.get("english_witness_recommendation"):
                lines.append(f"- english witness recommendation: {row['english_witness_recommendation']}")
            if row.get("english_witness_signals"):
                lines.append(f"- english witness signals: {row['english_witness_signals']}")
            lines.append(f"- fresh: {row['fresh_translation']}")
            lines.append(f"- brenton: {row['brenton_translation'] or '[missing]'}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--ot-source", default=str(DEFAULT_OT_SOURCE))
    parser.add_argument("--nt-idioms", default=str(DEFAULT_NT_IDIOMS))
    parser.add_argument("--nt-english-witness", default=str(DEFAULT_NT_ENGLISH_WITNESS))
    parser.add_argument("--english-witness", default=str(DEFAULT_ENGLISH_WITNESS))
    parser.add_argument("--logos-local", default=str(DEFAULT_LOGOS_LOCAL))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--csv-output", default=str(DEFAULT_CSV))
    parser.add_argument("--diagnostics", default=str(DEFAULT_DIAGNOSTICS))
    parser.add_argument("--per-book-limit", type=int, default=6)
    parser.add_argument("--min-score", type=int, default=4)
    args = parser.parse_args()

    source_rows = load_rows(Path(args.source))
    source_by_ref = load_by_ref(Path(args.ot_source))
    nt_map = load_nt_parallels(Path(args.nt_idioms))
    nt_english_map = load_nt_english_witness(Path(args.nt_english_witness))
    english_map = load_english_witness(Path(args.english_witness))
    logos_local_map = load_logos_local(Path(args.logos_local))
    families_by_ref = family_map(source_by_ref)
    crossrefs_by_ref = load_openbible_crossrefs()
    priority_rows = build_priority_rows(
        source_rows,
        args.per_book_limit,
        args.min_score,
        source_by_ref,
        nt_map,
        families_by_ref,
        crossrefs_by_ref,
        english_map,
        nt_english_map,
        logos_local_map,
    )
    if not priority_rows:
        raise SystemExit("No priority rows selected.")

    output_path = Path(args.output)
    csv_path = Path(args.csv_output)
    diagnostics_path = Path(args.diagnostics)

    output_path.write_text(build_markdown(priority_rows, args.per_book_limit, args.min_score), encoding="utf-8")
    write_csv(csv_path, priority_rows)
    diagnostics_path.write_text(
        json.dumps(
            {
                "source": str(Path(args.source)),
                "selected_rows": len(priority_rows),
                "per_book_limit": args.per_book_limit,
                "min_score": args.min_score,
                "rows_with_nt_parallels": sum(1 for row in priority_rows if row.get("nt_parallel_count") not in {"", "0"}),
                "rows_with_nt_english_signal": sum(
                    1 for row in priority_rows if row.get("nt_english_checked") not in {"", "0"}
                ),
                "rows_with_crossref_signal": sum(
                    1
                    for row in priority_rows
                    if row.get("crossref_top_vote") not in {"", "0"} or row.get("crossref_shared_family_hits") not in {"", "0"}
                ),
                "rows_with_english_witness_signal": sum(
                    1 for row in priority_rows if row.get("english_witness_checked") not in {"", "0"}
                ),
                "rows_with_logos_local_signal": sum(
                    1 for row in priority_rows if row.get("logos_local_checked") not in {"", "0"}
                ),
                "books": sorted({row["book_name"] for row in priority_rows}),
                "output": str(output_path),
                "csv_output": str(csv_path),
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": str(output_path),
                "csv_output": str(csv_path),
                "diagnostics": str(diagnostics_path),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
