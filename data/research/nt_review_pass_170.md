# NT Review Pass 170

Scope: 2 Timothy 3-4 focused queue rows after pass 169.

## 2 Timothy 3:1
- status: `revised`
- decision: Render touto de ginoske as "But know this" and chalepoi as "difficult."

## 2 Timothy 3:2
- status: `revised`
- decision: Render philautoi as "lovers of themselves" and philargyroi as "lovers of money."

## 2 Timothy 3:3
- status: `revised`
- decision: Render aspondoi as "implacable," diaboloi as "slanderers," akrateis as "without self-control," and aphilagathoi as "not lovers of good."

## 2 Timothy 3:4
- status: `revised`
- decision: Render propeteis as "reckless," tetuphomenoi as "puffed up," and philedonoi as "lovers of pleasure."

## 2 Timothy 3:7
- status: `revised`
- decision: Modernize "ever learning" as "always learning."

## 2 Timothy 3:8
- status: `revised`
- decision: Render hon tropon as "in the same way," katephtharmenoi ton noun as "corrupted in mind," and adokimoi as "unapproved."

## 2 Timothy 3:13
- status: `revised`
- decision: Render goites as "impostors" and prokopsousin epi to cheiron as "will advance to worse."

## 2 Timothy 3:14
- status: `revised`
- decision: Render mene as "continue" and para tinos as "from whom."

## 2 Timothy 3:16
- status: `revised`
- decision: Render theopneustos as "God-breathed" and didaskalia as "teaching."

## 2 Timothy 4:3
- status: `revised`
- decision: Render didaskalia as "teaching" and kata tas epithumias tas idias as "according to their own lusts."

## 2 Timothy 4:5
- status: `revised`
- decision: Render niphe as "be sober," kakopathison as "endure hardship," and plirophorison as "fulfill."

## 2 Timothy 4:6
- status: `revised`
- decision: Render spendomai as "being poured out" and ephestiken as "has come."

## 2 Timothy 4:7
- status: `revised`
- decision: Restore the article in "the good fight" and "the course."

## 2 Timothy 4:11
- status: `revised`
- decision: Render euchristos as "useful" and keep the ministry phrase direct.

## 2 Timothy 4:12
- status: `revised`
- decision: Modernize the inverted "Tychicus have I sent" while preserving the aorist.

## 2 Timothy 4:19
- status: `revised`
- decision: Render aspasai as "greet."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '2 Timothy 3:1,2 Timothy 3:2,2 Timothy 3:3,2 Timothy 3:4,2 Timothy 3:7,2 Timothy 3:8,2 Timothy 3:13,2 Timothy 3:14,2 Timothy 3:16,2 Timothy 4:3,2 Timothy 4:5,2 Timothy 4:6,2 Timothy 4:7,2 Timothy 4:11,2 Timothy 4:12,2 Timothy 4:19'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
