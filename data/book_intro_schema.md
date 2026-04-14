# Book Introduction Schema

Use this schema for one introduction page before each book.

Project assumptions for this dataset:

- Scripture is the inerrant word of God.
- The originals were verbally inspired.
- Jesus' attributions govern authorship where He identifies a human author.
- MT/LXX discussion may note corruption, Vorlage shifts, later editorial change, or preserved older readings.

Recommended fields:

- `book_code`
  - Internal code used by the build pipeline.
- `book_name`
  - Standard English display name.
- `canonical_order`
  - Integer used for sorting in this edition.
- `section`
  - `OT`, `NT`, or `Apocrypha`.
- `intro_title`
  - Usually same as `book_name`.
- `traditional_author`
  - Conservative evangelical authorship statement.
- `authorship_basis`
  - Short rationale, especially where Jesus or the NT attributes authorship.
- `jesus_or_nt_attribution`
  - Citation or summary if Christ or apostolic witness identifies the author.
- `composition_date`
  - Conservative composition date in plain English.
- `mt_timeline`
  - MT-oriented historical/timeline placement note.
- `lxx_timeline`
  - LXX-oriented historical/timeline placement note.
- `historical_setting`
  - Setting, audience, covenant-historical context.
- `purpose_theme`
  - Main purpose and theological burden.
- `key_themes`
  - Short semicolon-separated theme list.
- `outline`
  - Short paragraph or semicolon-separated outline.
- `oldest_fragment`
  - Earliest known fragment or witness.
- `oldest_fragment_date`
  - Approximate date.
- `oldest_substantial_manuscript`
  - Earliest substantial surviving witness.
- `oldest_substantial_date`
  - Approximate date.
- `oldest_complete_hebrew`
  - Oldest complete or near-complete Hebrew witness, if any.
- `oldest_complete_hebrew_date`
  - Approximate date.
- `oldest_complete_greek`
  - Oldest complete or near-complete Greek witness, if any.
- `oldest_complete_greek_date`
  - Approximate date.
- `oldest_external_reference`
  - Earliest known citation, quotation, or clear allusion outside Scripture.
- `oldest_external_reference_author`
  - Who made that reference.
- `oldest_external_reference_date`
  - Approximate date.
- `textual_notes`
  - Notes on MT, LXX, Vorlage, omissions, expansions, or debated loci.
- `conservative_notes`
  - Notes specific to conservative/inerrancy framing.
- `source_notes`
  - Research breadcrumbs or citations for internal use.
- `status`
  - `todo`, `draft`, or `reviewed`.

Rendering guidance:

- Keep final intro page concise enough for one printed page.
- Store fuller research in `source_notes`.
- Prefer plain-English dates like `ca. 1446-1406 BC` or `before AD 70`.
- Use `unknown` only when truly necessary.
- Where no Hebrew witness exists, say so plainly.
- Where only Greek survives, say so plainly.
