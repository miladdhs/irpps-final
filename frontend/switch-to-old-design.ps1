# اسکریپت برگشت به دیزاین قدیمی

Write-Host "🔙 شروع برگشت به دیزاین قدیمی..." -ForegroundColor Cyan
Write-Host ""

# بررسی وجود فایل‌های بکاپ
if (-not (Test-Path "src/AppOld.vue")) {
    Write-Host "❌ فایل‌های بکاپ یافت نشد!" -ForegroundColor Red
    Write-Host "لطفاً ابتدا دیزاین جدید را با اسکریپت switch-to-new-design.ps1 فعال کنید." -ForegroundColor Yellow
    exit
}

# تایید از کاربر
$confirmation = Read-Host "آیا مطمئن هستید که می‌خواهید به دیزاین قدیمی برگردید؟ (yes/no)"
if ($confirmation -ne 'yes') {
    Write-Host "❌ عملیات لغو شد." -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "🔄 بازگردانی فایل‌های قدیمی..." -ForegroundColor Yellow

# بازگردانی App.vue
Copy-Item "src/AppOld.vue" "src/App.vue" -Force
Write-Host "✅ App.vue قدیمی بازگردانی شد" -ForegroundColor Green

# بازگردانی فایل‌های views
$files = @("Home", "About", "News", "Events", "Services")
foreach ($file in $files) {
    $oldPath = "src/views/${file}Old.vue"
    $targetPath = "src/views/$file.vue"
    
    if (Test-Path $oldPath) {
        Copy-Item $oldPath $targetPath -Force
        Write-Host "✅ $file.vue قدیمی بازگردانی شد" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "✨ بازگشت به دیزاین قدیمی با موفقیت انجام شد!" -ForegroundColor Green
Write-Host ""
Write-Host "📝 نکات:" -ForegroundColor Cyan
Write-Host "1. دیزاین قدیمی شما فعال شد"
Write-Host "2. فایل‌های جدید همچنان با پسوند 'New' موجود هستند"
Write-Host "3. پروژه را با 'npm run dev' اجرا کنید"
Write-Host ""
