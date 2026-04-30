# NT Review Pass 186

Scope: 2 Peter focused queue rows after pass 185.

## 2 Peter 1:5
- status: `revised`
- decision: Render auto touto as "this very thing" and epichoregesate as "supply."

## 2 Peter 1:6
- status: `revised`
- decision: Correct egkrateian to "self-control" and hypomonen to "endurance."

## 2 Peter 1:18
- status: `revised`
- decision: Render phonen as "voice," enechtheisan as "brought," and orei as "mountain."

## 2 Peter 1:20
- status: `revised`
- decision: Render pases propheteias graphes as "no prophecy of Scripture" and idias epilyseos as "one's own interpretation."

## 2 Peter 2:2
- status: `revised`
- decision: Render apoleiais as "destructive ways" and blasphemethesetai as "shall be blasphemed."

## 2 Peter 2:5
- status: `revised`
- decision: Render archaiou kosmou as "ancient world" and ogdoon as "the eighth."

## 2 Peter 2:12
- status: `revised`
- decision: Render aloga as "irrational," halosin as "capture," and phthora terms as "corruption."

## 2 Peter 2:15
- status: `revised`
- decision: Render katalipontes as "having left," eutheian odon as "straight way," and misthon as singular "wage."

## 2 Peter 3:3
- status: `revised`
- decision: Render ep eschatou ton hemeron as "in the last days" and epithymias as "desires."

## 2 Peter 3:4
- status: `revised`
- decision: Retain "coming" for parousia and render houtos as "thus."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '2 Peter 1:5,2 Peter 1:6,2 Peter 1:18,2 Peter 1:20,2 Peter 2:2,2 Peter 2:5,2 Peter 2:12,2 Peter 2:15,2 Peter 3:3,2 Peter 3:4'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
