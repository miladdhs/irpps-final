<template>
  <div class="events-view position-relative">
    <span class="events-bubble bubble-1 blurred-bubble"></span>
    <span class="events-bubble bubble-2 blurred-bubble"></span>

    <section id="events-hero" class="events-hero-section page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center min-vh-80">
          <div class="col-md-6">
            <div class="events-hero-content animate__animated animate__fadeInRight">
              <span class="soft-badge mb-3"><i class="fa fa-calendar"></i> {{ $t('services.events') }}</span>
              <h1 class="display-4 fw-bold mb-4">{{ $t('services.eventsTitle') }}</h1>
              <p class="lead mb-4">{{ $t('services.eventsSubtitle') }}</p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="events-hero-image animate__animated animate__fadeInLeft">
              <div class="events-hero-image-wrapper image-frame image-frame--wide">
                <img :src="getAssetUrl('img/hero-events.svg')" class="img-fluid" alt="رویدادهای انجمن">
                <div class="floating-elements">
                  <div class="floating-icon floating-icon-1">
                    <i class="fa fa-calendar"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Events Section -->
    <section id="events-section" class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div v-if="eventsLoading" class="text-center py-5">
          <i class="fa fa-spinner fa-spin fa-3x col_blue"></i>
          <p class="mt-3 text-muted">{{ $t('services.loadingEvents') }}</p>
        </div>

        <div v-else-if="eventsError" class="alert alert-danger border-0 rounded-4">
          <i class="fa fa-exclamation-triangle me-2"></i>{{ eventsError }}
        </div>

        <div v-else>
          <div v-if="eventItems.length === 0" class="empty-state glass-card text-center p-5">
            <i class="fa fa-info-circle fa-2x mb-3 text-primary"></i>
            <h5 class="fw-bold mb-2">{{ $t('services.noEvents') }}</h5>
            <p class="text-muted mb-0">{{ $t('services.noEventsDesc') }}</p>
          </div>

          <div v-else class="row g-4">
            <div class="col-lg-4 col-md-6" v-for="event in eventItems" :key="event.id">
              <article class="event-card glass-card h-100" :class="{ 'event-finished': isEventFinished(event) }">
                <div class="event-card-image" v-if="event.image">
                  <img :src="event.image" :alt="event.title">
                </div>
                <div class="event-card-body">
                  <div class="event-card-meta">
                    <span class="badge rounded-pill" :class="event.is_featured ? 'bg-primary' : 'bg-secondary'">
                      {{ event.is_featured ? 'ویژه' : event.event_type }}
                    </span>
                    <span v-if="isEventFinished(event)" class="badge rounded-pill bg-dark text-white">
                      تمام شده
                    </span>
                  </div>
                  <h3 class="event-card-title">{{ event.title }}</h3>
                  <p class="event-card-content">{{ event.description }}</p>
                  <ul class="event-card-info list-unstyled">
                    <li>
                      <i class="fa fa-map-marker-alt me-2"></i>
                      {{ $t('services.location') }}: {{ event.location }}
                    </li>
                    <li>
                      <i class="fa fa-clock me-2"></i>
                      {{ $t('services.endDate') }}: {{ formatDateTime(event.end_date) }}
                    </li>
                    <li>
                      <i class="fa fa-users me-2"></i>
                      {{ $t('services.capacity') }}: {{ event.max_participants ? event.max_participants : $t('services.unlimited') }}
                    </li>
                    <li>
                      <i class="fa fa-money-bill-wave me-2"></i>
                      {{ $t('services.fee') }}: {{ formatPrice(event.price) }}
                    </li>
                  </ul>
                  <div class="event-card-footer">
                    <span
                      class="badge status-badge"
                      :class="event.is_registration_open ? 'bg-success-subtle text-success' : 'bg-danger-subtle text-danger'"
                    >
                      {{ event.is_registration_open ? $t('services.registrationOpen') : $t('services.registrationClosed') }}
                    </span>
                    <router-link :to="`/events/${event.slug}`" class="soft-button primary">
                      {{ $t('services.details') }}
                      <i class="fa fa-chevron-left me-1"></i>
                    </router-link>
                  </div>
                </div>
              </article>
            </div>
          </div>

          <div v-if="hasNextPage || hasPrevPage" class="text-center mt-5">
            <nav>
              <ul class="pagination justify-content-center">
                <li class="page-item" :class="{ disabled: !hasPrevPage }">
                  <button class="page-link" @click="loadPage(currentPage - 1)" :disabled="!hasPrevPage">
                    <i class="fa fa-chevron-right"></i>
                  </button>
                </li>
                <li class="page-item" v-for="page in visiblePages" :key="page" :class="{ active: page === currentPage }">
                  <button class="page-link" @click="loadPage(page)">{{ page }}</button>
                </li>
                <li class="page-item" :class="{ disabled: !hasNextPage }">
                  <button class="page-link" @click="loadPage(currentPage + 1)" :disabled="!hasNextPage">
                    <i class="fa fa-chevron-left"></i>
                  </button>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, computed } from 'vue';
import { useI18n } from 'vue-i18n';
import { getAssetUrl } from '@/utils/assets';
import { getApiUrl } from '@/utils/api';

const { t } = useI18n();

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

const eventItems = ref<EventItem[]>([]);
const eventsLoading = ref(true);
const eventsError = ref<string | null>(null);
const currentPage = ref(1);
const totalPages = ref(1);
const hasNextPage = ref(false);
const hasPrevPage = ref(false);

const visiblePages = computed(() => {
  const pages = [];
  const maxVisible = 5;
  let start = Math.max(1, currentPage.value - Math.floor(maxVisible / 2));
  let end = Math.min(totalPages.value, start + maxVisible - 1);
  
  if (end - start < maxVisible - 1) {
    start = Math.max(1, end - maxVisible + 1);
  }
  
  for (let i = start; i <= end; i++) {
    pages.push(i);
  }
  
  return pages;
});

const formatDateTime = (isoDate: string) => {
  try {
    return new Date(isoDate).toLocaleString('fa-IR', {
      dateStyle: 'medium',
      timeStyle: 'short',
    });
  } catch (error) {
    console.warn('Unable to format date:', isoDate, error);
    return isoDate;
  }
};

const formatPrice = (value: number) => {
  if (!value || value <= 0) {
    return t('services.free');
  }
  return `${value.toLocaleString('fa-IR')} ${t('services.currency')}`;
};

const isEventFinished = (event: EventItem): boolean => {
  if (!event.is_registration_open) {
    return true;
  }
  if (event.end_date) {
    const endDate = new Date(event.end_date);
    const now = new Date();
    return endDate < now;
  }
  return false;
};

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

    eventItems.value = data.events.map((event: any) => ({
      ...event,
      event_type: event.event_type || event.event_type_code || 'نامشخص',
    }));
    
    if (data.pagination) {
      totalPages.value = data.pagination.pages || 1;
      hasNextPage.value = data.pagination.has_next || false;
      hasPrevPage.value = data.pagination.has_prev || false;
    }
  } catch (error: any) {
    console.error('Failed to load events:', error);
    if (import.meta.env.DEV) {
      eventsError.value = error.message || 'خطای ناشناخته هنگام دریافت رویدادها';
    } else {
      eventItems.value = [];
    }
  } finally {
    eventsLoading.value = false;
  }
};

onMounted(() => {
  fetchEvents();

  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate__animated');
      }
    });
  }, observerOptions);

  document.querySelectorAll('.animate__fadeInUp, .animate__fadeInLeft, .animate__fadeInRight').forEach(el => {
    observer.observe(el);
  });
});
</script>

<style scoped>
.event-card {
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.event-card-image img {
  width: 100%;
  height: 210px;
  object-fit: cover;
}

.event-card-body {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  flex: 1;
}

.event-card-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.9rem;
  color: #5f6f8d;
}

.event-card-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #14233c;
  margin: 0;
}

.event-card-content {
  color: #4b5d77;
  flex: 1;
  line-height: 1.7;
}

.event-card-info li {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  color: #4b5d77;
  margin-bottom: 0.4rem;
}

.event-card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1rem;
}

.status-badge {
  font-size: 0.85rem;
  padding: 0.4rem 0.8rem;
}

.empty-state {
  border-radius: 24px;
}

.pagination .page-link {
  border-radius: 12px;
  margin: 0 4px;
  border: none;
  background: rgba(255, 255, 255, 0.1);
  color: #14233c;
  padding: 0.5rem 1rem;
}

.pagination .page-item.active .page-link {
  background: var(--col_blue, #2563eb);
  color: white;
}

.pagination .page-item.disabled .page-link {
  opacity: 0.5;
  cursor: not-allowed;
}

.event-finished {
  opacity: 0.65;
  filter: grayscale(0.3);
}

.event-finished .event-card-image img {
  filter: grayscale(0.4);
}

.event-finished .event-card-title,
.event-finished .event-card-content,
.event-finished .event-card-info {
  color: #6b7280;
}

@media (max-width: 575.98px) {
  .event-card-body {
    padding: 1.25rem;
  }

  .event-card-image img {
    height: 190px;
  }
}
</style>

