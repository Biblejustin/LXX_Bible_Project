#!/usr/bin/env python3
"""Sync OT support tables to current OT draft wording.

Keeps verse-level OT decision/footnote text aligned with current source draft and
strips raw Logos BibleKnowledgebase markup from support tables.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OT_SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
DECISIONS = ROOT / "data" / "research" / "translation_decisions.csv"
FOOTNOTES = ROOT / "data" / "research" / "translation_footnotes.csv"
CONTEXTUAL_NAME_DECISIONS = ROOT / "data" / "research" / "contextual_proper_name_decisions.csv"

LOGOS_LINK_RE = re.compile(r"\[\[([^>\]]+?)\s*>>\s*BibleKnowledgebase@[^]]+\]\]")
APPLYABLE_NAME_STATUSES = {"apply", "revise-main-text", "done"}

csv.field_size_limit(sys.maxsize)


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def strip_logos_links(text: str) -> str:
    return LOGOS_LINK_RE.sub(lambda match: match.group(1).strip(), text or "")


def replace_token(text: str, current_form: str, preferred_form: str) -> tuple[str, int]:
    pattern = re.compile(rf"\b{re.escape(current_form)}\b")
    return pattern.subn(preferred_form, text)


def apply_contextual_name_replacements(
    text: str,
    ref: str,
    decisions_by_ref: dict[str, list[dict[str, str]]],
) -> tuple[str, int]:
    updated = text or ""
    replacements = 0
    for row in decisions_by_ref.get(ref, []):
        match_text = (row.get("match_text") or "").strip()
        replacement_text = (row.get("replacement_text") or "").strip()
        current_form = (row.get("current_form") or "").strip()
        preferred_form = (row.get("preferred_form") or "").strip()
        if match_text and replacement_text:
            count = updated.count(match_text)
            if count:
                updated = updated.replace(match_text, replacement_text)
                replacements += count
                continue
        if not current_form or not preferred_form:
            continue
        updated, count = replace_token(updated, current_form, preferred_form)
        replacements += count
    return updated, replacements


def main() -> None:
    ot_rows = load_csv(OT_SOURCE)
    decisions = load_csv(DECISIONS)
    footnotes = load_csv(FOOTNOTES)
    contextual_name_rows = load_csv(CONTEXTUAL_NAME_DECISIONS)

    ot_by_ref = {row["ref"]: row.get("draft_translation", "") for row in ot_rows if row.get("ref")}
    contextual_by_ref: dict[str, list[dict[str, str]]] = {}
    for row in contextual_name_rows:
        status = (row.get("status") or "").strip().lower()
        ref = (row.get("ref") or "").strip()
        if status not in APPLYABLE_NAME_STATUSES or not ref:
            continue
        contextual_by_ref.setdefault(ref, []).append(row)

    decision_updates = 0
    decision_link_cleans = 0
    decision_name_updates = 0
    for row in decisions:
        ref = row.get("ref", "")
        chosen = row.get("chosen_rendering", "")
        alternate = row.get("alternate_renderings", "")
        rationale = row.get("rationale", "")
        cleaned_chosen = strip_logos_links(chosen)
        cleaned_alternate = strip_logos_links(alternate)
        cleaned_rationale = strip_logos_links(rationale)
        if cleaned_chosen != chosen:
            row["chosen_rendering"] = cleaned_chosen
            decision_link_cleans += 1
        if cleaned_alternate != alternate:
            row["alternate_renderings"] = cleaned_alternate
            decision_link_cleans += 1
        if cleaned_rationale != rationale:
            row["rationale"] = cleaned_rationale
            decision_link_cleans += 1
        if ref not in ot_by_ref:
            continue
        lemma = (row.get("lemma") or "").strip().lower()
        if lemma not in {"verse-level variant", "verse-level translation difference"}:
            desired = row.get("chosen_rendering", "")
        else:
            desired = ot_by_ref[ref]
            if desired and row.get("chosen_rendering", "") != desired:
                row["chosen_rendering"] = desired
                chosen = desired
                decision_updates += 1
        if ref in contextual_by_ref and row.get("chosen_rendering", ""):
            updated, count = apply_contextual_name_replacements(
                row.get("chosen_rendering", ""),
                ref,
                contextual_by_ref,
            )
            if count and updated != row.get("chosen_rendering", ""):
                row["chosen_rendering"] = updated
                decision_name_updates += 1
        if ref in contextual_by_ref and row.get("alternate_renderings", ""):
            updated, count = apply_contextual_name_replacements(
                row.get("alternate_renderings", ""),
                ref,
                contextual_by_ref,
            )
            if count and updated != row.get("alternate_renderings", ""):
                row["alternate_renderings"] = updated
                decision_name_updates += 1

    footnote_updates = 0
    footnote_link_cleans = 0
    footnote_name_updates = 0
    for row in footnotes:
        ref = row.get("ref", "")
        trigger = row.get("trigger_phrase", "")
        footnote = row.get("footnote_text", "")
        cleaned_trigger = strip_logos_links(trigger)
        cleaned_footnote = strip_logos_links(footnote)
        if cleaned_trigger != trigger:
            row["trigger_phrase"] = cleaned_trigger
            footnote_link_cleans += 1
        if cleaned_footnote != footnote:
            row["footnote_text"] = cleaned_footnote
            footnote_link_cleans += 1
        if ref not in ot_by_ref:
            continue
        source_basis = (row.get("source_basis") or "").strip().lower()
        if "variant" not in source_basis:
            desired = row.get("trigger_phrase", "")
        else:
            desired = ot_by_ref[ref]
            if desired and row.get("trigger_phrase", "") != desired:
                row["trigger_phrase"] = desired
                trigger = desired
                footnote_updates += 1
        if ref in contextual_by_ref and row.get("trigger_phrase", ""):
            updated, count = apply_contextual_name_replacements(
                row.get("trigger_phrase", ""),
                ref,
                contextual_by_ref,
            )
            if count and updated != row.get("trigger_phrase", ""):
                row["trigger_phrase"] = updated
                footnote_name_updates += 1
        if ref in contextual_by_ref and row.get("footnote_text", ""):
            updated, count = apply_contextual_name_replacements(
                row.get("footnote_text", ""),
                ref,
                contextual_by_ref,
            )
            if count and updated != row.get("footnote_text", ""):
                row["footnote_text"] = updated
                footnote_name_updates += 1

    write_csv(DECISIONS, decisions)
    write_csv(FOOTNOTES, footnotes)

    print(
        {
            "decision_updates": decision_updates,
            "decision_link_cleans": decision_link_cleans,
            "decision_name_updates": decision_name_updates,
            "footnote_updates": footnote_updates,
            "footnote_link_cleans": footnote_link_cleans,
            "footnote_name_updates": footnote_name_updates,
        }
    )


if __name__ == "__main__":
    main()
