# NT Review Pass 187

Scope: 1 John 1-3 focused queue rows after pass 186.

## 1 John 1:6
- status: `revised`
- decision: Render poiein ten aletheian as "practice the truth."

## 1 John 1:8
- status: `keep`
- decision: Retain the current no-sin/deceive-ourselves wording as direct.

## 1 John 1:9
- status: `keep`
- decision: Retain the current confess/faithful/just wording as direct.

## 1 John 2:16
- status: `revised`
- decision: Render epithymia as "desire" and ek tou patros as "from the Father."

## 1 John 2:25
- status: `revised`
- decision: Remove supplied "even" and render ten zoen ten aionion as "the eternal life."

## 1 John 2:28
- status: `revised`
- decision: Render menete as "remain" and phanerothe as "is manifested."

## 1 John 3:2
- status: `revised`
- decision: Render tekna theou as "children of God" and ephanerothe as "has not yet been manifested."

## 1 John 3:3
- status: `revised`
- decision: Render pas ho echon as "everyone who has" and keep the hope set on him explicit.

## 1 John 3:20
- status: `revised`
- decision: Modernize kataginoske as "condemns."

## 1 John 3:21
- status: `revised`
- decision: Modernize the negative heart/condemn clause.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '1 John 1:6,1 John 1:8,1 John 1:9,1 John 2:16,1 John 2:25,1 John 2:28,1 John 3:2,1 John 3:3,1 John 3:20,1 John 3:21'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
