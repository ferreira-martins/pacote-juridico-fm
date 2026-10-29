---
name: analise-contratual
description: "Use SEMPRE que o usuário pedir para REVISAR, ANALISAR ou AVALIAR RISCOS de um CONTRATO, aditivo, minuta, NDA ou cláusula — mesmo que o contrato pareça curto ou simples e mesmo que você ache que poderia responder direto. Consulte esta skill ANTES de analisar qualquer contrato, para garantir a metodologia padronizada do escritório (matriz de risco 🟢🟡🔴 por cláusula, redline, fundamentos legais BR e checagem de acurácia) em vez de uma análise de improviso. Entre por AQUI, não por `consultar-legislacao`: esta skill já manda verificar cada artigo na legislação durante a análise. Aponta cláusulas problemáticas e o que negociar, sempre a favor de um lado (contratante, contratada, locador, locatário etc.). Triggers — \"revisa esse contrato pra mim\", \"analisa as cláusulas desse aditivo\", \"que riscos tem nesse contrato de prestação de serviços?\", \"esse contrato de locação tá ruim pra gente?\", \"marca o que eu deveria negociar nesse NDA\". É uma análise CONSULTIVA (aconselha um lado). NÃO confunda com `relatorio-juridico`, que descreve processos de forma imparcial; aqui o objetivo é tomar partido pelo cliente. Direito brasileiro (CC, CDC, CLT, LGPD, Lei de Arbitragem)."
---

# Análise contratual (revisão de risco e negociação) — Brasil

Revisa um contrato cláusula a cláusula sob a ótica de **um lado** (o cliente),
apontando riscos, sugerindo redlines e priorizando o que negociar. Inspirada na
metodologia de *contract review* (matriz de cláusulas + risco
VERDE/AMARELO/VERMELHO + confiança + redline), **adaptada ao direito
brasileiro**.

## Natureza e guardrails (leia antes de tudo)

Esta skill é **consultiva e parcial** — ela trabalha **a favor do cliente**.
Isso a distingue da `relatorio-juridico`, que é descritiva e imparcial. **Não
misture as duas naturezas**: um relatório processual descreve sem advogar tese;
uma análise contratual aconselha. Se o usuário pedir "relatório" de um processo,
é a outra skill.

Limites que valem sempre:

- **Não substitui parecer assinado.** A saída é um **rascunho de trabalho** para
  o advogado revisar — sempre exige revisão de profissional habilitado (OAB)
  antes de ir ao cliente ou à contraparte.
- **Não invente dispositivo legal.** Para citar lei federal indexada (CC, CDC,
  CLT, LGPD, Lei de Locações etc.), busque o **texto vigente do artigo** em
  `consultar-legislacao` e fundamente a partir do trecho real; depois passe a
  saída pela `acuracia-juridica` antes de entregar. Lei não indexada (ex.: Lei
  de Arbitragem) ou na dúvida sobre o número do artigo, marque "(verificar
  dispositivo)" em vez de chutar.
- **Confiança honesta.** Onde a leitura depende de fato externo ao contrato
  (intenção das partes, prática do setor, jurisprudência local), baixe a
  confiança e sinalize — é onde o julgamento humano mais agrega.

## Pipeline

1. **Ingestão** — se o contrato vier em PDF/DOCX, use
   `formatacao-arquivos-juridicos` para extrair texto fiel; se for longo, use
   `chunking-juridico` para segmentar por cláusula. Se já estiver colado na
   conversa, leia direto (e use `busca-semantica-juridica` para achar cláusulas
   específicas).
2. **Contexto** — colha antes de analisar (não trave por falta; siga com o que
   tiver e marque as lacunas):
   - **Qual lado o cliente representa?** (contratante/contratada, locador/
     locatário, fornecedor/adquirente, licenciante/licenciado). Isso muda toda a
     leitura de risco — uma cláusula boa para um lado é ruim para o outro.
   - **Relação de consumo?** Se uma ponta é destinatário final e a outra
     fornecedor, incide o **CDC** (muda limites de multa, foro, cláusulas
     abusivas). Se é B2B paritário, regime do **CC**. Se é trabalho/PJ
     mascarado, atenção à **CLT**.
   - **Valor e prazo** do contrato, e **preocupações específicas** do cliente.
3. **Identificação** — tipo contratual (prestação de serviços, locação, compra
   e venda, distribuição, licença/SaaS, NDA, etc.), **lei de regência** e
   **foro** declarados.
4. **Análise cláusula a cláusula** — percorra a matriz de
   `references/matriz-clausulas-br.md`. Para cada cláusula relevante avalie:
   - **Risco**: 🟢 VERDE (aceitável) / 🟡 AMARELO (negociar) / 🔴 VERMELHO
     (risco sério para o cliente).
   - **Confiança** (0–100%).
   - **O que está no contrato** × **o que é usual/recomendado** para o lado do
     cliente.
   - **Impacto prático**: o que isso significa na operação / num litígio.
5. **Redline** dos itens 🟡 e 🔴 (ver formato abaixo).
6. **Pontos de escalonamento** — sinalize o que exige decisão estratégica do
   advogado (ver seção própria).
7. **Revisão** — passe pela `acuracia-juridica` (fidelidade ao texto do contrato
   + checagem de dispositivos legais citados) antes de entregar.

Opcional, quando útil: consulte `consultar-rag` para recuperar **a posição-padrão
do escritório** ou **peças/contratos-modelo** sobre o mesmo tipo contratual — útil
para alinhar as sugestões ao que o Ferreira e Martins costuma negociar.

## Formato do redline (itens 🟡 e 🔴)

```
**Cláusula**: [nº / título]
**Texto atual**: "[transcrição literal]"
**Risco para o cliente**: 🔴 / 🟡  (Confiança: X%)
**Problema**: [explicação em linguagem clara]
**Sugestão de redação**: "[nova cláusula proposta]"
**Prioridade**: Essencial / Importante / Desejável
**Fundamento**: [dispositivo/base — ex.: CDC art. 51, IX; CC art. 421-A;
                 ou "prática de mercado" quando não houver base legal]
```

## Estrutura da saída

```markdown
## Análise Contratual — [tipo do contrato]

**Cliente representa**: [lado]
**Partes**: [nomes e papéis]
**Regime**: [CC / CDC / CLT / misto] · **Foro/arbitragem**: [...]

### Visão geral de risco
| Métrica | Valor |
|---|---|
| Risco global | 🟢 / 🟡 / 🔴 |
| Achados | X 🔴, Y 🟡, Z 🟢 |
| Revisão de advogado recomendada | Sim / Não |

### Principais achados
1. **[Cláusula]** — 🔴 — [resumo de uma linha] (Confiança X%)
...

### Análise detalhada
[cláusula a cláusula, seguindo a matriz]

### Redlines sugeridos
[itens 🟡 e 🔴, priorizados]

### Pontos para decisão do advogado
[escalonamentos]
```

## Quando escalar para o advogado (humano)

Sinalize revisão humana obrigatória quando houver: qualquer achado 🔴;
confiança abaixo de ~70% em cláusula material; relação de consumo com cláusula
possivelmente abusiva (CDC art. 51); cláusula de não concorrência com restrição
ampla; tratamento de dados pessoais sensível (LGPD); penalidade desproporcional;
garantias/avais pessoais; foro ou arbitragem que afaste o cliente do juízo
natural; ou o próprio cliente expressar dúvida.

## Princípios

- **Tome partido — declarado.** Diga sempre **a favor de quem** está a análise.
  A mesma cláusula recebe leitura oposta conforme o lado.
- **Fidelidade ao texto.** Transcreva a cláusula analisada; não parafraseie a
  ponto de mudar o sentido.
- **Sem dispositivo inventado.** Base legal incerta → marque para verificação.
- **Saída em markdown.** Para entregar em DOCX/PDF formatado, use
  `formatacao-arquivos-juridicos`.
