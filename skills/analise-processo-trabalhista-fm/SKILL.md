---
name: analise-processo-trabalhista-fm
description: "Método do IA_JUR para ler e analisar autos trabalhistas com prova ancorada — extrator barato (Amazon Nova Micro ou DeepSeek/OpenAI-compatível) que devolve partes, datas, pedidos e inventário probatório em JSON com cada item CONFERIDO literalmente na peça e página; ficha de caso (pedidos × resultado, o que convenceu, prova que decidiu, lições); 40 fichas de casos reais do escritório; cálculos determinísticos (prescrição bienal/quinquenal com projeção do aviso, aviso prévio Lei 12.506, avos, contrato de experiência, prazo processual CLT). Use para analisar processo/autos trabalhistas grandes, montar ficha ou resumo de caso, levantar provas favoráveis/desfavoráveis, calcular prescrição ou prazo, ou buscar como casos parecidos do escritório terminaram."
---

# Análise de processo trabalhista F&M (método do IA_JUR)

Scripts em `scripts/` (Python 3.10+; no PC do Davi use `pythoncore-3.14-64\python.exe -X utf8`).

## 1. Ler autos grandes sem gastar contexto — `extrair_autos.py`

Autos que não cabem inteiros (ou para economizar): extração por modelo barato + **conferência em código**.

```
python scripts/extrair_autos.py <pasta|pdf|txt ...> -o caso.json            # Nova Micro (AWS_PROFILE=fm-admin)
python scripts/extrair_autos.py autos/ --campos data_admissao,pedidos,decisoes -o x.json
python scripts/extrair_autos.py autos/ --provedor openai --base-url https://api.deepseek.com   # Hermes/VPS
```
- Esquema padrão `references/esquema-trabalhista.json` (30 campos: CNJ, partes, vara, rito, datas, função, salário,
  pedidos, decisões, prazos + 10 campos de **inventário probatório**: provas favoráveis/desfavoráveis à defesa,
  confissões, contradições, pagamentos, controles, depoimentos/perícias, fatos impeditivos…). Esquema próprio: `--esquema`.
- Cada item só sobrevive se o **trecho existe literalmente** na peça e o valor está no trecho; a página sai dos
  marcadores `[Pagina N]`. Saída: `fonte` pronta (`[Fonte Documento: peça › p. N]`), `divergencias` (mesmo dado com
  valores diferentes entre peças — aponte, não "corrija"), `nao_encontrados`, `descartados`, tokens.
- Custo de referência: sentença de 20 mil caracteres ≈ 6 mil tokens ≈ US$ 0,0004 (Nova Micro). Janelas de 120 mil
  caracteres, 6 em paralelo.
- **Limites:** campo ausente = "a extração não achou", não "não consta dos autos". Item de lista: o `valor` é a
  descrição do modelo; a prova é o `trecho`. Para ler uma peça por inteiro, abra as páginas citadas.
- Requisitos: `pip install boto3 "botocore[crt]"` (Bedrock) e `pypdf` (PDF). Autoteste sem rede: `python scripts/teste_extrator.py`.

## 2. Ficha do caso — `references/ficha-instrucoes.md`

Formato do escritório para registrar um processo e **aprender argumentação**: cabeçalho único → Contexto → tabela
Pedidos × resultado (tese do autor, tese da defesa, 1º grau, 2º grau, fundamento decisivo) → CONVENCEU / NÃO
CONVENCEU → Prova que decidiu → Lições argumentativas → Não generalizar. Regras: só o que está nos arquivos, âncora
`(doc N)` em toda afirmação, lei/súmula só como a decisão citou, não suavizar derrota, anonimizar pessoas físicas.

## 3. Casos do escritório — `references/casos/`

As 40 fichas reais NÃO vão na versão pública; (TRT12 quase todas; polo reclamada em geral). `casos/_INDICE.md` traz a 1ª linha de cada uma
(resultado + temas). Busque por tema: `grep -il "banco de horas" references/casos/*.md`. Use para estimar risco e
achar o argumento que convenceu em caso parecido — **não** para citar na peça, e respeite o "Não generalizar".

## 4. Cálculos — `calc.py` (conta é do código, não do modelo)

```
python scripts/calc.py prescricao extincao=10/05/2023 ajuizamento=02/04/2025 admissao=03/02/2018
python scripts/calc.py aviso_previo admissao=.. desligamento=..     # Lei 12.506: 30 + 3/ano completo, até 90
python scripts/calc.py avos admissao=.. desligamento=..
python scripts/calc.py prazo_contrato inicio=22/09/2025 dias=45 prorrogacao_dias=45 experiencia=true
python scripts/calc.py prazo_processual disponibilizacao=13/11/2025 dias=8 [pessoal=true]
```
Prescrição projeta o aviso prévio (OJ 83 SBDI-1) e diz se cabe alegar bienal/quinquenal; cada saída traz `passos`,
`regras` e `alertas`. Feriado local/recesso do tribunal **não** estão no prazo processual — conferir a portaria
(ou usar `calculo-prazos-cpc`). Datas de entrada: só as que estão escritas nos autos.

## Checklist de análise (o que o IA_JUR errava)
- **Decisão vigente:** sentença anulada ou reformada não é a decisão a atacar; leia o dispositivo da última intimação.
- **Leitura parcial** (FM-READ-001): se só parte dos autos foi lida, diga quais peças/páginas — nunca "não consta".
- **Data:** ato futuro não é narrado como ocorrido; data final de prazo só com ato inicial identificado nos autos.
- **Lado do escritório:** procure "Ferreira", "Martins", "Clênio" (maiúsculas também) nas procurações/assinaturas.
- Prova de requisito legal (nexo técnico do INSS, DCB, espécie B31/B91/B94, CAT, indeferimento de prova oral) decide
  pedido — procure explicitamente.
- Fechamento: `conferencia-citacoes-fm` + `acuracia-juridica`. Relatório de carteira segue `relatorio-juridico`.
