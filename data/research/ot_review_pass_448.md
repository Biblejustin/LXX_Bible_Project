# OT Review Pass 448

Scope: Jeremiah 52:1,4-14 fall of Jerusalem and Zedekiah's capture.

Changes:
- Reviewed Zedekiah's reign notice, siege dates, city breach, Riblah judgment, Zedekiah's mill-house confinement, and Nebuzaradan's burning of Jerusalem.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Jeremiah 52:1,Jeremiah 52:4-14'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint intentionally deferred for batch boundary.
