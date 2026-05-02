# LXX Deuterocanon Source Inventory

This is a separate source workspace for the LXX deuterocanon/additions workstream.
It is not folded into the current 66-book Greek Heritage Study Bible outputs.

## Source

- Source: eBible GRCLXX Septuaginta USFM
- Details: https://ebible.org/details.php?id=grclxx
- Archive: https://ebible.org/Scriptures/grclxx_usfm.zip
- Status: eBible details page labels the source public domain; package includes Orthodox Media Network notice text.
- Source last updated: 2026-02-13
- Verified for this repo: 2026-05-01
- Archive SHA-256: `ecb6be2ca5e31098f6699df538158f2ca05f557bb4e31cf6bf7ad5d8f4c7b7c8`

## Import Policy

- Imported rows preserve Greek source text by verse.
- USFM source descriptors and footnotes are preserved as `syntax_notes`.
- `draft_translation` is intentionally blank.
- Brenton and other English witnesses are not used as the translation base.
- Greek Esther is imported as the full Greek Esther source for now; additions-only slicing remains a later editorial step.
- Importer validates source USFM IDs and Greek title lines before accepting source rows.
- Psalm 151 is imported from the Psalms source file as Psalms 151.

## Imported Books

| Code | Book | Rows | Source file | Source ID | Expected title | Validation | Note |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| TOB | Tobit | 245 | `41-TOBgrclxx.usfm` | TOB | ΤΩΒΙΤ | imported |  |
| JDT | Judith | 339 | `42-JDTgrclxx.usfm` | JDT | ΙΟΥΔΙΘ | imported |  |
| ESG | Greek Esther | 219 | `43-ESGgrclxx.usfm` | ESG | ΕΣΘΗΡ | imported | Imported as full Greek Esther for now; additions-only slicing remains a later editorial step. |
| WIS | Wisdom | 437 | `45-WISgrclxx.usfm` | WIS | ΣΟΦΙΑ ΣΟΛΟΜΩΝΤΟΣ | imported |  |
| SIR | Sirach | 1378 | `46-SIRgrclxx.usfm` | SIR | ΣΟΦΙΑ ΣΕΙΡΑΧ | imported |  |
| BAR | Baruch | 141 | `47-BARgrclxx.usfm` | BAR | ΒΑΡΟΥΧ | imported |  |
| LJE | Letter of Jeremiah | 72 | `48-LJEgrclxx.usfm` | LJE | ΕΠΙΣΤΟΛΗ ΙΕΡΕΜΙΟΥ | imported |  |
| S3Y | Song of the Three Young Men | 66 | `49-S3Ygrclxx.usfm` | S3Y | ΠΡΟΣΕΥΧΗ ΑΖΑΡΙΟΥ ΚΑΙ ΥΜΝΟΣ ΤΩΝ ΤΡΙΩΝ | imported |  |
| SUS | Susanna | 64 | `50-SUSgrclxx.usfm` | SUS | ΣΩΣΑΝΝΑ | imported |  |
| BEL | Bel and the Dragon | 42 | `51-BELgrclxx.usfm` | BEL | ΒΗΛ ΚΑΙ ΔΡΑΚΩΝ | imported |  |
| 1MA | 1 Maccabees | 917 | `52-1MAgrclxx.usfm` | 1MA | ΜΑΚΚΑΒΑΙΩΝ Α | imported |  |
| 1ES | 1 Esdras | 430 | `54-1ESgrclxx.usfm` | 1ES | ΕΣΔΡΑΣ Α | imported |  |
| 3MA | 3 Maccabees | 227 | `57-3MAgrclxx.usfm` | 3MA | ΜΑΚΚΑΒΑΙΩΝ Γ | imported |  |
| 4MA | 4 Maccabees | 481 | `53-2MAgrclxx.usfm` | 2MA | ΜΑΚΚΑΒΑΙΩΝ Δ | imported | The source package filename/id says 2MA, but the book title is ΜΑΚΚΑΒΑΙΩΝ Δ / 4 Maccabees. |
| PSA | Psalms | 7 | `20-PSAgrclxx.usfm` | PSA | ΨΑΛΜΟΙ | imported | Imported only Psalm 151 from the full Psalms source file. |

## Missing Target Books

| Code | Book | Reason |
| --- | --- | --- |
| MAN | Prayer of Manasseh | Not present in the pinned GRCLXX USFM package. |
| 2MA | 2 Maccabees | Not present as 2 Maccabees in the pinned GRCLXX USFM package; the package file named 2MA contains 4 Maccabees by title and content. |

## Excluded Package Files

| Code | Book | Reason |
| --- | --- | --- |
| 2ES | 2 Esdras / Greek Ezra B | In this package this is the Greek Ezra-Nehemiah stream, not the separate deuterocanon work target. |
| DAG | Greek Daniel | Canonical Daniel is handled by the main OT source; Daniel additions are imported from S3Y, SUS, and BEL. |

## Counts

- Imported verse rows: 5065
- Imported book/addition groups: 15
- Rows with source footnotes: 2
- Source ID mismatches: 0
- Source title mismatches: 0
- Imported CSV: `data/raw/lxx_deuterocanon/deuterocanon_full.csv`

## Next Work

- Translate one book/addition at a time from the Greek rows.
- Decide whether Greek Esther should remain full Greek Esther here or be split into additions-only ranges.
- Add lawful Greek source rows for Prayer of Manasseh and 2 Maccabees if those remain in scope.
- See `output/deuterocanon/missing_source_candidates.md` for checked-but-not-imported source candidates.
- Decide later whether this workstream gets Markdown-only, Logos DOCX, print proof, or full-LXX merged outputs.
