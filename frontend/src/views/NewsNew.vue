<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <!-- Header Section -->
        <div class="mb-8 flex flex-col gap-4">
          <h2 class="text-3xl font-black text-slate-900 dark:text-white">{{ $t('news.title') }}</h2>
          <p class="text-slate-500 dark:text-slate-400">{{ $t('news.subtitle') }}</p>
          
          <!-- Large Search Bar -->
          <div class="mt-4 flex w-full max-w-2xl overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="flex flex-1 items-center px-4">
              <span class="material-symbols-outlined text-slate-400">search</span>
              <input 
                v-model="searchQuery"
                class="w-full border-none bg-transparent py-4 text-sm focus:ring-0" 
                :placeholder="$t('news.searchPlaceholder')" 
                type="text"
              />
            </div>
            <button class="bg-primary px-8 font-bold text-white hover:bg-primary/90 transition-colors">
              {{ $t('news.search') }}
            </button>
          </div>
        </div>

        <!-- Content Grid -->
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-4">
          <!-- Sidebar -->
          <aside class="flex flex-col gap-8 lg:col-span-1">
            <!-- Categories Widget -->
            <div class="rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
              <h3 class="mb-4 flex items-center gap-2 text-lg font-bold">
                <span class="material-symbols-outlined text-primary">category</span>
                {{ $t('news.categories') }}
              </h3>
              <div class="flex flex-col gap-1">
                <a 
                  v-for="category in categories" 
                  :key="category.id"
                  class="flex items-center justify-between rounded-lg px-3 py-2 text-sm transition-colors"
                  :class="selectedCategory === category.id ? 'bg-primary/10 text-primary font-bold' : 'text-slate-600 hover:bg-slate-50 dark:text-slate-400 dark:hover:bg-slate-800'"
                  href="#"
                  @click.prevent="selectedCategory = category.id"
                >
                  <span>{{ category.name }}</span>
                  <span class="material-symbols-outlined text-sm">chevron_left</span>
                </a>
              </div>
            </div>

            <!-- Latest News Widget -->
            <div class="rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
              <h3 class="mb-4 flex items-center gap-2 text-lg font-bold">
                <span class="material-symbols-outlined text-primary">newsmode</span>
                {{ $t('news.latest') }}
              </h3>
              <div class="flex flex-col gap-4">
                <div v-for="item in latestNews" :key="item.id" class="group cursor-pointer">
                  <p class="text-xs text-slate-400 mb-1">{{ item.date }}</p>
                  <h4 class="text-sm font-medium leading-relaxed group-hover:text-primary transition-colors">
                    {{ item.title }}
                  </h4>
                </div>
              </div>
            </div>
          </aside>

          <!-- News List -->
          <div class="flex flex-col gap-6 lg:col-span-3">
            <!-- News Card -->
            <article 
              v-for="news in newsList" 
              :key="news.id"
              class="flex flex-col overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm transition-all hover:shadow-md dark:border-slate-800 dark:bg-slate-900 md:flex-row"
            >
              <div 
                class="h-48 w-full shrink-0 bg-cover bg-center md:h-auto md:w-64" 
                :style="`background-image: url('${news.image}')`"
              ></div>
              <div class="flex flex-1 flex-col p-6">
                <div class="mb-2 flex items-center justify-between">
                  <span class="inline-block rounded px-2 py-1 text-xs font-bold" :class="news.categoryClass">
                    {{ news.category }}
                  </span>
                  <span class="flex items-center gap-1 text-xs text-slate-400">
                    <span class="material-symbols-outlined text-[14px]">calendar_today</span>
                    {{ news.date }}
                  </span>
                </div>
                <h3 class="mb-3 text-xl font-bold leading-snug text-slate-900 dark:text-white">
                  {{ news.title }}
                </h3>
                <p class="mb-6 line-clamp-2 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                  {{ news.excerpt }}
                </p>
                <div class="mt-auto flex items-center justify-between border-t border-slate-100 pt-4 dark:border-slate-800">
                  <span class="text-xs font-medium text-slate-500">{{ $t('news.author') }}: {{ news.author }}</span>
                  <router-link 
                    :to="`/news/${news.slug}`"
                    class="flex items-center gap-1 text-sm font-bold text-primary hover:gap-2 transition-all"
                  >
                    {{ $t('news.readMore') }}
                    <span class="material-symbols-outlined text-[18px]">arrow_back</span>
                  </router-link>
                </div>
              </div>
            </article>

            <!-- Pagination -->
            <div class="mt-8 flex items-center justify-center gap-2">
              <button class="flex h-10 w-10 items-center justify-center rounded-lg border border-slate-200 bg-white hover:bg-slate-50 dark:border-slate-800 dark:bg-slate-900">
                <span class="material-symbols-outlined">chevron_right</span>
              </button>
              <button class="flex h-10 w-10 items-center justify-center rounded-lg bg-primary font-bold text-white">۱</button>
              <button class="flex h-10 w-10 items-center justify-center rounded-lg border border-slate-200 bg-white hover:bg-slate-50 dark:border-slate-800 dark:bg-slate-900">۲</button>
              <button class="flex h-10 w-10 items-center justify-center rounded-lg border border-slate-200 bg-white hover:bg-slate-50 dark:border-slate-800 dark:bg-slate-900">۳</button>
              <span class="px-2 text-slate-400">...</span>
              <button class="flex h-10 w-10 items-center justify-center rounded-lg border border-slate-200 bg-white hover:bg-slate-50 dark:border-slate-800 dark:bg-slate-900">۱۲</button>
              <button class="flex h-10 w-10 items-center justify-center rounded-lg border border-slate-200 bg-white hover:bg-slate-50 dark:border-slate-800 dark:bg-slate-900">
                <span class="material-symbols-outlined">chevron_left</span>
              </button>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const searchQuery = ref('');
const selectedCategory = ref('all');

const categories = ref([
  { id: 'all', name: 'همه' },
  { id: 'asthma', name: 'آسم' },
  { id: 'cf', name: 'فیبروز سیستیک' },
  { id: 'infections', name: 'عفونت‌های تنفسی' },
  { id: 'icu', name: 'مراقبت‌های ویژه' },
  { id: 'congenital', name: 'ناهنجاری‌های مادرزادی' }
]);

const latestNews = ref([
  { id: 1, date: '۲۲ آبان ۱۴۰۲', title: 'برگزاری دهمین کنگره بین‌المللی ریه کودکان' },
  { id: 2, date: '۱۸ آبان ۱۴۰۲', title: 'فراخوان مقاله برای ژورنال تخصصی انجمن' },
  { id: 3, date: '۱۴ آبان ۱۴۰۲', title: 'راهنمای جدید واکسیناسیون آنفولانزا در کودکان' }
]);

const newsList = ref([
  {
    id: 1,
    title: 'تازه های درمان آسم در کودکان: پروتکل های سال ۲۰۲۴',
    excerpt: 'مروری بر جدیدترین پروتکل‌های درمانی ارائه شده در سال ۲۰۲۴ برای مدیریت آسم در اطفال و روش‌های نوین استفاده از اسپری‌های ترکیبی...',
    category: 'مقاله علمی',
    categoryClass: 'bg-primary/10 text-primary',
    date: '۱۵ آبان ۱۴۰۲',
    author: 'دکتر محمد رضایی',
    image: '/img/news1.jpg',
    slug: 'asthma-treatment-2024'
  },
  {
    id: 2,
    title: 'تاثیر آلودگی هوای کلان‌شهرها بر تشدید بیماری‌های ریوی نوزادان',
    excerpt: 'مطالعه آماری انجام شده در بیمارستان‌های تخصصی تهران نشان‌دهنده افزایش ۱۵ درصدی بستری‌های تنفسی نوزادان در روزهای آلوده است...',
    category: 'گزارش موردی',
    categoryClass: 'bg-amber-100 text-amber-600',
    date: '۱۲ آبان ۱۴۰۲',
    author: 'تیم پژوهشی انجمن',
    image: '/img/news2.jpg',
    slug: 'air-pollution-impact'
  },
  {
    id: 3,
    title: 'استانداردهای نوین در تجهیز بخش‌های NICU و مراقبت‌های ریوی',
    excerpt: 'ابلاغیه جدید وزارت بهداشت در خصوص استانداردهای فیزیکی و تجهیزاتی بخش‌های مراقبت ویژه نوزادان با رویکرد سلامت ریه...',
    category: 'اطلاعیه',
    categoryClass: 'bg-emerald-100 text-emerald-600',
    date: '۰۸ آبان ۱۴۰۲',
    author: 'وزارت بهداشت',
    image: '/img/news3.jpg',
    slug: 'nicu-standards'
  }
]);
</script>
