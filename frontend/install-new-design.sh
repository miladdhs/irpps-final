#!/bin/bash

echo "🚀 شروع نصب دیزاین جدید..."

# نصب پکیج‌های مورد نیاز
echo "📦 نصب Tailwind CSS و وابستگی‌ها..."
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest

# نصب سایر پکیج‌ها
echo "📦 نصب پکیج‌های پروژه..."
npm install

# بکاپ فایل‌های قدیمی
echo "💾 ایجاد بکاپ از فایل‌های قدیمی..."
if [ -f "src/App.vue" ]; then
    cp src/App.vue src/AppOld.vue
    echo "✅ App.vue بکاپ شد"
fi

if [ -f "src/views/Home.vue" ]; then
    cp src/views/Home.vue src/views/HomeOld.vue
    echo "✅ Home.vue بکاپ شد"
fi

# فعال‌سازی فایل‌های جدید
echo "🔄 فعال‌سازی دیزاین جدید..."
if [ -f "src/AppNew.vue" ]; then
    cp src/AppNew.vue src/App.vue
    echo "✅ App.vue جدید فعال شد"
fi

if [ -f "src/views/HomeNew.vue" ]; then
    cp src/views/HomeNew.vue src/views/Home.vue
    echo "✅ Home.vue جدید فعال شد"
fi

echo ""
echo "✨ نصب با موفقیت انجام شد!"
echo ""
echo "📝 مراحل بعدی:"
echo "1. npm run dev - برای اجرای پروژه"
echo "2. مشاهده فایل NEW_DESIGN_MIGRATION.md برای ادامه کار"
echo ""
