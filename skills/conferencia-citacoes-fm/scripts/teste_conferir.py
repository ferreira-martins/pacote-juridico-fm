"""Autoteste do conferir.py (sem rede): existente, cancelada, artigo inexistente, fora da base, PN, transcrição."""
from conferir import buscar, conferir

st = {l["citacao"]: l["status"] for l in conferir(
    "art. 818 da CLT; art. 1.416 do CPC; Súmula 338 do TST; Súmula 2 do TST; Súmula 9999 do TST; PN 119 do TST; "
    "art. 58 da CLT; “admitido em 03/02/2021 na função de soldador”; “admitido em 04/02/2021 na função de soldador”",
    {"inicial.txt": "O autor foi admitido em 03/02/2021 na função de soldador."})}
assert st["CLT art. 818"] == "OK" and st["CLT art. 58"] == "OK", st
assert st["CPC art. 1416"] == "NÃO ENCONTRADO", st
assert st["TST Súmula 338"] == "OK" and st["TST Súmula 2"].startswith("ATENÇÃO"), st
assert st["TST Súmula 9999"] == "SEM LASTRO LOCAL" and st["TST PN 119"] == "OK", st
assert st["“admitido em 03/02/2021 na função de soldador”"] == "OK", st
assert st["“admitido em 04/02/2021 na função de soldador”"] == "NÃO ESTÁ NOS AUTOS", st
# 29/10: base inteira (CDC, LEF, Locações sem ano) e "Art. 5o-C" do Planalto
st2 = {l["citacao"]: l["status"] for l in conferir("art. 51 do CDC; art. 16 da Lei 6.830/1980; art. 51 da Lei 8.245; "
                                                   "art. 5º-C da Lei 6.019/1974; art. 216-A do CPC")}
assert st2["CDC art. 51"] == st2["Lei 6830/1980 art. 16"] == st2["Lei 8245 art. 51"] == "OK", st2
assert st2["Lei 6019/1974 art. 5-C"] == "OK" and st2["CPC art. 216-A"] == "NÃO ENCONTRADO", st2
st3 = {l["citacao"]: l["status"] for l in conferir("Súmula 437 do TST; Súmula 331 do TST; Súmula 338 do TST")}
assert "CANCELADA" in st3["TST Súmula 437"] and "PARCIAL" in st3["TST Súmula 331"] and st3["TST Súmula 338"] == "OK", st3
assert any(b["citacao"] == "TST Súmula 377" for b in buscar("preposto empregado")), buscar("preposto empregado")
# 29/10: revogação só no CAPUT — "Art. 206. Prescreve: § 1º … II - (Revogado)" é artigo vigente
st4 = {l["citacao"]: l["status"] for l in conferir("art. 206 do CC; art. 192 do CP")}
assert st4["CC art. 206"] == "OK" and st4["CP art. 192"] == "REVOGADO?", st4
print("ok")
