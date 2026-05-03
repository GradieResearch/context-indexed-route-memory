$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

$Python = Join-Path $ScriptDir "..\.venv\Scripts\python.exe"

if (-not (Test-Path $Python)) {
    Write-Host "Could not find shared virtual environment at: $Python" -ForegroundColor Red
    Write-Host "Create it one directory up, then install requirements:" -ForegroundColor Yellow
    Write-Host "  python -m venv ..\.venv"
    Write-Host "  ..\.venv\Scripts\python.exe -m pip install -r requirements.txt"
    exit 1
}

& $Python -m pip install -r requirements.txt

# Legitimate local Experiment 10 run.
# This run intentionally avoids raw predictions.csv by default to keep outputs manageable.
& $Python .\run_exp10_suite.py `
    --output-dir .\analysis\exp10 `
    --max-number 31 `
    --max-steps 8 `
    --initial-exposure-repeats 1 `
    --reversal-exposure-schedule "0 1 2 3 5 8 13 21" `
    --switchback-exposure-schedule "0 1 2 3 5 8 13" `
    --seeds 30 `
    --hidden-units 4096 `
    --number-assembly-size 72 `
    --mode-assembly-size 24 `
    --pair-assembly-size 48 `
    --world-assembly-size 24 `
    --feedback-noise 0.0 `
    --reward-delay-steps 0 `
    --phases reversal switchback `
    --force

Write-Host "Experiment 10 complete. Upload the contents of analysis/exp10 for review." -ForegroundColor Green
