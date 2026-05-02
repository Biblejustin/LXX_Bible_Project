# LXX Deuterocanon Progress

Separate workstream. These rows do not feed the 66-book Greek Heritage Study Bible outputs.

## Summary

- Imported groups: 15
- Verse rows: 5065
- Drafted rows: 0
- Remaining rows: 5065
- Source ID mismatches: 0
- Source title mismatches: 0

## Books

| Code | Book | Status | Rows | Drafted | Remaining | Chapters | First | Last | Source validation |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| TOB | Tobit | not_started | 245 | 0 | 245 | 14 | Tobit 1:1 | Tobit 14:15 | imported |
| JDT | Judith | not_started | 339 | 0 | 339 | 16 | Judith 1:1 | Judith 16:25 | imported |
| ESG | Greek Esther | not_started | 219 | 0 | 219 | 10 | Greek Esther 1:1α | Greek Esther 10:3λ | imported |
| WIS | Wisdom | not_started | 437 | 0 | 437 | 19 | Wisdom 1:1 | Wisdom 19:22 | imported |
| SIR | Sirach | not_started | 1378 | 0 | 1378 | 51 | Sirach 1:1 | Sirach 51:30 | imported |
| BAR | Baruch | not_started | 141 | 0 | 141 | 5 | Baruch 1:1 | Baruch 5:9 | imported |
| LJE | Letter of Jeremiah | not_started | 72 | 0 | 72 | 1 | Letter of Jeremiah 1:1 | Letter of Jeremiah 1:72 | imported |
| S3Y | Song of the Three Young Men | not_started | 66 | 0 | 66 | 1 | Song of the Three Young Men 1:1 | Song of the Three Young Men 1:67 | imported |
| SUS | Susanna | not_started | 64 | 0 | 64 | 1 | Susanna 1:1 | Susanna 1:64 | imported |
| BEL | Bel and the Dragon | not_started | 42 | 0 | 42 | 1 | Bel and the Dragon 1:1 | Bel and the Dragon 1:42 | imported |
| 1MA | 1 Maccabees | not_started | 917 | 0 | 917 | 16 | 1 Maccabees 1:1 | 1 Maccabees 16:24 | imported |
| 1ES | 1 Esdras | not_started | 430 | 0 | 430 | 9 | 1 Esdras 1:1 | 1 Esdras 9:55 | imported |
| 3MA | 3 Maccabees | not_started | 227 | 0 | 227 | 7 | 3 Maccabees 1:1 | 3 Maccabees 7:23 | imported |
| 4MA | 4 Maccabees | not_started | 481 | 0 | 481 | 18 | 4 Maccabees 1:1 | 4 Maccabees 18:24 | imported |
| PSA | Psalms | not_started | 7 | 0 | 7 | 1 | Psalms 151:1 | Psalms 151:7 | imported |

## Missing Targets

| Code | Book | Reason |
| --- | --- | --- |
| MAN | Prayer of Manasseh | Not present in the pinned GRCLXX USFM package. |
| 2MA | 2 Maccabees | Not present as 2 Maccabees in the pinned GRCLXX USFM package; the package file named 2MA contains 4 Maccabees by title and content. |

## Translation Loop

Use ignored one-book working output while translating:

```bash
make build-deuterocanon-book BOOK=Tobit
```

Use full output before handoff or commit:

```bash
make build-deuterocanon
```
