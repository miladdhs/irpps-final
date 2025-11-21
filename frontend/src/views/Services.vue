<template>
  <div class="page-shell services-view position-relative overflow-hidden">
    <span class="services-bubble bubble-1 blurred-bubble"></span>
    <span class="services-bubble bubble-2 blurred-bubble"></span>

    <section id="services-hero" class="services-hero-section page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center min-vh-80">
          <div class="col-md-6">
            <div class="services-hero-content animate__animated animate__fadeInRight">
              <span class="soft-badge mb-3"><i class="fa fa-calendar"></i> {{ $t('services.badge') }}</span>
              <h1 class="display-4 fw-bold mb-4">{{ $t('services.title') }}</h1>
              <p class="lead mb-4">{{ $t('services.subtitle') }}</p>
              <p class="mb-4 text-muted">{{ $t('services.description') }}</p>
              <div class="services-hero-buttons d-flex flex-wrap gap-2">
                <a class="soft-button primary animate__animated animate__pulse" href="#news-section">
                  <i class="fa fa-newspaper"></i>
                  {{ $t('services.news') }}
                </a>
                <a class="soft-button outline" href="#events-section">
                  <i class="fa fa-calendar"></i>
                  {{ $t('services.events') }}
                </a>
                <a class="soft-button outline" href="#announcements-section">
                  <i class="fa fa-bullhorn"></i>
                  {{ $t('services.announcements') }}
                </a>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="services-hero-image animate__animated animate__fadeInLeft">
              <div class="services-hero-image-wrapper image-frame image-frame--wide">
                <img :src="getAssetUrl('img/hero-events.svg')" class="img-fluid" alt="خدمات انجمن">
                <div class="floating-elements">
                  <div class="floating-icon floating-icon-1">
                    <i class="fa fa-newspaper"></i>
                  </div>
                  <div class="floating-icon floating-icon-2">
                    <i class="fa fa-bullhorn"></i>
                  </div>
                  <div class="floating-icon floating-icon-3">
                    <i class="fa fa-calendar"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row text-center mb-5 section-heading">
          <div class="col-md-12">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">{{ $t('services.servicesTitle') }}</h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('services.servicesSubtitle') }}</p>
          </div>
        </div>
        <div class="row g-4">
          <div class="col-md-6 col-lg-4" v-for="(service, index) in serviceCards" :key="service.title">
            <div class="service-card glass-card p-4 animate__animated animate__fadeInUp" :class="'animate__delay-' + (index + 2) + 's'">
              <div class="service-icon mb-4">
                <i :class="'fa fa-2x col_blue ' + service.icon"></i>
              </div>
              <h5 class="fw-bold mb-3">{{ service.title }}</h5>
              <p class="text-muted">{{ service.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- News Section -->
    <section id="news-section" class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row">
          <div class="col-md-12 text-center mb-5 section-heading">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">
              <i class="fa fa-newspaper me-2 col_blue"></i>
              {{ $t('services.newsTitle') }}
            </h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('services.newsSubtitle') }}</p>
          </div>
        </div>

        <div v-if="newsLoading" class="text-center py-5">
          <i class="fa fa-spinner fa-spin fa-3x col_blue"></i>
          <p class="mt-3 text-muted">{{ $t('services.loadingNews') }}</p>
        </div>

        <div v-else-if="newsError" class="alert alert-danger border-0 rounded-4">
          <i class="fa fa-exclamation-triangle me-2"></i>{{ newsError }}
        </div>

        <div v-else>
          <div v-if="newsItems.length === 0" class="empty-state glass-card text-center p-5">
            <i class="fa fa-info-circle fa-2x mb-3 text-primary"></i>
            <h5 class="fw-bold mb-2">{{ $t('services.noNews') }}</h5>
            <p class="text-muted mb-0">{{ $t('services.noNewsDesc') }}</p>
          </div>

          <div v-else class="row g-4">
            <div class="col-lg-4 col-md-6" v-for="item in newsItems.slice(0, 6)" :key="item.id">
              <article class="news-card glass-card h-100">
                <div class="news-card-image" v-if="item.image">
                  <img :src="item.image" :alt="item.title">
                </div>
                <div class="news-card-body">
                  <span class="news-card-meta">
                    <i class="fa fa-calendar me-1"></i>
                    {{ formatDate(item.created_at) }}
                  </span>
                  <h3 class="news-card-title">{{ item.title }}</h3>
                  <p class="news-card-content">{{ item.content }}</p>
                  <div class="news-card-footer">
                    <router-link :to="`/news/${item.slug}`" class="soft-button primary">
                      <i class="fa fa-arrow-left me-2"></i>
                      {{ $t('services.readMore') }}
                    </router-link>
                  </div>
                </div>
              </article>
            </div>
          </div>

          <div v-if="newsItems.length > 6" class="text-center mt-4">
            <router-link to="/services#news-section" class="soft-button outline">
              {{ $t('services.viewAll') }} {{ $t('services.news') }}
              <i class="fa fa-arrow-left me-2"></i>
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Events Section -->
    <section id="events-section" class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row">
          <div class="col-md-12 text-center mb-5 section-heading">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">
              <i class="fa fa-calendar me-2 col_blue"></i>
              {{ $t('services.eventsTitle') }}
            </h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('services.eventsSubtitle') }}</p>
          </div>
        </div>

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
            <div class="col-lg-4 col-md-6" v-for="event in eventItems.slice(0, 6)" :key="event.id">
              <article class="event-card glass-card h-100">
                <div class="event-card-image" v-if="event.image">
                  <img :src="event.image" :alt="event.title">
                </div>
                <div class="event-card-body">
                  <div class="event-card-meta">
                    <span>
                      <i class="fa fa-calendar-alt me-1"></i>
                      {{ formatDateTime(event.start_date) }}
                    </span>
                    <span class="badge rounded-pill" :class="event.is_featured ? 'bg-primary' : 'bg-secondary'">
                      {{ event.is_featured ? 'ویژه' : event.event_type }}
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

          <div v-if="eventItems.length > 6" class="text-center mt-4">
            <router-link to="/services#events-section" class="soft-button outline">
              {{ $t('services.viewAll') }} {{ $t('services.events') }}
              <i class="fa fa-arrow-left me-2"></i>
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Announcements Section -->
    <section id="announcements-section" class="p_3 glass-section">
      <div class="container-xl">
        <div class="row">
          <div class="col-md-12 text-center mb-5 section-heading">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">
              <i class="fa fa-bullhorn me-2 col_blue"></i>
              {{ $t('services.announcementsTitle') }}
            </h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('services.announcementsSubtitle') }}</p>
          </div>
        </div>

        <div v-if="announcementsLoading" class="text-center py-5">
          <i class="fa fa-spinner fa-spin fa-3x col_blue"></i>
          <p class="mt-3 text-muted">{{ $t('services.loadingAnnouncements') }}</p>
        </div>

        <div v-else-if="announcementsError" class="alert alert-danger border-0 rounded-4">
          <i class="fa fa-exclamation-triangle me-2"></i>{{ announcementsError }}
        </div>

        <div v-else>
          <div v-if="announcementItems.length === 0" class="empty-state glass-card text-center p-5">
            <i class="fa fa-info-circle fa-2x mb-3 text-primary"></i>
            <h5 class="fw-bold mb-2">{{ $t('services.noAnnouncements') }}</h5>
            <p class="text-muted mb-0">{{ $t('services.noAnnouncementsDesc') }}</p>
          </div>

          <div v-else class="row g-4">
            <div class="col-lg-6" v-for="item in announcementItems.slice(0, 6)" :key="item.id">
              <article class="announcement-card glass-card h-100">
                <div class="announcement-card-body">
                  <div class="announcement-card-header">
                    <span class="announcement-meta">
                      <i class="fa fa-calendar me-1"></i>
                      {{ formatDate(item.created_at) }}
                    </span>
                    <span
                      class="badge rounded-pill"
                      :class="item.is_important ? 'bg-danger' : 'bg-secondary'"
                    >
                      {{ item.is_important ? $t('services.important') : $t('services.normal') }}
                    </span>
                  </div>
                  <h3 class="announcement-title">{{ item.title }}</h3>
                  <p class="announcement-content">{{ item.content }}</p>
                  <div class="announcement-footer d-flex justify-content-between align-items-center">
                    <span class="announcement-author">
                      <i class="fa fa-user me-1"></i>
                      {{ item.author }}
                    </span>
                    <span class="announcement-views">
                      <i class="fa fa-eye me-1"></i>
                      {{ item.views.toLocaleString() }} {{ $t('services.views') }}
                    </span>
                  </div>
                </div>
              </article>
            </div>
          </div>

          <div v-if="announcementItems.length > 6" class="text-center mt-4">
            <router-link to="/services#announcements-section" class="soft-button outline">
              {{ $t('services.viewAll') }} {{ $t('services.announcements') }}
              <i class="fa fa-arrow-left me-2"></i>
            </router-link>
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

type AnnouncementItem = {
  id: number;
  title: string;
  slug: string;
  content: string;
  image: string | null;
  author: string;
  is_important: boolean;
  is_published: boolean;
  views: number;
  created_at: string;
};

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

const serviceCards = computed(() => [
  {
    icon: 'fa-graduation-cap',
    title: t('services.service1'),
    description: t('services.service1Desc')
  },
  {
    icon: 'fa-microphone',
    title: t('services.service2'),
    description: t('services.service2Desc')
  },
  {
    icon: 'fa-users',
    title: t('services.service3'),
    description: t('services.service3Desc')
  },
  {
    icon: 'fa-book',
    title: t('services.service4'),
    description: t('services.service4Desc')
  },
  {
    icon: 'fa-flask',
    title: t('services.service5'),
    description: t('services.service5Desc')
  },
  {
    icon: 'fa-certificate',
    title: t('services.service6'),
    description: t('services.service6Desc')
  }
]);

// News
const newsItems = ref<NewsItem[]>([]);
const newsLoading = ref(true);
const newsError = ref<string | null>(null);

// Announcements
const announcementItems = ref<AnnouncementItem[]>([]);
const announcementsLoading = ref(true);
const announcementsError = ref<string | null>(null);

// Events
const eventItems = ref<EventItem[]>([]);
const eventsLoading = ref(true);
const eventsError = ref<string | null>(null);

const formatDate = (isoDate: string) => {
  try {
    return new Date(isoDate).toLocaleDateString('fa-IR');
  } catch (error) {
    console.warn('Unable to format date:', isoDate, error);
    return isoDate;
  }
};

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

const fetchNews = async () => {
  newsLoading.value = true;
  newsError.value = null;

  try {
    const response = await fetch(getApiUrl('/api/news/?page=1&per_page=6'), {
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
  } catch (error: any) {
    console.error('Failed to load news:', error);
    if (import.meta.env.DEV) {
      newsError.value = error.message || 'خطای ناشناخته هنگام دریافت اخبار';
    } else {
      newsItems.value = [];
    }
  } finally {
    newsLoading.value = false;
  }
};

const fetchAnnouncements = async () => {
  announcementsLoading.value = true;
  announcementsError.value = null;

  try {
    const response = await fetch(getApiUrl('/api/news/announcements/?page=1&per_page=6'), {
      credentials: 'include',
    });

    if (response.status === 404) {
      // اگر endpoint وجود ندارد، از داده‌های خالی استفاده می‌کنیم
      announcementItems.value = [];
      announcementsLoading.value = false;
      return;
    }

    if (!response.ok) {
      throw new Error(`خطا در دریافت اطلاعیه‌ها از سرور (${response.status})`);
    }

    const data = await response.json();

    if (!data.success || !Array.isArray(data.announcements)) {
      throw new Error('ساختار داده اطلاعیه‌ها نامعتبر است');
    }

    announcementItems.value = data.announcements;
  } catch (error: any) {
    console.error('Failed to load announcements:', error);
    // اگر خطا رخ داد، فقط در حالت development نمایش می‌دهیم
    if (import.meta.env.DEV) {
      announcementsError.value = error.message || 'خطای ناشناخته هنگام دریافت اطلاعیه‌ها';
    } else {
      // در production، فقط لیست خالی نمایش می‌دهیم
      announcementItems.value = [];
    }
  } finally {
    announcementsLoading.value = false;
  }
};

const fetchEvents = async () => {
  eventsLoading.value = true;
  eventsError.value = null;

  try {
    const response = await fetch(getApiUrl('/api/events/?page=1&per_page=6'), {
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
  fetchNews();
  fetchAnnouncements();
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

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector((this as HTMLElement).getAttribute('href') || '');
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
});
</script>

<style scoped>
.news-card {
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.news-card-image img {
  width: 100%;
  height: 220px;
  object-fit: cover;
}

.news-card-body {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  flex: 1;
}

.news-card-meta {
  font-size: 0.9rem;
  color: #5f6f8d;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
}

.news-card-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: #14233c;
  margin: 0;
}

.news-card-content {
  color: #4b5d77;
  flex: 1;
  line-height: 1.7;
  margin-bottom: 0;
}

.news-card-footer {
  display: flex;
  justify-content: flex-end;
}

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

.announcement-card {
  border-radius: 24px;
  padding: 1.6rem;
}

.announcement-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.announcement-meta {
  font-size: 0.9rem;
  color: #5f6f8d;
}

.announcement-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #14233c;
  margin-bottom: 0.75rem;
}

.announcement-content {
  color: #4b5d77;
  line-height: 1.8;
  margin-bottom: 1.25rem;
}

.announcement-footer {
  font-size: 0.9rem;
  color: #5f6f8d;
}

.announcement-footer span {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
}

.empty-state {
  border-radius: 24px;
}

@media (max-width: 575.98px) {
  .news-card-body,
  .event-card-body {
    padding: 1.25rem;
  }

  .news-card-image img {
    height: 190px;
  }
}
</style>
