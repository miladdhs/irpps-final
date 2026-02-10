<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100 font-display">
    <div class="relative flex h-auto min-h-screen w-full flex-col overflow-x-hidden">
      <main class="flex-1 flex flex-col max-w-[1200px] mx-auto w-full px-6 md:px-10 py-10">
        <!-- Page Hero / Intro -->
        <div class="flex flex-col gap-4 mb-8">
          <h1 class="text-4xl font-black text-slate-900 dark:text-white tracking-tight">{{ $t('events.title') }}</h1>
          <p class="text-slate-600 dark:text-slate-400 text-lg max-w-2xl leading-relaxed">
            {{ $t('events.subtitle') }}
          </p>
        </div>

        <!-- Tabs Container -->
        <div class="flex flex-col bg-white dark:bg-slate-900 rounded-xl shadow-sm border border-slate-200 dark:border-slate-800 overflow-hidden">
          <!-- Tabs Header -->
          <div class="flex border-b border-slate-200 dark:border-slate-800 px-6 gap-10 overflow-x-auto">
            <button 
              v-for="tab in tabs" 
              :key="tab.id"
              class="flex flex-col items-center justify-center border-b-[3px] pb-4 pt-5 whitespace-nowrap transition-colors"
              :class="activeTab === tab.id ? 'border-primary text-slate-900 dark:text-white' : 'border-transparent text-slate-500 hover:text-primary'"
              @click="activeTab = tab.id"
            >
              <span class="text-sm font-bold tracking-tight">{{ tab.name }}</span>
            </button>
          </div>

          <!-- Filter Bar -->
          <div class="p-6 flex flex-wrap items-center justify-between gap-4 bg-slate-50/50 dark:bg-slate-800/50">
            <div class="flex gap-2 flex-wrap">
              <span class="text-sm text-slate-600 dark:text-slate-400 font-medium py-2 ml-2">{{ $t('events.filterBy') }}:</span>
              <button 
                v-for="filter in filters" 
                :key="filter.id"
                class="px-4 py-1.5 rounded-full text-sm font-medium border transition-colors"
                :class="selectedFilter === filter.id 
                  ? 'bg-primary/10 text-primary border-primary/20' 
                  : 'bg-white dark:bg-slate-900 text-slate-600 dark:text-slate-400 border-slate-200 dark:border-slate-700 hover:border-primary/30'"
                @click="selectedFilter = filter.id"
              >
                {{ filter.name }}
              </button>
            </div>
            <div class="text-sm text-slate-600 dark:text-slate-400">
              {{ $t('events.showing') }} {{ filteredEvents.length }} {{ $t('events.activeEvents') }}
            </div>
          </div>

          <!-- Events Grid -->
          <div v-if="eventsLoading" class="p-12 text-center">
            <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
            <p class="mt-4 text-slate-500">در حال بارگذاری رویدادها...</p>
          </div>

          <div v-else-if="eventsError" class="p-6">
            <div class="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-xl p-6 text-center">
              <span class="material-symbols-outlined text-red-600 text-4xl mb-2">error</span>
              <p class="text-red-600 dark:text-red-400">{{ eventsError }}</p>
            </div>
          </div>

          <div v-else-if="filteredEvents.length === 0" class="p-12 text-center">
            <span class="material-symbols-outlined text-slate-400 text-5xl mb-4">info</span>
            <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-2">رویدادی یافت نشد</h3>
            <p class="text-slate-500 dark:text-slate-400">در حال حاضر رویدادی برای نمایش وجود ندارد.</p>
          </div>

          <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
            <!-- Event Card -->
            <div 
              v-for="event in filteredEvents" 
              :key="event.id"
              class="flex flex-col bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl overflow-hidden hover:shadow-lg hover:border-primary/30 transition-all group"
            >
              <div class="relative w-full aspect-[16/9] bg-center bg-cover" :style="`background-image: url('${event.image}')`">
                <div class="absolute top-3 right-3 text-white text-[10px] font-bold px-3 py-1 rounded-full flex items-center gap-1" :class="event.statusClass">
                  <span v-if="event.status === 'active'" class="size-1.5 rounded-full bg-white animate-pulse"></span>
                  {{ event.statusText }}
                </div>
                <div v-if="event.type" class="absolute top-3 left-3 bg-white/90 backdrop-blur-sm text-primary text-[10px] font-bold px-3 py-1 rounded-full border border-primary/20">
                  {{ event.type }}
                </div>
                <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex items-end p-4">
                  <span class="text-white text-xs font-medium">{{ $t('events.viewDetails') }}</span>
                </div>
              </div>
              <div class="p-5 flex flex-col gap-4 flex-1">
                <div class="flex flex-col gap-2">
                  <h3 class="text-slate-900 dark:text-white text-lg font-bold leading-tight line-clamp-2 min-h-[3.5rem]">
                    {{ event.title }}
                  </h3>
                  <div class="flex items-center gap-2 text-slate-600 dark:text-slate-400 text-xs">
                    <span class="material-symbols-outlined text-primary text-base">calendar_month</span>
                    <span>{{ event.date }}</span>
                  </div>
                  <div class="flex items-center gap-2 text-slate-600 dark:text-slate-400 text-xs">
                    <span class="material-symbols-outlined text-primary text-base">{{ event.locationIcon }}</span>
                    <span>{{ event.location }}</span>
                  </div>
                  <div v-if="event.badge" class="flex items-center gap-2 text-xs font-bold mt-1 p-2 rounded-lg" :class="event.badgeClass">
                    <span class="material-symbols-outlined text-base">{{ event.badgeIcon }}</span>
                    <span>{{ event.badge }}</span>
                  </div>
                </div>
                <div class="mt-auto pt-4 border-t border-slate-100 dark:border-slate-800">
                  <router-link 
                    :to="`/events/${event.slug}`"
                    class="w-full bg-primary text-white py-2.5 rounded-lg text-sm font-bold hover:bg-primary/90 transition-colors flex items-center justify-center"
                  >
                    {{ event.buttonText }}
                  </router-link>
                </div>
              </div>
            </div>
          </div>

          <!-- Pagination -->
          <div v-if="totalPages > 1" class="p-6 border-t border-slate-200 dark:border-slate-800 flex items-center justify-center gap-2">
            <button 
              @click="loadPage(currentPage - 1)"
              :disabled="!hasPrevPage"
              class="size-9 flex items-center justify-center rounded-lg border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-800 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span class="material-symbols-outlined">chevron_right</span>
            </button>
            <button 
              v-for="page in Math.min(totalPages, 5)" 
              :key="page"
              @click="loadPage(page)"
              :class="currentPage === page ? 'bg-primary text-white' : 'border border-slate-200 dark:border-slate-800 text-slate-900 dark:text-white hover:bg-slate-50 dark:hover:bg-slate-800'"
              class="size-9 flex items-center justify-center rounded-lg font-bold text-sm"
            >
              {{ page }}
            </button>
            <button 
              @click="loadPage(currentPage + 1)"
              :disabled="!hasNextPage"
              class="size-9 flex items-center justify-center rounded-lg border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-800 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span class="material-symbols-outlined">chevron_left</span>
            </button>
          </div>
        </div>

        <!-- Past Events Banner -->
        <div class="mt-12 bg-primary/5 dark:bg-primary/10 rounded-xl p-8 flex flex-col md:flex-row items-center justify-between gap-6 border border-primary/10">
          <div class="flex flex-col gap-2 text-center md:text-right">
            <h2 class="text-slate-900 dark:text-white text-xl font-bold">{{ $t('events.archiveTitle') }}</h2>
            <p class="text-slate-600 dark:text-slate-400 text-sm">{{ $t('events.archiveDesc') }}</p>
          </div>
          <button class="flex items-center gap-2 px-6 py-3 bg-white dark:bg-slate-800 text-primary border border-primary/20 rounded-lg font-bold text-sm hover:bg-primary/5 transition-all">
            {{ $t('events.viewArchive') }}
            <span class="material-symbols-outlined">history</span>
          </button>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { getApiUrl } from '@/utils/api';

type EventItem = {
  id: number;
  title: string;
  slug: string;
  description: string;
  event_type: string;
  event_type_code?: string;
  image: string | null;
  location: string;
  start_date: string;
  end_date: string;
  registration_deadline: string | null;
  max_participants: number | null;
  price: number;
  is_published: boolean;
  is_featured: boolean;
  is_registration_open: boolean;
  views: number;
  created_at: string;
};

const activeTab = ref('current');
const selectedFilter = ref('all');
const eventItems = ref<EventItem[]>([]);
const eventsLoading = ref(true);
const eventsError = ref<string | null>(null);
const currentPage = ref(1);
const totalPages = ref(1);
const hasNextPage = ref(false);
const hasPrevPage = ref(false);

const tabs = ref([
  { id: 'current', name: 'رویدادهای جاری (آماده ثبت‌نام)' },
  { id: 'past', name: 'رویدادهای گذشته' }
]);

const filters = ref([
  { id: 'all', name: 'همه' },
  { id: 'congress', name: 'کنگره سالانه' },
  { id: 'webinar', name: 'وبینار' },
  { id: 'workshop', name: 'کارگاه آموزشی' }
]);

const formatDate = (isoDate: string | null) => {
  if (!isoDate) return '';
  try {
    return new Date(isoDate).toLocaleDateString('fa-IR', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });
  } catch (error) {
    return isoDate;
  }
};

const isEventFinished = (event: EventItem): boolean => {
  if (!event.is_registration_open) {
    return true;
  }
  if (event.registration_deadline) {
    const deadline = new Date(event.registration_deadline);
    const now = new Date();
    deadline.setHours(23, 59, 59, 999);
    if (deadline < now) {
      return true;
    }
  }
  if (event.end_date) {
    const endDate = new Date(event.end_date);
    const now = new Date();
    return endDate < now;
  }
  return false;
};

const activeEvents = computed(() => {
  return eventItems.value.filter(event => !isEventFinished(event));
});

const finishedEvents = computed(() => {
  return eventItems.value.filter(event => isEventFinished(event));
});

const filteredEvents = computed(() => {
  const events = activeTab.value === 'current' ? activeEvents.value : finishedEvents.value;
  
  return events.map(event => ({
    id: event.id,
    title: event.title,
    date: formatDate(event.start_date) + (event.end_date ? ' تا ' + formatDate(event.end_date) : ''),
    location: event.location,
    locationIcon: 'location_on',
    status: event.is_registration_open ? 'active' : 'closed',
    statusText: event.is_registration_open ? 'در حال ثبت‌نام' : 'ثبت‌نام بسته',
    statusClass: event.is_registration_open ? 'bg-green-500' : 'bg-gray-500',
    badge: event.registration_deadline ? `مهلت ثبت‌نام: ${formatDate(event.registration_deadline)}` : null,
    badgeIcon: 'timer',
    badgeClass: 'text-red-600 bg-red-50',
    buttonText: event.is_registration_open ? 'ثبت‌نام در رویداد' : 'مشاهده جزئیات',
    image: event.image ? getApiUrl(event.image) : '/img/hero-events.svg',
    slug: event.slug,
    type: event.event_type,
    filter: event.event_type_code || 'other'
  })).filter(event => {
    if (selectedFilter.value === 'all') return true;
    return event.filter === selectedFilter.value;
  });
});

const loadPage = async (page: number) => {
  if (page < 1 || page > totalPages.value) return;
  currentPage.value = page;
  await fetchEvents();
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

const fetchEvents = async () => {
  eventsLoading.value = true;
  eventsError.value = null;

  try {
    const response = await fetch(getApiUrl(`/api/events/?page=${currentPage.value}&per_page=12`), {
      credentials: 'include',
    });

    if (response.status === 404) {
      eventItems.value = [];
      eventsLoading.value = false;
      return;
    }

    if (!response.ok) {
      throw new Error(`خطا در دریافت رویدادها از سرور (${response.status})`);
    }

    const data = await response.json();

    if (!data.success || !Array.isArray(data.events)) {
      throw new Error('ساختار داده رویدادها نامعتبر است');
    }

    eventItems.value = data.events;
    
    if (data.pagination) {
      totalPages.value = data.pagination.pages || 1;
      hasNextPage.value = data.pagination.has_next || false;
      hasPrevPage.value = data.pagination.has_prev || false;
    }
  } catch (error: any) {
    console.error('Failed to load events:', error);
    eventsError.value = error.message || 'خطای ناشناخته هنگام دریافت رویدادها';
  } finally {
    eventsLoading.value = false;
  }
};

onMounted(() => {
  fetchEvents();
});
</script>
