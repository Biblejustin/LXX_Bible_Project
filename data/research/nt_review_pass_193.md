# NT Review Pass 193

Scope: Revelation 7-8 focused queue rows after pass 192.

## Revelation 7:1
- status: `revised`
- decision: Render hina me pnee anemos as "that no wind should blow."

## Revelation 7:2
- status: `revised`
- decision: Render apo anatoles heliou as "from the rising of the sun," phone megale as "great voice," and adikesai as "harm."

## Revelation 7:7
- status: `keep`
- decision: Retain the current tribe/sealed wording as direct.

## Revelation 7:16
- status: `revised`
- decision: Render pese as "fall upon" and kauma as "burning heat."

## Revelation 8:1
- status: `revised`
- decision: Remove supplied "space of" and use "about half an hour."

## Revelation 8:5
- status: `revised`
- decision: Render ek tou pyros as "from the fire" and brontai as "thunders."

## Revelation 8:9
- status: `revised`
- decision: Render to triton as "the third" and ta echonta psychas as "those having life."

## Revelation 8:10
- status: `revised`
- decision: Render pegas hydaton as "springs of waters" and remove supplied "as it were."

## Revelation 8:11
- status: `revised`
- decision: Render polloi anthropon as "many of men" and ek ton hydaton as "from the waters."

## Revelation 8:12
- status: `revised`
- decision: Render eplege as "was struck" and hina skotisthe as "so that ... might be darkened."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Revelation 7:1,Revelation 7:2,Revelation 7:7,Revelation 7:16,Revelation 8:1,Revelation 8:5,Revelation 8:9,Revelation 8:10,Revelation 8:11,Revelation 8:12'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
