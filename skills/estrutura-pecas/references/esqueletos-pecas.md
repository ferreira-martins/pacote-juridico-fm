# Esqueletos por tipo de peça (CPC)

Andaimes para o advogado preencher. `[COMPLETAR]` = dado do caso; **PESQUISAR** =
citação a confirmar (`pesquisa-jurisprudencia` / `consultar-legislacao`).

## Petição inicial (art. 319)

1. Endereçamento — "EXMO. SR. DR. JUIZ DE DIREITO DA [vara] DA COMARCA DE
   [COMPLETAR]".
2. Qualificação do autor e do réu (art. 319, II) `[COMPLETAR]`.
3. **Dos fatos** — linha do tempo.
4. **Do direito** — uma tese por bloco (premissa → norma → interpretação →
   **PESQUISAR** jurisprudência).
5. **Da tutela** (se houver) — fumus + periculum + reversibilidade.
6. **Dos pedidos** (art. 322/324) — principal, subsidiários; citação;
   procedência; honorários; provas.
7. **Valor da causa** (art. 291).
8. Requerimentos finais e provas pretendidas.

## Contestação → usar `redacao-defesa`

Esta skill só monta o esqueleto; o texto desenvolvido de contestação/réplica/
contrarrazões é produto da `redacao-defesa`.

## Recurso (apelação / agravo)

1. Endereçamento (juízo a quo) + interposição.
2. Razões recursais:
   - **Tempestividade** e preparo (`calculo-prazos-cpc`).
   - **Síntese** da decisão recorrida.
   - **Preliminares** (nulidade, cerceamento).
   - **Mérito** — por capítulo atacado: erro de fato/direito → norma →
     **PESQUISAR** precedente.
   - **Pedido** de reforma/anulação; efeitos.

## Agravo de instrumento (art. 1.016)

1. Nomes, endereços dos advogados.
2. Exposição do fato e do direito.
3. Razões da reforma da decisão.
4. Pedido de **efeito suspensivo / tutela recursal** (art. 1.019) com requisitos.
5. Peças obrigatórias (art. 1.017) — checklist.

## Manifestação / petição simples

1. Referência ao despacho/intimação `[COMPLETAR]`.
2. Objeto da manifestação.
3. Fundamento sucinto.
4. Pedido.

## Memoriais

1. Síntese da causa e do que se provou.
2. Por tese: prova produzida → norma → **PESQUISAR** jurisprudência.
3. Refutação dos argumentos da parte contrária.
4. Pedido de procedência/improcedência.

## Bloco de argumentação (reutilizável)

> **Tese:** [nome]
> - **Premissa fática:** [o que os autos mostram] `[COMPLETAR]`
> - **Norma:** [art. — confirmar em `consultar-legislacao`]
> - **Interpretação:** [subsunção]
> - **Jurisprudência:** **PESQUISAR** [tribunal/tema, sem nº inventado]
> - **Contra-argumento esperado:** [...] → **refutação:** [...]
> - **Provas:** [docs/testemunhas]

## Checklist pré-protocolo

- [ ] Procuração nos autos.
- [ ] Custas/preparo ou gratuidade.
- [ ] Cálculo atualizado.
- [ ] Documentos e anexos.
- [ ] Prazo conferido (`calculo-prazos-cpc`).
- [ ] Competência/endereçamento correto.
