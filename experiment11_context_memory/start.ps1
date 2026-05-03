$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

$Python = Join-Path $ScriptDir "..\.venv\Scripts\python.exe"

if (-not (Test-Path $Python)) {
    Write-Host "Could not find Python at $Python" -ForegroundColor Red
    Write-Host "Create the shared venv one directory up, or adjust start.ps1." -ForegroundColor Yellow
    exit 1
}

Write-Host "Running Experiment 11 — Context-Separated Memory and Non-Destructive Rebinding" -ForegroundColor Cyan
Write-Host "Using Python: $Python" -ForegroundColor Cyan
Write-Host "Progress will stream to console and also write to analysis/exp11/exp11_run.log" -ForegroundColor Cyan

& $Python .\run_exp11_suite.py `
    --output-dir analysis/exp11 `
    --max-number 31 `
    --max-steps 8 `
    --worlds "A B C D" `
    --seeds 30 `
    --initial-exposure-repeats 1 `
    --new-world-exposure-schedule "0 1 2 3 5 8 13 21" `
    --alternation-cycles 21 `
    --alternation-eval-schedule "0 1 2 3 5 8 13 21" `
    --scaling-exposure-repeats 3 `
    --context-bleed-sweep "0 0.05 0.10 0.20 0.35" `
    --context-dropout-sweep "0 0.05 0.10 0.20" `
    --phases sequential alternating scaling context_noise `
    --log-level INFO `
    --force

if ($LASTEXITCODE -ne 0) {
    Write-Host "Experiment 11 failed with exit code $LASTEXITCODE" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "Experiment 11 complete. Upload analysis/exp11 for review." -ForegroundColor Green
