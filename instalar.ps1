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
        if (Test-Path $alvo) { Remove-Item -Recurse -Force $alvo }   # versão anterior do pacote
        Copy-Item -Recurse $_.FullName $alvo
    }
    Write-Host "OK  $pasta -> $destino"
}

# Python: o conferidor de citações e o cálculo de prazos precisam dele (3.10+)
$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) {
    Write-Host "`nFalta o Python. Instale pela Microsoft Store ('Python 3.12') ou python.org e rode este instalador de novo." -ForegroundColor Yellow
    exit 0
}
& python -m pip install --user --quiet pypdf python-docx
& python -X utf8 (Join-Path $claude "skills\conferencia-citacoes-fm\scripts\teste_conferir.py")
Write-Host "`nPronto. Feche e abra o Claude Code. Comece pelo GUIA-DO-TIME.md." -ForegroundColor Green
