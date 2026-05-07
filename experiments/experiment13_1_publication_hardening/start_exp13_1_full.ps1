param(
    [string]$RunId = "",
    [int]$ProgressEvery = 10,
    [switch]$Clean,
    [switch]$NoSqlite
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Args = @("-ExecutionPolicy", "Bypass", "-File", (Join-Path $ScriptDir "start_exp13_1_run.ps1"), "-Profile", "full", "-ProgressEvery", $ProgressEvery.ToString())
if ($RunId -ne "") { $Args += @("-RunId", $RunId) }
if ($Clean) { $Args += "-Clean" }
if ($NoSqlite) { $Args += "-NoSqlite" }

powershell @Args
if ($LASTEXITCODE -ne 0) {
    throw "Experiment 13.1 full run failed with exit code $LASTEXITCODE"
}
