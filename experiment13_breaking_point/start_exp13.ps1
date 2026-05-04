param(
    [ValidateSet("smoke", "standard", "full")]
    [string]$Profile = "standard",

    [switch]$SkipValidation,
    [switch]$Clean
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

$LocalPython = Join-Path $ScriptDir "..\.venv\Scripts\python.exe"
$RepoPython = Join-Path $ScriptDir ".venv\Scripts\python.exe"

if (Test-Path $RepoPython) {
    $Python = $RepoPython
} elseif (Test-Path $LocalPython) {
    $Python = $LocalPython
} else {
    $Python = "python"
}

Write-Host "Using Python: $Python" -ForegroundColor Cyan
Write-Host "Running Experiment 13 with profile: $Profile" -ForegroundColor Cyan

$RunArgs = @("run_experiment13.py", "--profile", $Profile, "--output-dir", "analysis")
if ($Clean) {
    $RunArgs += "--clean"
}

& $Python @RunArgs
if ($LASTEXITCODE -ne 0) {
    throw "Experiment 13 run failed with exit code $LASTEXITCODE"
}

if (-not $SkipValidation) {
    Write-Host "Running Experiment 13 validation..." -ForegroundColor Cyan
    & $Python "validate_exp13.py" "--analysis-dir" "analysis"
    if ($LASTEXITCODE -ne 0) {
        throw "Experiment 13 validation failed with exit code $LASTEXITCODE. Inspect analysis/validation_report.md."
    }
}

Write-Host "Experiment 13 complete. Upload analysis/exp13_report.md, validation_report.md, summary CSVs, and plots for review." -ForegroundColor Green
