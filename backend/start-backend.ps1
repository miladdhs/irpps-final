# اسکریپت اجرای Backend

Write-Host "=== راه‌اندازی Backend ===" -ForegroundColor Cyan
Write-Host ""

# چک کردن Python
Write-Host "چک کردن Python..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Python نصب نیست!" -ForegroundColor Red
    exit 1
}
Write-Host "✓ $pythonVersion" -ForegroundColor Green
Write-Host ""

# چک کردن MySQL
Write-Host "چک کردن اتصال به MySQL..." -ForegroundColor Yellow
$mysqlCheck = docker-compose ps mysql 2>&1
if ($mysqlCheck -match "running") {
    Write-Host "✓ MySQL در حال اجرا است" -ForegroundColor Green
} else {
    Write-Host "⚠ MySQL اجرا نیست. در حال اجرا..." -ForegroundColor Yellow
    Set-Location ..
    docker-compose up -d mysql
    Set-Location backend
    Write-Host "منتظر آماده شدن MySQL..." -ForegroundColor Yellow
    Start-Sleep -Seconds 15
}
Write-Host ""

# نصب dependencies
Write-Host "بررسی dependencies..." -ForegroundColor Yellow
$venvExists = Test-Path "venv"
if (-not $venvExists) {
    Write-Host "ایجاد virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

Write-Host "فعال‌سازی virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

Write-Host "نصب dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt --quiet
Write-Host "✓ Dependencies نصب شد" -ForegroundColor Green
Write-Host ""

# اجرای migrations
Write-Host "اجرای migrations..." -ForegroundColor Yellow
python manage.py migrate
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Migrations با موفقیت اجرا شد" -ForegroundColor Green
} else {
    Write-Host "❌ خطا در اجرای migrations" -ForegroundColor Red
    exit 1
}
Write-Host ""

# ایجاد superuser (اختیاری)
Write-Host "آیا میخواهید یک superuser ایجاد کنید؟ (y/n)" -ForegroundColor Yellow
$createSuperuser = Read-Host
if ($createSuperuser -eq "y") {
    python manage.py createsuperuser
}
Write-Host ""

# اجرای سرور
Write-Host "=== اجرای Django Development Server ===" -ForegroundColor Cyan
Write-Host "Backend در حال اجرا است: http://localhost:8000" -ForegroundColor Green
Write-Host "Admin Panel: http://localhost:8000/admin" -ForegroundColor Green
Write-Host ""
Write-Host "برای توقف سرور: Ctrl+C" -ForegroundColor Yellow
Write-Host ""

python manage.py runserver 0.0.0.0:8000
