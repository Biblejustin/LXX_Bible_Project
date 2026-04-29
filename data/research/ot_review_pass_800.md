# OT Review Pass 800

Scope: Joel 4:6-10.

Changes:
- Reviewed Joel 4:6-10: supplied sons of the Greeks, from the place where you sold them, far distant nation, among the nations, rouse warriors, bring near and go up all men of war, and the weak one saying I am strong.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Joel 4:6-10'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint intentionally deferred for batch boundary.
