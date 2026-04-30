# Fresh Translation Research Workspace

Purpose:

- keep source-driven translation decisions separate from current study-Bible builder
- capture paraphrased Logos findings without storing credentials in repo
- track verse-level choices, alternates, and variant-impact notes

Rules:

- do not store usernames, passwords, cookies, session tokens, or exported secrets in repo
- do not paste large copyrighted chunks from lexicons or encyclopedias into tracked files
- store short citations, paraphrases, locations, and translation decisions
- put any sensitive local-only files under `data/research/local/` or another ignored path

Tracked files:

- `logos_notes.csv` = paraphrased lexicon / encyclopedia / apparatus notes
- `translation_decisions.csv` = chosen renderings by verse or phrase
- `translation_footnotes.csv` = public translation, textual, and comparison notes
- `variant_notes.csv` = textual variant impact notes
- `logos_translation_stack.json` = scoped OT/NT research-resource stack
- `translation_rules.md` = living style guide for the new translation

Current review scope:

- `data/raw/lxx_greek/ot_full.csv` = complete OT LXX source workspace
- `data/raw/tr_greek/nt_full.csv` = complete NT Scrivener TR source workspace
- record phrase-level decisions where wording is non-obvious or reused
- record public notes only when they help readers inspect the translation
- keep private Logos/local observations under ignored `data/research/local/`
