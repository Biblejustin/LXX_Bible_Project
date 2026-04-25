.PHONY: setup test build-ot checkpoint-ot build-ot-review build-nt clean-working

PYTHON ?= python3

setup:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m compileall -q scripts
	$(PYTHON) -m pytest -q

build-ot:
	$(PYTHON) scripts/run_book_checkpoint.py

checkpoint-ot:
	$(PYTHON) scripts/run_book_checkpoint.py --diff-check --smoke-test

build-ot-review:
	$(PYTHON) scripts/run_priority_review_suite.py

build-nt:
	$(PYTHON) scripts/apply_nt_tr_literal_revision.py
	$(PYTHON) scripts/build_nt_tr_vs_ukjv_review.py
	$(PYTHON) scripts/build_fresh_translation.py --source data/raw/tr_greek/nt_full.csv --output output/fresh_translation_nt_tr_full.md --translation-only-output output/fresh_translation_nt_tr_translation_only.md --diagnostics output/fresh_translation_nt_tr_diagnostics.json
	$(PYTHON) scripts/build_fresh_logos_bible.py --testament nt --source data/raw/tr_greek/nt_full.csv --logos-docx output/logos_nt/fresh_translation_nt_tr_logos_bible.docx --mt-bridge-docx output/logos_nt/fresh_translation_nt_tr_reference_notes.docx --proof-docx output/logos_nt/fresh_translation_nt_tr_proofreading.docx --diagnostics output/logos_nt/fresh_translation_nt_tr_diagnostics.json --readme output/logos_nt/README.md --preview output/logos_nt/fresh_translation_nt_tr_preview.md

clean-working:
	rm -rf output/working
