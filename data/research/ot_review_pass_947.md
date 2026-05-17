# OT Review Pass 947

Scope: Genesis 4:13.

Changes:
- Reworded Cain complaint to natural English while preserving the LXX forgiveness wording and added a compact MT/LXX lexical note.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python scripts/run_fast_review_checkpoint.py --testament ot --refs 'Genesis 4:13'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint intentionally deferred for batch boundary.
