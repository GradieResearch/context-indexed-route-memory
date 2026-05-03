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

& $pythonExe (Join-Path $scriptDir "run_exp4_suite.py") `
    --max-number 24 `
    --max-addend 5 `
    --train-transition-repeats 120 `
    --hidden-units 4096 `
    --assembly-size 96 `
    --active-units 96 `
    --recurrent-edges-per-unit 48

& $pythonExe (Join-Path $scriptDir "analyze_exp4_suite.py") `
    --db (Join-Path $scriptDir "runs\exp4_successor_suite.sqlite3") `
    --output-dir (Join-Path $scriptDir "analysis\exp4")
