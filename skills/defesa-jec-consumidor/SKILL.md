---
name: defesa-jec-consumidor
description: "Use SEMPRE que a EMPRESA cliente for RÉ no JUIZADO ESPECIAL CÍVEL (Lei 9.099/1995) — em geral ação de consumidor por cobrança indevida, negativação, vício/defeito de produto ou serviço, dano moral — para montar a DEFESA: contestação escrita para a audiência, carta de preposição, checklist de provas e da audiência, pedido contraposto e, perdida a causa, RECURSO INOMINADO (10 dias úteis + preparo em 48 h) ou embargos de declaração no JEC. Triggers — \"a empresa foi citada no juizado\", \"contestação no JEC\", \"ação de consumidor no juizado especial\", \"audiência de conciliação no JEC, o que levar?\", \"preposto no juizado\", \"recurso inominado dessa sentença\", \"cliente condenado em dano moral no juizado\". Polo: fornecedor/empresa. NÃO confunda com o agente `acao-cdc-pratica-abusiva` (lado do CONSUMIDOR), com `redacao-defesa` (rito comum do CPC) nem com `embargos-declaracao-contrarrazoes` (ED/contrarrazões fora do JEC). RASCUNHO para revisão de advogado habilitado. Direito brasileiro (Lei 9.099/95, CDC, CPC subsidiário)."
---

# Defesa da empresa no Juizado Especial Cível (Lei 9.099/1995)

O JEC é rápido e oral, e quase todo erro da empresa é de forma: preposto sem carta, ausência na audiência, prova
deixada para depois. Primeiro garanta a forma, depois discuta o mérito.

## 0. Antes de tudo: o que perde a causa sem discutir mérito

| Risco | Regra | O que fazer |
|---|---|---|
| Não comparecer à conciliação ou à instrução | art. 20 da Lei 9.099/1995: presumem-se verdadeiros os fatos da inicial | confirmar data/hora/link D-7 e D-1; preposto + advogado |
| Preposto sem poderes | art. 9º, § 4º, da Lei 9.099/1995: PJ pode ser representada por preposto credenciado, com carta de preposição **com poderes para transigir**, sem vínculo empregatício | carta assinada por quem tem poderes no contrato social, com poder de transigir |
| Prova não levada | art. 33 da Lei 9.099/1995: todas as provas são produzidas na audiência de instrução | contestação e documentos juntados antes ou levados na audiência; até 3 testemunhas por parte, levadas pela empresa ou intimadas a pedido feito no mínimo 5 dias antes da instrução (art. 34, § 1º) |
| Reconvenção | art. 31 da Lei 9.099/1995: não cabe; cabe **pedido contraposto** fundado nos mesmos fatos, nos limites do art. 3º | se a empresa tem crédito com o autor pelos mesmos fatos, pedir na contestação |
| Prazo | art. 12-A da Lei 9.099/1995: prazos em **dias úteis** | rodar `calculo-prazos-cpc` |

## 1. Triagem da inicial (15 minutos)

1. **Competência** — valor até 40 salários mínimos (art. 3º, I) e causa de menor complexidade. Se o caso exige
   perícia complexa (ex.: vício técnico que só laudo resolve), alegar incompatibilidade com o rito — art. 51, II
   (extinção quando inadmissível o procedimento) e art. 35 (o juiz só ouve técnico de confiança, não há perícia formal).
2. **Legitimidade** — a empresa é mesmo a fornecedora? Há outro da cadeia (fabricante, marketplace, banco)?
3. **Prazo do consumidor** — vício aparente: decadência de 30/90 dias (CDC art. 26); fato do produto/serviço:
   prescrição de 5 anos (CDC art. 27). Contar a partir da entrega/término do serviço.
4. **Inversão do ônus da prova** — CDC art. 6º, VIII: depende de verossimilhança ou hipossuficiência, a critério do
   juiz. Não é automática; se não houve decisão invertendo, dizer isso.
5. **Pedido de dano moral** — há fato concreto além do aborrecimento? Há negativação anterior legítima
   (Súmula 385 do STJ afasta o dano moral)?

## 2. Contestação (escrita, para juntar antes ou entregar na audiência)

Toda a defesa vai nela, exceto suspeição/impedimento (art. 30 da Lei 9.099/1995). Estrutura:

```
EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE [COMPLETAR]
Autos nº [CNJ]
[EMPRESA], [qualificação], por seu advogado, vem apresentar CONTESTAÇÃO …

I.   SÍNTESE DA INICIAL (pedidos numerados, valor)
II.  PRELIMINARES (só as que cabem: incompetência/complexidade; ilegitimidade; decadência/prescrição;
     inépcia; falta de interesse — ex.: problema já resolvido antes da ação)
III. DOS FATOS PELA EMPRESA (cronologia com documento para cada fato: protocolo, tela de sistema, e-mail,
     nota fiscal, gravação de atendimento)
IV.  DO MÉRITO
     – inexistência do defeito ou culpa exclusiva do consumidor ou de terceiro (CDC art. 14, § 3º; art. 12, § 3º)
     – vício sanado no prazo de 30 dias (CDC art. 18, § 1º) ou oferta de solução recusada
     – cobrança/negativação devida (contrato + inadimplência + notificação prévia)
     – dano moral: ausência de lesão a direito da personalidade; mero aborrecimento; Súmula 385 do STJ se couber
     – subsidiariamente: valor proporcional (critérios do caso, sem citar valor de outro processo sem fonte)
V.   PEDIDO CONTRAPOSTO (se houver crédito pelos mesmos fatos — art. 31)
VI.  PEDIDOS (improcedência; subsidiários)
VII. PROVAS (documentos anexos; depoimento pessoal do autor; testemunhas — nome e função)
```

Peça curta: o juiz leigo lê na audiência. Prefira tabela "alegação do autor × fato provado pela empresa × documento".

## 3. Audiência — checklist da empresa

- [ ] Carta de preposição com poder para transigir (modelo: `procuracao`/agente `agenda-audiencia`)
- [ ] Preposto conhece os fatos (roteiro de 1 página: o que aconteceu, datas, o que a empresa ofereceu)
- [ ] Proposta de acordo autorizada pelo cliente (teto e forma de pagamento) — o JEC sempre tenta conciliar
- [ ] Documentos em ordem e numerados; cópia para o autor
- [ ] Testemunhas avisadas (ou intimação requerida no mínimo 5 dias antes da instrução — art. 34, § 1º)

## 4. Perdeu: recurso inominado

| Item | Regra |
|---|---|
| Cabimento | sentença, salvo homologatória de acordo ou laudo arbitral (art. 41) |
| Prazo | 10 dias, contados da ciência da sentença (art. 42), em dias úteis (art. 12-A) |
| Preparo | nas **48 horas seguintes à interposição**, independentemente de intimação, sob pena de deserção (art. 42, § 1º); compreende todas as despesas, inclusive as dispensadas em 1º grau (art. 54, parágrafo único) |
| Efeito | só devolutivo; o juiz pode dar efeito suspensivo para evitar dano irreparável (art. 43) — pedir fundamentadamente |
| Advogado | obrigatório no recurso (art. 41, § 2º) |
| Sucumbência | recorrente vencido paga custas e honorários de 10% a 20% (art. 55) — pesar antes de recorrer |
| Depois da Turma | **não cabe recurso especial** (Súmula 203 do STJ); recurso extraordinário só com questão constitucional e repercussão geral |

Embargos de declaração no JEC: 5 dias, interrompem o prazo do recurso (arts. 48 a 50) — ver
`embargos-declaracao-contrarrazoes`.

## 5. Teses frequentes da empresa (conferir o teor antes de citar)

| Situação | Fundamento conferido na base |
|---|---|
| Negativação, mas o autor já tinha outra inscrição legítima | Súmula 385 do STJ |
| Banco: fraude de terceiro | Súmula 479 do STJ responsabiliza o banco por fortuito **interno** — a defesa precisa mostrar fato externo à operação |
| CDC aplicado a banco | Súmula 297 do STJ (não discutir aplicabilidade; discutir o mérito) |
| Serviço sem defeito / culpa exclusiva | CDC art. 14, § 3º, I e II |
| Vício sanado em 30 dias | CDC art. 18, § 1º |

Enunciados do FONAJE são muito usados no JEC, mas **não estão na base local**: só cite com o número e o texto
conferidos no site do FONAJE.

## 6. Fecho obrigatório

1. `conferencia-citacoes-fm` sobre a minuta (`conferir.py minuta.md`). Lei 9.099 sempre como "art. X da Lei 9.099/1995".
2. `calculo-prazos-cpc` para a data da audiência/recurso.
3. `acuracia-juridica` (fatos × documentos).

Toda peça é rascunho: revisão e assinatura do advogado responsável.
