---
name: notificacao-extrajudicial
description: Use SEMPRE que o usuário pedir para REDIGIR uma NOTIFICAÇÃO ou INTERPELAÇÃO EXTRAJUDICIAL — cobrança de dívida, constituição em mora, rescisão/distrato, vício redibitório, cessação de uso (marca, direito autoral, concorrência desleal), exigência de retratação ou interpelar a parte a cumprir obrigação — mesmo que o caso pareça simples e mesmo que você ache que poderia escrever direto. Consulte esta skill ANTES de minutar, para garantir o método padronizado do escritório (qualificação completa, síntese fática sem retórica ofensiva, fundamento legal com dispositivo específico via `consultar-legislacao`, pedido mensurável, prazo explícito em dias úteis/corridos, advertência de medidas cabíveis sem tipificar crime indevidamente e checagem de acurácia). Triggers — "redige uma notificação extrajudicial de cobrança", "preciso notificar o fornecedor que descumpriu o prazo", "manda uma interpelação pra constituir em mora", "notifica pra cessar o uso da marca", "exige retratação desse cliente", "minuta de distrato com notificação". É um produto PARCIAL (escreve a favor do notificante) e um RASCUNHO para revisão de advogado habilitado (OAB) antes do envio. NÃO confunda com `redacao-defesa` (peças processuais) nem com `analise-contratual` (revisão de contrato existente). Direito brasileiro (CC, CDC, CPC, Lei da Propriedade Industrial).
---

# Notificação / interpelação extrajudicial — Brasil

Redige notificação extrajudicial a favor do **notificante**: tom profissional e
assertivo, fundamentação legal específica, pedido mensurável e prazo claro. A
saída é um **rascunho de trabalho** — exige revisão de advogado habilitado (OAB)
e conferência de valores/datas **antes do envio**.

## Natureza e guardrails (leia antes)

- **Produto parcial.** Trabalha pelo notificante, mas em tom **profissional** —
  sem insulto, sem ameaça de crime salvo hipótese típica e com redação cuidadosa.
- **Não invente dispositivo legal.** Para citar lei federal indexada (CC, CDC,
  CPC, Lei do Cheque, Lei de Locações etc.), busque o **texto vigente do artigo**
  em `consultar-legislacao` e fundamente a partir do trecho real. Lei não
  indexada (ex.: Lei da Propriedade Industrial) ou dúvida sobre o número →
  marque "(verificar dispositivo)" em vez de chutar.
- **Revisão obrigatória.** Termine sempre passando a minuta pela
  `acuracia-juridica` (verifica citações e dados) e entregue com a advertência de
  "não enviar sem conferir valores, datas e qualificação".

## Pipeline

1. **Ingestão** — se houver contrato, e-mails ou comprovantes em PDF/DOCX, use
   `formatacao-arquivos-juridicos` para extrair texto fiel; cite as provas como
   anexos na notificação.
2. **Classifique o pedido** — dívida (título/contrato/inadimplemento) ·
   rescisão/distrato/vício redibitório · propriedade intelectual (marca, direito
   autoral, concorrência desleal) · interpelar para cumprir obrigação ou
   caracterizar **mora** · retratação (conteúdo exato a retirar/corrigir).
3. **Fundamento** — levante o dispositivo em `consultar-legislacao` (evite "nos
   termos da legislação vigente" sozinho).
4. **Prazo** — defina prazo coerente (5 a 30 dias) e diga **explicitamente**
   "úteis" ou "corridos". Se o prazo for processual/legal, confirme a contagem
   com `calculo-prazos-cpc`.
5. **Revisão** — `acuracia-juridica`.

## Estrutura padrão

1. Título e **qualificação completa** das partes e advogados (OAB se constar).
2. **Síntese fática** cronológica, sem retórica ofensiva, com referência a provas.
3. **Fundamento jurídico** com dispositivos **específicos**.
4. **Pedido** mensurável: pagar X, cumprir Y, cessar Z até data.
5. **Prazo** explícito (úteis/corridos).
6. **Advertência** de medidas judiciais **cabíveis**, sem especular pena de crime.
7. Local, data, assinatura; menção a anexos.

## Níveis de tom (pergunte ao usuário)

- **1 Amigável** — cooperação, solução consensual.
- **2 Firme** — formal, prazo, consequências.
- **3 Contencioso** — mora, medidas liminares possíveis (sem garantir deferimento).

## Prova de envio (oriente o cliente)

AR · **Cartório de Títulos e Documentos** · e-mail com confirmação de leitura
(avaliar validade) · entrega com protocolo. Registrar **cópia** para o processo futuro.

## Saída

Minuta completa + **checklist de fatos a conferir** (valores, datas,
qualificação) + lembrete "não enviar sem revisão do advogado". Modelos por tipo
em `references/modelos-notificacao.md`.
