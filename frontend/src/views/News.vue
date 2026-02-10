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
          <div v-if="newsLoading" class="flex flex-col gap-6 lg:col-span-3">
            <div class="text-center py-12">
              <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
              <p class="mt-4 text-slate-500">در حال بارگذاری اخبار...</p>
            </div>
          </div>

          <div v-else-if="newsError" class="flex flex-col gap-6 lg:col-span-3">
            <div class="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-xl p-6 text-center">
              <span class="material-symbols-outlined text-red-600 text-4xl mb-2">error</span>
              <p class="text-red-600 dark:text-red-400">{{ newsError }}</p>
            </div>
          </div>

          <div v-else-if="newsItems.length === 0" class="flex flex-col gap-6 lg:col-span-3">
            <div class="bg-slate-50 dark:bg-slate-800 rounded-xl p-12 text-center">
              <span class="material-symbols-outlined text-slate-400 text-5xl mb-4">info</span>
              <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-2">خبری یافت نشد</h3>
              <p class="text-slate-500 dark:text-slate-400">در حال حاضر خبری برای نمایش وجود ندارد.</p>
            </div>
          </div>

          <div v-else class="flex flex-col gap-6 lg:col-span-3">
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
            <div v-if="totalPages > 1" class="mt-8 flex items-center justify-center gap-2">
              <button 
                @click="loadPage(currentPage - 1)"
                :disabled="!hasPrevPage"
                class="flex h-10 w-10 items-center justify-center rounded-lg border border-slate-200 bg-white hover:bg-slate-50 dark:border-slate-800 dark:bg-slate-900 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span class="material-symbols-outlined">chevron_right</span>
              </button>
              <button 
                v-for="page in Math.min(totalPages, 5)" 
                :key="page"
                @click="loadPage(page)"
                :class="currentPage === page ? 'bg-primary text-white' : 'border border-slate-200 bg-white hover:bg-slate-50 dark:border-slate-800 dark:bg-slate-900'"
                class="flex h-10 w-10 items-center justify-center rounded-lg font-bold"
              >
                {{ page }}
              </button>
              <button 
                @click="loadPage(currentPage + 1)"
                :disabled="!hasNextPage"
                class="flex h-10 w-10 items-center justify-center rounded-lg border border-slate-200 bg-white hover:bg-slate-50 dark:border-slate-800 dark:bg-slate-900 disabled:opacity-50 disabled:cursor-not-allowed"
              >
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
import { ref, onMounted, computed } from 'vue';
import { getApiUrl } from '@/utils/api';

type NewsItem = {
  id: number;
  title: string;
  slug: string;
  content: string;
  image: string | null;
  author: string;
  is_published: boolean;
  views: number;
  created_at: string;
};

const searchQuery = ref('');
const selectedCategory = ref('all');
const newsItems = ref<NewsItem[]>([]);
const newsLoading = ref(true);
const newsError = ref<string | null>(null);
const currentPage = ref(1);
const totalPages = ref(1);
const hasNextPage = ref(false);
const hasPrevPage = ref(false);

const categories = ref([
  { id: 'all', name: 'همه' },
  { id: 'asthma', name: 'آسم' },
  { id: 'cf', name: 'فیبروز سیستیک' },
  { id: 'infections', name: 'عفونت‌های تنفسی' },
  { id: 'icu', name: 'مراقبت‌های ویژه' },
  { id: 'congenital', name: 'ناهنجاری‌های مادرزادی' }
]);

const formatDate = (isoDate: string) => {
  try {
    return new Date(isoDate).toLocaleDateString('fa-IR');
  } catch (error) {
    return isoDate;
  }
};

const latestNews = computed(() => {
  return newsItems.value.slice(0, 3).map(item => ({
    id: item.id,
    date: formatDate(item.created_at),
    title: item.title
  }));
});

const newsList = computed(() => {
  return newsItems.value.map(item => ({
    id: item.id,
    title: item.title,
    excerpt: item.content,
    category: 'خبر',
    categoryClass: 'bg-primary/10 text-primary',
    date: formatDate(item.created_at),
    author: item.author,
    image: item.image ? getApiUrl(item.image) : '/img/hero-events.svg',
    slug: item.slug
  }));
});

const loadPage = async (page: number) => {
  if (page < 1 || page > totalPages.value) return;
  currentPage.value = page;
  await fetchNews();
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

const fetchNews = async () => {
  newsLoading.value = true;
  newsError.value = null;

  try {
    const response = await fetch(getApiUrl(`/api/news/?page=${currentPage.value}&per_page=12`), {
      credentials: 'include',
    });

    if (response.status === 404) {
      newsItems.value = [];
      newsLoading.value = false;
      return;
    }

    if (!response.ok) {
      throw new Error(`خطا در دریافت اخبار از سرور (${response.status})`);
    }

    const data = await response.json();

    if (!data.success || !Array.isArray(data.news)) {
      throw new Error('ساختار داده اخبار نامعتبر است');
    }

    newsItems.value = data.news;
    
    if (data.pagination) {
      totalPages.value = data.pagination.pages || 1;
      hasNextPage.value = data.pagination.has_next || false;
      hasPrevPage.value = data.pagination.has_prev || false;
    }
  } catch (error: any) {
    console.error('Failed to load news:', error);
    newsError.value = error.message || 'خطای ناشناخته هنگام دریافت اخبار';
  } finally {
    newsLoading.value = false;
  }
};

onMounted(() => {
  fetchNews();
});
</script>
