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
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
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
          <div class="p-6 border-t border-slate-200 dark:border-slate-800 flex items-center justify-center gap-2">
            <button class="size-9 flex items-center justify-center rounded-lg border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-800">
              <span class="material-symbols-outlined">chevron_right</span>
            </button>
            <button class="size-9 flex items-center justify-center rounded-lg bg-primary text-white font-bold text-sm">۱</button>
            <button class="size-9 flex items-center justify-center rounded-lg border border-slate-200 dark:border-slate-800 text-slate-900 dark:text-white hover:bg-slate-50 dark:hover:bg-slate-800 text-sm">۲</button>
            <button class="size-9 flex items-center justify-center rounded-lg border border-slate-200 dark:border-slate-800 text-slate-900 dark:text-white hover:bg-slate-50 dark:hover:bg-slate-800 text-sm">۳</button>
            <button class="size-9 flex items-center justify-center rounded-lg border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-800">
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
import { ref, computed } from 'vue';

const activeTab = ref('current');
const selectedFilter = ref('all');

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

const events = ref([
  {
    id: 1,
    title: 'نهمین کنگره بیماری‌های ریوی کودکان و نوزادان ایران',
    date: '۲۵ لغایت ۲۷ مهر ۱۴۰۳',
    location: 'تهران، مرکز طبی کودکان - تالار همایش‌ها',
    locationIcon: 'location_on',
    status: 'active',
    statusText: 'در حال ثبت‌نام',
    statusClass: 'bg-green-500',
    badge: 'مهلت ثبت‌نام: تا ۱۵ مهر',
    badgeIcon: 'timer',
    badgeClass: 'text-red-600 bg-red-50',
    buttonText: 'ثبت‌نام در کنگره',
    image: '/img/event1.jpg',
    slug: 'congress-2024',
    type: null,
    filter: 'congress'
  },
  {
    id: 2,
    title: 'وبینار کشوری تازه‌های تشخیص و درمان آسم در اطفال',
    date: '۱۰ آبان ۱۴۰۳ | ساعت ۱۸ تا ۲۰',
    location: 'پلتفرم اسکای‌روم (آنلاین)',
    locationIcon: 'video_library',
    status: 'limited',
    statusText: 'ظرفیت محدود',
    statusClass: 'bg-amber-500',
    type: 'وبینار آنلاین',
    badge: 'دارای امتیاز بازآموزی برای پزشکان عمومی و اطفال',
    badgeIcon: 'school',
    badgeClass: 'text-primary bg-primary/5',
    buttonText: 'رزرو صندلی مجازی',
    image: '/img/event2.jpg',
    slug: 'asthma-webinar',
    filter: 'webinar'
  },
  {
    id: 3,
    title: 'کارگاه آموزشی پیشرفته اسپیرومتری و تفسیر نوار ریه',
    date: '۱۵ آذر ۱۴۰۳',
    location: 'تهران، هتل المپیک - سالن نشست‌های تخصصی',
    locationIcon: 'location_on',
    status: 'active',
    statusText: 'در حال ثبت‌نام',
    statusClass: 'bg-green-500',
    badge: 'ویژه پرستاران و تکنیسین‌های تنفسی',
    badgeIcon: 'info',
    badgeClass: 'text-slate-600 dark:text-slate-400 bg-slate-50 dark:bg-slate-800 italic',
    buttonText: 'ثبت‌نام کارگاه',
    image: '/img/event3.jpg',
    slug: 'spirometry-workshop',
    type: null,
    filter: 'workshop'
  }
]);

const filteredEvents = computed(() => {
  if (selectedFilter.value === 'all') {
    return events.value;
  }
  return events.value.filter(event => event.filter === selectedFilter.value);
});
</script>
