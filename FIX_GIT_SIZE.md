# راهنمای رفع مشکل حجم بالا در Git

## مشکل
حجم Git commit خیلی بالا رفته (12+ MB) به دلیل commit شدن فایل‌های بزرگ.

## علت
فایل‌های زیر در Git track شده‌اند:
1. فایل‌های PDF در `frontend/public/Content/` (کتاب‌ها، بروشورها)
2. فایل‌های تصویر و docx در `frontend/public/Content/`
3. ممکن است `node_modules` یا `dist` هم track شده باشند

## راه حل

### مرحله 1: حذف فایل‌های بزرگ از Git (بدون حذف از سیستم)

```bash
# حذف فایل‌های PDF از Git tracking
git rm --cached frontend/public/Content/**/*.pdf

# حذف فایل‌های تصویر
git rm --cached frontend/public/Content/**/*.jpg
git rm --cached frontend/public/Content/**/*.jpeg
git rm --cached frontend/public/Content/**/*.png

# حذف فایل‌های docx
git rm --cached frontend/public/Content/**/*.docx
git rm --cached frontend/public/Content/**/*.doc

# اگر dist یا node_modules track شده باشند:
git rm -r --cached frontend/dist
git rm -r --cached frontend/node_modules
```

### مرحله 2: اطمینان از .gitignore

`.gitignore` به‌روزرسانی شده است تا این فایل‌ها ignore شوند:

```
# Frontend Build Files
frontend/dist/
frontend/.vite/
frontend/.cache/
frontend/build/
frontend/node_modules/

# Large Content Files
frontend/public/Content/**/*.pdf
frontend/public/Content/**/*.jpg
frontend/public/Content/**/*.jpeg
frontend/public/Content/**/*.png
frontend/public/Content/**/*.docx
frontend/public/Content/**/*.doc
```

### مرحله 3: Commit تغییرات

```bash
git add .gitignore
git commit -m "Remove large files from Git and update .gitignore"
```

### مرحله 4: Push

```bash
git push
```

## نکات مهم

1. **فایل‌های Content**: این فایل‌ها باید در سرور باشند اما در Git نباشند. می‌توانید آن‌ها را روی سرور مستقیماً آپلود کنید.

2. **node_modules**: همیشه باید ignore شود - هرگز در Git commit نکنید.

3. **dist**: فایل‌های build شده باید ignore شوند و در سرور با `npm run build` ساخته شوند.

4. **فایل‌های بزرگ موجود**: اگر فایل‌های بزرگ در history Git هستند، باید از Git history حذف شوند (این کار پیچیده است).

## برای فایل‌های Content

اگر می‌خواهید فایل‌های Content را نگه دارید اما در Git نباشند:

1. فایل‌ها را از Git حذف کنید (با `git rm --cached`)
2. آن‌ها را در `.gitignore` اضافه کنید
3. فایل‌ها را مستقیماً روی سرور آپلود کنید یا از یک storage جداگانه استفاده کنید

## بررسی حجم

```bash
# بررسی فایل‌های بزرگ در Git
git ls-files | xargs ls -lh | sort -k5 -hr | head -20

# بررسی حجم کل repository
du -sh .git
```

