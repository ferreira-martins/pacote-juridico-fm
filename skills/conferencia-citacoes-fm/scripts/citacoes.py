"""Citações de dispositivos ("art. 59 da CLT" → "CLT art. 59"). Só stdlib: as ferramentas de carga
(tools/base_grafo.py) importam este módulo sem as dependências do servidor."""

from __future__ import annotations

import re


def artigo_canon(numero: str) -> str:
    """"59", "4º", "1.025", "457-A", "401A" → "59", "4", "1025", "457-A", "401-A" (chave estável dos dois lados do grafo)."""
    n = re.sub(r"\s+", "", numero or "").replace("º", "").replace("°", "").replace(".", "")
    n = re.sub(r"(?<=\d)o$", "", n)
    n = re.sub(r"(?<=\d)o(?=-[A-Za-z]$)", "", n)  # 29/10: "5o-C" (Planalto, Lei 6.019) → "5-C"; antes nunca casava
    return re.sub(r"(?<=\d)-?([A-Za-z])$", lambda m: "-" + m.group(1).upper(), n)


# Diploma depois do artigo: sigla (maiúscula, palavra inteira), nome por extenso ou número ("Lei nº 12.506/2011",
# "Decreto-Lei 911/69", "LC 150"). As siglas casam com `aliases` dos documentos de lei (tools/leis_geral.py).
_NOMES = {
    "CLT": r"CLT|(?i:Consolida[çc][ãa]o das Leis do Trabalho)", "CF": r"CF(?:/88)?|(?i:Constitui[çc][ãa]o(?: Federal)?)", "CPC": r"CPC|(?i:C[óo]digo de Processo Civil)",
    "CPP": r"CPP|(?i:C[óo]digo de Processo Penal)", "CDC": r"CDC|(?i:C[óo]digo de Defesa do Consumidor)",
    "CTN": r"CTN|(?i:C[óo]digo Tribut[áa]rio Nacional)", "CTB": r"CTB|(?i:C[óo]digo de Tr[âa]nsito)",
    "CC": r"CC|(?i:C[óo]digo Civil)", "CP": r"CP|(?i:C[óo]digo Penal)", "ECA": r"ECA", "LINDB": r"LINDB",
}
# 27/10: número começa por dígito — "desta lei. Art. 86" casava "lei." como diploma ("Lei  art. 86")
_NUMERADO = r"(?i:Decreto-Lei|Decreto|Lei\s+Complementar|LC|Lei)\s*(?:n\.?[º°]?\.?)?\s*\d[\d.]*(?:/\d{2,4})?"
_DIPLOMA = r"(" + "|".join(r"\b(?:" + v + r")\b" for v in _NOMES.values()) + "|" + _NUMERADO + ")"
# número: "59", "4º", "1.025", "457-A", "401A" — letra só MAIÚSCULA colada (senão o "e" de "59 e 61" vira sufixo)
_N = r"\d[\d.]*(?:\s?[ºo°])?(?:-?[A-Z](?![A-Za-zÀ-ú]))?"
# 27/10 (leitor único): "artigo 847 da Consolidação das Leis do Trabalho" (peças reais e minutas) — só o medidor lia
_ART = r"\b(?:[Aa][Rr][Tt][Ss]?\s*\.|(?i:artigos?)\b)"
# 27/10 (leitor único, aval22 h4): "artigos 5º, 373, II, 385, 489, § 1º, IV, do CPC" — inciso e parágrafo no meio da
# lista não a encerram; "§§ 2º e 3º" é parágrafo, não artigo (sai antes de ler os números)
_PARAGRAFO = r"§+\s*\d+\s*[ºo°]?(?:\s*(?:,|e)\s*\d+\s*[ºo°]?(?![\d.]))*"
_INCISO = r"(?:[IVXL]+|[a-z]\))(?![A-Za-zÀ-ú])"
_ARTIGOS = re.compile(_ART + r"\s*(" + _N + r"(?:\s*(?:,\s*e|,|e|a|/)\s*(?:" + _N + "|" + _PARAGRAFO + "|" + _INCISO + r"))*)")
_PARAGRAFO_RE = re.compile(_PARAGRAFO)
_DIPLOMA_RE = re.compile(_DIPLOMA)
# 26/10 (aval25, conv1 passo 5): o rótulo estável do próprio sistema põe o diploma ANTES — "[Fonte Base: CLT (Decreto-Lei
# 5.452/1943), art. 818]". A edição da peça repete esses rótulos; sem lê-los, nenhum voltava à base e todos saíam como
# "Citações não conferidas". Também "CLT, art. 2º" e a chave canônica "CLT art. 818" (golden, grafo).
# 27/10: "Lei de Práticas Discriminatórias (Lei 9.029/1995), art. 4" — o número entre parênteses é o diploma
_DIPLOMA_ANTES_RE = re.compile(_DIPLOMA + r"\)?\s*(?:\([^)]{0,40}\)\s*)?,?\s*$")
_PROXIMO_ART_RE = re.compile(_ART)
# 27/10: "CLT (toda — esp. arts. 477, 482, 847), Lei 13.467/17" — artigo dentro do parêntese aberto logo depois do
# diploma é dele (a lei colada depois do parêntese levava os artigos; o leitor antigo também)
_DENTRO_DE_RE = re.compile(_DIPLOMA + r"\s*\([^()]{0,60}$")
_DE_OUTRO_ART_RE = re.compile(_ART + r"\s*" + _N + r"[^.;\]\n(]{0,40}\bd[oa]s?\s+$")
_DEPOIS_COLADO_RE = re.compile(r"\s*\)?\s*,?\s*(?:todos\s+)?(?:d[oa]s?\s+|n[oa]s?\s+)?(?:(?:C\.|E\.)\s*)?" + _DIPLOMA)
_NUM = re.compile(_N)
# 27/10 (leitor único): "art. 832 da CLT e 489 do CPC" — o número depois do diploma, sem "art.", é de outro diploma
_CONTINUA_RE = re.compile(r"\s*(?:,|\be\b)\s*(" + _N + r")\s*,?\s*(?:d[oa]s?\s+)?" + _DIPLOMA)


def sigla_canon(diploma: str) -> str:
    d = re.sub(r"\s+", " ", diploma or "").strip()
    for sigla, rx in _NOMES.items():
        if re.fullmatch(rx, d):
            return sigla
    m = re.search(r"([\d.]+)(?:/(\d{2,4}))?$", d)
    if not m:
        return d
    tipo = ("Decreto-Lei" if re.match(r"(?i)decreto-lei", d) else "Decreto" if re.match(r"(?i)decreto", d)
            else "LC" if re.match(r"(?i)(lei complementar|lc)", d) else "Lei")
    numero = m.group(1).replace(".", "")
    if not m.group(2):
        return f"{tipo} {numero}"  # "LC 150": casa com o alias sem ano
    ano = m.group(2) if len(m.group(2)) == 4 else ("19" if int(m.group(2)) > 30 else "20") + m.group(2)
    return f"{tipo} {numero}/{ano}"


def citacoes(texto: str) -> list[str]:
    """Dispositivos citados ("CLT art. 59") na ordem em que aparecem. Só artigo com diploma explícito em até
    60 caracteres depois do número — "art. 59" solto não vira aresta (não dá para saber de qual lei é)."""
    vistos: dict[str, None] = {}
    for m in _ARTIGOS.finditer(texto or ""):
        # o "]" fecha a citação: "[… art. 818]. O art. 7º da CF" não faz do 818 um artigo da CF
        # 27/10: até 100 caracteres, com o diploma começando nos 60 primeiros — o corte em 60 partia o nome ("(CP" de
        # "(CPC, art. 400)" virava CP; "Lei nº 9.02" virava Lei 902)
        janela = re.split(r"[;|\n\]]", texto[m.end(): m.end() + 100], maxsplit=1)[0]
        depois, prox = _DIPLOMA_RE.search(janela), _PROXIMO_ART_RE.search(janela)
        depois = depois if depois and depois.start() <= 60 else None
        # diploma colado depois ("art. 818 da CLT") vence; depois o colado antes ("CLT, art. 818", "CLT art. 818"); depois
        # o primeiro antes do próximo "art". Em "art. 341 CPC, art. 818 CLT" o "CPC, " antes do 818 é do 341; em
        # "(CLT, art. 818, § 1º) ou … (CPC, art. 400)" o 818 é da CLT (27/10: o CPC de longe vencia)
        colado = _DEPOIS_COLADO_RE.match(janela)
        inicio = max(0, m.start() - 80)
        antes = _DIPLOMA_ANTES_RE.search(texto[inicio:m.start()])
        # "Art. 790-B da CLT, Art. 98, caput … do CPC": o "CLT, " antes do 98 é do artigo anterior
        if antes and _DE_OUTRO_ART_RE.search(texto[max(0, inicio + antes.start() - 60):inicio + antes.start()]):
            antes = None
        # ponytail: "CLT, art. 157, Lei 8.213/91, art. 19" dá Lei 8.213 ao 157 (o leitor antigo também) — a lista pós-fixa
        # do sistema ("art. 341 CPC, art. 818 CLT") tem a mesma forma; separar exigiria ler a sequência inteira
        # diploma do parêntese que contém o artigo vence só o colado que vem DEPOIS de fechar o parêntese: "(c.c. art. 769
        # da CLT)" é da CLT; "CLT (… arts. 477, 847), Lei 13.467/17" é da CLT também
        dentro = _DENTRO_DE_RE.search(texto[inicio:m.start()])
        if dentro and re.match(r"\s*,?\s*d[ao]s?\s+[A-ZÀ-Ú]", janela):  # "CLT (art. 12 da Instrução Normativa 41)": é da IN
            dentro = None
        if dentro and colado and colado.group(0).lstrip().startswith(")"):
            colado = None
        d = (colado or dentro or antes or (depois if depois and (not prox or depois.start() < prox.start()) else None) or depois)
        if not d:
            continue
        sigla = sigla_canon(d.group(1))
        for numero in _NUM.findall(_PARAGRAFO_RE.sub(" ", m.group(1))):
            vistos.setdefault(f"{sigla} art. {artigo_canon(numero)}", None)
        if d in (colado, depois) and (c := _CONTINUA_RE.match(janela, d.end())):
            vistos.setdefault(f"{sigla_canon(c.group(2))} art. {artigo_canon(c.group(1))}", None)
    return list(vistos) + [c for c in citacoes_jurisprudencia(texto) if c not in vistos]


# Súmulas e OJs: "Súmula 338, III TST", "Súmulas 264 e 347 TST", "Súm. 7/STJ", "OJ 394 da SBDI-1", "OJ-SDI1-394"
_ITEM = r"(?:\s*,\s*(?:ite(?:m|ns)\s+)?[IVX]+(?:\s*(?:,|e)\s*[IVX]+)*\b)?"  # 06/10: "Súmula 338, item III, do TST"
_ITENS = r"\d+" + _ITEM + r"(?:\s*(?:,|e)\s*\d+" + _ITEM + r")*"
_SUMULA = re.compile(r"\bS[úu]m(?:ulas?|\.)\s*(?:n\.?[º°]?s?\.?\s*)?(" + _ITENS + r")\s*(?:,?\s*(?:d[oa]\s+|/)?\s*)(?:(?:C\.|E\.|Colendo|Egr[ée]gio)\s*)?"
                     r"(TST|STJ|STF|TRT[\s-]?12|TRT[\s-]?SC|TRT\s+da\s+12[ªa]\s+Regi[ãa]o)\b")   # 06/10: + TRT12
_SUMULA_ANTES = re.compile(r"\b(TST|STJ|STF|TRT12)\s+S[úu]mula\s+(?:n[º°.]*\s*)?(\d+)\b")
# 06/10: teses do TRT12 ("Tese Jurídica nº 26 do TRT12") e anexos das NRs ("Anexo 13 da NR-15", "NR-16, Anexo 2")
_TESE_TRT12 = re.compile(r"\bTese\s+Jur[íi]dica\s+(?:n[º°.]?\s*)?(\d+)\s*(?:\(?(?:em\s+)?(IRDR|IUJ)\)?)?\s*,?\s*d[oa]\s+TRT[\s-]?(?:12|SC)\b", re.I)
# 16/10: + NR-1/6/7/17 ("Anexo II da NR-7", "Anexo I da NR-01"); as de 2 dígitos vêm antes na alternância
_NR_ANEXO = re.compile(r"\bAnexo\s+(?:n[º°.]?\s*)?(\d+(?:-A)?|[IVX]+)\s*,?\s*(?:d[ao]|à)\s+NR[\s-]?0?(12|15|16|17|35|36|1|6|7)\b"
                       r"|\bNR[\s-]?0?(12|15|16|17|35|36|1|6|7)\s*,?\s*(?:em\s+seu\s+)?Anexo\s+(?:n[º°.]?\s*)?(\d+(?:-A)?|[IVX]+)\b", re.I)
# 16/10: STF — Súmula Vinculante ("Súmula Vinculante nº 4", "Súmulas Vinculantes 15 e 16") e tema de repercussão geral
# ("Tema 932 do STF", "Tema 1.046 do Supremo", "Tema 725 da repercussão geral", "Tema 725/STF")
_SV = re.compile(r"\bS[úu]mulas?\s+Vinculantes?\s+(?:n[º°.]*s?\s*)?(\d+(?:\s*(?:,|e)\s*\d+)*)", re.I)
_TEMA_STF = re.compile(r"\bTema\s+(?:n[º°.]*\s*)?(\d{1,2}(?:\.\d{3})+|\d+)(?=\s*,?\s*\(?\s*(?:/\s*|d[ao]\s+|de\s+)?"
                       r"(?:STF\b|Supremo\b|Repercuss[ãa]o\s+Geral\b))", re.I)
# 07/10: temas repetitivos do TST ("Tema 125 do TST", "Tema de IRR n.º 23", "IRR Tema 70", "Tema 39 da Tabela de Incidente de
# Recurso de Revista Repetitivo"). "Tema 1.046 do STF" não casa: exige TST/IRR/recurso de revista repetitivo junto.
_TEMA_TST = re.compile(r"\bTema\s+(?:n[º°.]*\s*)?(\d+)(?=\s*,?\s*\(?\s*(?:d[ao]\s+)?(?:TST\b|IRR\b|Tabela\s+de\s+Incidentes?\s+de\s+Recursos?\s+de\s+Revista"
                       r"|(?:Incidente\s+de\s+)?Recursos?\s+de\s+Revista\s+Repetitivos?))"
                       r"|\b(?:IRR\s*[-–]?\s*Tema|Tema\s+de\s+IRR)\s+(?:n[º°.]*\s*)?(\d+)", re.I)
_ROMANO = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X", 11: "XI", 12: "XII"}
# 06/10: pergunta de periculosidade/insalubridade raramente cita a NR ("troca o cilindro de GLP…"): o tema aponta o anexo.
# ponytail: lista fixa dos anexos que mais aparecem nos casos do escritório; tema novo entra aqui.
_ADICIONAL = re.compile(r"(?i)periculos|perigos|insalubr")
_TEMAS_NR = (
    (r"\bGLP\b|g[áa]s\s+liquefeito|inflam[áa]ve|combust[íi]ve|abastec|tanque\s+de\s+(?:combust|[óo]leo)", "NR-16 Anexo II"),
    (r"eletricidade|energia\s+el[ée]trica|eletricista|alta\s+tens[ãa]o", "NR-16 Anexo IV"),
    (r"motocicl|motoboy|motoneta", "NR-16 Anexo V"),
    (r"vigilante|seguran[çc]a\s+(?:patrimonial|pessoal)|roubo", "NR-16 Anexo III"),
    (r"explosiv", "NR-16 Anexo I"),
    (r"ru[íi]do", "NR-15 Anexo 1"),
    (r"\bcalor\b|temperatura\s+elevada", "NR-15 Anexo 3"),
    (r"\bfrio\b|c[âa]mara\s+fria|frigor[íi]fic", "NR-15 Anexo 9"),
    (r"umidade", "NR-15 Anexo 10"),
    (r"vibra[çc]", "NR-15 Anexo 8"),
    (r"poeira|s[íi]lica|amianto|asbesto", "NR-15 Anexo 12"),
    (r"benzeno", "NR-15 Anexo 13-A"),
    (r"hidrocarbonet|[óo]leo\s+mineral|graxa|agentes?\s+qu[íi]mic|fumos?\s+met[áa]lic|solda", "NR-15 Anexo 13"),
    (r"agentes?\s+biol[óo]gic|lixo\s+urbano|hospital|esgoto|limpeza\s+de\s+banheir", "NR-15 Anexo 14"),
)


def normas_por_tema(texto: str) -> list[str]:
    """Anexos de NR-15/16 sugeridos pelo tema de uma pergunta sobre adicional (insalubridade/periculosidade)."""
    if not _ADICIONAL.search(texto or ""):
        return []
    return [chave for rx, chave in _TEMAS_NR if re.search(rx, texto, re.I)]
_OJ = re.compile(r"\b(?:OJs?|Orienta[çc](?:[ãa]o|[õo]es)\s+Jurisprudencia(?:l|is))\s*[-\s]?(?:(?:n\.?[º°]?\.?\s*)?(\d+)\s*(?:,?\s*d[ao]\s+)?(?:Colenda\s+)?(SBDI|SDI)\s*-?\s*(1|I|2|II)\b(\s*Transit[óo]ria)?"
                 r"|(SDI1T|SDI1|SDI2|SDC)-(\d+))", re.IGNORECASE)


def citacoes_jurisprudencia(texto: str) -> list[str]:
    """Chaves no formato dos enunciados da base ("TST Súmula 338", "TST OJ SBDI-1 394", "STJ Súmula 7")."""
    # 07/10: rajada de espaços (texto colado de PDF na pergunta) fazia as regex com \s*,?\s*\(?\s* explodirem
    # ("Tema 1" + 400 espaços = 2,6 s; 800 = 35 s). Nenhuma delas depende de quebra de linha.
    texto = re.sub(r"\s+", " ", texto or "")
    vistos: dict[str, None] = {}
    for m in _SUMULA.finditer(texto or ""):
        for n in re.findall(r"(?<![,\s][IVX])\b(\d+)\b", re.sub(r",\s*(?:ite(?:m|ns)\s+)?[IVX]+(?:\s*(?:,|e)\s*[IVX]+)*\b", "", m.group(1))):
            vistos.setdefault(f"{'TRT12' if m.group(2).upper().startswith('TRT') else m.group(2)} Súmula {n}", None)
    for m in _SUMULA_ANTES.finditer(texto):  # 27/10: a própria chave ("TST Súmula 219": golden, rótulo da base)
        vistos.setdefault(f"{m.group(1)} Súmula {m.group(2)}", None)
    for m in _SV.finditer(texto):
        for n in re.findall(r"\d+", m.group(1)):
            vistos.setdefault(f"STF Súmula Vinculante {n}", None)
    for m in _OJ.finditer(texto or ""):
        if m.group(1):
            sec = "SBDI-1" if m.group(3).upper() in ("1", "I") else "SBDI-2"
            vistos.setdefault(f"TST OJ {sec}{' Transitória' if m.group(4) and sec == 'SBDI-1' else ''} {m.group(1)}", None)
        else:
            sec = {"SDI1": "SBDI-1", "SDI1T": "SBDI-1 Transitória", "SDI2": "SBDI-2", "SDC": "SDC"}[m.group(5).upper()]
            vistos.setdefault(f"TST OJ {sec} {m.group(6)}", None)
    for m in _TESE_TRT12.finditer(texto or ""):
        vistos.setdefault(f"TRT12 Tese Jurídica {m.group(1)} ({(m.group(2) or 'IRDR').upper()})", None)
    for m in _TEMA_TST.finditer(texto or ""):
        vistos.setdefault(f"TST Tema IRR {m.group(1) or m.group(2)}", None)
    for m in _TEMA_STF.finditer(texto):
        vistos.setdefault(f"STF Tema {m.group(1).replace('.', '')}", None)
    for m in _NR_ANEXO.finditer(texto or ""):
        num, nr = (m.group(1), m.group(2)) if m.group(1) else (m.group(4), m.group(3))
        num = num.upper()
        if nr != "15" and num.isdigit():   # as outras NRs numeram em romano, a NR-15 em arábico
            num = _ROMANO.get(int(num), num)
        elif nr == "15" and num in _ROMANO.values():
            num = str(next(k for k, v in _ROMANO.items() if v == num))
        vistos.setdefault(f"NR-{nr} Anexo {num}", None)
    return list(vistos)
