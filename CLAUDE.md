# CLAUDE.md

Guia operacional para trabalhar neste repositório com foco em conteúdo de
estudos do CFO PMDF.

## Objetivo do Repositório

Este projeto organiza:

- conteúdo programático do CFO PMDF em Markdown e Excel;
- editais oficiais (PDF) e consolidações;
- comparações entre PMDF e PLF CD para apoio estratégico de estudo.

## Estrutura Principal

```text
CFOPMDF/
├── CONTEUDO_PROGRAMATICO/
│   ├── CONTEUDO_PMDF.md
│   ├── CONTEUDO_PMDF.xlsx
│   └── CONTEUDO_PLCD.md
├── EDITAIS/
│   ├── *.pdf
│   ├── EDITAL_CFO.md
│   ├── EDITAL_PLF.md
│   ├── PM_DF_25_CFO_manifest.json
│   └── CONSOLIDADO_EDITAIS_PMDF_CFO_ATUALIZADO.md
├── scripts/
│   ├── download_editais_pm_df_25_cfo.py
│   └── md_to_xlsx_pmfd.py
├── comparacao_conteudos.md
└── comparacao_editais_cfo_plf.md
```

## Fontes de Verdade

1. **PDFs em `EDITAIS/`**: fonte primária para regras e retificações.
2. `CONSOLIDADO_EDITAIS_PMDF_CFO_ATUALIZADO.md`: síntese vigente.
3. `CONTEUDO_PROGRAMATICO/CONTEUDO_PMDF.md`: base de estudo editável.

Em conflito, prevalece sempre o ato retificador mais recente.

## Fluxo de Trabalho Recomendado

1. Atualizar editais:
   - `uv run python scripts/download_editais_pm_df_25_cfo.py`
2. Detectar impacto no conteúdo:
   - `pdftotext EDITAIS/<arquivo>.pdf - | rg "ANEXO III|retificação|subitem"`
3. Ajustar `CONTEUDO_PMDF.md` (mantendo checklist e hierarquia).
4. Regerar planilha:
   - `uv run --with openpyxl python scripts/md_to_xlsx_pmfd.py`
5. Atualizar consolidado de editais se necessário.

## Padrões de Edição

- Conteúdo programático em checklist Markdown (`- [ ]`).
- Subitens devem seguir hierarquia numérica (`1`, `1.1`, `1.1.1`).
- Evitar alterar texto legal sem confirmação no PDF correspondente.
- Nomes de PDFs devem seguir `YYYY-MM-DD_<slug>.pdf`.

## Validação Antes de Finalizar

- `markdownlint CONTEUDO_PROGRAMATICO/CONTEUDO_PMDF.md`
- Verificar se mudanças batem com o(s) subitem(ns) retificado(s).
- Se houver impacto estrutural, validar `CONTEUDO_PMDF.xlsx` (abas, colunas,
  fórmulas e comportamento de checklist).

## Ambiente

- Python via `uv` com `.venv` local.
- Preferir `rg` para busca textual.
- Não incluir segredos no repositório.
