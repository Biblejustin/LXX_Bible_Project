# NT Review Pass 164

Scope: 1 Thessalonians focused queue rows after pass 163.

## 1 Thessalonians 1:2
- status: `keep`
- decision: Retain the current thanksgiving and prayer wording as already clear and close to the Greek.

## 1 Thessalonians 2:3
- status: `revised`
- decision: Render ek planes as "from error" and modernize "guile" to "deceit."

## 1 Thessalonians 2:6
- status: `revised`
- decision: Remove inverted inherited word order and keep the apostolic burden clause explicit.

## 1 Thessalonians 2:7
- status: `revised`
- decision: Render trophos as "nursing mother" and preserve her own children.

## 1 Thessalonians 3:10
- status: `revised`
- decision: Render katartisai as "complete" and ta hysteremata as "the things lacking."

## 1 Thessalonians 5:3
- status: `revised`
- decision: Render the present saying clause directly and odin as birth pains upon a pregnant woman.

## 1 Thessalonians 5:6
- status: `revised`
- decision: Render hoi loipoi as "the rest" and keep watch/sober language.

## 1 Thessalonians 5:10
- status: `revised`
- decision: Match gregoromen with the local "watch" wording rather than "wake."

## 1 Thessalonians 5:16
- status: `revised`
- decision: Modernize pantote as "always" rather than inherited "evermore."

## 1 Thessalonians 5:17
- status: `keep`
- decision: Retain "Pray without ceasing" as direct and idiomatic.

## 1 Thessalonians 5:20
- status: `revised`
- decision: Modernize the imperative and render propheteias as "prophecies."

## 1 Thessalonians 5:21
- status: `revised`
- decision: Render dokimazete as "test" and to kalon as "the good."

## 1 Thessalonians 5:22
- status: `revised`
- decision: Render eidous ponerou as "form of evil" rather than inherited "appearance of evil."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '1 Thessalonians 1:2,1 Thessalonians 2:3,1 Thessalonians 2:6,1 Thessalonians 2:7,1 Thessalonians 3:10,1 Thessalonians 5:3,1 Thessalonians 5:6,1 Thessalonians 5:10,1 Thessalonians 5:16,1 Thessalonians 5:17,1 Thessalonians 5:20,1 Thessalonians 5:21,1 Thessalonians 5:22'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
