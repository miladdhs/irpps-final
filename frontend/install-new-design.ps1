# اسکریپت نصب دیزاین جدید برای Windows PowerShell

Write-Host "🚀 شروع نصب دیزاین جدید..." -ForegroundColor Green

# نصب پکیج‌های مورد نیاز
Write-Host "📦 نصب Tailwind CSS و وابستگی‌ها..." -ForegroundColor Yellow
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest

# نصب سایر پکیج‌ها
Write-Host "📦 نصب پکیج‌های پروژه..." -ForegroundColor Yellow
npm install

# بکاپ فایل‌های قدیمی
Write-Host "💾 ایجاد بکاپ از فایل‌های قدیمی..." -ForegroundColor Yellow
if (Test-Path "src/App.vue") {
    Copy-Item "src/App.vue" "src/AppOld.vue"
    Write-Host "✅ App.vue بکاپ شد" -ForegroundColor Green
}

if (Test-Path "src/views/Home.vue") {
    Copy-Item "src/views/Home.vue" "src/views/HomeOld.vue"
    Write-Host "✅ Home.vue بکاپ شد" -ForegroundColor Green
}

# فعال‌سازی فایل‌های جدید
Write-Host "🔄 فعال‌سازی دیزاین جدید..." -ForegroundColor Yellow
if (Test-Path "src/AppNew.vue") {
    Copy-Item "src/AppNew.vue" "src/App.vue" -Force
    Write-Host "✅ App.vue جدید فعال شد" -ForegroundColor Green
}

if (Test-Path "src/views/HomeNew.vue") {
    Copy-Item "src/views/HomeNew.vue" "src/views/Home.vue" -Force
    Write-Host "✅ Home.vue جدید فعال شد" -ForegroundColor Green
}

Write-Host ""
Write-Host "✨ نصب با موفقیت انجام شد!" -ForegroundColor Green
Write-Host ""
Write-Host "📝 مراحل بعدی:" -ForegroundColor Cyan
Write-Host "1. npm run dev - برای اجرای پروژه"
Write-Host "2. مشاهده فایل NEW_DESIGN_MIGRATION.md برای ادامه کار"
Write-Host ""
