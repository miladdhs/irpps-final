# 🔧 حل مشکل Build در Docker

## مشکل

```
error during build:
[vite:terser] terser not found. Since Vite v3, terser has become an optional dependency.
```

## راه حل 1: استفاده از esbuild (توصیه می‌شود) ✅

فایل `vite.config.ts` بروزرسانی شد:

```typescript
build: {
  minify: 'esbuild', // به جای 'terser'
}
```

**مزایا:**
- سریعتر از terser
- بدون نیاز به نصب جداگانه
- کمتر حجم می‌گیرد

**اجرا:**
```bash
docker-compose build frontend
docker-compose up -d
```

---

## راه حل 2: نصب terser (اگر راه حل 1 کار نکرد)

### گزینه A: اضافه کردن به package.json

```bash
cd frontend
npm install --save-dev terser
```

یا مستقیماً به `package.json` اضافه کنید:

```json
{
  "devDependencies": {
    "@vitejs/plugin-vue": "^5.0.0",
    "autoprefixer": "^10.4.24",
    "postcss": "^8.5.6",
    "tailwindcss": "^3.4.19",
    "terser": "^5.31.0",
    "typescript": "^5.3.0",
    "vite": "^5.0.0",
    "vue-tsc": "^1.8.27"
  }
}
```

سپس:
```bash
docker-compose build frontend --no-cache
docker-compose up -d
```

### گزینه B: تغییر Dockerfile

اضافه کردن نصب terser به Dockerfile:

```dockerfile
# Install dependencies with fallback registry
RUN npm config set registry "https://archive.ito.gov.ir/npm/" && \
    npm install || ( \
        echo "Iranian registry failed, trying official npm registry..." && \
        npm config set registry "https://registry.npmjs.org/" && \
        npm install \
    )

# Install terser explicitly
RUN npm install --save-dev terser
```

---

## راه حل 3: غیرفعال کردن minify (فقط برای تست)

در `vite.config.ts`:

```typescript
build: {
  minify: false, // غیرفعال کردن minification
}
```

**توجه:** این روش برای production توصیه نمی‌شود چون فایل‌ها بزرگتر می‌شوند.

---

## بررسی Build موفق

بعد از build، بررسی کنید:

```bash
# بررسی لاگ‌ها
docker-compose logs frontend

# بررسی فایل‌های build شده
docker-compose exec frontend ls -la /usr/share/nginx/html/

# تست سایت
curl http://localhost/
```

---

## مقایسه minifiers

| Minifier | سرعت | حجم خروجی | نصب |
|----------|------|-----------|-----|
| esbuild | ⚡⚡⚡ سریع | خوب | پیش‌فرض |
| terser | 🐌 کند | عالی | نیاز به نصب |
| none | ⚡⚡⚡ سریع | بد | - |

**توصیه:** استفاده از `esbuild` برای تعادل بین سرعت و حجم.

---

## دستورات مفید

```bash
# پاک کردن cache و rebuild
docker-compose down
docker system prune -a
docker-compose build --no-cache
docker-compose up -d

# بررسی وضعیت
docker-compose ps
docker-compose logs -f frontend

# تست اتصال
./test-connection.sh
```

---

## نتیجه

✅ مشکل با تغییر `minify: 'terser'` به `minify: 'esbuild'` حل شد.

اگر هنوز مشکل دارید، راه حل 2 را امتحان کنید.
