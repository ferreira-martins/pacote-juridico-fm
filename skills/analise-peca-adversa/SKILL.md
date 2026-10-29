---
name: analise-peca-adversa
description: Use para analisar a peça da PARTE CONTRÁRIA (petição inicial, contestação, reconvenção, recurso) com o objetivo de PREPARAR A RESPOSTA do cliente — extrair pedidos, causa de pedir, fatos e fundamentos alegados, provas juntadas, e mapear os pontos frágeis, as preliminares cabíveis e as teses de defesa/refutação. Triggers — "analisa essa inicial pra eu contestar", "que teses dá pra levantar contra essa petição?", "monta os pontos de ataque dessa contestação pra réplica", "o que dá pra impugnar aqui?". É uma análise PARCIAL, a favor do cliente (municia a defesa). NÃO confunda com `relatorio-juridico`, que descreve o processo de forma imparcial e neutra — aqui o objetivo é tomar partido e achar como derrubar a tese adversária. Direito processual brasileiro (CPC).
---

# Análise de peça adversa (preparar a resposta)

Lê a peça da parte contrária e produz um **mapa de defesa** — o insumo para
redigir a contestação, a réplica ou as contrarrazões. Trabalha **a favor do
cliente**.

## Natureza e guardrails

- **Parcial, por desenho.** Diferente da `relatorio-juridico` (imparcial), aqui
  o objetivo é encontrar fragilidades na tese adversária e construir a defesa.
- **Rascunho de trabalho** para o advogado — não é peça final nem dispensa
  revisão de profissional habilitado (OAB).
- **Sem inventar.** Para dispositivo de lei federal (CPC — arts. 337, 341 etc.),
  confira o texto vigente em `consultar-legislacao` e cite a partir do trecho
  real; súmula/precedente, verifique via `acuracia-juridica`. Na dúvida, marque
  "(verificar)".
- **Fidelidade ao que a peça diz.** Separe o que a parte **alega** do que ela
  **prova** — alegação não é fato provado.

## Pipeline

1. **Ingestão** — se vier em PDF/DOCX, use `formatacao-arquivos-juridicos`;
   peça longa, `chunking-juridico`; para localizar trechos específicos,
   `busca-semantica-juridica`.
2. **Extração estruturada** da peça adversa:
   - **Partes e polo**, juízo, fase processual, qual peça é.
   - **Pedidos** (principal e subsidiários) e **valor**.
   - **Causa de pedir** (fundamentos de fato e de direito).
   - **Fatos alegados** × **provas efetivamente juntadas** (documento, número).
   - **Fundamentos jurídicos** invocados (dispositivos, jurisprudência).
3. **Mapa de ataque** — para cada ponto, avalie:
   - **Preliminares cabíveis** (art. 337 CPC — incompetência, inépcia, coisa
     julgada, litispendência, ausência de pressuposto, etc.).
   - **Prejudiciais de mérito** — prescrição/decadência.
   - **Fragilidades**: fato sem prova, contradição interna, pedido juridicamente
     impossível, documento que não comprova o alegado, tese superada.
   - **Ônus da impugnação especificada** (art. 341 CPC) — liste fato a fato o que
     precisa ser impugnado para não se tornar incontroverso.
   - **Provas a produzir** pela defesa (documental, pericial, testemunhal).
4. **Subsídios internos** — use `consultar-rag` para recuperar **defesas
   anteriores do escritório** sobre tese/vara/tema análogos (peças-modelo,
   contestações passadas) e citar o que já funcionou.
5. **Revisão** — `acuracia-juridica` (fidelidade ao texto + checagem de
   dispositivos) antes de entregar.

## Estrutura da saída

```markdown
## Mapa de Defesa — [tipo da peça adversa]
**Processo**: [CNJ] · **Juízo**: [...] · **Cliente (polo)**: [...]

### Síntese da pretensão adversária
- Pedidos: [...]
- Causa de pedir: [...]

### Preliminares cabíveis (art. 337 CPC)
1. [preliminar] — [por quê] — (Confiança X%)

### Prejudiciais de mérito
- Prescrição/decadência: [análise]

### Pontos frágeis da tese adversária
| Alegação | Tem prova? | Como atacar |
|---|---|---|

### Impugnação especificada (art. 341) — fato a fato
- [fato] → [posição da defesa]

### Provas a produzir
- [...]

### Subsídios do acervo (consultar-rag)
- [peça/processo análogo encontrado]
```

## Princípios

- **Tome partido — declarado.** A leitura é a favor do cliente.
- **Alegação ≠ prova.** Marque o que a parte não comprovou.
- **Não deixe fato sem resposta** (art. 341): o que não for impugnado vira
  incontroverso.
- **Sem dispositivo/precedente inventado.** Verifique antes de citar.
- Saída em markdown; para DOCX/PDF, `formatacao-arquivos-juridicos`.
