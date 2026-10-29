---
name: embargos-declaracao-contrarrazoes
description: "Use SEMPRE que for preciso OPOR EMBARGOS DE DECLARAÇÃO (contra sentença, decisão interlocutória, decisão monocrática ou acórdão — omissão, contradição, obscuridade, erro material, prequestionamento) ou REDIGIR CONTRARRAZÕES / RESPOSTA a recurso da parte contrária (apelação, agravo de instrumento, agravo interno, REsp/RE, recurso inominado) no processo CÍVEL. Também para RESPONDER a embargos de declaração com efeito modificativo. Triggers — \"opõe embargos de declaração dessa sentença\", \"a decisão foi omissa sobre X\", \"precisa prequestionar para o REsp\", \"faz as contrarrazões da apelação\", \"responde ao agravo\", \"contrarrazões ao recurso especial\", \"os embargos deles podem mudar a sentença, como respondo?\". NÃO confunda com `analise-sentenca` (decidir SE recorre), com o agente `recurso`/`apelacao-civel`/`agravo-instrumento` (recurso PRÓPRIO do cliente), com `peca-trabalhista` (ED e contrarrazões na Justiça do Trabalho — CLT 897-A e prazos próprios) nem com `defesa-jec-consumidor` (rito da Lei 9.099). RASCUNHO para revisão de advogado habilitado. Direito brasileiro (CPC/2015)."
---

# Embargos de declaração e contrarrazões (cível — CPC/2015)

Duas peças curtas que quase sempre se fazem com pressa. Os dois erros que custam caro são **embargos genéricos**
(multa por protelação e prequestionamento perdido) e **contrarrazões que só repetem a sentença** (perdem a chance de
levantar questões não preclusas).

## Parte A — Embargos de declaração

### A.1 Cabimento e prazo
| Item | Regra (texto conferido na base) |
|---|---|
| Contra o quê | **qualquer decisão judicial** (art. 1.022 do CPC) |
| Para quê | I — obscuridade ou contradição; II — omissão de ponto ou questão sobre o qual o juiz devia se pronunciar; III — erro material (art. 1.022) |
| Omissão "presumida" | a decisão é omissa se não se manifestar sobre tese de casos repetitivos/IAC aplicável ou se incorrer no art. 489, § 1º (fundamentação genérica) — art. 1.022, parágrafo único |
| Prazo | **5 dias** úteis, petição ao juiz com a indicação do vício; **sem preparo** (art. 1.023); litisconsortes com procuradores distintos têm prazo em dobro, salvo autos eletrônicos (art. 1.023, § 1º, c/c art. 229, § 2º) |
| Efeito | não suspendem a decisão; **interrompem** o prazo dos demais recursos (art. 1.026) |
| Contraditório | se o acolhimento puder modificar a decisão, o embargado é intimado para responder em 5 dias (art. 1.023, § 2º) |
| Juizado Especial | 5 dias, interrompem o prazo do recurso (arts. 48 a 50 da Lei 9.099/1995) |

### A.2 Método (uma linha por vício)
Para cada vício, preencha antes de redigir:

| # | Vício (art. 1.022, I, II ou III) | Onde está na decisão (trecho literal) | O que foi alegado e onde (fls./ID) | O que se pede que o juiz declare |
|---|---|---|---|---|

Sem trecho literal da decisão e sem a folha onde a questão foi suscitada, **não é omissão**: é inconformismo, e
inconformismo vai em recurso. Transcrições entre aspas: conferir com `conferir.py minuta.md --autos <pasta>`.

### A.3 Prequestionamento (para REsp/RE)
- Questão federal ou constitucional **não decidida** no acórdão não sobe: Súmula 282 do STF; ponto omisso sem
  embargos não pode ser objeto de RE (Súmula 356 do STF); questão não apreciada apesar dos embargos impede o REsp
  (Súmula 211 do STJ).
- **Prequestionamento ficto:** consideram-se incluídos no acórdão os elementos suscitados nos embargos, ainda que
  inadmitidos ou rejeitados, se o tribunal superior reconhecer o vício (art. 1.025). Por isso os embargos devem
  **nomear o dispositivo** e a tese, e o REsp deve alegar violação do art. 1.022.
- Embargos com propósito notório de prequestionar **não são protelatórios** (Súmula 98 do STJ).
- Não precisa ratificar o REsp já interposto se o julgamento dos embargos não alterar o resultado (Súmula 579 do STJ).
  A Súmula 418 do STJ (exigia ratificação) está **cancelada**.

### A.4 Riscos
- Multa de até 2% do valor atualizado da causa se manifestamente protelatórios; na reiteração, multa de até 10% e
  depósito prévio da multa para recorrer (art. 1.026, §§ 2º e 3º).
- Embargos contra decisão de relator podem ser conhecidos como agravo interno, com intimação para complementar as
  razões em 5 dias (art. 1.024, § 3º).

### A.5 Esqueleto
```
EXCELENTÍSSIMO(A) … / EGRÉGIO TRIBUNAL … (dirigido ao prolator — art. 1.023)
Autos nº [CNJ]
[CLIENTE], nos autos em epígrafe, vem opor EMBARGOS DE DECLARAÇÃO contra [decisão/sentença/acórdão de fls./ID],
com fundamento no art. 1.022, [incisos], do CPC, pelos motivos a seguir.
I.   TEMPESTIVIDADE (intimação em __; 5 dias úteis; vencimento __ — calculo-prazos-cpc)
II.  VÍCIO 1 — [OMISSÃO]: a decisão não examinou [questão], suscitada às fls. __ ("trecho"), relevante porque [efeito no resultado]
III. VÍCIO 2 — …
IV.  PREQUESTIONAMENTO (se for o caso): dispositivos [art. X da Lei Y] — art. 1.025 do CPC
V.   PEDIDO: acolher os embargos para [sanar o vício]; [com efeito modificativo, se o saneamento mudar o resultado,
     intimando-se o embargado — art. 1.023, § 2º]
```

## Parte B — Contrarrazões

### B.1 Prazos
| Recurso da parte contrária | Prazo da resposta |
|---|---|
| Apelação | 15 dias (art. 1.010, § 1º) |
| Agravo de instrumento, agravo interno, REsp/RE e demais (exceto ED) | 15 dias (art. 1.003, § 5º; agravo interno: art. 1.021, § 2º; REsp/RE: art. 1.030) |
| Embargos de declaração com efeito modificativo | 5 dias (art. 1.023, § 2º) |
| Recurso inominado (JEC) | 10 dias (art. 42, § 2º, da Lei 9.099/1995) |

Todos em dias úteis — rodar `calculo-prazos-cpc`.

### B.2 Método
1. **Admissibilidade primeiro** (preliminar de não conhecimento): tempestividade, preparo (deserção — art. 1.007),
   regularidade formal (razões que não atacam os fundamentos da decisão), interesse, cabimento.
2. **Questões não preclusas a favor do cliente:** as resolvidas na fase de conhecimento sem agravo de instrumento
   podem ser suscitadas nas contrarrazões (art. 1.009, § 1º). Se o cliente também perdeu em algum ponto, avaliar
   recurso adesivo, que segue a sorte do principal (art. 997, § 2º).
3. **Rebater fundamento por fundamento**, com a mesma numeração das razões do recorrente (tabela "razão do recorrente
   × resposta × prova/folha"). Não basta pedir a manutenção da sentença "por seus próprios fundamentos".
4. **Honorários recursais:** pedir a majoração em caso de desprovimento (art. 85, § 11 — ler o teor antes de citar).
5. No REsp/RE: apontar óbices de admissibilidade conferidos (ex.: reexame de prova — Súmula 7 do STJ; falta de
   prequestionamento — Súmula 211 do STJ / Súmula 282 do STF). No JEC: não cabe REsp contra a Turma Recursal
   (Súmula 203 do STJ).

### B.3 Esqueleto
```
CONTRARRAZÕES DE [APELAÇÃO/AGRAVO/…]
Recorrente: … | Recorrido: [CLIENTE] | Autos nº …
I.   SÍNTESE DO RECURSO (pontos atacados, numerados)
II.  PRELIMINAR DE NÃO CONHECIMENTO (se houver)
III. QUESTÕES DO ART. 1.009, § 1º (se houver)
IV.  MÉRITO — resposta ponto a ponto (mesma numeração do recurso)
V.   PEDIDOS: não conhecimento; subsidiariamente desprovimento; majoração dos honorários (art. 85, § 11)
```

## Fecho obrigatório
1. `conferencia-citacoes-fm` (`conferir.py minuta.md --autos <pasta>`): citações **e** trechos entre aspas da
   decisão/das razões.
2. `calculo-prazos-cpc` (prazo da peça).
3. `acuracia-juridica`.

Toda peça é rascunho: revisão e assinatura do advogado responsável.
