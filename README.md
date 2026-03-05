# CFOPMDF

Repositório de apoio para organização de estudos do concurso PMDF (CFO), com
conteúdo programático estruturado, editais oficiais baixados e documentos de
comparação/consolidação.

## Objetivo

Centralizar em um único lugar:

- conteúdo programático em Markdown e Excel;
- editais oficiais e retificações em PDF;
- consolidados para leitura da versão vigente;
- scripts para automação de download e transformação de arquivos.

## Estrutura do Projeto

- `CONTEUDO_PROGRAMATICO/`
  - `CONTEUDO_PMDF.md`: conteúdo programático principal (checklist).
  - `CONTEUDO_PMDF.xlsx`: versão em planilha (abas por matéria).
  - `CONTEUDO_PLCD.md`: conteúdo de referência adicional.
- `EDITAIS/`
  - PDFs oficiais do concurso.
  - `PM_DF_25_CFO_manifest.json`: inventário dos downloads.
  - `CONSOLIDADO_EDITAIS_PMDF_CFO_ATUALIZADO.md`: consolidação vigente.
- `scripts/`
  - `download_editais_pm_df_25_cfo.py`: baixa e padroniza editais.
  - `md_to_xlsx_pmfd.py`: converte Markdown para planilha.
- Arquivos na raiz: comparações e análises (`comparacao_*.md`).

## Pré-requisitos

- `uv`
- Python 3.13+
- `markdownlint`
- `pdftotext` (Poppler)

## Comandos Úteis

- Atualizar editais:
  - `uv run python scripts/download_editais_pm_df_25_cfo.py`
- Regerar planilha do conteúdo:
  - `uv run --with openpyxl python scripts/md_to_xlsx_pmfd.py`
- Validar Markdown principal:
  - `markdownlint CONTEUDO_PROGRAMATICO/CONTEUDO_PMDF.md`
- Buscar mudanças em edital PDF:
  - `pdftotext EDITAIS/<arquivo>.pdf - | rg "ANEXO III|retificação"`

## Fluxo Recomendado de Atualização

1. Baixar os novos editais com o script.
2. Verificar retificações com `pdftotext` + `rg`.
3. Ajustar `CONTEUDO_PROGRAMATICO/CONTEUDO_PMDF.md` se necessário.
4. Regerar `CONTEUDO_PMDF.xlsx`.
5. Atualizar consolidado em `EDITAIS/`.

## Boas Práticas

- Não editar PDFs manualmente (fonte de verdade).
- Manter nomes padronizados em `EDITAIS/` (`YYYY-MM-DD_<slug>.pdf`).
- Validar markdown antes de concluir alterações.
