# Editorial Methodology

This project is a draft Bible-translation and study-apparatus pipeline. It is
not a claim that every Septuagint reading is automatically original or that
every Masoretic reading is secondary. The edition has a confessional and
text-critical point of view, but the build data should show where that point of
view affects the output.

## Limitations And Review Request

The project author is not a biblical scholar or a Koine Greek expert. Scripture
is received as without error in the original manuscripts, but this translation
is a fallible working draft. There definitely are mistakes in the translation,
notes, data, and generated outputs.

Readers and contributors should test the work carefully. Be Berean, as in Acts
17:11: inspect the text, source evidence, and notes diligently to see whether
these things are correct. Corrections and careful issue reports are appreciated.

## Core Commitments

- Scripture is received as God's inerrant word, given by word inspiration in
  the original writings.
- Translation starts from the source text in view, not from inherited English
  phrasing.
- Editorial notes should distinguish source-text data, translation judgment,
  and theological or interpretive comment.
- Contested matters should be flagged with enough detail that a reader can see
  why the note exists.

## Current Text Bases

- Old Testament fresh translation: Greek LXX workspace in
  `data/raw/lxx_greek/ot_full.csv`.
- New Testament fresh translation: Scrivener 1894 Textus Receptus workspace in
  `data/raw/tr_greek/nt_full.csv`.
- Legacy public-domain study Bible prototype: Brenton LXX English plus UKJV NT,
  with TSK cross-reference apparatus.
- English witnesses such as UKJV, Brenton, and other private local witnesses are
  review aids unless a build script explicitly names them as the output source.

## Translation Rules

Detailed working rules live in `data/research/translation_rules.md`. In short:

- Translate source-language syntax first, then smooth only as much as English
  requires.
- Preserve repeated terms where repetition is meaningful.
- Prefer concrete renderings over inherited jargon when context allows.
- Mark ambiguity rather than hiding it.
- Keep alternate renderings in review tables, not only in memory.
- Use familiar English proper-name equivalents when a Greek form clearly
  represents the same biblical referent.
- Put original transliterated forms and name meanings in notes when the form is
  useful for readers.

## Textual Notes

Textual notes are selective. They are added when a variant or textual stream
meaningfully affects translation, theology, canonical reuse, proper-name
identity, or reader understanding.

The project gives deliberate weight to early Greek and other ancient witnesses,
including Septuagintal evidence and pre-medieval Hebrew textual plurality. That
does not mean every LXX reading is preferred. Notes should identify the local
issue rather than giving a global one-size-fits-all comment.

New Testament quotations of the Old Testament are treated case by case. Many NT
quotations align more closely with Septuagintal or otherwise non-Masoretic
forms than with the medieval Masoretic tradition, but there are important
exceptions. The output should show the local evidence instead of flattening all
quotation relationships into one rule.

## Cross-References

Cross-references are generated from public-domain TSK data, with OpenBible data
available as a separately noticed support layer. Large reference sets are
filtered for readability in the Logos Personal Book output.

## Reader-Facing Conventions

The Old Testament Logos output keeps LXX source ordering and visible LXX verse
numbers. The MT-note bridge file may remap hidden Logos milestones to standard
English/MT references so existing reference-anchored notes can appear, but the
printed verse numbers remain from the LXX source rows by design.

Jeremiah 40:14-26 is a deliberate completeness insertion for MT Jeremiah
33:14-26. It is bracketed in the main text because those verses are present in
the Masoretic Text, absent from the LXX text used for this edition, and not
quoted in the New Testament.

Some 1 Kings material follows the Greek order rather than the standard
English/MT chapter order. The Naboth vineyard account appears in this
LXX-numbered edition at 1 Kings 20, while the Ben-Hadad battle material appears
at 1 Kings 21. That is source ordering, not a missing chapter.

Phrases such as "sons of Israel" and "sons of men" are intentionally literal
where the Greek uses son-language. These may be smoothed later only after local
review, not by a global replacement.

## Proper Names And Places

Proper-name notes come from:

- `data/proper_names.csv`
- `data/proper_name_transliteration_notes.csv`
- `data/names_of_god.csv`
- `data/raw/hitchcock_bible_names.txt`
- manual equivalence overrides in
  `scripts/update_proper_name_transliteration_notes.py`

The intended policy is:

- Main text uses a recognizable English equivalent when the referent is clear.
- Notes preserve the source form, Greek form where available, English
  equivalent, and name meaning.
- Place-name notes are included when they help readers identify the location or
  meaning.
- Deuterocanonical and non-canonical names may be marked for later review when
  no reliable equivalent is established.

Name meanings are a reader aid, not a claim of final etymological certainty.
Many current meanings are seeded from public-domain legacy resources such as
Hitchcock's Bible Names Dictionary, then supplemented with manual review. These
entries should be corrected when stronger lexical evidence is found.

## Private Research Boundary

Local Logos resources and copyrighted English witnesses may inform short
derived observations in ignored/local files. Long copyrighted excerpts should
not be committed. Public outputs should use short paraphrased observations,
public-domain witnesses, or original analysis.

## Audit Trail

Important review data is stored in CSV and JSON artifacts under `data/research/`
and `output/`. Build diagnostics are intentional: they are part of how the
edition exposes coverage, unresolved rows, and placement counts.
