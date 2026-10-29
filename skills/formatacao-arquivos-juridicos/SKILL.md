---
name: formatacao-arquivos-juridicos
description: Use para ler documentos jurídicos em PDF e DOCX (extração fiel de texto) e para gerar o relatório final formatado em PDF ou DOCX, seguindo o modelo padrão. Cobre OCR, preservação de estrutura e diagramação.
---

# Formatação de arquivos jurídicos (PDF / DOCX / TXT)

Trata a entrada e a saída de documentos. Formatos suportados: PDF, DOCX e TXT.

## 0. Origem do arquivo — local ou Drive

Antes de ler, identifique a origem:

- **Anexo local / caminho passado pelo usuário** → leitura direta com `Read`.
- **Pasta do Drive** (Modo A da `relatorio-juridico` — identificador) → use as
  ferramentas MCP do Google Drive:
  - `mcp__claude_ai_Google_Drive__search_files` para localizar pasta/arquivo.
  - `mcp__claude_ai_Google_Drive__read_file_content` para ler texto direto
    (preferencial para `.txt` e `.docx`).
  - `mcp__claude_ai_Google_Drive__download_file_content` para o binário
    quando precisar processar (ex.: PDF que exige OCR).
- **Sempre prefira o `.txt` ao `.pdf`** quando ambos existirem na pasta. O
  conversor `pdf2txt` do escritório gera os dois lado a lado; o `.txt` já traz
  marcadores `[Pagina N]` para citação e reduz drasticamente o consumo de
  tokens. Caia para o `.pdf` apenas se o `.txt` estiver ausente ou se o
  cabeçalho do `.txt` sinalizar páginas digitalizadas sem texto.

## Leitura (entrada)
1. **PDF**: leia com a ferramenta `Read` (suporta PDF). Para PDFs digitalizados
   (imagem), aplique OCR; marque trechos ilegíveis em vez de adivinhar.
2. **DOCX**: extraia texto preservando títulos, listas, tabelas e numeração de
   cláusulas.
3. **TXT**: texto já extraído (ex.: pelo conversor PDF→TXT do escritório). Leia
   direto. O cabeçalho do arquivo indica o documento de origem e o total de
   páginas; marcadores `[Pagina N]` preservam a paginação para citação. Se o
   cabeçalho avisar que há páginas digitalizadas sem texto, sinalize a lacuna.
4. **Preserve a estrutura**: mantenha cabeçalhos de peça, paginação dos autos
   (folhas) e a ordem original.
5. Reporte: nº de páginas, peças identificadas, qualidade do OCR e páginas
   faltantes.

## Geração (saída)
1. Siga **rigorosamente o modelo padrão** carregado pela skill
   `relatorio-juridico`.
2. **DOCX**: gere via biblioteca apropriada (ex.: `python-docx`) — estilos de
   título, sumário, tabelas, numeração.
3. **PDF**: gere a partir do DOCX/Markdown (conversão via LibreOffice ou
   pandoc) ou diretamente (ex.: `reportlab`/`weasyprint`). Confirme com o
   usuário a ferramenta disponível no ambiente.
4. **Diagramação jurídica**: fonte legível, margens adequadas, cabeçalho/rodapé
   com identificação do processo, numeração de páginas, citações recuadas.
5. **Texto justificado**: todo texto em prosa (células de texto, blocos
   descritivos, observações) deve ter alinhamento justificado em ambas as
   margens. Em DOCX, aplicar `WD_ALIGN_PARAGRAPH.JUSTIFY` aos parágrafos;
   em PDF/Markdown, usar CSS `text-align: justify` ou equivalente.
6. **Dados sempre em tabela**: não deixar conteúdo solto fora de tabela.
   Blocos de texto corrido vão em tabela de uma coluna (cabeçalho + célula).
7. Nomeie o arquivo de forma rastreável:
   `Relatorio_<numeroProcesso>_<AAAA-MM-DD>.<ext>`.

## Cuidados
- Não altere conteúdo ao reformatar: formatação não é edição.
- Transcrições devem ser literais; sínteses devem ser marcadas como tais.
- Verifique se o ambiente tem as bibliotecas necessárias; se faltar, instrua o
  usuário a instalá-las antes de gerar.
