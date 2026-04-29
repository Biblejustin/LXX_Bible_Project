# OT Review Pass 876

Scope: Habakkuk 1:6-11.

Changes:
- Reviewed Habakkuk 1:6-11: supplied Chaldeans/breadths/wolves/spirit articles, rendered tent-dwellings and mound directly, kept hyper as beyond, and changed like-comparisons to as-comparisons where Greek uses hos.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Habakkuk 1:6-11'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint intentionally deferred for chapter boundary.
