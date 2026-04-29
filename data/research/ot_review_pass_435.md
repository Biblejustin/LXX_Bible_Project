# OT Review Pass 435

Scope: Jeremiah 41 release covenant judgment oracle.

Changes:
- Reviewed release-covenant reversal wording, Zedekiah death oracle, calf-ritual phrase, and Babylonian force clause.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Jeremiah 41:1-22'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint intentionally deferred for batch boundary.
