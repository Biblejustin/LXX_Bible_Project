# OT Review Pass 804

Scope: Amos 1:6-10.

Changes:
- Reviewed Amos 1:6-10: supplied the captivity of Solomon, inhabitants from Ashdod, a tribe from Ashkelon, the remnant of the foreigners, the captivity of Solomon into Edom, and the covenant of brothers while keeping standard Edom/Ashdod/Ashkelon/Ekron names.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Amos 1:6-10'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint passed at the Amos 1 boundary.
