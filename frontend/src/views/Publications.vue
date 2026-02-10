<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <!-- Header Section -->
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary w-fit">
            <span class="material-symbols-outlined text-[20px]">article</span>
            انتشارات
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">انتشارات علمی</h1>
          <p class="text-lg text-slate-600 dark:text-slate-400 max-w-2xl">مجلات، کتاب‌ها و مقالات علمی منتشر شده توسط انجمن</p>
        </div>

        <!-- Main Publications Grid -->
        <div class="grid grid-cols-1 gap-6 lg:grid-cols-2">
          <!-- Newsletters -->
          <div class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-blue-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-blue-300 dark:border-slate-800 dark:from-slate-900 dark:to-slate-900">
            <div class="absolute top-0 right-0 h-32 w-32 translate-x-8 -translate-y-8 rounded-full bg-blue-500/5 blur-3xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-blue-500 to-blue-600 shadow-lg shadow-blue-500/30 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-5xl text-white">newspaper</span>
              </div>
              <h3 class="mb-3 text-2xl font-black">خبرنامه‌ها</h3>
              <p class="mb-6 text-slate-600 dark:text-slate-400">
                خبرنامه‌های سالانه انجمن با آخرین اخبار و دستاوردهای علمی
              </p>
              <div class="mb-6 flex flex-wrap gap-2">
                <span class="rounded-full bg-blue-500/10 px-3 py-1 text-xs font-bold text-blue-600">سالانه</span>
                <span class="rounded-full bg-blue-500/10 px-3 py-1 text-xs font-bold text-blue-600">اخبار علمی</span>
                <span class="rounded-full bg-blue-500/10 px-3 py-1 text-xs font-bold text-blue-600">دستاوردها</span>
              </div>
              <div class="inline-flex items-center gap-2 rounded-full bg-amber-500/10 px-4 py-2 text-sm font-bold text-amber-600">
                <span class="material-symbols-outlined text-[18px]">schedule</span>
                به زودی
              </div>
            </div>
          </div>

          <!-- Congress Booklets -->
          <div 
            @click="openModal('congress')"
            class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-emerald-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-emerald-300 cursor-pointer dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute top-0 right-0 h-32 w-32 translate-x-8 -translate-y-8 rounded-full bg-emerald-500/5 blur-3xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-emerald-500 to-green-600 shadow-lg shadow-emerald-500/30 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-5xl text-white">book</span>
              </div>
              <h3 class="mb-3 text-2xl font-black">کتابچه کنگره‌ها و همایش‌ها</h3>
              <p class="mb-6 text-slate-600 dark:text-slate-400">
                کتابچه‌های کنگره‌ها و همایش‌های علمی با خلاصه مقالات
              </p>
              <div class="mb-6 flex flex-wrap gap-2">
                <span class="rounded-full bg-emerald-500/10 px-3 py-1 text-xs font-bold text-emerald-600">2 فایل</span>
                <span class="rounded-full bg-emerald-500/10 px-3 py-1 text-xs font-bold text-emerald-600">PDF</span>
                <span class="rounded-full bg-emerald-500/10 px-3 py-1 text-xs font-bold text-emerald-600">دانلود رایگان</span>
              </div>
              <div class="flex items-center gap-2 text-emerald-600 font-bold group-hover:gap-3 transition-all">
                <span>مشاهده و دانلود</span>
                <span class="material-symbols-outlined">download</span>
              </div>
            </div>
          </div>

          <!-- Journal -->
          <a 
            href="https://brieflands.com/journals/jcp" 
            target="_blank"
            class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-purple-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-purple-300 dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute top-0 right-0 h-32 w-32 translate-x-8 -translate-y-8 rounded-full bg-purple-500/5 blur-3xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-purple-500 to-purple-600 shadow-lg shadow-purple-500/30 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-5xl text-white">description</span>
              </div>
              <h3 class="mb-3 text-2xl font-black">مجله انجمن</h3>
              <p class="mb-6 text-slate-600 dark:text-slate-400">
                مجله علمی انجمن در سایت Brieflands با مقالات داوری شده
              </p>
              <div class="mb-6 flex flex-wrap gap-2">
                <span class="rounded-full bg-purple-500/10 px-3 py-1 text-xs font-bold text-purple-600">Peer-Reviewed</span>
                <span class="rounded-full bg-purple-500/10 px-3 py-1 text-xs font-bold text-purple-600">ISI</span>
                <span class="rounded-full bg-purple-500/10 px-3 py-1 text-xs font-bold text-purple-600">بین‌المللی</span>
              </div>
              <div class="flex items-center gap-2 text-purple-600 font-bold group-hover:gap-3 transition-all">
                <span>مشاهده در سایت</span>
                <span class="material-symbols-outlined">open_in_new</span>
              </div>
            </div>
          </a>

          <!-- Other Products -->
          <div 
            @click="openModal('other')"
            class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-orange-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-orange-300 cursor-pointer dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute top-0 right-0 h-32 w-32 translate-x-8 -translate-y-8 rounded-full bg-orange-500/5 blur-3xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-orange-500 to-orange-600 shadow-lg shadow-orange-500/30 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-5xl text-white">folder_open</span>
              </div>
              <h3 class="mb-3 text-2xl font-black">سایر محصولات</h3>
              <p class="mb-6 text-slate-600 dark:text-slate-400">
                سایر انتشارات و محصولات علمی انجمن
              </p>
              <div class="mb-6 flex flex-wrap gap-2">
                <span class="rounded-full bg-orange-500/10 px-3 py-1 text-xs font-bold text-orange-600">1 فایل</span>
                <span class="rounded-full bg-orange-500/10 px-3 py-1 text-xs font-bold text-orange-600">PDF</span>
                <span class="rounded-full bg-orange-500/10 px-3 py-1 text-xs font-bold text-orange-600">دانلود رایگان</span>
              </div>
              <div class="flex items-center gap-2 text-orange-600 font-bold group-hover:gap-3 transition-all">
                <span>مشاهده و دانلود</span>
                <span class="material-symbols-outlined">download</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Research Section -->
        <div class="mt-8">
          <div class="group rounded-2xl border border-slate-200 bg-gradient-to-br from-pink-50 to-white p-8 shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:from-slate-900 dark:to-slate-900">
            <div class="flex flex-col gap-6 md:flex-row md:items-center">
              <div class="flex h-20 w-20 shrink-0 items-center justify-center rounded-2xl bg-gradient-to-br from-pink-500 to-pink-600 shadow-lg shadow-pink-500/30">
                <span class="material-symbols-outlined text-5xl text-white">science</span>
              </div>
              <div class="flex-1">
                <h3 class="mb-2 text-2xl font-black">تحقیقات و پژوهش</h3>
                <p class="mb-4 text-slate-600 dark:text-slate-400">
                  مقالات و تحقیقات علمی اعضای انجمن در مجلات معتبر داخلی و بین‌المللی
                </p>
                <div class="flex flex-wrap gap-2">
                  <span class="rounded-full bg-pink-500/10 px-3 py-1 text-xs font-bold text-pink-600">مقالات ISI</span>
                  <span class="rounded-full bg-pink-500/10 px-3 py-1 text-xs font-bold text-pink-600">پایان‌نامه‌ها</span>
                  <span class="rounded-full bg-pink-500/10 px-3 py-1 text-xs font-bold text-pink-600">پروژه‌های تحقیقاتی</span>
                </div>
              </div>
              <div class="inline-flex items-center gap-2 rounded-full bg-amber-500/10 px-4 py-2 text-sm font-bold text-amber-600">
                <span class="material-symbols-outlined text-[18px]">schedule</span>
                به زودی
              </div>
            </div>
          </div>
        </div>

        <!-- Stats -->
        <div class="mt-16 grid grid-cols-2 gap-6 md:grid-cols-4">
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">article</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">100+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">مقاله منتشر شده</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">book</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">15+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">کتاب منتشر شده</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">event</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">9</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">کنگره برگزار شده</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">groups</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">500+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">محقق و نویسنده</div>
          </div>
        </div>
      </main>
    </div>

    <!-- Files Modal -->
    <div 
      v-if="showModal" 
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4"
      @click.self="closeModal"
    >
      <div class="max-h-[80vh] w-full max-w-2xl overflow-y-auto rounded-2xl border border-slate-200 bg-white shadow-2xl dark:border-slate-800 dark:bg-slate-900">
        <div class="sticky top-0 flex items-center justify-between border-b border-slate-200 bg-white p-6 dark:border-slate-800 dark:bg-slate-900">
          <h2 class="text-2xl font-black">{{ modalTitle }}</h2>
          <button @click="closeModal" class="rounded-lg p-2 hover:bg-slate-100 transition-colors dark:hover:bg-slate-800">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>
        <div class="p-6">
          <div class="flex flex-col gap-3">
            <a 
              v-for="file in modalFiles" 
              :key="file.path"
              :href="file.path" 
              target="_blank"
              class="group flex items-center justify-between rounded-xl border border-slate-200 p-4 transition-all hover:border-primary/30 hover:bg-slate-50 hover:shadow-md dark:border-slate-800 dark:hover:bg-slate-800"
            >
              <div class="flex items-center gap-4">
                <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary/10">
                  <span class="material-symbols-outlined text-primary text-2xl">picture_as_pdf</span>
                </div>
                <div>
                  <div class="font-bold group-hover:text-primary transition-colors">{{ file.name }}</div>
                  <div class="text-sm text-slate-500">{{ file.size }}</div>
                </div>
              </div>
              <span class="material-symbols-outlined text-slate-400 group-hover:text-primary transition-colors">download</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';

const showModal = ref(false);
const modalType = ref('');

const files = {
  congress: [
    { name: 'کتابچه کنگره', path: '/Content/Other/1_23033290624.pdf', size: '5.2 MB' },
    { name: 'خلاصه مقالات پنجمین همایش 1403', path: '/Content/Other/خلاصه مقالات 5 همایش 403.pdf', size: '3.7 MB' }
  ],
  other: [
    { name: 'سند علمی', path: '/Content/Other/DOC-20251227-WA0007.pdf', size: '1.2 MB' }
  ]
};

const modalTitle = computed(() => {
  if (modalType.value === 'congress') return 'کتابچه کنگره‌ها و همایش‌ها';
  if (modalType.value === 'other') return 'سایر محصولات';
  return '';
});

const modalFiles = computed(() => {
  return files[modalType.value as keyof typeof files] || [];
});

function openModal(type: string) {
  modalType.value = type;
  showModal.value = true;
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  showModal.value = false;
  document.body.style.overflow = 'auto';
}
</script>
