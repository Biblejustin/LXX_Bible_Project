# NT Review Pass 182

Scope: James 1-2 focused queue rows after pass 181.

## James 1:3
- status: `revised`
- decision: Render dokimion as "testing" and hupomonen as "endurance."

## James 1:5
- status: `revised`
- decision: Render leipetai as "lacks," aplos as "generously," and me oneidizontos as "does not reproach."

## James 1:8
- status: `revised`
- decision: Hyphenate "double-minded" and retain the unstable-ways clause.

## James 1:9
- status: `revised`
- decision: Render tapeinos as "lowly" and kauchastho as "boast."

## James 1:10
- status: `revised`
- decision: Carry the implied "boast" thought and render tapeinosei as "humiliation."

## James 1:14
- status: `revised`
- decision: Render hekastos as "each one" and epithumias as "desire."

## James 1:17
- status: `revised`
- decision: Render dosis as "giving," dorema as "gift," and parallage as "variation."

## James 1:20
- status: `revised`
- decision: Modernize the word order while retaining "works" for katergazetai.

## James 1:24
- status: `revised`
- decision: Render katanoesen as "observed" and hopoios as "what kind."

## James 1:27
- status: `revised`
- decision: Render orphanous as "orphans" and aspilon as "unstained."

## James 2:13
- status: `revised`
- decision: Render krisis as "judgment," anileos as "without mercy," and katakauchatai as "boasts over."

## James 2:15
- status: `revised`
- decision: Modernize the condition and render leipomenoi as "lacking."

## James 2:17
- status: `revised`
- decision: Render kath heauten as "by itself."

## James 2:20
- status: `revised`
- decision: Render kenos as "empty" and keep the TR reading "dead."

## James 2:21
- status: `revised`
- decision: Render anenegkas as "having offered."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'James 1:3,James 1:5,James 1:8,James 1:9,James 1:10,James 1:14,James 1:17,James 1:20,James 1:24,James 1:27,James 2:13,James 2:15,James 2:17,James 2:20,James 2:21'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
