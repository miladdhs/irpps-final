# اسکریپت اجرای محیط توسعه

Write-Host "=== راه‌اندازی محیط توسعه ISPP ===" -ForegroundColor Cyan
Write-Host ""

# چک کردن Docker
Write-Host "چک کردن Docker..." -ForegroundColor Yellow
$dockerRunning = docker ps 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Docker Desktop اجرا نیست!" -ForegroundColor Red
    Write-Host "لطفاً Docker Desktop را اجرا کنید و دوباره تلاش کنید." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "برای اجرای Docker Desktop:" -ForegroundColor Cyan
    Write-Host "  1. از Start Menu به Docker Desktop بروید" -ForegroundColor White
    Write-Host "  2. منتظر بمانید تا آیکون Docker سبز شود" -ForegroundColor White
    Write-Host "  3. این اسکریپت را دوباره اجرا کنید" -ForegroundColor White
    exit 1
}

Write-Host "✓ Docker در حال اجرا است" -ForegroundColor Green
Write-Host ""

# اجرای MySQL
Write-Host "اجرای MySQL با Docker..." -ForegroundColor Yellow
docker-compose up -d mysql

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ MySQL با موفقیت اجرا شد" -ForegroundColor Green
} else {
    Write-Host "❌ خطا در اجرای MySQL" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "منتظر آماده شدن MySQL..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

# چک کردن وضعیت MySQL
$mysqlStatus = docker-compose ps mysql
Write-Host $mysqlStatus
Write-Host ""

# اجرای Backend
Write-Host "=== اجرای Backend ===" -ForegroundColor Cyan
Write-Host "برای اجرای Backend، در یک ترمینال جدید این دستورات را اجرا کنید:" -ForegroundColor Yellow
Write-Host ""
Write-Host "  cd backend" -ForegroundColor White
Write-Host "  python manage.py migrate" -ForegroundColor White
Write-Host "  python manage.py runserver 0.0.0.0:8000" -ForegroundColor White
Write-Host ""

# اجرای Frontend
Write-Host "=== اجرای Frontend ===" -ForegroundColor Cyan
Write-Host "برای اجرای Frontend، در یک ترمینال جدید این دستورات را اجرا کنید:" -ForegroundColor Yellow
Write-Host ""
Write-Host "  cd frontend" -ForegroundColor White
Write-Host "  npm run dev" -ForegroundColor White
Write-Host ""

Write-Host "=== اطلاعات دسترسی ===" -ForegroundColor Cyan
Write-Host "Frontend: http://localhost:5174" -ForegroundColor Green
Write-Host "Backend:  http://localhost:8000" -ForegroundColor Green
Write-Host "MySQL:    localhost:3306" -ForegroundColor Green
Write-Host ""
Write-Host "برای مشاهده لاگ‌های MySQL:" -ForegroundColor Yellow
Write-Host "  docker-compose logs -f mysql" -ForegroundColor White
Write-Host ""
Write-Host "برای متوقف کردن MySQL:" -ForegroundColor Yellow
Write-Host "  docker-compose down" -ForegroundColor White
Write-Host ""
