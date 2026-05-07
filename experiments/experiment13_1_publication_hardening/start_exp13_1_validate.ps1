param(
    [string]$RunId = "latest",
    [string]$AnalysisDir = "",
    [switch]$FailOnWarn
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

$ValidationArgs = @(
    "validate_exp13_1.py",
    "--experiment-dir", $ScriptDir
)

if ($AnalysisDir -ne "") {
    $ValidationArgs += @("--analysis-dir", $AnalysisDir)
} else {
    $ValidationArgs += @("--run-id", $RunId)
}

if ($FailOnWarn) {
    $ValidationArgs += "--fail-on-warn"
}

Write-Host "Using Python: $Python" -ForegroundColor Cyan
Write-Host "Validating Experiment 13.1 run: $RunId" -ForegroundColor Cyan

& $Python @ValidationArgs
if ($LASTEXITCODE -ne 0) {
    throw "Experiment 13.1 validation failed with exit code $LASTEXITCODE. Inspect validation_report.md in the analysis run directory."
}

Write-Host "Experiment 13.1 validation complete." -ForegroundColor Green
