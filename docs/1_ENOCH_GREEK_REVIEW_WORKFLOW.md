# 1 Enoch Greek Fragment Review Workflow

The 1 Enoch Greek-fragment workstream is a source-audit workflow, not a Bible
source import yet.

## Generated Queues

- `data/research/1_enoch_charles_1912_greek_ocr_audit.csv`: all Greek-heavy OCR
  lines in Charles 1912.
- `data/research/1_enoch_charles_1912_greek_ocr_priority.csv`: high-density
  Greek lines in the Greek-fragment text section.
- `data/research/1_enoch_greek_fragment_ref_review.csv`: grouped review queue
  with best-effort 1 Enoch references, printed-page hints, PDF-page hints, and
  nearby Charles Ethiopic-base witness text.

Run:

```sh
make build-enoch-witness
```

## Page Image Check

The Charles 1912 Internet Archive PDF is a review cache, not a tracked source
artifact.

```sh
mkdir -p output/enoch/cache output/enoch/page_images
curl -L -o output/enoch/cache/bookofenochor1en00char.pdf \
  https://archive.org/download/bookofenochor1en00char/bookofenochor1en00char.pdf

for p in 389 393 411 417 419 421; do
  pdftoppm -f "$p" -l "$p" -png -r 180 \
    output/enoch/cache/bookofenochor1en00char.pdf \
    "output/enoch/page_images/charles1912_pdf_page_${p}"
done
```

The current review queue maps Charles printed pages 272, 276, 294, 300, 302,
and 304 to PDF pages 389, 393, 411, 417, 419, and 421.

## Review Rule

Do not import OCR lines directly. For each grouped row, check the page image,
correct OCR mistakes manually, then compare the Greek fragment with the Charles
Ethiopic-base witness row before drafting any appendix wording.
