# NT Review Pass 196

Scope: Revelation 12 focused queue rows after pass 195.

## Revelation 12:1
- status: `revised`
- decision: Render semeion as "sign" and hypokato as "underneath."

## Revelation 12:2
- status: `revised`
- decision: Render en gastri echousa as "having in the womb" and odinousa/basanizomene as participles.

## Revelation 12:6
- status: `revised`
- decision: Render apo tou theou as "from God," trephosin as "nourish," and modernize the day count.

## Revelation 12:7
- status: `revised`
- decision: Retain the war-in-heaven wording with modern punctuation.

## Revelation 12:9
- status: `revised`
- decision: Render ophis ho archaios as "ancient serpent" and oikoumene as "inhabited world."

## Revelation 12:14
- status: `revised`
- decision: Render tou aetou tou megalou as "the great eagle" and eis ton topon as "to her place."

## Revelation 12:15
- status: `revised`
- decision: Render potamon as "river" and potamophoreton as "carried away by the river."

## Revelation 12:16
- status: `revised`
- decision: Render potamon as "river" and keep the earth-mouth image direct.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Revelation 12:1,Revelation 12:2,Revelation 12:6,Revelation 12:7,Revelation 12:9,Revelation 12:14,Revelation 12:15,Revelation 12:16'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
