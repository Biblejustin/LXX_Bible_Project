# OT Review Pass 49

Scope: reader-facing footnote provenance cleanup.

- Replaced `Direct Logos export shows...` phrasing in reviewed translation footnotes with neutral witness wording.
- Added `clean_public_note_provenance()` to `scripts/sync_ot_support_text.py` so checkpoint regeneration keeps public footnotes neutral.
- Left internal decision rationales unchanged; those remain editorial audit data, not Bible note text.
- Removed `Logos` from the affected public `source_basis` field where it only named the provenance mechanism.
- Added a smoke-test guard so `translation_footnotes.csv` no longer publishes `Direct Logos export` wording.
