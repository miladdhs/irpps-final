<template>
  <div class="page-shell news-detail-view">
    <section class="hero-section glass-section py-5 mb-4">
      <div class="container-xl">
        <nav class="breadcrumb-nav mb-3">
          <router-link to="/services#news-section" class="breadcrumb-link">
            <i class="fa fa-chevron-right"></i>
            بازگشت به خدمات
          </router-link>
        </nav>
        <div class="row align-items-center">
          <div class="col-lg-8">
            <h1 class="display-6 fw-bold text-primary mb-3">{{ newsItem?.title || 'بارگذاری...' }}</h1>
            <div v-if="newsItem" class="meta d-flex flex-wrap gap-3 text-muted">
              <span><i class="fa fa-calendar me-2"></i>{{ formatDate(newsItem.created_at) }}</span>
              <span><i class="fa fa-user me-2"></i>{{ newsItem.author }}</span>
              <span><i class="fa fa-eye me-2"></i>{{ newsItem.views.toLocaleString() }} بازدید</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="detail-section pb-5">
      <div class="container-xl">
        <div v-if="loading" class="text-center py-5">
          <i class="fa fa-spinner fa-spin fa-3x col_blue"></i>
          <p class="mt-3 text-muted">در حال بارگذاری خبر...</p>
        </div>

        <div v-else-if="errorMessage" class="alert alert-danger border-0 rounded-4">
          <i class="fa fa-exclamation-triangle me-2"></i>{{ errorMessage }}
        </div>

        <article v-else-if="newsItem" class="news-article glass-card p-4 p-md-5">
          <div v-if="newsItem.image" class="article-image mb-4">
            <img :src="newsItem.image" :alt="newsItem.title">
          </div>
          <div class="article-content" v-html="formattedContent"></div>
        </article>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import { getApiUrl } from '@/utils/api';

type NewsDetail = {
  id: number;
  title: string;
  slug: string;
  content: string;
  image: string | null;
  author: string;
  views: number;
  created_at: string;
  updated_at: string;
};

const route = useRoute();

const newsItem = ref<NewsDetail | null>(null);
const loading = ref(true);
const errorMessage = ref<string | null>(null);

const formatDate = (isoDate: string) => {
  try {
    return new Date(isoDate).toLocaleDateString('fa-IR');
  } catch (error) {
    console.warn('Unable to format date:', isoDate, error);
    return isoDate;
  }
};

const formattedContent = computed(() => {
  if (!newsItem.value) {
    return '';
  }

  // تبدیل خط جدید به پاراگراف برای نمایش تمیز
  return newsItem.value.content
    .split(/\n{2,}/)
    .map((paragraph) => `<p>${paragraph.trim().replace(/\n/g, '<br>')}</p>`)
    .join('');
});

const fetchNewsDetail = async (slug: string) => {
  if (!slug) {
    errorMessage.value = 'شناسه خبر نامعتبر است.';
    return;
  }

  loading.value = true;
  errorMessage.value = null;

  try {
    const response = await fetch(getApiUrl(`/api/news/${encodeURIComponent(slug)}/`), {
      credentials: 'include',
    });

    if (response.status === 404) {
      throw new Error('خبر مورد نظر پیدا نشد یا منتشر نشده است.');
    }

    if (!response.ok) {
      throw new Error('خطا در دریافت اطلاعات خبر از سرور.');
    }

    const data = await response.json();

    if (!data.success || !data.news) {
      throw new Error('ساختار داده خبر نامعتبر است.');
    }

    newsItem.value = data.news;
  } catch (error: any) {
    console.error('Failed to load news detail:', error);
    errorMessage.value = error.message || 'خطای ناشناخته هنگام دریافت خبر.';
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
      fetchNewsDetail(slug);
    }
  }
);

onMounted(() => {
  const slug = resolveSlug();
  if (slug) {
    fetchNewsDetail(slug);
  } else {
    errorMessage.value = 'شناسه خبر نامعتبر است.';
  }
});
</script>

<style scoped>
.news-detail-view {
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

.news-article {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 24px;
  box-shadow: 0 20px 45px rgba(15, 23, 42, 0.12);
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

@media (max-width: 575.98px) {
  .hero-section {
    border-radius: 0 0 24px 24px;
  }
}
</style>

