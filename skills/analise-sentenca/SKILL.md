---
name: analise-sentenca
description: Use SEMPRE que o usuário pedir para ANALISAR uma DECISÃO JUDICIAL (sentença, acórdão, decisão interlocutória, despacho decisório) sob a ótica de VIABILIDADE e ESTRATÉGIA RECURSAL — identificar pontos desfavoráveis recorríveis, cabimento e timing do recurso, força de reforma, risco de reformatio in pejus e recomendação recorrer/negociar/não recorrer. Consulte esta skill ANTES de opinar sobre recurso, para seguir o método padronizado (síntese fiel da decisão, tabela recursal ponto a ponto, cabimento via CPC em `consultar-legislacao`, prazo via `calculo-prazos-cpc`, precedentes via `pesquisa-jurisprudencia`/`consulta-apis-juridicas` e checagem de acurácia). NÃO invente trechos da decisão. Triggers — "vale a pena recorrer dessa sentença?", "analisa esse acórdão pra apelação", "que pontos dá pra atacar nessa decisão?", "cabe agravo ou embargos aqui?", "qual a chance de reforma?", "esse despacho é recorrível?". É um produto ESTRATÉGICO a favor do cliente, mas honesto quanto a chances — RASCUNHO para decisão do advogado, sem garantir resultado. NÃO confunda com `analise-peca-adversa` (peça da parte contrária, não decisão do juiz), com `redacao-defesa` (minuta de peça) nem com `relatorio-juridico` (descrição imparcial do processo). Direito brasileiro (CPC, recursos).
---

# Análise de sentença e viabilidade recursal — Brasil

Mapeia, a partir de uma **decisão judicial**, o **cabimento**, os **pressupostos**
e a **estratégia recursal**. O texto da decisão deve ser fornecido ou resumido
com fidelidade — **não invente trechos**.

## Natureza e guardrails

- **Estratégico, mas honesto.** Trabalha pelo cliente, porém a força de reforma e
  a probabilidade são **qualitativas** (alta/média/baixa) — nunca garantia.
- **Fidelidade à decisão.** Cite só o que está na decisão; o que não constar,
  marque "(não consta / confirmar nos autos)".
- **Fundamente o cabimento.** Para artigos do CPC (apelação, agravo, embargos,
  RE/REsp, prazos), use `consultar-legislacao`. Precedentes a pesquisar entram
  como **roteiro** (não invente número de processo).
- **Rascunho.** Decisão de recorrer é do **cliente** assessorado pelo advogado.
  Passe a análise pela `acuracia-juridica`.

## Pipeline

1. **Ingestão** — decisão em PDF/DOCX → `formatacao-arquivos-juridicos`.
2. **Síntese** fiel da decisão.
3. **Tabela recursal** ponto a ponto.
4. **Cabimento e timing** — `consultar-legislacao` (CPC) + `calculo-prazos-cpc`
   para o prazo recursal (confirmar publicação/intimação).
5. **Precedentes** — roteiro com `pesquisa-jurisprudencia`; andamento/peças com
   `consulta-apis-juridicas` ou `consultar-rag` se for processo do acervo.
6. **Recomendação** + `acuracia-juridica`.

## 1. Síntese da decisão

- Resultado (procedente / improcedente / parcial) e **dispositivo**.
- **Fundamentos centrais** do julgador (separar fato e direito).
- O que foi **explicitamente** decidido vs deixado de lado (omissão →
  embargos de declaração?).

## 2. Pontos desfavoráveis — tabela recursal

Para cada ponto: natureza (erro de **direito** / **fato** / **processual** /
**ausência de prova**) | Fundamento de ataque | **Precedentes a pesquisar**
(tribunal/nível) | Força de reforma (alta/média/baixa) | Risco de **reformatio
in pejus** (se aplicável).

## 3. Cabimento e timing

- Recurso adequado (apelação, agravo de instrumento, embargos de declaração,
  RE/REsp se houver hipótese de cabimento).
- **Prazo** via `calculo-prazos-cpc` — sempre com a ressalva "confirmar
  publicação e contagem".
- Efeitos (suspensivo / devolutivo / sem efeito suspensivo automático).

## 4. Estratégia

- Ordem dos ataques (preliminar/prejudicial antes do mérito).
- Pedidos **subsidiários**; cenário de **acordo** ou **cumprimento parcial**.

## 5. Recomendação

- **Recorrer / negociar / não recorrer**, com custo-benefício qualitativo.
- Perguntas que o advogado deve fazer ao cliente antes de assinar o recurso.

## Saída

Análise estruturada (1–5) + tabela recursal + recomendação + ressalva de prazo e
de "sem garantia de resultado". Mapa de recursos e prazos em
`references/mapa-recursos-cpc.md`.
