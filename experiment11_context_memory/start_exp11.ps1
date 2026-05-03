param(
    [switch]$SkipDependencyInstall,
    [switch]$ValidationOnly
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

$Python = if ($env:EXP11_PYTHON) {
    $env:EXP11_PYTHON
} else {
    Join-Path $ScriptDir "..\.venv\Scripts\python.exe"
}

$ValidationDir = Join-Path $ScriptDir "analysis\exp11_validation"
$RunDir = Join-Path $ScriptDir "analysis\exp11"

function Write-Section {
    param([Parameter(Mandatory = $true)][string]$Message)
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor DarkGray
    Write-Host $Message -ForegroundColor Cyan
    Write-Host "============================================================" -ForegroundColor DarkGray
}

function Invoke-PythonStep {
    param(
        [Parameter(Mandatory = $true)][string]$Name,
        [Parameter(Mandatory = $true)][string[]]$Arguments
    )

    Write-Host ""
    Write-Host "[$Name]" -ForegroundColor Yellow
    & $Python @Arguments

    $ExitCode = $LASTEXITCODE
    if ($ExitCode -ne 0) {
        throw "$Name failed with exit code $ExitCode"
    }
}

function Assert-FileExists {
    param([Parameter(Mandatory = $true)][string]$Path)

    if (-not (Test-Path $Path)) {
        throw "Expected output file was not produced: $Path"
    }
}

Write-Section "Experiment 11 - Context-Separated Memory and Non-Destructive Rebinding"
Write-Host "Working directory: $ScriptDir" -ForegroundColor Gray
Write-Host "Python: $Python" -ForegroundColor Gray
Write-Host "Validation output: $ValidationDir" -ForegroundColor Gray
Write-Host "Full output: $RunDir" -ForegroundColor Gray

if (-not (Test-Path $Python)) {
    Write-Host "Could not find Python at $Python" -ForegroundColor Red
    Write-Host "Expected the shared virtual environment at ..\.venv\Scripts\python.exe." -ForegroundColor Yellow
    Write-Host "Either create that venv or set EXP11_PYTHON to the Python executable you want to use." -ForegroundColor Yellow
    exit 1
}

if (-not $SkipDependencyInstall) {
    Write-Section "Installing / validating Python dependencies"

    if (Test-Path (Join-Path $ScriptDir "requirements.txt")) {
        Invoke-PythonStep "Install requirements.txt" @("-m", "pip", "install", "-r", "requirements.txt")
    }

    # pandas.DataFrame.to_markdown needs tabulate. It is not always included in minimal envs.
    Invoke-PythonStep "Install analysis markdown dependency" @("-m", "pip", "install", "tabulate")
} else {
    Write-Host "Skipping dependency installation because -SkipDependencyInstall was supplied." -ForegroundColor Yellow
}

Write-Section "Validation step 1 - compile and import checks"

Invoke-PythonStep "Compile Python files" @(
    "-m", "py_compile",
    "exp11/core.py",
    "run_exp11_suite.py",
    "analyze_exp11_suite.py",
    "run_exp11_context_memory.py"
)

$VariantCheck = @'
from exp11.core import make_variants

variants = [v.name for v in make_variants()]
expected = {
    "exp11_full_context_separated_memory",
    "exp11_world_gated_plasticity",
    "exp11_no_world_context",
    "exp11_no_context_binding",
    "exp11_no_structural_plasticity",
    "exp11_no_recurrence",
    "exp11_no_inhibition",
    "exp11_no_consolidation",
    "exp11_strong_consolidation",
    "exp11_shared_edges_only",
}
missing = sorted(expected.difference(variants))
if missing:
    raise SystemExit(f"Missing expected variants: {missing}")
print("Validated variants:")
for name in variants:
    print(f"  - {name}")
'@

Invoke-PythonStep "Import and variant check" @("-c", $VariantCheck)

Write-Section "Validation step 2 - all-variant smoke run"
Write-Host "This intentionally exercises every variant, including no_context_binding and no_recurrence." -ForegroundColor Gray

$ValidationArgs = @(
    ".\run_exp11_suite.py",
    "--output-dir", "analysis/exp11_validation",
    "--max-number", "9",
    "--max-steps", "3",
    "--worlds", "A B C",
    "--seeds", "1",
    "--initial-exposure-repeats", "1",
    "--new-world-exposure-schedule", "0 1",
    "--alternation-cycles", "1",
    "--alternation-eval-schedule", "0 1",
    "--scaling-exposure-repeats", "1",
    "--context-bleed-sweep", "0 0.10",
    "--context-dropout-sweep", "0 0.10",
    "--phases", "sequential", "alternating", "scaling", "context_noise",
    "--log-level", "INFO",
    "--force"
)

Invoke-PythonStep "Experiment 11 smoke validation run" $ValidationArgs

Write-Section "Validation step 3 - smoke output checks"

Assert-FileExists (Join-Path $ValidationDir "runs.csv")
Assert-FileExists (Join-Path $ValidationDir "metrics.csv")
Assert-FileExists (Join-Path $ValidationDir "route_diagnostics.csv")
Assert-FileExists (Join-Path $ValidationDir "failure_taxonomy.csv")
Assert-FileExists (Join-Path $ValidationDir "baselines.csv")
Assert-FileExists (Join-Path $ValidationDir "metrics_wide.csv")
Assert-FileExists (Join-Path $ValidationDir "exp11_report.md")

$SmokeOutputCheck = @'
from pathlib import Path
import pandas as pd

out = Path("analysis/exp11_validation")
runs = pd.read_csv(out / "runs.csv")
metrics = pd.read_csv(out / "metrics.csv")

expected_variants = {
    "exp11_full_context_separated_memory",
    "exp11_world_gated_plasticity",
    "exp11_no_world_context",
    "exp11_no_context_binding",
    "exp11_no_structural_plasticity",
    "exp11_no_recurrence",
    "exp11_no_inhibition",
    "exp11_no_consolidation",
    "exp11_strong_consolidation",
    "exp11_shared_edges_only",
}
expected_phases = {"sequential", "alternating", "scaling", "context_noise"}

actual_variants = set(runs["run_name"].dropna())
actual_phases = set(runs["phase"].dropna())

missing_variants = sorted(expected_variants.difference(actual_variants))
missing_phases = sorted(expected_phases.difference(actual_phases))

if missing_variants:
    raise SystemExit(f"Smoke run did not complete variants: {missing_variants}")
if missing_phases:
    raise SystemExit(f"Smoke run did not complete phases: {missing_phases}")
if metrics.empty:
    raise SystemExit("Smoke run produced an empty metrics.csv")

print(f"Smoke validation completed {len(runs)} run rows and {len(metrics)} metric rows.")
print("All expected variants and phases were exercised.")
'@

Invoke-PythonStep "Smoke result integrity check" @("-c", $SmokeOutputCheck)

Write-Host "Validation completed successfully." -ForegroundColor Green

if ($ValidationOnly) {
    Write-Host "ValidationOnly was supplied, so the full Experiment 11 run will not start." -ForegroundColor Yellow
    exit 0
}

Write-Section "Starting full Experiment 11 run"
Write-Host "Progress will stream to the console and write to analysis/exp11/exp11_run.log." -ForegroundColor Gray
Write-Host "Raw per-task predictions are disabled by default to keep outputs manageable." -ForegroundColor Gray

$FullRunArgs = @(
    ".\run_exp11_suite.py",
    "--output-dir", "analysis/exp11",
    "--max-number", "31",
    "--max-steps", "8",
    "--worlds", "A B C D",
    "--seeds", "30",
    "--initial-exposure-repeats", "1",
    "--new-world-exposure-schedule", "0 1 2 3 5 8 13 21",
    "--alternation-cycles", "21",
    "--alternation-eval-schedule", "0 1 2 3 5 8 13 21",
    "--scaling-exposure-repeats", "3",
    "--context-bleed-sweep", "0 0.05 0.10 0.20 0.35",
    "--context-dropout-sweep", "0 0.05 0.10 0.20",
    "--phases", "sequential", "alternating", "scaling", "context_noise",
    "--log-level", "INFO",
    "--log-every-seed", "1",
    "--force"
)

Invoke-PythonStep "Experiment 11 full run" $FullRunArgs

Write-Section "Full run output checks"

Assert-FileExists (Join-Path $RunDir "runs.csv")
Assert-FileExists (Join-Path $RunDir "metrics.csv")
Assert-FileExists (Join-Path $RunDir "route_diagnostics.csv")
Assert-FileExists (Join-Path $RunDir "failure_taxonomy.csv")
Assert-FileExists (Join-Path $RunDir "baselines.csv")
Assert-FileExists (Join-Path $RunDir "metrics_wide.csv")
Assert-FileExists (Join-Path $RunDir "exp11_memory_indices.csv")
Assert-FileExists (Join-Path $RunDir "exp11_report.md")

Write-Host "Experiment 11 complete." -ForegroundColor Green
Write-Host "Upload analysis/exp11 for review." -ForegroundColor Green
