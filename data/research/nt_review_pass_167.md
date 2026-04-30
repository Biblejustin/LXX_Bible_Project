# NT Review Pass 167

Scope: 1 Timothy 3-4 focused queue rows after pass 166.

## 1 Timothy 3:3
- status: `revised`
- decision: Render plekten as "striker," aischrokerde as "greedy for shameful gain," epieike as "gentle," amachon as "peaceable," and aphilargyron as "not loving money."

## 1 Timothy 3:4
- status: `revised`
- decision: Render proistamenon as "ruling," hypotage as "submission," and semnotetos as "dignity."

## 1 Timothy 3:9
- status: `keep`
- decision: Retain the current mystery of the faith and pure conscience wording as direct.

## 1 Timothy 3:11
- status: `revised`
- decision: Remove supplied "their" from "wives" and render semnas as "dignified."

## 1 Timothy 4:2
- status: `revised`
- decision: Render the phrase as "in hypocrisy of liars" and keep the seared conscience wording without the supplied hot iron.

## 1 Timothy 4:4
- status: `revised`
- decision: Render apobleton as "rejected" and the participle as "being received."

## 1 Timothy 4:11
- status: `revised`
- decision: Restore the Greek word order: command and teach these things.

## 1 Timothy 4:13
- status: `revised`
- decision: Modernize "Till" and render proseche as "give attention."

## 1 Timothy 4:14
- status: `revised`
- decision: Modernize "Neglect not" and render dia propheteias as "through prophecy."

## 1 Timothy 4:15
- status: `revised`
- decision: Render meleta as "practice," en toutois isthi as "be in them," and prokope as "progress."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '1 Timothy 3:3,1 Timothy 3:4,1 Timothy 3:9,1 Timothy 3:11,1 Timothy 4:2,1 Timothy 4:4,1 Timothy 4:11,1 Timothy 4:13,1 Timothy 4:14,1 Timothy 4:15'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
