# NT Review Pass 150

Scope: 2 Corinthians 12-13 focused queue rows after pass 149.

## 2 Corinthians 12:3
- status: `keep`
- decision: Keep the current "such a man" wording; it is clear and consistent with 12:2.

## 2 Corinthians 12:7
- status: `revised`
- decision: Render te hyperbole ton apokalypseon as the surpassing greatness of the revelations and remove the inherited article before "messenger of Satan."

## 2 Corinthians 12:10
- status: `revised`
- decision: Render astheneiais as "weaknesses" for consistency with nearby verses and remove the inherited inversion at the end.

## 2 Corinthians 12:15
- status: `revised`
- decision: Restore "your souls" for psychon hymon and strengthen ekdapanethesomai as "be fully spent."

## 2 Corinthians 12:16
- status: `revised`
- decision: Replace "nevertheless" with "but" and render elabon dolo as "took you by deceit."

## 2 Corinthians 13:4
- status: `keep`
- decision: Keep the current crucified-through-weakness wording; it is clear and close.

## 2 Corinthians 13:8
- status: `keep`
- decision: Keep the current truth clause; it is already literal and clear.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '2 Corinthians 12:3,2 Corinthians 12:7,2 Corinthians 12:10,2 Corinthians 12:15,2 Corinthians 12:16,2 Corinthians 13:4,2 Corinthians 13:8'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
