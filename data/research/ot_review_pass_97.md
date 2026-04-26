# OT Review Pass 97

Scope: recurring national-title, sacred-object, and theology-term article cleanup after pass 96.

Changes:
- Normalized national-title formulas:
  - `king of Assyrians` -> `king of the Assyrians`
  - `king of Persians` -> `king of the Persians`
  - `king of north` -> `king of the north`
- Normalized selected bare house formulas:
  - `as house of Ahab` -> `as the house of Ahab`
  - `let house of David` -> `let the house of David`
  - `like house of David` -> `like the house of David`
  - `gathered house of Judah` -> `gathered the house of Judah`
  - non-vocative `house of Jacob` formulas -> `the house of Jacob`
- Normalized sacred-object formulas:
  - `ark of God` -> `the ark of God`
  - `ark of covenant` -> `the ark of the covenant`
- Normalized `law of God`, `glory of God`, `heart of man`, `remnant of Israel`, `mountains of Israel`, `mouth of ungodly`, `camp of Philistines`, and `tent of testimony` article defects.
- Normalized Psalm 150:3 `in sound of trumpet` -> `with the sound of a trumpet`.

Validation:
- `scripts/apply_ot_article_cleanup.py` updated 117 source rows, 40 decision rows, and 101 footnote rows.
- Targeted smoke test passed.
- Follow-up scan returned zero for pass 97 exact guards and double articles.
