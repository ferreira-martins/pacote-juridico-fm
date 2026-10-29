---
name: argumentacao-trabalhista-fm
description: "Repertório argumentativo trabalhista do Ferreira e Martins extraído do IA_JUR — ideias de argumento por tema (13), teses defensivas por verba (29), POP-JUR-009-A de contestação, estilo de redação F&M, lições de erros reais e 21 peças reais protocoladas (contestações, RO, RR, ED, impugnação de laudo, MS). Use ao montar a estratégia ou redigir contestação, recurso, contrarrazões, ED ou manifestação trabalhista (polo reclamada sobretudo), ao escolher teses por pedido, ou quando pedirem argumentos/munição para um pedido trabalhista (horas extras, acidente, insalubridade, justa causa, grupo econômico etc.)."
---

# Argumentação trabalhista F&M (conhecimento do IA_JUR)

Base condensada do agente IA_JUR (`Desktop\ia-jur\base_grafo`). Repertório de ideia, **não fonte**: toda lei/súmula
que for para a peça passa pela skill `conferencia-citacoes-fm` (ou `consultar-legislacao`) antes.

> 🔴 **Cancelamentos do TST (Pleno, 30/06/2025 — 36 verbetes):** esta base ainda cita verbetes cancelados — Súmulas 219, 329 (honorários — hoje CLT 791-A), 331 item I, 6 (itens I, II, VI-b e X), 228, 294, 366, 377, 437 e OJ SBDI-1 355 (as fichas de `casos/` e as peças de `modelos/` são históricas: citam o que valia na época). Não use o número como fundamento vigente: troque pelo dispositivo legal (CLT pós-Reforma) ou pelo verbete atual. O `conferir.py` marca cada um como `ATENÇÃO: CANCELADA` (lista completa e fonte em `conferencia-citacoes-fm/references/jurisprudencia/cancelamentos_tst.json`).

## Onde está cada coisa (references/)

| Preciso de… | Abra |
|---|---|
| Ideias de argumento de um tema, com **quando NÃO usar** e o caso do escritório que as sustentou | `argumentos/<tema>.md` (acidente-de-trabalho, dano-moral, doenca-ocupacional-estabilidade, equiparacao-acumulo, honorarios-gratuidade, horas-extras-jornada, insalubridade-periculosidade, intervalos, justa-causa-rescisao-indireta, preliminares-prescricao-limitacao, recursal, rescisao-verbas-multas, vinculo-grupo-terceirizacao) |
| Tabela tese × fundamento × como argumentar, por verba | `teses/tese-defensiva-<verba>.md` (29 verbas; `atualizacao-monetaria-e-juros-…` para juros/correção) |
| Passo a passo obrigatório da contestação | `metodo/pop-contestacao.md` (POP-JUR-009-A v2.0 — **prevalece** sobre checklist genérico) |
| Método de defesa da empresa / inicial pelo empregado | `metodo/metodo-defesa-empresa.md`, `metodo/metodo-inicial-empregado.md` |
| Estrutura e checklist por peça (contestação, RO, RR, AIRR, ED, contrarrazões, cálculos, memoriais, inicial da empresa, sustentação) | `metodo/estruturas-e-checklists.md` |
| Como o escritório escreve (profundidade do capítulo, endereçamento, numeração, anti-padrões) | `metodo/estilo-fm.md` |
| Erros reais que o agente cometeu e a regra que nasceu deles | `metodo/licoes.md` |
| Peça real do escritório como forma (seções completas) | (peças reais: só na versão interna do escritório) |

Busca rápida: `grep -ril "<termo>" references/` (ex.: "banco de horas", "Súmula 338", "culpa exclusiva").

## Como usar (regras que o IA_JUR aprendeu apanhando)

1. **Fato primeiro, argumento depois.** Uma ideia só entra se os fatos e documentos do caso a comportarem. Leia a
   linha "Quando NÃO usar / riscos" antes de usar qualquer ideia — ela registra onde o escritório perdeu.
2. **Fundamente com a fonte, nunca com a ideia.** A ideia aponta o caminho; a peça cita a lei/súmula conferida e a
   página dos autos. Caso antigo do escritório **não** é citado na peça (serve para calibrar o risco).
3. **Ordem da defesa em acidente/doença** (orientação do escritório): inexistência do acidente → ausência de nexo →
   ausência de concausa → culpa exclusiva da vítima → (subsidiária) culpa concorrente → quantum.
4. **Impugnação específica** de cada fato e pedido (CPC 341, aplicado no processo do trabalho) — fato não impugnado
   presume-se verdadeiro. Preliminares checadas uma a uma antes do mérito (ver POP).
5. **Peça certa para a decisão certa** (FM-PROC-001): recurso só contra a decisão **vigente** (não contra sentença
   anulada); na JT é RO/RR/AIRR/ED, não apelação; contrarrazões **não pedem reforma**; contestação trabalhista vai
   até a audiência (CLT 847), não "15 dias".
6. **Lado do cliente** (FM-SIDE-001): nunca escrever algo que condene o próprio cliente, peça gratuidade para a
   empresa sem prova de insuficiência, ou admita fato que a defesa nega.
7. **Modelo só do mesmo tipo de peça e do mesmo lado** (FM-MODEL-001): modelo de contestação não é forma de recurso;
   modelo de outro tema só como inspiração de seção. Seção marcada "não está nestes autos" vai só com o título.
8. **Dado essencial faltando** (data da intimação, decisão recorrida, lado do cliente, versão dos fatos do cliente)
   → **pare e pergunte** antes de redigir. Lacuna menor vira `[CONFIRMAR: …]`, nunca um valor plausível.
9. **Prova desfavorável não some** (FM-COV-001): enfrente, diferencie ou registre o risco.
10. Ao final: `conferencia-citacoes-fm` sobre a minuta + `acuracia-juridica` (regra da casa).

## Relação com outras skills
- Ler/extrair os autos: `analise-processo-trabalhista-fm`. Conferir citações: `conferencia-citacoes-fm`.
- Agentes de peça do plugin (`ferreira-martins-juridico:defesa-trabalhista-empregador`, `recurso`, …) e
  `peca-trabalhista`/`municao-processual` continuam sendo o fluxo de redação; esta skill é o repertório que eles
  não têm (o A/B de 26/10 mostrou que eles citam de memória).
- Atualizar a base: `python ..\montar.py` (recopia do IA_JUR; não edite `references/` à mão).
