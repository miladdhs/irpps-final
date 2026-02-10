<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <!-- Header Section -->
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary w-fit">
            <span class="material-symbols-outlined text-[20px]">campaign</span>
            تبلیغات
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">فرصت‌های تبلیغاتی</h1>
          <p class="text-lg text-slate-600 dark:text-slate-400 max-w-2xl">فرصت‌های تبلیغاتی و همکاری با انجمن علمی ریه کودکان ایران</p>
        </div>

        <!-- Advertising Options Grid -->
        <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          <!-- Website Advertising -->
          <div class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-blue-50 to-white p-8 shadow-sm transition-all hover:shadow-xl hover:border-blue-300 dark:border-slate-800 dark:from-slate-900 dark:to-slate-900">
            <div class="absolute top-0 right-0 h-24 w-24 translate-x-6 -translate-y-6 rounded-full bg-blue-500/5 blur-2xl"></div>
            <div class="relative">
              <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-xl bg-gradient-to-br from-blue-500 to-blue-600 shadow-lg shadow-blue-500/20 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-white text-4xl">web</span>
              </div>
              <h3 class="mb-3 text-xl font-black">تبلیغات در وب‌سایت</h3>
              <p class="mb-6 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                نمایش تبلیغات شما در صفحات مختلف وب‌سایت انجمن با بازدید بالا
              </p>
              <ul class="space-y-2 text-sm">
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-blue-600 text-[18px]">check_circle</span>
                  <span>بازدید ماهانه بالا</span>
                </li>
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-blue-600 text-[18px]">check_circle</span>
                  <span>مخاطبان تخصصی</span>
                </li>
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-blue-600 text-[18px]">check_circle</span>
                  <span>موقعیت‌های متنوع</span>
                </li>
              </ul>
            </div>
          </div>

          <!-- Congress Advertising -->
          <div class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-emerald-50 to-white p-8 shadow-sm transition-all hover:shadow-xl hover:border-emerald-300 dark:border-slate-800 dark:from-slate-900 dark:to-slate-900">
            <div class="absolute top-0 right-0 h-24 w-24 translate-x-6 -translate-y-6 rounded-full bg-emerald-500/5 blur-2xl"></div>
            <div class="relative">
              <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-xl bg-gradient-to-br from-emerald-500 to-green-600 shadow-lg shadow-emerald-500/20 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-white text-4xl">event</span>
              </div>
              <h3 class="mb-3 text-xl font-black">تبلیغات در کنگره‌ها</h3>
              <p class="mb-6 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                حضور برند شما در کنگره‌ها و همایش‌های علمی انجمن
              </p>
              <ul class="space-y-2 text-sm">
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-emerald-600 text-[18px]">check_circle</span>
                  <span>غرفه نمایشگاهی</span>
                </li>
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-emerald-600 text-[18px]">check_circle</span>
                  <span>بنر و پوستر</span>
                </li>
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-emerald-600 text-[18px]">check_circle</span>
                  <span>اسپانسرشیپ</span>
                </li>
              </ul>
            </div>
          </div>

          <!-- Publication Advertising -->
          <div class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-purple-50 to-white p-8 shadow-sm transition-all hover:shadow-xl hover:border-purple-300 dark:border-slate-800 dark:from-slate-900 dark:to-slate-900">
            <div class="absolute top-0 right-0 h-24 w-24 translate-x-6 -translate-y-6 rounded-full bg-purple-500/5 blur-2xl"></div>
            <div class="relative">
              <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-xl bg-gradient-to-br from-purple-500 to-purple-600 shadow-lg shadow-purple-500/20 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-white text-4xl">article</span>
              </div>
              <h3 class="mb-3 text-xl font-black">تبلیغات در انتشارات</h3>
              <p class="mb-6 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                درج تبلیغات در مجلات، خبرنامه‌ها و کتابچه‌های انجمن
              </p>
              <ul class="space-y-2 text-sm">
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-purple-600 text-[18px]">check_circle</span>
                  <span>مجله علمی</span>
                </li>
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-purple-600 text-[18px]">check_circle</span>
                  <span>خبرنامه</span>
                </li>
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-purple-600 text-[18px]">check_circle</span>
                  <span>کتابچه کنگره</span>
                </li>
              </ul>
            </div>
          </div>

          <!-- Email Marketing -->
          <div class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-orange-50 to-white p-8 shadow-sm transition-all hover:shadow-xl hover:border-orange-300 dark:border-slate-800 dark:from-slate-900 dark:to-slate-900">
            <div class="absolute top-0 right-0 h-24 w-24 translate-x-6 -translate-y-6 rounded-full bg-orange-500/5 blur-2xl"></div>
            <div class="relative">
              <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-xl bg-gradient-to-br from-orange-500 to-orange-600 shadow-lg shadow-orange-500/20 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-white text-4xl">mail</span>
              </div>
              <h3 class="mb-3 text-xl font-black">ایمیل مارکتینگ</h3>
              <p class="mb-6 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                ارسال پیام تبلیغاتی به اعضای انجمن از طریق ایمیل
              </p>
              <ul class="space-y-2 text-sm">
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-orange-600 text-[18px]">check_circle</span>
                  <span>دسترسی مستقیم</span>
                </li>
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-orange-600 text-[18px]">check_circle</span>
                  <span>مخاطبان هدفمند</span>
                </li>
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-orange-600 text-[18px]">check_circle</span>
                  <span>گزارش عملکرد</span>
                </li>
              </ul>
            </div>
          </div>

          <!-- Social Media -->
          <div class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-pink-50 to-white p-8 shadow-sm transition-all hover:shadow-xl hover:border-pink-300 dark:border-slate-800 dark:from-slate-900 dark:to-slate-900">
            <div class="absolute top-0 right-0 h-24 w-24 translate-x-6 -translate-y-6 rounded-full bg-pink-500/5 blur-2xl"></div>
            <div class="relative">
              <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-xl bg-gradient-to-br from-pink-500 to-pink-600 shadow-lg shadow-pink-500/20 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-white text-4xl">share</span>
              </div>
              <h3 class="mb-3 text-xl font-black">شبکه‌های اجتماعی</h3>
              <p class="mb-6 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                تبلیغات در کانال‌ها و صفحات اجتماعی انجمن
              </p>
              <ul class="space-y-2 text-sm">
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-pink-600 text-[18px]">check_circle</span>
                  <span>پست‌های تبلیغاتی</span>
                </li>
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-pink-600 text-[18px]">check_circle</span>
                  <span>استوری</span>
                </li>
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-pink-600 text-[18px]">check_circle</span>
                  <span>دسترسی گسترده</span>
                </li>
              </ul>
            </div>
          </div>

          <!-- Custom Packages -->
          <div class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-amber-50 to-white p-8 shadow-sm transition-all hover:shadow-xl hover:border-amber-300 dark:border-slate-800 dark:from-slate-900 dark:to-slate-900">
            <div class="absolute top-0 right-0 h-24 w-24 translate-x-6 -translate-y-6 rounded-full bg-amber-500/5 blur-2xl"></div>
            <div class="relative">
              <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-xl bg-gradient-to-br from-amber-500 to-amber-600 shadow-lg shadow-amber-500/20 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-white text-4xl">package</span>
              </div>
              <h3 class="mb-3 text-xl font-black">پکیج‌های سفارشی</h3>
              <p class="mb-6 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                طراحی پکیج تبلیغاتی متناسب با نیاز شما
              </p>
              <ul class="space-y-2 text-sm">
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-amber-600 text-[18px]">check_circle</span>
                  <span>ترکیب روش‌ها</span>
                </li>
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-amber-600 text-[18px]">check_circle</span>
                  <span>قیمت ویژه</span>
                </li>
                <li class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-amber-600 text-[18px]">check_circle</span>
                  <span>مشاوره رایگان</span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Contact CTA -->
        <div class="mt-16 rounded-2xl border border-primary/20 bg-gradient-to-br from-primary/5 to-blue-500/5 p-8 lg:p-12 dark:from-primary/10 dark:to-blue-500/10">
          <div class="flex flex-col items-center gap-8 text-center lg:flex-row lg:text-right">
            <div class="flex h-20 w-20 shrink-0 items-center justify-center rounded-2xl bg-gradient-to-br from-primary to-blue-600 text-white shadow-lg shadow-primary/30">
              <span class="material-symbols-outlined text-5xl">contact_phone</span>
            </div>
            <div class="flex-1">
              <h3 class="mb-3 text-2xl font-black">برای اطلاعات بیشتر با ما تماس بگیرید</h3>
              <p class="mb-6 text-slate-600 dark:text-slate-400">
                تیم ما آماده است تا بهترین پکیج تبلیغاتی را متناسب با نیاز شما طراحی کند
              </p>
              <div class="flex flex-col gap-4 sm:flex-row sm:justify-center lg:justify-start">
                <router-link 
                  to="/contact"
                  class="flex items-center justify-center gap-2 rounded-xl bg-primary px-8 py-4 font-bold text-white shadow-lg shadow-primary/30 transition-all hover:bg-primary/90 hover:shadow-xl"
                >
                  <span class="material-symbols-outlined">mail</span>
                  <span>تماس با ما</span>
                </router-link>
                <a 
                  href="tel:09013684856"
                  class="flex items-center justify-center gap-2 rounded-xl border-2 border-primary bg-white px-8 py-4 font-bold text-primary transition-all hover:bg-primary/5 dark:bg-slate-900"
                >
                  <span class="material-symbols-outlined">call</span>
                  <span>09013684856</span>
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- Stats -->
        <div class="mt-16 grid grid-cols-2 gap-6 md:grid-cols-4">
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">visibility</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">10K+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">بازدید ماهانه</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">groups</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">500+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">عضو فعال</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">event</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">20+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">رویداد سالانه</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">trending_up</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">95%</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">رضایت مشتریان</div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
