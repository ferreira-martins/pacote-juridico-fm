---
name: estrutura-pecas
description: Use SEMPRE que o usuário pedir para MONTAR o ESQUELETO ou a ESTRUTURA ARGUMENTATIVA de uma PEÇA PROCESSUAL — petição inicial, manifestação, recurso, agravo, memoriais, contrarrazões etc. — quando o foco é a ORDEM dos tópicos, as teses, a linha de raciocínio e os pedidos (e não a redação final pronta para protocolo). Consulte esta skill ANTES de estruturar a peça, para seguir o método padronizado (endereçamento, resumo dos fatos, fundamentos por tese com premissa→norma→interpretação→jurisprudência, pedidos principal/subsidiários, requisitos de tutela, checklist pré-protocolo). Marque PESQUISAR onde não houver citação segura e use placeholders [COMPLETAR]. Triggers — "monta o esqueleto dessa petição", "estrutura os argumentos dessa inicial", "como organizo essa manifestação?", "qual a ordem das teses nesse recurso?", "esboça os tópicos da peça", "faz o esqueleto argumentativo". É um RASCUNHO/estrutura — NÃO é peça pronta para protocolo sem revisão humana e conferência de fatos/provas. NÃO confunda com `redacao-defesa` (que MINUTA contestação/réplica/contrarrazões com texto desenvolvido) nem com `relatorio-juridico` (descrição imparcial). Direito brasileiro (CPC).
---

# Estrutura e esqueleto de peças processuais — Brasil

Monta o **esqueleto argumentativo** de uma peça (títulos, ordem, teses, linha de
raciocínio, pedidos). **Não** é petição pronta para protocolo sem revisão humana
e conferência de fatos/provas.

## Natureza e guardrails

- **Estrutura, não peça final.** Entrega o andaime; a redação desenvolvida de
  defesa fica na `redacao-defesa`.
- **Não invente.** Citações de lei → `consultar-legislacao`; jurisprudência →
  roteiro via `pesquisa-jurisprudencia` (marque **PESQUISAR**, não invente
  número de processo). Fatos sem lastro → `[COMPLETAR]`.
- **Rascunho.** Passe pela `acuracia-juridica` e entregue com a lista de
  pendências para o advogado preencher.

## Pipeline

1. **Ingestão** — documentos do caso em PDF/DOCX → `formatacao-arquivos-juridicos`;
   peças longas → `chunking-juridico`. Acervo → `consultar-rag`.
2. **Esqueleto** — montar a estrutura abaixo.
3. **Fundamentos** — lei em `consultar-legislacao`; jurisprudência em
   `pesquisa-jurisprudencia`.
4. `acuracia-juridica`.

## Entrada mínima

Tipo de peça e fase · comarca/vara · partes · fatos (cronologia) · provas
mencionadas · teses desejadas · pedidos (se o usuário souber).

## Esqueleto sugerido

1. **Endereçamento e qualificação** (com placeholders `[COMPLETAR]`).
2. **Breve resumo dos fatos** (linha do tempo).
3. **Fundamentos** — por tese, em blocos: premissa fática → norma →
   interpretação → jurisprudência (marcar **PESQUISAR** quando não houver citação
   segura).
4. **Pedidos** — principal, subsidiários, alternativos; tutelas com **fumus**,
   **periculum** e **reversibilidade** quando cabível.
5. **Valor da causa** (se aplicável) e requerimentos finais (provas, intimações).

## Por cada tese central

2–3 argumentos | dispositivos legais prováveis | contra-argumento esperado |
linha de refutação | provas que sustentam.

## Checklist pré-protocolo

Anexos · custas/preparo · cálculo atualizado · comprovantes · procuração ·
declaração de hipossuficiência/honorários · prazo · competência.

## Saída

Estrutura em markdown, seções numeradas, com placeholders e marcações
**PESQUISAR**/`[COMPLETAR]` + **lista de pendências**. Modelos de esqueleto por
tipo de peça em `references/esqueletos-pecas.md`.
