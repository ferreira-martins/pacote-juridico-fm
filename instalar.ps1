# Pacote Jurídico F&M — instalador (Windows, PowerShell 5.1+)
# Uso: botão direito > "Executar com PowerShell", ou:  powershell -ExecutionPolicy Bypass -File instalar.ps1
# Copia skills/ e agents/ para a pasta do Claude Code do usuário (%USERPROFILE%\.claude). Não precisa de admin.
$ErrorActionPreference = "Stop"
$aqui = Split-Path -Parent $MyInvocation.MyCommand.Path
$claude = Join-Path $env:USERPROFILE ".claude"

if (Test-Path (Join-Path $env:USERPROFILE "ferreira-martins-juridico")) {
    Write-Host "Este PC tem o plugin ferreira-martins-juridico (PC do TI). Não instale o pacote aqui: as skills ficariam duplicadas." -ForegroundColor Yellow
    exit 1
}

foreach ($pasta in "skills", "agents") {
    if (-not (Test-Path (Join-Path $aqui $pasta))) { continue }   # versão pública não traz agents/
    $destino = Join-Path $claude $pasta
    New-Item -ItemType Directory -Force $destino | Out-Null
    Get-ChildItem (Join-Path $aqui $pasta) | ForEach-Object {
        $alvo = Join-Path $destino $_.Name
        if (Test-Path -LiteralPath $alvo) {   # versão anterior do pacote (skill = pasta; agente = arquivo .md)
            $velho = (Resolve-Path -LiteralPath $alvo).ProviderPath
            if ((Get-Item -LiteralPath $velho).PSIsContainer) { [IO.Directory]::Delete($velho, $true) } else { [IO.File]::Delete($velho) }
        }
        Copy-Item -Recurse $_.FullName $alvo
    }
    Write-Host "OK  $pasta -> $destino"
}

# Regras + tabela de roteamento no CLAUDE.md do usuário (lido em toda conversa): bloco entre marcadores, regravado a
# cada instalação; o resto do arquivo do usuário fica intacto. UTF-8 sem BOM.
$bloco = Join-Path $aqui "CLAUDE-pacote.md"
if (Test-Path $bloco) {
    $md = Join-Path $claude "CLAUDE.md"
    $ini = "<!-- pacote-juridico-fm:inicio -->"; $fim = "<!-- pacote-juridico-fm:fim -->"
    $novo = "$ini`r`n" + [IO.File]::ReadAllText($bloco, [Text.Encoding]::UTF8).Trim() + "`r`n$fim"
    $atual = if (Test-Path $md) { [IO.File]::ReadAllText($md, [Text.Encoding]::UTF8) } else { "" }
    $rx = [regex]::Escape($ini) + "[\s\S]*?" + [regex]::Escape($fim)
    $saida = if ($atual -match $rx) { [regex]::Replace($atual, $rx, { param($m) $novo }) } else { ($atual.TrimEnd() + "`r`n`r`n" + $novo + "`r`n").TrimStart() }
    [IO.File]::WriteAllText($md, $saida, (New-Object Text.UTF8Encoding $false))
    Write-Host "OK  regras do pacote -> $md"
}

# Python: o conferidor de citações e o cálculo de prazos precisam dele (3.10+)
$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) {
    Write-Host "`nFalta o Python. Instale pela Microsoft Store ('Python 3.12') ou python.org e rode este instalador de novo." -ForegroundColor Yellow
    exit 0
}
& python -m pip install --user --quiet pypdf python-docx
& python -X utf8 (Join-Path $claude "skills\conferencia-citacoes-fm\scripts\teste_conferir.py")
Write-Host "`nPronto. Feche e abra o Claude Code. Comece pelo GUIA-DO-TIME.md ou pelo README.md." -ForegroundColor Green
