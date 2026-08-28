$gitBin = "$env:LOCALAPPDATA\Programs\MinGit\cmd\git.exe"
if (Test-Path $gitBin) {
    Write-Host "Found Git at $gitBin" -ForegroundColor Cyan
    & $gitBin push -u origin main
} else {
    git push -u origin main
}
