# NT Review Pass 183

Scope: James 3-5 focused queue rows after pass 182.

## James 3:7
- status: `revised`
- decision: Render enalion as "sea creatures" and te physei te anthropine as "by human nature."

## James 3:11
- status: `revised`
- decision: Render pege as "spring" and opes as "opening."

## James 3:15
- status: `revised`
- decision: Render psychike as "natural" and daimoniodes as "demonic."

## James 3:16
- status: `revised`
- decision: Render zelos as "jealousy," akatastasia as "disorder," and phaulos pragma as "evil practice."

## James 3:17
- status: `revised`
- decision: Render eupeithes as "easily entreated" and anypokritos as "without hypocrisy."

## James 4:7
- status: `keep`
- decision: Retain the current submit/resist wording as direct.

## James 4:9
- status: `revised`
- decision: Render kathepheian as "dejection."

## James 4:12
- status: `keep`
- decision: Retain the current one-lawgiver wording as direct.

## James 5:13
- status: `revised`
- decision: Render kakopathei as "suffering," euthymei as "cheerful," and psalleto as "sing praise."

## James 5:17
- status: `revised`
- decision: Render homoiopathes as "of like nature" and the rain duration with plain "for."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'James 3:7,James 3:11,James 3:15,James 3:16,James 3:17,James 4:7,James 4:9,James 4:12,James 5:13,James 5:17'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
