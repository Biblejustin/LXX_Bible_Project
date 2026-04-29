# OT Review Pass 436

Scope: Jeremiah 42 Rechabite obedience oracle.

Changes:
- Reviewed Rechabite household wording, abstinence command, obedience contrast, and perpetuity promise.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Jeremiah 42:1-19'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint intentionally deferred for batch boundary.
