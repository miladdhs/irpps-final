<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1024px] grow px-6 py-8 lg:px-10">
        <!-- Breadcrumb -->
        <nav class="mb-6 flex items-center gap-2 text-sm text-slate-500">
          <router-link to="/" class="hover:text-primary">{{ $t('nav.home') }}</router-link>
          <span class="material-symbols-outlined text-[16px]">chevron_left</span>
          <router-link to="/news" class="hover:text-primary">{{ $t('nav.news') }}</router-link>
          <span class="material-symbols-outlined text-[16px]">chevron_left</span>
          <span class="text-slate-900 dark:text-white">جزئیات خبر</span>
        </nav>

        <!-- Article Header -->
        <article class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
          <div class="mb-6">
            <div class="mb-4 inline-block rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary">
              مقاله علمی
            </div>
            <h1 class="mb-4 text-3xl font-black leading-tight md:text-4xl">
              تازه‌های درمان آسم در کودکان: پروتکل‌های سال ۲۰۲۴
            </h1>
            <div class="flex flex-wrap items-center gap-4 text-sm text-slate-500">
              <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[18px]">person</span>
                <span>دکتر محمد رضایی</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[18px]">calendar_today</span>
                <span>۱۵ آبان ۱۴۰۲</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[18px]">visibility</span>
                <span>۱,۲۳۴ بازدید</span>
              </div>
            </div>
          </div>

          <!-- Featured Image -->
          <div class="mb-8 aspect-video overflow-hidden rounded-xl bg-slate-100 dark:bg-slate-800">
            <img 
              src="/img/logo.png" 
              alt="تازه‌های درمان آسم" 
              class="h-full w-full object-contain p-8"
            />
          </div>

          <!-- Article Content -->
          <div class="prose prose-slate max-w-none dark:prose-invert">
            <p class="lead text-lg leading-relaxed text-slate-600 dark:text-slate-400">
              مروری بر جدیدترین پروتکل‌های درمانی ارائه شده در سال ۲۰۲۴ برای مدیریت آسم در اطفال و روش‌های نوین استفاده از اسپری‌های ترکیبی که توسط سازمان بهداشت جهانی تأیید شده است.
            </p>

            <h2 class="mt-8 mb-4 text-2xl font-bold">مقدمه</h2>
            <p class="leading-relaxed">
              آسم یکی از شایع‌ترین بیماری‌های مزمن دوران کودکی است که بر کیفیت زندگی کودکان و خانواده‌های آنها تأثیر قابل توجهی دارد. با پیشرفت علم پزشکی و تحقیقات گسترده در این زمینه، پروتکل‌های درمانی جدیدی برای مدیریت بهتر این بیماری ارائه شده است.
            </p>

            <h2 class="mt-8 mb-4 text-2xl font-bold">پروتکل‌های جدید درمانی</h2>
            <p class="leading-relaxed">
              در سال ۲۰۲۴، سازمان بهداشت جهانی (WHO) و انجمن بین‌المللی آسم (GINA) راهنماهای به‌روز شده‌ای را برای درمان آسم در کودکان منتشر کردند. این راهنماها بر اساس آخرین یافته‌های علمی و تجربیات بالینی تدوین شده‌اند.
            </p>

            <h3 class="mt-6 mb-3 text-xl font-bold">نکات کلیدی:</h3>
            <ul class="list-disc pr-6 space-y-2">
              <li>استفاده از اسپری‌های ترکیبی ICS-LABA به عنوان خط اول درمان</li>
              <li>تأکید بر آموزش صحیح تکنیک استفاده از اسپری به کودکان و والدین</li>
              <li>پایش منظم عملکرد ریوی با اسپیرومتری</li>
              <li>شناسایی و کنترل عوامل محرک محیطی</li>
              <li>برنامه‌ریزی برای مدیریت حملات حاد</li>
            </ul>

            <h2 class="mt-8 mb-4 text-2xl font-bold">نتیجه‌گیری</h2>
            <p class="leading-relaxed">
              با پیروی از پروتکل‌های جدید و استفاده از روش‌های درمانی به‌روز، می‌توان کنترل بهتری بر آسم کودکان داشت و کیفیت زندگی آنها را به طور قابل توجهی بهبود بخشید.
            </p>
          </div>

          <!-- Tags -->
          <div class="mt-8 flex flex-wrap gap-2 border-t border-slate-200 pt-6 dark:border-slate-800">
            <span class="rounded-full bg-slate-100 px-4 py-2 text-sm font-medium dark:bg-slate-800">آسم</span>
            <span class="rounded-full bg-slate-100 px-4 py-2 text-sm font-medium dark:bg-slate-800">کودکان</span>
            <span class="rounded-full bg-slate-100 px-4 py-2 text-sm font-medium dark:bg-slate-800">درمان</span>
            <span class="rounded-full bg-slate-100 px-4 py-2 text-sm font-medium dark:bg-slate-800">پروتکل</span>
          </div>

          <!-- Share -->
          <div class="mt-6 flex items-center gap-4 border-t border-slate-200 pt-6 dark:border-slate-800">
            <span class="font-medium">اشتراک‌گذاری:</span>
            <button class="flex h-10 w-10 items-center justify-center rounded-full bg-slate-100 hover:bg-primary hover:text-white transition-colors dark:bg-slate-800">
              <span class="material-symbols-outlined text-[20px]">share</span>
            </button>
          </div>
        </article>

        <!-- Related News -->
        <div class="mt-12">
          <h2 class="mb-6 text-2xl font-bold">اخبار مرتبط</h2>
          <div class="grid grid-cols-1 gap-6 md:grid-cols-3">
            <router-link 
              to="/news/related"
              class="group rounded-xl border border-slate-200 bg-white p-4 shadow-sm transition-all hover:shadow-lg hover:border-primary/30 dark:border-slate-800 dark:bg-slate-900"
            >
              <div class="mb-3 aspect-video overflow-hidden rounded-lg bg-slate-100 dark:bg-slate-800">
                <img 
                  src="/img/logo.png" 
                  alt="خبر مرتبط" 
                  class="h-full w-full object-contain p-4 transition-transform group-hover:scale-110"
                />
              </div>
              <h3 class="mb-2 font-bold line-clamp-2 group-hover:text-primary">عنوان خبر مرتبط شماره 1</h3>
              <p class="text-sm text-slate-500">۱۰ آبان ۱۴۰۲</p>
            </router-link>
            <router-link 
              to="/news/related"
              class="group rounded-xl border border-slate-200 bg-white p-4 shadow-sm transition-all hover:shadow-lg hover:border-primary/30 dark:border-slate-800 dark:bg-slate-900"
            >
              <div class="mb-3 aspect-video overflow-hidden rounded-lg bg-slate-100 dark:bg-slate-800">
                <img 
                  src="/img/logo.png" 
                  alt="خبر مرتبط" 
                  class="h-full w-full object-contain p-4 transition-transform group-hover:scale-110"
                />
              </div>
              <h3 class="mb-2 font-bold line-clamp-2 group-hover:text-primary">عنوان خبر مرتبط شماره 2</h3>
              <p class="text-sm text-slate-500">۱۰ آبان ۱۴۰۲</p>
            </router-link>
            <router-link 
              to="/news/related"
              class="group rounded-xl border border-slate-200 bg-white p-4 shadow-sm transition-all hover:shadow-lg hover:border-primary/30 dark:border-slate-800 dark:bg-slate-900"
            >
              <div class="mb-3 aspect-video overflow-hidden rounded-lg bg-slate-100 dark:bg-slate-800">
                <img 
                  src="/img/logo.png" 
                  alt="خبر مرتبط" 
                  class="h-full w-full object-contain p-4 transition-transform group-hover:scale-110"
                />
              </div>
              <h3 class="mb-2 font-bold line-clamp-2 group-hover:text-primary">عنوان خبر مرتبط شماره 3</h3>
              <p class="text-sm text-slate-500">۱۰ آبان ۱۴۰۲</p>
            </router-link>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
