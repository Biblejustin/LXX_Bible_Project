# OT Review Pass 670

Scope: Ezekiel 48:1.

Changes:
- Adjusted Ezekiel 48:1 Hamath-court wording to court of Hamath to avoid a spurious compound name note while retaining the Greek court term.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Ezekiel 48:1'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint intentionally deferred for batch boundary.
