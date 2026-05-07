param(
    [string]$AnalysisDir = ""
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

if ([string]::IsNullOrWhiteSpace($AnalysisDir)) {
    & $Python "validate_exp13_2.py" "--analysis-root" (Join-Path $ScriptDir "analysis")
} else {
    & $Python "validate_exp13_2.py" "--analysis-dir" $AnalysisDir
}
if ($LASTEXITCODE -ne 0) {
    throw "Validation failed with exit code $LASTEXITCODE"
}
