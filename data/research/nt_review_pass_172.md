# NT Review Pass 172

Scope: Philemon focused queue rows after pass 171, plus adjacent Philemon 1:6.

## Philemon 1:4
- status: `revised`
- decision: Restore the Greek word order with "always making mention."

## Philemon 1:6
- status: `revised`
- decision: Render koinonia as "fellowship," energes as "effective," and epignosei as "knowledge."

## Philemon 1:10
- status: `revised`
- decision: Render peri as "concerning," teknou as "child," and egenniisa as "begot."

## Philemon 1:11
- status: `revised`
- decision: Make the Onesimus wordplay direct: once useless, now useful.

## Philemon 1:14
- status: `revised`
- decision: Render gnomis as "consent," ithelesa as "wished," and hekousion as "willingly."

## Philemon 1:17
- status: `revised`
- decision: Render ei oun eme echeis koinonon as "If therefore you have me as a partner."

## Philemon 1:23
- status: `revised`
- decision: Render aspazontai se as "greets you" and remove the supplied "there."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Philemon 1:4,Philemon 1:6,Philemon 1:10,Philemon 1:11,Philemon 1:14,Philemon 1:17,Philemon 1:23'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
