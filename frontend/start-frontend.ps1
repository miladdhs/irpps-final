# اسکریپت اجرای Frontend

Write-Host "=== راه‌اندازی Frontend ===" -ForegroundColor Cyan
Write-Host ""

# چک کردن Node.js
Write-Host "چک کردن Node.js..." -ForegroundColor Yellow
$nodeVersion = node --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Node.js نصب نیست!" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Node.js $nodeVersion" -ForegroundColor Green
Write-Host ""

# چک کردن node_modules
$nodeModulesExists = Test-Path "node_modules"
if (-not $nodeModulesExists) {
    Write-Host "نصب dependencies..." -ForegroundColor Yellow
    npm install
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Dependencies نصب شد" -ForegroundColor Green
    } else {
        Write-Host "❌ خطا در نصب dependencies" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "✓ Dependencies نصب شده است" -ForegroundColor Green
}
Write-Host ""

# اجرای dev server
Write-Host "=== اجرای Vite Development Server ===" -ForegroundColor Cyan
Write-Host "Frontend در حال اجرا است: http://localhost:5174" -ForegroundColor Green
Write-Host ""
Write-Host "برای توقف سرور: Ctrl+C" -ForegroundColor Yellow
Write-Host ""

npm run dev
