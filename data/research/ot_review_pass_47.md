# OT Review Pass 47

Scope: English article cleanup around recurring divine-name formulas.

- Added `scripts/apply_ot_article_cleanup.py` for scoped cleanup of repeated bare English formula artifacts.
- Inserted missing articles in common constructs such as `word/day/name/hand/face/fear/wrath of the Lord` when no determiner already governed the phrase.
- Normalized repeated bare `Lord` subject/object formulas such as `Seek Lord`, `Lord showed`, and `Lord stirred`.
- Fixed `2 Chronicles 30:18` from `Lord the good one make atonement` to `May the good Lord make atonement`.
- Added a second exact-formula pass for clear non-vocative cases such as `Serve the Lord`, `Great is the Lord`, `The Lord is my strength and my hymn`, and `unless the Lord guards a city`.
- Added a dedupe guard for article cleanup so `the Lord` cannot become `the the Lord`.
- Left determined phrases such as `a word of the Lord`, `every word of the Lord`, `right hand of the Lord`, `holy name of the Lord`, and `this day of the Lord` unchanged.
