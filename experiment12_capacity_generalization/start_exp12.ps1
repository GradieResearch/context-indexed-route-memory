param(
    [ValidateSet('full', 'validate', 'custom')]
    [string]$Profile = 'full',

    [string]$OutDir = 'analysis/exp12',

    [switch]$InstallDependencies,

    [switch]$ValidateOnly
)

$ErrorActionPreference = 'Stop'

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

$CandidatePythons = @(
    (Join-Path $ScriptDir '..\.venv\Scripts\python.exe'),
    (Join-Path $ScriptDir '.venv\Scripts\python.exe'),
    'python'
)

$Python = $null
foreach ($Candidate in $CandidatePythons) {
    try {
        if ($Candidate -eq 'python') {
            $version = & python --version 2>$null
            if ($LASTEXITCODE -eq 0) {
                $Python = 'python'
                break
            }
        } elseif (Test-Path $Candidate) {
            $Python = $Candidate
            break
        }
    } catch {
        # Try the next candidate.
    }
}

if (-not $Python) {
    throw 'Could not find Python. Create a .venv or ensure python is on PATH.'
}

Write-Host "Using Python: $Python" -ForegroundColor Cyan
& $Python --version

if ($InstallDependencies) {
    Write-Host 'Installing Python dependencies from requirements.txt...' -ForegroundColor Cyan
    & $Python -m pip install -r requirements.txt
}

if ($ValidateOnly) {
    $Profile = 'validate'
    if ($OutDir -eq 'analysis/exp12') {
        $OutDir = 'analysis/exp12_validation'
    }
}

Write-Host "Starting Experiment 12 with profile '$Profile'..." -ForegroundColor Green
Write-Host "Output directory: $OutDir" -ForegroundColor Green

& $Python .\experiment12.py --profile $Profile --out $OutDir

if ($LASTEXITCODE -ne 0) {
    throw "Experiment 12 failed with exit code $LASTEXITCODE."
}

Write-Host 'Experiment 12 complete. Upload the analysis directory for review.' -ForegroundColor Green
