---
name: excecao-pre-executividade
description: "Use SEMPRE que o cliente for EXECUTADO (execução de título extrajudicial, cumprimento de sentença ou EXECUÇÃO FISCAL) e houver vício que o juiz pode reconhecer DE OFÍCIO e que se prova SÓ COM DOCUMENTO — prescrição (inclusive intercorrente), decadência, nulidade do título (falta de certeza, liquidez ou exigibilidade), falta ou nulidade de citação, ilegitimidade, pagamento documentado, CDA nula — para decidir se cabe EXCEÇÃO (OBJEÇÃO) DE PRÉ-EXECUTIVIDADE em vez de embargos/impugnação e redigi-la. Especialmente útil quando não há garantia do juízo na execução fiscal ou quando o prazo dos embargos já passou. Triggers — \"cabe exceção de pré-executividade?\", \"a execução está prescrita\", \"o título não é exigível\", \"o cliente não foi citado e já bloquearam a conta\", \"execução fiscal sem garantia, como defender?\", \"perdemos o prazo dos embargos\". NÃO confunda com o agente `embargos-execucao-fiscal` (defesa com garantia, art. 16 da LEF), com `impugnacao-cumprimento-sentenca` (defesa típica do art. 525 do CPC) nem com `execucao-recuperacao-ativos` (lado do CREDOR). RASCUNHO para revisão de advogado habilitado. Direito brasileiro (CPC/2015, LEF, CTN, CC)."
---

# Exceção (objeção) de pré-executividade

Não há artigo de lei com esse nome: é construção da doutrina e da jurisprudência, admitida para **matéria de ordem
pública** que o juiz conhece de ofício e que **não exige produção de prova**. A âncora escrita está em três lugares:

| Âncora | Texto conferido na base |
|---|---|
| Execução fiscal | Súmula 393 do STJ: admissível na execução fiscal para matérias conhecíveis de ofício que não demandem dilação probatória |
| Execução de título extrajudicial | art. 803 do CPC: é nula a execução se o título não corresponder a obrigação certa, líquida e exigível (I), se o executado não foi regularmente citado (II) ou se instaurada antes da condição/termo (III); parágrafo único: a nulidade é pronunciada de ofício ou a requerimento, **independentemente de embargos** |
| Cumprimento de sentença | art. 518 do CPC: questões de validade do procedimento e dos atos executivos podem ser arguidas nos próprios autos |

## 1. Filtro: exceção, embargos ou impugnação?

Responda às 3 perguntas. Exceção só se as três forem "sim":

1. **O juiz poderia reconhecer sozinho?** (prescrição, decadência, nulidade do título, citação, ilegitimidade,
   pressupostos processuais — art. 485, § 3º, do CPC, que manda conhecer de ofício os incisos IV, V, VI e IX)
2. **Prova-se só com documento já disponível?** (certidão, comprovante de pagamento, a própria CDA, cálculo de datas)
3. **A via típica é pior agora?**
   - Execução fiscal: os embargos exigem garantia (art. 16, § 1º, da Lei 6.830/1980) → exceção não exige.
   - Título extrajudicial: os embargos **independem de penhora** (art. 914 do CPC) e têm prazo de 15 dias (art. 915)
     → dentro do prazo e com matéria ampla, prefira embargos; exceção para matéria de ordem pública fora do prazo.
   - Cumprimento de sentença: a impugnação (art. 525) também não exige garantia; exceção para vício surgido depois ou
     matéria do art. 518.

Se a tese depende de perícia, testemunha ou discussão de cláusula contratual (ex.: excesso de execução por juros
abusivos) → **não é exceção**: embargos/impugnação. Exceção usada fora do lugar é rejeitada e gasta credibilidade.

## 2. Matérias típicas e como provar

| Matéria | Fundamento | Prova que vai junto |
|---|---|---|
| Prescrição do crédito civil | CC arts. 205/206 (prazo da pretensão) e 202 (interrupção, uma única vez) | linha do tempo: vencimento → ajuizamento → despacho que ordenou a citação |
| Prescrição do crédito tributário | CTN art. 174 (5 anos da constituição definitiva; interrupção pelo despacho que ordena a citação) | data da constituição (notificação/declaração), data do despacho |
| Prescrição intercorrente — execução civil | CPC art. 921: suspensão de 1 ano (§ 1º); termo inicial na ciência da primeira tentativa infrutífera (§ 4º); reconhecimento de ofício, ouvidas as partes em 15 dias (§ 5º) | extrato do andamento com as tentativas e as datas |
| Prescrição intercorrente — execução fiscal | Lei 6.830/1980, art. 40 + Súmula 314 do STJ (1 ano de suspensão, depois corre a quinquenal); Temas 566 a 571 do STJ (REsp 1.340.553 — conferir a tese no site do STJ antes de citar) | idem |
| Título sem certeza/liquidez/exigibilidade | CPC art. 803, I | o próprio título; ausência de assinaturas/testemunhas; condição não implementada (art. 803, III) |
| Falta ou nulidade de citação | CPC art. 803, II | AR/certidão do oficial; endereço errado documentado |
| Ilegitimidade passiva | CPC art. 485, VI e § 3º | contrato social, certidão da junta, contrato que prova outro devedor |
| Pagamento | documento bancário inequívoco | comprovante + correspondência com o débito executado |
| CDA nula (execução fiscal) | requisitos da CDA na Lei 6.830/1980 (art. 2º — ler o teor) | a própria CDA |

## 3. Esqueleto

```
EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) …
Autos nº [CNJ] — Execução [de título extrajudicial / fiscal / cumprimento de sentença]
[CLIENTE], executado, vem apresentar EXCEÇÃO DE PRÉ-EXECUTIVIDADE, com fundamento [no art. 803 do CPC /
na Súmula 393 do STJ / no art. 518 do CPC], pelos motivos a seguir.
I.   CABIMENTO (matéria de ordem pública + prova pré-constituída; dispensa de garantia)
II.  [MATÉRIA 1 — ex.: PRESCRIÇÃO]: linha do tempo em tabela, com o documento de cada data
III. [MATÉRIA 2 …]
IV.  TUTELA (se houver constrição): liberação do valor/bem bloqueado enquanto se decide — demonstrar a urgência
V.   PEDIDOS: acolher a exceção para extinguir a execução [total/parcialmente]; levantar as constrições;
     condenar o exequente em honorários (pesquisar o entendimento atual sobre honorários na exceção acolhida antes de
     citar precedente); subsidiariamente, [pedido menor]
```

## 4. Cuidados

- A exceção **não suspende** a execução por si: se houver bloqueio, pedir a liberação de forma expressa e fundamentada.
- Não misturar matérias: uma tese que exige prova contamina o pedido inteiro. Se houver as duas, exceção para a de
  ordem pública e embargos/impugnação para o resto, no prazo.
- Datas são o coração da prescrição: calcular com `calculo-prazos-cpc` quando for prazo processual e montar a linha
  do tempo com o documento de cada data (folha/ID).
- Temas repetitivos do STJ e REsp **não estão na base local**: conferir no site do STJ antes de citar o número.

## 5. Fecho obrigatório
1. `conferencia-citacoes-fm` (`conferir.py minuta.md --autos <pasta>`).
2. `acuracia-juridica` (cada data da linha do tempo × documento).

Toda peça é rascunho: revisão e assinatura do advogado responsável.
