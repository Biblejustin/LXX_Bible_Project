# Canon Policy

This branch currently builds a Protestant-canon fresh translation:

- Old Testament: 39-book Protestant OT order, using the Greek LXX stream as the translation base.
- New Testament: 27-book NT order, using the Textus Receptus Greek stream as the translation base.

The project is LXX-based for the OT text it currently translates, but this
branch remains the Protestant-canon edition. Deuterocanonical and apocryphal LXX
books are handled as a separate workstream and separate output, not folded into
the 66-book outputs by accident. The separate workspace begins at
`data/raw/lxx_deuterocanon/deuterocanon_full.csv`; the main Protestant-canon OT
source remains `data/raw/lxx_greek/ot_full.csv`.

## Source Policy

The OT translation is made from the normalized LXX Greek source rows in
`data/raw/lxx_greek/ot_full.csv`, not by revising Brenton or another English
base text. Brenton and other public-domain materials may provide comparison
notes or source checks, but they are not the translation base.

The NT translation is made from the Scrivener 1894 Textus Receptus Greek stream
imported from byztxt/greektext-scrivener text-only files.

The separate deuterocanon/additions workspace imports Greek rows primarily from
the eBible GRCLXX Septuaginta USFM archive pinned at
`data/raw/lxx_deuterocanon/grclxx_usfm.zip`. It also uses the public-domain
eBible Brenton Greek Septuagint archive pinned at
`data/raw/lxx_deuterocanon/grcbrent_usfm.zip` for Prayer of Manasseh and true
2 Maccabees, because those rows are absent from the GRCLXX package. Its
`draft_translation` column starts blank on first import, then importer reruns
preserve existing draft rows when the reference and Greek source text still
match. USFM source descriptors and footnotes are preserved as `syntax_notes`.
Books or appendix materials are in scope only where a Greek source is present,
or where there is strong evidence for a Greek source behind the extant text.
Latin-only appendix material is skipped unless that Greek-source threshold is
met and documented.
That workspace currently includes Tobit, Judith, Greek Esther, Wisdom, Sirach,
Baruch, Letter of Jeremiah, Song of the Three Young Men, Susanna, Bel and the
Dragon, 1-4 Maccabees, 1 Esdras, Greek Ezra B / 2 Esdras, Prayer of Manasseh,
Psalm 151, and a separate Greek Esther Additions view derived from the suffixed
and inline-labeled GRCLXX Greek Esther rows.
Plain embedded verse labels in the Greek source are split into separate rows
when they mark a distinct verse; bracketed source-text sections remain bracketed
in the imported Greek and draft text.
The pinned GRCLXX package contains a file named 2MA, but its title and content
identify it as 4 Maccabees, so this workspace labels it by content and imports
true 2 Maccabees from the Brenton Greek supplement.
Checked source candidates and final source choice are recorded in
`docs/DEUTEROCANON_MISSING_SOURCES.md`.
Resolved and remaining review decisions are tracked in
`docs/DEUTEROCANON_PENDING_DECISIONS.md`.
1 Enoch is tracked separately in `docs/1_ENOCH_SOURCE_STATUS.md`: the repo has
Charles's public-domain English witness text, but no normalized Greek or Aramaic
source rows for a Greek Heritage translation, so it is not part of the
deuterocanon source workspace. `make build-enoch-witness` refreshes a separate
Charles witness/comparison workspace for appendix planning only.
Use `make validate-deuterocanon` for focused rebuild and smoke validation of
this separate workstream.

Daniel follows the Greek Daniel rows currently present in this branch's LXX
source workspace. It should not be silently replaced with Theodotion- or
MT/Aramaic-shaped wording. Where Greek Daniel differs sharply from familiar
Theodotion or MT/Aramaic readings, use front-matter explanation and local
footnotes rather than harmonizing the translation text.

## Reference And Numbering Policy

Primary Logos and proofreading outputs preserve the LXX source order and visible
LXX numbering for the Old Testament. A separate reference-note bridge output
remaps OT milestones to standard English/Protestant references where a reliable
mapping exists, so common reference-anchored Logos notes can still surface.
The translation text and notes preserve LXX ordering, wording, and numbering
decisions where the Greek source diverges from the Masoretic tradition.

Reader-facing book prefaces and selected footnotes should call out the high
traffic divergence points, especially Psalms, Jeremiah, Daniel, Isaiah 9, Micah
5, Malachi 3-4, and Exodus 20.

When LXX and English/MT ordering diverge, the desired behavior is:

- Keep the primary visible reference tied to the LXX source row.
- Keep the bridge milestone reference usable for standard navigation where the
  mapping is reliable.
- Keep LXX source wording in the translation text.
- Add selective notes for material differences that affect readers.
- Do not silently import MT wording unless explicitly marked as supplied for
  completeness.

Jeremiah 33:14-26 is an example of intentionally supplied MT material: it is
bracketed and footnoted because it is absent from the LXX stream used here, but
included for completeness.

## Future Work

Future branches or separate release artifacts may add:

- A full LXX-canon edition after the separate deuterocanon work is mature.
- Separate release artifacts for Protestant-canon, full-LXX-canon, and study
  editions.
