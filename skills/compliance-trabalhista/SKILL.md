---
name: compliance-trabalhista
description: Use SEMPRE que o usuário pedir AUDITORIA PREVENTIVA ou DIAGNÓSTICO DE CONFORMIDADE TRABALHISTA de uma EMPRESA (cliente empregador) — mapear se as práticas de jornada/ponto, SST (NRs, PGR, PCMSO, CIPA), contratos e registros (eSocial, CTPS digital), terceirização/pejotização, cotas (PCD, aprendiz), assédio (Lei 14.457/2022), igualdade salarial (Lei 14.611/2023) e folha estão em dia — produzindo checklist P0/P1/P2 por domínio, matriz de passivo contingente e plano de adequação. Consulte esta skill ANTES de responder sobre "a empresa está em conformidade trabalhista?", para seguir o método padronizado. Triggers — "faz um compliance trabalhista do cliente X", "auditoria trabalhista preventiva", "a empresa está exposta a passivo trabalhista?", "checklist de obrigações trabalhistas", "o cliente vai ser fiscalizado pelo MTE, o que revisar?", "due diligence trabalhista dessa empresa", "risco de pejotização nesses contratos PJ". É produto de COMPLIANCE PREVENTIVO (sem processo em curso) — NÃO confunda com o agente `defesa-trabalhista-empregador` (reclamação JÁ ajuizada), com `calculo-verbas-rescisorias` (conferir TRCT), com `compliance-regulatorio` (regulação setorial geral — se a dúvida for licença/agência, vai para lá) nem com `lgpd-escritorio` (dados pessoais de empregados — mesmo em contexto de RH, LGPD é de lá). RASCUNHO para revisão de advogado trabalhista. Direito brasileiro (CLT, NRs do MTE, eSocial).
---

# Compliance trabalhista preventivo — empregador

Diagnostica a **conformidade trabalhista** de uma empresa cliente e entrega
checklist priorizado + matriz de passivo + plano de adequação. Foco preventivo:
reduzir exposição antes de fiscalização do MTE ou de reclamações.

## Natureza e guardrails

- **Mapa, não parecer.** Rascunho de apoio; decisões sensíveis (desligamentos em
  massa, reenquadramento de PJs) exigem revisão do advogado trabalhista.
- **Não invente dispositivo.** CLT e leis federais indexadas → texto vigente via
  `consultar-legislacao`. NRs, portarias do MTE e manuais do eSocial não estão
  indexados → marque **"(confirmar vigência em fonte primária — gov.br/trabalho)"**.
- **Escopo primeiro.** Pergunte porte (nº de empregados — muda cota PCD, CIPA,
  ponto obrigatório), setor/CNAE (muda NRs e CCT aplicável), UF e se há PJs,
  terceirizados ou teletrabalho.
- **CCT manda.** Convenção/acordo coletivo pode criar obrigações além da CLT —
  peça a CCT da categoria ou marque como pendência P0 de verificação.
- **Rascunho.** Passe a entrega pela `acuracia-juridica`.

## Pipeline

1. Definir **escopo** (porte, CNAE, UF, formas de contratação, CCT).
2. Se houver documentos (contratos, espelhos de ponto, PGR, holerites), ingerir
   com `formatacao-arquivos-juridicos`.
3. Varrer os **domínios** do checklist (`references/checklist-trabalhista.md`)
   aplicáveis ao porte/setor — não aplicar domínio que não incide.
4. Para cada gap: obrigação + dispositivo + risco (multa MTE / passivo em
   reclamação / dano reputacional) + prova de cumprimento exigível.
5. Montar **matriz de passivo contingente** (tema × probabilidade × ordem de
   grandeza) e **plano de adequação 30/90/180**.
6. `acuracia-juridica`.

## Domínios auditados

Jornada e ponto · SST (NRs/PGR/PCMSO/CIPA/EPI) · Contratos e registros
(eSocial/CTPS) · Terceirização e pejotização · Cotas PCD e aprendiz · Assédio e
canal de denúncias · Igualdade salarial · Folha e verbas · Teletrabalho.
Detalhamento, dispositivos e gatilhos por porte em
`references/checklist-trabalhista.md` — leia antes da varredura.

## Priorização

- **P0** — infração que gera autuação imediata do MTE ou passivo certo em
  reclamação (ponto inexistente com 20+ empregados, PGR/PCMSO ausentes, cota PCD
  descoberta, PJ com subordinação evidente).
- **P1** — multa relevante ou tese recorrente na JT (banco de horas sem acordo,
  intervalos suprimidos, EPI sem registro de entrega).
- **P2** — boa prática / mitigação probatória (políticas escritas, treinamentos
  documentados).

## Modelos prontos (assets/modelos/)

Quando um gap pedir documento, parta do modelo DOCX correspondente em vez de
redigir do zero — são modelos da casa com placeholders:

- Contratação: `contrato-individual-trabalho.docx`,
  `termo-prorrogacao-contrato-experiencia.docx`,
  `termo-confidencialidade-trabalhista.docx`,
  `termo-recebimento-cartao-beneficios.docx`.
- Disciplina (gradação advertência → suspensão → justa causa):
  `carta-advertencia-disciplinar.docx`, `carta-suspensao-disciplinar.docx`,
  `procedimento-administrativo-justa-causa.docx`,
  `carta-faltas-injustificadas-abandono-emprego.docx`,
  `orientacao-devido-falta.docx`.
- SST: `termo-compromisso-uso-epi.docx` — cobre o gap "EPI sem registro" (NR-6).

Preencha via `formatacao-arquivos-juridicos` e passe pela `acuracia-juridica`.

## Saída

Diagnóstico por domínio (semáforo 🟢🟡🔴) + checklist P0/P1/P2 + matriz de
passivo contingente + plano 30/90/180 + lista do que depende de confirmação em
fonte primária ou da CCT.
