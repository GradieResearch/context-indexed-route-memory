param(
    [ValidateSet("smoke", "standard", "full")]
    [string]$Profile = "smoke",
    [string]$RunId = "",
    [int]$ProgressEvery = 10,
    [switch]$Clean,
    [switch]$NoSqlite
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $ScriptDir "..\..")

function Resolve-Python {
    $Candidates = @(
        (Join-Path $RepoRoot ".venv\Scripts\python.exe"),
        (Join-Path $ScriptDir ".venv\Scripts\python.exe")
    )

    foreach ($Candidate in $Candidates) {
        if (Test-Path $Candidate) {
            return $Candidate
        }
    }

    $PythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if ($PythonCommand) {
        return $PythonCommand.Source
    }

    throw "Could not find Python. Expected repo-local .venv\Scripts\python.exe or a python command on PATH."
}

$Python = Resolve-Python
Set-Location $ScriptDir

$RunArgs = @(
    "run_exp13_1_publication_hardening.py",
    "--profile", $Profile,
    "--experiment-dir", $ScriptDir,
    "--progress-every", $ProgressEvery.ToString()
)

if ($RunId -ne "") {
    $RunArgs += @("--run-id", $RunId)
}

if ($Clean) {
    $RunArgs += "--clean"
}

if ($NoSqlite) {
    $RunArgs += "--no-sqlite"
}

Write-Host "Using Python: $Python" -ForegroundColor Cyan
Write-Host "Experiment 13.1 run profile: $Profile" -ForegroundColor Cyan
Write-Host "Experiment directory: $ScriptDir" -ForegroundColor Cyan
Write-Host "Progress logging: console + analysis/<run_id>/progress.jsonl" -ForegroundColor Cyan

& $Python @RunArgs
if ($LASTEXITCODE -ne 0) {
    throw "Experiment 13.1 run failed with exit code $LASTEXITCODE"
}

Write-Host "Experiment 13.1 $Profile run complete. Run validation separately with .\start_exp13_1_validate.ps1 -RunId latest" -ForegroundColor Green
