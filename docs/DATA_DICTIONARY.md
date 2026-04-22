# Data Dictionary

This file documents the CSV columns most likely to be edited or reviewed.

## Fresh Translation Source CSV

Applies to:

- `data/raw/lxx_greek/ot_full.csv`
- `data/raw/tr_greek/nt_full.csv`

| Column | Meaning |
| --- | --- |
| `ref` | Canonical English reference, such as `Genesis 1:1` or `Matthew 1:1` |
| `book_code` | Short source/import code for the book |
| `book_name` | English book name used by output builders |
| `chapter` | Chapter number as text |
| `verse` | Verse number as text; may include source-specific verse labels if needed |
| `greek_text` | Source Greek text for the verse |
| `transliteration` | Greek transliteration support field |
| `literal_gloss` | Draft lexical/literal gloss support field |
| `syntax_notes` | Source-language or review notes used during drafting |
| `draft_translation` | Current fresh translation draft used by output builders |

NT rows also include:

| Column | Meaning |
| --- | --- |
| `ukjv_translation` | UKJV witness text used for review comparison, not as the source text |
| `review_status` | NT review state, such as `tr_literal_pass1` or `needs_focused_tr_review` |
| `review_notes` | Short audit notes from NT revision scripts |

## Translation Footnotes

Applies to `data/research/translation_footnotes.csv`.

| Column | Meaning |
| --- | --- |
| `ref` | Verse reference |
| `anchor` | Word or phrase where the note should attach |
| `note_type` | Note category, such as translation, name, place, or textual |
| `note` | Public note text |

## Variant Notes

Applies to `data/research/variant_notes.csv`.

| Column | Meaning |
| --- | --- |
| `ref` | Verse reference |
| `anchor` | Word or phrase where the note should attach |
| `variant_type` | Local category for the textual issue |
| `note` | Reader-facing note text |
| `source` | Witness or review source used for the note |

## Proper Name Notes

Applies to `data/proper_name_transliteration_notes.csv`.

| Column | Meaning |
| --- | --- |
| `scope` | Testament/book scope for the note |
| `ref` | Reference where the name occurs |
| `name` | Source transliterated form found in the draft/source layer |
| `english_equivalent` | Familiar English equivalent used or recommended in the main text |
| `name_meaning` | Meaning supplied from public-domain name sources or manual research |
| `note` | Reader-facing note text |

## Diagnostics JSON

Diagnostics files under `output/` are build audit artifacts. Common fields:

| Field | Meaning |
| --- | --- |
| `rows` | Number of processed source rows |
| `status_counts` | Count by review or build status |
| `footnote_count` | Total generated footnotes |
| `validations` | DOCX/XML/ZIP checks for Logos outputs |
| `queue_rows` | Rows still needing review |

If a script emits diagnostics, preserve them with the matching generated output
so reviewers can see coverage and unresolved work.
