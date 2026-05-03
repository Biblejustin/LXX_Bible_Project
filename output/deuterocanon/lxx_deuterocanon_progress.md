# LXX Deuterocanon Progress

Separate workstream. These rows do not feed the 66-book Greek Heritage Study Bible outputs.

## Summary

- Imported groups: 19
- Verse rows: 5970
- Drafted rows: 5970
- Remaining rows: 0
- Source ID mismatches: 0
- Source title mismatches: 0

## Books

| Code | Book | Status | Rows | Drafted | Remaining | Chapters | First | Last | Source validation |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| TOB | Tobit | drafted | 245 | 245 | 0 | 14 | Tobit 1:1 | Tobit 14:15 | imported |
| JDT | Judith | drafted | 339 | 339 | 0 | 16 | Judith 1:1 | Judith 16:25 | imported |
| ESG | Greek Esther | drafted | 219 | 219 | 0 | 10 | Greek Esther 1:1α | Greek Esther 10:3λ | imported |
| ESGA | Greek Esther Additions | drafted | 55 | 55 | 0 | 4 | Greek Esther Additions 1:1α | Greek Esther Additions 10:3λ | imported |
| WIS | Wisdom | drafted | 437 | 437 | 0 | 19 | Wisdom 1:1 | Wisdom 19:22 | imported |
| SIR | Sirach | drafted | 1378 | 1378 | 0 | 51 | Sirach 1:1 | Sirach 51:30 | imported |
| BAR | Baruch | drafted | 141 | 141 | 0 | 5 | Baruch 1:1 | Baruch 5:9 | imported |
| LJE | Letter of Jeremiah | drafted | 72 | 72 | 0 | 1 | Letter of Jeremiah 1:1 | Letter of Jeremiah 1:72 | imported |
| S3Y | Song of the Three Young Men | drafted | 66 | 66 | 0 | 1 | Song of the Three Young Men 1:1 | Song of the Three Young Men 1:67 | imported |
| SUS | Susanna | drafted | 64 | 64 | 0 | 1 | Susanna 1:1 | Susanna 1:64 | imported |
| BEL | Bel and the Dragon | drafted | 42 | 42 | 0 | 1 | Bel and the Dragon 1:1 | Bel and the Dragon 1:42 | imported |
| 1MA | 1 Maccabees | drafted | 917 | 917 | 0 | 16 | 1 Maccabees 1:1 | 1 Maccabees 16:24 | imported |
| 2MA | 2 Maccabees | drafted | 555 | 555 | 0 | 15 | 2 Maccabees 1:1 | 2 Maccabees 15:39 | imported |
| 1ES | 1 Esdras | drafted | 430 | 430 | 0 | 9 | 1 Esdras 1:1 | 1 Esdras 9:55 | imported |
| 2ES | 2 Esdras | drafted | 280 | 280 | 0 | 10 | 2 Esdras 1:1 | 2 Esdras 10:44 | imported |
| MAN | Prayer of Manasseh | drafted | 15 | 15 | 0 | 1 | Prayer of Manasseh 1:1 | Prayer of Manasseh 1:15 | imported |
| 3MA | 3 Maccabees | drafted | 227 | 227 | 0 | 7 | 3 Maccabees 1:1 | 3 Maccabees 7:23 | imported |
| 4MA | 4 Maccabees | drafted | 481 | 481 | 0 | 18 | 4 Maccabees 1:1 | 4 Maccabees 18:24 | imported |
| PSA | Psalms | drafted | 7 | 7 | 0 | 1 | Psalms 151:1 | Psalms 151:7 | imported |

## Missing Targets

| Code | Book | Reason |
| --- | --- | --- |

Checked source candidates: `docs/DEUTEROCANON_MISSING_SOURCES.md`
Pending decisions: `docs/DEUTEROCANON_PENDING_DECISIONS.md`

## Review Loop

Use ignored one-book working output while reviewing or polishing:

```bash
make build-deuterocanon-book BOOK=Tobit
```

Use full output before handoff or commit:

```bash
make validate-deuterocanon
```
