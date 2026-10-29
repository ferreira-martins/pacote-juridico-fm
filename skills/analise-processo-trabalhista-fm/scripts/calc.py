"""Cálculos determinísticos do IA_JUR (calculos.py, copiado pelo montar.py) pela linha de comando.

  python calc.py prescricao extincao=10/05/2023 ajuizamento=02/04/2025 admissao=03/02/2018 [projecao=09/06/2023]
  python calc.py aviso_previo admissao=03/02/2018 desligamento=10/05/2023
  python calc.py avos admissao=03/02/2018 desligamento=10/05/2023
  python calc.py prazo_contrato inicio=22/09/2025 dias=45 prorrogacao_dias=45 experiencia=true [rescisao=..]
  python calc.py prazo_processual disponibilizacao=13/11/2025 dias=8 [corridos=false] [pessoal=true]

Feriados: só nacionais + Carnaval/Sexta-feira Santa/Corpus Christi. Feriado local/forense e recesso: conferir à parte.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from calculos import CALCULOS, ler_data  # noqa: E402


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 2 or sys.argv[1] not in CALCULOS:
        sys.exit(__doc__ + f"\nCálculos: {', '.join(CALCULOS)}")
    funcao, tipos = CALCULOS[sys.argv[1]]
    tipos = {**tipos, "pessoal": "bool"}
    args = {}
    for par in sys.argv[2:]:
        nome, _, valor = par.partition("=")
        if nome not in tipos:
            sys.exit(f"parâmetro desconhecido: {nome} (aceitos: {', '.join(tipos)})")
        if tipos[nome] == "data":
            args[nome] = ler_data(valor) or sys.exit(f"data ilegível: {valor}")
        elif tipos[nome] == "int":
            args[nome] = int(valor)
        else:
            args[nome] = valor.strip().casefold() in ("true", "sim", "s", "1")
    print(json.dumps(funcao(**args), ensure_ascii=False, indent=1, default=str))


if __name__ == "__main__":
    main()
