<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100 font-display">
    <div class="relative flex min-h-screen w-full flex-col overflow-x-hidden">
      <main class="mx-auto flex w-full max-w-[1200px] flex-1 flex-col px-6 py-10 md:px-10">
        <div class="mb-8 flex flex-col gap-4">
          <h1 class="text-4xl font-black tracking-tight text-slate-900 dark:text-white">{{ $t('events.title') }}</h1>
          <p class="max-w-2xl text-lg leading-relaxed text-slate-600 dark:text-slate-400">
            {{ $t('events.subtitle') }}
          </p>
        </div>

        <div class="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm dark:border-slate-800 dark:bg-slate-900">
          <div class="flex gap-10 overflow-x-auto border-b border-slate-200 px-6 dark:border-slate-800">
            <button
              v-for="tab in tabs"
              :key="tab.id"
              class="flex flex-col items-center justify-center whitespace-nowrap border-b-[3px] pb-4 pt-5 transition-colors"
              :class="activeTab === tab.id ? 'border-primary text-slate-900 dark:text-white' : 'border-transparent text-slate-500 hover:text-primary'"
              @click="activeTab = tab.id"
            >
              <span class="text-sm font-bold tracking-tight">{{ tab.name }}</span>
            </button>
          </div>

          <div class="flex flex-wrap items-center justify-between gap-4 bg-slate-50/50 p-6 dark:bg-slate-800/50">
            <div class="flex flex-wrap gap-2">
              <span class="ml-2 py-2 text-sm font-medium text-slate-600 dark:text-slate-400">{{ $t('events.filterBy') }}:</span>
              <button
                v-for="filter in filters"
                :key="filter.id"
                class="rounded-full border px-4 py-1.5 text-sm font-medium transition-colors"
                :class="selectedFilter === filter.id ? 'border-primary/20 bg-primary/10 text-primary' : 'border-slate-200 bg-white text-slate-600 hover:border-primary/30 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-400'"
                @click="selectedFilter = filter.id"
              >
                {{ filter.name }}
              </button>
            </div>
            <div class="text-sm text-slate-600 dark:text-slate-400">
              {{ $t('events.showing') }} {{ filteredEvents.length }} {{ activeTab === 'current' ? currentEventsLabel : archiveEventsLabel }}
            </div>
          </div>

          <div v-if="eventsLoading" class="p-12 text-center">
            <div class="inline-block h-12 w-12 animate-spin rounded-full border-b-2 border-primary"></div>
            <p class="mt-4 text-slate-500">{{ $t('services.loadingEvents') }}</p>
          </div>

          <div v-else-if="eventsError" class="p-6">
            <div class="rounded-xl border border-red-200 bg-red-50 p-6 text-center dark:border-red-800 dark:bg-red-900/20">
              <span class="material-symbols-outlined mb-2 text-4xl text-red-600">error</span>
              <p class="text-red-600 dark:text-red-400">{{ eventsError }}</p>
            </div>
          </div>

          <div v-else-if="filteredEvents.length === 0" class="p-12 text-center">
            <span class="material-symbols-outlined mb-4 text-5xl text-slate-400">info</span>
            <h3 class="mb-2 text-xl font-bold text-slate-900 dark:text-white">{{ $t('services.noEvents') }}</h3>
            <p class="text-slate-500 dark:text-slate-400">{{ $t('services.noEventsDesc') }}</p>
          </div>

          <div v-else class="grid grid-cols-1 gap-6 p-6 md:grid-cols-2 lg:grid-cols-3">
            <div
              v-for="event in filteredEvents"
              :key="event.id"
              class="group flex flex-col overflow-hidden rounded-xl border border-slate-200 bg-white transition-all hover:border-primary/30 hover:shadow-lg dark:border-slate-800 dark:bg-slate-900"
            >
              <div class="relative aspect-[16/9] w-full overflow-hidden bg-slate-100">
                <img
                  :src="event.image"
                  :alt="event.title"
                  class="h-full w-full object-cover"
                  @error="handleEventImageError"
                >
                <div class="absolute right-3 top-3 flex items-center gap-1 rounded-full px-3 py-1 text-[10px] font-bold text-white" :class="event.statusClass">
                  <span v-if="event.statusCode === 'registration_open'" class="size-1.5 animate-pulse rounded-full bg-white"></span>
                  {{ event.statusText }}
                </div>
                <div v-if="event.type" class="absolute left-3 top-3 rounded-full border border-primary/20 bg-white/90 px-3 py-1 text-[10px] font-bold text-primary backdrop-blur-sm">
                  {{ event.type }}
                </div>
                <div class="absolute inset-0 flex items-end bg-gradient-to-t from-black/60 to-transparent p-4 opacity-0 transition-opacity group-hover:opacity-100">
                  <span class="text-xs font-medium text-white">{{ $t('events.viewDetails') }}</span>
                </div>
              </div>

              <div class="flex flex-1 flex-col gap-4 p-5">
                <div class="flex flex-col gap-2">
                  <h3 class="min-h-[3.5rem] text-lg font-bold leading-tight text-slate-900 line-clamp-2 dark:text-white">
                    {{ event.title }}
                  </h3>
                  <div class="flex items-center gap-2 text-xs text-slate-600 dark:text-slate-400">
                    <span class="material-symbols-outlined text-base text-primary">calendar_month</span>
                    <span>{{ event.date }}</span>
                  </div>
                  <div class="flex items-center gap-2 text-xs text-slate-600 dark:text-slate-400">
                    <span class="material-symbols-outlined text-base text-primary">location_on</span>
                    <span>{{ event.location }}</span>
                  </div>

                  <div v-if="event.retrainingNumber" class="mt-1 flex items-center gap-2 rounded-lg border border-primary/20 bg-primary/10 p-3 text-xs font-bold text-primary">
                    <span class="material-symbols-outlined text-base">badge</span>
                    <span>{{ retrainingLabel }}: {{ event.retrainingNumber }}</span>
                  </div>

                  <div v-else-if="event.badge" class="mt-1 flex items-center gap-2 rounded-lg p-2 text-xs font-bold" :class="event.badgeClass">
                    <span class="material-symbols-outlined text-base">{{ event.badgeIcon }}</span>
                    <span>{{ event.badge }}</span>
                  </div>
                </div>

                <div class="mt-auto border-t border-slate-100 pt-4 dark:border-slate-800">
                  <router-link
                    :to="`/events/${event.slug}`"
                    class="flex w-full items-center justify-center rounded-lg bg-primary py-2.5 text-sm font-bold text-white transition-colors hover:bg-primary/90"
                  >
                    {{ event.buttonText }}
                  </router-link>
                </div>
              </div>
            </div>
          </div>

          <div v-if="totalPages > 1" class="flex items-center justify-center gap-2 border-t border-slate-200 p-6 dark:border-slate-800">
            <button
              @click="loadPage(currentPage - 1)"
              :disabled="!hasPrevPage"
              class="flex size-9 items-center justify-center rounded-lg border border-slate-200 text-slate-600 hover:bg-slate-50 dark:border-slate-800 dark:text-slate-400 dark:hover:bg-slate-800 disabled:cursor-not-allowed disabled:opacity-50"
            >
              <span class="material-symbols-outlined">chevron_right</span>
            </button>
            <button
              v-for="page in Math.min(totalPages, 5)"
              :key="page"
              @click="loadPage(page)"
              :class="currentPage === page ? 'bg-primary text-white' : 'border border-slate-200 text-slate-900 hover:bg-slate-50 dark:border-slate-800 dark:text-white dark:hover:bg-slate-800'"
              class="flex size-9 items-center justify-center rounded-lg text-sm font-bold"
            >
              {{ page }}
            </button>
            <button
              @click="loadPage(currentPage + 1)"
              :disabled="!hasNextPage"
              class="flex size-9 items-center justify-center rounded-lg border border-slate-200 text-slate-600 hover:bg-slate-50 dark:border-slate-800 dark:text-slate-400 dark:hover:bg-slate-800 disabled:cursor-not-allowed disabled:opacity-50"
            >
              <span class="material-symbols-outlined">chevron_left</span>
            </button>
          </div>
        </div>

        <div class="mt-12 flex flex-col items-center justify-between gap-6 rounded-xl border border-primary/10 bg-primary/5 p-8 dark:bg-primary/10 md:flex-row">
          <div class="flex flex-col gap-2 text-center md:text-right">
            <h2 class="text-xl font-bold text-slate-900 dark:text-white">{{ $t('events.archiveTitle') }}</h2>
            <p class="text-sm text-slate-600 dark:text-slate-400">{{ $t('events.archiveDesc') }}</p>
          </div>
          <button class="flex items-center gap-2 rounded-lg border border-primary/20 bg-white px-6 py-3 text-sm font-bold text-primary transition-all hover:bg-primary/5 dark:bg-slate-800">
            {{ $t('events.viewArchive') }}
            <span class="material-symbols-outlined">history</span>
          </button>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import { useI18n } from 'vue-i18n';
import { getApiUrl } from '@/utils/api';
import { DEFAULT_EVENT_IMAGE, resolveImageUrl } from '@/utils/assets';

type EventItem = {
  id: number;
  title: string;
  slug: string;
  description: string;
  short_description?: string;
  event_type: string;
  event_type_code?: string;
  image: string | null;
  location: string;
  start_date: string | null;
  end_date: string | null;
  registration_deadline: string | null;
  retraining_number?: string | null;
  max_participants: number | null;
  price: number;
  is_published: boolean;
  is_featured: boolean;
  is_registration_open: boolean;
  has_ended?: boolean;
  status_code?: string;
  views: number;
  created_at: string;
};

const { locale, t } = useI18n();
const activeTab = ref('current');
const selectedFilter = ref('all');
const eventItems = ref<EventItem[]>([]);
const eventsLoading = ref(true);
const eventsError = ref<string | null>(null);
const currentPage = ref(1);
const totalPages = ref(1);
const hasNextPage = ref(false);
const hasPrevPage = ref(false);

const currentEventsLabel = computed(() => (locale.value === 'fa' ? 'رویداد فعال' : 'active events'));
const archiveEventsLabel = computed(() => (locale.value === 'fa' ? 'رویداد آرشیوی' : 'archived events'));
const retrainingLabel = computed(() => (locale.value === 'fa' ? 'شماره بازآموزی' : 'Retraining No.'));
const registerText = computed(() => (locale.value === 'fa' ? 'ثبت‌نام در رویداد' : 'Register'));
const detailsText = computed(() => (locale.value === 'fa' ? 'مشاهده جزئیات' : 'View details'));
const deadlineText = computed(() => (locale.value === 'fa' ? 'مهلت ثبت‌نام' : 'Registration deadline'));

const tabs = computed(() => [
  { id: 'current', name: locale.value === 'fa' ? 'رویدادهای جاری' : 'Current Events' },
  { id: 'past', name: locale.value === 'fa' ? 'رویدادهای گذشته' : 'Past Events' },
]);

const filters = computed(() => [
  { id: 'all', name: locale.value === 'fa' ? 'همه' : 'All' },
  { id: 'congress', name: locale.value === 'fa' ? 'کنگره' : 'Congress' },
  { id: 'conference', name: locale.value === 'fa' ? 'کنفرانس' : 'Conference' },
  { id: 'webinar', name: locale.value === 'fa' ? 'وبینار' : 'Webinar' },
  { id: 'workshop', name: locale.value === 'fa' ? 'کارگاه' : 'Workshop' },
]);

const formatDate = (isoDate: string | null) => {
  if (!isoDate) {
    return '';
  }

  try {
    return new Date(isoDate).toLocaleDateString(locale.value === 'fa' ? 'fa-IR' : 'en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });
  } catch {
    return isoDate;
  }
};

const statusTextMap: Record<string, { fa: string; en: string; className: string }> = {
  registration_open: {
    fa: 'در حال ثبت‌نام',
    en: 'Open',
    className: 'bg-green-500',
  },
  registration_closed: {
    fa: 'ثبت‌نام بسته',
    en: 'Closed',
    className: 'bg-amber-500',
  },
  ended: {
    fa: 'برگزار شده',
    en: 'Ended',
    className: 'bg-slate-500',
  },
};

const normalizedEvents = computed(() =>
  eventItems.value.map((event) => {
    const statusCode = event.status_code || (event.has_ended ? 'ended' : (event.is_registration_open ? 'registration_open' : 'registration_closed'));
    const statusMeta = statusTextMap[statusCode] || statusTextMap.registration_closed;
    const badge = !event.retraining_number && event.registration_deadline
      ? `${deadlineText.value}: ${formatDate(event.registration_deadline)}`
      : null;

    return {
      id: event.id,
      title: event.title,
      date: event.end_date ? `${formatDate(event.start_date)} - ${formatDate(event.end_date)}` : formatDate(event.start_date),
      location: event.location,
      statusCode,
      statusText: locale.value === 'fa' ? statusMeta.fa : statusMeta.en,
      statusClass: statusMeta.className,
      retrainingNumber: event.retraining_number,
      badge,
      badgeIcon: 'timer',
      badgeClass: 'bg-red-50 text-red-600',
      buttonText: statusCode === 'registration_open' && !event.retraining_number ? registerText.value : detailsText.value,
      image: resolveImageUrl(event.image, DEFAULT_EVENT_IMAGE),
      slug: event.slug,
      type: event.event_type,
      filter: event.event_type_code || 'other',
      hasEnded: Boolean(event.has_ended),
    };
  }),
);

const activeEvents = computed(() => normalizedEvents.value.filter((event) => !event.hasEnded));
const finishedEvents = computed(() => normalizedEvents.value.filter((event) => event.hasEnded));

const filteredEvents = computed(() => {
  const items = activeTab.value === 'current' ? activeEvents.value : finishedEvents.value;
  if (selectedFilter.value === 'all') {
    return items;
  }

  return items.filter((event) => event.filter === selectedFilter.value);
});

const loadPage = async (page: number) => {
  if (page < 1 || page > totalPages.value) {
    return;
  }

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
      cache: 'no-store',
    });

    if (response.status === 404) {
      eventItems.value = [];
      return;
    }

    if (!response.ok) {
      throw new Error(`Failed to load events (${response.status})`);
    }

    const data = await response.json();

    if (!data.success || !Array.isArray(data.events)) {
      throw new Error('Invalid events response');
    }

    eventItems.value = data.events;

    if (data.pagination) {
      totalPages.value = data.pagination.pages || 1;
      hasNextPage.value = data.pagination.has_next || false;
      hasPrevPage.value = data.pagination.has_prev || false;
    }
  } catch (error: any) {
    console.error('Failed to load events:', error);
    eventsError.value = error.message || t('common.error');
  } finally {
    eventsLoading.value = false;
  }
};

onMounted(() => {
  fetchEvents();
});

function handleEventImageError(event: Event) {
  const img = event.target as HTMLImageElement
  if (img.src.endsWith(DEFAULT_EVENT_IMAGE)) {
    return
  }
  img.src = DEFAULT_EVENT_IMAGE
}
</script>
