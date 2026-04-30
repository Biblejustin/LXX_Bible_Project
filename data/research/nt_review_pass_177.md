# NT Review Pass 177

Scope: Hebrews 9 focused queue rows after pass 176, plus adjacent Hebrews 9:20.

## Hebrews 9:3
- status: `revised`
- decision: Render hagia hagion as "Holy of Holies."

## Hebrews 9:5
- status: `revised`
- decision: Use "cherubim" and render kata meros as "in detail."

## Hebrews 9:6
- status: `revised`
- decision: Render kateskeuasmenon as "having been thus prepared" and latreias as "services."

## Hebrews 9:7
- status: `revised`
- decision: Restore the present-tense entry/offering verbs and render agnoimaton as "ignorances."

## Hebrews 9:12
- status: `revised`
- decision: Render ephapax as "once for all," ta hagia as "the holy places," and remove the supplied "for us."

## Hebrews 9:19
- status: `revised`
- decision: Render lalitheisis as "had been spoken" and auto te to biblion as "the book itself."

## Hebrews 9:20
- status: `revised`
- decision: Remove unsupported "with authority" from eneteilato.

## Hebrews 9:21
- status: `revised`
- decision: Render skeui tis leitourgias as "vessels of the service."

## Hebrews 9:23
- status: `revised`
- decision: Render hupodeigmata as "copies" and tighten the purification clause.

## Hebrews 9:24
- status: `revised`
- decision: Render antitupa as "copies" and to prosopo tou theou as "before the face of God."

## Hebrews 9:25
- status: `revised`
- decision: Render ta hagia as "the holy places" and haimati allotrio as "another's blood."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Hebrews 9:3,Hebrews 9:5,Hebrews 9:6,Hebrews 9:7,Hebrews 9:12,Hebrews 9:19,Hebrews 9:20,Hebrews 9:21,Hebrews 9:23,Hebrews 9:24,Hebrews 9:25'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
