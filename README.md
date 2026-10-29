# Pacote Jurídico F&M — skills para Claude Code

Skills do escritório **Ferreira e Martins Advogados Associados** para o Claude Code: métodos de peça e de análise e um
**verificador offline de citações**, com 130 leis federais (texto do Planalto) e 4.660 súmulas, OJs, PNs e temas do
TST, STF, STJ e TRT-12. Direito brasileiro.

> Esta é a **versão pública**. Ela não traz fichas de processos, peças protocoladas, dados de clientes nem conteúdo de
> terceiros licenciado só para uso interno.

## Instalar (Windows)

Peça ao Claude Code, em qualquer pasta:

> Clona https://github.com/ferreira-martins/pacote-juridico-fm e roda o instalar.ps1

Ou faça você mesmo:

```powershell
git clone https://github.com/ferreira-martins/pacote-juridico-fm
powershell -ExecutionPolicy Bypass -File pacote-juridico-fm\instalar.ps1
```

O instalador copia as skills para `%USERPROFILE%\.claude\skills`, instala `pypdf` e `python-docx` e roda o autoteste.
Precisa de **Python 3.10 ou mais novo** (Microsoft Store → "Python 3.12"). Depois, feche e abra o Claude Code.
Para atualizar, rode `git pull` e o instalador de novo.

## Regra de ouro: nada sai sem conferência

```
python "%USERPROFILE%\.claude\skills\conferencia-citacoes-fm\scripts\conferir.py" minuta.md
python "%USERPROFILE%\.claude\skills\conferencia-citacoes-fm\scripts\conferir.py" minuta.md --autos "pasta dos autos"
python "%USERPROFILE%\.claude\skills\conferencia-citacoes-fm\scripts\conferir.py" --texto "Súmula 338 do TST, art. 841 da CLT"
python "%USERPROFILE%\.claude\skills\conferencia-citacoes-fm\scripts\conferir.py" --buscar "fiador locação"
```

| Resultado | O que fazer |
|---|---|
| `OK` | Leia o teor e confirme que ele diz o que a peça afirma. O erro mais comum é o número certo com o assunto errado. |
| `ATENÇÃO: CANCELADA` | Tire a citação ou troque pelo fundamento vigente. |
| `NÃO ENCONTRADO` | O artigo não existe naquela lei. |
| `SEM LASTRO LOCAL` | Fora da base (tema repetitivo do STJ, REsp, ADI). Confira no site oficial. Não confirmou, não cita. |
| `NÃO ESTÁ NOS AUTOS` | O trecho entre aspas não é literal. |

## Qual usar para quê

| Tarefa | Skill |
|---|---|
| Contestação e recursos trabalhistas (empresa) | `analise-processo-trabalhista-fm` → `argumentacao-trabalhista-fm` → `peca-trabalhista` |
| Peça adversa / vale recorrer? | `analise-peca-adversa` · `analise-sentenca` |
| Contestação ou réplica cível | `redacao-defesa` · esqueleto: `estrutura-pecas` |
| Empresa ré no Juizado Especial (consumidor) | `defesa-jec-consumidor` |
| Embargos de declaração / contrarrazões | `embargos-declaracao-contrarrazoes` |
| Executado: prescrição, título inexigível, sem citação | `excecao-pre-executividade` |
| Prazo processual (dias úteis, recesso, feriados) | `calculo-prazos-cpc` |
| Contrato: revisar / criar | `analise-contratual` (+ `contratos-fm`) · `gerador-minutas` |
| Bancário (revisional, embargos) | `direito-bancario-fm` |
| Compliance trabalhista preventivo | `compliance-trabalhista` |
| Notificação extrajudicial · LGPD · publicidade OAB | `notificacao-extrajudicial` · `lgpd-escritorio` · `etica-oab-publicidade` |
| Jurisprudência | `conferir.py --buscar` → `pesquisa-jurisprudencia` |
| Revisão final de qualquer peça | `conferencia-citacoes-fm` → `acuracia-juridica` |

## Alertas de jurisprudência (conferidos na fonte oficial em 29/10/2026)

1. **O TST cancelou 36 verbetes em 30/06/2025 (Resolução nº 225).** Entre eles estão as Súmulas 90, 219, 228, 277, 294,
   329, 366, 377, 426, 437, 444 e 449, o item I da 331, itens da 6 e da 372, e as OJs SBDI-1 14, 270, 355, 383 e 418.
2. **STJ:** 24 súmulas canceladas ainda circulam como vigentes. Exemplos: a 418 (hoje vale a 579), a 469 e a 603.
3. **Dano extrapatrimonial trabalhista (CLT art. 223-G, § 1º):** nas ADIs 6050, 6069 e 6082, o STF tornou os tetos
   orientativos. Não declarou a regra inconstitucional.
4. **Juros de mora cíveis:** desde 30/08/2024 vale Selic − IPCA (CC art. 406, Lei 14.905/2024). Antes, vale a Selic
   (Tema 1.368 do STJ).
5. **Prazo em dobro de litisconsortes** não vale em autos eletrônicos (CPC art. 229, § 2º).
6. **Usucapião extrajudicial:** o fundamento é a Lei 6.015/1973, art. 216-A. Não é "CPC 216-A".

## Limites

- Temas repetitivos do STJ e acórdãos não estão na base local.
- Os feriados forenses dos tribunais não vêm preenchidos no cálculo de prazos.
- O OCR de PDF escaneado da `peca-trabalhista` só funciona no Mac.
- O **timbre do escritório** (`peca_modelo_FM.docx`, logo e rodapé) não está no repo público. Para o DOCX timbrado da
  `peca-trabalhista`, peça o arquivo ao TI e rode `gerar_docx.py --template <caminho do peca_modelo_FM.docx>`.
- Toda peça gerada é **rascunho**: revisão e assinatura são do advogado responsável.

## Aviso

Os textos de lei e de súmulas são documentos oficiais públicos. O restante (métodos, teses, modelos e código) é do
Ferreira e Martins Advogados Associados, publicado para uso do escritório. Não há licença de reuso.
