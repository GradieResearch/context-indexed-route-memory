param(
    [ValidateSet("smoke", "validation", "full")]
    [string]$Profile = "smoke",
    [string]$RunId = "",
    [int]$ProgressEvery = 0,
    [switch]$SkipValidation,
    [switch]$NoSqlite
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

$VenvPython = Join-Path $ScriptDir "..\..\.venv\Scripts\python.exe"
if (Test-Path $VenvPython) {
    $Python = $VenvPython
} else {
    $Python = "python"
}

Write-Host "Experiment 13.2 baseline suite" -ForegroundColor Cyan
Write-Host "Profile: $Profile" -ForegroundColor Cyan
Write-Host "Python: $Python" -ForegroundColor Cyan

$RunArgs = @("run_exp13_2_baseline_suite.py", "--profile", $Profile)
if (-not [string]::IsNullOrWhiteSpace($RunId)) {
    $RunArgs += @("--run-id", $RunId)
}
if ($ProgressEvery -gt 0) {
    $RunArgs += @("--progress-every", $ProgressEvery)
}
if ($NoSqlite) {
    $RunArgs += "--no-sqlite"
}

Write-Host "Running: $Python $($RunArgs -join ' ')" -ForegroundColor DarkCyan
& $Python @RunArgs
if ($LASTEXITCODE -ne 0) {
    throw "Experiment run failed with exit code $LASTEXITCODE"
}

$LatestRun = Get-ChildItem -Path (Join-Path $ScriptDir "analysis") -Directory |
    Where-Object { $_.Name -like "exp13_2_$Profile*" } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

if ($null -eq $LatestRun) {
    throw "Could not find latest analysis run directory for profile '$Profile'."
}

Write-Host "Latest analysis run: $($LatestRun.FullName)" -ForegroundColor Green

if (-not $SkipValidation) {
    Write-Host "Validating run..." -ForegroundColor Cyan
    & $Python "validate_exp13_2.py" "--analysis-dir" $LatestRun.FullName
    if ($LASTEXITCODE -ne 0) {
        throw "Validation failed with exit code $LASTEXITCODE"
    }
}

Write-Host "Experiment 13.2 $Profile run complete." -ForegroundColor Green
Write-Host "Upload this directory for analysis: $($LatestRun.FullName)" -ForegroundColor Green
