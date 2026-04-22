# Source Provenance

This file pins the tracked source artifacts used by the current workspace. Keep
it updated whenever raw source archives or imported CSV files change.

## Raw Archives

| Path | Role | Upstream | Status | SHA-256 |
| --- | --- | --- | --- | --- |
| `data/raw/eng-Brenton_usfm.zip` | Brenton 1851 LXX English USFM archive used by legacy comparison/prototype tooling | `https://ebible.org/Scriptures/eng-Brenton_usfm.zip`; details page `https://ebible.org/find/details.php?all=1&id=eng-Brenton`; verified 2026-04-22 | Public domain source text | `b1380a21d81103a7c6a1a379e6f3734acf8dcb25bd345cb91eaaa1087aba5c4a` |
| `data/raw/SF_2009-01-20_ENG_UKJV_(UPDATED KING JAMES VERSION).zip` | UKJV XML witness and NT seed text | SourceForge Zefania path `https://sourceforge.net/projects/zefania-sharp/files/Bibles/ENG/King%20James/Updated%20King%20James%20Version/`; verified 2026-04-22 | Public domain; credit line in `NOTICE.md` | `c4e998d53e595d317d60893accb0298ccef20f9a544ee8f7af85c84eca8987cf` |
| `data/raw/TSK.zip` | Treasury of Scripture Knowledge cross-reference apparatus | CrossWire beta module page `https://www2.crosswire.org/sword/modules/ModInfo.jsp?beta=true&modName=TSK`; raw download servlet `https://www.crosswire.org/sword/servlet/SwordMod.Verify?beta=true&modName=TSK&pkgType=raw`; verified 2026-04-22 | Public-domain CrossWire module distribution, version 1.5 | `53a94765a3b5a528249990a552aa639f00bb265548b84214343fb8de9db27557` |
| `data/raw/cross-references.zip` | OpenBible cross-reference support layer | `https://a.openbible.info/data/cross-references.zip`; page `https://www.openbible.info/labs/cross-references/`; verified 2026-04-22 | CC-BY data layer; TSK remains primary public output layer | `a4636893d50cae6191ca35a07bb65b2091a6d97990f61c169ee43d01af7b943c` |
| `data/raw/1_enoch_charles_1917.txt` | R. H. Charles 1917 1 Enoch source | Local public-domain text file; upstream URL not pinned yet | Public domain in the United States | `54ef78037e6ff4fb9831a5278c8c0e0d77622e4edc5325a080808efa66605c37` |
| `data/raw/hitchcock_bible_names.txt` | Hitchcock name meanings | CCEL public-domain text; upstream URL not pinned yet | Public domain CCEL text | `95d6eb253e4237ba198bb4ee92b4de9bccfab69fe7775eb82134444d44b2e850` |

## Textus Receptus Source

- Source: Scrivener 1894 Textus Receptus text-only files.
- Upstream repository: <https://github.com/byztxt/greektext-scrivener>
- Pinned commit: `6049a43b135ed870f843b83eb6a04764fc796678`
- Raw base:
  <https://raw.githubusercontent.com/byztxt/greektext-scrivener/6049a43b135ed870f843b83eb6a04764fc796678/textonly>
- Upstream license notice: `Public Domain. Copy freely.`
- Manifest: `data/raw/tr_greek/source_manifest.json`
- Imported CSV: `data/raw/tr_greek/nt_full.csv`
- Imported row count: 7,957

## Fresh Translation Sources

| Path | Role | Rows |
| --- | --- | ---: |
| `data/raw/lxx_greek/ot_full.csv` | LXX Greek OT fresh translation workspace | 22,896 |
| `data/raw/lxx_greek/genesis_full.csv` | Genesis fresh translation workspace | 1,533 |
| `data/raw/lxx_greek/genesis_1_3_pilot.csv` | Genesis 1-3 pilot worksheet | 80 |
| `data/raw/tr_greek/nt_full.csv` | TR Greek NT fresh translation workspace with UKJV witness column | 7,957 |

## Apparatus And Review Data

| Path | Role |
| --- | --- |
| `data/research/translation_decisions.csv` | Phrase and verse-level translation decisions |
| `data/research/translation_footnotes.csv` | Public footnote source table |
| `data/research/variant_notes.csv` | Selective textual variant notes |
| `data/proper_names.csv` | Curated proper-name notes |
| `data/proper_name_transliteration_notes.csv` | Generated Greek/LXX/TR name and place notes |
| `data/names_of_god.csv` | Divine-name and title notes |
| `data/versification/lxx_to_eng_map.json` | LXX-to-English versification bridge, derived from `versification-utils` |

## Gaps To Close Before Public Release

- Add exact upstream URL and retrieval date for `data/raw/1_enoch_charles_1917.txt`.
- Add exact upstream URL and retrieval date for `data/raw/hitchcock_bible_names.txt`.
- Re-download raw archives in a clean release workspace and confirm hashes still
  match this file.
