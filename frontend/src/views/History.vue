<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <!-- Header Section -->
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary w-fit">
            <span class="material-symbols-outlined text-[20px]">history</span>
            تاریخچه انجمن
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">تاریخچه فعالیت‌های انجمن</h1>
          <p class="text-lg text-slate-600 dark:text-slate-400 max-w-2xl">سیر تکامل و دستاوردهای انجمن علمی ریه کودکان ایران از آغاز تا کنون</p>
        </div>

        <!-- Timeline -->
        <div class="relative">
          <!-- Vertical Line -->
          <div class="absolute right-8 top-0 bottom-0 w-0.5 bg-primary/20 hidden md:block"></div>

          <!-- Timeline Items -->
          <div class="flex flex-col gap-8">
            <!-- 1395 -->
            <div class="flex gap-6 items-start">
              <div class="hidden md:flex h-16 w-16 shrink-0 items-center justify-center rounded-full bg-primary text-white shadow-lg">
                <span class="material-symbols-outlined text-3xl">flag</span>
              </div>
              <div class="flex-1 rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                <div class="mb-2 inline-block rounded-full bg-primary/10 px-3 py-1 text-sm font-bold text-primary">۱۳۹۵</div>
                <h3 class="mb-3 text-xl font-bold">تأسیس انجمن</h3>
                <p class="leading-relaxed text-slate-600 dark:text-slate-400">
                  انجمن علمی ریه کودکان ایران در تاریخ ۱۶ آذر ۱۳۹۵ با هدف ارتقای دانش و آگاهی در زمینه بیماری‌های ریوی کودکان و با همکاری متخصصان برجسته ریه کودکان کشور تأسیس شد.
                </p>
              </div>
            </div>

            <!-- 1396 -->
            <div class="flex gap-6 items-start">
              <div class="hidden md:flex h-16 w-16 shrink-0 items-center justify-center rounded-full bg-primary text-white shadow-lg">
                <span class="material-symbols-outlined text-3xl">groups</span>
              </div>
              <div class="flex-1 rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                <div class="mb-2 inline-block rounded-full bg-primary/10 px-3 py-1 text-sm font-bold text-primary">۱۳۹۶</div>
                <h3 class="mb-3 text-xl font-bold">تشکیل هیئت مدیره اول</h3>
                <p class="leading-relaxed text-slate-600 dark:text-slate-400">
                  اولین هیئت مدیره انجمن با حضور متخصصان مجرب و برجسته در زمینه بیماری‌های ریوی کودکان تشکیل شد و برنامه‌های راهبردی انجمن تدوین گردید.
                </p>
              </div>
            </div>

            <!-- 1397 -->
            <div class="flex gap-6 items-start">
              <div class="hidden md:flex h-16 w-16 shrink-0 items-center justify-center rounded-full bg-primary text-white shadow-lg">
                <span class="material-symbols-outlined text-3xl">school</span>
              </div>
              <div class="flex-1 rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                <div class="mb-2 inline-block rounded-full bg-primary/10 px-3 py-1 text-sm font-bold text-primary">۱۳۹۷</div>
                <h3 class="mb-3 text-xl font-bold">شروع فعالیت‌های آموزشی</h3>
                <p class="leading-relaxed text-slate-600 dark:text-slate-400">
                  برگزاری اولین کارگاه‌ها و سمینارهای آموزشی تخصصی برای پزشکان، پرستاران و دانشجویان رشته‌های پزشکی با هدف ارتقای دانش و مهارت‌های بالینی.
                </p>
              </div>
            </div>

            <!-- 1398 -->
            <div class="flex gap-6 items-start">
              <div class="hidden md:flex h-16 w-16 shrink-0 items-center justify-center rounded-full bg-primary text-white shadow-lg">
                <span class="material-symbols-outlined text-3xl">menu_book</span>
              </div>
              <div class="flex-1 rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                <div class="mb-2 inline-block rounded-full bg-primary/10 px-3 py-1 text-sm font-bold text-primary">۱۳۹۸</div>
                <h3 class="mb-3 text-xl font-bold">انتشارات علمی</h3>
                <p class="leading-relaxed text-slate-600 dark:text-slate-400">
                  شروع انتشار مجلات، کتاب‌ها و مقالات علمی تخصصی در زمینه بیماری‌های ریوی کودکان و نوزادان با همکاری محققان برجسته داخلی و بین‌المللی.
                </p>
              </div>
            </div>

            <!-- 1399 -->
            <div class="flex gap-6 items-start">
              <div class="hidden md:flex h-16 w-16 shrink-0 items-center justify-center rounded-full bg-primary text-white shadow-lg">
                <span class="material-symbols-outlined text-3xl">biotech</span>
              </div>
              <div class="flex-1 rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                <div class="mb-2 inline-block rounded-full bg-primary/10 px-3 py-1 text-sm font-bold text-primary">۱۳۹۹</div>
                <h3 class="mb-3 text-xl font-bold">توسعه پژوهش‌های علمی</h3>
                <p class="leading-relaxed text-slate-600 dark:text-slate-400">
                  حمایت از طرح‌های پژوهشی دانشجویان و اساتید، برگزاری همایش‌های علمی و ایجاد شبکه همکاری با مراکز تحقیقاتی معتبر داخلی و خارجی.
                </p>
              </div>
            </div>

            <!-- 1400 -->
            <div class="flex gap-6 items-start">
              <div class="hidden md:flex h-16 w-16 shrink-0 items-center justify-center rounded-full bg-primary text-white shadow-lg">
                <span class="material-symbols-outlined text-3xl">public</span>
              </div>
              <div class="flex-1 rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                <div class="mb-2 inline-block rounded-full bg-primary/10 px-3 py-1 text-sm font-bold text-primary">۱۴۰۰</div>
                <h3 class="mb-3 text-xl font-bold">گسترش فعالیت‌های بین‌المللی</h3>
                <p class="leading-relaxed text-slate-600 dark:text-slate-400">
                  برگزاری کنگره‌ها و همایش‌های بین‌المللی با حضور متخصصان برجسته از سراسر جهان، تبادل دانش و تجربیات علمی و عضویت در شبکه‌های بین‌المللی سلامت ریه.
                </p>
              </div>
            </div>

            <!-- 1401-1403 -->
            <div class="flex gap-6 items-start">
              <div class="hidden md:flex h-16 w-16 shrink-0 items-center justify-center rounded-full bg-primary text-white shadow-lg">
                <span class="material-symbols-outlined text-3xl">trending_up</span>
              </div>
              <div class="flex-1 rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                <div class="mb-2 inline-block rounded-full bg-primary/10 px-3 py-1 text-sm font-bold text-primary">۱۴۰۱ - ۱۴۰۳</div>
                <h3 class="mb-3 text-xl font-bold">رشد و توسعه مستمر</h3>
                <p class="leading-relaxed text-slate-600 dark:text-slate-400">
                  افزایش تعداد اعضا، گسترش فعالیت‌های آموزشی و پژوهشی، تدوین راهنماهای بالینی بومی، راه‌اندازی پلتفرم آموزش آنلاین و ارائه خدمات مشاوره‌ای به خانواده‌ها و پزشکان.
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Stats Section -->
        <div class="mt-16 grid grid-cols-2 gap-6 md:grid-cols-4">
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">calendar_today</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">8+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">سال فعالیت</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">event</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">50+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">رویداد برگزار شده</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">groups</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">200+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">عضو فعال</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">article</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">100+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">مقاله منتشر شده</div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
