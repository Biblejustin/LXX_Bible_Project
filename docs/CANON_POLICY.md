# Canon Policy

This branch currently builds a Protestant-canon fresh translation:

- Old Testament: 39-book Protestant OT order, using the Greek LXX stream as the translation base.
- New Testament: 27-book NT order, using the Textus Receptus Greek stream as the translation base.

The project is LXX-based for the OT text it currently translates, but it is not
yet a full LXX canon edition. Deuterocanonical and apocryphal book-introduction
rows exist as future-work scaffolding, but current source text does not yet
include Tobit, Judith, Wisdom, Sirach, Baruch, Letter of Jeremiah, Susanna, Bel
and the Dragon, Maccabees, 1 Esdras, Prayer of Manasseh, or Psalm 151. Their
absence is a canon-scope decision for this branch, not a claim that they are
absent from every LXX tradition.

## Reference And Numbering Policy

Primary Logos and proofreading outputs preserve the LXX source order and visible
LXX numbering for the Old Testament. A separate reference-note bridge output
remaps OT milestones to standard English/Protestant references where a reliable
mapping exists, so common reference-anchored Logos notes can still surface.
The translation text and notes preserve LXX ordering, wording, and numbering
decisions where the Greek source diverges from the Masoretic tradition.

Reader-facing front matter and selected footnotes should call out the high
traffic divergence points, especially Psalms, Jeremiah, Isaiah 9, Micah 5, and
Malachi 3-4.

Daniel currently follows the Greek source rows in this branch rather than
silently replacing them with Theodotion- or MT-shaped wording. Major differences
should be footnoted where they affect familiar readings.

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

Future branches may add:

- A full LXX-canon edition.
- Deuterocanonical/apocryphal books and Greek additions.
- Separate release artifacts for Protestant-canon, full-LXX-canon, and study
  editions.
