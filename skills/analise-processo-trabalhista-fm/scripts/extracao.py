"""Extração estruturada do contrato v1 (docs/contrato): o modelo propõe valor + documento + trecho; o CÓDIGO confere.

Valor só volta preenchido quando (1) o trecho existe literalmente no documento (investigacao.conferir_trecho) e
(2) o valor está dentro do trecho (data, número, texto). Sem isso: valor null + motivo — nunca um valor plausível.
07/10: pedido do Davi (JSON de entrada e saída padrão para integração).
"""
from __future__ import annotations

import json
import logging
import re

from calculos import datas_no_texto, ler_data
from investigacao import _norm, conferir_trecho, ler_json
chamar = None  # pacote: extrair_autos.py faz a chamada ao modelo

logger = logging.getLogger(__name__)

MATERIAL_MAX = 300_000  # ponytail: cabe numa chamada; autos maiores pedem extração por peça
FORMATO_TIPO = {
    "texto": "texto como está escrito",
    "data": "DD/MM/AAAA",
    "numero": "número como está escrito (ex.: 44 ou 1.234,5)",
    "moeda": "valor como está escrito (ex.: 154.394,38)",
    "booleano": "true ou false",
    "cnj": "número CNJ completo",
    "cpf_cnpj": "como está escrito",
    "lista_texto": "lista de textos, cada item como está escrito",
    "opcao": "uma das opções, exatamente como listada",
}
MARCA_RE = re.compile(r"\[(CONFERIR|CONFIRMAR|PREENCHER)\b[^\]\n]*\]", re.IGNORECASE)


def instrucao(campos: list, itens: bool = False) -> str:
    """`itens`: campo de lista volta item a item, cada um com o próprio documento e trecho (pipeline de duas IAs)."""
    linhas = []
    for c in campos:
        extra = f" Opções: {', '.join(c.opcoes)}." if c.tipo == "opcao" and c.opcoes else ""
        linhas.append(f'- "{c.nome}" ({FORMATO_TIPO[c.tipo]}): {c.descricao or c.nome.replace("_", " ")}.{extra}')
    formato = '{"campos": {"<nome>": {"valor": ..., "documento": "...", "trecho": "..."}}}'
    if itens:
        formato += (' — campo de LISTA: {"<nome>": {"itens": [{"valor": "...", "documento": "...", "trecho": "..."}]}}, '
                    "um item por ocorrência, cada um com o próprio documento e trecho (até 15 itens por lista)")
    return (
        "Extraia dos DOCUMENTOS os campos abaixo. Para cada campo, devolva o valor, o nome exato do documento "
        "(como em [DOCUMENTO: nome]) e o trecho: cópia LITERAL de até 300 caracteres que contém o valor (sem resumir, "
        "sem corrigir). Se o campo não estiver escrito nos documentos, devolva valor null — nunca deduza nem complete.\n"
        "Campos:\n" + "\n".join(linhas) + "\n\nResponda só JSON: " + formato
    )


def _numero(valor) -> float | None:
    if isinstance(valor, bool):
        return None
    if isinstance(valor, (int, float)):
        return float(valor)
    s = re.sub(r"[^\d,.\-]", "", str(valor or ""))
    if not re.search(r"\d", s):
        return None
    if "," in s:  # padrão brasileiro: 1.234,56
        s = s.replace(".", "").replace(",", ".")
    elif s.count(".") > 1 or re.fullmatch(r"-?\d{1,3}(\.\d{3})+", s):  # 1.234.567 / 154.394 = milhar
        s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return None


def normalizar(tipo: str, valor, opcoes: list[str]):
    """(valor no formato da saída, motivo da recusa)."""
    if valor is None or valor == "" or valor == []:
        return None, "não encontrado nos documentos"
    if tipo == "data":
        d = ler_data(valor)
        return (d.isoformat(), "") if d else (None, f"data ilegível: {valor}")
    if tipo in ("numero", "moeda"):
        n = _numero(valor)
        return (n, "") if n is not None else (None, f"número ilegível: {valor}")
    if tipo == "booleano":
        if isinstance(valor, bool):
            return valor, ""
        v = str(valor).strip().casefold()
        if v in ("true", "sim", "s", "1", "yes"):
            return True, ""
        if v in ("false", "não", "nao", "n", "0", "no"):
            return False, ""
        return None, f"booleano ilegível: {valor}"
    if tipo == "cnj":
        d = re.sub(r"\D", "", str(valor))
        if len(d) != 20:
            return None, f"CNJ inválido: {valor}"
        return f"{d[:7]}-{d[7:9]}.{d[9:13]}.{d[13]}.{d[14:16]}.{d[16:]}", ""
    if tipo == "cpf_cnpj":
        d = re.sub(r"\D", "", str(valor))
        return (str(valor).strip(), "") if len(d) in (11, 14) else (None, f"CPF/CNPJ inválido: {valor}")
    if tipo == "lista_texto":
        itens = [str(i).strip() for i in (valor if isinstance(valor, list) else [valor]) if str(i).strip()]
        return (itens, "") if itens else (None, "lista vazia")
    if tipo == "opcao":
        achada = next((o for o in opcoes if _norm(o) == _norm(str(valor))), None)
        return (achada, "") if achada else (None, f"fora das opções: {valor}")
    texto = str(valor).strip()
    return (texto, "") if texto else (None, "não encontrado nos documentos")


def valor_no_trecho(tipo: str, valor, trecho: str) -> bool:
    """O valor está mesmo no trecho? Para opção, booleano e lista basta o trecho existir (é interpretação)."""
    if tipo == "data":
        return any(d.isoformat() == valor for d in datas_no_texto(trecho))
    if tipo in ("numero", "moeda"):
        return any(_numero(m) == valor for m in re.findall(r"\d(?:[\d.,]*\d)?", trecho))  # 15/10: "R$ 2.500,00," no fim da frase
    if tipo in ("cnj", "cpf_cnpj"):
        return re.sub(r"\D", "", str(valor)) in re.sub(r"\D", "", trecho)
    if tipo == "texto":
        return _norm(str(valor)) in _norm(trecho)
    return True


def extrair(provider, campos: list, documentos: dict[str, str], modelo: str | None, usage) -> dict:
    """{"dados": {nome: {...}}, "faltando": [...]} — sempre com todos os campos pedidos."""
    material = "\n\n".join(f"[DOCUMENTO: {nome}]\n{texto}" for nome, texto in documentos.items())[:MATERIAL_MAX]
    achados: dict = {}
    if material.strip():
        try:
            bruto = chamar(provider, usage, "estruturado", instrucao(campos), material, modelo)
            achados = (ler_json(bruto) or {}).get("campos") or {}
        except Exception:  # noqa: BLE001 — falha do modelo: todos os campos voltam vazios com o motivo
            logger.exception("extração falhou")
            achados = {"__erro__": True}
    dados = {}
    for c in campos:
        item = achados.get(c.nome) if isinstance(achados.get(c.nome), dict) else {}
        valor, motivo = normalizar(c.tipo, item.get("valor"), c.opcoes)
        if "__erro__" in achados:
            motivo = "a extração falhou nesta execução; tente de novo"
        elif not documentos:
            motivo = "nenhum documento enviado"
        trecho = str(item.get("trecho") or "")[:600]
        onde = conferir_trecho(str(item.get("documento") or ""), trecho, documentos) if valor is not None else None
        conferido = bool(onde) and valor_no_trecho(c.tipo, valor, trecho)
        if valor is not None and not conferido and c.exigir_trecho:
            motivo = "o trecho citado não está no documento" if not onde else "o valor não está no trecho citado"
            valor = None
        dados[c.nome] = {"valor": valor, "conferido": conferido, "documento": onde, "trecho": trecho if onde else None,
                         **({"motivo": motivo} if valor is None else {})}
    faltando = [c.nome for c in campos if c.obrigatorio and dados[c.nome]["valor"] is None]
    logger.info("extração: %d campos, %d conferidos, faltando %s", len(campos),
                sum(d["conferido"] for d in dados.values()), json.dumps(faltando, ensure_ascii=False))
    return {"dados": dados, "faltando": faltando}


def marcas(texto: str) -> list[dict]:
    """Pendências do texto ([CONFERIR…], [CONFIRMAR…], [PREENCHER…]) com a linha onde estão."""
    return [{"tipo": m.group(1).upper(), "texto": m.group(0), "linha": n}
            for n, linha in enumerate((texto or "").split("\n"), start=1) for m in MARCA_RE.finditer(linha)]
