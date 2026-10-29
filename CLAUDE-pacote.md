# Pacote Jurídico F&M (instalado pelo instalar.ps1 — não edite entre os marcadores; o instalador regrava)

Regras para todo trabalho jurídico:
1. **Use a skill do pacote** da tarefa (tabela abaixo) antes de redigir ou analisar — não escreva de improviso.
2. **Siga o método e o POP** que a skill indica: abra os arquivos de `references/` que o SKILL.md mandar (ex.: POP da
   contestação, padrão de redação F&M, catálogo de teses) **antes** de redigir.
3. **Nunca cite de memória** lei, súmula, OJ, tema ou precedente. Antes de entregar qualquer peça, parecer ou análise,
   rode a `conferencia-citacoes-fm` (`conferir.py`) e corrija tudo que não sair `OK`. Não confirmou, não cita.
4. Toda peça é **rascunho** para revisão e assinatura do advogado responsável. Português do Brasil.

| Tarefa | Skill |
|---|---|
| Contestação e recursos trabalhistas (empresa) | `analise-processo-trabalhista-fm` → `argumentacao-trabalhista-fm` → `peca-trabalhista` |
| Peça adversa / vale recorrer? | `analise-peca-adversa` · `analise-sentenca` |
| Contestação ou réplica cível | `redacao-defesa` (esqueleto: `estrutura-pecas`) |
| Empresa ré no Juizado Especial (consumidor) | `defesa-jec-consumidor` |
| Embargos de declaração / contrarrazões | `embargos-declaracao-contrarrazoes` |
| Executado: prescrição, título inexigível, sem citação | `excecao-pre-executividade` |
| Prazo processual | `calculo-prazos-cpc` |
| Contrato: revisar / criar | `analise-contratual` (+ `contratos-fm`) · `gerador-minutas` |
| Bancário (revisional, embargos) | `direito-bancario-fm` |
| Compliance trabalhista, cartas de advertência/suspensão/justa causa, termo de EPI | `compliance-trabalhista` |
| Notificação extrajudicial · LGPD · publicidade OAB | `notificacao-extrajudicial` · `lgpd-escritorio` · `etica-oab-publicidade` |
| Jurisprudência | `conferencia-citacoes-fm` (`--buscar`) → `pesquisa-jurisprudencia` |
| Revisão final | `conferencia-citacoes-fm` → `acuracia-juridica` |
