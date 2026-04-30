# NT Review Pass 190

Scope: Jude focused queue rows after pass 189.

## Jude 1:8
- status: `revised`
- decision: Render enypniazomenoi as "dreaming," kyrioteta as "lordship," and doxas as "glories."

## Jude 1:15
- status: `revised`
- decision: Render exelegxai as "convict" and skleron as "harsh things."

## Jude 1:16
- status: `revised`
- decision: Render epithymias as "desires," hyperogka as "swelling things," and opheleias charin as "for advantage."

## Jude 1:18
- status: `revised`
- decision: Render eschato chrono as "last time" and epithymias as "desires."

## Jude 1:22
- status: `revised`
- decision: Render eleeite as "have mercy" and diakrinomenoi as "making a distinction."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Jude 1:8,Jude 1:15,Jude 1:16,Jude 1:18,Jude 1:22'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
