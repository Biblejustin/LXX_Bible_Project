# Deuterocanon Pending Decisions

This separate workstream is fully drafted for the rows present in the pinned
eBible GRCLXX package. Greek Ezra B / 2 Esdras is included for broad-EO appendix
coverage. The added Prayer of Manasseh rows are drafted; true 2 Maccabees rows
are sourced and drafted.

## Added Greek Source Rows

Prayer of Manasseh and real 2 Maccabees are not present in the pinned GRCLXX
package. The package file named `53-2MAgrclxx.usfm` identifies itself by title
and content as 4 Maccabees, so it is imported as 4 Maccabees here.

Decision made: import Prayer of Manasseh and true 2 Maccabees from the
public-domain eBible Brenton Greek Septuagint archive
`data/raw/lxx_deuterocanon/grcbrent_usfm.zip`.

Checked source candidates and final source choice are recorded in
`docs/DEUTEROCANON_MISSING_SOURCES.md`.

Remaining work: review and polish the drafted Prayer of Manasseh and
2 Maccabees translations.

## Greek Ezra B / 2 Esdras Scope

Decision made: import `58-2ESgrclxx.usfm` as `2ES` / 2 Esdras. This source is
Greek Ezra B and overlaps canonical Ezra. The separate rows are included for
broad-EO appendix coverage; their first draft reuses the current Ezra draft text
while preserving the distinct GRCLXX Greek rows for review.

Remaining work: audit the 2 Esdras rows against their Greek source where they
differ from the main Ezra source stream.

## Greek Esther Scope

Greek Esther remains imported as full Greek Esther from the pinned GRCLXX source
package.

Decision made: keep the full Greek Esther import and also add `ESGA`, a separate
Greek Esther Additions view derived from the suffixed GRCLXX Greek Esther rows.

Remaining work: audit whether any additions need finer slicing beyond the
suffixed source rows already imported.
