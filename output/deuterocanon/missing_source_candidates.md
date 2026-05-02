# Missing LXX Deuterocanon Source Check

This note records source candidates checked for books still missing from the
separate Greek deuterocanon workspace.

## Current Missing Targets

| Code | Book | Current status |
| --- | --- | --- |
| MAN | Prayer of Manasseh | Not present as a separate book in the pinned eBible GRCLXX USFM archive. |
| 2MA | 2 Maccabees | Not present as 2 Maccabees in the pinned eBible GRCLXX USFM archive. The package file named `53-2MAgrclxx.usfm` identifies itself by title/content as 4 Maccabees. |

## Sources Checked

| Source | Result | Decision |
| --- | --- | --- |
| eBible GRCLXX details page, `https://ebible.org/details.php?id=grclxx` | The details page labels the text public domain and links the USFM archive used here. The package includes Prayer of Azariah/Song of the Three, Susanna, Bel, Psalm 151, and 4 Maccabees, but not a separate Prayer of Manasseh or 2 Maccabees file. | Keep as the pinned primary deuterocanon source for now. |
| CrossWire LXX module, `https://crosswire.org/sword/modules/ModInfo.jsp?modName=LXX` | Module notes say Prayer of Manasseh is in Odes 12, but distribution license is `Copyrighted; Free non-commercial distribution`. | Do not import into this CC-BY/open repo output without a clearer compatible source/license. |
| HakkaAC LXX Prayer of Manasses page, `https://hakkaac.org/Bible/Bible/ap/LXX/LXX-AP/LXX_Prayer-of-Manasses.html` | Page is English LXX2012 text, not Greek source rows. | Do not use as Greek source. |
| CCEL Swete volume 3 page, `https://www.ccel.org/ccel/swete/lxx3/htm/iii.htm` | Public-domain Swete volume metadata is available, but the accessible HTML page checked is front matter/page links rather than clean machine-readable Greek verse text. | Candidate only if we later build an OCR/page extraction path and verify rights and text quality. |

## Next Decision

Either leave MAN and 2MA absent from the first separate workstream, or choose a
compatible Greek source for those two books and add a second pinned importer.
