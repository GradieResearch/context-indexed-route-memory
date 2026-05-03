$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

$Python = Join-Path $ScriptDir "..\.venv\Scripts\python.exe"
if (-not (Test-Path $Python)) {
    Write-Host "Could not find shared virtualenv Python at: $Python" -ForegroundColor Yellow
    Write-Host "Create it from the workspace root with:" -ForegroundColor Yellow
    Write-Host "  py -m venv .venv" -ForegroundColor Yellow
    Write-Host "  .\.venv\Scripts\python.exe -m pip install -r .\plastic_graph_mnist_experiment9_robust_adaptive_route_plasticity\requirements.txt" -ForegroundColor Yellow
    exit 1
}

& $Python -m pip install -r .\requirements.txt

& $Python .\run_exp9_suite.py `
    --db .\runs\exp9_robust_adaptive_route_plasticity.sqlite3 `
    --output-dir .\analysis\exp9 `
    --max-number 31 `
    --max-steps 8 `
    --transition-train-repeats 1 `
    --seeds 30 `
    --hidden-units 4096 `
    --number-assembly-size 72 `
    --mode-assembly-size 24 `
    --pair-assembly-size 48 `
    --phases interference feedback `
    --context-bleed-sweep "0 0.05 0.10 0.20 0.35 0.50" `
    --feedback-noise-sweep "0 0.05 0.10 0.20 0.30" `
    --reward-delay-sweep "0 2 4" `
    --force

Write-Host "Experiment 9 complete. Upload .\analysis\exp9 for review." -ForegroundColor Green
