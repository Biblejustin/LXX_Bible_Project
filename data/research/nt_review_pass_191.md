# NT Review Pass 191

Scope: Revelation 1-3 focused queue rows after pass 190.

## Revelation 1:12
- status: `revised`
- decision: Render lychniais as "lampstands" and epistrepsas as "having turned."

## Revelation 1:14
- status: `keep`
- decision: Retain the current white-wool/snow and flame-of-fire wording as direct.

## Revelation 1:16
- status: `revised`
- decision: Render echon as "having," ekporeuomene as "proceeding," and opsis as "appearance."

## Revelation 1:19
- status: `revised`
- decision: Render eides as "saw" and mellei ginesthai as "are about to happen."

## Revelation 2:6
- status: `revised`
- decision: Render erga as "works" while retaining Nicolaitanes.

## Revelation 2:27
- status: `revised`
- decision: Render poimanei as "shall shepherd" and syntribetai as "are broken to pieces."

## Revelation 2:28
- status: `keep`
- decision: Retain the current morning-star wording as direct.

## Revelation 3:2
- status: `revised`
- decision: Render ginou gregoron as "Become watchful," ta loipa as "remaining things," and pepleromena as "fulfilled."

## Revelation 3:3
- status: `revised`
- decision: Render terei as "keep" and ou me gnos as "shall by no means know."

## Revelation 3:15
- status: `revised`
- decision: Render ophelon as "I wish."

## Revelation 3:16
- status: `revised`
- decision: Render mello as "I am about to" and emesai as "vomit."

## Revelation 3:19
- status: `revised`
- decision: Render elegcho as "reprove" and paideuo as "discipline."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Revelation 1:12,Revelation 1:14,Revelation 1:16,Revelation 1:19,Revelation 2:6,Revelation 2:27,Revelation 2:28,Revelation 3:2,Revelation 3:3,Revelation 3:15,Revelation 3:16,Revelation 3:19'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
