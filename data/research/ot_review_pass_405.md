# OT Review Pass 405

Scope: Jeremiah 25.

Changes:
- Reviewed Jeremiah 25 Judah warning and Elam oracle, including article cleanup, Amon name standardization, seventy-year service language, family-from-north line, joy/bridegroom/bride/lamp removal, Elam bow/four-winds/outcasts judgment, and Zedekiah reign heading.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Jeremiah 25:1-20'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint intentionally deferred for batch boundary.
