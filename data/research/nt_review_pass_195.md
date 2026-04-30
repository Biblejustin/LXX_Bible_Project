# NT Review Pass 195

Scope: Revelation 10-11 focused queue rows after pass 194.

## Revelation 10:1
- status: `revised`
- decision: Render katabainonta as "coming down" and remove supplied "as it were" before the sun comparison.

## Revelation 10:2
- status: `revised`
- decision: Render biblaridion as "little scroll" and aneogmenon as "opened."

## Revelation 10:3
- status: `revised`
- decision: Render phone megale as "great voice" and elalesan as "spoke."

## Revelation 10:10
- status: `revised`
- decision: Render biblaridion as "little scroll" and epikranthe as "was made bitter."

## Revelation 11:4
- status: `revised`
- decision: Render lychniai as "lampstands."

## Revelation 11:6
- status: `revised`
- decision: Render exousia as "authority," hina me breche huetos as "that no rain should rain," and pasa plege as "every plague."

## Revelation 11:7
- status: `revised`
- decision: Render abyssos as "abyss" and polemon met auton as "war with them."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Revelation 10:1,Revelation 10:2,Revelation 10:3,Revelation 10:10,Revelation 11:4,Revelation 11:6,Revelation 11:7'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
