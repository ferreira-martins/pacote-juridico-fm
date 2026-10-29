---
name: direito-bancario-fm
description: "Produção de peças de direito bancário do escritório Ferreira & Martins na perspectiva do devedor/consumidor — embargos à execução de contrato bancário e ação revisional de contrato bancário (cédula de crédito bancário, financiamento, capital de giro, alienação fiduciária, confissão de dívida). Cobre o catálogo de teses revisionais (CDC, juros abusivos x taxa média BACEN, capitalização/anatocismo, comissão de permanência, descaracterização da mora, repetição de indébito, exibição de documentos) e a formatação FM. Use SEMPRE que o usuário pedir embargos à execução bancária, ação revisional de contrato bancário, revisão de juros/encargos, defesa de cliente executado por banco ou cooperativa, ou citar cédula de crédito bancário, financiamento abusivo, alienação fiduciária, comissão de permanência, anatocismo — mesmo sem nomear a skill."
---

# Direito Bancário FM — embargos e revisional (perspectiva do devedor)

Skill para produzir as duas peças bancárias centrais do escritório **Ferreira & Martins**, na ótica do **cliente devedor/consumidor**: **embargos à execução** de contrato bancário e **ação revisional** de contrato bancário. As duas compartilham o mesmo núcleo de teses; muda o veículo.

## Distinção entre as duas peças

- **Embargos à execução** — defesa do executado em ação fundada em contrato bancário, que é título executivo extrajudicial regido pelo CPC. **Independem de garantia** — art. 914 do CPC: o executado pode embargar sem penhora, depósito ou caução. Prazo de **15 dias úteis**, contado da juntada do mandado de citação — art. 915, não 30 dias. A **garantia só é exigida para o efeito suspensivo** — art. 919, § 1º, do CPC, junto com a relevância dos fundamentos e o risco de dano. Atenção: a regra de garantia como pressuposto e o prazo de 30 dias valem apenas na execução fiscal — art. 16 da Lei 6.830/80 —, que não é o caso dos contratos bancários comuns. Usar `references/pop-embargos.md`.
- **Ação revisional** — ação autônoma do devedor para revisar as cláusulas do contrato, com ou sem execução em curso. Não exige garantia. Usar `references/pop-revisional.md`.

## PORTÃO OBRIGATÓRIO — antes de aplicar qualquer POP

Antes de estruturar a peça, **perguntar ao usuário se há laudo ou cálculo do expert** — perito ou contador. Isso define como satisfazer o requisito de admissibilidade ligado ao valor.

- **Se HÁ laudo/cálculo:** usar os valores apurados pelo expert — encargos expurgados, débito recalculado, valor que se entende correto, repetição de indébito. Citar o laudo como fundamento e anexo.
- **Se NÃO HÁ:** elaborar um **cálculo genérico/estimativo** apenas para preencher o requisito de admissibilidade — nos embargos, a **declaração do valor que se entende correto** e o **demonstrativo do excesso** (art. 917, II e § 2º, do CPC; sob pena de rejeição liminar dessa alegação, § 4º); na revisional, o **valor controvertido** e o **proveito pretendido**. Registrar expressamente que o cálculo é estimativo e **requer-se perícia contábil** para a apuração definitiva.

Detalhe do procedimento em `references/calculos-laudo.md`. Nunca redigir a peça sem resolver este ponto.

> **Skill companheira — o laudo.** O laudo/cálculo de revisão bancária é produzido pelo perito (metodologias do perito Ederson Gobato) — a skill `pericia-bancaria-fm` citada em versões antigas NÃO está instalada. Sem laudo, pare e peça o laudo antes de redigir. Esta skill produz a PEÇA; o laudo a instrui — inclusive o valor do depósito do incontroverso e o valor da causa.

## SEGUNDO PORTÃO — é contrato de renegociação?

Antes de redigir, **identificar a natureza do título**. Se for cédula de **renegociação, confissão, composição ou refinanciamento de dívida**, o saldo renegociado em regra carrega os encargos abusivos dos contratos anteriores. Nesse caso:

- **Pedir ao cliente o contrato originário e toda a cadeia de contratos** — originário, aditivos e renegociações sucessivas — para juntar à peça.
- **Revisar desde a origem.** A novação não convalida as cláusulas abusivas dos pactos anteriores; sustentar a revisão de toda a cadeia, art. 51, IV, do CDC, e a possibilidade de rediscutir os contratos extintos por novação quando eivados de abusividade — conferir o entendimento do STJ.
- **Requerer a exibição** da cadeia completa pela instituição quando o cliente não a tiver, reforçando a inversão do ônus.
- O cálculo, com laudo ou genérico, deve alcançar **desde o primeiro contrato**, não apenas o saldo renegociado.

Não redigir sem mapear a cadeia quando houver renegociação.

## Fluxo de trabalho

1. **Identificar a peça** — embargos ou revisional — e ler o POP correspondente.
2. **Passar pelo portão** — confirmar laudo/cálculo e definir a via de valor.
3. **Coletar os dados** do caso conforme o POP — juízo, partes, contrato, encargos, garantia.
4. **Selecionar as teses cabíveis** do catálogo em `references/teses-bancarias.md` — só as que o contrato concreto suportar.
5. **Redigir** na estrutura do POP, com a formatação FM.
6. **Conferir** as súmulas e precedentes — nunca inventar — e fechar pelo checklist.

## Regras de qualidade — inegociáveis

- Não inventar jurisprudência, súmula, número de processo ou ementa; conferir cada citação; em dúvida, sinalizar para conferência.
- Citar dispositivo com precisão — lei, artigo, parágrafo, inciso.
- Não suprir dado ausente com presunção; perguntar.
- Não afirmar valores sem memória de cálculo ou laudo.

## Gerador de peça em .docx

Após redigir o conteúdo e passar pelo portão, montar a peça final no padrão FM com o helper `scripts/gerar_peca.py`. O agente redige o texto jurídico; o script aplica a formatação — logo no cabeçalho, rodapé com contatos, Times New Roman, justificado, numeração romana, pedidos numerados sem parênteses.

Uso: `python3 scripts/gerar_peca.py dados.json` — ou `-` para ler o JSON do stdin. O esquema completo do JSON está no cabeçalho do próprio script: tipo, enderecamento, dependencia, preambulo, secoes [{titulo, paragrafos}], pedidos, valor_causa, local_data, assinaturas, out. As seções devem seguir a ordem do POP correspondente, e os pedidos sair na ordem do POP. Confirmar a assinatura — Francieli e/ou Clênio — antes de gerar.

## Referências

- `references/teses-bancarias.md` — catálogo das teses revisionais com fundamentos, reutilizável pelas duas peças.
- `references/pop-embargos.md` — POP dos embargos à execução, estrutura e pedidos.
- `references/pop-revisional.md` — POP da ação revisional, estrutura e pedidos.
- `references/calculos-laudo.md` — o portão do laudo x cálculo genérico e como preencher o requisito de admissibilidade.
- `templates/modelo-revisional.docx` / `.md` / `.json` — modelo da revisional (estrutura I–XVII), padrão POP-JUR-007, pronto para preencher; o `.json` regenera o `.docx` via `gerar_peca.py`.
- `templates/modelo-embargos.docx` / `.md` / `.json` — modelo dos embargos (estrutura I–XVIII: tempestividade, preliminares, excesso de execução, efeito suspensivo), mesmo padrão; o `.json` regenera o `.docx`.

## Formatação e assinatura

Padrão oficial do escritório — **POP-JUR-007 v1.1** ("Formatação de Petições e Organização do Drive"), já implementado no `gerar_peca.py`:
- **Fonte Bookman Old Style**; alinhamento **justificado**; espaçamento **1,5** no corpo.
- **Texto corrido:** tamanho **12**, recuo de primeira linha **1,25 cm**, entrelinhas 1,5.
- **Qualificação inicial das partes:** Bookman 12 justificado, **SEM recuo de primeira linha** — exceção do item 6.1.3.b do POP; não aplicar os 1,25 cm ao cabeçalho das partes.
- **Citações diretas longas:** tamanho **11**, recuo do bloco **2,5 cm** em todo o texto, entrelinhas **simples (1,0)**, com separação visual antes e depois.
- É **vedado misturar** fontes, tamanhos e espaçamentos fora do padrão, salvo exigência formal do tribunal (justificar nos comentários internos).
- Margens superior 4,5 / inferior 2,25 / esquerda 3,0 / direita 3,0 cm (o POP-JUR-007 não trata de margens; mantidas do modelo FM).
- **Nomeação do arquivo no Drive** (POP-JUR-007, item 6.2.6): `N- TIPO DA PEÇA – complemento objetivo` — ex.: `1- Petição Inicial – Ação Revisional`; numeração `1-`, `2-` (nunca `01-`, `1.` ou `0-`).
- Logo no cabeçalho e rodapé com contatos das filiais; sóbrio, sem emojis; numeração hierárquica; enumerar sem parênteses.
- **Termos em latim sempre em itálico** — pacta sunt servanda, bis in idem, in casu, ex vi, fumus boni iuris, periculum in mora e correlatos. O gerador aplica o itálico automaticamente; ao redigir, escrever os termos normalmente.
- **Números de processo no padrão CNJ** — NNNNNNN-DD.AAAA.J.TR.OOOO — sempre que descrever autos.
- Assinatura: Francieli Martins, OAB/SC 32.723, e Clênio Jorge Ferreira, OAB/SC 29.267 — confirmar quem subscreve.
