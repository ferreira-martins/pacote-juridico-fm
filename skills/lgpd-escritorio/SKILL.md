---
name: lgpd-escritorio
description: Use SEMPRE que o tema for PROTEÇÃO DE DADOS PESSOAIS / LGPD — diagnóstico, adequação ou plano de conformidade LGPD — SEJA para o PRÓPRIO ESCRITÓRIO de advocacia OU para um CLIENTE como controlador/operador (inclusive os dados de FUNCIONÁRIOS/EMPREGADOS na relação de emprego). Esta é a dona de QUALQUER pergunta sobre o que a LGPD exige, mesmo quando vier fraseada como "o que a regulação/lei exige sobre tratamento de dados". Inclui mapear tratamento de dados de clientes, funcionários e fornecedores, identificar bases legais, apontar gaps por domínio com semáforo, montar plano 30/90/180 dias e rascunhar política de privacidade, DPA, comunicado de incidente e script de resposta ao titular. Consulte esta skill ANTES de responder sobre adequação à LGPD, para seguir o método padronizado (inventário de dados, bases legais, direitos ARCO, segurança, retenção, operadores) e fundamentar nos artigos reais da LGPD via `consultar-legislacao`. Triggers — "o escritório está adequado à LGPD?", "monta um plano de LGPD pra gente", "preciso adequar à LGPD os dados dos funcionários do cliente", "o cliente é controlador e quer um plano de adequação à LGPD", "o que a LGPD exige no tratamento de dados de empregados?", "preciso de uma política de privacidade pro escritório", "como respondo a esse pedido de titular?", "houve vazamento, o que comunico?", "que base legal uso pra cobrança/marketing?". É um produto de COMPLIANCE — NÃO substitui DPO nem RIPD formal sem revisão especializada. RASCUNHO para revisão de advogado habilitado. NÃO confunda com `compliance-regulatorio` (regulação setorial geral) nem com `consultar-legislacao` (busca de um artigo isolado). Direito brasileiro (LGPD — Lei 13.709/18).
---

# Compliance LGPD para escritório de advocacia

Apoia o **diagnóstico LGPD**: mapeia o tratamento de dados, prioriza riscos e
rascunha a documentação mínima. **Não** substitui DPO nem RIPD formal — é
rascunho para revisão especializada.

## Natureza e guardrails

- **Controlador.** O escritório quase sempre é **controlador** dos dados de
  clientes; o segredo profissional **não dispensa** transparência LGPD.
- **Fundamente no artigo real.** A LGPD está indexada — busque o dispositivo em
  `consultar-legislacao` (bases legais art. 7º/11, direitos do titular art. 18,
  segurança art. 46–49, incidente art. 48 etc.) e cite a partir do texto vigente.
- **Rascunho.** Modelos e plano são ponto de partida; passe a entrega pela
  `acuracia-juridica` e marque o que depende de DPO/RIPD formal.

## Pipeline

1. Se houver contratos/políticas atuais em arquivo, ingira com
   `formatacao-arquivos-juridicos`.
2. Levante o inventário (perguntas abaixo) — pergunte só o que faltar.
3. Pontue gaps por domínio (semáforo) e monte o plano 30/90/180.
4. Rascunhe os modelos pedidos.
5. `acuracia-juridica`.

## Diagnóstico (pergunte se necessário)

- Quais **dados pessoais** (incl. **sensíveis**: saúde, dado criminal)?
- **Finalidades**: atendimento, cobrança, marketing, recrutamento, TI.
- **Bases legais** (execução de contrato, legítimo interesse com teste,
  consentimento quando aplicável, cumprimento de obrigação legal/regulatória).
- **Armazenamento**: local, nuvem (qual fornecedor?), backup, e-mail, WhatsApp
  Business, software jurídico/CRM.
- **Acessos**: quem, logs, confidencialidade; **suboperadores**.
- **Transferência internacional** e cláusulas-tipo.
- **Encarregado (DPO)** nomeado? Canal do titular publicado?
- **Retenção e eliminação**; incidentes passados.

## Gaps por domínio (semáforo 🟢🟡🔴)

Consentimento e informação · Bases legais · Direitos do titular (ARCO) ·
Segurança · Retenção · Compartilhamento · Contratos com operadores · Cookies/site
· Treinamento.

## Plano 30 / 90 / 180 dias

- **Quick wins (30)**: política de privacidade, aviso interno, registro de
  operações simplificado, nomear encarregado.
- **Médio (90)**: DPIA/RIPD quando houver dado sensível; DPA com fornecedores.
- **Longo (180)**: programa de cultura, treinamento e auditorias internas.

## Modelos (rascunho)

- Cláusula de **privacidade** para o contrato de honorários.
- **Comunicado de incidente** (fato · dados afetados · medidas · canal · ANPD).
- **Script de resposta ao titular** (direito exercido · prazo · entrega).

Estruturas prontas em `references/modelos-lgpd.md`.

## Saída

Diagnóstico + mapa de gaps (semáforo) + plano 30/90/180 + modelos solicitados +
ressalva de que dado sensível/RIPD exige revisão especializada.
