---
name: redacao-defesa
description: Use para REDIGIR a minuta de uma peça de DEFESA do cliente — contestação, reconvenção, réplica, impugnação, contrarrazões — seguindo a estrutura do CPC e o padrão do escritório. Triggers — "redige uma contestação pra esse caso", "monta a minuta de defesa com base nesses fatos", "faz a contestação", "escreve a réplica a essa contestação", "minuta as contrarrazões do recurso". É redação PARCIAL (advoga pelo cliente). NÃO confunda com `relatorio-juridico` (relatório imparcial de processo) nem com `analise-peca-adversa` (que só analisa e mapeia, não redige a peça). Direito processual brasileiro (CPC). Toda minuta é rascunho para revisão de advogado habilitado.
---

# Redação de peça de defesa (minuta)

Produz a **minuta** de uma peça defensiva, advogando pelo cliente. Idealmente
parte do **mapa de defesa** da `analise-peca-adversa`; se ele não existir,
gere-o antes (ou peça os fatos ao usuário).

> **Prazo nunca "de cabeça".** A tempestividade da peça depende de uma conta em
> dias úteis (CPC 219/224) sujeita a recesso e feriados — delegue-a sempre à
> skill [[calculo-prazos-cpc]].

## Natureza e guardrails (críticos)

- **Minuta, nunca peça final.** A saída é um **rascunho** para o advogado
  revisar, ajustar e assinar. Deixe isso explícito no topo do documento.
- **Não invente jurisprudência nem dispositivo.** Para o **texto vigente de
  artigo de lei federal** (CPC, CC, CDC, CLT etc.), busque o dispositivo em
  `consultar-legislacao` e cite a partir do trecho real. Súmula, tema repetitivo
  e precedente — só cite se verificado (`acuracia-juridica`); na dúvida, use
  "[citar precedente — verificar]" em vez de fabricar.
- **Não invente fatos.** Use apenas os fatos fornecidos pelo usuário, pelos
  autos ou pelo mapa de defesa. Lacuna de fato → "[CONFIRMAR COM CLIENTE]".
- **Fundamente cada tese.** Toda alegação de direito aponta a base legal.

## Pipeline

1. **Reúna os insumos** — mapa de defesa (`analise-peca-adversa`), fatos do
   cliente, documentos. Identifique **qual peça** redigir e o **prazo**. Para a
   seção "Da tempestividade", **calcule o vencimento com `calculo-prazos-cpc`**
   (não conte dias à mão) e cole a trilha de auditoria; se houver dúvida de
   tempestividade, sinalize com a conta à vista.
2. **Recupere o padrão do escritório** — `consultar-rag` por **peças-modelo** e
   **defesas anteriores** do mesmo tipo/tese/vara. Siga o estilo do escritório,
   não um genérico.
3. **Redija seguindo a estrutura** de `references/estrutura-contestacao.md`
   (endereçamento → tempestividade → preliminares → impugnação especificada →
   mérito/teses → reconvenção, se cabível → provas → pedidos).
4. **Cubra o ônus da impugnação especificada (art. 341 CPC)** — nenhum fato
   relevante da inicial pode ficar sem resposta.
5. **Revisão** — `acuracia-juridica` (fidelidade aos fatos + checagem de toda
   citação legal/jurisprudencial) **obrigatória** antes de entregar.
6. **Saída** — markdown; para DOCX no padrão do escritório,
   `formatacao-arquivos-juridicos`.

## Princípios

- **Advogue — com técnica e sobriedade.** Defenda o cliente sem adjetivação
  vazia; força está no argumento e na prova, não no exagero.
- **Espelhe a inicial** ao impugnar (fato a fato), para não deixar incontroverso.
- **Marque o que falta** com `[CONFIRMAR]` / `[verificar]` — melhor um furo
  visível que o advogado fecha do que um fato/precedente inventado.
- A minuta termina sempre com nota: *"Minuta gerada para revisão — conferir
  fatos, provas e fundamentos antes de protocolar."*
