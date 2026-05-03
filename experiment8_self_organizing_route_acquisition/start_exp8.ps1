param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ExtraArgs
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

$Python = Join-Path $ScriptDir "..\.venv\Scripts\python.exe"
if (-not (Test-Path $Python)) {
    throw "Could not find Python at $Python. Create the shared virtualenv one directory up first."
}

Write-Host "Using Python: $Python"
Write-Host "Running Experiment 8 - Self-Organizing Contextual Route Acquisition"

# Legitimate local experiment:
# - one-step transition training only
# - no direct multi-step answer training
# - 30 seeds
# - bounded symbolic world 0..31
# - composition evaluated on paths up to 8 steps
& $Python .\run_exp8_suite.py `
    --db .\runs\exp8_self_organizing_route_acquisition.sqlite3 `
    --output-dir .\analysis\exp8 `
    --max-number 31 `
    --max-steps 8 `
    --transition-train-repeats 1 `
    --path-train-repeats 0 `
    --seeds 30 `
    --hidden-units 2048 `
    --number-assembly-size 72 `
    --mode-assembly-size 24 `
    --pair-assembly-size 48 `
    --mode-overlap 0.0 `
    --context-bleed 0.0 `
    --feedback-noise 0.0 `
    --force `
    @ExtraArgs

if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

if ($ExtraArgs -contains "--help" -or $ExtraArgs -contains "-h") {
    return
}

Write-Host "Experiment 8 complete. Outputs are in .\analysis\exp8"
