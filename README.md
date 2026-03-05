# 🎓 CFOPMDF

Repositório de Apoio ao Concurso CFO PMDF 2025/2026

[![Status do Concurso](https://img.shields.io/badge/Status-Ativo-green)](https://www.pm.df.gov.br/)
[![Última Atualização](https://img.shields.io/badge/Atualização-Jan%2F2026-blue)](EDITAIS/)
[![Edital Vigente](https://img.shields.io/badge/Edital-N%C2%BA%2018%2F2026-orange)](EDITAIS/)

Organização inteligente de conteúdo programático, editais oficiais e scripts
automatizados para otimizar seus estudos.

---

## 📋 Sobre o Projeto

Este repositório foi desenvolvido para centralizar e organizar todo o material
necessário para o concurso de **Cadete da Polícia Militar do Distrito Federal
(CFO PMDF 2025/2026)**. O projeto oferece:

- ✅ **Conteúdo programático estruturado** em checklist Markdown e planilha
  Excel
- 📄 **Editais oficiais** e retificações organizados cronologicamente
- 🔄 **Scripts automatizados** para download e processamento de arquivos
- 📊 **Consolidação vigente** com todas as alterações dos editais
- 🎯 **Comparação estratégica** entre PMDF e PLF CD para apoio estratégico

### Público-Alvo

- Candidatos ao CFO PMDF 2025/2026
- Estudantes que buscam organização sistemática do conteúdo
- Profissionais que desejam acompanhar atualizações do concurso

---

## 📁 Estrutura do Repositório

```text
CFOPMDF/
├── CONTEUDO_PROGRAMATICO/
│   ├── CONTEUDO_PMDF.md      # Conteúdo principal (checklist)
│   ├── CONTEUDO_PMDF.xlsx    # Versão em planilha (abas por matéria)
│   └── CONTEUDO_PLCD.md      # Conteúdo de referência adicional
│
├── EDITAIS/
│   ├── *.pdf                  # Editais oficiais em PDF
│   ├── PM_DF_25_CFO_manifest.json
│   ├── EDITAL_CFO.md
│   ├── EDITAL_PLF.md
│   └── CONSOLIDADO_EDITAIS_PMDF_CFO_ATUALIZADO.md
│
├── scripts/
│   ├── download_editais_pm_df_25_cfo.py
│   └── md_to_xlsx_pmfd.py
│
├── comparacao_conteudos.md
├── comparacao_editais_cfo_plf.md
└── CLAUDE.md                  # Documentação técnica detalhada
```

---

## 🎯 Fontes de Verdade

A hierarquia de documentos garante que você sempre tenha acesso à versão mais
atualizada:

```text
PDFs Oficiais (Fonte Primária)
        ↓
Consolidado de Editais (Síntese Vigente)
        ↓
Markdown Editável (Base de Estudos)
```

**Em caso de conflito**, prevalece sempre o ato retificador mais recente.

---

## 🚀 Como Usar

### Pré-requisitos

- **[uv](https://github.com/astral-sh/uv)** - Gerenciador de pacotes Python
- **Python 3.13+**
- **markdownlint** - Para validação de Markdown
- **pdftotext** (Poppler) - Para extração de texto de PDFs

### Instalação Rápida

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/CFOPMDF.git
cd CFOPMDF

# Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

# Instalar dependências (se necessário)
pip install openpyxl requests markdownlint
```

---

## 🛠️ Scripts Disponíveis

### 1. Download de Editais

Baixa automaticamente os editais oficiais do concurso:

```bash
uv run python scripts/download_editais_pm_df_25_cfo.py
```

Funcionalidades:

- Download dos editais mais recentes
- Padronização de nomes (`YYYY-MM-DD_<slug>.pdf`)
- Atualização do manifesto de downloads

### 2. Conversão Markdown → Excel

Converte o conteúdo programático em planilha estruturada:

```bash
uv run --with openpyxl python scripts/md_to_xlsx_pmfd.py
```

Características:

- Gera abas separadas por matéria
- Mantém estrutura hierárquica
- Inclui checkboxes para acompanhamento

---

## 📚 Fluxo de Trabalho Recomendado

### Atualização de Conteúdo

```bash
# 1. Baixar novos editais
uv run python scripts/download_editais_pm_df_25_cfo.py

# 2. Verificar mudanças relevantes
pdftotext EDITAIS/<arquivo>.pdf - | rg "ANEXO III|retificação|subitem"

# 3. Ajustar conteúdo se necessário
# Editar: CONTEUDO_PROGRAMATICO/CONTEUDO_PMDF.md

# 4. Regerar planilha
uv run --with openpyxl python scripts/md_to_xlsx_pmfd.py

# 5. Validar Markdown
markdownlint CONTEUDO_PROGRAMATICO/CONTEUDO_PMDF.md
```

---

## 📊 Status do Concurso

### Histórico de Alterações

| Data | Edital | Descrição |
| :--- | :--- | :--- |
| 03/02/2025 | Nº 03/2025 | Abertura do concurso |
| 28/02/2025 | Nº 20/2025 | Primeira retificação |
| 21/03/2025 | Nº 32/2025 | Segunda retificação |
| 28/03/2025 | Nº 39/2025 | Terceira retificação |
| 26/05/2025 | Nº 69/2025 | ⚠️ **Suspensão do concurso** |
| 19/12/2025 | Nº 207/2025 | ✅ **Retomada do concurso** |
| 30/12/2025 | Nº 212/2025 | Retificação de vagas e PCD |
| 08/01/2026 | Nº 10/2026 | Correção de numeração |
| 08/01/2026 | Nº 12/2026 | Atualização de remuneração |
| 21/01/2026 | Nº 18/2026 | Locais de acesso à internet |

### Informações Vigentes

- **Remuneração Cadete 1º Ano:** R$ 7.669,44 (Edital nº 12/2026)
- **Vagas:** Conforme quadro retificado pelo Edital nº 212/2025
- **Cronograma:** Atualizado no Edital nº 207/2025

> ⚠️ **Importante:** O concurso foi suspenso em maio/2025 e retomado em
> dezembro/2025.

---

## ✅ Padrões de Edição

Ao contribuir com o repositório:

- ✅ Mantenha estrutura hierárquica numérica (`1`, `1.1`, `1.1.1`)
- ✅ Use checkboxes Markdown (`- [ ]`) para itens de estudo
- ✅ Preserve formatação legal ao copiar de PDFs
- ✅ Valide sintaxe Markdown antes de commitar
- ✅ Mantenha nomes de PDFs padronizados (`YYYY-MM-DD_<slug>.pdf`)

### Validação

```bash
# Validar Markdown principal
markdownlint CONTEUDO_PROGRAMATICO/CONTEUDO_PMDF.md

# Verificar mudanças em edital
pdftotext EDITAIS/<arquivo>.pdf - | rg "ANEXO III|retificação|subitem"
```

---

## 📖 Documentação Adicional

- **[CLAUDE.md](CLAUDE.md)** - Documentação técnica detalhada para operações
  do repositório
- **[CONSOLIDADO_EDITAIS](EDITAIS/CONSOLIDADO_EDITAIS_PMDF_CFO_ATUALIZADO.md)**
  - Síntese completa das alterações
- **[comparacao_conteudos.md](comparacao_conteudos.md)** - Comparação PMDF × PLF
  CD

---

## 🔗 Links Úteis

- [Site Oficial PMDF](https://www.pm.df.gov.br/)
- [CEBRASPE - Banca Organizadora](http://www.cebraspe.org.br/)
- [Página Oficial do Concurso](http://www.cebraspe.org.br/concursos/pm_df_25_cfo)

---

## 📄 Licença

Este projeto é disponibilizado para uso educacional e pessoal. Os editais e
conteúdo programático são documentos oficiais da PMDF e CEBRASPE.

---

**📚 Bom estudo e boa sorte no concurso!**
