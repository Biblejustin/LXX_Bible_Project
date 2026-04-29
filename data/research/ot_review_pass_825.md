# OT Review Pass 825

Scope: Amos 8:11-14.

Changes:
- Reviewed Amos 8:11-14: kept the famine/thirst genitive phrasing, preserved the waters-to-sea wording, rendered doubled negatives as certainty, supplied articles for the fair virgins/young men and Samaria propitiation phrases, and marked Dan and Beersheba as vocatives.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Amos 8:11-14'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint passed at the Amos 8 boundary.
