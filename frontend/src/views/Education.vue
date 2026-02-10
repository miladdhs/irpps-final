<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <!-- Header Section -->
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary w-fit">
            <span class="material-symbols-outlined text-[20px]">school</span>
            آموزش
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">محتوای آموزشی</h1>
          <p class="text-lg text-slate-600 dark:text-slate-400 max-w-2xl">دسترسی به منابع آموزشی، کتاب‌ها و محتوای علمی تخصصی</p>
        </div>

        <!-- Education Categories Grid -->
        <div class="grid grid-cols-1 gap-6 lg:grid-cols-2">
          <!-- Doctors Resources -->
          <router-link 
            to="/education/doctors"
            class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-blue-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-primary/30 dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute top-0 right-0 h-32 w-32 translate-x-8 -translate-y-8 rounded-full bg-primary/5 blur-3xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-primary to-blue-600 shadow-lg shadow-primary/30 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-5xl text-white">medical_services</span>
              </div>
              <h2 class="mb-3 text-2xl font-black">منابع و محتوای پزشکی</h2>
              <p class="mb-6 leading-relaxed text-slate-600 dark:text-slate-400">
                دسترسی به کتاب‌های آموزشی، راهنماهای بالینی و محتوای علمی تخصصی برای پزشکان
              </p>
              
              <!-- Features Grid -->
              <div class="mb-6 grid grid-cols-2 gap-3">
                <div class="flex items-center gap-2 rounded-lg bg-white/50 px-3 py-2 dark:bg-slate-800/50">
                  <span class="material-symbols-outlined text-primary text-[20px]">menu_book</span>
                  <span class="text-sm font-medium">19 کتاب</span>
                </div>
                <div class="flex items-center gap-2 rounded-lg bg-white/50 px-3 py-2 dark:bg-slate-800/50">
                  <span class="material-symbols-outlined text-primary text-[20px]">category</span>
                  <span class="text-sm font-medium">7 دسته</span>
                </div>
                <div class="flex items-center gap-2 rounded-lg bg-white/50 px-3 py-2 dark:bg-slate-800/50">
                  <span class="material-symbols-outlined text-primary text-[20px]">download</span>
                  <span class="text-sm font-medium">دانلود رایگان</span>
                </div>
                <div class="flex items-center gap-2 rounded-lg bg-white/50 px-3 py-2 dark:bg-slate-800/50">
                  <span class="material-symbols-outlined text-primary text-[20px]">update</span>
                  <span class="text-sm font-medium">به‌روز 2025</span>
                </div>
              </div>

              <!-- Topics -->
              <div class="mb-6 flex flex-wrap gap-2">
                <span class="rounded-full bg-primary/10 px-3 py-1 text-xs font-bold text-primary">IMCI</span>
                <span class="rounded-full bg-primary/10 px-3 py-1 text-xs font-bold text-primary">IMNCI</span>
                <span class="rounded-full bg-primary/10 px-3 py-1 text-xs font-bold text-primary">GINA</span>
                <span class="rounded-full bg-primary/10 px-3 py-1 text-xs font-bold text-primary">واکسیناسیون</span>
                <span class="rounded-full bg-primary/10 px-3 py-1 text-xs font-bold text-primary">تکامل کودک</span>
              </div>

              <div class="flex items-center gap-2 text-primary font-bold group-hover:gap-3 transition-all">
                <span>مشاهده منابع</span>
                <span class="material-symbols-outlined">arrow_back</span>
              </div>
            </div>
          </router-link>

          <!-- Parents Guide -->
          <div class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-emerald-50 to-white p-8 shadow-sm dark:border-slate-800 dark:from-slate-900 dark:to-slate-900">
            <div class="absolute top-0 right-0 h-32 w-32 translate-x-8 -translate-y-8 rounded-full bg-emerald-500/5 blur-3xl"></div>
            <div class="relative">
              <div class="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-emerald-500 to-green-600 shadow-lg shadow-emerald-500/30">
                <span class="material-symbols-outlined text-5xl text-white">family_restroom</span>
              </div>
              <h2 class="mb-3 text-2xl font-black">همراه والدین</h2>
              <p class="mb-6 leading-relaxed text-slate-600 dark:text-slate-400">
                آموزش و راهنمایی برای خانواده‌های کودکان مبتلا به بیماری‌های ریوی و تنفسی
              </p>
              
              <!-- Features Grid -->
              <div class="mb-6 grid grid-cols-2 gap-3">
                <div class="flex items-center gap-2 rounded-lg bg-white/50 px-3 py-2 dark:bg-slate-800/50">
                  <span class="material-symbols-outlined text-emerald-600 text-[20px]">health_and_safety</span>
                  <span class="text-sm font-medium">راهنمای مراقبت</span>
                </div>
                <div class="flex items-center gap-2 rounded-lg bg-white/50 px-3 py-2 dark:bg-slate-800/50">
                  <span class="material-symbols-outlined text-emerald-600 text-[20px]">restaurant</span>
                  <span class="text-sm font-medium">نکات تغذیه</span>
                </div>
                <div class="flex items-center gap-2 rounded-lg bg-white/50 px-3 py-2 dark:bg-slate-800/50">
                  <span class="material-symbols-outlined text-emerald-600 text-[20px]">quiz</span>
                  <span class="text-sm font-medium">پرسش و پاسخ</span>
                </div>
                <div class="flex items-center gap-2 rounded-lg bg-white/50 px-3 py-2 dark:bg-slate-800/50">
                  <span class="material-symbols-outlined text-emerald-600 text-[20px]">video_library</span>
                  <span class="text-sm font-medium">ویدیوهای آموزشی</span>
                </div>
              </div>

              <div class="inline-flex items-center gap-2 rounded-full bg-emerald-500/10 px-4 py-2 text-sm font-bold text-emerald-600">
                <span class="material-symbols-outlined text-[18px]">schedule</span>
                به زودی
              </div>
            </div>
          </div>
        </div>

        <!-- Additional Resources -->
        <div class="mt-8 grid grid-cols-1 gap-6 md:grid-cols-3">
          <!-- Video Tutorials -->
          <div class="group rounded-xl border border-slate-200 bg-white p-6 shadow-sm transition-all hover:shadow-lg hover:border-purple-300 dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-4 flex h-14 w-14 items-center justify-center rounded-xl bg-purple-500/10 transition-transform group-hover:scale-110">
              <span class="material-symbols-outlined text-purple-600 text-3xl">play_circle</span>
            </div>
            <h3 class="mb-2 text-lg font-bold">ویدیوهای آموزشی</h3>
            <p class="mb-4 text-sm text-slate-600 dark:text-slate-400">
              دسترسی به ویدیوهای آموزشی و وبینارهای علمی
            </p>
            <div class="inline-flex items-center gap-2 rounded-full bg-amber-500/10 px-3 py-1 text-xs font-bold text-amber-600">
              <span class="material-symbols-outlined text-[16px]">schedule</span>
              به زودی
            </div>
          </div>

          <!-- Slides & Presentations -->
          <div class="group rounded-xl border border-slate-200 bg-white p-6 shadow-sm transition-all hover:shadow-lg hover:border-orange-300 dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-4 flex h-14 w-14 items-center justify-center rounded-xl bg-orange-500/10 transition-transform group-hover:scale-110">
              <span class="material-symbols-outlined text-orange-600 text-3xl">slideshow</span>
            </div>
            <h3 class="mb-2 text-lg font-bold">اسلایدها و ارائه‌ها</h3>
            <p class="mb-4 text-sm text-slate-600 dark:text-slate-400">
              اسلایدهای علمی کنگره‌ها و همایش‌ها
            </p>
            <div class="inline-flex items-center gap-2 rounded-full bg-amber-500/10 px-3 py-1 text-xs font-bold text-amber-600">
              <span class="material-symbols-outlined text-[16px]">schedule</span>
              به زودی
            </div>
          </div>

          <!-- Online Courses -->
          <div class="group rounded-xl border border-slate-200 bg-white p-6 shadow-sm transition-all hover:shadow-lg hover:border-pink-300 dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-4 flex h-14 w-14 items-center justify-center rounded-xl bg-pink-500/10 transition-transform group-hover:scale-110">
              <span class="material-symbols-outlined text-pink-600 text-3xl">cast_for_education</span>
            </div>
            <h3 class="mb-2 text-lg font-bold">دوره‌های آنلاین</h3>
            <p class="mb-4 text-sm text-slate-600 dark:text-slate-400">
              دوره‌های آموزشی تخصصی آنلاین
            </p>
            <div class="inline-flex items-center gap-2 rounded-full bg-amber-500/10 px-3 py-1 text-xs font-bold text-amber-600">
              <span class="material-symbols-outlined text-[16px]">schedule</span>
              به زودی
            </div>
          </div>
        </div>

        <!-- Stats Section -->
        <div class="mt-16 grid grid-cols-2 gap-6 md:grid-cols-4">
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">menu_book</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">19+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">کتاب آموزشی</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">play_circle</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">50+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">ویدیوی آموزشی</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">slideshow</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">100+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">اسلاید علمی</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">groups</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">1000+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">کاربر فعال</div>
          </div>
        </div>

        <!-- CTA Section -->
        <div class="mt-16 rounded-2xl border border-primary/20 bg-gradient-to-br from-primary/5 to-blue-500/5 p-8 dark:from-primary/10 dark:to-blue-500/10">
          <div class="flex flex-col items-center gap-6 text-center md:flex-row md:text-right">
            <div class="flex h-20 w-20 shrink-0 items-center justify-center rounded-2xl bg-gradient-to-br from-primary to-blue-600 text-white shadow-lg shadow-primary/30">
              <span class="material-symbols-outlined text-5xl">info</span>
            </div>
            <div class="flex-1">
              <h3 class="mb-2 text-2xl font-black">نیاز به راهنمایی دارید؟</h3>
              <p class="text-slate-600 dark:text-slate-400">
                برای دریافت اطلاعات بیشتر درباره دوره‌های آموزشی و منابع علمی، با ما تماس بگیرید
              </p>
            </div>
            <router-link 
              to="/contact"
              class="rounded-xl bg-primary px-8 py-4 font-bold text-white shadow-lg shadow-primary/30 transition-all hover:bg-primary/90 hover:shadow-xl"
            >
              تماس با ما
            </router-link>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
