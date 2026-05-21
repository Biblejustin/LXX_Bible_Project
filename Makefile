.PHONY: setup test csv-check build-fresh build-ot checkpoint-ot review-ot-fast build-ot-review import-deuterocanon build-deuterocanon build-deuterocanon-logos validate-deuterocanon build-deuterocanon-book build-nt build-nt-fast build-nt-book review-nt-fast build-combined build-combined-logos build-concordance-preview build-concordance-broad-preview build-study-helps-appendix generate-print-pericopes build-print-proof build-print-proof-lulu-pdf build-print-proof-lulu-pandoc-pdf build-print-proof-lulu-pandoc-pdf-with-backmatter build-print-proof-handy-pandoc-pdf release-combined clean-working

PYTHON ?= python
SOFFICE ?= /Applications/LibreOffice.app/Contents/MacOS/soffice
PANDOC ?= pandoc
XELATEX ?= xelatex
GS ?= gs
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

import-deuterocanon:
	$(PYTHON) scripts/import_lxx_deuterocanon_from_grclxx.py

build-deuterocanon: import-deuterocanon
	$(PYTHON) scripts/build_fresh_translation.py --source data/raw/lxx_deuterocanon/deuterocanon_full.csv --output output/deuterocanon/lxx_deuterocanon_worksheet.md --translation-only-output output/deuterocanon/lxx_deuterocanon_translation_only.md --diagnostics output/deuterocanon/lxx_deuterocanon_diagnostics.json --no-review-data
	$(PYTHON) scripts/build_deuterocanon_progress.py

build-deuterocanon-logos: build-deuterocanon
	$(PYTHON) scripts/build_fresh_logos_bible.py --testament deuterocanon --source data/raw/lxx_deuterocanon/deuterocanon_full.csv --logos-docx output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_logos_bible.docx --mt-bridge-docx output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_reference_notes.docx --proof-docx output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_proofreading.docx --diagnostics output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_diagnostics.json --readme output/logos_deuterocanon/README.md --preview output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_preview.md --no-crossrefs --docx-output-set logos-only

validate-deuterocanon: build-deuterocanon
	$(PYTHON) -m compileall -q scripts
	$(PYTHON) scripts/check_csv_shapes.py
	git diff --check
	$(PYTHON) -m pytest -q tests/test_smoke.py::test_deuterocanon_source_workspace_is_separate_and_sourced

build-deuterocanon-book: import-deuterocanon
	@test -n "$(BOOK)" || (echo 'Usage: make build-deuterocanon-book BOOK=Tobit'; exit 1)
	rm -rf output/working/deuterocanon_book
	$(PYTHON) scripts/build_fresh_translation.py --source data/raw/lxx_deuterocanon/deuterocanon_full.csv --book "$(BOOK)" --output output/working/deuterocanon_book/lxx_deuterocanon_worksheet.md --translation-only-output output/working/deuterocanon_book/lxx_deuterocanon_translation_only.md --diagnostics output/working/deuterocanon_book/lxx_deuterocanon_diagnostics.json --no-review-data

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

build-concordance-preview:
	$(PYTHON) scripts/build_greek_concordance_preview.py

build-concordance-broad-preview:
	$(PYTHON) scripts/build_greek_concordance_preview.py --profile broad

build-study-helps-appendix:
	$(PYTHON) scripts/build_study_helps_appendix.py
	$(PANDOC) output/doc/greek_heritage_study_helps_appendix.md -s -o output/doc/greek_heritage_study_helps_appendix.pdf --pdf-engine=xelatex -V documentclass=extarticle -V papersize=letter -V geometry:margin=0.65in -V mainfont="Times New Roman" -V mainfontoptions=Ligatures=NoCommon

generate-print-pericopes:
	$(PYTHON) scripts/generate_print_pericope_headings.py

build-print-proof: generate-print-pericopes
	$(PYTHON) scripts/build_print_proof_bible.py

build-print-proof-lulu-pdf: build-print-proof-lulu-pandoc-pdf

build-print-proof-lulu-pandoc-pdf: generate-print-pericopes
	$(PYTHON) scripts/build_print_proof_bible.py --lulu-pod-margins --run-in-verse-paragraphs --run-in-group-size 0 --include-openbible-crossrefs --max-crossref-refs 4 --output output/print/the_greek_heritage_study_bible_lulu_print_proof.docx --diagnostics output/print/the_greek_heritage_study_bible_lulu_print_proof_diagnostics.json --readme output/print/README_lulu.md
	$(PANDOC) output/print/the_greek_heritage_study_bible_lulu_print_proof.docx -s -o output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc_raw.tex --lua-filter scripts/pandoc_split_xrefs.lua --lua-filter scripts/pandoc_pericope_keep.lua -H scripts/pandoc_print_header_8_75_green_xrefs.tex -V documentclass=extarticle -V papersize=letter -V classoption=twoside -V geometry:inner=0.55in -V geometry:outer=0.40in -V geometry:top=0.45in -V geometry:bottom=0.45in -V mainfont="Times New Roman" -V mainfontoptions=Ligatures=NoCommon
	cd output/print && $(XELATEX) -interaction=nonstopmode -halt-on-error -cnf-line=stack_size=500000 the_greek_heritage_study_bible_lulu_print_proof_pandoc_raw.tex
	cd output/print && $(XELATEX) -interaction=nonstopmode -halt-on-error -cnf-line=stack_size=500000 the_greek_heritage_study_bible_lulu_print_proof_pandoc_raw.tex
	cd output/print && $(XELATEX) -interaction=nonstopmode -halt-on-error -cnf-line=stack_size=500000 the_greek_heritage_study_bible_lulu_print_proof_pandoc_raw.tex
	rm -f output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc_raw.aux output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc_raw.log output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc_raw.out output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc_raw.tex
	$(PYTHON) scripts/stamp_print_pdf_headers.py --input output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc_raw.pdf --output output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf --source data/raw/lxx_greek/ot_full.csv --nt-source data/raw/tr_greek/nt_full.csv --diagnostics output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc_pdf_headers.json
	rm -f output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc_raw.pdf

build-print-proof-lulu-pandoc-pdf-with-backmatter: build-print-proof-lulu-pandoc-pdf build-study-helps-appendix build-concordance-broad-preview
	$(PANDOC) output/concordance/the_greek_heritage_study_bible_greek_concordance_broad_preview.md -s -o output/concordance/the_greek_heritage_study_bible_greek_concordance_broad_preview.pdf --pdf-engine=xelatex -H scripts/pandoc_concordance_header.tex -V documentclass=extarticle -V classoption=twocolumn -V papersize=letter -V geometry:margin=0.45in -V mainfont="Times New Roman" -V mainfontoptions=Ligatures=NoCommon
	$(GS) -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.7 -dPDFSETTINGS=/prepress -sOutputFile=output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc_with_appendix_concordance.pdf output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf output/doc/greek_heritage_study_helps_appendix.pdf output/concordance/the_greek_heritage_study_bible_greek_concordance_broad_preview.pdf

build-print-proof-handy-pandoc-pdf: generate-print-pericopes
	mkdir -p output/print/size_sweep/handy_6_39x9_46
	$(PYTHON) scripts/build_print_proof_bible.py --lulu-pod-margins --run-in-verse-paragraphs --run-in-group-size 0 --include-openbible-crossrefs --max-crossref-refs 3 --output output/print/size_sweep/handy_6_39x9_46/the_greek_heritage_study_bible_handy_6_39x9_46.docx --diagnostics output/print/size_sweep/handy_6_39x9_46/the_greek_heritage_study_bible_handy_6_39x9_46_diagnostics.json --readme output/print/size_sweep/handy_6_39x9_46/README.md
	$(PANDOC) output/print/size_sweep/handy_6_39x9_46/the_greek_heritage_study_bible_handy_6_39x9_46.docx -o output/print/size_sweep/handy_6_39x9_46/the_greek_heritage_study_bible_handy_6_39x9_46_raw.pdf --pdf-engine=xelatex --pdf-engine-opt=-cnf-line=stack_size=500000 --lua-filter scripts/pandoc_pericope_keep.lua -H scripts/pandoc_print_header_8_75_green_xrefs.tex -V documentclass=extarticle -V geometry:paperwidth=6.39in -V geometry:paperheight=9.46in -V classoption=twoside -V geometry:inner=0.50in -V geometry:outer=0.35in -V geometry:top=0.42in -V geometry:bottom=0.42in -V mainfont="Times New Roman" -V mainfontoptions=Ligatures=NoCommon
	$(PYTHON) scripts/stamp_print_pdf_headers.py --input output/print/size_sweep/handy_6_39x9_46/the_greek_heritage_study_bible_handy_6_39x9_46_raw.pdf --output output/print/size_sweep/handy_6_39x9_46/the_greek_heritage_study_bible_handy_6_39x9_46.pdf --source data/raw/lxx_greek/ot_full.csv --nt-source data/raw/tr_greek/nt_full.csv --diagnostics output/print/size_sweep/handy_6_39x9_46/the_greek_heritage_study_bible_handy_6_39x9_46_headers.json

release-combined: build-combined build-combined-logos
	$(PYTHON) scripts/build_release_hardening_report.py
	$(PYTHON) scripts/build_combined_release_package.py

clean-working:
	rm -rf output/working
