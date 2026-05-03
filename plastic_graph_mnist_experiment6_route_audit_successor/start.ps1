$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvDir = Join-Path $scriptDir "..\.venv"
$pythonExe = Join-Path $venvDir "Scripts\python.exe"
$venvCfg = Join-Path $venvDir "pyvenv.cfg"

if ((Test-Path $pythonExe) -and -not (Test-Path $venvCfg)) {
    Remove-Item -Recurse -Force $venvDir
}

if (-not (Test-Path $pythonExe) -or -not (Test-Path $venvCfg)) {
    python -m venv $venvDir
}

& $pythonExe -m pip install -r (Join-Path $scriptDir "requirements.txt")

& $pythonExe (Join-Path $scriptDir "run_exp6_suite.py") `
    --max-number 24 `
    --max-steps 5 `
    --train-sequence-repeats 180 `
    --training-max-steps 3 `
    --hidden-units 4096 `
    --assembly-size 72 `
    --mode-assembly-size 24 `
    --active-units 96 `
    --recurrent-edges-per-unit 48

& $pythonExe (Join-Path $scriptDir "analyze_exp6_suite.py") `
    --db (Join-Path $scriptDir "runs\exp6_route_audit_successor_suite.sqlite3") `
    --output-dir (Join-Path $scriptDir "analysis\exp6")
