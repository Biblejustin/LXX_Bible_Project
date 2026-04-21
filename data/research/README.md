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
- `variant_notes.csv` = textual variant impact notes
- `translation_rules.md` = living style guide for the new translation

Suggested pilot:

- `Genesis 1-3`
- one Greek base text
- 2-3 lexicons
- 1 textual apparatus source
- one decision row per meaningful phrase
