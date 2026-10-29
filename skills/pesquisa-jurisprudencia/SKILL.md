---
name: pesquisa-jurisprudencia
description: Use SEMPRE que o usuário pedir para PESQUISAR, MAPEAR ou ESTRUTURAR JURISPRUDÊNCIA sobre uma tese/tema — montar roteiro de busca, mapa argumentativo (teses a favor e contra), strings e operadores de busca para tribunais/buscadores, âncoras (súmulas, temas repetitivos, IRDR), tendência do entendimento e probabilidade qualitativa. Consulte esta skill ANTES de pesquisar jurisprudência, para seguir o método padronizado (mapeamento de teses, hierarquia STF/STJ/TJ, strings sugeridas, filtros, panorama e estratégia). NÃO invente números de processo nem ementas — as citações de julgados devem ser CONFERIDAS pelo advogado nas fontes oficiais. Triggers — "pesquisa jurisprudência sobre X", "como está o entendimento dos tribunais sobre Y?", "monta as strings de busca pra esse tema", "que súmula/tema repetitivo se aplica?", "qual a tendência do STJ sobre isso?", "mapeia os argumentos a favor e contra essa tese". É um produto de PESQUISA/estratégia — roteiro auxiliar que SEMPRE exige validação em fonte oficial antes de peticionar. NÃO confunda com `consulta-apis-juridicas` (que CONSULTA ao vivo andamento/dados de um processo específico via API), com `consultar-rag` (acervo interno do escritório) nem com `consultar-legislacao` (lei seca). Direito brasileiro.
---

# Pesquisa e mapeamento de jurisprudência — Brasil

Estrutura um **roteiro de pesquisa jurisprudencial** e um **mapa argumentativo**.
Sintetiza conhecimento geral, mas **citações de julgados devem ser conferidas**
pelo advogado nas fontes oficiais — **não invente número de processo nem ementa**.

## Natureza e guardrails

- **Roteiro, não verdade pronta.** Entrega estratégia e strings; o julgado
  concreto é localizado e validado pelo advogado.
- **Sem invenção.** Nunca crie nº de processo, relator ou ementa. Quando não
  tiver certeza, descreva o **tema/tribunal** e marque "localizar decisão
  semelhante / confirmar vigência".
- **Integração.** Súmulas/temas e legislação de apoio → `consultar-legislacao`.
  Para puxar julgado/andamento ao vivo, é a `consulta-apis-juridicas`. Para
  precedentes do acervo do escritório, `consultar-rag`.
- **Probabilidade qualitativa** (alta/média/baixa) com fatores — nunca garantia.
  Feche pela `acuracia-juridica`.

## Entrada ideal do usuário

Tese ou pedido · área · tribunal competente provável · fatos em 5–10 linhas ·
peça (inicial, agravo, recurso). Se faltar, pergunte **uma vez** o nível (1º/2º
grau, STJ, STF) e o ano mínimo desejado.

## Mapeamento inicial

- **Teses a favor e contra** (bullets).
- **Hierarquia**: STF/STJ (uniformização) → TJ/TRT/TRE conforme a matéria.
- **Âncoras**: súmulas, OJs, IRDR, **tema repetitivo/repercussão geral** quando
  aplicável (mencionar "confirmar vigência").

## Estratégia de busca (entregue ao advogado)

- **Strings sugeridas** (3–8 variações), sinônimos e latinismos usuais.
- **Operadores** (E/OU, aspas, exclusão) para JusBrasil, Escavador e sites de
  tribunal.
- **Filtros**: período, câmara/órgão, tipo de recurso, relator (se útil).

## Para cada tese (até 5 principais)

Nome da tese | resumo do entendimento | argumentos centrais | **tendência**
(consolidada / em mudança / divergente entre câmaras) | contra-argumentos | "o
que o juiz costuma olhar".

## Relatório final

- Panorama em 1 parágrafo.
- **Estratégia**: ordem dos argumentos e pedidos subsidiários.
- **Precedentes-chave**: Tribunal, órgão, tema (sem número se não tiver certeza)
  + "localizar decisão semelhante".
- **Probabilidade qualitativa** (alta/média/baixa) com **fatores** (provas,
  jurisprudência dominante, prescrição) — não como garantia.

## Saída

Mapa argumentativo + strings/filtros + relatório final + ressalva "validar em
fonte oficial antes de peticionar". Guia de busca por base em
`references/guia-busca-jurisprudencia.md`.
