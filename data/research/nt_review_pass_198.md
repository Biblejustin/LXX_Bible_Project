# NT Review Pass 198

Scope: Revelation 15-17 focused queue rows after pass 197.

## Revelation 15:6
- status: `revised`
- decision: Render lampron as "bright" and zonas as "belts."

## Revelation 16:16
- status: `revised`
- decision: Render Hebraisti as "in Hebrew" and keep Armageddon.

## Revelation 16:18
- status: `revised`
- decision: Render aph hou hoi anthropoi egenonto as "since men came to be" and keep the double earthquake emphasis.

## Revelation 16:20
- status: `keep`
- decision: Retain the current island/mountain wording as direct.

## Revelation 17:9
- status: `revised`
- decision: Remove supplied "And" and render hopou as "where."

## Revelation 17:10
- status: `revised`
- decision: Render epesan as "have fallen" and oligon as "a short time."

## Revelation 17:12
- status: `revised`
- decision: Render exousia as "authority" and mian horan as "for one hour."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Revelation 15:6,Revelation 16:16,Revelation 16:18,Revelation 16:20,Revelation 17:9,Revelation 17:10,Revelation 17:12'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
