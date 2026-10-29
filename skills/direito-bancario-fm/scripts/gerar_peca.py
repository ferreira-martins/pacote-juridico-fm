#!/usr/bin/env python3
"""
Gerador de peca bancaria em .docx no padrao Ferreira & Martins.
Recebe um JSON com o conteudo JA REDIGIDO pelo agente e aplica a formatacao FM,
fiel aos modelos do escritorio.

Formatacao FM (POP-JUR-007 v1.1 - padrao oficial do escritorio):
  - Fonte Bookman Old Style; alinhamento justificado; espacamento 1,5 no corpo.
  - Texto corrido: tamanho 12, recuo de 1a linha 1,25 cm, entrelinhas 1,5.
  - Qualificacao inicial das partes (preambulo): Bookman 12 justificado, SEM
    recuo de primeira linha (excecao do item 6.1.3.b do POP).
  - Citacoes diretas longas: tamanho 11, recuo do bloco 2,5 cm em todo o texto,
    entrelinhas simples (1,0), com separacao visual antes/depois.
  - Margens: superior 4,5 / inferior 2,25 / esquerda 3,0 / direita 3,0 cm
    (o POP-JUR-007 nao trata de margens; mantidas do modelo FM).
  - Termos em latim em italico (automatico).
  - Numeros de processo no padrao CNJ.

Uso:
  python3 gerar_peca.py dados.json
  python3 gerar_peca.py -                      # le o JSON do stdin
  python3 gerar_peca.py dados.json --out "/caminho/Peca.docx"

Esquema do JSON - ver exemplo ao final deste cabecalho. Campos de cada secao:
  "secoes": [
    {"titulo": "I - SINTESE FATICA", "paragrafos": ["...", {"citacao": "Ementa..."}]}
  ]
Um item de paragrafo pode ser uma string (paragrafo normal) ou
{"citacao": "texto"} para transcricao recuada em fonte 11.
"""
import sys, json, os, re
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX

# 29/10: logo/rodapé vêm na própria skill (antes: caminho do Mac do Dr. Clênio — no Windows a peça saía sem timbre)
TPL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates")
LOGO = os.path.join(TPL, "logo_FM.png")
RODAPE = os.path.join(TPL, "rodape_FM.png")
FONTE = "Bookman Old Style"

# Termos latinos a italicizar automaticamente (palavra/expressao inteira, sem acento no padrao).
LATIM = [
    "pacta sunt servanda", "bis in idem", "data maxima venia", "maxima venia",
    "data venia", "in casu", "in verbis", "ipsis litteris", "ex vi", "caput",
    "a quo", "ad quem", "habeas corpus", "mutatis mutandis", "ad cautelam",
    "ex officio", "de cujus", "inaudita altera parte", "periculum in mora",
    "fumus boni iuris", "onus probandi", "sine qua non", "ultra petita",
    "extra petita", "citra petita", "erga omnes", "inter partes", "ex tunc",
    "ex nunc", "exceptio", "in dubio pro reo", "quantum debeatur",
    "quantum", "et al", "ad judicia et extra", "ad judicia", "ad argumentandum",
    "venire contra factum proprium", "supressio", "in limine", "ab initio",
]
# ordenar por tamanho desc para casar expressoes compostas antes de palavras isoladas
LATIM.sort(key=len, reverse=True)
_LAT_RE = re.compile(r"(?<![\wÀ-ú])(" + "|".join(re.escape(t) for t in LATIM) + r")(?![\wÀ-ú])", re.IGNORECASE)
# ==texto== -> realce amarelo (ponto de atencao ao revisor, padrao FM)
_HL_RE = re.compile(r"==(.+?)==", re.S)


def _add_latim(p, texto, size=None, highlight=False):
    """Adiciona um trecho ao paragrafo: termos latinos em italico; opcional realce amarelo."""
    def style(r):
        if size: r.font.size = Pt(size)
        if highlight: r.font.highlight_color = WD_COLOR_INDEX.YELLOW
    pos = 0
    for m in _LAT_RE.finditer(texto):
        if m.start() > pos:
            style(p.add_run(texto[pos:m.start()]))
        ri = p.add_run(m.group(0)); ri.italic = True; style(ri)
        pos = m.end()
    if pos < len(texto):
        style(p.add_run(texto[pos:]))


def add_runs_italico(p, texto, size=None):
    """Runs do paragrafo: `==texto==` vira realce AMARELO (ponto de atencao ao revisor);
    termos latinos em italico."""
    pos = 0
    for m in _HL_RE.finditer(texto):
        if m.start() > pos:
            _add_latim(p, texto[pos:m.start()], size, highlight=False)
        _add_latim(p, m.group(1), size, highlight=True)
        pos = m.end()
    if pos < len(texto):
        _add_latim(p, texto[pos:], size, highlight=False)


def build(d):
    doc = Document()
    st = doc.styles['Normal']
    st.font.name = FONTE; st.font.size = Pt(12)
    st.paragraph_format.line_spacing = 1.5
    sec = doc.sections[0]
    sec.top_margin = Cm(4.5); sec.bottom_margin = Cm(2.25)
    sec.left_margin = Cm(3.0); sec.right_margin = Cm(3.0)
    sec.header_distance = Cm(1.71); sec.footer_distance = Cm(1.25)

    if d.get("com_timbre", True):
        hp = sec.header.paragraphs[0]; hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if os.path.exists(LOGO): hp.add_run().add_picture(LOGO, width=Cm(5.5))
        fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if os.path.exists(RODAPE): fp.add_run().add_picture(RODAPE, width=Cm(15.5))

    def base(p, align=WD_ALIGN_PARAGRAPH.JUSTIFY, first=0.0, left=0.0, sb=0, sa=0, ls=1.5):
        p.alignment = align
        pf = p.paragraph_format
        pf.line_spacing = ls
        if first: pf.first_line_indent = Cm(first)
        if left: pf.left_indent = Cm(left)
        pf.space_before = Pt(sb); pf.space_after = Pt(sa)
        return p

    def titulo(text):
        p = doc.add_paragraph(); base(p, sa=6)
        r = p.add_run(text.upper()); r.bold = True
        return p

    def corpo(text, first=1.25):
        p = doc.add_paragraph(); base(p, first=first)
        add_runs_italico(p, text)
        return p

    def citacao(text):
        # Ementas, jurisprudencia, doutrina e artigos transcritos: recuo esquerdo
        # 2,5 cm, fonte 11, espacamento SIMPLES (1,0). Texto em fonte normal;
        # apenas as expressoes em latim ficam em italico.
        p = doc.add_paragraph(); base(p, left=2.5, ls=1.0, sb=4, sa=4)
        add_runs_italico(p, text, size=11)
        return p

    def simples(text, **kw):
        p = doc.add_paragraph(); base(p, **kw)
        for ln in text.split("\n"):
            if ln is not text.split("\n")[0]:
                p.add_run().add_break()
            add_runs_italico(p, ln)
        return p

    # Enderecamento (maiusculas, negrito)
    for ln in d["enderecamento"].split("\n"):
        p = doc.add_paragraph(); base(p, sa=2)
        p.add_run(ln.upper()).bold = True
    doc.add_paragraph()

    # Distribuicao / autos (direita, negrito)
    if d.get("dependencia"):
        for ln in d["dependencia"].split("\n"):
            p = doc.add_paragraph(); base(p, align=WD_ALIGN_PARAGRAPH.RIGHT, sa=2)
            p.add_run(ln).bold = True
        doc.add_paragraph()

    # Preambulo / qualificacao inicial das partes: SEM recuo de primeira linha
    # (POP-JUR-007, item 6.1.3.b - excecao ao recuo de 1,25 cm).
    for blk in d["preambulo"].split("\n"):
        if blk.strip():
            corpo(blk, first=0.0)
    doc.add_paragraph()

    # Secoes
    for s in d.get("secoes", []):
        titulo(s["titulo"])
        for item in s.get("paragrafos", []):
            if isinstance(item, dict) and "citacao" in item:
                citacao(item["citacao"])
            else:
                corpo(item)

    # Pedidos
    if d.get("pedidos"):
        titulo(d.get("pedidos_titulo", "DOS PEDIDOS E REQUERIMENTOS"))
        if d.get("pedidos_intro"):
            corpo(d["pedidos_intro"])
        for i, ped in enumerate(d["pedidos"], 1):
            p = doc.add_paragraph(); base(p, left=1.25, sa=4)
            p.add_run(f"{i}. ").bold = True
            add_runs_italico(p, ped)

    if d.get("valor_causa"):
        doc.add_paragraph()
        corpo(f"Da-se a causa o valor de {d['valor_causa']}.")

    # Fecho
    doc.add_paragraph()
    p = doc.add_paragraph(); base(p, align=WD_ALIGN_PARAGRAPH.CENTER, sa=18)
    p.add_run(d.get("fecho", "Termos em que, pede deferimento."))
    if d.get("local_data"):
        p = doc.add_paragraph(); base(p, align=WD_ALIGN_PARAGRAPH.CENTER, sa=24)
        p.add_run(d["local_data"])

    # Assinaturas
    for a in d.get("assinaturas", []):
        for txt, bold, sa in [("_" * 40, False, 0), (a["nome"], True, 0), (a.get("oab", ""), False, 14)]:
            p = doc.add_paragraph(); base(p, align=WD_ALIGN_PARAGRAPH.CENTER, sa=sa)
            r = p.add_run(txt); r.bold = bold
    return doc


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    src = sys.argv[1]
    raw = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
    d = json.loads(raw)
    out = d.get("out")
    if "--out" in sys.argv:
        out = sys.argv[sys.argv.index("--out") + 1]
    if not out:
        nome = "Embargos a Execucao" if d.get("tipo") == "embargos" else "Acao Revisional"
        out = os.path.join(os.path.expanduser("~"), "Downloads", f"{nome} - FM.docx")
    build(d).save(out)
    print(out)


if __name__ == "__main__":
    main()
