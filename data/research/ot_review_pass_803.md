# OT Review Pass 803

Scope: Amos 1:1-5.

Changes:
- Reviewed Amos 1:1-5: kept the LXX Nakkarim/Jerusalem heading, supplied articles in the Zion/Carmel line, retained the Damascus sawed-pregnant-women variant, supplied foundations of Ben-hadad, bars of Damascus, inhabitants from the plain of On, and a tribe from the men of Haran.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Amos 1:1-5'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint passed at the Amos 1 boundary.
