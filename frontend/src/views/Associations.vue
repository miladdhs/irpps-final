<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <!-- Header Section -->
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary w-fit">
            <span class="material-symbols-outlined text-[20px]">public</span>
            انجمن‌های مرتبط
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">انجمن‌های وابسته و مرتبط</h1>
          <p class="text-lg text-slate-600 dark:text-slate-400 max-w-2xl">انجمن‌های ملی و بین‌المللی مرتبط با ریه کودکان و پزشکی اطفال</p>
        </div>

        <!-- Associations Grid -->
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
          <!-- Iranian Chest Society -->
          <a 
            href="https://chestnet.ir/fa" 
            target="_blank"
            class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-blue-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-blue-300 dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute top-0 right-0 h-32 w-32 translate-x-8 -translate-y-8 rounded-full bg-blue-500/5 blur-3xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-blue-500 to-blue-600 shadow-lg shadow-blue-500/30 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-5xl text-white">pulmonology</span>
              </div>
              <h2 class="mb-3 text-2xl font-black">انجمن ریه ایران</h2>
              <p class="mb-2 text-sm font-medium text-blue-600">مرجع تخصصی بیماری‌های ریوی در ایران</p>
              <p class="mb-6 leading-relaxed text-slate-600 dark:text-slate-400">
                انجمن علمی ریه ایران به عنوان مرجع تخصصی بیماری‌های ریوی، فعالیت‌های گسترده‌ای در زمینه آموزش، پژوهش و ارتقای سطح دانش پزشکان انجام می‌دهد.
              </p>
              <div class="mb-6 flex flex-wrap gap-2">
                <span class="rounded-full bg-blue-500/10 px-3 py-1 text-xs font-bold text-blue-600">آموزش</span>
                <span class="rounded-full bg-blue-500/10 px-3 py-1 text-xs font-bold text-blue-600">پژوهش</span>
                <span class="rounded-full bg-blue-500/10 px-3 py-1 text-xs font-bold text-blue-600">کنگره</span>
              </div>
              <div class="flex items-center gap-2 text-blue-600 font-bold group-hover:gap-3 transition-all">
                <span>بازدید از وب‌سایت</span>
                <span class="material-symbols-outlined text-[20px]">open_in_new</span>
              </div>
            </div>
          </a>

          <!-- European Respiratory Society -->
          <a 
            href="https://www.ersnet.org/" 
            target="_blank"
            class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-purple-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-purple-300 dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute top-0 right-0 h-32 w-32 translate-x-8 -translate-y-8 rounded-full bg-purple-500/5 blur-3xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-purple-500 to-purple-600 shadow-lg shadow-purple-500/30 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-5xl text-white">public</span>
              </div>
              <h2 class="mb-3 text-2xl font-black">European Respiratory Society</h2>
              <p class="mb-2 text-sm font-medium text-purple-600">انجمن تنفسی اروپا</p>
              <p class="mb-6 leading-relaxed text-slate-600 dark:text-slate-400">
                انجمن تنفسی اروپا یکی از بزرگترین و معتبرترین انجمن‌های بین‌المللی در زمینه بیماری‌های تنفسی است که با برگزاری کنگره‌های سالانه و انتشار مجلات علمی، نقش مهمی در پیشرفت این حوزه دارد.
              </p>
              <div class="mb-6 flex flex-wrap gap-2">
                <span class="rounded-full bg-purple-500/10 px-3 py-1 text-xs font-bold text-purple-600">بین‌المللی</span>
                <span class="rounded-full bg-purple-500/10 px-3 py-1 text-xs font-bold text-purple-600">مجلات ISI</span>
                <span class="rounded-full bg-purple-500/10 px-3 py-1 text-xs font-bold text-purple-600">کنگره سالانه</span>
              </div>
              <div class="flex items-center gap-2 text-purple-600 font-bold group-hover:gap-3 transition-all">
                <span>بازدید از وب‌سایت</span>
                <span class="material-symbols-outlined text-[20px]">open_in_new</span>
              </div>
            </div>
          </a>

          <!-- American Thoracic Society -->
          <a 
            href="https://www.thoracic.org/" 
            target="_blank"
            class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-red-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-red-300 dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute top-0 right-0 h-32 w-32 translate-x-8 -translate-y-8 rounded-full bg-red-500/5 blur-3xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-red-500 to-red-600 shadow-lg shadow-red-500/30 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-5xl text-white">medical_services</span>
              </div>
              <h2 class="mb-3 text-2xl font-black">American Thoracic Society</h2>
              <p class="mb-2 text-sm font-medium text-red-600">انجمن قفسه سینه آمریکا</p>
              <p class="mb-6 leading-relaxed text-slate-600 dark:text-slate-400">
                انجمن قفسه سینه آمریکا با بیش از 100 سال سابقه، پیشرو در تحقیقات و آموزش بیماری‌های ریوی، قلبی-ریوی و مراقبت‌های ویژه است و راهنماهای بالینی معتبری را منتشر می‌کند.
              </p>
              <div class="mb-6 flex flex-wrap gap-2">
                <span class="rounded-full bg-red-500/10 px-3 py-1 text-xs font-bold text-red-600">100+ سال سابقه</span>
                <span class="rounded-full bg-red-500/10 px-3 py-1 text-xs font-bold text-red-600">راهنماهای بالینی</span>
                <span class="rounded-full bg-red-500/10 px-3 py-1 text-xs font-bold text-red-600">تحقیقات</span>
              </div>
              <div class="flex items-center gap-2 text-red-600 font-bold group-hover:gap-3 transition-all">
                <span>بازدید از وب‌سایت</span>
                <span class="material-symbols-outlined text-[20px]">open_in_new</span>
              </div>
            </div>
          </a>

          <!-- Iranian Pediatric Society -->
          <a 
            href="https://irpediatrics.com/" 
            target="_blank"
            class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-emerald-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-emerald-300 dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute top-0 right-0 h-32 w-32 translate-x-8 -translate-y-8 rounded-full bg-emerald-500/5 blur-3xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-emerald-500 to-green-600 shadow-lg shadow-emerald-500/30 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-5xl text-white">child_care</span>
              </div>
              <h2 class="mb-3 text-2xl font-black">انجمن پزشکان کودکان ایران</h2>
              <p class="mb-2 text-sm font-medium text-emerald-600">مرجع تخصصی اطفال در ایران</p>
              <p class="mb-6 leading-relaxed text-slate-600 dark:text-slate-400">
                انجمن علمی پزشکان کودکان ایران با هدف ارتقای سطح علمی و حرفه‌ای پزشکان اطفال، برگزاری کنگره‌ها، کارگاه‌ها و انتشار مجلات علمی، نقش مهمی در سلامت کودکان کشور ایفا می‌کند.
              </p>
              <div class="mb-6 flex flex-wrap gap-2">
                <span class="rounded-full bg-emerald-500/10 px-3 py-1 text-xs font-bold text-emerald-600">اطفال</span>
                <span class="rounded-full bg-emerald-500/10 px-3 py-1 text-xs font-bold text-emerald-600">کنگره</span>
                <span class="rounded-full bg-emerald-500/10 px-3 py-1 text-xs font-bold text-emerald-600">مجله علمی</span>
              </div>
              <div class="flex items-center gap-2 text-emerald-600 font-bold group-hover:gap-3 transition-all">
                <span>بازدید از وب‌سایت</span>
                <span class="material-symbols-outlined text-[20px]">open_in_new</span>
              </div>
            </div>
          </a>
        </div>

        <!-- CTA Section -->
        <div class="mt-16 rounded-2xl border border-primary/20 bg-gradient-to-br from-primary/5 to-blue-500/5 p-8 lg:p-12 dark:from-primary/10 dark:to-blue-500/10">
          <div class="flex flex-col items-center gap-8 text-center">
            <div class="flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-primary to-blue-600 text-white shadow-lg shadow-primary/30">
              <span class="material-symbols-outlined text-5xl">handshake</span>
            </div>
            <div>
              <h3 class="mb-3 text-2xl font-black">همکاری با انجمن‌های بین‌المللی</h3>
              <p class="text-slate-600 dark:text-slate-400 max-w-2xl mx-auto">
                انجمن علمی ریه کودکان ایران با همکاری نزدیک با انجمن‌های معتبر بین‌المللی، به تبادل دانش و تجربیات علمی می‌پردازد
              </p>
            </div>
            <div class="flex flex-wrap gap-4 justify-center">
              <div class="flex items-center gap-2 rounded-lg bg-white px-4 py-2 dark:bg-slate-900">
                <span class="material-symbols-outlined text-primary">check_circle</span>
                <span class="text-sm font-medium">تبادل دانش</span>
              </div>
              <div class="flex items-center gap-2 rounded-lg bg-white px-4 py-2 dark:bg-slate-900">
                <span class="material-symbols-outlined text-primary">check_circle</span>
                <span class="text-sm font-medium">کنگره‌های مشترک</span>
              </div>
              <div class="flex items-center gap-2 rounded-lg bg-white px-4 py-2 dark:bg-slate-900">
                <span class="material-symbols-outlined text-primary">check_circle</span>
                <span class="text-sm font-medium">انتشارات علمی</span>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
