# NT Review Pass 174

Scope: Hebrews 3-4 focused queue rows after pass 173, plus adjacent Hebrews 3:18.

## Hebrews 3:8
- status: `revised`
- decision: Modernize the prohibition and render peirasmou as "testing."

## Hebrews 3:9
- status: `revised`
- decision: Render hou as "where" and epeirasan as "tested."

## Hebrews 3:11
- status: `keep`
- decision: Retain the current oath wording as direct for the quotation formula.

## Hebrews 3:16
- status: `revised`
- decision: Restore the interrogative force: who provoked, was it not all who came out by Moses?

## Hebrews 3:18
- status: `revised`
- decision: Correct the generated garble and render apeithisasin as "those who disobeyed."

## Hebrews 3:19
- status: `revised`
- decision: Render kai as "and" and remove the unnecessary "in" after enter.

## Hebrews 4:1
- status: `revised`
- decision: Render kataleipomenis epangelias as "a promise remaining" and husterikenai as "have come short."

## Hebrews 4:3
- status: `revised`
- decision: Render hoi pisteusantes as "we who have believed" and keep the oath idiom as "They shall not enter."

## Hebrews 4:4
- status: `revised`
- decision: Render pou as "somewhere" and houtos as "in this way."

## Hebrews 4:5
- status: `revised`
- decision: Render the oath idiom as "They shall not enter into my rest."

## Hebrews 4:8
- status: `revised`
- decision: Render Iisous as "Joshua" in this context.

## Hebrews 4:9
- status: `revised`
- decision: Render sabbatismos as "Sabbath rest."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Hebrews 3:8,Hebrews 3:9,Hebrews 3:11,Hebrews 3:16,Hebrews 3:18,Hebrews 3:19,Hebrews 4:1,Hebrews 4:3,Hebrews 4:4,Hebrews 4:5,Hebrews 4:8,Hebrews 4:9'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
