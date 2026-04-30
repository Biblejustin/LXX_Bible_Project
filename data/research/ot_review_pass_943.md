# OT Review Pass 943

Scope: cross-reference watch cleanup after full priority-suite refresh.

Status keys:
- `keep` = leave wording
- `revised` = wording changed in source or tracked review note

## Zechariah 9:9
- status: `keep`
- reason: Cross-references confirm the daughter-of-Zion king-coming context. Current wording preserves the vocatives, the saving/righteous king line, and the beast-of-burden/young-foal mount language already supported by reviewed decisions and guards.

## Daniel 6:23
- status: `keep`
- reason: Cross-references support Daniel's rescue-from-lions context. Current wording preserves the righteousness-before-God claim, the vocative to the king, and the lions' den for destruction.

## Ezekiel 4:14
- status: `keep`
- reason: Cross-references support the forbidden-food purity protest. Current wording keeps uncleanness, carrion/torn-by-beasts food, and stale flesh visible with reviewed notes.

## Ezekiel 18:5
- status: `keep`
- reason: Cross-references support the righteous-man judgment-and-righteousness formula. Current wording keeps the Greek man/righteous/judgment/righteousness sequence.

## Zechariah 11:6
- status: `keep`
- reason: Cross-references support the no-sparing judgment context. Current wording keeps inhabitants of the land, neighbor/king hands, and the no-rescue ending.

## Daniel 6:4
- status: `keep`
- reason: Cross-references support Daniel's blameless public service setting. Current wording preserves authority over the kingdom, holy spirit in him, and the king's plan to set him over the kingdom.

## Micah 6:5
- status: `keep`
- reason: Cross-references support the Balak/Balaam remembrance context. Current wording keeps the reeds-to-Gilgal phrase and righteousness-of-the-Lord purpose clause.

## Habakkuk 2:2
- status: `keep`
- reason: Cross-references support the write-the-vision context. Current wording keeps the tablet command and the one-reading-these-things may run clause.

## Zephaniah 1:9
- status: `keep`
- reason: Cross-references support judgment on the house-filling offenders. Current wording keeps the foregates, the house of the Lord their God, and impiety/deceit.

## Jonah 3:3
- status: `keep`
- reason: Cross-references are loose but do not require wording change. Current wording preserves Jonah's rising, the Lord's speech, and the three-days journey-of-a-way phrase.

## Lamentations 2:2
- status: `keep`
- reason: Cross-references support the no-sparing destruction context. Current wording keeps submerged, beautiful things of Jacob, strongholds of daughter Judah, and profaned king/rulers.

## Lamentations 2:7
- status: `keep`
- reason: Cross-references support sanctuary rejection and enemy destruction. Current wording keeps cast-off altar, shaken-off sanctuary, enemy-hand palace wall, and feast-day voice.

## Obadiah 1:18
- status: `keep`
- reason: Cross-references support the fire/stubble judgment on Esau. Current wording keeps Jacob as fire, Joseph as flame, Esau as stubble, and the grain-bearer phrase.

## Lamentations 1:18
- status: `keep`
- reason: Cross-references support the righteous-Lord confession and captivity setting. Current wording keeps the provoked-his-mouth idiom and the pain/captivity lines.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament ot --refs 'Zechariah 9:9,Daniel 6:23,Ezekiel 4:14,Ezekiel 18:5,Zechariah 11:6,Daniel 6:4,Micah 6:5,Habakkuk 2:2,Zephaniah 1:9,Jonah 3:3,Lamentations 2:2,Lamentations 2:7,Obadiah 1:18,Lamentations 1:18'` passed.
- Focused smoke tests passed.
- Full aggregate/DOCX checkpoint intentionally deferred for batch boundary.
