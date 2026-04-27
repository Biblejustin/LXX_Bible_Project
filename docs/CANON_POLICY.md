# Canon Policy

This branch currently builds a Protestant-canon fresh translation:

- Old Testament: 39-book Protestant OT order, using the Greek LXX stream as the translation base.
- New Testament: 27-book NT order, using the Textus Receptus Greek stream as the translation base.

The project is LXX-based for the OT text it currently translates, but it is not
yet a full LXX canon edition. Deuterocanonical and apocryphal book-introduction
rows exist as future-work scaffolding, but current source text does not yet
include Tobit, Judith, Wisdom, Sirach, Baruch, Letter of Jeremiah, Susanna, Bel
and the Dragon, Maccabees, 1 Esdras, Prayer of Manasseh, or Psalm 151.

## Reference And Numbering Policy

Logos milestones use standard English/Protestant references so the Personal Book
can navigate with common Bible reference tooling. The translation text and notes
may still preserve LXX ordering, wording, and numbering decisions where the Greek
source diverges from the Masoretic tradition.

When LXX and English/MT ordering diverge, the desired behavior is:

- Keep the Logos milestone reference usable for standard navigation.
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
