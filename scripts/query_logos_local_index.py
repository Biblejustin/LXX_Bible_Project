#!/usr/bin/env python3
import argparse
import json
import sqlite3
import unicodedata
from pathlib import Path
from typing import Dict, List

from inspect_logos_local_state import DEFAULT_LOGOS_ROOT, choose_accounts, discover_accounts, read_only_connect


def fold_text(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    stripped = "".join(ch for ch in normalized if unicodedata.category(ch) != "Mn")
    return unicodedata.normalize("NFC", stripped).casefold()


def fetch_autocomplete_rows(db_path: Path, term: str, limit: int) -> List[Dict[str, str]]:
    query = """
    SELECT
        lw.FoldedText,
        l.LabelText,
        t.Reference,
        ik.IconKind,
        COALESCE(d.Description, '') AS Description
    FROM LabelWords lw
    JOIN Labels l ON l.LabelId = lw.LabelId
    JOIN Terms t ON t.TermId = l.TermId
    JOIN IconKinds ik ON ik.IconKindId = t.IconKindId
    LEFT JOIN Descriptions d ON d.TermId = t.TermId AND d.LanguageId = 1
    WHERE lw.FoldedText LIKE ? OR l.LabelText LIKE ? OR t.Reference LIKE ?
    ORDER BY
        CASE WHEN lw.FoldedText = ? THEN 0 ELSE 1 END,
        CASE WHEN l.LabelText = ? THEN 0 ELSE 1 END,
        lw.FoldedText,
        l.LabelText
    LIMIT ?
    """
    folded = fold_text(term)
    like_term = f"{folded}%"
    contains_term = f"%{term}%"
    with read_only_connect(db_path) as conn:
        rows = conn.execute(query, (like_term, contains_term, contains_term, folded, term, limit)).fetchall()
    out: List[Dict[str, str]] = []
    for folded_text, label_text, reference, icon_kind, description in rows:
        out.append(
            {
                "folded_text": folded_text,
                "label_text": label_text,
                "reference": reference,
                "icon_kind": icon_kind,
                "description": description,
            }
        )
    return out


def fetch_word_sense_rows(db_path: Path, term: str, limit: int) -> List[Dict[str, str]]:
    query = """
    SELECT
        l.LabelText,
        t.Reference
    FROM Labels l
    JOIN Terms t ON t.TermId = l.TermId
    JOIN IconKinds ik ON ik.IconKindId = t.IconKindId
    WHERE ik.IconKind = 'WordSense'
      AND (l.LabelText LIKE ? OR t.Reference LIKE ?)
    ORDER BY l.LabelText
    LIMIT ?
    """
    contains_term = f"%{term}%"
    with read_only_connect(db_path) as conn:
        rows = conn.execute(query, (contains_term, contains_term, limit)).fetchall()
    return [{"label_text": label_text, "reference": reference} for label_text, reference in rows]


def fetch_headword_rows(db_path: Path, term: str, limit: int) -> List[Dict[str, str]]:
    query = """
    SELECT
        hm.FoldedText,
        rv.ResourceId,
        rv.ResourceVersion
    FROM HeadwordMilestones hm
    JOIN ResourceVersions rv ON rv.ResourceVersionId = hm.ResourceVersionId
    WHERE hm.FoldedText LIKE ?
    ORDER BY hm.FoldedText, rv.ResourceId
    LIMIT ?
    """
    folded = fold_text(term)
    with read_only_connect(db_path) as conn:
        rows = conn.execute(query, (f"%{folded}%", limit)).fetchall()
    return [
        {"folded_text": folded_text, "resource_id": resource_id, "resource_version": resource_version}
        for folded_text, resource_id, resource_version in rows
    ]


def fetch_recent_history_rows(db_path: Path, term: str, limit: int) -> List[Dict[str, str]]:
    query = """
    SELECT Title, Subtitle, LastVisited, Bookmark
    FROM History
    WHERE IsDeleted = 0
      AND (Title LIKE ? OR Subtitle LIKE ? OR Bookmark LIKE ?)
    ORDER BY LastVisited DESC
    LIMIT ?
    """
    contains_term = f"%{term}%"
    with read_only_connect(db_path) as conn:
        rows = conn.execute(query, (contains_term, contains_term, contains_term, limit)).fetchall()
    return [
        {
            "title": title or "",
            "subtitle": subtitle or "",
            "last_visited": last_visited or "",
            "bookmark": bookmark or "",
        }
        for title, subtitle, last_visited, bookmark in rows
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Query usable local Logos indexes without touching encrypted payload files.")
    parser.add_argument("term")
    parser.add_argument("--logos-root", type=Path, default=DEFAULT_LOGOS_ROOT)
    parser.add_argument("--account")
    parser.add_argument("--limit", type=int, default=30)
    args = parser.parse_args()

    accounts = discover_accounts(args.logos_root)
    account = choose_accounts(accounts, args.account, all_accounts=False)[0]
    account_name = account["account"].name
    autocomplete_db = account["account"] / "AutoComplete" / "AutoComplete.db"
    milestones_db = account["account"] / "GlobalMilestoneIndex" / "milestones.db"

    result = {
        "account": account_name,
        "term": args.term,
        "autocomplete": fetch_autocomplete_rows(autocomplete_db, args.term, args.limit),
        "word_senses": fetch_word_sense_rows(autocomplete_db, args.term, args.limit),
        "headwords": fetch_headword_rows(milestones_db, args.term, args.limit),
        "recent_history": fetch_recent_history_rows(account["history_db"], args.term, args.limit),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
