<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1024px] grow px-6 py-8 lg:px-10">
        <nav class="mb-6 flex items-center gap-2 text-sm text-slate-500">
          <router-link to="/" class="hover:text-primary">{{ $t('nav.home') }}</router-link>
          <span class="material-symbols-outlined text-[16px]">chevron_left</span>
          <router-link to="/events" class="hover:text-primary">{{ $t('nav.eventsItem') }}</router-link>
          <span class="material-symbols-outlined text-[16px]">chevron_left</span>
          <span class="text-slate-900 dark:text-white">{{ detailLabel }}</span>
        </nav>

        <div v-if="eventLoading" class="p-12 text-center">
          <div class="inline-block h-12 w-12 animate-spin rounded-full border-b-2 border-primary"></div>
          <p class="mt-4 text-slate-500">{{ $t('services.loadingEvents') }}</p>
        </div>

        <div v-else-if="eventError" class="p-6">
          <div class="rounded-xl border border-red-200 bg-red-50 p-6 text-center dark:border-red-800 dark:bg-red-900/20">
            <span class="material-symbols-outlined mb-2 text-4xl text-red-600">error</span>
            <p class="text-red-600 dark:text-red-400">{{ eventError }}</p>
          </div>
        </div>

        <div v-else-if="event" class="grid grid-cols-1 gap-8 lg:grid-cols-3">
          <div class="lg:col-span-2">
            <article class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
              <div class="mb-6">
                <div class="mb-4 inline-block rounded-full px-4 py-2 text-sm font-bold text-white" :class="statusClass">
                  {{ statusLabel }}
                </div>
                <h1 class="mb-4 text-3xl font-black leading-tight md:text-4xl">{{ event.title }}</h1>
              </div>

              <div class="mb-8 aspect-video overflow-hidden rounded-xl bg-slate-100 dark:bg-slate-800">
                <img :src="event.image || '/img/events.png'" :alt="event.title" class="h-full w-full object-contain" />
              </div>

              <div class="prose prose-slate max-w-none dark:prose-invert">
                <h2 class="mb-4 text-2xl font-bold">{{ aboutLabel }}</h2>
                <div v-html="event.description" class="leading-relaxed"></div>
              </div>
            </article>
          </div>

          <div class="lg:col-span-1">
            <div class="sticky top-24 flex flex-col gap-6">
              <div class="rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                <h3 class="mb-4 text-lg font-bold">{{ infoLabel }}</h3>
                <div class="flex flex-col gap-4">
                  <div class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-primary">calendar_month</span>
                    <div>
                      <div class="text-sm font-medium text-slate-500 dark:text-slate-400">{{ dateLabel }}</div>
                      <div class="font-medium">{{ eventDate }}</div>
                    </div>
                  </div>

                  <div class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-primary">location_on</span>
                    <div>
                      <div class="text-sm font-medium text-slate-500 dark:text-slate-400">{{ locationLabel }}</div>
                      <div class="font-medium">{{ event.location }}</div>
                    </div>
                  </div>

                  <div v-if="event.max_participants" class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-primary">group</span>
                    <div>
                      <div class="text-sm font-medium text-slate-500 dark:text-slate-400">{{ capacityLabel }}</div>
                      <div class="font-medium">{{ event.max_participants }}</div>
                    </div>
                  </div>

                  <div v-if="event.retraining_number" class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-primary">badge</span>
                    <div>
                      <div class="text-sm font-medium text-slate-500 dark:text-slate-400">{{ retrainingLabel }}</div>
                      <div class="text-lg font-bold text-primary">{{ event.retraining_number }}</div>
                    </div>
                  </div>
                </div>

                <button
                  v-if="!event.retraining_number && event.status_code === 'registration_open'"
                  @click="showRegistrationForm = true"
                  class="mt-6 w-full rounded-lg bg-primary py-3 font-bold text-white transition-colors hover:bg-primary/90"
                >
                  {{ registerLabel }}
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>

    <div
      v-if="showRegistrationForm"
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4"
      @click.self="showRegistrationForm = false"
    >
      <div class="w-full max-w-lg rounded-xl border border-slate-200 bg-white p-6 shadow-xl dark:border-slate-800 dark:bg-slate-900">
        <div class="mb-4 flex items-center justify-between">
          <h2 class="text-2xl font-bold">{{ registerLabel }}</h2>
          <button @click="showRegistrationForm = false" class="rounded-lg p-2 hover:bg-slate-100 dark:hover:bg-slate-800">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>
        <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">
          {{ locale === 'fa' ? 'ثبت‌نام مستقیم این رویداد هنوز در این صفحه پیاده‌سازی نشده است. جزئیات رویداد را از پنل مدیریت یا مسیر ثبت‌نام اختصاصی کامل کنید.' : 'Direct registration is not wired on this page yet. Complete event registration through the dedicated backend flow or admin panel.' }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { getApiUrl } from '@/utils/api';

const route = useRoute();
const { locale, t } = useI18n();
const showRegistrationForm = ref(false);
const event = ref<any>(null);
const eventLoading = ref(true);
const eventError = ref<string | null>(null);

const detailLabel = computed(() => (locale.value === 'fa' ? 'جزئیات رویداد' : 'Event Details'));
const aboutLabel = computed(() => (locale.value === 'fa' ? 'درباره رویداد' : 'About this event'));
const infoLabel = computed(() => (locale.value === 'fa' ? 'اطلاعات رویداد' : 'Event Information'));
const dateLabel = computed(() => (locale.value === 'fa' ? 'تاریخ' : 'Date'));
const locationLabel = computed(() => (locale.value === 'fa' ? 'مکان' : 'Location'));
const capacityLabel = computed(() => (locale.value === 'fa' ? 'ظرفیت' : 'Capacity'));
const retrainingLabel = computed(() => (locale.value === 'fa' ? 'شماره بازآموزی' : 'Retraining No.'));
const registerLabel = computed(() => (locale.value === 'fa' ? 'ثبت‌نام در رویداد' : 'Register for Event'));

const statusMap: Record<string, { fa: string; en: string; className: string }> = {
  registration_open: { fa: 'در حال ثبت‌نام', en: 'Open', className: 'bg-green-500' },
  registration_closed: { fa: 'ثبت‌نام بسته', en: 'Closed', className: 'bg-amber-500' },
  ended: { fa: 'برگزار شده', en: 'Ended', className: 'bg-slate-500' },
};

const statusCode = computed(() => event.value?.status_code || 'registration_closed');
const statusClass = computed(() => statusMap[statusCode.value]?.className || 'bg-slate-500');
const statusLabel = computed(() => {
  const meta = statusMap[statusCode.value] || statusMap.registration_closed;
  return locale.value === 'fa' ? meta.fa : meta.en;
});

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

const eventDate = computed(() => {
  if (!event.value) {
    return '';
  }

  return event.value.end_date
    ? `${formatDate(event.value.start_date)} - ${formatDate(event.value.end_date)}`
    : formatDate(event.value.start_date);
});

const fetchEvent = async () => {
  eventLoading.value = true;
  eventError.value = null;

  try {
    const slug = route.params.slug as string;
    const response = await fetch(getApiUrl(`/api/events/${slug}/`), {
      credentials: 'include',
      cache: 'no-store',
    });

    if (!response.ok) {
      throw new Error(`Failed to load event (${response.status})`);
    }

    const data = await response.json();

    if (!data.success || !data.event) {
      throw new Error('Invalid event response');
    }

    event.value = {
      ...data.event,
      image: data.event.image ? getApiUrl(data.event.image) : '/img/events.png',
    };
  } catch (error: any) {
    console.error('Failed to load event:', error);
    eventError.value = error.message || t('common.error');
  } finally {
    eventLoading.value = false;
  }
};

onMounted(() => {
  fetchEvent();
});
</script>
