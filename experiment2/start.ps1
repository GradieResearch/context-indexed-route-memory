$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvDir = Join-Path $scriptDir ".venv"
$pythonExe = Join-Path $venvDir "Scripts\python.exe"

if (-not (Test-Path $pythonExe)) {
    python -m venv $venvDir
}

& $pythonExe -m pip install -r (Join-Path $scriptDir "requirements.txt")

& $pythonExe (Join-Path $scriptDir "run_mnist_experiment.py") `
    --epochs 3 `
    --hidden-units 4096 `
    --active-hidden 128 `
    --max-train 10000 `
    --max-test 2000

& $pythonExe (Join-Path $scriptDir "analyze_results.py") `
    --db (Join-Path $scriptDir "runs\plastic_graph_mnist.sqlite3") `
    --output-dir (Join-Path $scriptDir "analysis")
