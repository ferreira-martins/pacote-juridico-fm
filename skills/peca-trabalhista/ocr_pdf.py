#!/usr/bin/env python3
"""Wrapper Python para OCR de PDFs escaneados (TRCT, ASOs, INSS, contratos, etc.).

Usa a Vision API nativa do macOS (sem dependências externas — não precisa
brew, tesseract ou pip extra). Suporta português nativamente.

Recursos:
- OCR de arquivo único (.pdf, .png, .jpg)
- OCR de pasta inteira (todos os PDFs/imagens dentro)
- OCR de zip (extrai e processa)
- Cache automático: o resultado é salvo em arquivo .txt ao lado do original
  (se já existir e for mais novo, reutiliza)

Uso:
  python3 ocr_pdf.py arquivo.pdf
  python3 ocr_pdf.py pasta/
  python3 ocr_pdf.py arquivo.zip
  python3 ocr_pdf.py arquivo.pdf --fast        # mais rápido, menos preciso
  python3 ocr_pdf.py arquivo.pdf --lang pt-BR,en-US
  python3 ocr_pdf.py arquivo.pdf --out resultado.txt
  python3 ocr_pdf.py arquivo.pdf --no-cache    # força re-OCR
"""

import argparse
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

SKILL_DIR = Path(__file__).parent
SWIFT_SCRIPT = SKILL_DIR / "ocr_pdf.swift"

SUPPORTED_PDF = {".pdf"}
SUPPORTED_IMG = {".png", ".jpg", ".jpeg", ".tiff", ".tif", ".bmp", ".heic"}
SUPPORTED = SUPPORTED_PDF | SUPPORTED_IMG


def cache_path(src: Path) -> Path:
    return src.with_suffix(src.suffix + ".ocr.txt")


def is_cache_fresh(src: Path) -> bool:
    cache = cache_path(src)
    return cache.exists() and cache.stat().st_mtime >= src.stat().st_mtime


def ocr_one(src: Path, langs: str, fast: bool, use_cache: bool) -> str:
    if use_cache and is_cache_fresh(src):
        return cache_path(src).read_text(encoding="utf-8")

    cmd = ["swift", str(SWIFT_SCRIPT), str(src), "--lang", langs]
    if fast:
        cmd.append("--fast")

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        sys.stderr.write(f"[{src.name}] erro Swift/Vision:\n{res.stderr}\n")
        return ""
    text = res.stdout
    if use_cache:
        cache_path(src).write_text(text, encoding="utf-8")
    return text


def collect_files(target: Path) -> list[Path]:
    if target.is_file():
        if target.suffix.lower() == ".zip":
            tmpdir = Path(tempfile.mkdtemp(prefix="ocr_zip_"))
            with zipfile.ZipFile(target) as z:
                for info in z.infolist():
                    try:
                        name = info.filename.encode("cp437").decode("utf-8")
                    except Exception:
                        name = info.filename
                    outp = tmpdir / name
                    outp.parent.mkdir(parents=True, exist_ok=True)
                    with open(outp, "wb") as f:
                        f.write(z.read(info))
            return [
                p for p in tmpdir.rglob("*")
                if p.is_file() and p.suffix.lower() in SUPPORTED
            ]
        return [target] if target.suffix.lower() in SUPPORTED else []

    return [
        p for p in target.rglob("*")
        if p.is_file() and p.suffix.lower() in SUPPORTED
    ]


def main():
    ap = argparse.ArgumentParser(description="OCR de PDFs/imagens via Vision API (macOS).")
    ap.add_argument("target", help="Arquivo (.pdf/.png/.jpg/.zip) ou pasta.")
    ap.add_argument("--lang", default="pt-BR,en-US", help="Idiomas (default: pt-BR,en-US).")
    ap.add_argument("--fast", action="store_true", help="Modo rápido (menos preciso).")
    ap.add_argument("--no-cache", action="store_true", help="Força re-OCR ignorando cache .ocr.txt.")
    ap.add_argument("--out", help="Arquivo de saída (default: stdout).")
    ap.add_argument("--quiet", action="store_true", help="Não imprime cabeçalhos.")
    args = ap.parse_args()

    target = Path(args.target).expanduser().resolve()
    if not target.exists():
        sys.exit(f"Não encontrado: {target}")

    files = collect_files(target)
    if not files:
        sys.exit(f"Nenhum arquivo suportado em: {target}")

    chunks: list[str] = []
    for f in sorted(files):
        if not args.quiet:
            chunks.append(f"\n========== {f.name} ==========\n")
        chunks.append(ocr_one(f, args.lang, args.fast, use_cache=not args.no_cache))

    out_text = "".join(chunks)
    if args.out:
        Path(args.out).expanduser().write_text(out_text, encoding="utf-8")
        if not args.quiet:
            print(f"OK -> {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(out_text)


if __name__ == "__main__":
    main()
