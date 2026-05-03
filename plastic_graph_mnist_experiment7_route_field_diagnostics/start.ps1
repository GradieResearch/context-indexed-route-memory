$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

$Python = Join-Path $ScriptDir "..\.venv\Scripts\python.exe"

if (-not (Test-Path $Python)) {
    throw "Expected Python virtual environment at '$Python'. Create the shared venv one directory above this experiment folder, then install requirements.txt."
}

& $Python -m pip install -r .\requirements.txt

& $Python .\run_exp7_suite.py `
    --max-number 31 `
    --max-steps 8 `
    --train-repeats 1 `
    --path-train-repeats 0 `
    --seeds 30 `
    --force

& $Python .\analyze_exp7_suite.py `
    --db .\runs\exp7_route_field_diagnostics.sqlite3 `
    --output-dir .\analysis\exp7

Write-Host "Experiment 7 complete. Open .\analysis\exp7\exp7_report.md"
