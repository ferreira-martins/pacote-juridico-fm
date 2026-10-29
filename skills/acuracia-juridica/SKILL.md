---
name: acuracia-juridica
description: "Use como etapa de revisão final de qualquer relatório, parecer, minuta ou análise jurídica — para garantir acurácia, fidelidade às fontes e total imparcialidade antes da entrega. Mais que um checklist: EXTRAI cada citação legal/jurisprudencial (artigo, súmula, tema, precedente) e cada dado factual (data, valor, CNJ, dispositivo de decisão) numa tabela e VERIFICA um a um contra a fonte, marcando o que não fecha. Reprova o texto que contiver citação inventada, dado sem lastro ou viés de tese. Verifica que o texto descreve o processo sem advogar (nos produtos imparciais) ou, nos produtos parciais (defesa/contrato), que a tese se apoia em fundamento real e verificado."
---

# Acurácia jurídica, verificação de citações e imparcialidade

Etapa de controle de qualidade — **a última antes de entregar**. Aplique a
qualquer relatório, parecer, minuta de defesa ou análise contratual. O risco
nº 1 de um produto jurídico de IA é a **citação plausível mas falsa** (artigo
que não existe, súmula com número trocado, precedente inventado) e o **dado sem
lastro** (data, valor ou dispositivo que não está nos autos). Esta skill caça
exatamente esses dois.

## Posição no fluxo — relatórios de carteira

Em relatórios de carteira, esta skill é a **revisão global final** sobre o documento
consolidado. Ela roda **depois** da [[verificacao-ficha-processo]], que já executou o QA
adversarial âncora a âncora de cada processo contra os autos completos (emitindo
`{cnj}.qa.json` por CNJ antes da montagem). Aqui o foco muda: verificar as **citações
legais e jurisprudenciais** usadas na análise transversal, assegurar **imparcialidade**
da redação e **coerência entre fichas**. Esta skill não é a verificação primária por
processo — é a última barreira antes da entrega.

## Como funciona — verificar, não só conferir

A versão antiga era um checklist passivo ("confira as citações"). O problema:
pedir ao modelo que "confira" o que ele mesmo escreveu raramente pega a
alucinação — ele tende a reafirmar. Por isso aqui o trabalho é **ativo e
externalizado**: tudo o que pode ser falso vira **linha de uma tabela**, e cada
linha recebe um **veredito** com a fonte. O que não puder ser verificado **não
passa como verdade** — vira ressalva visível.

### Passo 1 — Extrair tudo que é verificável

Varra o texto e extraia, para uma tabela de verificação, **toda**:

- **Citação legal** — artigo, inciso, parágrafo de lei/código (CPC, CC, CDC,
  CLT, LGPD, CF, leis esparsas).
- **Citação jurisprudencial** — súmula (STF/STJ/TST/vinculante), tema
  repetitivo/de repercussão geral, enunciado, acórdão/precedente nominado.
- **Dado factual de fonte** — datas, valores (causa, condenação, multa), nº
  CNJ, nomes das partes, e o **dispositivo** de cada decisão (procedente/
  improcedente, extensão, condenações).

### Passo 2 — Verificar cada linha

Para cada item, atribua um veredito e a base:

| Item | Tipo | O que o texto afirma | Verificação | Veredito |
|---|---|---|---|---|
| CDC art. 51, IX | lei | cláusula abusiva | confere com o texto da lei | ✅ confirma |
| Súmula 297 STJ | súmula | aplica CDC a bancos | confere enunciado | ✅ confirma |
| Tema 1.234 STJ | tema | (citado no parecer) | não localizado | ❌ não confirma |
| R$ 48.000 (valor da causa) | fato | consta da inicial | não achei nos autos | ⚠️ sem lastro |

Vereditos possíveis:
- ✅ **Confirma** — a fonte sustenta exatamente o que o texto diz.
- ⚠️ **Impreciso** — existe, mas o texto distorce (número do artigo certo,
  conteúdo descrito errado; súmula real aplicada fora do seu alcance).
- ❌ **Não confirma / não localizado** — não foi possível achar a fonte, ou ela
  diz outra coisa. **Trata-se como provável alucinação até prova em contrário.**

Como verificar, por ordem de preferência:
1. **Fonte nos autos / no documento** (para dados factuais) — confronte com o
   texto-fonte já em mãos; se o documento estiver no acervo, recupere via
   [[consultar-rag]] ou [[consulta-dados-internos]].
2. **Fonte oficial da norma** — para **lei seca federal** (CF, CPC, CC, CDC,
   CLT, CTN, CTB, LGPD, ECA, Improbidade, Licitações, Locações, Cheque,
   Recuperação Judicial, Estatuto da Terra, Código Florestal, LINDB etc.),
   confira o dispositivo via [[consultar-legislacao]] — busca o artigo na
   biblioteca do Planalto indexada e devolve o trecho real para conferência.
   Para **súmula, tema repetitivo/repercussão geral e jurisprudência**, ou lei
   **não indexada** (estadual/municipal/esparsa fora da biblioteca), use
   [[consulta-apis-juridicas]] / web (STF/STJ/TST, banco de repetitivos).
   Registre a fonte/URL.
3. **Sem acesso à fonte?** Então **não** marque ✅. Rebaixe para ⚠️/❌ e
   sinalize "não verificável neste ambiente — conferir manualmente".

### Passo 3 — Fechar (fail-closed)

- Todo item ❌ **deve** ser corrigido (removido, substituído por fonte real) ou
  rebaixado no texto a marcador explícito: `[citar precedente — verificar]`,
  `[dispositivo a confirmar]`, `[dado não localizado nos autos]`.
- Nunca "aprove" um texto deixando um ❌ disfarçado de afirmação. Na dúvida
  entre afirmar e ressalvar, **ressalve** (regra de ouro, abaixo).
- Entregue a tabela de verificação junto, ou ao menos um resumo
  ("N citações verificadas: X ✅, Y ⚠️, Z ❌ corrigidas").

## Checklist de acurácia (após a verificação)

- [ ] Toda citação legal/jurisprudencial passou pela tabela do Passo 1-2.
- [ ] Nenhum item ❌ sobrou como afirmação — todos corrigidos ou marcados.
- [ ] Cada afirmação de fato rastreia até uma fonte (peça + folha/página).
- [ ] Transcrições são literais; sínteses estão marcadas como síntese.
- [ ] Datas, números de processo, valores e nomes conferidos contra os autos.
- [ ] Dispositivos de decisões reproduzidos com precisão (procedente/
      improcedente, extensão, condenações).
- [ ] Lacunas explicitadas como "não localizado nos autos", nunca preenchidas
      por suposição.

## Checklist de imparcialidade

> Aplica-se em peso aos produtos **descritivos** ([[relatorio-juridico]]). Nos
> produtos **parciais por desenho** ([[redacao-defesa]], [[analise-contratual]],
> [[analise-peca-adversa]]) o texto **deve** advogar por um lado — aqui o teste
> muda: a tese pode ser parcial, mas **cada fundamento dela** tem de ser real e
> verificado (Passos 1-3), e o texto não pode **deturpar o fato** para caber na
> tese.

- [ ] (Descritivo) O texto **descreve** o processo; não defende uma das partes.
- [ ] (Descritivo) Pedidos do autor e defesa do réu com igual profundidade.
- [ ] (Descritivo) Pontos fortes e fracos de cada lado expostos de forma
      equilibrada; cenários (favorável/desfavorável) sem viés de torcida.
- [ ] Linguagem proporcional: adjetivo valorativo ("absurdo", "evidente",
      "frágil") só quando transcrito da fonte.
- [ ] Inferências do redator separadas dos fatos e marcadas como inferência.
- [ ] (Parcial) A parcialidade está **declarada** (a favor de quem) e nenhum
      fato foi distorcido para sustentar a tese.

## Distinção de camadas

Mantenha sempre separados e rotulados:
1. **Fato** — o que consta dos autos.
2. **Alegação** — o que uma parte afirma.
3. **Decisão** — o que o juízo determinou.
4. **Inferência** — leitura analítica do redator.

## Regra de ouro

Na dúvida entre afirmar e ressalvar, **ressalve**. Um produto jurídico erra por
excesso de cautela, nunca por excesso de certeza. Se a fonte não sustenta a
frase, reescreva a frase. Uma citação que você não conseguiu verificar é um
passivo, não um enfeite — prefira removê-la a arriscar a credibilidade do
escritório.
