# OT Review Pass 443

Scope: Jeremiah 49 remnant asks Jeremiah about Egypt and receives warning.

Changes:
- Reviewed the remnant's oath to obey, the Lord's promise if they remain in the land, and the sword/famine warning if they enter Egypt.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Jeremiah 49:1-22'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint intentionally deferred for batch boundary.
