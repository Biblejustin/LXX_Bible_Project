# OT Review Pass 837

Scope: Jonah 3:6-10.

Changes:
- Reviewed Jonah 3:6-10: supplied word/king articles, kept the proclamation wording, made sackcloths plural, clarified the injustice-in-hands phrase, rendered the anger/wrath pair directly, and supplied the article/relative clause in the evil-that-he-spoke line.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Jonah 3:6-10'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint intentionally deferred for chapter boundary.
