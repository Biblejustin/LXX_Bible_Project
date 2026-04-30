# NT Review Pass 171

Scope: Titus focused queue rows after pass 170.

## Titus 1:2
- status: `revised`
- decision: Render pro chronon aionion as "before eternal times" instead of "before the world began."

## Titus 1:5
- status: `revised`
- decision: Modernize the inverted clause and render katastises as "appoint."

## Titus 1:6
- status: `revised`
- decision: Render ei tis as "if anyone" and asotia/anupotakta as "dissipation or insubordination."

## Titus 1:8
- status: `revised`
- decision: Correct philagathon from "lover of good men" to "lover of good" and render egkrate as "self-controlled."

## Titus 1:10
- status: `revised`
- decision: Render anupotaktoi as "unruly men" and malista as "especially."

## Titus 1:11
- status: `revised`
- decision: Render anatrepousin as "overturn" and aischrou kerdous as "shameful gain," removing the unsupported "illegal."

## Titus 1:12
- status: `revised`
- decision: Render Kretes as "Cretans" and gasteres argai as "idle bellies."

## Titus 1:14
- status: `revised`
- decision: Tie apostrephomenon to "men who turn away from the truth."

## Titus 2:1
- status: `revised`
- decision: Render prepei as "befit" and didaskalia as "teaching."

## Titus 2:4
- status: `revised`
- decision: Render sophronizosin as "train" and keep the husband/children love clauses direct.

## Titus 2:6
- status: `revised`
- decision: Render tous neoterous as "the younger men" and sophronein as "be sober-minded."

## Titus 2:7
- status: `revised`
- decision: Render didaskalia as "teaching," semnotita as "dignity," and keep the good-works pattern.

## Titus 2:11
- status: `revised`
- decision: Render soterios as "saving."

## Titus 2:12
- status: `revised`
- decision: Render en to nyn aioni as "in the present age" instead of "in this present world."

## Titus 3:1
- status: `revised`
- decision: Render archais kai exousiais as "rulers and authorities" and peitharchein as "to obey."

## Titus 3:9
- status: `revised`
- decision: Render machas nomikas as "fights about the law" and anopheleis as "unprofitable."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Titus 1:2,Titus 1:5,Titus 1:6,Titus 1:8,Titus 1:10,Titus 1:11,Titus 1:12,Titus 1:14,Titus 2:1,Titus 2:4,Titus 2:6,Titus 2:7,Titus 2:11,Titus 2:12,Titus 3:1,Titus 3:9'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
