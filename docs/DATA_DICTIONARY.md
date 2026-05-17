# Data Dictionary

This file documents the CSV columns most likely to be edited or reviewed.

## Fresh Translation Source CSV

Applies to:

- `data/raw/lxx_greek/ot_full.csv`
- `data/raw/lxx_deuterocanon/deuterocanon_full.csv`
- `data/raw/tr_greek/nt_full.csv`

| Column | Meaning |
| --- | --- |
| `ref` | Project reference, such as `Genesis 1:1`, `Matthew 1:1`, or source-specific labels like `Greek Esther 1:1α` |
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

Deuterocanon rows are isolated from the 66-book OT/NT outputs. Their source
manifest is `data/raw/lxx_deuterocanon/source_manifest.json`; source candidates
and the supplemental-source choice for Prayer of Manasseh and 2 Maccabees are
tracked in `docs/DEUTEROCANON_MISSING_SOURCES.md`.
Plain embedded verse labels in deuterocanon Greek source rows are split into
separate CSV rows when they mark a distinct verse. Bracketed source-text
sections remain bracketed.

## Translation Footnotes

Applies to `data/research/translation_footnotes.csv`.

| Column | Meaning |
| --- | --- |
| `ref` | Verse reference |
| `note_type` | Note category, such as translation, name, place, or textual |
| `trigger_phrase` | Word or phrase where the note should attach |
| `footnote_text` | Public note text |
| `source_basis` | Short evidence or source category behind the note |
| `status` | Review state, such as `drafted`, `reviewed`, or `approved` |

## Translation Decisions

Applies to `data/research/translation_decisions.csv`.

| Column | Meaning |
| --- | --- |
| `ref` | Verse reference |
| `greek_phrase` | Source phrase or verse span under review |
| `lemma` | Lemma support field when available |
| `morphology` | Morphology support field when available |
| `chosen_rendering` | Reviewed English rendering used by the fresh output |
| `alternate_renderings` | Other renderings considered during review |
| `rationale` | Short reason for the chosen rendering |
| `status` | Review state, such as `drafted`, `reviewed`, or `accepted` |
| `reviewer` | Reviewer/source marker for the decision |

## Variant Notes

Applies to `data/research/variant_notes.csv`.

| Column | Meaning |
| --- | --- |
| `ref` | Verse reference |
| `witnesses` | Witnesses or source tradition named for the variant |
| `reading` | Variant reading or textual issue under review |
| `translation_impact` | Plain-language effect on translation, if any |
| `decision` | Current editorial decision for the note |
| `status` | Review state, such as `pending` or `reviewed` |

## Reviewed Phrase Guards

Applies to `data/research/reviewed_phrase_guards.csv`.

| Column | Meaning |
| --- | --- |
| `testament` | Source workspace scope, such as `ot` or `nt` |
| `ref` | Verse reference |
| `mode` | Guard mode, such as `contains` or `equals` |
| `phrase` | Reviewed phrase that must remain in the source output |
| `note` | Short reason for the guard |
| `status` | Review state for the guard row |

## Proper Name Notes

Applies to `data/proper_name_transliteration_notes.csv`.

| Column | Meaning |
| --- | --- |
| `name` | Source transliterated form found in the draft/source layer |
| `kind` | Name category, such as transliterated form or place name |
| `first_reference` | First reference where the name note applies |
| `source` | Testament or source scope for the note |
| `english_equivalent` | Familiar English equivalent used or recommended in the main text |
| `source_form` | Source-form spelling found in the draft/source layer |
| `greek_form` | Greek spelling tied to the source form |
| `name_meaning` | Meaning supplied from public-domain name sources or manual research |
| `equivalent_source` | Source or rule used to choose the English equivalent |
| `equivalent_confidence` | Confidence category for the chosen equivalent |
| `footnote` | Reader-facing note text |

## Contextual Proper Name Decisions

Applies to `data/research/contextual_proper_name_decisions.csv`.

| Column | Meaning |
| --- | --- |
| `ref` | Verse reference |
| `current_form` | Form currently found in the source draft |
| `preferred_form` | Context-specific English form to use |
| `match_text` | Optional exact text to replace |
| `replacement_text` | Optional exact replacement text |
| `reason` | Short reason for the contextual decision |
| `status` | Review or application state |
| `notes` | Application notes or extra review details |

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
