"""Confere as citações de um texto (minuta, parecer, resposta) contra a base local — sem IA, só código.

  python conferir.py minuta.md                      # artigos, súmulas, OJs, temas, SV, teses TRT12, NR
  python conferir.py minuta.md --autos pasta_ou_pdf # + cada trecho entre aspas existe literalmente nos autos?
  python conferir.py --texto "Súmula 338 do TST e art. 818 da CLT"   # consulta rápida: imprime o teor
  python conferir.py minuta.md --json               # saída para máquina

Leitores de citação = os do IA_JUR (citacoes.py, copiado pelo montar.py). "Sem lastro local" NÃO quer dizer que a
citação é falsa: quer dizer que não está nesta base — conferir no consultar-legislacao / site oficial antes de usar.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from citacoes import artigo_canon, citacoes, citacoes_jurisprudencia  # noqa: E402
from investigacao import conferir_trecho  # noqa: E402

REFS = AQUI.parent / "references"
LEIS = {  # chave canônica do citacoes.sigla_canon → arquivo
    "CLT": "CLT-Decreto-Lei-5452-1943.txt", "Decreto-Lei 5452/1943": "CLT-Decreto-Lei-5452-1943.txt",
    "CF": "Constituicao-Federal-1988.txt", "CPC": "Codigo-de-Processo-Civil-Lei-13105-2015.txt",
    "Lei 13105/2015": "Codigo-de-Processo-Civil-Lei-13105-2015.txt", "CC": "Codigo-Civil-Lei-10406-2002.txt",
    "Lei 10406/2002": "Codigo-Civil-Lei-10406-2002.txt", "Lei 8213/1991": "Lei-de-Beneficios-da-Previdencia-Lei-8213-1991.txt",
    "Lei 6019/1974": "Trabalho-Temporario-e-Terceirizacao-Lei-6019-1974.txt", "Lei 12506/2011": "Lei-do-Aviso-Previo-Lei-12506-2011.txt",
    "Lei 605/1949": "Repouso-Semanal-Remunerado-Lei-605-1949.txt", "Lei 4090/1962": "Lei-4090-1962-13o-Salario.txt",
    "Lei 7418/1985": "Lei-7418-1985-Vale-Transporte.txt", "Lei 9029/1995": "Lei-9029-1995-Praticas-Discriminatorias-no-Trabalho.txt",
    "LC 150/2015": "LC-150-2015-Empregado-Domestico.txt", "LC 150": "LC-150-2015-Empregado-Domestico.txt",
    "Lei 5889/1973": "Lei-5889-1973-Trabalho-Rural.txt", "Lei 7783/1989": "Lei-7783-1989-Direito-de-Greve.txt",
}

def _aliases() -> dict[str, str]:
    """29/10: base inteira (126 leis do IA_JUR + extras) — alias do .meta.json ("CDC", "Lei 8245/1991") → arquivo.
    O "Lei 8245" sem ano (forma abreviada das peças) também casa."""
    mapa: dict[str, str] = {}
    for meta in (REFS / "legislacao").glob("*.txt.meta.json"):
        for a in json.loads(meta.read_text(encoding="utf-8")).get("metadados", {}).get("aliases", []):
            mapa.setdefault(a, meta.name[:-10])
            mapa.setdefault(a.split("/")[0], meta.name[:-10])
    return mapa


LEIS = {**_aliases(), **LEIS}
CABECALHO_RE = re.compile(r"^### (.+?)(?:\s+\[([^\]]+)\])?(?:\s+[—–]\s+(.*))?$")
ART_RE = re.compile(r"^\s*Art\.\s*(\d[\d.]*\s*[º°o]?(?:-[A-Z])?)(?=[\s.,;:])", re.M)  # "Art. 58 - A duração" é o 58
PN_RE = re.compile(r"\b(?:Precedentes?\s+Normativos?|PNs?)\s*(?:n\.?\s*[º°]?\s*)?(\d+)", re.I)  # o citacoes.py não lê PN
ASPAS_RE = re.compile(r"[“\"]([^”\"]{25,600})[”\"]")


@lru_cache(maxsize=1)
def enunciados() -> dict[str, dict]:
    """"TST Súmula 338" → {status, titulo, teor} de references/jurisprudencia e normas."""
    base: dict[str, dict] = {}
    for f in sorted((REFS / "jurisprudencia").glob("*.md")) + sorted((REFS / "normas").glob("*.md")):
        blocos = re.split(r"(?m)^(?=### )", f.read_text(encoding="utf-8"))
        for b in blocos:
            m = CABECALHO_RE.match(b.split("\n", 1)[0])
            if m:
                base.setdefault(m.group(1).strip(), {"status": m.group(2) or "", "titulo": (m.group(3) or "").strip(),
                                                     "teor": b.split("\n", 1)[1].strip() if "\n" in b else "", "arquivo": f.name})
    # 29/10: overlay do pacote — cancelamentos que a coleta do IA_JUR ainda traz como vigentes (Pleno TST 30/06/2025)
    over = REFS / "jurisprudencia" / "cancelamentos_tst.json"
    if over.exists():
        for chave, status in json.loads(over.read_text(encoding="utf-8"))["cancelamentos"].items():
            if chave in base:
                base[chave]["status"] = status
    return base


def _canon(numero: str) -> str:
    """29/10: o Planalto grafa "Art. 5o-C" (Lei 6.019) — o artigo_canon do IA_JUR devolvia "5o-C" e nunca casava."""
    return artigo_canon(re.sub(r"(?<=\d)\s*[oº°](?=\s*-)", "", numero))


@lru_cache(maxsize=32)
def artigos(arquivo: str) -> dict[str, list[str]]:
    texto = (REFS / "legislacao" / arquivo).read_text(encoding="utf-8")
    marcas = list(ART_RE.finditer(texto))
    saida: dict[str, list[str]] = {}
    for i, m in enumerate(marcas):
        fim = marcas[i + 1].start() if i + 1 < len(marcas) else len(texto)
        saida.setdefault(_canon(m.group(1)), []).append(texto[m.start():fim].strip())
    return saida


def conferir_artigo(chave: str) -> dict:
    diploma, _, art = chave.rpartition(" art. ")
    arquivo = LEIS.get(diploma)
    if not arquivo:
        return {"citacao": chave, "status": "SEM LASTRO LOCAL", "nota": f"{diploma} fora da base local"}
    textos = artigos(arquivo).get(_canon(art))
    if not textos:
        return {"citacao": chave, "status": "NÃO ENCONTRADO", "nota": f"art. {art} não achado em {arquivo}"}
    # 29/10: só o CAPUT conta — "Art. 206. Prescreve: § 1º … II - (Revogado …)" não é artigo revogado
    caput = [re.split(r"\s§\s*\d|\n\s*(?:[IVXL]+\s*[-–]|§)", t, maxsplit=1)[0][:300] for t in textos]
    revogado = all(re.search(r"\(\s*Revogad|\bRevogad[oa]\b", c, re.I) for c in caput)
    # ponytail: 1ª ocorrência = texto principal (CF: o ADCT vem depois); 2+ ocorrências só avisam
    return {"citacao": chave, "status": "REVOGADO?" if revogado else "OK", "teor": textos[0][:700],
            "nota": f"{len(textos)} ocorrências no arquivo (ex.: ADCT) — mostrada a 1ª" if len(textos) > 1 else ""}


def conferir_enunciado(chave: str) -> dict:
    e = enunciados().get(chave)
    if not e:
        return {"citacao": chave, "status": "SEM LASTRO LOCAL", "nota": "não está na base de enunciados"}
    cancelado = re.search(r"cancel|superad|revog", e["status"], re.I)
    return {"citacao": chave, "status": f"ATENÇÃO: {e['status']}" if cancelado else "OK",
            "titulo": e["titulo"][:200], "teor": e["teor"][:700]}


def ler_autos(caminho: Path) -> dict[str, str]:
    """Pasta ou arquivo: .txt/.md lidos como estão; .pdf com marcadores [Pagina N] (pypdf)."""
    arquivos = sorted(p for p in (caminho.rglob("*") if caminho.is_dir() else [caminho])
                      if p.suffix.lower() in (".txt", ".md", ".pdf"))
    docs = {}
    for p in arquivos:
        if p.suffix.lower() == ".pdf":
            from pypdf import PdfReader
            docs[p.name] = "\n".join(f"[Pagina {i}]\n{pg.extract_text() or ''}" for i, pg in enumerate(PdfReader(p).pages, 1))
        else:
            docs[p.name] = p.read_text(encoding="utf-8", errors="replace")
    return docs


def conferir(texto: str, autos: dict[str, str] | None = None) -> list[dict]:
    linhas = [conferir_artigo(c) for c in citacoes(texto) if " art. " in c] + [conferir_enunciado(c) for c in citacoes_jurisprudencia(texto)]
    linhas += [conferir_enunciado(f"TST PN {n}") for n in dict.fromkeys(PN_RE.findall(texto))]
    for trecho in (ASPAS_RE.findall(texto) if autos else []):
        onde = conferir_trecho("", trecho, autos)
        linhas.append({"citacao": f"“{trecho[:80]}…”" if len(trecho) > 80 else f"“{trecho}”",
                       "status": "OK" if onde else "NÃO ESTÁ NOS AUTOS", "nota": onde or "transcrição não literal"})
    return linhas


def _sem_acento(t: str) -> str:
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", t.lower()) if unicodedata.category(c) != "Mn")


def buscar(termos: str, limite: int = 15) -> list[dict]:
    """29/10: súmula/OJ/tema por ASSUNTO — todos os termos no título+teor (sem acento); vigentes primeiro.
    ponytail: varredura linear (~5 mil enunciados, <1 s); índice só se a base crescer muito."""
    palavras = [w for w in _sem_acento(termos).split() if len(w) > 2]
    achados = []
    for chave, e in enunciados().items():
        alvo = _sem_acento(chave + " " + e["titulo"] + " " + e["teor"])
        if palavras and all(w in alvo for w in palavras):
            cancelado = bool(re.search(r"cancel|superad|revog", e["status"], re.I))
            achados.append({"citacao": chave, "status": f"ATENÇÃO: {e['status']}" if cancelado else "OK",
                            "titulo": e["titulo"][:200], "teor": e["teor"][:400], "_ordem": (cancelado, len(alvo))})
    achados.sort(key=lambda a: a.pop("_ordem"))
    return achados[:limite]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivo", nargs="?", help="texto a conferir (.md/.txt); '-' = stdin")
    ap.add_argument("--texto", help="texto direto em vez de arquivo")
    ap.add_argument("--autos", type=Path, help="pasta ou arquivo dos autos para conferir as transcrições entre aspas")
    ap.add_argument("--buscar", help="achar súmula/OJ/tema por assunto (ex.: \"aviso prévio indenizado\")")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if a.buscar:
        achados = buscar(a.buscar)
        if a.json:
            print(json.dumps(achados, ensure_ascii=False, indent=1))
            return
        for l in achados:
            print(f"\n## [{l['status']}] {l['citacao']}" + (f" — {l['titulo']}" if l.get("titulo") else "") + f"\n{l['teor']}")
        print(f"\n---\n{len(achados)} enunciados com todos os termos (máx. 15). Nada? Tente menos termos ou sinônimos.")
        return
    texto = a.texto or (sys.stdin.read() if a.arquivo == "-" else Path(a.arquivo).read_text(encoding="utf-8") if a.arquivo else "")
    if not texto:
        ap.error("informe o arquivo ou --texto")
    linhas = conferir(texto, ler_autos(a.autos) if a.autos else None)
    if a.json:
        print(json.dumps(linhas, ensure_ascii=False, indent=1))
        return
    for l in linhas:
        print(f"\n## [{l['status']}] {l['citacao']}" + (f" — {l['titulo']}" if l.get("titulo") else ""))
        if l.get("nota"):
            print(f"_{l['nota']}_")
        if l.get("teor"):
            print(l["teor"])
    ruins = [l for l in linhas if l["status"] != "OK"]
    print(f"\n---\n{len(linhas)} citações; {len(linhas) - len(ruins)} OK; {len(ruins)} a conferir: "
          + "; ".join(f"{l['citacao']} ({l['status']})" for l in ruins))


if __name__ == "__main__":
    main()
