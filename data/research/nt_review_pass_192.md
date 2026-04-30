# NT Review Pass 192

Scope: Revelation 4-6 focused queue rows after pass 191.

## Revelation 4:7
- status: `revised`
- decision: Render zoon as "living creature" rather than beast and preserve the four comparisons.

## Revelation 5:11
- status: `revised`
- decision: Render zoon as "living creatures," kykloθεν as "around," and myriades myriadon as "myriads of myriads."

## Revelation 6:1
- status: `revised`
- decision: Render zoon as "living creatures" and keep the thunder-voice phrase direct.

## Revelation 6:3
- status: `revised`
- decision: Render zoon as "living creature" and remove the supplied pluperfect.

## Revelation 6:7
- status: `revised`
- decision: Render zoon as "living creature" and phone as "voice."

## Revelation 6:14
- status: `revised`
- decision: Render apechoristhe as "was separated" and heilissomenon as "being rolled up."

## Revelation 6:15
- status: `revised`
- decision: Render megistanes as "great ones," chiliarchoi as "commanders of thousands," doulos as "slave," and spelaia as "caves."

## Revelation 6:17
- status: `revised`
- decision: Render dynatai as present "is able."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Revelation 4:7,Revelation 5:11,Revelation 6:1,Revelation 6:3,Revelation 6:7,Revelation 6:14,Revelation 6:15,Revelation 6:17'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
