"""Cálculos determinísticos do caso (02/10): o modelo diz O QUE calcular e com quais fatos; o código confere que
cada data/número de entrada está escrito nos fatos citados e faz a conta. Conta não é opinião do modelo
(caso real: o DeepSeek errou 22/09 + 45 + 45 numa rodada e acertou noutra).

Regras conferidas no texto da base de legislação em 02/10/2026:
- CLT art. 445, parágrafo único: contrato de experiência não pode exceder 90 dias;
- CLT art. 451: prazo determinado prorrogado mais de uma vez passa a vigorar sem prazo;
- CLT arts. 479/480: rescisão antecipada em contrato com termo (empregador: metade da remuneração até o termo;
  empregado: indeniza prejuízos, limitada ao que o empregado teria direito em idênticas condições);
- CLT art. 481: com cláusula assecuratória, valem as regras do prazo indeterminado;
- Lei 12.506/2011: aviso de 30 dias + 3 por ano de serviço, até 60 a mais (total 90);
- CF art. 7º, XXIX: prescrição de 5 anos, até o limite de 2 anos após a extinção do contrato.
"""
from __future__ import annotations

import re
import unicodedata
from datetime import date, timedelta

MESES = {m: i for i, m in enumerate(
    ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"], start=1)}
DATA_NUM_RE = re.compile(r"\b(\d{1,2})[/.-](\d{1,2})[/.-](\d{4})\b")
DATA_EXT_RE = re.compile(r"\b(\d{1,2})(?:o|º|°)?\s+de\s+([a-z]+)\s+de\s+(\d{4})\b")  # 15/10: _plano faz "1º" virar "1o"


def _plano(texto: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", (texto or "").casefold()) if not unicodedata.combining(c))


def datas_no_texto(texto: str) -> set[date]:
    """Todas as datas escritas no texto: 22/09/2025, 22.09.2025 e "22 de SETEMBRO de 2025"."""
    achadas = set()
    t = _plano(texto)
    for d, m, a in DATA_NUM_RE.findall(t):
        achadas.add(_data(int(a), int(m), int(d)))
    for d, mes, a in DATA_EXT_RE.findall(t):
        if mes in MESES:
            achadas.add(_data(int(a), MESES[mes], int(d)))
    return {d for d in achadas if d and 1950 <= d.year <= 2100}  # "5.12.0013" do número CNJ não é data


def _data(a: int, m: int, d: int) -> date | None:
    try:
        return date(a, m, d)
    except ValueError:
        return None


def ler_data(valor) -> date | None:
    datas = datas_no_texto(str(valor or ""))
    return next(iter(datas)) if len(datas) == 1 else None


def fmt(d: date | None) -> str:
    return d.strftime("%d/%m/%Y") if d else "-"


def termo(inicio: date, dias: int) -> date:
    """Prazo de N dias com o 1º dia incluído: 45 dias a partir de 22/09/2025 terminam em 05/11/2025."""
    return inicio + timedelta(days=dias - 1)


def prazo_contrato(inicio: date, dias: int, prorrogacao_dias: int = 0, rescisao: date | None = None,
                   experiencia: bool = True, prorrogacoes: int = 1) -> dict:
    termo_inicial = termo(inicio, dias)
    termo_final = termo(termo_inicial + timedelta(days=1), prorrogacao_dias) if prorrogacao_dias else termo_inicial
    total = dias + prorrogacao_dias
    passos = [f"{dias} dias a partir de {fmt(inicio)} → termo em {fmt(termo_inicial)}"]
    if prorrogacao_dias:
        passos.append(f"prorrogação de {prorrogacao_dias} dias a partir de {fmt(termo_inicial + timedelta(days=1))} → termo em {fmt(termo_final)}")
    alertas, regras = [], []
    if experiencia and total > 90:
        alertas.append(f"experiência de {total} dias excede o limite de 90 dias")
        regras.append("CLT, art. 445, parágrafo único")
    if prorrogacoes > 1:
        alertas.append(f"{prorrogacoes} prorrogações: o contrato passa a vigorar sem prazo")
        regras.append("CLT, art. 451")
    resultado = {"termo_inicial": fmt(termo_inicial), "termo_final": fmt(termo_final), "total_dias": total,
                 "passos": passos, "alertas": alertas, "regras": regras}
    if rescisao:
        if rescisao <= termo_inicial:
            situacao = "rescisão antes do termo inicial (sem prorrogação em curso)"
        elif rescisao <= termo_final:
            situacao = "rescisão dentro do prazo prorrogado: o contrato ainda era por prazo determinado"
        else:
            situacao = "rescisão depois do termo final: o contrato já vigorava por prazo indeterminado"
        restantes = (termo_final - rescisao).days if rescisao <= termo_final else 0
        passos.append(f"rescisão em {fmt(rescisao)}: {situacao}; faltavam {restantes} dias para o termo ({fmt(termo_final)})")
        resultado.update(situacao=situacao, dias_restantes=restantes, antecipada=restantes > 0)
        if restantes > 0 and not alertas:
            regras += ["CLT, art. 479", "CLT, art. 480", "CLT, art. 481"]
    return resultado


def aviso_previo(admissao: date, desligamento: date) -> dict:
    """30 dias + 3 por ano completo de serviço, até 90. ponytail: "ano de serviço" = ano completo (leitura usual);
    a contagem do ano incompleto é controvertida e fica no alerta."""
    anos = (desligamento.year - admissao.year) - ((desligamento.month, desligamento.day) < (admissao.month, admissao.day))
    dias = min(30 + 3 * max(anos, 0), 90)
    return {"anos_completos": max(anos, 0), "dias_aviso": dias, "regras": ["Lei 12.506/2011, art. 1º"],
            "passos": [f"{fmt(admissao)} a {fmt(desligamento)}: {max(anos, 0)} ano(s) completo(s) → 30 + 3×{max(anos, 0)} = {dias} dias"],
            "alertas": ["contagem por ano completo; conferir o entendimento sobre fração de ano"]}


def prescricao(extincao: date, ajuizamento: date | None = None, admissao: date | None = None,
               projecao: date | None = None) -> dict:
    """20/10 (aval7, c2): o biênio conta do fim do aviso prévio, não do último dia trabalhado — a contestação declarou
    "fora do biênio" (16/09/2022 → 16/09/2024) uma ação de 18/10/2024 com aviso projetado até 19/10/2022.
    Base (conferida em 20/10): CLT, art. 487, § 1º (integração do aviso no tempo de serviço); OJ 83 da SBDI-1 ("a
    prescrição começa a fluir no final da data do término do aviso prévio"); Lei 12.506/2011 (dias do aviso).
    `projecao` = termo do aviso escrito nos autos; sem ela, projeta pela Lei 12.506 a partir da admissão; sem as duas,
    conta do desligamento e avisa. Quinquenal só com admissão anterior ao marco (ajuizamento − 5 anos)."""
    regras, passos, alertas = ["CF, art. 7º, XXIX"], [], []
    fim = extincao
    if projecao:
        fim = projecao
        passos.append(f"desligamento em {fmt(extincao)}, aviso prévio projetado até {fmt(projecao)} (escrito nos autos)")
        regras += ["CLT, art. 487, § 1º", "OJ 83 da SBDI-1 do TST"]
    elif admissao:
        dias = aviso_previo(admissao, extincao)["dias_aviso"]
        fim = extincao + timedelta(days=dias)
        passos.append(f"desligamento em {fmt(extincao)} + aviso prévio de {dias} dias → contrato projetado até {fmt(fim)}")
        regras += ["Lei 12.506/2011, art. 1º", "CLT, art. 487, § 1º", "OJ 83 da SBDI-1 do TST"]
        alertas.append("projeção presume aviso indenizado a partir do desligamento; se o aviso foi trabalhado, a extinção é a própria data")
    else:
        alertas.append("sem admissão nem termo do aviso projetado: biênio contado do desligamento, sem projeção do aviso — "
                       "conferir antes de alegar prescrição bienal")
    limite = _mesmo_dia(fim, 2)
    passos.append(f"extinção em {fmt(fim)} → ação até {fmt(limite)} (2 anos)")
    resultado = {"limite_bienal": fmt(limite), "extincao_projetada": fmt(fim), "regras": regras, "passos": passos, "alertas": alertas}
    if ajuizamento:
        dentro = ajuizamento <= limite
        marco = _mesmo_dia(ajuizamento, -5)
        resultado.update(dentro_do_biênio=dentro, marco_quinquenal=fmt(marco))
        passos.append(f"ajuizada em {fmt(ajuizamento)}: " + ("DENTRO do biênio — NÃO alegar prescrição bienal" if dentro
                                                            else "FORA do biênio — prescrição bienal (total)"))
        if admissao:
            resultado["sem_parcela_prescrita"] = admissao >= marco
            passos.append(f"admissão em {fmt(admissao)} {'posterior' if admissao >= marco else 'anterior'} ao marco quinquenal "
                          f"({fmt(marco)}): " + ("NENHUMA parcela prescrita — não alegar prescrição quinquenal" + (
                              " nem criar tópico de prescrição" if dentro else "") if admissao >= marco
                              else f"créditos anteriores a {fmt(marco)} prescritos, se houver pedido sobre esse período"))
        else:
            passos.append(f"créditos anteriores a {fmt(marco)} prescritos (quinquenal), se o contrato começou antes dessa data")
    return resultado


def _mesmo_dia(d: date, anos: int) -> date:
    try:
        return d.replace(year=d.year + anos)
    except ValueError:  # 29/02
        return d.replace(year=d.year + anos, day=28)


# ---- avos de 13º e férias proporcionais (02/10). Regras conferidas na base:
# Lei 4.090/1962, art. 1º, §2º: fração IGUAL OU SUPERIOR a 15 dias de trabalho = mês integral (13º, por mês civil);
# CLT, art. 146, parágrafo único: férias proporcionais na proporção de 1/12 por mês de serviço ou fração SUPERIOR a 14 dias
# (mês contado a partir da data de admissão, dentro do período aquisitivo em curso).
def _mais_meses(d: date, meses: int) -> date:
    m = d.month - 1 + meses
    ano, mes = d.year + m // 12, m % 12 + 1
    for dia in (d.day, 30, 29, 28):
        try:
            return date(ano, mes, min(d.day, dia))
        except ValueError:
            continue
    raise ValueError(d)


def avos(admissao: date, desligamento: date) -> dict:
    """ponytail: sem projeção do aviso prévio indenizado; quando houver, somar os dias antes de chamar (alerta)."""
    inicio_ano = max(admissao, date(desligamento.year, 1, 1))
    avos13, meses13 = 0, []
    mes = date(inicio_ano.year, inicio_ano.month, 1)
    while mes <= desligamento:
        prox = _mais_meses(mes, 1)
        dias = (min(prox - timedelta(days=1), desligamento) - max(mes, inicio_ano)).days + 1
        if dias >= 15:
            avos13 += 1
        meses13.append(f"{mes.month:02d}/{mes.year}: {dias} dia(s){' ✓' if dias >= 15 else ''}")
        mes = prox
    anos = (desligamento.year - admissao.year) - ((desligamento.month, desligamento.day) < (admissao.month, admissao.day))
    periodo = _mais_meses(admissao, 12 * max(anos, 0))
    meses = 0
    while _mais_meses(periodo, meses + 1) - timedelta(days=1) <= desligamento:
        meses += 1
    resto = (desligamento - _mais_meses(periodo, meses)).days + 1
    avos_ferias = min(meses + (1 if resto > 14 else 0), 12)
    return {
        "avos_13": avos13, "avos_ferias": avos_ferias, "periodo_aquisitivo_inicio": fmt(periodo),
        "passos": [f"13º de {desligamento.year}: " + "; ".join(meses13) + f" → {avos13}/12",
                   f"férias: período aquisitivo desde {fmt(periodo)}, {meses} mês(es) completo(s) + {resto} dia(s)"
                   f"{' (> 14: conta)' if resto > 14 else ''} → {avos_ferias}/12"],
        "alertas": ["sem projeção do aviso prévio indenizado; se houver, recalcular com a data projetada"],
        "regras": ["Lei 4.090/1962, art. 1º, §2º", "CLT, art. 146, parágrafo único"],
    }


# ---- prazo processual (porta do motor da skill calculo-prazos-cpc do plugin, 02/10)
# CPC 219 / CLT 775: dias úteis; CPC 224 §2-3: publicação = 1º dia útil após a disponibilização, contagem no 1º dia
# útil seguinte; CPC 220 / CLT 775-A: suspensão de 20/12 a 20/01. Feriados: nacionais fixos e móveis forenses da
# lista do plugin. ponytail: sem feriado local por tribunal (alerta pede conferir a portaria), entra quando houver tabela.
FERIADOS_FIXOS = {(1, 1): "Confraternização Universal", (4, 21): "Tiradentes", (5, 1): "Dia do Trabalho",
                  (9, 7): "Independência", (10, 12): "Nossa Senhora Aparecida", (11, 2): "Finados",
                  (11, 15): "Proclamação da República", (11, 20): "Consciência Negra", (12, 25): "Natal"}


def pascoa(ano: int) -> date:
    """Domingo de Páscoa (Meeus/Butcher)."""
    a, b, c = ano % 19, ano // 100, ano % 100
    d, e = b // 4, b % 4
    g = (b - (b + 8) // 25 + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l_ = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l_) // 451
    return date(ano, (h + l_ - 7 * m + 114) // 31, (h + l_ - 7 * m + 114) % 31 + 1)


def feriados(ano: int) -> dict[date, str]:
    fer = {date(ano, m, d): nome for (m, d), nome in FERIADOS_FIXOS.items()}
    p = pascoa(ano)
    fer.update({p - timedelta(days=48): "Carnaval (segunda)", p - timedelta(days=47): "Carnaval (terça)",
                p - timedelta(days=2): "Sexta-feira Santa", p + timedelta(days=60): "Corpus Christi"})
    return fer


def _nao_util(d: date, fer: dict[date, str]) -> str | None:
    if d.weekday() >= 5:
        return "sábado" if d.weekday() == 5 else "domingo"
    if (d.month == 12 and d.day >= 20) or (d.month == 1 and d.day <= 20):
        return "suspensão de 20/12 a 20/01"
    return fer.get(d)


def prazo_processual(disponibilizacao: date, dias: int, corridos: bool = False, pessoal: bool = False) -> dict:
    fer = {k: v for ano in range(disponibilizacao.year, disponibilizacao.year + 3) for k, v in feriados(ano).items()}

    def seguinte_util(d: date) -> date:
        d += timedelta(days=1)
        while _nao_util(d, fer):
            d += timedelta(days=1)
        return d

    # 20/10 (aval7): ciência pessoal (oficial de justiça, AR) não tem o dia da publicação — CLT 774 conta "a partir da
    # data em que for feita pessoalmente, ou recebida a notificação" e CLT 775 exclui o dia do começo (c1: 13/11 → 05/12)
    publicacao = disponibilizacao if pessoal else seguinte_util(disponibilizacao)
    inicio = seguinte_util(publicacao)
    pulados, venc = [], inicio
    if corridos:
        venc = inicio + timedelta(days=dias - 1)
        while motivo := _nao_util(venc, fer):
            pulados.append(f"{fmt(venc)} ({motivo})")
            venc += timedelta(days=1)
    else:
        contados = 1
        while contados < dias:
            venc += timedelta(days=1)
            if motivo := _nao_util(venc, fer):
                pulados.append(f"{fmt(venc)} ({motivo})")
            else:
                contados += 1
    passos = [f"ciência pessoal em {fmt(disponibilizacao)} → contagem a partir de {fmt(inicio)}" if pessoal else
              f"disponibilizado em {fmt(disponibilizacao)} → publicação {fmt(publicacao)} → contagem a partir de {fmt(inicio)}",
              f"{dias} dias {'corridos' if corridos else 'úteis'} → vencimento em {fmt(venc)}"]
    if pulados:
        passos.append("dias não contados: " + ", ".join(pulados[:15]) + (" …" if len(pulados) > 15 else ""))
    return {"publicacao": fmt(publicacao), "inicio": fmt(inicio), "vencimento": fmt(venc), "passos": passos,
            "alertas": ["feriados locais e suspensões do tribunal não incluídos: conferir a portaria"],
            "regras": (["CLT, art. 774", "CLT, art. 775", "CLT, art. 775-A"] if pessoal else
                       ["CPC, art. 219", "CPC, art. 220", "CPC, art. 224", "CLT, art. 775", "CLT, art. 775-A"])}


CALCULOS = {
    "avos": (avos, {"admissao": "data", "desligamento": "data"}),
    "prazo_processual": (prazo_processual, {"disponibilizacao": "data", "dias": "int", "corridos": "bool"}),
    "prazo_contrato": (prazo_contrato, {"inicio": "data", "dias": "int", "prorrogacao_dias": "int", "rescisao": "data",
                                        "experiencia": "bool", "prorrogacoes": "int"}),
    "aviso_previo": (aviso_previo, {"admissao": "data", "desligamento": "data"}),
    "prescricao": (prescricao, {"extincao": "data", "ajuizamento": "data", "admissao": "data", "projecao": "data"}),
}


def executar(tipo: str, parametros: dict, texto_dos_fatos: str) -> tuple[dict | None, str]:
    """Roda um cálculo só com entradas que estão ESCRITAS nos fatos citados. Devolve (resultado, motivo da recusa)."""
    if tipo not in CALCULOS:
        return None, f"cálculo desconhecido: {tipo}"
    funcao, campos = CALCULOS[tipo]
    datas_dos_fatos = datas_no_texto(texto_dos_fatos)
    # 07/10: número tem de estar escrito como número — "9" dentro de "01/09/2025", do CNJ ou de "1.234,56" não vale
    sem_datas = re.sub(r"\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}|\d{1,2}/\d{1,2}/\d{2,4}|\d+(?:[.,]\d+)+", " ", texto_dos_fatos)
    numeros_dos_fatos = {int(n) for n in re.findall(r"\b\d{1,4}\b", sem_datas)}
    args = {}
    for nome, valor in (parametros or {}).items():
        if nome not in campos or valor in (None, ""):
            continue
        if campos[nome] == "data":
            d = ler_data(valor)
            if not d or d not in datas_dos_fatos:
                return None, f"{nome}={valor} não está escrito nos fatos citados"
            args[nome] = d
        elif campos[nome] == "int":
            try:
                n = int(valor)
            except (TypeError, ValueError):
                return None, f"{nome}={valor} não é número"
            if nome != "prorrogacoes" and n not in numeros_dos_fatos:
                return None, f"{nome}={n} não está escrito nos fatos citados"
            args[nome] = n
        else:   # 07/10: bool("false") é True — prazo em dias corridos saía como úteis (vencimento errado)
            args[nome] = valor is True or str(valor).strip().casefold() in ("true", "sim", "s", "1", "yes")
    for antes, depois in (("admissao", "desligamento"), ("inicio", "rescisao"), ("extincao", "ajuizamento"),
                          ("admissao", "extincao"), ("extincao", "projecao"), ("projecao", "ajuizamento")):
        if antes in args and depois in args and args[antes] > args[depois]:
            return None, f"{antes} posterior a {depois}: datas trocadas ou lidas errado"
    try:
        return funcao(**args), ""
    except TypeError as exc:  # faltou parâmetro obrigatório
        return None, f"parâmetros incompletos: {exc}"


# ---- tempestividade da peça pedida (20/10, aval7: em 6 de 7 peças a data final saiu em branco, [PREENCHER] ou contada de
# outra intimação — c1 contou da publicação DJEN ao reclamante, 29/09, em vez da citação por oficial, 13/11). O ato inicial
# é achado EM CÓDIGO nas peças dos autos e o prazo sai do motor acima; o modelo só escreve. Regras conferidas na base
# (legislacao/CLT-Decreto-Lei-5452-1943.txt): art. 774 — prazo "a partir da data em que for feita pessoalmente, ou recebida
# a notificação" ou da publicação; art. 775 — dias úteis, "com exclusão do dia do começo e inclusão do dia do vencimento".
# ponytail: cobre (a) data fixada no despacho/notificação ("defesa até o dia X"), (b) certidão do oficial de justiça e
# (c) certidão de disponibilização no DJEN da intimação da decisão; ciência pelo Domicílio Judicial Eletrônico, AR e
# o que mais não casar vira lacuna explícita — nunca uma data deduzida.
NOME_PECA_RE = re.compile(r"›\s*([^›(]+?)\s*\(Id\s*([0-9a-f]{7}),\s*(\d{2}/\d{2}/\d{4})", re.I)  # "› Certidão (Id 5293968, 13/11/2025, p. 48)"
ATO_NOME_RE = re.compile(r"cita|despacho|intima|audien|decis|notific")
DEFESA_ATE_RE = re.compile(r"defesa\b[^.;]{0,60}?\bat[ée]\s+(?:o\s+)?dia\s+(\d{1,2}/\d{1,2}/\d{4})", re.I)
PRAZO_DEFESA_RE = re.compile(r"(?:contesta\w*|defesa)\b[^.;]{0,160}?\bprazo de (\d{1,2})\s*(?:\([^)]{0,20}\)\s*)?dias?\b\s*(corridos)?", re.I)
CIENCIA_PESSOAL_RE = re.compile(r"\bcitei\b|\bnotifiquei\b|procedeu-se [àa] (?:cita|notifica)|recebeu (?:e assinou )?a contraf[ée]|"
                                r"citad[ao] na pessoa", re.I)
DJEN_RE = re.compile(r"Documento Publicado:[^\n]{0,80}?\b([0-9a-f]{7})\b.{0,80}?Data de Disponibiliza[çc][ãa]o:\s*(\d{2}/\d{2}/\d{4})", re.I)
INTIMACAO_DECISAO_RE = re.compile(r"ci[êe]ncia d[ao] (?:senten[çc]a|decis[ãa]o|ac[óo]rd[ãa]o)", re.I)
CONTRARRAZOES_RE = re.compile(r"contra-?r?raz", re.I)  # 22/10 (auditoria): "contrarrazões" tem dois r — antes só "contrarazões"
PRAZO_CONTRARRAZOES = (8, ["Lei 5.584/1970 art. 6º", "CLT art. 900"])  # texto em trava_processual.FONTES


def _data_da_certidao(texto: str) -> date | None:
    """A data da ciência na certidão do oficial: a escrita por extenso ("XANXERE/SC, 13 de novembro de 2025"); sem ela,
    a única data do texto. Mais de uma candidata = ambíguo, fica a lacuna."""
    t = _plano(texto)
    extenso = {d for dd, mes, a in DATA_EXT_RE.findall(t) if mes in MESES for d in [_data(int(a), MESES[mes], int(dd))] if d}
    if len(extenso) == 1:
        return next(iter(extenso))
    todas = datas_no_texto(texto)
    return next(iter(todas)) if len(todas) == 1 else None


def tempestividade(pecas: list[tuple[str, str]], pedido: str) -> dict | None:
    """Ato inicial, prazo e vencimento da PEÇA PEDIDA, achados nas peças dos autos [(nome, texto)]. None quando o pedido
    não é contestação nem peça recursal. Sem o ato nos autos: `vencimento` None e `lacuna` com o [PREENCHER] a escrever."""
    from collections import Counter

    from ..trava_processual import NOMES, REMEDIOS, peca_pedida

    cod = peca_pedida(pedido)
    if not cod and not re.search(r"contest|defesa", _plano(pedido)):  # "conteste" (c1, c3) não contém "contesta"
        return None
    lidas = []  # (nome, tipo pelo nome, id, texto numa linha)
    for nome, texto in pecas:
        m = NOME_PECA_RE.search(nome)
        lidas.append((nome, _plano(m.group(1)) if m else _plano(nome), m.group(2).lower() if m else "", " ".join((texto or "").split())))
    fontes = lambda *nomes: "; ".join(f"[Fonte Documento: {n}]" for n in nomes)  # noqa: E731
    if not cod:
        r = {"peca": "contestação", "dias": None, "vencimento": None, "lacuna": None, "passos": [], "alertas": [], "regras": [], "fontes": ""}
        atos = [(nome, t) for nome, tipo, _, t in lidas if ATO_NOME_RE.search(tipo)]
        fixadas = [(d, nome) for nome, t in atos for m in DEFESA_ATE_RE.finditer(t) if (d := ler_data(m.group(1)))]
        if fixadas:  # c2: "apresente defesa até dia 02/12/2024" — a data vem escrita; vale a última fixada
            venc, nome = fixadas[-1]
            r.update(vencimento=fmt(venc), passos=[f"o juízo fixou a defesa até {fmt(venc)}"], fontes=fontes(nome))
            return r
        prazos = Counter((int(m.group(1)), bool(m.group(2))) for _, t in atos for m in PRAZO_DEFESA_RE.finditer(t))
        certidoes = [(nome, t) for nome, tipo, _, t in lidas if re.search(r"certid|cita|mandado", tipo) and CIENCIA_PESSOAL_RE.search(t)]
        if prazos:
            (r["dias"], corridos), _ = prazos.most_common(1)[0]
            r["fontes"] = fontes(next(nome for nome, t in atos if PRAZO_DEFESA_RE.search(t)))
        if certidoes and prazos:
            nome, t = certidoes[-1]  # a última: a reiteração por oficial substitui a tentativa anterior (c3)
            if ciencia := _data_da_certidao(t):
                calc = prazo_processual(ciencia, r["dias"], corridos=corridos, pessoal=True)
                r.update(vencimento=calc["vencimento"], passos=[f"citação/notificação por oficial de justiça em {fmt(ciencia)}", *calc["passos"]],
                         alertas=calc["alertas"], regras=calc["regras"], fontes=fontes(nome) + "; " + r["fontes"])
                return r
            r["lacuna"] = f"[PREENCHER: data da ciência — a certidão {nome.split('›')[-1].strip()} tem mais de uma data]"
            return r
        r["lacuna"] = ("[PREENCHER: data em que a reclamada recebeu a citação/notificação]" if prazos else
                       "[PREENCHER: data da citação/notificação e prazo fixado para a defesa]")
        return r
    dias, regras = REMEDIOS.get(cod, {}).get("prazo", (None, [])) if cod != "contrarrazoes" else PRAZO_CONTRARRAZOES
    r = {"peca": NOMES.get(cod, cod), "dias": dias, "vencimento": None, "lacuna": None, "passos": [], "alertas": [],
         "regras": list(regras), "fontes": ""}
    alvo = CONTRARRAZOES_RE if cod == "contrarrazoes" else INTIMACAO_DECISAO_RE
    intimacoes = [(nome, id_) for nome, tipo, id_, t in lidas if "intima" in tipo and alvo.search(t)]
    if not intimacoes:
        r["lacuna"] = ("[PREENCHER: data da intimação para contrarrazões]" if cod == "contrarrazoes" else
                       "[PREENCHER: data da intimação da decisão recorrida]")
        return r
    nome_i, id_i = intimacoes[-1]  # a última intimação de decisão: a dos embargos, quando houve (r1, r2)
    djen = next(((d, nome) for nome, _, _, t in lidas for m in DJEN_RE.finditer(t)
                 if m.group(1).lower() == id_i and (d := ler_data(m.group(2)))), None)
    if djen and dias:
        calc = prazo_processual(djen[0], dias)
        # 28/10 (aval27 r1): "intimação Intimação (Id 0055708, 13/04/2026…)" fazia escrever "a intimação ocorreu em 13/04" —
        # a data do nome é a da expedição; intimada a parte está na publicação (CPC 224, § 2º)
        r.update(vencimento=calc["vencimento"], passos=[
                     f"{nome_i.split('›')[-1].strip()}: a data no nome é a da expedição, não a da intimação — a parte "
                     f"está intimada na publicação no DJEN, em {calc['publicacao']}", *calc["passos"]],
                 alertas=calc["alertas"], regras=r["regras"] + calc["regras"], fontes=fontes(nome_i, djen[1]))
        return r
    r["lacuna"] = f"[PREENCHER: data da publicação/ciência da intimação {nome_i.split('›')[-1].strip()}]"
    r["fontes"] = fontes(nome_i)
    return r


def bloco_tempestividade(r: dict) -> str:
    """Texto que vai ao modelo: datas prontas ou a lacuna exata a escrever."""
    if r["vencimento"]:
        linhas = [f"- {p}" for p in r["passos"]] + [f"- VENCIMENTO: {r['vencimento']}"] + [f"- ⚠ {a}" for a in r["alertas"]]
        if r["regras"]:
            linhas.append(f"- regras: {', '.join(r['regras'])}")
        linhas.append(f"- fontes a citar: {r['fontes']}")
        ordem = "escreva a seção de tempestividade com ESTAS datas e fontes; não recalcule nem conte de outra intimação"
    else:
        prazo = (f" O prazo é de {r['dias']} dias úteis" + (f" ({', '.join(r['regras'])})" if r["regras"] else "") + "."
                 if r["dias"] else "")
        linhas = [f"- A data do ato inicial NÃO está nos autos enviados: escreva exatamente \"{r['lacuna']}\" na seção.{prazo}"
                  + (f" Fonte do prazo: {r['fontes']}" if r["fontes"] else "")]
        ordem = "não deduza a data de outra peça, da data da decisão nem de intimação dirigida à outra parte"
    return f"TEMPESTIVIDADE DA PEÇA — {r['peca'].upper()} (achada pelo sistema nos autos, sem IA; {ordem}):\n" + "\n".join(linhas)
