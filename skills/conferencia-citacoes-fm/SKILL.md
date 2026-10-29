---
name: conferencia-citacoes-fm
description: "Verificador offline de citações jurídicas (leitores do IA_JUR), para TODAS as áreas (trabalhista, cível, consumidor, tributário, família, empresarial, penal) — extrai de uma minuta, parecer ou resposta cada artigo de lei (130 leis federais), súmula/OJ/PN do TST, tema IRR, súmula e tema do STF/STJ, súmula vinculante, súmula e tese do TRT12 e anexo de NR, e confere contra a base local: existe? está cancelada/superada? qual o teor? Também confere se cada trecho entre aspas existe literalmente nos autos e acha súmula/tema por assunto (--buscar). Use ANTES de entregar qualquer peça, parecer ou análise, sempre que for citar súmula/OJ/tema/artigo (inclusive para ler o teor ou descobrir qual enunciado trata de um assunto), e ao revisar texto gerado por IA ou por outro agente."
---

# Conferência de citações F&M

Cumpre a regra de ouro "nunca citar de cabeça": o código lê as citações e mostra o teor da base; quem decide é você.

```
python scripts/conferir.py minuta.md                       # todas as citações + teor
python scripts/conferir.py minuta.md --autos <pasta|pdf>   # + transcrições "entre aspas" × autos (literal)
python scripts/conferir.py --texto "Súmula 338 do TST, art. 818 da CLT"   # consulta rápida do teor
python scripts/conferir.py --buscar "fiador locação"     # qual súmula/OJ/tema trata do assunto (vigentes primeiro)
python scripts/conferir.py minuta.md --json
```
(No PC do Davi: `pythoncore-3.14-64\python.exe -X utf8`.)

## Status
| Status | Significado | O que fazer |
|---|---|---|
| OK | existe na base; teor impresso | ler o teor e confirmar que diz o que a peça afirma |
| ATENÇÃO: CANCELADA/SUPERADA | enunciado cancelado | **tirar** ou trocar pelo vigente |
| NÃO ENCONTRADO | o artigo não existe no diploma indicado (ex.: "art. 1.416 do CPC") | erro provável — corrigir |
| REVOGADO? | todas as redações achadas falam em revogação | conferir no Planalto |
| SEM LASTRO LOCAL | fora desta base (outra lei, tribunal, número inexistente) | `consultar-legislacao`, `pesquisa-jurisprudencia` ou site oficial; não confirmou → não cita |
| NÃO ESTÁ NOS AUTOS | transcrição entre aspas não é literal | copiar o texto exato da peça ou tirar as aspas |

## Base (references/)
- `jurisprudencia/`: TST (súmulas, OJs SBDI-1/SBDI-1 Transitória/SBDI-2/SDC/TP-OE, PNs), TST temas IRR, STF súmulas,
  vinculantes e temas de repercussão geral, STJ súmulas, TRT12 súmulas e teses (IRDR/IAC).
- `legislacao/`: 130 leis federais — as 126 da base do IA_JUR (CF, CC, CPC, CLT, CDC, CP, CPP, CTN, CTB, ECA, LINDB, LGPD,
  Locações, LEF 6.830, RJ 11.101, Registros Públicos 6.015, Juizados 9.099, Alimentos 5.478, Protesto, Cheque, SA, CCB,
  Simples, FGTS, leis trabalhistas…) + 5 extras do Planalto (MS 12.016, Processo eletrônico 11.419, EAOAB 8.906,
  Arbitragem 9.307, Mediação 13.140; `_extras/baixar_extras.py` no pacote). Aliases de cada lei no `.meta.json`.
- `normas/`: NR-1, 6, 7, 12, 15, 16, 17, 35, 36.
Teor = cópia das fontes oficiais coletadas pelo IA_JUR (data da coleta: ver `montar.py`/IA_JUR). Grep direto também
serve: `grep -n "^### TST Súmula 85" references/jurisprudencia/tst.md -A 30`.

## Limites conhecidos
- Artigo sem diploma ("art. 59" solto) não é conferido — escreva sempre "art. 59 da CLT".
- Inciso/parágrafo não é conferido isoladamente: confira no teor impresso.
- Lei 13.467/2017 e outras leis alteradoras não estão na base (o texto consolidado da CLT já traz as alterações).
- Lei por sigla: o leitor conhece CLT, CF, CPC, CPP, CDC, CTN, CTB, CC, CP, ECA, LINDB. Outras leis pelo NÚMERO
  ("art. 48 da Lei 13.709/2018", não "da LGPD"; "art. 22 da Lei 8.906/94", não "do EAOAB") — senão o artigo pode ser
  atribuído à lei seguinte do texto.
- Temas repetitivos do STJ e acórdãos (REsp, RE, ADI) NÃO estão na base: saem SEM LASTRO LOCAL ou nem são lidos —
  conferir no site oficial (processo.stj.jus.br/repetitivos, portal.stf.jus.br); não confirmou, não cita.
- Leis alteradoras (13.467/2017, 14.905/2024…) não precisam: o texto consolidado já traz a redação vigente.
