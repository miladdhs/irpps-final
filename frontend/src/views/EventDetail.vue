<template>
  <div class="event-detail-view">
    <section class="hero-section glass-section py-5 mb-4">
      <div class="container-xl">
        <nav class="breadcrumb-nav mb-3">
          <router-link to="/events" class="breadcrumb-link">
            <i class="fa fa-chevron-right"></i>
            بازگشت به رویدادها
          </router-link>
        </nav>
        <div class="row align-items-center">
          <div class="col-lg-9">
            <h1 class="display-6 fw-bold text-primary mb-3">{{ eventItem?.title || 'بارگذاری...' }}</h1>
            <div v-if="eventItem" class="meta d-flex flex-wrap gap-3 text-muted">
              <span><i class="fa fa-calendar me-2"></i>{{ formatDateTime(eventItem.start_date) }}</span>
              <span><i class="fa fa-map-marker-alt me-2"></i>{{ eventItem.location }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="detail-section pb-5">
      <div class="container-xl">
        <div v-if="loading" class="text-center py-5">
          <i class="fa fa-spinner fa-spin fa-3x col_blue"></i>
          <p class="mt-3 text-muted">در حال بارگذاری اطلاعات رویداد...</p>
        </div>

        <div v-else-if="errorMessage" class="alert alert-danger border-0 rounded-4">
          <i class="fa fa-exclamation-triangle me-2"></i>{{ errorMessage }}
        </div>

        <article v-else-if="eventItem" class="event-article glass-card p-4 p-md-5">
          <div class="article-header mb-4">
            <span class="badge rounded-pill bg-primary">
              شناسه: {{ eventItem.id }}
            </span>
          </div>

          <div v-if="eventItem.image" class="article-image mb-4">
            <img :src="eventItem.image" :alt="eventItem.title">
          </div>

          <div class="article-content" v-html="formattedDescription"></div>

          <div class="event-meta-info row gy-3 mt-4">
            <div class="col-md-4" v-if="eventItem.registration_deadline">
              <div class="info-card">
                <i class="fa fa-hourglass-half"></i>
                <div>
                  <h6 class="fw-bold mb-1">مهلت ثبت‌نام</h6>
                  <p class="mb-0 text-muted">{{ formatDate(eventItem.registration_deadline) }}</p>
                </div>
              </div>
            </div>
            <div class="col-md-4">
              <div class="info-card">
                <i class="fa fa-eye"></i>
                <div>
                  <h6 class="fw-bold mb-1">تعداد بازدید</h6>
                  <p class="mb-0 text-muted">{{ eventItem.views.toLocaleString() }}</p>
                </div>
              </div>
            </div>
          </div>
        </article>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import { getApiUrl } from '@/utils/api';

type EventDetail = {
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
  is_featured: boolean;
  is_registration_open: boolean;
  views: number;
  created_at: string;
};

const route = useRoute();

const eventItem = ref<EventDetail | null>(null);
const loading = ref(true);
const errorMessage = ref<string | null>(null);

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

const formatDate = (isoDate: string | null) => {
  if (!isoDate) return '';
  try {
    return new Date(isoDate).toLocaleDateString('fa-IR', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });
  } catch (error) {
    console.warn('Unable to format date:', isoDate, error);
    return isoDate;
  }
};

const formatPrice = (value: number) => {
  if (!value || value <= 0) {
    return 'رایگان';
  }
  return `${value.toLocaleString('fa-IR')} تومان`;
};

const formattedDescription = computed(() => {
  if (!eventItem.value) {
    return '';
  }
  return eventItem.value.description
    .split(/\n{2,}/)
    .map((paragraph) => `<p>${paragraph.trim().replace(/\n/g, '<br>')}</p>`)
    .join('');
});

const fetchEventDetail = async (slug: string) => {
  if (!slug) {
    errorMessage.value = 'شناسه رویداد نامعتبر است.';
    return;
  }

  loading.value = true;
  errorMessage.value = null;

  try {
    const response = await fetch(getApiUrl(`/api/events/${encodeURIComponent(slug)}/`), {
      credentials: 'include',
    });

    if (response.status === 404) {
      throw new Error('رویداد مورد نظر پیدا نشد یا فعال نیست.');
    }

    if (!response.ok) {
      throw new Error('خطا در دریافت جزئیات رویداد از سرور.');
    }

    const data = await response.json();

    if (!data.success || !data.event) {
      throw new Error('ساختار داده رویداد نامعتبر است.');
    }

    eventItem.value = {
      ...data.event,
      event_type: data.event.event_type || data.event.event_type_code || 'نامشخص',
    };
  } catch (error: any) {
    console.error('Failed to load event detail:', error);
    errorMessage.value = error.message || 'خطای ناشناخته هنگام دریافت رویداد.';
  } finally {
    loading.value = false;
  }
};

const resolveSlug = () => {
  const { slug } = route.params;
  return Array.isArray(slug) ? slug[0] : slug;
};

watch(
  () => route.params.slug,
  (newSlug) => {
    const slug = Array.isArray(newSlug) ? newSlug[0] : newSlug;
    if (slug) {
      fetchEventDetail(slug);
    }
  }
);

onMounted(() => {
  const slug = resolveSlug();
  if (slug) {
    fetchEventDetail(slug);
  } else {
    errorMessage.value = 'شناسه رویداد نامعتبر است.';
  }
});
</script>

<style scoped>
.event-detail-view {
  min-height: 100vh;
  background: #f3f4f8;
  padding-bottom: 3rem;
}

.hero-section {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 0 0 32px 32px;
  box-shadow: 0 20px 50px rgba(15, 23, 42, 0.08);
}

.breadcrumb-nav {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.breadcrumb-link {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  color: #0d6efd;
  font-weight: 600;
  text-decoration: none;
}

.breadcrumb-link i {
  transform: rotate(180deg);
}

.detail-section {
  margin-top: -40px;
}

.event-article {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 24px;
  box-shadow: 0 20px 45px rgba(15, 23, 42, 0.12);
}

.article-header {
  display: flex;
  gap: 0.75rem;
  align-items: center;
}

.status-badge {
  font-size: 0.85rem;
  padding: 0.4rem 0.8rem;
}

.article-image img {
  width: 100%;
  border-radius: 18px;
  object-fit: cover;
}

.article-content p {
  color: #37465e;
  line-height: 2;
  margin-bottom: 1.4rem;
  font-size: 1.05rem;
}

.article-content p:last-child {
  margin-bottom: 0;
}

.info-card {
  display: flex;
  gap: 0.75rem;
  align-items: flex-start;
  padding: 1rem 1.2rem;
  border-radius: 16px;
  background: rgba(248, 250, 255, 0.85);
}

.info-card i {
  font-size: 1.3rem;
  color: #0d6efd;
}

@media (max-width: 575.98px) {
  .hero-section {
    border-radius: 0 0 24px 24px;
  }
}
</style>

