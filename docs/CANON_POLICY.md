# Canon Policy

This branch currently builds a Protestant-canon fresh translation:

- Old Testament: 39-book Protestant OT order, using the Greek LXX stream as the translation base.
- New Testament: 27-book NT order, using the Textus Receptus Greek stream as the translation base.

The project is LXX-based for the OT text it currently translates, but this
branch remains the Protestant-canon edition. Deuterocanonical and apocryphal LXX
books should be handled as a separate workstream and separate output, not folded
into this branch by accident. Current source text does not yet include Tobit,
Judith, Wisdom, Sirach, Baruch, Letter of Jeremiah, Susanna, Bel and the Dragon,
Maccabees, 1 Esdras, Prayer of Manasseh, or Psalm 151. Their absence is a
branch-scope decision, not a claim that they are absent from every LXX tradition.

## Source Policy

The OT translation is made from the normalized LXX Greek source rows in
`data/raw/lxx_greek/ot_full.csv`, not by revising Brenton or another English
base text. Brenton and other public-domain materials may provide comparison
notes or source checks, but they are not the translation base.

The NT translation is made from the Scrivener 1894 Textus Receptus Greek stream
imported from byztxt/greektext-scrivener text-only files.

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

- A separate LXX deuterocanon edition.
- A full LXX-canon edition after the separate deuterocanon work is mature.
- Deuterocanonical/apocryphal books and Greek additions.
- Separate release artifacts for Protestant-canon, full-LXX-canon, and study
  editions.
