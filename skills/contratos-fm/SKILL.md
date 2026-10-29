---
name: contratos-fm
description: >
  Análise de risco contratual no direito brasileiro para o escritório Ferreira & Martins,
  na perspectiva do advogado defendendo cliente. Lê contratos civis, empresariais,
  imobiliários, rurais, de construção civil e de terceirização em .docx, .pdf ou
  texto colado, mapeia cláusulas críticas à luz do CC/02, CPC, CDC, LGPD, Lei de
  Arbitragem, Lei do Inquilinato (8.245/91), Estatuto da Terra (4.504/64),
  Representação Comercial (4.886/65), Corretagem (CC + Lei 6.530/78), Terceirização
  (Lei 6.019/74 com 13.429/17 e 13.467/17), Lei Ferrari (6.729/79), Incorporação
  (4.591/64) e demais leis setoriais, e devolve relatório classificado por severidade
  com fundamentação legal, redação sugerida e plano de negociação.
  Tipos contratuais cobertos: prestação de serviços, prestação de serviços na
  construção civil, terceirização e proteção anti-pejotização, distribuição,
  representação comercial autônoma (RCA), concessão comercial de veículos
  (Lei Ferrari), revenda, fornecimento contínuo, sociedade limitada, acordo de
  sócios, SPA/M&A, locação residencial, locação não-residencial, locação por
  temporada, *built to suit*, comodato, NDA, MoU, licenciamento de software,
  licenciamento de marca/franquia, contrato de influenciador, joint venture,
  mútuo, compra e venda imobiliária, promessa de CCV, permuta (com e sem torna),
  corretagem imobiliária, arrendamento rural, parceria rural, empreitada em
  todas as modalidades (global, preço unitário, administração).
  Use SEMPRE que o usuário pedir "análise de contrato", "minuta", "revisão
  contratual", "due diligence de contrato", "avaliar riscos", "parecer sobre
  contrato", "redação contraproposta", ou encaminhar/anexar contrato/minuta/draft
  para revisão, mesmo sem nomear esta skill.
  Acione também ao mencionar termos como "cláusula penal", "rescisão", "non-compete",
  "indenização contratual", "cláusula leonina", "abusividade", "responsabilidade
  solidária", "garantias", "MAC clause", "earn-out", "vesting", "tag along",
  "drag along", "lock-up", "indenização especial", "denúncia vazia", "renovatória",
  "built to suit", "CCV", "promessa de compra e venda", "permuta", "torna",
  "comissão de corretagem", "corretagem", "arrendamento rural", "parceria rural",
  "estatuto da terra", "preempção", "empreitada", "empreitada global",
  "preço fixo", "cost plus", "administração", "responsabilidade do construtor",
  "patrimônio de afetação", "incorporação", "retenção de 11%", "INSS construção",
  "cessão de mão de obra", "terceirização", "pejotização", "vínculo empregatício",
  "quarentena 18 meses", "art. 5º-C", "art. 5º-D", "Lei 6.019", "representação
  comercial", "RCA", "Lei Ferrari", "concessão comercial", "revenda", "distrato"
  no contexto contratual cível ou empresarial. Não usar para contratos
  trabalhistas individuais (CLT) — para matéria criminal use a skill `criminalista`;
  para contratos de honorários do próprio FM existe template canônico já registrado
  em memória.
---

# Análise Contratual — Ferreira & Martins

Skill para análise técnica de contratos sob o direito brasileiro, na perspectiva do advogado patrocinador da causa. Os outputs são orientativos para a decisão do advogado, nunca substituem o juízo final dele.

## Quando acionar

Sempre que o usuário encaminhar um contrato, minuta ou draft para revisão — anexado, colado ou referenciado por caminho de arquivo. Também quando perguntar sobre cláusulas específicas, riscos contratuais, ou pedir parecer sobre risco de um negócio jurídico.

## Quick start

```
Usuário: "Olha essa minuta de prestação de serviços que mandaram pro cliente — vê o que tem de problema."
→ Skill identifica tipo contratual, partes e papéis (quem é cliente FM, quem é
  contraparte), percorre as 8 categorias de risco, devolve relatório
  Vermelho/Amarelo/Verde + plano de contraproposta + minuta de redação
  alternativa para os pontos críticos.
```

## Pré-leitura obrigatória

Antes de analisar, identificar:

1. **Cliente FM × Contraparte** — quem o escritório representa. A análise pende para proteção do cliente, sinalizando o que beneficia e o que prejudica.
2. **Tipo contratual** — civil típico, atípico (art. 425 CC), misto, de adesão (art. 423 CC), em relação de consumo (CDC), empresarial, societário. A legislação aplicável muda.
3. **Posição negocial** — quem redigiu (parte forte costuma redigir; cláusulas ambíguas interpretam-se contra ela, art. 113 CC e art. 423 CC), quem tem urgência, qual o histórico das partes.
4. **Documento completo** — ler anexos, exhibits, "considerandos" (têm valor interpretativo, art. 112 CC), cláusula de prevalência. Riscos relevantes frequentemente ficam em anexos.
5. **Casos FM ativos relacionados** — verificar memória se o contrato faz parte de caso conhecido para contextualizar.

## Workflow

### 1. Obter o contrato

Em ordem de preferência:
- Arquivo local indicado pelo usuário (`.docx`, `.pdf`, `.doc`). Para `.docx` use a skill `docx`; para `.pdf` use a skill `pdf`.
- Texto colado na conversa.
- Anexo de e-mail (se houver Gmail conectado).

Ler integralmente antes de opinar. **Nunca** opinar com base em trechos isolados.

**Integridade dos anexos (obrigatório — não pular).** Ao receber conversas/arquivos exportados (WhatsApp, ZIP, e-mail), conferir **cada** referência de anexo ("arquivo anexado", imagem, .docx, .pdf, comprovante) contra os arquivos efetivamente presentes. Se algum anexo referenciado **não estiver presente ou não abrir**, **avisar o usuário imediatamente e pedir o reenvio antes de concluir a análise ou gerar qualquer documento** — nunca prosseguir como se o material estivesse completo. Exports de WhatsApp frequentemente omitem mídias/documentos, deixando só a marcação textual (caso real: dois comprovantes de pagamento omitidos quase inflaram um saldo devedor).

### 2. Mapear as 8 categorias de risco

Trabalhar na ordem abaixo, mas usar julgamento. Algumas categorias não se aplicam a todo contrato (ex.: PI em locação imobiliária).

#### Categoria 1 — Validade, qualificação e capacidade

- **Capacidade e legitimidade** (art. 104, I CC): partes capazes; representantes com poderes (procuração com firma reconhecida quando exigido, contrato social atualizado da PJ); diretor estatutário dentro dos limites do estatuto.
- **Objeto** (art. 104, II CC): lícito, possível, determinado ou determinável. Objeto vago é vetor de litígio.
- **Forma** (art. 104, III CC): forma prescrita quando exigida (escritura pública para imóveis > 30 SM — art. 108 CC; registro para eficácia contra terceiros).
- **Causa**: motivo determinante declarado nos considerandos. Atenção a simulação (art. 167 CC) e fraude contra credores (art. 158 CC).
- **CNPJ ativo e situação cadastral** da PJ (Receita, CADIN, certidões).
- **Vícios de consentimento** (arts. 138-165 CC): erro, dolo, coação, lesão, estado de perigo.

#### Categoria 2 — Preço, reajuste e pagamento

- **Preço determinado ou determinável** (art. 487 CC para compra e venda; analogia para prestação de serviços).
- **Forma e prazo de pagamento**: à vista, parcelado, contra entrega, contra medição. Atenção a "pagamento após aprovação do cliente sem prazo" — abre janela infinita.
- **Reajuste**: índice (IPCA, IGPM, INPC, IPC-FIPE, salário mínimo, dólar), periodicidade (mínimo anual — Lei 10.192/2001 art. 2º; salário mínimo é vetado fora de hipóteses específicas, art. 7º, IV CF + Súmula Vinculante 4), data-base.
- **Mora**: juros moratórios (1% am — art. 406 CC c/c art. 161 §1º CTN, ou Selic conforme entendimento STJ), correção monetária, multa moratória (2% no CDC; livre fora dele, usualmente 2%-10%).
- **Cláusula penal compensatória vs moratória** (arts. 408-416 CC): compensatória substitui perdas e danos; moratória cumula com obrigação principal. Limite: valor da obrigação principal (art. 412 CC). Possibilidade de redução equitativa (art. 413 CC).
- **Gross-up tributário**: quem suporta IRRF, INSS, ISS, PIS/COFINS, IOF. Cláusula "líquido de impostos" desloca o ônus para o pagador.
- **Garantias do crédito**: fiança (art. 818 CC — escrita, expressa, com outorga conjugal art. 1.647 III; benefício de ordem art. 827; renúncia ao benefício é comum), aval, penhor, hipoteca, alienação fiduciária, carta de fiança bancária, seguro garantia, conta caução.

#### Categoria 3 — Responsabilidade civil, indenização e garantias

- **Limitação de responsabilidade** (cap): válida no direito civil/empresarial entre partes paritárias (autonomia da vontade); inválida em relação de consumo (art. 51, I CDC); discutível em adesão se abusiva (art. 424 CC).
- **Exclusão de lucros cessantes**: válida fora do CDC; deve ser **expressa e bilateral** para reduzir risco de discussão.
- **Indenização por perdas e danos** (art. 402 CC): danos emergentes + lucros cessantes; danos morais possíveis para PJ (Súmula 227 STJ).
- **Indenização especial / "indemnification" anglo-saxônico**: comum em SPAs e contratos internacionais. Verificar: hipóteses de cobertura, baskets (de minimis, threshold, tipping), caps, sobrevida, procedimento de claim, defesa de terceiros.
- **Evicção** (arts. 447-457 CC): perda do bem por decisão judicial em razão de causa anterior. Renúncia válida se expressa e ciente (art. 449 CC).
- **Vícios redibitórios** (arts. 441-446 CC): defeito oculto que torna a coisa imprópria ou diminui seu valor. Prazo: 30 dias móveis / 180 dias semoventes / 1 ano imóvel.
- **Solidariedade** (arts. 264-285 CC): só por lei ou contrato expresso (art. 265 CC). Cláusula que diz "responsabilidade solidária" sem ressalva amplia exposição.
- **Caso fortuito e força maior** (art. 393 CC): exclui responsabilidade salvo cláusula em contrário (parágrafo único). Verificar definição contratual — pandemia, ato de governo, ciberataque.
- **Seguros**: tipo (RC profissional/E&O, RC geral, ciber, D&O), limites mínimos, beneficiário, prazo, certificado, sub-rogação.

#### Categoria 4 — Resolução, rescisão e saída

- **Resilição unilateral imotivada** (art. 473 CC): admitida quando prevista; prazo de aviso prévio compatível com investimentos feitos (art. 473, parágrafo único — denúncia abusiva).
- **Resolução por inadimplemento** (art. 475 CC): notificação extrajudicial constitutiva ou apenas declaratória, prazo de cura ("cure period"), definição de "inadimplemento substancial" (teoria do adimplemento substancial — STJ).
- **Resolução por onerosidade excessiva** (arts. 478-480 CC): teoria da imprevisão; revisão como alternativa à resolução.
- **Cláusula resolutiva expressa** (art. 474 CC): opera de pleno direito; expressa supera tácita.
- **Multa rescisória**: redução proporcional ao adimplemento parcial (art. 413 CC); limite do valor da obrigação (art. 412 CC).
- **Distrato** (art. 472 CC): forma do contrato originário.
- **Sobrevida de obrigações**: confidencialidade, não-competição, garantias, indenizações, propriedade intelectual.
- **Transição e wind-down**: trabalho em curso, devolução de valores antecipados, devolução de materiais e documentos, assistência paga vs gratuita.

#### Categoria 5 — Propriedade intelectual, dados e privacidade

- **Direitos autorais** (Lei 9.610/98): obra intelectual; cessão deve ser expressa, escrita e específica (art. 49); cessão presume-se onerosa e por 5 anos quando silente (art. 49, III); direitos morais inalienáveis (art. 27).
- **Software** (Lei 9.609/98): titularidade do empregador/contratante quando obra de serviço (art. 4º); license vs cessão; código-fonte e escrow.
- **Propriedade industrial** (Lei 9.279/96): marca, patente, desenho industrial. Cessão registrável no INPI; licença com averbação.
- **Direito de imagem e personalidade** (CC art. 20; CF art. 5º X): autorização específica, finalidade, prazo, território, contraprestação. Influenciadores: contrato deve detalhar entregáveis, exclusividade, métricas, rescisão.
- **LGPD** (Lei 13.709/2018):
  - Papéis: controlador, operador, suboperador (arts. 5º VI-VII; art. 39).
  - Base legal do tratamento (art. 7º): consentimento, execução de contrato, legítimo interesse, etc.
  - Transferência internacional (arts. 33-36).
  - Encarregado/DPO (art. 41).
  - Incidentes: notificação à ANPD e titulares (art. 48).
  - Responsabilidade solidária do operador (art. 42 §1º II).
  - Cláusulas mínimas: finalidade, duração, segurança, sub-tratamento, eliminação, auditoria.
- **Confidencialidade** (NDA ou cláusula): definição de informação confidencial, exceções (já pública, desenvolvida independentemente, recebida de terceiro lícito, divulgação por ordem legal/judicial), prazo (3-5 anos típico; perpétuo para trade secret), devolução/destruição.

#### Categoria 6 — Escopo, qualidade e gestão de mudanças

- **Objeto e escopo**: especificações técnicas, anexo de escopo detalhado, SLA mensurável, KPIs.
- **Critérios de aceitação**: objetivos (testes definidos) vs subjetivos ("a critério do contratante" — flag amarelo no mínimo).
- **Prazo e cronograma**: marcos contratuais (milestones), penalidade por atraso de cada lado (simétrica?).
- **Procedimento de mudança de escopo** (change order): formal, por escrito, com precificação acordada antes da execução. Ausência abre brecha para escopo creep sem remuneração.
- **Exceção do contrato não cumprido** (art. 476 CC): direito de suspender a própria prestação. Cláusula que renuncia ao "exceptio" é desfavorável.
- **Garantia técnica**: prazo, escopo, exclusões, foro para chamados.
- **Subcontratação**: permitida ou condicionada à aprovação prévia; responsabilidade do contratante principal.

#### Categoria 7 — Não-competição, exclusividade e proteção de mercado

- **Cláusula de não-concorrência**: validade exige limitação **temporal**, **territorial** e **material**, além de **contrapartida econômica** quando restringe atividade profissional (construção jurisprudencial — não há artigo de lei específico; pesquisar precedente atual antes de citar). Sem esses requisitos, alta chance de nulidade por restrição abusiva à livre iniciativa (art. 170 CF).
- **Exclusividade**: bilateral ou unilateral; prazo; território; produtos/serviços abrangidos; metas mínimas como condição para manter exclusividade.
- **Non-solicitation**: de empregados (lícita com limites); de clientes (mais delicada — risco de configurar não-concorrência disfarçada).
- **Tying / venda casada**: vedada (art. 39 I CDC; Lei 12.529/2011 art. 36 III "d" — infração à ordem econômica).

#### Categoria 8 — Foro, solução de conflitos e cláusulas operacionais

- **Eleição de foro** (art. 63 CPC): admitida, podendo ser declarada nula de ofício se abusiva em adesão (art. 63 §3º CPC).
- **Arbitragem** (Lei 9.307/96):
  - Cláusula compromissória **cheia** (com regras): institui imediatamente.
  - Cláusula **vazia** (apenas "submetem-se à arbitragem"): exige compromisso arbitral posterior (art. 7º).
  - Sede, idioma, número de árbitros, lei aplicável, regulamento, câmara (CAM-CCBC, CCI, AAA-ICDR, FGV, AMCHAM).
  - Em adesão, validade condicionada (art. 4º §2º Lei 9.307/96).
- **Mediação prévia** (Lei 13.140/2015): condição de procedibilidade quando expressa.
- **Lei aplicável**: relevante em contrato internacional (LINDB art. 9º — local da obrigação; CISG eventualmente aplicável a compra e venda internacional de mercadorias).
- **Idioma**: prevalência em contratos bilíngues.
- **Vigência, prorrogação automática e termo final**: aviso de não-renovação (60-90 dias é razoável).
- **Cessão contratual** (arts. 286-303 CC para créditos; assunção de dívida arts. 299-303): exigir anuência expressa em cessão de posição contratual.
- **Comunicações**: forma (e-mail vale como prova — STJ), endereços, alteração de endereço.
- **Anti-corrupção e compliance**: cláusula sob Lei 12.846/2013, FCPA, UK Bribery Act quando aplicável; due diligence de contrapartes; auditoria.
- **Lavagem de dinheiro** (Lei 9.613/98): declaração de origem lícita de recursos em transações relevantes.
- **CDC** (Lei 8.078/90 — se aplicável): cláusulas abusivas (art. 51); inversão do ônus da prova; foro do consumidor.

### 3. Estruturar o relatório por severidade

Usar **exatamente** este template:

```markdown
# Análise Contratual — [Tipo contratual] [Cliente FM × Contraparte]

## Sumário executivo
[3-5 linhas: o que é o contrato, qual a posição do cliente, qual o veredito geral
(assinável como está? assinável com ressalvas? rejeitar?), e qual o ponto mais
crítico.]

## 🔴 Vermelho — recusar ou exigir reescrita
Para cada item:
- **Cláusula X.Y** — [título do problema]
  > [transcrição literal da cláusula]
  
  **Risco:** [descrição técnica do risco jurídico/econômico]
  
  **Fundamento legal:** [arts., súmulas, jurisprudência]
  
  **Redação sugerida:**
  > [proposta de redação alternativa]

## 🟡 Amarelo — negociar
[Mesmo formato. Itens que não são deal-breakers mas pioram a posição do cliente.]

## 🟢 Verde — pontos de atenção (sem ação imediata)
[Itens que o cliente precisa **saber** mesmo que aceite: prazos de aviso,
gatilhos de renovação, datas críticas, contatos.]

## 📋 Sumário do negócio
[O que o cliente está se comprometendo a fazer/pagar/entregar; o que recebe em
contrapartida; em qual prazo; sob quais condições. Em linguagem clara, sem
juridiquês.]

## ⚖️ Plano de contraproposta
Lista priorizada do que pedir, em qual ordem, e qual o "fallback" aceitável:
1. **[item]** — pedir: [X]. Fallback: [Y]. Linha vermelha: [Z].
2. [...]

## 📎 Próximos passos sugeridos
- [ ] Reunião com cliente para validar prioridades de negociação
- [ ] Diligência adicional (ex.: certidões da contraparte, situação do imóvel,
      contrato social vigente)
- [ ] Preparar minuta de contraproposta com as redações sugeridas
- [ ] [outros, conforme caso]
```

### 4. Oferecer redação da contraproposta

Após o relatório, oferecer ao usuário a redação completa da minuta com as alterações sugeridas, em `.docx`, usando a skill `docx`. Marcar as alterações com **negrito** para revisão fácil, ou usando o esquema do Word de controle de alterações se solicitado.

Perguntar: *"Quer que eu prepare a minuta de contraproposta em .docx com as redações sugeridas?"*

## Diretrizes editoriais (não-negociáveis)

- **Nunca caracterize o output como parecer jurídico formal.** A análise é orientativa; a decisão técnica final é do advogado. Para peças formais (parecer, opinion legal), o advogado lapida e assina.
- **Transcreva a cláusula literalmente** ao apontar problema. O advogado precisa do texto exato para negociar e redigir.
- **Aponte o que está faltando**, não só o que está ruim. Contrato silente sobre cap de responsabilidade, reajuste, ou procedimento de change order frequentemente é mais perigoso que um com cláusula desfavorável explícita.
- **Não sinalize boilerplate inofensivo.** Se a cláusula é razoável e padrão de mercado, não comente. O advogado quer sinal, não recapitulação cláusula por cláusula.
- **Compare com padrões de mercado** ao classificar: *"Prazo de pagamento de 90 dias é incomum em prestação de serviços B2B brasileira — 30 dias é a média; 60 dias quando o contratante é grande corporação."*
- **Calibre pela relação de força.** Análise de MSA da Petrobras × startup é diferente de contrato entre duas PMEs. O *poder de negociação real* do cliente determina o que vale a pena pedir.
- **Cite o artigo** sempre que possível: "Art. 413 CC permite redução equitativa…" — o advogado precisa do gancho legal pronto para a peça.
- **Sinalize CDC** sempre que houver relação de consumo, mesmo disfarçada. Muda completamente a análise: nulidade de cláusulas abusivas, inversão do ônus, foro privilegiado.
- **Para casos FM ativos**, conferir memória e contextualizar.

## Estilo de redação (alinhado ao escritório)

Para sugestões de redação contratual, seguir o padrão do escritório (referenciado em `references/estilo-fm.md`):

- Português jurídico claro, evitando arcaísmo desnecessário.
- Numeração hierárquica (Cláusula 1ª, 1.1, 1.1.1).
- Definições em letra maiúscula no início, usadas com inicial maiúscula no corpo.
- Considerandos quando há contexto relevante para interpretação.
- Cláusula de integridade ("entire agreement"), de não-novação, de tolerância (não renúncia), de validade parcial (severability) ao final.

### Padrão visual dos documentos gerados (obrigatório — evitar "cara de IA")

- **Paleta sóbria:** preto e cinza-grafite azulado (tom do logo ≈ #405060). NÃO usar navy chapado, dourado, fundos coloridos em tabelas, "cards" ou blocos coloridos. Tabelas discretas (linhas finas, sem preenchimento berrante).
- **Nunca** usar linha/régua decorativa sob títulos; sem emojis; negrito só em destaques pontuais.
- **Tipografia/estrutura:** Times New Roman, justificado, numeração hierárquica, margens FM, logo no cabeçalho e rodapé com contatos (documento do escritório).
- **Enumerações sem parênteses:** ao elencar no texto, não usar "(a)", "(b)", "(i)"; usar "a.", "b." / "1.", "2." / travessões / listas.
- Detalhes em [[feedback_padrao_formatacao_FM]] e `references/estilo-fm.md`.

## References

- `references/legislacao-base.md` — artigos-chave por categoria (CC, CPC, CDC, LGPD, Lei 9.307/96, Lei 9.610/98, Lei 9.279/96, Lei 12.846/13).
- `references/clausulas-criticas.md` — cláusulas perigosas mais comuns e como tratá-las.
- `references/checklist-por-tipo.md` — checklists rápidos por tipo contratual (prestação de serviços, distribuição, fornecimento, sociedade, locação, comodato, NDA, M&A/SPA, licenciamento, influencer).
- `references/jurisprudencia.md` — súmulas e julgados-âncora do STJ/STF.
- `references/estilo-fm.md` — padrão redacional do escritório.
- `references/casos-fm.md` — particularidades dos casos ativos do escritório que aparecem em análises contratuais.
