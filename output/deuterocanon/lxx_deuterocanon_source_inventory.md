# LXX Deuterocanon Source Inventory

This is a separate source workspace for the LXX deuterocanon/additions workstream.
It is not folded into the current 66-book Greek Heritage Study Bible outputs.

## Sources

- Source: eBible GRCLXX Septuaginta USFM
- Details: https://ebible.org/details.php?id=grclxx
- Archive: https://ebible.org/Scriptures/grclxx_usfm.zip
- Status: eBible details page labels the source public domain; package includes Orthodox Media Network notice text.
- Source last updated: 2026-02-13
- Verified for this repo: 2026-05-01
- Archive SHA-256: `ecb6be2ca5e31098f6699df538158f2ca05f557bb4e31cf6bf7ad5d8f4c7b7c8`
- Supplemental source: eBible GRCBRE Brenton Septuagint USFM
- Supplemental details: https://ebible.org/details.php?id=grcbrent
- Supplemental archive: https://ebible.org/Scriptures/grcbrent_usfm.zip
- Supplemental status: eBible details page labels the Brenton Greek Septuagint source public domain.
- Supplemental source last updated: 2026-04-08
- Supplemental verified for this repo: 2026-05-03
- Supplemental archive SHA-256: `8fa575a5d1565ae2ceb0d7cabac251ff460242eab823f4ebd40d8eefdeaf6881`

## Import Policy

- Imported rows preserve Greek source text by verse.
- USFM source descriptors and footnotes are preserved as `syntax_notes`.
- `draft_translation` starts blank on first import; importer reruns preserve existing drafts when the reference and Greek source text still match.
- Brenton English and other English witnesses are not used as the translation base.
- The public-domain eBible Brenton Greek package is used only as a supplemental Greek source for Prayer of Manasseh and true 2 Maccabees.
- Greek Esther is imported twice: `ESG` is full Greek Esther, and `ESGA` is an additions-only view made from suffixed GRCLXX Greek Esther rows.
- `2ES` is Greek Ezra B / 2 Esdras from GRCLXX; it overlaps canonical Ezra and reuses the current Ezra draft text for its first draft while keeping separate Greek rows for audit.
- Importer validates source USFM IDs and Greek title lines before accepting source rows.
- Psalm 151 is imported from the Psalms source file as Psalms 151.

## Imported Books

| Code | Book | Rows | Source | Source file | Source ID | Expected title | Validation | Note |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- |
| TOB | Tobit | 245 | grclxx | `41-TOBgrclxx.usfm` | TOB | ΤΩΒΙΤ | imported |  |
| JDT | Judith | 339 | grclxx | `42-JDTgrclxx.usfm` | JDT | ΙΟΥΔΙΘ | imported |  |
| ESG | Greek Esther | 219 | grclxx | `43-ESGgrclxx.usfm` | ESG | ΕΣΘΗΡ | imported | Imported as full Greek Esther; `ESGA` separately provides an additions-only view from the suffixed rows. |
| ESGA | Greek Esther Additions | 55 | grclxx | `43-ESGgrclxx.usfm` | ESG | ΕΣΘΗΡ | imported | Additions-only view derived from the suffixed rows in the full GRCLXX Greek Esther source; full Greek Esther remains imported as ESG. |
| WIS | Wisdom | 437 | grclxx | `45-WISgrclxx.usfm` | WIS | ΣΟΦΙΑ ΣΟΛΟΜΩΝΤΟΣ | imported |  |
| SIR | Sirach | 1378 | grclxx | `46-SIRgrclxx.usfm` | SIR | ΣΟΦΙΑ ΣΕΙΡΑΧ | imported |  |
| BAR | Baruch | 141 | grclxx | `47-BARgrclxx.usfm` | BAR | ΒΑΡΟΥΧ | imported |  |
| LJE | Letter of Jeremiah | 72 | grclxx | `48-LJEgrclxx.usfm` | LJE | ΕΠΙΣΤΟΛΗ ΙΕΡΕΜΙΟΥ | imported |  |
| S3Y | Song of the Three Young Men | 66 | grclxx | `49-S3Ygrclxx.usfm` | S3Y | ΠΡΟΣΕΥΧΗ ΑΖΑΡΙΟΥ ΚΑΙ ΥΜΝΟΣ ΤΩΝ ΤΡΙΩΝ | imported |  |
| SUS | Susanna | 64 | grclxx | `50-SUSgrclxx.usfm` | SUS | ΣΩΣΑΝΝΑ | imported |  |
| BEL | Bel and the Dragon | 42 | grclxx | `51-BELgrclxx.usfm` | BEL | ΒΗΛ ΚΑΙ ΔΡΑΚΩΝ | imported |  |
| 1MA | 1 Maccabees | 917 | grclxx | `52-1MAgrclxx.usfm` | 1MA | ΜΑΚΚΑΒΑΙΩΝ Α | imported |  |
| 2MA | 2 Maccabees | 555 | grcbrent | `53-2MAgrcbrent.usfm` | 2MA | ΜΑΚΚΑΒΑΙΩΝ Βʹ | imported | Imported from the public-domain eBible Brenton Greek Septuagint package because the pinned GRCLXX package's 2MA file contains 4 Maccabees. |
| 1ES | 1 Esdras | 430 | grclxx | `54-1ESgrclxx.usfm` | 1ES | ΕΣΔΡΑΣ Α | imported |  |
| 2ES | 2 Esdras | 280 | grclxx | `58-2ESgrclxx.usfm` | 2ES | ΕΣΔΡΑΣ Β | imported | Greek Ezra B / 2 Esdras from the primary GRCLXX package; this overlaps canonical Ezra and is included for broad EO appendix coverage. |
| MAN | Prayer of Manasseh | 15 | grcbrent | `55-MANgrcbrent.usfm` | MAN | ΠΡΟΣΕΥΧΗ ΜΑΝΑΣΣΗ ΥΙΟΥ ΕΖΕΚΙΟΥ | imported | Imported from the public-domain eBible Brenton Greek Septuagint package because Prayer of Manasseh is absent from the pinned GRCLXX package. |
| 3MA | 3 Maccabees | 227 | grclxx | `57-3MAgrclxx.usfm` | 3MA | ΜΑΚΚΑΒΑΙΩΝ Γ | imported |  |
| 4MA | 4 Maccabees | 481 | grclxx | `53-2MAgrclxx.usfm` | 2MA | ΜΑΚΚΑΒΑΙΩΝ Δ | imported | The source package filename/id says 2MA, but the book title is ΜΑΚΚΑΒΑΙΩΝ Δ / 4 Maccabees. |
| PSA | Psalms | 7 | grclxx | `20-PSAgrclxx.usfm` | PSA | ΨΑΛΜΟΙ | imported | Imported only Psalm 151 from the full Psalms source file. |

## Missing Target Books

| Code | Book | Reason |
| --- | --- | --- |

## Excluded Package Files

| Code | Book | Reason |
| --- | --- | --- |
| DAG | Greek Daniel | Canonical Daniel is handled by the main OT source; Daniel additions are imported from S3Y, SUS, and BEL. |

## Counts

- Imported verse rows: 5970
- Imported book/addition groups: 19
- Rows with source notes/descriptors: 4
- Preserved draft translation rows: 5970
- Source ID mismatches: 0
- Source title mismatches: 0
- Imported CSV: `data/raw/lxx_deuterocanon/deuterocanon_full.csv`
- Missing source candidates: `docs/DEUTEROCANON_MISSING_SOURCES.md`
- Pending decisions: `docs/DEUTEROCANON_PENDING_DECISIONS.md`
- Validation command: `make validate-deuterocanon`

## Next Work

- Review and polish one book/addition at a time against the Greek rows.
- Review the drafted Prayer of Manasseh, true 2 Maccabees, and 2 Esdras rows against the Greek.
- Audit whether the `ESGA` additions-only view needs additional slicing beyond suffixed verse rows.
- See `docs/DEUTEROCANON_MISSING_SOURCES.md` for checked source candidates and final source choice.
- See `docs/DEUTEROCANON_PENDING_DECISIONS.md` for resolved decisions and remaining review notes.
- Use `make validate-deuterocanon` before handoff or commit.
- Decide later whether this workstream gets Markdown-only, Logos DOCX, print proof, or full-LXX merged outputs.
