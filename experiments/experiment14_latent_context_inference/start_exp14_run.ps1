param(
    [ValidateSet("smoke", "validation", "full")]
    [string]$Profile = "smoke",

    [switch]$SkipValidation,
    [switch]$NoSqlite,
    [int]$ProgressEvery = 0
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

Write-Host "Experiment 14: latent context inference" -ForegroundColor Cyan
Write-Host "Profile: $Profile" -ForegroundColor Cyan
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

$RunArgs = @("run_exp14_latent_context_inference.py", "--profile", $Profile)
if ($NoSqlite) {
    $RunArgs += "--no-sqlite"
}
if ($ProgressEvery -gt 0) {
    $RunArgs += @("--progress-every", $ProgressEvery)
}

Write-Host "Starting experiment run..." -ForegroundColor Yellow
& $Python @RunArgs

if ($LASTEXITCODE -ne 0) {
    throw "Experiment run failed with exit code $LASTEXITCODE"
}

if (-not $SkipValidation) {
    Write-Host "Starting validation..." -ForegroundColor Yellow
    & $Python "validate_exp14.py" "--analysis-root" "analysis"
    if ($LASTEXITCODE -ne 0) {
        throw "Validation failed with exit code $LASTEXITCODE"
    }
}
else {
    Write-Host "Validation skipped by request." -ForegroundColor Yellow
}

Write-Host "Experiment 14 $Profile run complete." -ForegroundColor Green
Write-Host "Upload the latest analysis/exp14_* directory for review." -ForegroundColor Green
