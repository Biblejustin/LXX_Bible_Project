# Deuterocanon Pending Decisions

This separate workstream is fully drafted and has received a first polish pass
for the Greek rows currently imported from the pinned eBible GRCLXX package and
the public-domain eBible Brenton Greek supplement. Greek Ezra B / 2 Esdras is
included for broad-EO appendix coverage.

Scope rule: this project translates Greek textual sources. Additional appendix
material is skipped unless a Greek source is present, or unless strong evidence
for a Greek source behind the extant text is documented.

## Added Greek Source Rows

Prayer of Manasseh and real 2 Maccabees are not present in the pinned GRCLXX
package. The package file named `53-2MAgrclxx.usfm` identifies itself by title
and content as 4 Maccabees, so it is imported as 4 Maccabees here.

Decision made: import Prayer of Manasseh and true 2 Maccabees from the
public-domain eBible Brenton Greek Septuagint archive
`data/raw/lxx_deuterocanon/grcbrent_usfm.zip`.

Checked source candidates and final source choice are recorded in
`docs/DEUTEROCANON_MISSING_SOURCES.md`.

Status: Prayer of Manasseh and true 2 Maccabees have been sourced, drafted, and
polished against their imported Greek rows.

## Greek Ezra B / 2 Esdras Scope

Decision made: import `58-2ESgrclxx.usfm` as `2ES` / 2 Esdras. This source is
Greek Ezra B and overlaps canonical Ezra. The separate rows are included for
broad-EO appendix coverage. On a blank first import, the importer can seed those
rows from the current Ezra draft while still preserving the distinct GRCLXX
Greek rows for review.

Status: the 2 Esdras rows have been audited and polished against their Greek
source rows where they differ from the main Ezra source stream.

## Greek Esther Scope

Greek Esther remains imported as full Greek Esther from the pinned GRCLXX source
package.

Decision made: keep the full Greek Esther import and also add `ESGA`, a separate
Greek Esther Additions view derived from the suffixed and inline-labeled GRCLXX
Greek Esther rows.

Status: the additions-only view now includes the inline-labeled prayer and
throne-scene addition rows embedded in Greek Esther 4:17, 5:1, 5:2, and 10:3α,
not only separately suffixed source rows.

## Embedded Verse Labels

Decision made: split plain embedded verse labels in the Greek source into
separate source rows when they identify a distinct verse. Keep bracketed
source-text sections bracketed rather than treating those brackets as display
noise.

## Remaining Review

No additional deuterocanonical appendix material is queued unless a Greek source
is present, or unless strong evidence for a Greek source behind the extant text
is documented. Remaining work is proofreading, selected note/preface work, and
formatting/output polish rather than adding Latin-only appendix books.
