# OT Review Pass 211: Ecclesiastes 9 articles

Scope: Ecclesiastes 9:1-5, 9:7, 9:9, 9:11-12, 9:14, 9:17.

Changes:
- Supplied English articles and predicate support for righteous/wise, good/evil, heart-of-sons, living/dead, woman/days, race/war, sons-of-man, city/king, and cry-of-rulers phrases.
- Preserved existing Ecclesiastes 9:15-16 poor-wise-man decisions.
- Left Ecclesiastes 9:6, 9:8, 9:10, 9:13, and 9:18 unchanged because current wording is readable for this article-focused pass.

Validation:
- CSV shape check passed.
- `python3 -m pytest -q tests/test_smoke.py` passed.
- `make checkpoint-ot` passed.
- `make build-ot-review` passed.
