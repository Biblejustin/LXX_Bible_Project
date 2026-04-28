# OT Review Pass 414

Scope: Jeremiah 30:17-33.

Changes:
- Reviewed Jeremiah 30 Ammon, Kedar/court, and Damascus oracles, including Milcom/Gad inheritance line, Rabbah/Heshbon/Ai judgment, Enakim plains, Kedar and sons of east, clipped-around-face phrase, court/sparrows desolation, Damascus/Hamath/Arpad shame, and Ben-Hadad fire line.
- Synced translation comparison footnotes and added data-driven smoke guards for reviewed verses.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Jeremiah 30:17-21,Jeremiah 30:23-33'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint intentionally deferred for batch boundary.
