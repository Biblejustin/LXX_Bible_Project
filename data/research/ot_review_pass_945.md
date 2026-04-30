# OT Review Pass 945

Scope: Joshua 19:38 CSV field repair.

Changes:
- Restored full Joshua 19:38 LXX name list and quoted comma-bearing support rows.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Joshua 19:38'` passed.
- Focused smoke tests passed.
- `make checkpoint-ot PYTHON=python` passed after the scoped repair.
