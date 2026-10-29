# Estrutura de peça de defesa (CPC) — esqueleto

Esqueleto-padrão para minutar peças defensivas. Adapte ao caso e **sempre**
prefira o estilo das peças-modelo do escritório (recupere via `consultar-rag`)
ao genérico abaixo.

## A) Contestação

1. **Endereçamento** — "AO JUÍZO DA [Nº] VARA [MATÉRIA] DA COMARCA DE [CIDADE]/[UF]".
   Linha em branco; abaixo, "Autos n. [CNJ]".
2. **Preâmbulo/qualificação** — nome e qualificação do(s) réu(s), "já
   devidamente qualificado(s) nos autos", por seus procuradores, com fundamento
   nos **arts. 335 e seguintes do CPC**, apresenta CONTESTAÇÃO à ação que lhe
   move [autor], pelos fatos e fundamentos a seguir.
3. **Da tempestividade** — demonstre o termo inicial do prazo (art. 335, c/c
   art. 231 CPC) e a contagem em **dias úteis** (art. 219). **Calcule o
   vencimento com a skill `calculo-prazos-cpc`** (não conte à mão) e use a
   trilha de auditoria para fundamentar. Conclua pela tempestividade.
4. **Preliminares (art. 337 CPC)** — só as cabíveis: inexistência/nulidade de
   citação, incompetência (absoluta/relativa), incorreção do valor da causa,
   inépcia da inicial, perempção, litispendência, coisa julgada, conexão,
   ilegitimidade, falta de interesse, ausência de caução, convenção de
   arbitragem, etc.
5. **Prejudiciais de mérito** — prescrição e/ou decadência, se houver.
6. **Do mérito** — impugnação **especificada** dos fatos (art. 341 CPC): rebata
   fato a fato, pois o não impugnado torna-se incontroverso. Organize por tese;
   sustente cada uma com fundamento legal e prova. Distinga claramente fato de
   alegação.
7. **Da reconvenção** (art. 343 CPC), se cabível — pode vir na própria
   contestação; qualifique o pedido reconvencional, causa de pedir e valor.
8. **Das provas** — proteste por todos os meios (documental, pericial,
   testemunhal, depoimento pessoal), justificando a pertinência.
9. **Dos pedidos** — acolhimento das preliminares; no mérito, improcedência
   total; condenação do autor em custas e honorários; (eventual) procedência da
   reconvenção; especificação de provas.
10. **Fecho** — local, data, advogado e OAB.

## B) Réplica (impugnação à contestação)

1. Endereçamento e referência aos autos.
2. Tempestividade (prazo do art. 351 CPC — 15 dias úteis).
3. Refutação das **preliminares** arguidas pelo réu.
4. Impugnação às **provas/documentos** novos juntados com a contestação
   (art. 437 CPC).
5. Reforço do mérito da inicial, ponto a ponto.
6. Pedidos (rejeição das preliminares; prosseguimento; procedência).

## C) Contrarrazões de recurso

1. Endereçamento ao juízo/relator conforme o recurso.
2. Tempestividade e cabimento (impugne pressupostos do recurso, se for o caso).
3. Mérito recursal — defenda a decisão recorrida, ponto a ponto.
4. Pedido de desprovimento / manutenção da decisão.

## Lembretes de qualidade (não pular)

- **Nada de fato inventado**: lacuna vira `[CONFIRMAR COM CLIENTE]`.
- **Nada de precedente inventado**: súmula/tema/acórdão só se verificado;
  do contrário, `[citar precedente — verificar]`.
- **Cubra todos os fatos da inicial** (art. 341) — faça um checklist fato a fato.
- Toda minuta sai com a nota: *"Minuta para revisão — conferir fatos, provas e
  fundamentos antes de protocolar."*
