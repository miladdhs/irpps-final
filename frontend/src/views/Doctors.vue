<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <!-- Header Section -->
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary w-fit">
            <span class="material-symbols-outlined text-[20px]">medical_services</span>
            منابع پزشکی
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">منابع و محتوای پزشکی</h1>
          <p class="text-lg text-slate-600 dark:text-slate-400 max-w-2xl">دسترسی به کتاب‌ها، انتشارات، راهنماها و محتوای علمی تخصصی</p>
        </div>

        <!-- Categories Grid -->
        <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          <!-- Books Category -->
          <div 
            @click="openCategory('books')"
            class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-blue-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-blue-300 cursor-pointer dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute top-0 right-0 h-24 w-24 translate-x-6 -translate-y-6 rounded-full bg-blue-500/5 blur-2xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-xl bg-gradient-to-br from-blue-500 to-blue-600 shadow-lg shadow-blue-500/20 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-white text-4xl">menu_book</span>
              </div>
              <h3 class="mb-3 text-xl font-black">کتاب‌های آموزشی</h3>
              <p class="mb-4 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                کتاب‌های تخصصی و راهنماهای بالینی
              </p>
              <div class="flex items-center gap-2 text-blue-600 font-bold group-hover:gap-3 transition-all">
                <span>19 کتاب</span>
                <span class="material-symbols-outlined text-[20px]">arrow_back</span>
              </div>
            </div>
          </div>

          <!-- Newsletters -->
          <div 
            @click="openCategory('newsletters')"
            class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-purple-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-purple-300 cursor-pointer dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute top-0 right-0 h-24 w-24 translate-x-6 -translate-y-6 rounded-full bg-purple-500/5 blur-2xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-xl bg-gradient-to-br from-purple-500 to-purple-600 shadow-lg shadow-purple-500/20 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-white text-4xl">newspaper</span>
              </div>
              <h3 class="mb-3 text-xl font-black">خبرنامه‌ها</h3>
              <p class="mb-4 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                خبرنامه‌های سالانه انجمن
              </p>
              <div class="inline-flex items-center gap-2 rounded-full bg-amber-500/10 px-3 py-1 text-xs font-bold text-amber-600">
                <span class="material-symbols-outlined text-[16px]">schedule</span>
                به زودی
              </div>
            </div>
          </div>

          <!-- Congress Booklets -->
          <div 
            @click="openCategory('congress')"
            class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-emerald-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-emerald-300 cursor-pointer dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute top-0 right-0 h-24 w-24 translate-x-6 -translate-y-6 rounded-full bg-emerald-500/5 blur-2xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-xl bg-gradient-to-br from-emerald-500 to-green-600 shadow-lg shadow-emerald-500/20 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-white text-4xl">book</span>
              </div>
              <h3 class="mb-3 text-xl font-black">کتابچه کنگره‌ها</h3>
              <p class="mb-4 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                کتابچه‌های کنگره‌ها و همایش‌ها
              </p>
              <div class="flex items-center gap-2 text-emerald-600 font-bold group-hover:gap-3 transition-all">
                <span>2 فایل</span>
                <span class="material-symbols-outlined text-[20px]">arrow_back</span>
              </div>
            </div>
          </div>

          <!-- Journal -->
          <a 
            href="https://brieflands.com/journals/jcp" 
            target="_blank"
            class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-pink-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-pink-300 dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute top-0 right-0 h-24 w-24 translate-x-6 -translate-y-6 rounded-full bg-pink-500/5 blur-2xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-xl bg-gradient-to-br from-pink-500 to-pink-600 shadow-lg shadow-pink-500/20 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-white text-4xl">description</span>
              </div>
              <h3 class="mb-3 text-xl font-black">مجله انجمن</h3>
              <p class="mb-4 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                مجله علمی در سایت Brieflands
              </p>
              <div class="flex items-center gap-2 text-pink-600 font-bold group-hover:gap-3 transition-all">
                <span>مشاهده در سایت</span>
                <span class="material-symbols-outlined text-[20px]">open_in_new</span>
              </div>
            </div>
          </a>

          <!-- Other Products -->
          <div 
            @click="openCategory('other')"
            class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-orange-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-orange-300 cursor-pointer dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute top-0 right-0 h-24 w-24 translate-x-6 -translate-y-6 rounded-full bg-orange-500/5 blur-2xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-xl bg-gradient-to-br from-orange-500 to-orange-600 shadow-lg shadow-orange-500/20 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-white text-4xl">folder_open</span>
              </div>
              <h3 class="mb-3 text-xl font-black">سایر محصولات</h3>
              <p class="mb-4 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                سایر انتشارات و محصولات علمی
              </p>
              <div class="flex items-center gap-2 text-orange-600 font-bold group-hover:gap-3 transition-all">
                <span>1 فایل</span>
                <span class="material-symbols-outlined text-[20px]">arrow_back</span>
              </div>
            </div>
          </div>

          <!-- Research -->
          <div 
            @click="openCategory('research')"
            class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-red-50 to-white p-8 shadow-sm transition-all hover:shadow-2xl hover:border-red-300 cursor-pointer dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute top-0 right-0 h-24 w-24 translate-x-6 -translate-y-6 rounded-full bg-red-500/5 blur-2xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-xl bg-gradient-to-br from-red-500 to-red-600 shadow-lg shadow-red-500/20 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-white text-4xl">science</span>
              </div>
              <h3 class="mb-3 text-xl font-black">تحقیقات و پژوهش</h3>
              <p class="mb-4 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                مقالات و تحقیقات علمی انجمن
              </p>
              <div class="inline-flex items-center gap-2 rounded-full bg-amber-500/10 px-3 py-1 text-xs font-bold text-amber-600">
                <span class="material-symbols-outlined text-[16px]">schedule</span>
                به زودی
              </div>
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
            <div class="text-sm text-slate-500 dark:text-slate-400">کتاب و راهنما</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">category</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">6</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">دسته‌بندی</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">download</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">5K+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">دانلود</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">update</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">2025</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">به‌روزرسانی</div>
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
      <div class="max-h-[80vh] w-full max-w-4xl overflow-y-auto rounded-2xl border border-slate-200 bg-white shadow-2xl dark:border-slate-800 dark:bg-slate-900">
        <div class="sticky top-0 flex items-center justify-between border-b border-slate-200 bg-white p-6 dark:border-slate-800 dark:bg-slate-900">
          <h2 class="text-2xl font-black">{{ modalTitle }}</h2>
          <button @click="closeModal" class="rounded-lg p-2 hover:bg-slate-100 transition-colors dark:hover:bg-slate-800">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>
        <div class="p-6">
          <!-- Books with Categories -->
          <div v-if="currentCategory === 'books'" class="space-y-8">
            <div v-for="(category, key) in booksData" :key="key">
              <h3 class="mb-4 flex items-center gap-2 text-lg font-bold">
                <span class="material-symbols-outlined text-primary">folder</span>
                {{ category.title }}
              </h3>
              <div class="grid grid-cols-1 gap-3 md:grid-cols-2">
                <a 
                  v-for="book in category.files" 
                  :key="book.path"
                  :href="book.path" 
                  target="_blank"
                  class="group flex items-center gap-4 rounded-xl border border-slate-200 p-4 transition-all hover:border-primary/30 hover:bg-slate-50 hover:shadow-md dark:border-slate-800 dark:hover:bg-slate-800"
                >
                  <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary/10">
                    <span class="material-symbols-outlined text-primary text-2xl">picture_as_pdf</span>
                  </div>
                  <div class="flex-1 min-w-0">
                    <div class="font-bold truncate group-hover:text-primary transition-colors">{{ book.name }}</div>
                    <div class="text-sm text-slate-500">{{ book.size }}</div>
                  </div>
                  <span class="material-symbols-outlined text-slate-400 group-hover:text-primary transition-colors">download</span>
                </a>
              </div>
            </div>
          </div>

          <!-- Other Categories -->
          <div v-else class="grid grid-cols-1 gap-3">
            <a 
              v-for="file in currentFiles" 
              :key="file.path"
              :href="file.path" 
              target="_blank"
              class="group flex items-center gap-4 rounded-xl border border-slate-200 p-4 transition-all hover:border-primary/30 hover:bg-slate-50 hover:shadow-md dark:border-slate-800 dark:hover:bg-slate-800"
            >
              <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary/10">
                <span class="material-symbols-outlined text-primary text-2xl">picture_as_pdf</span>
              </div>
              <div class="flex-1 min-w-0">
                <div class="font-bold group-hover:text-primary transition-colors">{{ file.name }}</div>
                <div class="text-sm text-slate-500">{{ file.size }}</div>
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
const currentCategory = ref('');

const booksData = {
  development: {
    title: "تکامل کودک",
    files: [
      { name: "کتاب تکامل دوران ابتدای کودکی", path: "/Content/Books/تکامل/کتاب-تکامل-دوران-ابتدای-کودکی.pdf", size: "2.5 MB" },
      { name: "تقویت تکامل در اوایل کودکی", path: "/Content/Books/تکامل/تقویت-تکامل-در-اوایل-کودکی-.pdf", size: "1.8 MB" },
      { name: "فعالیت‌هایی برای ارتقای تکامل کودک", path: "/Content/Books/تکامل/فعالیت-هایی-برای-ارتقای-تکامل-کودک.pdf", size: "3.2 MB" },
      { name: "152 Games and Exercises", path: "/Content/Books/تکامل/152-games-and-exercises-for-childrens-development.pdf", size: "4.1 MB" },
      { name: "Children's Development Book", path: "/Content/Books/تکامل/Childrens-development-book.pdf", size: "2.9 MB" }
    ]
  },
  family: {
    title: "گفتار خانواده",
    files: [
      { name: "راهنمای خانواده", path: "/Content/Books/گفتار خانواده/khanevade.pdf", size: "1.5 MB" }
    ]
  },
  imci: {
    title: "مراقبت‌های ادغام ناخوشی‌های اطفال (IMCI)",
    files: [
      { name: "دستورالعمل نهایی اجرا", path: "/Content/Books/مراقبت های ادغام ناخوشی های اطفال/Final-instructions-implementation.pdf", size: "2.1 MB" },
      { name: "راهنمای غیرپزشک", path: "/Content/Books/مراقبت های ادغام ناخوشی های اطفال/mana-np.pdf", size: "1.8 MB" },
      { name: "راهنمای پزشک", path: "/Content/Books/مراقبت های ادغام ناخوشی های اطفال/mana-p.pdf", size: "2.3 MB" }
    ]
  },
  imnci: {
    title: "مراقبت‌های ادغام یافته کودک سالم (IMNCI)",
    files: [
      { name: "کتابچه غیرپزشک", path: "/Content/Books/مراقبت های ادغام یافته‌ی کودک سالم/booklet-غیر-پزشک.pdf", size: "1.9 MB" },
      { name: "کتابچه پزشک کودک سالم", path: "/Content/Books/مراقبت های ادغام یافته‌ی کودک سالم/booklet-پزشک-کودک-سالم.pdf", size: "2.2 MB" },
      { name: "راهنمای مشاوره", path: "/Content/Books/مراقبت های ادغام یافته‌ی کودک سالم/counselling-guide-23-12-1400_compressed.pdf", size: "3.1 MB" },
      { name: "راهنمای غیرپزشک", path: "/Content/Books/مراقبت های ادغام یافته‌ی کودک سالم/non-physician-guide-25-12-1400_compressed.pdf", size: "2.8 MB" },
      { name: "راهنمای پزشک", path: "/Content/Books/مراقبت های ادغام یافته‌ی کودک سالم/physician-guide-30-1-1401_compressed.pdf", size: "3.5 MB" },
      { name: "راهنمای جامع کودک", path: "/Content/Books/مراقبت های ادغام یافته‌ی کودک سالم/rahnamay-jame-koodak.pdf", size: "4.2 MB" }
    ]
  },
  hypothyroidism: {
    title: "هیپوتیروئیدی",
    files: [
      { name: "کتاب بیماری کم‌کاری تیرویید", path: "/Content/Books/هیپوتیروئیدی/کتاب-بیماری-کم-کاری-تیرویید-99.pdf", size: "2.7 MB" }
    ]
  },
  vaccination: {
    title: "واکسیناسیون",
    files: [
      { name: "برنامه و راهنمای ایمن‌سازی 1403", path: "/Content/Books/واکسیناسیون/برنامه-و-راهنمای-ایمن-سازی-1403.pdf", size: "3.8 MB" }
    ]
  },
  gina: {
    title: "GINA - راهنمای آسم",
    files: [
      { name: "GINA Summary Guide 2025", path: "/Content/lAST/GINA-Summary-Guide-2025-WEB_FINAL-WMS.pdf", size: "2.1 MB" },
      { name: "GINA 2025 Update", path: "/Content/lAST/GINA-2025-Update-25_11_08-WMS.pdf", size: "1.5 MB" }
    ]
  }
};

const filesData = {
  congress: [
    { name: 'کتابچه کنگره', path: '/Content/Other/1_23033290624.pdf', size: '5.2 MB' },
    { name: 'خلاصه مقالات پنجمین همایش 1403', path: '/Content/Other/خلاصه مقالات 5 همایش 403.pdf', size: '3.7 MB' }
  ],
  other: [
    { name: 'سند علمی', path: '/Content/Other/DOC-20251227-WA0007.pdf', size: '1.2 MB' }
  ]
};

const modalTitle = computed(() => {
  const titles: Record<string, string> = {
    books: 'کتاب‌های آموزشی',
    newsletters: 'خبرنامه‌ها',
    congress: 'کتابچه کنگره‌ها و همایش‌ها',
    other: 'سایر محصولات',
    research: 'تحقیقات و پژوهش'
  };
  return titles[currentCategory.value] || '';
});

const currentFiles = computed(() => {
  return filesData[currentCategory.value as keyof typeof filesData] || [];
});

function openCategory(category: string) {
  currentCategory.value = category;
  showModal.value = true;
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  showModal.value = false;
  document.body.style.overflow = 'auto';
}
</script>
