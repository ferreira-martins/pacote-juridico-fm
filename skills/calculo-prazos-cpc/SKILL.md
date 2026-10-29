---
name: calculo-prazos-cpc
description: Use SEMPRE que precisar calcular, conferir ou explicar um PRAZO processual (CPC) — vencimento de contestação, réplica, recurso, embargos, cumprimento, impugnação, manifestação etc. — a partir de uma data de intimação/publicação/disponibilização. Calcula em DIAS ÚTEIS (CPC 219), aplica disponibilização→publicação→início (CPC 224 §§1-3), suspensão de 20/12 a 20/01 (CPC 220) e feriados nacionais/forenses, devolvendo o vencimento com TRILHA DE AUDITORIA (cada dia pulado e o porquê). Não calcule prazo "de cabeça" nem conte dias corridos por engano — rode o motor `scripts/prazos.py`. Triggers — "qual o prazo da contestação se fui intimado dia X", "quando vence esse recurso", "conta 15 dias úteis a partir dessa publicação", "esse prazo cai no recesso?", "confere se a apelação ainda tá no prazo", "vencimento da réplica intimada em DD/MM". É uma FERRAMENTA DE CÁLCULO determinística; não confunda com `redacao-defesa` (que redige a peça) nem com `analise-peca-adversa` (que mapeia teses). Direito processual brasileiro (CPC/2015). O controle de prazo é responsabilidade final do escritório — a saída é insumo conferível, não dispensa a checagem da portaria do tribunal.
---

# Cálculo de prazos processuais (CPC/2015)

Calcula vencimento de prazo processual de forma **determinística e auditável**.
Esta é uma das poucas tarefas do escritório em que um erro de um dia é fatal —
por isso **não se conta prazo "no olho"**: roda-se o motor `scripts/prazos.py`,
que aplica as regras do CPC e devolve a trilha de cada dia pulado para o
advogado conferir.

## Por que existe (e por que um script, não a sua aritmética)

Contar dias úteis somando feriados móveis (Páscoa, Carnaval, Corpus Christi),
recesso forense e a cascata disponibilização → publicação → início é
exatamente o tipo de conta em que o modelo erra silenciosamente. O motor é
testado, replica a regra do CPC e **mostra o trabalho** — o que torna o
resultado conferível em vez de uma alegação. Se a sua conta mental divergir do
script, **o script está certo e a conta mental está errada**: investigue a
divergência (provavelmente um feriado ou o recesso).

## Regras aplicadas (e a base legal)

| Regra | Dispositivo |
|---|---|
| Considera-se publicação o 1º dia útil seguinte à disponibilização (DJE) | CPC 224, §2º |
| O prazo começa a correr no 1º dia útil seguinte à publicação (*dies a quo*) | CPC 224, §3º |
| Prazos processuais contam-se só em **dias úteis** | CPC 219 |
| Vence no dia seguinte se o termo cair em dia sem expediente | CPC 224, §1º |
| Prazos **suspensos de 20/12 a 20/01** | CPC 220 |
| Feriados nacionais (fixos + móveis) e forenses | leis/portarias |

> ⚠️ **Limite de competência da skill.** O motor cobre o **regime geral do
> CPC**. Ele **não** sabe: prazos em dobro (Fazenda Pública CPC 183,
> Defensoria, litisconsortes com procuradores distintos CPC 229), prazos
> próprios de outros ramos (Juizados, CLT, execução fiscal), nem **suspensões
> locais** não cadastradas. Quando o caso tiver qualquer um desses, **ajuste a
> entrada** (ex.: passe o dobro de dias) ou **sinalize ao usuário** que a conta
> precisa de revisão — não silencie a exceção.

## Pré-requisito

`scripts/prazos.py` usa só a biblioteca padrão do Python (nenhuma dependência
externa). Precisa de Python 3.8+. Se o ambiente não tiver Python, avise o
usuário em vez de tentar contar à mão.

## Como rodar

A skill já traz o motor empacotado em `scripts/prazos.py`. Forma geral:

```powershell
python "<skill>\scripts\prazos.py" <AAAA-MM-DD> <DIAS> [--corridos] [--tribunal SIGLA] [--cfg CAMINHO]
```

- `<AAAA-MM-DD>` — data da **disponibilização** no DJE (ou a data-base que o
  usuário informar; confirme **qual** data é, porque muda a cascata).
- `<DIAS>` — tamanho do prazo (ex.: 15 para contestação/recurso comuns).
- `--corridos` — força contagem em dias corridos (prazos de direito material;
  o padrão é **dias úteis**, que é o processual).
- `--tribunal SIGLA` — aplica feriados forenses daquele tribunal (precisa estar
  cadastrado em `feriados_forenses.json`).
- `--cfg CAMINHO` — usa um arquivo de feriados específico.

### Exemplos

```powershell
# Contestação (15 dias úteis) intimada/disponibilizada em 01/06/2026
python prazos.py 2026-06-01 15

# Prazo que atravessa o recesso (mostra a suspensão CPC 220 na auditoria)
python prazos.py 2026-12-15 15 --tribunal TJSC

# Prazo de direito material em dias corridos
python prazos.py 2026-06-01 30 --corridos
```

## Feriados — configurar antes de confiar no resultado

O motor já conhece os **feriados nacionais** (fixos + móveis). Os **forenses e
locais** (Dia da Justiça, Dia do Servidor, feriados municipais da comarca,
suspensões por portaria) variam por tribunal e por ano e vêm de
`feriados_forenses.json`:

1. Copie `references/feriados_forenses.example.json` para
   `scripts/feriados_forenses.json` (ou aponte com `--cfg`).
2. Preencha `feriados_por_tribunal` e `feriados_extras_geral` conforme o
   calendário oficial do tribunal do processo, para o(s) ano(s) em jogo.
3. **Sempre confronte com a portaria/calendário oficial.** Suspensão de
   expediente não cadastrada é a causa nº 1 de erro de prazo — e o motor não
   adivinha o que não está no arquivo.

## Como ler a saída

O motor imprime, em ordem:

- **Disponibilização → Publicação → Início** — a cascata do art. 224, para o
  advogado ver onde cada marco caiu (e o dia da semana).
- **VENCIMENTO** — a data-alvo, com quantos dias corridos faltam até lá.
- **Dias pulados na contagem** — cada sábado, domingo, feriado (pelo nome) e
  dia de recesso que o motor descartou. **Esta é a trilha de auditoria**:
  confira-a contra o calendário do tribunal antes de cravar a data.

## Integração com as outras skills

- [[redacao-defesa]] — antes de redigir a seção "Da tempestividade", calcule
  aqui o vencimento e cole a trilha de auditoria; nunca afirme tempestividade
  sem a conta.
- [[analise-peca-adversa]] — ao mapear a resposta, registre o prazo e o
  vencimento para a peça que será produzida.
- [[relatorio-juridico]] — se o relatório precisar informar prazo em curso,
  use esta skill em vez de estimar.

## Princípios

- **Mostre o trabalho.** Entregue sempre a trilha de auditoria, não só a data.
  Um vencimento sem a cascata e os dias pulados não é conferível.
- **Confirme qual é a data-base.** Disponibilização, publicação e intimação
  pessoal entram em pontos diferentes da cascata — pergunte se houver dúvida.
- **Exceções não entram caladas.** Prazo em dobro, outro ramo, suspensão local:
  sinalize. Melhor um aviso visível do que uma data errada com cara de certa.
- **A última palavra é do advogado.** A saída é insumo auditável; o controle de
  prazo é responsabilidade do escritório. Toda resposta termina lembrando de
  conferir a portaria do tribunal.
