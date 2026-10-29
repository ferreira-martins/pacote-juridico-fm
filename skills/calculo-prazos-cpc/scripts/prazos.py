# -*- coding: utf-8 -*-
"""
prazos.py - Motor de cálculo de prazo processual (CPC) do plugin Ferreira e Martins.

Regras implementadas:
  - Publicação = 1º dia útil seguinte à disponibilização          (CPC 224, §2)
  - Início (dies a quo) = 1º dia útil seguinte à publicação        (CPC 224, §3)
  - Contagem em DIAS ÚTEIS para prazos processuais                 (CPC 219)
  - Prorroga para o próximo dia útil se vencer sem expediente      (CPC 224, §1)
  - Suspensão de prazos de 20/12 a 20/01                           (CPC 220)
  - Feriados nacionais (fixos + móveis) + forenses (configuráveis)

AUDITORIA: toda conta devolve a lista de dias pulados, com o motivo (sábado,
domingo, nome do feriado, recesso), para o advogado conferir.

AVISO: feriados locais/suspensões variam por tribunal e ano. Confirme sempre a
portaria oficial. Veja feriados_forenses.json (copie de
references/feriados_forenses.example.json e ajuste por tribunal/ano).

Uso direto (demonstração):
  python prazos.py 2026-06-01 15                 # 15 dias úteis
  python prazos.py 2026-06-01 5 --corridos
  python prazos.py 2026-12-18 15 --tribunal TJSC
  python prazos.py 2026-06-01 15 --cfg "C:\\caminho\\feriados_forenses.json"
"""

import json
import os
import sys
from datetime import date, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UM_DIA = timedelta(days=1)


def _carregar_cfg(caminho=None):
    """Carrega feriados_forenses.json. Procura, em ordem:
    1) caminho explícito (--cfg);
    2) feriados_forenses.json ao lado deste script;
    3) ../references/feriados_forenses.example.json (fallback do plugin).
    """
    candidatos = []
    if caminho:
        candidatos.append(caminho)
    candidatos.append(os.path.join(BASE_DIR, "feriados_forenses.json"))
    candidatos.append(
        os.path.join(BASE_DIR, "..", "references", "feriados_forenses.example.json")
    )
    for c in candidatos:
        try:
            with open(c, encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            continue
    return {}


def pascoa(ano):
    """Domingo de Páscoa (algoritmo de Meeus/Butcher)."""
    a = ano % 19
    b = ano // 100
    c = ano % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mes = (h + l - 7 * m + 114) // 31
    dia = ((h + l - 7 * m + 114) % 31) + 1
    return date(ano, mes, dia)


def feriados_do_ano(ano, tribunal=None, cfg=None):
    """Dict {date: nome} com feriados nacionais + forenses para o ano."""
    cfg = cfg if cfg is not None else _carregar_cfg()
    fer = {}

    # Nacionais fixos (civis)
    fixos = {
        (1, 1): "Confraternização Universal",
        (4, 21): "Tiradentes",
        (5, 1): "Dia do Trabalho",
        (9, 7): "Independência",
        (10, 12): "Nossa Senhora Aparecida",
        (11, 2): "Finados",
        (11, 15): "Proclamação da República",
        (11, 20): "Consciência Negra",          # Lei 14.759/2023 (nacional desde 2024)
        (12, 25): "Natal",
    }
    for (mes, dia), nome in fixos.items():
        fer[date(ano, mes, dia)] = nome

    # Móveis (forenses, configuráveis)
    mov = (cfg.get("moveis_forenses") or {})
    pa = pascoa(ano)
    if mov.get("sexta_feira_santa", True):
        fer[pa - timedelta(days=2)] = "Sexta-feira Santa"
    if mov.get("carnaval_segunda_terca", True):
        fer[pa - timedelta(days=48)] = "Carnaval (segunda)"
        fer[pa - timedelta(days=47)] = "Carnaval (terça)"
    if mov.get("corpus_christi", True):
        fer[pa + timedelta(days=60)] = "Corpus Christi"

    # Forenses fixos (config)
    for mmdd, nome in (cfg.get("forense_fixos") or {}).items():
        mes, dia = (int(x) for x in mmdd.split("-"))
        fer[date(ano, mes, dia)] = nome

    # Extras gerais + por tribunal (datas ISO)
    def _add_iso(lista, rotulo):
        for s in (lista or []):
            try:
                d = date.fromisoformat(s)
                if d.year == ano:
                    fer[d] = rotulo
            except ValueError:
                pass

    _add_iso(cfg.get("feriados_extras_geral"), "Feriado (config geral)")
    if tribunal:
        por_trib = (cfg.get("feriados_por_tribunal") or {}).get(tribunal)
        _add_iso(por_trib, f"Feriado ({tribunal})")

    return fer


def em_recesso(d):
    """Suspensão de prazos de 20/12 a 20/01, inclusive (CPC 220)."""
    return (d.month == 12 and d.day >= 20) or (d.month == 1 and d.day <= 20)


def _motivo_nao_util(d, fer):
    if d.weekday() == 5:
        return "sábado"
    if d.weekday() == 6:
        return "domingo"
    if em_recesso(d):
        return "recesso/suspensão (CPC 220)"
    if d in fer:
        return fer[d]
    return None


def is_dia_util(d, fer):
    return _motivo_nao_util(d, fer) is None


def _feriados_intervalo(ini_ano, fim_ano, tribunal, cfg):
    fer = {}
    for ano in range(ini_ano, fim_ano + 1):
        fer.update(feriados_do_ano(ano, tribunal, cfg))
    return fer


def proximo_dia_util(d, fer):
    """Menor dia útil >= d."""
    while not is_dia_util(d, fer):
        d += UM_DIA
    return d


def primeiro_dia_util_seguinte(d, fer):
    """Primeiro dia útil estritamente após d."""
    return proximo_dia_util(d + UM_DIA, fer)


def calcular(disponibilizacao, dias, tipo="uteis", tribunal=None, cfg=None):
    """
    disponibilizacao: date ou 'AAAA-MM-DD'
    dias: int (tamanho do prazo)
    tipo: 'uteis' (processual, padrão) ou 'corridos'
    Retorna dict com publicacao, inicio, vencimento e a trilha de auditoria.
    """
    if isinstance(disponibilizacao, str):
        disponibilizacao = date.fromisoformat(disponibilizacao)
    cfg = cfg if cfg is not None else _carregar_cfg()
    fer = _feriados_intervalo(disponibilizacao.year, disponibilizacao.year + 2, tribunal, cfg)

    publicacao = primeiro_dia_util_seguinte(disponibilizacao, fer)
    inicio = primeiro_dia_util_seguinte(publicacao, fer)

    pulados = []  # (data, motivo) dos dias não-úteis dentro da contagem

    if tipo == "uteis":
        contados = 1            # 'inicio' já é o 1º dia útil contado
        venc = inicio
        while contados < dias:
            venc += UM_DIA
            motivo = _motivo_nao_util(venc, fer)
            if motivo:
                pulados.append((venc, motivo))
            else:
                contados += 1
    else:  # corridos
        venc = inicio + timedelta(days=dias - 1)
        # prorroga se cair em dia sem expediente (CPC 224 §1)
        while not is_dia_util(venc, fer):
            pulados.append((venc, _motivo_nao_util(venc, fer)))
            venc += UM_DIA

    return {
        "disponibilizacao": disponibilizacao,
        "publicacao": publicacao,
        "inicio": inicio,
        "vencimento": venc,
        "dias": dias,
        "tipo": tipo,
        "tribunal": tribunal,
        "dias_pulados": pulados,
    }


def descrever(resultado):
    """Texto auditável do cálculo."""
    r = resultado
    dias_para_venc = (r["vencimento"] - date.today()).days
    linhas = [
        f"Disponibilização : {r['disponibilizacao']:%d/%m/%Y} ({_dow(r['disponibilizacao'])})",
        f"Publicação       : {r['publicacao']:%d/%m/%Y} ({_dow(r['publicacao'])})  [1º dia útil seguinte]",
        f"Início da contagem: {r['inicio']:%d/%m/%Y} ({_dow(r['inicio'])})  [dies a quo]",
        f"Prazo            : {r['dias']} dias {r['tipo']}"
        + (f"  | tribunal {r['tribunal']}" if r["tribunal"] else ""),
        f">>> VENCIMENTO   : {r['vencimento']:%d/%m/%Y} ({_dow(r['vencimento'])})"
        f"   (faltam {dias_para_venc} dia(s) corridos)",
    ]
    if r["dias_pulados"]:
        linhas.append("Dias pulados na contagem:")
        for d, motivo in r["dias_pulados"]:
            linhas.append(f"   - {d:%d/%m/%Y}: {motivo}")
    return "\n".join(linhas)


_DOW = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
def _dow(d):
    return _DOW[d.weekday()]


def _main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    if len(sys.argv) < 3:
        print("Uso: python prazos.py AAAA-MM-DD DIAS [--corridos] [--tribunal SIGLA] [--cfg CAMINHO]")
        return
    disp = sys.argv[1]
    dias = int(sys.argv[2])
    tipo = "corridos" if "--corridos" in sys.argv else "uteis"
    tribunal = None
    if "--tribunal" in sys.argv:
        tribunal = sys.argv[sys.argv.index("--tribunal") + 1]
    cfg = None
    if "--cfg" in sys.argv:
        cfg = _carregar_cfg(sys.argv[sys.argv.index("--cfg") + 1])
    print(descrever(calcular(disp, dias, tipo, tribunal, cfg)))
    print("\n[AVISO] Confirme feriados locais/suspensões na portaria do tribunal. "
          "Controle de prazo é responsabilidade do escritório.")


if __name__ == "__main__":
    _main()
