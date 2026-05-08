$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

Write-Host "Experiment 15: neural baseline comparator validation profile" -ForegroundColor Cyan
Write-Host "Directory: $ScriptDir" -ForegroundColor DarkCyan

$CandidatePythons = @(
    (Join-Path $ScriptDir "..\..\.venv\Scripts\python.exe"),
    (Join-Path $ScriptDir "..\.venv\Scripts\python.exe"),
    (Join-Path $ScriptDir ".venv\Scripts\python.exe")
)

$Python = $null
foreach ($Candidate in $CandidatePythons) {
    if (Test-Path $Candidate) {
        $Python = $Candidate
        break
    }
}

if (-not $Python) {
    $Python = "python"
}

Write-Host "Using Python: $Python" -ForegroundColor DarkCyan
Write-Host "Starting validation-profile run..." -ForegroundColor Yellow
& $Python "run_experiment15.py" "--profile" "validation"
if ($LASTEXITCODE -ne 0) {
    throw "Experiment 15 validation-profile run failed with exit code $LASTEXITCODE"
}

Write-Host "Analyzing latest Exp15 run..." -ForegroundColor Yellow
& $Python "analyze_experiment15.py" "--analysis-root" "analysis"
if ($LASTEXITCODE -ne 0) {
    throw "Experiment 15 analysis failed with exit code $LASTEXITCODE"
}

Write-Host "Validating latest Exp15 artifacts..." -ForegroundColor Yellow
& $Python "validate_experiment15.py" "--analysis-root" "analysis"
if ($LASTEXITCODE -ne 0) {
    throw "Experiment 15 artifact validation failed with exit code $LASTEXITCODE"
}

Write-Host "Experiment 15 validation profile complete." -ForegroundColor Green
Write-Host "Review the latest analysis/exp15_validation_* directory before running full." -ForegroundColor Green
