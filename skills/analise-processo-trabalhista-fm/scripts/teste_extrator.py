"""Autoteste sem rede: o modelo falso acerta um campo, inventa outro e erra o trecho de um terceiro."""
import json
from types import SimpleNamespace as C
from extrair_autos import extrair

docs = {"inicial.txt": "[Pagina 1]\nRECLAMANTE admitido em 03/02/2021 na função de soldador.\n[Pagina 2]\n"
                      "Foi dispensado sem justa causa em 10/05/2023, último salário de R$ 2.500,00."}
campos = [C(nome="data_admissao", tipo="data", descricao="", opcoes=[]),
          C(nome="salario", tipo="moeda", descricao="", opcoes=[]),
          C(nome="funcao", tipo="texto", descricao="", opcoes=[])]
falso = {"campos": {
    "data_admissao": {"valor": "03/02/2021", "documento": "inicial.txt", "trecho": "RECLAMANTE admitido em 03/02/2021 na função"},
    "salario": {"valor": "3.100,00", "documento": "inicial.txt", "trecho": "último salário de R$ 2.500,00"},  # valor fora do trecho
    "funcao": {"valor": "soldador", "documento": "inicial.txt", "trecho": "exercia a função de soldador líder"},  # trecho inventado
}}
r = extrair(docs, campos, lambda s, c: (json.dumps(falso), {"entrada": 1, "saida": 1}))
assert r["dados"]["data_admissao"]["valor"] == "2021-02-03", r
assert r["dados"]["data_admissao"]["fonte"] == "[Fonte Documento: inicial.txt › p. 1]", r
assert "salario" not in r["dados"] and "funcao" not in r["dados"] and r["descartados"] == 2, r
print("ok", json.dumps(r["dados"], ensure_ascii=False))
