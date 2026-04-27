# OT Review Pass 229

Scope: Isaiah 15:1-9; 16:1-14.

Changes:
- Supplied English articles and predicate support for Moabite land, wall, water, cry/border/well, rock/mountain, fugitives, throne, dwellers, fields/vine, altars, and hired-worker phrases.
- Synced translation footnote triggers and aligned several place-name spellings with the source wording: Nebo, Luhith, Nimrim, Rimmon, Admah, Shebam, and Jaazer.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah string, footnote-sync, and decision-coverage checks passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
