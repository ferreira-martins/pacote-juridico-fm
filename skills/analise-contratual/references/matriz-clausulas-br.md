# Matriz de cláusulas — análise contratual (Brasil)

Checklist de cláusulas a percorrer na análise. Para cada uma: identifique o
texto, avalie o risco **para o lado do cliente** (🟢/🟡/🔴), atribua confiança e
proponha redline quando 🟡/🔴.

> **Atenção a dispositivos legais.** Os artigos citados abaixo são **pontos de
> partida** para orientar a análise — confirme o número e a vigência antes de
> citar na saída (passe pela `acuracia-juridica`). Direito muda; não cite de
> memória sem verificar.

## Regime aplicável (decida primeiro)

A leitura de quase toda cláusula muda conforme o regime:

- **Código Civil (CC, Lei 10.406/2002)** — contratos paritários (B2B), regra da
  autonomia da vontade; revisão do CC 2002 reforçou a força obrigatória em
  contratos empresariais (vide art. 421-A, incluído pela Lei da Liberdade
  Econômica).
- **CDC (Lei 8.078/1990)** — relação de consumo (destinatário final +
  fornecedor). Traz vedações de ordem pública: cláusulas abusivas (art. 51),
  limites de multa, foro protetivo. **Não é afastável por vontade das partes.**
- **CLT** — se houver pessoalidade, habitualidade, subordinação e onerosidade
  (atenção a "PJ" que mascara emprego).
- **LGPD (Lei 13.709/2018)** — sempre que houver tratamento de dados pessoais.

## 1. Objeto e escopo
- Objeto determinado/determinável? Escopo aberto demais favorece quem executa e
  prejudica quem contrata (e vice-versa). Anexos/SLA fazem parte?

## 2. Preço, reajuste e pagamento
- **Índice de reajuste** explícito (IPCA, INPC, IGP-M)? Periodicidade mínima
  legal (anual). Ausência de índice é risco para o credor.
- **Multa e juros moratórios**: em consumo, multa de mora limitada a **2%**
  (CDC art. 52, §1º). Entre empresas, multa moratória costuma ser livre, mas
  multa compensatória desproporcional pode ser reduzida (CC art. 413 — redução
  equitativa pelo juiz).
- Condições de reajuste extraordinário/desequilíbrio (revisão — CC arts. 317 e
  478, onerosidade excessiva).

## 3. Responsabilidade e limitação
- **Cláusula limitativa/exonerativa de responsabilidade**: válida entre
  empresas paritárias; **nula em consumo** quando exonera ou atenua de forma
  abusiva (CDC art. 51, I). Verifique teto (cap), exclusão de danos indiretos/
  lucros cessantes, reciprocidade.
- Caps unilaterais (só protegem uma parte) são 🟡/🔴 conforme o lado.

## 4. Indenização / perdas e danos
- Escopo, reciprocidade, hipóteses (violação de dados, PI, terceiros). Dever de
  indenizar e extensão (CC arts. 402-404). Carve-outs equilibrados?

## 5. Garantias e vícios
- Vícios redibitórios (CC arts. 441 e ss.); em consumo, garantia legal e prazos
  de reclamação (CDC arts. 18, 26). Garantia contratual adicional? Disclaimers
  amplos são 🔴 em consumo.

## 6. Confidencialidade e proteção de dados (LGPD)
- Definição de informação confidencial, prazo de sobrevivência, exceções.
- **LGPD**: papéis de **controlador/operador** (art. 5º), **base legal** do
  tratamento (art. 7º / art. 11 para dados sensíveis), finalidade, segurança,
  resposta a incidente, e **responsabilidade** (arts. 42-45). Subcontratação de
  operador (suboperador) autorizada? Cláusula de eliminação ao fim do contrato.

## 7. Propriedade intelectual
- Titularidade do resultado/obra (CC; Lei 9.610/98 direitos autorais; Lei
  9.279/96 PI). Cessão x licença, escopo, exclusividade, IP de background do
  prestador. "Tudo do contratante" sem ressalva pode ser 🔴 para o prestador.

## 8. Prazo, renovação e rescisão
- Prazo determinado/indeterminado; **renovação automática** (e janela para
  denúncia). Direito de **resilição** (CC art. 473) e necessidade de aviso
  prévio proporcional ao investimento (parágrafo único do art. 473).
- **Multa rescisória/compensatória**: proporcional? (CC art. 413 permite redução).
- Hipóteses de rescisão por inadimplemento (CC arts. 474-475, cláusula
  resolutiva expressa x tácita).

## 9. Foro e arbitragem
- **Foro de eleição** (CPC art. 63). Em contrato de adesão/consumo, foro que
  dificulte a defesa do aderente é abusivo e pode ser declarado de ofício (CPC
  art. 63, §§; CDC art. 51, IV). Para o cliente aderente, foro distante é 🔴.
- **Arbitragem** (Lei 9.307/96): cuidado em consumo e adesão — cláusula
  compromissória só vincula o aderente se ele tomar a iniciativa ou concordar
  expressamente (art. 4º, §2º). Avalie custo da arbitragem x valor do contrato.

## 10. Penalidades e cláusula penal
- Cláusula penal (CC arts. 408-416): não pode exceder a obrigação principal
  (art. 412); redução por cumprimento parcial ou exagero (art. 413).

## 11. Cessão, subcontratação e mudança de controle
- Necessidade de anuência para ceder/subcontratar; gatilho de *change of control*.

## 12. Caso fortuito / força maior
- Definição e efeitos (CC art. 393). Pandemia/eventos cobertos? Suspensão x
  rescisão; quem suporta custos.

## 13. Cláusulas abusivas (radar de consumo — CDC art. 51)
Se for relação de consumo, varra o rol exemplificativo do art. 51 (exoneração de
responsabilidade, renúncia de direitos, inversão de ônus em desfavor do
consumidor, opção exclusiva do fornecedor, etc.). Achado aqui é tipicamente 🔴.

## 14. Não concorrência / não aliciamento
- Restrição de concorrência precisa de **limite de tempo, território e
  atividade** e, em regra, contrapartida — restrição ampla/sem compensação é
  🔴 (e em vínculo trabalhista, atenção à validade).
