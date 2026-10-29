# Skill `peca-trabalhista` — Manual da Equipe FM

Esta skill ajuda a produzir peças trabalhistas seguindo o padrão do escritório Ferreira & Martins: formatação, identidade visual, método de análise e catálogo de teses por verba.

## Como usar (passo a passo)

1. **Abra o Claude Code** (terminal).
2. **Invoque a skill** digitando `/peca-trabalhista` ou simplesmente descrevendo o que precisa: "preciso contestar uma reclamatória trabalhista", "redige um Recurso Ordinário", "prepara minha sustentação oral", etc.
3. **Responda à triagem.** A skill vai pedir: tipo de peça, número dos autos, vara/TRT, partes, principais pedidos, fase processual, tese central, documentos disponíveis.
4. **Envie os documentos** (sentença, inicial, contestação, contrato, cartões de ponto, etc.). Pode colar texto, indicar caminho do arquivo ou um link do Google Drive — a skill busca.
5. **Revise a minuta** que a skill apresenta em texto. Peça ajustes, novas teses, mudança de tom.
6. **Aprove a versão final.** A skill vai gerar automaticamente o `.docx` aplicando o template visual FM (logo, rodapé, margens, fonte).
7. **Abra o `.docx` no Word**, faça revisão final humana, confira numeração de páginas, salve e protocole.

## O que a skill faz por você

- Aplica o **método de análise FM**: fatos → problema → controvérsias → direito → teses × objeções → conclusão.
- Consulta o **catálogo de teses por verba** (`teses_por_verba.md`) com teses defensivas para 28+ tipos de pedidos trabalhistas (horas extras, intervalo, vínculo, equiparação, justa causa, dano moral, terceirização, grupo econômico, sucessão, FGTS, multas, estabilidades, etc.).
- Aplica o **checklist por tipo de peça** (`tipos_de_peca.md`): preliminares obrigatórias, prazos, preparo, prequestionamento, transcendência (RR), dialeticidade, etc.
- Gera o **.docx final** com:
  - Logo do escritório no cabeçalho
  - Rodapé com contatos de Chapecó e Joaçaba
  - Margens A4: superior 4,50 cm | inferior 2,50 cm | esquerda 3,00 cm | direita 2,50 cm
  - Texto justificado, sem recuo
  - Estrutura formal padrão (endereçamento, qualificação, fatos, fundamentos, pedidos, fecho, assinatura)

## O que a skill NÃO faz (não confie cegamente)

- **Não inventa jurisprudência.** Quando cita súmula, OJ ou precedente, a skill marca para você conferir o teor atualizado. Sempre conferir antes de protocolar.
- **Não substitui revisão humana.** É uma minuta inteligente, não uma peça final. O advogado responsável precisa ler, ajustar argumentos ao caso concreto e assumir a responsabilidade técnica.
- **Não tem acesso ao processo eletrônico.** Você precisa fornecer os documentos (texto colado, PDF anexado ou link do Drive).
- **Não acompanha prazos.** Confirme tempestividade no seu sistema (Iilex).

## Tipos de peça cobertos

- Contestação trabalhista
- Recurso Ordinário (RO)
- Recurso de Revista (RR) — com transcendência e indicação de trecho
- Agravo de Instrumento em RR (AIRR)
- Embargos de Declaração
- Contrarrazões
- Manifestação sobre cálculos / impugnação à liquidação
- Razões finais / Memoriais
- Sustentação oral (roteiro)
- Petição inicial (quando a empresa é autora)

## Estrutura dos arquivos

```
~/.claude/skills/peca-trabalhista/
├── SKILL.md              # instruções carregadas pelo Claude
├── teses_por_verba.md    # catálogo de teses defensivas
├── tipos_de_peca.md      # checklist por tipo de peça
├── gerar_docx.py         # script que gera o .docx aplicando template FM
├── ocr_pdf.py            # OCR de PDFs escaneados (wrapper Python)
├── ocr_pdf.swift         # OCR via Vision API nativa do macOS
└── README.md             # este manual
```

## OCR de documentos escaneados

Muitos documentos trabalhistas chegam como **PDF escaneado** (imagem dentro do PDF, sem texto). A skill já trata isso automaticamente quando você manda os arquivos para análise — ela detecta que não há texto extraível e roda o OCR.

Para rodar manualmente (sem chamar o Claude):

```bash
# 1 arquivo
python3 ~/.claude/skills/peca-trabalhista/ocr_pdf.py /caminho/TRCT.pdf

# Pasta inteira (todos os PDFs/imagens dentro)
python3 ~/.claude/skills/peca-trabalhista/ocr_pdf.py /caminho/pasta_do_processo/

# Arquivo .zip (extrai e processa)
python3 ~/.claude/skills/peca-trabalhista/ocr_pdf.py /caminho/arquivos.zip
```

O texto extraído é salvo automaticamente em `<arquivo>.pdf.ocr.txt`, para que rodadas futuras reaproveitem.

Vantagens:
- Usa Vision API nativa do macOS — **sem instalar nada** (sem brew, sem tesseract).
- Suporte nativo a português brasileiro.
- Cache automático para não reprocessar.
- Funciona com PDFs, PNG, JPG, HEIC, TIFF.

Template visual (interno à skill):
```
~/.claude/skills/peca-trabalhista/templates/
├── peca_modelo_FM.docx   # base do .docx (header com logo, footer com rodapé)
├── logo_FM.png
├── rodape_FM.png
└── word_header1.xml
```

## Geração manual do .docx (sem chamar o Claude)

Caso você já tenha o texto da peça pronto em Markdown e queira só montar o .docx:

```bash
python3 ~/.claude/skills/peca-trabalhista/gerar_docx.py \
  --corpo-arquivo /caminho/sua_peca.md \
  --saida ~/Downloads/contestacao_caso_X.docx
```

Convenções aceitas no `.md` de entrada:
- `# TÍTULO` → centralizado, negrito, MAIÚSCULAS, 14pt
- `## I — Seção` → negrito, esquerda, 12pt
- `### I.1 — Subseção` → negrito itálico, 12pt
- `**texto**` inline → negrito
- `*texto*` inline → itálico
- `> linha` → centralizada (fecho, local/data, assinatura)
- Linha em branco → parágrafo em branco
- Resto → justificado

## Dúvidas e melhorias

Reporte ao Clênio ou Francieli. Ajustes na skill (incluir nova tese, novo tipo de peça, alterar template visual) podem ser pedidos diretamente ao Claude.
