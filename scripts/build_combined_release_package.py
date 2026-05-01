#!/usr/bin/env python3
import argparse
import hashlib
import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASE_DIR = ROOT / "release" / "fresh-translation-full-bible-rc1"
MANIFEST = RELEASE_DIR / "MANIFEST.md"
CHECKSUMS = RELEASE_DIR / "CHECKSUMS.sha256"

READER_ARTIFACTS = [
    "output/fresh_translation_full_bible_translation_only.md",
    "output/fresh_translation_full_bible.md",
    "output/fresh_translation_full_bible_diagnostics.json",
]

LOGOS_ARTIFACTS = [
    "output/logos_full/fresh_translation_full_bible_logos_bible.docx",
    "output/logos_full/fresh_translation_full_bible_reference_notes.docx",
    "output/logos_full/fresh_translation_full_bible_proofreading.docx",
    "output/logos_full/fresh_translation_full_bible_diagnostics.json",
    "output/logos_full/fresh_translation_full_bible_preview.md",
    "output/logos_full/README.md",
]

VERIFICATION_ARTIFACTS = [
    "output/release_hardening_report.md",
    "output/release_hardening_report.json",
    "output/release_hardening_samples.csv",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require_artifacts(relative_paths: list[str]) -> None:
    missing = [path for path in relative_paths if not (ROOT / path).exists()]
    if missing:
        raise FileNotFoundError("Missing release artifacts: " + ", ".join(missing))


def bullet_list(paths: list[str]) -> str:
    return "\n".join(f"- `{path}`" for path in paths)


def build_manifest(date_prepared: str) -> str:
    return f"""# Fresh Translation Full Bible RC1 Manifest

Release candidate: `fresh-translation-full-bible-rc1`

Date prepared: {date_prepared}

This package is a lightweight manifest for the committed full OT/NT release artifacts. Large generated outputs remain in `output/` to avoid duplicating multi-megabyte files in git.

## Primary Reader Artifacts

{bullet_list(READER_ARTIFACTS)}

## Logos Personal Book Artifacts

{bullet_list(LOGOS_ARTIFACTS)}

## Release Verification Artifacts

{bullet_list(VERIFICATION_ARTIFACTS)}

## Scope

- OT source: `data/raw/lxx_greek/ot_full.csv`
- NT source: `data/raw/tr_greek/nt_full.csv`
- Combined reader draft: Genesis through Revelation, 66 books.
- Combined Logos DOCX: compile `output/logos_full/fresh_translation_full_bible_logos_bible.docx` in Logos Personal Books as resource type `Bible`.

## Checksums

See `CHECKSUMS.sha256`.

## Rebuild

```bash
make release-combined
```
"""


def write_checksums(relative_paths: list[str]) -> None:
    lines = [f"{sha256(ROOT / path)}  {path}" for path in relative_paths]
    CHECKSUMS.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date-prepared", default=date.today().isoformat())
    args = parser.parse_args()

    artifacts = [*READER_ARTIFACTS, *LOGOS_ARTIFACTS, *VERIFICATION_ARTIFACTS]
    require_artifacts(artifacts)
    RELEASE_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(build_manifest(args.date_prepared), encoding="utf-8")
    write_checksums(artifacts)
    print(
        json.dumps(
            {
                "manifest": str(MANIFEST),
                "checksums": str(CHECKSUMS),
                "artifacts": len(artifacts),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
