---
name: gerador-minutas
description: Use SEMPRE que o usuário pedir para REDIGIR/GERAR uma MINUTA de CONTRATO ou instrumento do zero — prestação de serviços, compra e venda, locação, NDA/confidencialidade, parceria, distrato, termo, procuração, contrato de honorários etc. — mesmo que o pedido pareça simples. Consulte esta skill ANTES de minutar, para seguir o método padronizado (coleta mínima de dados das partes e do objeto, cláusulas numeradas, campos [PREENCHER], notas [NOTA DO ADVOGADO] onde há risco, e fundamentação em lei real via `consultar-legislacao`). Triggers — "faz uma minuta de contrato de prestação de serviços", "gera um NDA pra gente", "preciso de um contrato de locação", "monta um distrato", "redige um contrato de honorários", "cria uma minuta de parceria". É um produto de REDAÇÃO (gera documento novo) e um RASCUNHO que EXIGE revisão final do advogado antes da assinatura. NÃO confunda com `analise-contratual` (que REVISA um contrato já existente e aponta riscos) nem com `redacao-defesa`/`estrutura-pecas` (peças processuais). Direito brasileiro (CC, CDC, CLT, LGPD, Lei de Locações, Lei de Arbitragem).
---

# Gerador de minutas contratuais — Brasil

Redige **minutas sob medida** para o advogado revisar: cláusulas numeradas,
linguagem precisa e campos **[PREENCHER]** onde faltar dado. A minuta **exige
revisão final** antes da assinatura.

## Natureza e guardrails

- **Redação, não revisão.** Esta skill **cria** o documento; para analisar/apontar
  risco em contrato existente, é a `analise-contratual`.
- **Não invente dispositivo.** Onde a cláusula depender de lei (CDC, CC, CLT,
  LGPD, Locações), confirme o **artigo vigente** em `consultar-legislacao` antes
  de citar; lei não indexada ou dúvida → "(verificar dispositivo)".
- **Marque o que falta.** Se faltar dado essencial, **liste as pendências antes**
  de gerar e use `[PREENCHER]` no corpo — não invente nome, CPF, valor ou prazo.
- **Sinalize risco.** Insira `[NOTA DO ADVOGADO]` onde houver ponto sensível
  (limitação de responsabilidade em B2C, exclusão de danos indiretos, não
  concorrência, transferência de IP).
- **Rascunho.** Passe a minuta pela `acuracia-juridica` e entregue com a lista de
  pendências + lembrete de revisão final.

## Coleta mínima (se ausente, liste o que falta antes da minuta)

- Tipo de contrato e regime (B2B, B2C/consumidor, trabalhista).
- Partes: nome/razão social, nacionalidade, estado civil (PF), CPF/CNPJ,
  endereço, representação.
- Objeto, prazo, valor, forma e cronograma de pagamento, multa e juros.
- Rescisão: com/sem justa causa, aviso prévio contratual, efeitos.
- Foro, lei aplicável; necessidade de **LGPD** (cláusula de dados) e/ou
  **propriedade intelectual**.

## Estrutura sugerida da minuta

1. Título e epígrafe.
2. Qualificações completas.
3. Objeto e escopo (entregáveis ou bem).
4. Obrigações das partes (simétricas quando couber).
5. Preço, reajuste, faturamento, tributos.
6. Prazo, vigência, renovação.
7. Confidencialidade e proteção de dados (se aplicável).
8. Propriedade intelectual / uso de marca (se aplicável).
9. Rescisão, multa, devolução.
10. Comunicações e tolerância de atraso.
11. Cessão, sucessão.
12. Foro ou arbitragem; assinaturas e testemunhas.

## Boas práticas

- Linguagem **precisa**; para público leigo, incluir subseção "definições".
- Evitar cláusulas genéricas demais em **objeto** e **preço**.
- B2C: cuidado com cláusulas abusivas (CDC art. 51) — sinalizar em `[NOTA DO
  ADVOGADO]`.

## Saída

Minuta completa numerada + **lista de pendências** (o que cruzar com documentos
reais) + lembrete de revisão final obrigatória. Cláusulas-modelo reutilizáveis
em `references/clausulas-modelo.md`.
