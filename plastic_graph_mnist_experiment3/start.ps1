$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvDir = Join-Path $scriptDir "..\.venv"
$pythonExe = Join-Path $venvDir "Scripts\python.exe"

if (-not (Test-Path $pythonExe)) {
    python -m venv $venvDir
}

& $pythonExe -m pip install -r (Join-Path $scriptDir "requirements.txt")

& $pythonExe (Join-Path $scriptDir "run_experiment_suite.py") `
    --epochs 3 `
    --hidden-units 4096 `
    --active-hidden 128 `
    --input-edges-per-hidden 64 `
    --max-train 10000 `
    --max-test 2000

& $pythonExe (Join-Path $scriptDir "analyze_experiment_suite.py") `
    --db (Join-Path $scriptDir "runs\plastic_graph_suite.sqlite3") `
    --output-dir (Join-Path $scriptDir "analysis\suite")
