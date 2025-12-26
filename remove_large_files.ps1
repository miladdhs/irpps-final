# PowerShell Script to Remove Large Files from Git
# Run this script to remove PDF, image, and document files from Git tracking

Write-Host "=== Removing Large Files from Git ===" -ForegroundColor Green
Write-Host ""

# Get all tracked files in Content folder that match patterns
$filesToRemove = git ls-files "frontend/public/Content" | Where-Object { 
    $_ -match '\.(pdf|jpg|jpeg|png|docx|doc|pptx|ppt)$' 
}

if ($filesToRemove.Count -eq 0) {
    Write-Host "No large files found in Git tracking." -ForegroundColor Yellow
    exit 0
}

Write-Host "Found $($filesToRemove.Count) files to remove from Git:" -ForegroundColor Cyan
$filesToRemove | ForEach-Object { Write-Host "  - $_" }

Write-Host ""
$confirm = Read-Host "Do you want to remove these files from Git? (y/N)"

if ($confirm -ne "y" -and $confirm -ne "Y") {
    Write-Host "Operation cancelled." -ForegroundColor Yellow
    exit 0
}

Write-Host ""
Write-Host "Removing files from Git tracking..." -ForegroundColor Green

# Remove files from Git tracking (but keep them on disk)
$filesToRemove | ForEach-Object {
    git rm --cached $_ 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ Removed: $_" -ForegroundColor Green
    } else {
        Write-Host "  ✗ Failed: $_" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "=== Done! ===" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Check git status: git status" -ForegroundColor White
Write-Host "2. Commit the changes: git commit -m 'Remove large files from Git'" -ForegroundColor White
Write-Host "3. Push: git push" -ForegroundColor White
Write-Host ""
Write-Host "Note: The files are still on your disk, just removed from Git tracking." -ForegroundColor Yellow

