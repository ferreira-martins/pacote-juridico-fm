---
name: etica-oab-publicidade
description: Use SEMPRE que o usuário pedir para VERIFICAR, REVISAR ou APROVAR uma peça de MARKETING JURÍDICO quanto à ÉTICA da OAB — post, anúncio, site, vídeo, áudio, e-mail, perfil em rede social, cartão ou material institucional do escritório/advogado — mesmo que o material pareça inofensivo. Consulte esta skill ANTES de aprovar qualquer publicidade, para aplicar a pré-checagem padronizada contra o Provimento OAB nº 205/2021 e os princípios da publicidade da advocacia (tom educativo vs mercantilização, identificação com nome+OAB, captação indevida, promessa de resultado, superlativos vedados, uso de imagem/depoimento de cliente, transparência de conteúdo gerado por IA), com classificação APTO / AJUSTES MÍNIMOS / REPROVADO e redação corrigida trecho a trecho. Triggers — "esse post tá dentro da ética da OAB?", "posso anunciar isso?", "revisa esse material de marketing do escritório", "esse texto do site infringe o provimento 205?", "pode usar esse depoimento de cliente?", "esse criativo de Google Ads passa na OAB?". É uma análise de COMPLIANCE (não advoga tese) e um RASCUNHO para decisão do advogado responsável. Sempre indique "confirmar atualização normativa" — provimentos mudam. NÃO confunda com `analise-contratual` nem com `compliance-regulatorio` (regulação setorial). Direito brasileiro (EOAB, CED, Provimento 205/2021).
---

# Verificador de ética OAB em publicidade

Pré-checagem **rigorosa** de peças de marketing jurídico contra o **Provimento
OAB nº 205/2021** e os princípios da publicidade da advocacia. Melhor **corrigir
antes** de publicar do que responder a processo ético.

## Natureza e guardrails

- **Compliance, não tese.** A skill avalia conformidade; não advoga.
- **Norma viva.** Provimentos e entendimentos de TED mudam. Indique **sempre**
  "confirmar atualização normativa e jurisprudência ética do Tribunal local".
- **Rascunho.** A classificação e as correções são apoio à decisão do advogado
  responsável pela peça. Passe o parecer pela `acuracia-juridica` antes de entregar.
- Para citar o EOAB (Lei 8.906/94) indexado, use `consultar-legislacao`. O
  Provimento 205/2021 e o CED **não** são lei seca federal indexada — cite por
  artigo apenas se tiver o texto à mão e marque "(verificar dispositivo)".

## Pipeline

1. Se o material vier em arquivo (PDF/imagem/roteiro em DOCX), use
   `formatacao-arquivos-juridicos` para extrair o texto/roteiro.
2. Rode a lista de verificação abaixo, trecho a trecho.
3. Classifique e proponha redação corrigida.
4. `acuracia-juridica`.

## Lista de verificação (sim/não + evidência no texto)

- Tom **educativo/informativo** vs mercantilização da profissão.
- **Identificação**: nome + **OAB/UF** (e endereço profissional quando exigido
  em peça institucional).
- **Captação indevida** (chamariz, exploração de caso sensacional, "corra", senso
  de urgência mercantil).
- **Promessa de resultado** ou sugestão de influência sobre autoridade.
- **Valores de honorários** usados como isca promocional / desconto/oferta.
- **Superlativos e comparativos** vedados ("melhor", "nº 1", "garantido",
  "imbatível").
- **Imagens e casos de clientes**: há autorização explícita? Sigilo preservado?
- **Depoimentos**: autenticidade e contexto; risco de endosso enganoso.
- **IA**: transparência quando o conteúdo for majoritariamente gerado por IA
  (boa prática + reputação).
- **Mídia social paga** (Meta/Google Ads): segmentação que explore público
  sensível ou vulnerável.

## Classificação final

**APTO** · **AJUSTES MÍNIMOS** · **REPROVADO** (com risco disciplinar).

## Para cada problema (tabela)

Trecho | Problema | Fundamento (art./§ do Provimento 205 ou CED quando possível,
senão "(verificar)") | **Redação sugerida** | Risco (alto/médio/baixo).

## Extras

- Notas específicas para **Meta/Google Ads** (palavras vetadas pela plataforma,
  segmentação sensível).
- Sugestão de **disclaimer** genérico ("conteúdo educativo, não constitui
  consultoria jurídica").

## Saída

Parecer com classificação + tabela trecho-a-trecho + versão corrigida da peça +
ressalva de atualização normativa. Checklist completo em
`references/checklist-publicidade.md`.
