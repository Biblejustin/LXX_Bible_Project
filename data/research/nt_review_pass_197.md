# NT Review Pass 197

Scope: Revelation 13-14 focused queue rows after pass 196.

## Revelation 13:1
- status: `revised`
- decision: Render anabainon as "ascending," diademata as "diadems," and onoma blasphemias as "a name of blasphemy."

## Revelation 13:3
- status: `revised`
- decision: Render esphagmenen eis thanaton as "having been slain to death" and ge as "earth."

## Revelation 13:11
- status: `revised`
- decision: Render anabainon as "ascending" and keep the lamb/dragon contrast direct.

## Revelation 13:13
- status: `revised`
- decision: Render semeia megala as "great signs" and enopion ton anthropon as "before men."

## Revelation 14:2
- status: `revised`
- decision: Render kitharodon kitharizonton as "harpists playing" and keep the repeated voice imagery.

## Revelation 14:5
- status: `revised`
- decision: Render dolos as "deceit" and amomoi as "blameless."

## Revelation 14:17
- status: `revised`
- decision: Retain the temple-in-heaven line with direct word order.

## Revelation 14:19
- status: `revised`
- decision: Render ebalen as "cast," etrygesen as "harvested," and preserve the great-winepress image.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Revelation 13:1,Revelation 13:3,Revelation 13:11,Revelation 13:13,Revelation 14:2,Revelation 14:5,Revelation 14:17,Revelation 14:19'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
