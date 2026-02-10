# اسکریپت جابجایی به دیزاین جدید (با بکاپ)

Write-Host "🔄 شروع جابجایی به دیزاین جدید..." -ForegroundColor Cyan
Write-Host ""

# تایید از کاربر
$confirmation = Read-Host "آیا مطمئن هستید که می‌خواهید به دیزاین جدید تغییر کنید؟ (yes/no)"
if ($confirmation -ne 'yes') {
    Write-Host "❌ عملیات لغو شد." -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "💾 ایجاد بکاپ از فایل‌های قدیمی..." -ForegroundColor Yellow

# بکاپ App.vue
if (Test-Path "src/App.vue") {
    Copy-Item "src/App.vue" "src/AppOld.vue" -Force
    Write-Host "✅ App.vue بکاپ شد" -ForegroundColor Green
}

# بکاپ فایل‌های views
$files = @("Home", "About", "News", "Events", "Services")
foreach ($file in $files) {
    $sourcePath = "src/views/$file.vue"
    $backupPath = "src/views/${file}Old.vue"
    
    if (Test-Path $sourcePath) {
        Copy-Item $sourcePath $backupPath -Force
        Write-Host "✅ $file.vue بکاپ شد" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "🔄 فعال‌سازی دیزاین جدید..." -ForegroundColor Yellow

# جایگزینی App.vue
if (Test-Path "src/AppNew.vue") {
    Copy-Item "src/AppNew.vue" "src/App.vue" -Force
    Write-Host "✅ App.vue جدید فعال شد" -ForegroundColor Green
} else {
    Write-Host "⚠️  AppNew.vue یافت نشد!" -ForegroundColor Red
}

# جایگزینی فایل‌های views
foreach ($file in $files) {
    $newPath = "src/views/${file}New.vue"
    $targetPath = "src/views/$file.vue"
    
    if (Test-Path $newPath) {
        Copy-Item $newPath $targetPath -Force
        Write-Host "✅ $file.vue جدید فعال شد" -ForegroundColor Green
    } else {
        Write-Host "⚠️  ${file}New.vue یافت نشد!" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "✨ جابجایی با موفقیت انجام شد!" -ForegroundColor Green
Write-Host ""
Write-Host "📝 نکات مهم:" -ForegroundColor Cyan
Write-Host "1. فایل‌های قدیمی با پسوند 'Old' ذخیره شده‌اند"
Write-Host "2. برای برگشت، از اسکریپت switch-to-old-design.ps1 استفاده کنید"
Write-Host "3. پروژه را با 'npm run dev' اجرا کنید"
Write-Host ""
