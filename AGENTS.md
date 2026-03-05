# Repository Guidelines

## Project Structure & Module Organization

This repository is document-first and focused on PMDF/PLCD study materials.

- `CONTEUDO_PROGRAMATICO/`: source content files and generated workbook.
- `EDITAIS/`: official edital PDFs, parsed markdown references, and
  consolidated summaries.
- `scripts/`: automation scripts for downloads and markdown-to-XLSX conversion.
- Root `.md` files: comparison documents and high-level summaries.

## Build, Test, and Development Commands

Use `uv` with the local virtual environment for Python tasks.

- `uv run python scripts/download_editais_pm_df_25_cfo.py`
  Downloads/updates edital PDFs and writes a manifest.
- `uv run --with openpyxl python scripts/md_to_xlsx_pmfd.py`
  Regenerates `CONTEUDO_PROGRAMATICO/CONTEUDO_PMDF.xlsx`.
- `markdownlint CONTEUDO_PROGRAMATICO/CONTEUDO_PMDF.md`
  Validates markdown style and structure.
- `pdftotext EDITAIS/<arquivo>.pdf - | rg "ANEXO III|retificação"`
  Quick check for retification impact in source PDFs.

## Coding Style & Naming Conventions

- Python: 4-space indentation, UTF-8 encoding, small deterministic functions.
- Prefer idempotent scripts and stable ordering in outputs.
- PDF naming pattern in `EDITAIS/`: `YYYY-MM-DD_<slug>.pdf`.
- Consolidation docs: explicit uppercase names (example:
  `CONSOLIDADO_EDITAIS_PMDF_CFO_ATUALIZADO.md`).
- Run `markdownlint` before finalizing markdown edits.

## Testing Guidelines

There is no formal test suite yet. Validate by behavior.

- Confirm script exit code is zero.
- Check generated file presence and non-zero size.
- For XLSX updates, verify sheet names, columns, and formulas manually.
- For edital updates, confirm changed subitems against newest retification PDFs.

## Commit & Pull Request Guidelines

No Git history is available in this directory. Use this convention:

- Commit format: `type(scope): summary`.
- Example: `docs(editais): consolidate Jan 2026 retifications`.
- Keep each commit to one logical change.
- PRs should include changed paths, rationale, and validation commands run.

## Security & Configuration Tips

- Treat edital PDFs as source of truth. Do not edit them manually.
- Do not include secrets or credentials in scripts or markdown.
- Keep environment/runtime folders (`.venv/`, `.omc/`) out of content edits.
