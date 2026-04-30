# NT Review Pass 166

Scope: 1 Timothy 1-2 focused queue rows after pass 165, plus adjacent 2:12 quietness harmonization.

## 1 Timothy 1:8
- status: `revised`
- decision: Replace "if a man use it" with "if anyone uses it."

## 1 Timothy 1:9
- status: `revised`
- decision: Render nomos ou keitai as "law is not laid down" and modernize the offender list.

## 1 Timothy 1:13
- status: `revised`
- decision: Restore the first-person clause and render hybristen as "an insolent man."

## 1 Timothy 2:1
- status: `revised`
- decision: Render eucharistias as "thanksgivings" and smooth the first-of-all clause.

## 1 Timothy 2:2
- status: `revised`
- decision: Render hesychion as "tranquil" and semnoteti as "dignity."

## 1 Timothy 2:5
- status: `keep`
- decision: Retain the one God, one mediator, and man Christ Jesus wording as already direct.

## 1 Timothy 2:6
- status: `revised`
- decision: Render to martyrion kairois idiois as "the testimony in its own times."

## 1 Timothy 2:10
- status: `revised`
- decision: Remove the inherited parenthesis and render prepei as "befits."

## 1 Timothy 2:11
- status: `revised`
- decision: Render hesychia as "quietness" and hypotage as "submission."

## 1 Timothy 2:12
- status: `revised`
- decision: Harmonize hesychia as "quietness" with 2:11 and render authentein as "exercise authority."

## 1 Timothy 2:13
- status: `keep`
- decision: Retain the Adam and Eve order wording as already direct.

## 1 Timothy 2:14
- status: `revised`
- decision: Render the participle as "having been deceived" and gegonen as "came to be."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '1 Timothy 1:8,1 Timothy 1:9,1 Timothy 1:13,1 Timothy 2:1,1 Timothy 2:2,1 Timothy 2:5,1 Timothy 2:6,1 Timothy 2:10,1 Timothy 2:11,1 Timothy 2:12,1 Timothy 2:13,1 Timothy 2:14'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
