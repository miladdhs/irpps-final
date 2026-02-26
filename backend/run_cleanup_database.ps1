# اسکریپت اجرای تمیزکاری دیتابیس

Write-Host "اجرای اسکریپت تمیزکاری دیتابیس..." -ForegroundColor Green

# تغییر به دایرکتوری backend
Set-Location $PSScriptRoot

# فعال‌سازی محیط مجازی
if (Test-Path "venv\Scripts\Activate.ps1") {
    Write-Host "فعال‌سازی محیط مجازی..." -ForegroundColor Yellow
    & "venv\Scripts\Activate.ps1"
}

# اجرای اسکریپت Python
Write-Host "اجرای اسکریپت تمیزکاری..." -ForegroundColor Yellow
python cleanup_database.py

Write-Host "اتمام اجرا" -ForegroundColor Green
