<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <!-- Header Section -->
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary w-fit">
            <span class="material-symbols-outlined text-[20px]">help</span>
            راهنمای سایت
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">راهنمای استفاده از سایت</h1>
          <p class="text-lg text-slate-600 dark:text-slate-400 max-w-2xl">راهنمای کامل استفاده از امکانات و بخش‌های مختلف سایت انجمن</p>
        </div>

        <!-- Guide Sections -->
        <div class="grid grid-cols-1 gap-8">
          <!-- Getting Started -->
          <div class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-6 flex items-center gap-3">
              <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-blue-500/10">
                <span class="material-symbols-outlined text-blue-600 text-2xl">rocket_launch</span>
              </div>
              <h2 class="text-2xl font-bold">شروع کار</h2>
            </div>
            <div class="prose prose-slate max-w-none dark:prose-invert">
              <p class="leading-relaxed">
                سایت انجمن علمی ریه کودکان ایران یک پلتفرم جامع برای پزشکان، محققان و علاقه‌مندان به حوزه بیماری‌های تنفسی کودکان است. در این سایت می‌توانید:
              </p>
              <ul class="space-y-2">
                <li>به منابع آموزشی و علمی دسترسی داشته باشید</li>
                <li>در رویدادها و کنگره‌ها ثبت‌نام کنید</li>
                <li>آخرین اخبار و مقالات علمی را مطالعه کنید</li>
                <li>با اعضای انجمن ارتباط برقرار کنید</li>
              </ul>
            </div>
          </div>

          <!-- Main Sections -->
          <div class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-6 flex items-center gap-3">
              <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-emerald-500/10">
                <span class="material-symbols-outlined text-emerald-600 text-2xl">dashboard</span>
              </div>
              <h2 class="text-2xl font-bold">بخش‌های اصلی سایت</h2>
            </div>
            <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
              <div class="rounded-lg border border-slate-200 p-4 dark:border-slate-800">
                <div class="mb-2 flex items-center gap-2">
                  <span class="material-symbols-outlined text-primary">home</span>
                  <h3 class="font-bold">صفحه اصلی</h3>
                </div>
                <p class="text-sm text-slate-600 dark:text-slate-400">
                  نمای کلی از انجمن، آخرین اخبار و رویدادها
                </p>
              </div>

              <div class="rounded-lg border border-slate-200 p-4 dark:border-slate-800">
                <div class="mb-2 flex items-center gap-2">
                  <span class="material-symbols-outlined text-primary">info</span>
                  <h3 class="font-bold">درباره ما</h3>
                </div>
                <p class="text-sm text-slate-600 dark:text-slate-400">
                  تاریخچه، اهداف و فعالیت‌های انجمن
                </p>
              </div>

              <div class="rounded-lg border border-slate-200 p-4 dark:border-slate-800">
                <div class="mb-2 flex items-center gap-2">
                  <span class="material-symbols-outlined text-primary">school</span>
                  <h3 class="font-bold">آموزش</h3>
                </div>
                <p class="text-sm text-slate-600 dark:text-slate-400">
                  منابع آموزشی، کتاب‌ها و راهنماهای پزشکی
                </p>
              </div>

              <div class="rounded-lg border border-slate-200 p-4 dark:border-slate-800">
                <div class="mb-2 flex items-center gap-2">
                  <span class="material-symbols-outlined text-primary">article</span>
                  <h3 class="font-bold">انتشارات</h3>
                </div>
                <p class="text-sm text-slate-600 dark:text-slate-400">
                  مجلات، کتابچه کنگره‌ها و مقالات علمی
                </p>
              </div>

              <div class="rounded-lg border border-slate-200 p-4 dark:border-slate-800">
                <div class="mb-2 flex items-center gap-2">
                  <span class="material-symbols-outlined text-primary">event</span>
                  <h3 class="font-bold">رویدادها</h3>
                </div>
                <p class="text-sm text-slate-600 dark:text-slate-400">
                  کنگره‌ها، همایش‌ها و کارگاه‌های آموزشی
                </p>
              </div>

              <div class="rounded-lg border border-slate-200 p-4 dark:border-slate-800">
                <div class="mb-2 flex items-center gap-2">
                  <span class="material-symbols-outlined text-primary">groups</span>
                  <h3 class="font-bold">اعضا</h3>
                </div>
                <p class="text-sm text-slate-600 dark:text-slate-400">
                  لیست اعضای انجمن و هیئت مدیره
                </p>
              </div>
            </div>
          </div>

          <!-- How to Register -->
          <div class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-6 flex items-center gap-3">
              <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-purple-500/10">
                <span class="material-symbols-outlined text-purple-600 text-2xl">person_add</span>
              </div>
              <h2 class="text-2xl font-bold">نحوه ثبت‌نام</h2>
            </div>
            <div class="prose prose-slate max-w-none dark:prose-invert">
              <p class="leading-relaxed mb-4">
                برای ثبت‌نام در رویدادها و استفاده از امکانات ویژه، مراحل زیر را دنبال کنید:
              </p>
              <ol class="space-y-3">
                <li>روی دکمه "ثبت‌نام" در منوی بالای سایت کلیک کنید</li>
                <li>فرم ثبت‌نام را با اطلاعات صحیح تکمیل کنید</li>
                <li>ایمیل تأیید را چک کنید و لینک فعال‌سازی را کلیک کنید</li>
                <li>با نام کاربری و رمز عبور خود وارد شوید</li>
                <li>پروفایل خود را تکمیل کنید</li>
              </ol>
            </div>
          </div>

          <!-- Download Resources -->
          <div class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-6 flex items-center gap-3">
              <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-orange-500/10">
                <span class="material-symbols-outlined text-orange-600 text-2xl">download</span>
              </div>
              <h2 class="text-2xl font-bold">دانلود منابع</h2>
            </div>
            <div class="prose prose-slate max-w-none dark:prose-invert">
              <p class="leading-relaxed mb-4">
                برای دانلود کتاب‌ها، مقالات و سایر منابع:
              </p>
              <ul class="space-y-2">
                <li>به بخش "آموزش" یا "انتشارات" بروید</li>
                <li>دسته‌بندی مورد نظر را انتخاب کنید</li>
                <li>روی دکمه "دانلود" کنار هر فایل کلیک کنید</li>
                <li>فایل به صورت خودکار دانلود می‌شود</li>
              </ul>
            </div>
          </div>

          <!-- Contact Support -->
          <div class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-6 flex items-center gap-3">
              <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-red-500/10">
                <span class="material-symbols-outlined text-red-600 text-2xl">support_agent</span>
              </div>
              <h2 class="text-2xl font-bold">پشتیبانی</h2>
            </div>
            <div class="prose prose-slate max-w-none dark:prose-invert">
              <p class="leading-relaxed mb-4">
                در صورت بروز مشکل یا نیاز به راهنمایی:
              </p>
              <ul class="space-y-2">
                <li>از بخش "تماس با ما" پیام ارسال کنید</li>
                <li>با شماره تلفن 09013684856 تماس بگیرید</li>
                <li>ایمیل خود را به info@irspp.ir ارسال کنید</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- FAQ Section -->
        <div class="mt-16 rounded-xl border border-primary/20 bg-primary/5 p-8 dark:bg-primary/10">
          <div class="mb-6 text-center">
            <h2 class="mb-2 text-2xl font-bold">سوالات متداول</h2>
            <p class="text-slate-600 dark:text-slate-400">پاسخ سوالات رایج کاربران</p>
          </div>
          <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
            <div class="rounded-lg border border-slate-200 bg-white p-4 dark:border-slate-800 dark:bg-slate-900">
              <h3 class="mb-2 font-bold">آیا ثبت‌نام در سایت رایگان است؟</h3>
              <p class="text-sm text-slate-600 dark:text-slate-400">
                بله، ثبت‌نام در سایت کاملاً رایگان است.
              </p>
            </div>
            <div class="rounded-lg border border-slate-200 bg-white p-4 dark:border-slate-800 dark:bg-slate-900">
              <h3 class="mb-2 font-bold">چگونه می‌توانم عضو انجمن شوم؟</h3>
              <p class="text-sm text-slate-600 dark:text-slate-400">
                از طریق بخش "تماس با ما" درخواست عضویت خود را ارسال کنید.
              </p>
            </div>
            <div class="rounded-lg border border-slate-200 bg-white p-4 dark:border-slate-800 dark:bg-slate-900">
              <h3 class="mb-2 font-bold">آیا منابع آموزشی رایگان هستند؟</h3>
              <p class="text-sm text-slate-600 dark:text-slate-400">
                بله، تمام منابع آموزشی به صورت رایگان در دسترس است.
              </p>
            </div>
            <div class="rounded-lg border border-slate-200 bg-white p-4 dark:border-slate-800 dark:bg-slate-900">
              <h3 class="mb-2 font-bold">چگونه در کنگره‌ها شرکت کنم؟</h3>
              <p class="text-sm text-slate-600 dark:text-slate-400">
                از بخش "رویدادها" رویداد مورد نظر را انتخاب و ثبت‌نام کنید.
              </p>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
