<template>
  <div class="news-view position-relative">
    <span class="news-bubble bubble-1 blurred-bubble"></span>
    <span class="news-bubble bubble-2 blurred-bubble"></span>

    <section id="news-hero" class="news-hero-section page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center min-vh-80">
          <div class="col-md-6">
            <div class="news-hero-content animate__animated animate__fadeInRight">
              <span class="soft-badge mb-3"><i class="fa fa-newspaper"></i> {{ $t('services.news') }}</span>
              <h1 class="display-4 fw-bold mb-4">{{ $t('services.newsTitle') }}</h1>
              <p class="lead mb-4">{{ $t('services.newsSubtitle') }}</p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="news-hero-image animate__animated animate__fadeInLeft">
              <div class="news-hero-image-wrapper image-frame image-frame--wide">
                <img :src="getAssetUrl('img/hero-events.svg')" class="img-fluid" alt="اخبار انجمن">
                <div class="floating-elements">
                  <div class="floating-icon floating-icon-1">
                    <i class="fa fa-newspaper"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- News Section -->
    <section id="news-section" class="p_3 glass-section mb-4">
      <div class="container-xl">
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
            <div class="col-lg-4 col-md-6" v-for="item in newsItems" :key="item.id">
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

const newsItems = ref<NewsItem[]>([]);
const newsLoading = ref(true);
const newsError = ref<string | null>(null);
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

const formatDate = (isoDate: string) => {
  try {
    return new Date(isoDate).toLocaleDateString('fa-IR');
  } catch (error) {
    console.warn('Unable to format date:', isoDate, error);
    return isoDate;
  }
};

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
    if (import.meta.env.DEV) {
      newsError.value = error.message || 'خطای ناشناخته هنگام دریافت اخبار';
    } else {
      newsItems.value = [];
    }
  } finally {
    newsLoading.value = false;
  }
};

onMounted(() => {
  fetchNews();

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

@media (max-width: 575.98px) {
  .news-card-body {
    padding: 1.25rem;
  }

  .news-card-image img {
    height: 190px;
  }
}
</style>

