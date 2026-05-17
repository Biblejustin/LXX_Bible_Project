# OT Review Pass 946

Scope: Joshua 6:10-11.

Changes:
- Tightened Joshua shout instruction wording and replaced ark slept phrasing with lodged while preserving the Septuagint construction.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python scripts/run_fast_review_checkpoint.py --testament ot --refs 'Joshua 6:10-11'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint intentionally deferred for batch boundary.
