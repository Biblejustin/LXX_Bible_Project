.PHONY: setup test csv-check build-fresh build-ot checkpoint-ot review-ot-fast build-ot-review build-nt build-nt-fast build-nt-book review-nt-fast build-combined build-combined-logos build-print-proof release-combined clean-working

PYTHON ?= python
CHANGES ?= Reviewed article and readability cleanup.
GUARD_NOTE ?= review chunk

setup:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m compileall -q scripts
	$(PYTHON) scripts/check_csv_shapes.py
	$(PYTHON) -m pytest -q

csv-check:
	$(PYTHON) scripts/check_csv_shapes.py

build-fresh: build-ot build-nt release-combined

build-ot:
	$(PYTHON) scripts/run_book_checkpoint.py

checkpoint-ot:
	$(PYTHON) scripts/run_book_checkpoint.py --diff-check --smoke-test

review-ot-fast:
	@test -n "$(REFS)" || (echo 'Usage: make review-ot-fast REFS="Isaiah 44:24-28" [PASS=262] [CHANGES="..."]'; exit 1)
	$(PYTHON) scripts/run_fast_review_checkpoint.py --testament ot --refs "$(REFS)" --sync-footnotes --add-full-verse-guards --guard-note "$(GUARD_NOTE)" $(if $(PASS),--pass-id $(PASS),) --changes "$(CHANGES)"

build-ot-review:
	$(PYTHON) scripts/run_priority_review_suite.py

build-nt:
	$(PYTHON) scripts/apply_nt_tr_literal_revision.py
	$(PYTHON) scripts/build_nt_tr_vs_ukjv_review.py
	$(PYTHON) scripts/build_fresh_translation.py --source data/raw/tr_greek/nt_full.csv --output output/fresh_translation_nt_tr_full.md --translation-only-output output/fresh_translation_nt_tr_translation_only.md --diagnostics output/fresh_translation_nt_tr_diagnostics.json
	$(PYTHON) scripts/build_fresh_logos_bible.py --testament nt --source data/raw/tr_greek/nt_full.csv --logos-docx output/logos_nt/fresh_translation_nt_tr_logos_bible.docx --mt-bridge-docx output/logos_nt/fresh_translation_nt_tr_reference_notes.docx --proof-docx output/logos_nt/fresh_translation_nt_tr_proofreading.docx --diagnostics output/logos_nt/fresh_translation_nt_tr_diagnostics.json --readme output/logos_nt/README.md --preview output/logos_nt/fresh_translation_nt_tr_preview.md

build-nt-fast:
	rm -rf output/working/nt_fast output/working/logos_nt_fast
	$(PYTHON) scripts/apply_nt_tr_literal_revision.py
	$(PYTHON) scripts/build_nt_tr_vs_ukjv_review.py
	$(PYTHON) scripts/build_fresh_translation.py --source data/raw/tr_greek/nt_full.csv --output output/working/nt_fast/fresh_translation_nt_tr_full.md --translation-only-output output/working/nt_fast/fresh_translation_nt_tr_translation_only.md --diagnostics output/working/nt_fast/fresh_translation_nt_tr_diagnostics.json
	$(PYTHON) scripts/build_fresh_logos_bible.py --testament nt --source data/raw/tr_greek/nt_full.csv --logos-docx output/working/logos_nt_fast/fresh_translation_nt_tr_logos_bible.docx --mt-bridge-docx output/working/logos_nt_fast/fresh_translation_nt_tr_reference_notes.docx --proof-docx output/working/logos_nt_fast/fresh_translation_nt_tr_proofreading.docx --diagnostics output/working/logos_nt_fast/fresh_translation_nt_tr_diagnostics.json --readme output/working/logos_nt_fast/README.md --preview output/working/logos_nt_fast/fresh_translation_nt_tr_preview.md --docx-compresslevel 1 --skip-docx-validation --docx-output-set logos-only

build-nt-book:
	@test -n "$(BOOK)" || (echo 'Usage: make build-nt-book BOOK=Matthew'; exit 1)
	rm -rf output/working/nt_book output/working/logos_nt_book
	$(PYTHON) scripts/apply_nt_tr_literal_revision.py
	$(PYTHON) scripts/build_fresh_translation.py --source data/raw/tr_greek/nt_full.csv --book "$(BOOK)" --output output/working/nt_book/fresh_translation_nt_tr_full.md --translation-only-output output/working/nt_book/fresh_translation_nt_tr_translation_only.md --diagnostics output/working/nt_book/fresh_translation_nt_tr_diagnostics.json
	$(PYTHON) scripts/build_fresh_logos_bible.py --testament nt --book "$(BOOK)" --source data/raw/tr_greek/nt_full.csv --logos-docx output/working/logos_nt_book/fresh_translation_nt_tr_logos_bible.docx --mt-bridge-docx output/working/logos_nt_book/fresh_translation_nt_tr_reference_notes.docx --proof-docx output/working/logos_nt_book/fresh_translation_nt_tr_proofreading.docx --diagnostics output/working/logos_nt_book/fresh_translation_nt_tr_diagnostics.json --readme output/working/logos_nt_book/README.md --preview output/working/logos_nt_book/fresh_translation_nt_tr_preview.md --docx-compresslevel 1 --skip-docx-validation --docx-output-set logos-only

review-nt-fast:
	@test -n "$(REFS)" || (echo 'Usage: make review-nt-fast REFS="Matthew 1:1-5" [PASS=262] [CHANGES="..."]'; exit 1)
	$(PYTHON) scripts/run_fast_review_checkpoint.py --testament nt --refs "$(REFS)" --sync-footnotes --add-full-verse-guards --guard-note "$(GUARD_NOTE)" $(if $(PASS),--pass-id $(PASS),) --changes "$(CHANGES)"

build-combined:
	$(PYTHON) scripts/build_combined_fresh_translation.py

build-combined-logos:
	$(PYTHON) scripts/build_fresh_logos_bible.py --testament combined --source data/raw/lxx_greek/ot_full.csv --nt-source data/raw/tr_greek/nt_full.csv --logos-docx output/logos_greek_heritage/the_greek_heritage_study_bible_logos_bible.docx --mt-bridge-docx output/logos_greek_heritage/the_greek_heritage_study_bible_reference_notes.docx --proof-docx output/logos_greek_heritage/the_greek_heritage_study_bible_proofreading.docx --diagnostics output/logos_greek_heritage/the_greek_heritage_study_bible_diagnostics.json --readme output/logos_greek_heritage/README.md --preview output/logos_greek_heritage/the_greek_heritage_study_bible_preview.md

build-print-proof:
	$(PYTHON) scripts/build_print_proof_bible.py

release-combined: build-combined build-combined-logos
	$(PYTHON) scripts/build_combined_release_package.py

clean-working:
	rm -rf output/working
