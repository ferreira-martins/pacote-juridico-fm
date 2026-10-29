"""Investigação dos autos antes da resposta: ousada para levantar, conservadora para afirmar.

1. O modelo lê os autos e devolve JSON: fatos (cada um com o trecho LITERAL e a peça), contradições,
   o que deveria existir e não está nos autos, hipóteses e se a tese se sustenta.
2. O código confere cada trecho na peça indicada (sem IA). Trecho que não existe = fato não provado.
3. A resposta recebe só os fatos conferidos como fato; o resto vai como hipótese ou lacuna.
"""
from __future__ import annotations

import json
import re
from bisect import bisect_right
import unicodedata
from functools import lru_cache

INSTRUCAO = """Você é o investigador do caso: leia os autos (DOCUMENTOS DESTA EXECUÇÃO) procurando minúcias.
Levante hipóteses com ousadia, mas não afirme nada sem o trecho que prova. Compare peças entre si
(inicial × contestação × documentos × ata × laudo): datas, valores, funções, jornadas, versões que mudam.
Sua função não é defender uma conclusão escolhida: aponte também o que é desfavorável ao cliente.

Responda SÓ com um JSON, sem texto fora dele, neste formato:
{"fatos": [{"afirmacao": "...", "documento": "nome exato da peça", "trecho": "cópia literal de até 300 caracteres"}],
 "contradicoes": [{"descricao": "...", "trechos": [{"documento": "...", "trecho": "..."}]}],
 "ausencias": [{"item": "o que deveria estar nos autos e não está", "por_que_importa": "..."}],
 "hipoteses": [{"descricao": "possibilidade a investigar", "como_verificar": "..."}],
 "avaliacao": "a documentação sustenta ou não a tese pedida, e por quê (inclusive contra o cliente)"}
Regras: "trecho" é cópia EXATA do documento (sem resumir, sem corrigir); "documento" é o nome como
aparece em [Fonte Documento: nome]. Sem trecho literal, não é fato: vira hipótese ou ausência.
Tamanho: no máximo 20 fatos, 8 contradições, 8 ausências e 6 hipóteses — os que mais pesam no pedido."""
# 07/10 (conversa 73): sem teto, o JSON passava de uma chamada, o provedor emendava continuações (~5 min) e a emenda
# quebrava o JSON ("investigação sem JSON válido") — a investigação custava 5 min e não entregava nada.


def _norm(texto: str) -> str:
    t = unicodedata.normalize("NFKC", texto or "").casefold()
    t = t.replace("“", '"').replace("”", '"').replace("’", "'").replace("–", "-").replace("—", "-")
    t = re.sub(r"-\s*\n\s*", "", t)  # hifenização de quebra de linha
    return " ".join(t.split())


def ler_json(texto: str) -> dict | None:
    """O modelo às vezes cerca o JSON com texto ou ```; pega do 1º { ao último }."""
    inicio, fim = (texto or "").find("{"), (texto or "").rfind("}")
    if inicio < 0 or fim <= inicio:
        return None
    try:
        dados = json.loads(texto[inicio : fim + 1])
    except json.JSONDecodeError:
        return None
    return dados if isinstance(dados, dict) else None


def conferir_trecho(documento: str, trecho: str, documentos: dict[str, str]) -> str | None:
    """Nome da peça onde o trecho existe literalmente (a indicada primeiro); None se não existe."""
    alvo = _norm(trecho)
    if len(alvo) < 12:  # trecho curto demais ("sim", uma data solta) prova qualquer coisa
        return None
    # 26/10 (caso grande, 24 PDFs: varredura de 5–6 min com as 167 janelas no cache): cada passo da busca binária de cada item
    # percorria as peças uma a uma. Agora o trecho é procurado uma vez no texto único dos autos e a peça sai da posição
    # (a 1ª ocorrência na ordem das peças, como antes); a indicada pelo extrator continua tendo preferência.
    nomes = list(documentos)
    corpus, inicios = _corpus(tuple(documentos.values()))
    doc = _norm_doc(documento)
    indicado = next((nome for nome in nomes if _norm_doc(nome) == doc), None)
    if indicado is not None and alvo in _norm_doc(documentos[indicado]):
        return indicado
    pos = corpus.find(alvo)
    return nomes[bisect_right(inicios, pos) - 1] if pos >= 0 else None


@lru_cache(maxsize=4096)  # 26/10: 512 < peças do caso grande (24 PDFs): o cache girava e normalizava tudo de novo
def _norm_doc(texto: str) -> str:
    """16/10: a peça era normalizada de novo a cada item conferido (centenas de itens × 80 peças por execução)."""
    return _norm(texto)


SEPARADOR = "\n\x00\n"  # nenhum trecho normalizado o contém: não há achado atravessando duas peças


@lru_cache(maxsize=8)
def _corpus(textos: tuple[str, ...]) -> tuple[str, list[int]]:
    """Os autos normalizados num texto só + onde começa cada peça."""
    partes, inicios, pos = [], [], 0
    for t in textos:
        n = _norm_doc(t)
        inicios.append(pos)
        partes.append(n)
        pos += len(n) + len(SEPARADOR)
    return SEPARADOR.join(partes), inicios


RETICENCIAS_RE = re.compile(r"^\s*(?:\.{3}|…)\s*|\s*(?:\.{3}|…)\s*$")
TRECHO_LITERAL_MIN = 60


def conferir_literal(documento: str, trecho: str, documentos: dict[str, str]) -> tuple[str | None, str]:
    """(peça, trecho conferido). 16/10 (conversa 85): o Nova Micro fecha o trecho com "..." ou junta um número que a
    peça quebra em dois — 43 de 89 itens de prova descartados assim, entre eles o atestado de 2 dias que decide a
    estabilidade. Reticências nas pontas saem; se o trecho não confere inteiro, vale o maior começo literal com pelo
    menos TRECHO_LITERAL_MIN caracteres, e o trecho devolvido é só esse começo (nunca texto que não está na peça)."""
    trecho = RETICENCIAS_RE.sub("", trecho or "")
    if (onde := conferir_trecho(documento, trecho, documentos)):
        return onde, trecho
    palavras = trecho.split()
    # 26/10 (caso grande, autos de ~5 milhões de caracteres): cada passo da busca binária percorre os autos inteiros. O menor
    # começo aceitável vem antes: se nem ele é literal, nenhum maior é (monotônico) — 1 varredura em vez de ~10 — e,
    # se é, a busca começa dele.
    minimo = next((k for k in range(1, len(palavras)) if len(_norm(" ".join(palavras[:k]))) >= TRECHO_LITERAL_MIN), None)
    if minimo is None or not conferir_trecho(documento, " ".join(palavras[:minimo]), documentos):
        return None, trecho
    baixo, alto = minimo, len(palavras) - 1  # maior k com palavras[:k] literal (prefixo literal é monotônico)
    while baixo < alto:
        meio = (baixo + alto + 1) // 2
        if conferir_trecho(documento, " ".join(palavras[:meio]), documentos):
            baixo = meio
        else:
            alto = meio - 1
    prefixo = " ".join(palavras[:baixo])
    if len(_norm(prefixo)) < TRECHO_LITERAL_MIN:
        return None, trecho
    return conferir_trecho(documento, prefixo, documentos), prefixo


def validar(achados: dict, documentos: dict[str, str]) -> dict:
    """Separa o que o código conseguiu provar do que ficou só na palavra do modelo."""
    fatos, sem_prova = [], []
    for fato in achados.get("fatos") or []:
        if not isinstance(fato, dict):
            continue
        onde = conferir_trecho(str(fato.get("documento", "")), str(fato.get("trecho", "")), documentos)
        (fatos if onde else sem_prova).append({**fato, "documento": onde or fato.get("documento", "")})
    contradicoes = []
    for item in achados.get("contradicoes") or []:
        if not isinstance(item, dict):
            continue
        trechos = [
            {"documento": onde, "trecho": t.get("trecho", "")}
            for t in item.get("trechos") or [] if isinstance(t, dict)
            if (onde := conferir_trecho(str(t.get("documento", "")), str(t.get("trecho", "")), documentos))
        ]
        if len(trechos) >= 2:  # contradição precisa dos dois lados provados
            contradicoes.append({"descricao": item.get("descricao", ""), "trechos": trechos})
    return {
        "fatos": fatos,
        "sem_prova": sem_prova,
        "contradicoes": contradicoes,
        "ausencias": [a for a in achados.get("ausencias") or [] if isinstance(a, dict)],
        "hipoteses": [h for h in achados.get("hipoteses") or [] if isinstance(h, dict)],
        "avaliacao": str(achados.get("avaliacao") or "").strip(),
    }


def bloco(validado: dict) -> str:
    """Contexto da resposta. Os trechos conferidos citam a peça; o resto não é citável como fato."""
    linhas = ["INVESTIGAÇÃO PRÉVIA DOS AUTOS (cada trecho abaixo foi conferido literalmente pelo sistema):"]
    if validado["fatos"]:
        linhas.append("FATOS CONFERIDOS (use como fato, citando a peça):")
        linhas += [f'- {f.get("afirmacao", "")} [Fonte Documento: {f["documento"]}] — "{f.get("trecho", "")}"'
                   for f in validado["fatos"]]
    if validado.get("leituras_erradas"):
        linhas.append("LEITURAS NÃO SUSTENTADAS (o trecho existe, mas NÃO diz o que a leitura afirma): use o trecho "
                      "literal, não a leitura; aponte ao advogado se a inicial ou uma etapa anterior afirma a leitura:")
        linhas += [f'- Leitura descartada: {f.get("afirmacao", "")} — o trecho diz: "{f.get("trecho", "")}" '
                   f'[Fonte Documento: {f["documento"]}]' for f in validado["leituras_erradas"]]
    if validado["contradicoes"]:
        linhas.append("CONTRADIÇÕES ENTRE PEÇAS (os dois lados conferidos):")
        for c in validado["contradicoes"]:
            lados = "; ".join(f'"{t["trecho"]}" [Fonte Documento: {t["documento"]}]' for t in c["trechos"])
            linhas.append(f"- {c['descricao']}: {lados}")
    if validado["sem_prova"]:
        linhas.append("NÃO CONFERIDOS (o trecho não existe nos autos): NÃO afirme como fato; trate como ponto a confirmar:")
        linhas += [f"- {f.get('afirmacao', '')}" for f in validado["sem_prova"]]
    if validado["ausencias"]:
        linhas.append("O QUE DEVERIA ESTAR NOS AUTOS E NÃO ESTÁ:")
        linhas += [f"- {a.get('item', '')}: {a.get('por_que_importa', '')}" for a in validado["ausencias"]]
    if validado["hipoteses"]:
        linhas.append("HIPÓTESES A INVESTIGAR (não são fatos):")
        linhas += [f"- {h.get('descricao', '')} (verificar: {h.get('como_verificar', '')})" for h in validado["hipoteses"]]
    if validado["avaliacao"]:
        linhas.append(f"AVALIAÇÃO DO INVESTIGADOR (opinião, não fato): {validado['avaliacao']}")
    linhas.append(
        # 30/09: não escrever marcador genérico aqui ("[Fonte N]"): o modelo copiava literalmente (21 citações inválidas no A/B)
        "Na resposta: fato só dos FATOS CONFERIDOS ou de trecho que você mesmo cite da peça. Esta "
        "investigação é apoio, não substitui a citação: NA MINUTA, cada frase ou parágrafo que afirma "
        "fato termina com a citação da peça de onde ele vem (igual às dos FATOS CONFERIDOS acima), e "
        "cada fundamento com o número real do trecho da BASE DE CONHECIMENTO que o traz (por exemplo, "
        "[Fonte 3] se o trecho 3 for o que sustenta), mesmo que o fato já apareça acima. Não gaste a "
        "resposta repetindo trechos: vá à peça. Traga as contradições, o que falta nos autos e as "
        "hipóteses como tais, e diga com franqueza se a documentação sustenta a tese."
    )
    return "\n".join(linhas)
