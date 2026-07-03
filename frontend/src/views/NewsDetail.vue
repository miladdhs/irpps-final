<template>
  <div class="bg-background-light text-slate-900 dark:bg-background-dark dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1024px] grow px-6 py-8 lg:px-10">
        <nav class="mb-6 flex items-center gap-2 text-sm text-slate-500">
          <router-link to="/" class="hover:text-primary">{{ $t('nav.home') }}</router-link>
          <span class="material-symbols-outlined text-[16px]">chevron_left</span>
          <router-link to="/news" class="hover:text-primary">{{ $t('nav.news') }}</router-link>
          <span class="material-symbols-outlined text-[16px]">chevron_left</span>
          <span class="text-slate-900 dark:text-white">{{ breadcrumbLabel }}</span>
        </nav>

        <div v-if="loading" class="rounded-xl bg-slate-50 p-12 text-center dark:bg-slate-900/50">
          <div class="mx-auto inline-block h-12 w-12 animate-spin rounded-full border-b-2 border-primary"></div>
          <p class="mt-4 text-slate-500 dark:text-slate-400">{{ loadingText }}</p>
        </div>

        <div v-else-if="error" class="rounded-xl border border-red-200 bg-red-50 p-6 text-center dark:border-red-800 dark:bg-red-900/20">
          <span class="material-symbols-outlined mb-2 text-4xl text-red-600">error</span>
          <p class="text-red-600 dark:text-red-400">{{ error }}</p>
        </div>

        <article v-else-if="newsItem" class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
          <div class="mb-6">
            <div v-if="newsItem.category" class="mb-4 inline-block rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary">
              {{ newsItem.category }}
            </div>
            <h1 class="mb-4 text-3xl font-black leading-tight md:text-4xl">
              {{ newsItem.title }}
            </h1>
            <div class="flex flex-wrap items-center gap-4 text-sm text-slate-500">
              <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[18px]">person</span>
                <span>{{ newsItem.author }}</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[18px]">calendar_today</span>
                <span>{{ formatDate(newsItem.created_at) }}</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-[18px]">visibility</span>
                <span>{{ newsItem.views }} {{ viewsLabel }}</span>
              </div>
            </div>
          </div>

          <div class="mb-8 aspect-video overflow-hidden rounded-xl bg-slate-100 dark:bg-slate-800">
            <img
              :src="newsImage"
              :alt="newsItem.title"
              class="h-full w-full object-contain p-4"
            />
          </div>

          <div v-if="newsItem.short_content" class="mb-6 rounded-xl bg-slate-50 p-5 text-base leading-8 text-slate-700 dark:bg-slate-800 dark:text-slate-200">
            {{ newsItem.short_content }}
          </div>

          <div class="prose prose-slate max-w-none dark:prose-invert">
            <div v-html="renderedContent"></div>
          </div>

          <div v-if="tagList.length" class="mt-8 flex flex-wrap gap-2 border-t border-slate-200 pt-6 dark:border-slate-800">
            <span
              v-for="tag in tagList"
              :key="tag"
              class="rounded-full bg-slate-100 px-4 py-2 text-sm font-medium dark:bg-slate-800"
            >
              {{ tag }}
            </span>
          </div>

          <div class="mt-6 flex flex-wrap items-center gap-4 border-t border-slate-200 pt-6 dark:border-slate-800">
            <span class="font-medium">{{ sourceLabel }}</span>
            <a
              v-if="newsItem.source"
              :href="newsItem.source"
              target="_blank"
              rel="noopener"
              class="text-primary underline-offset-4 hover:underline"
            >
              {{ sourceLinkLabel }}
            </a>
          </div>
        </article>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'

import { getApiUrl } from '@/utils/api'

type NewsDetailItem = {
  id: number
  title: string
  slug: string
  content: string
  short_content: string
  category: string
  tags: string
  source: string
  image: string | null
  author: string
  views: number
  created_at: string
  updated_at: string
}

type NewsDetailResponse = {
  success: boolean
  news?: NewsDetailItem
}

const route = useRoute()
const { locale } = useI18n()

const loading = ref(true)
const error = ref<string | null>(null)
const newsItem = ref<NewsDetailItem | null>(null)

const breadcrumbLabel = computed(() => locale.value === 'fa' ? 'جزئیات خبر' : 'News Details')
const loadingText = computed(() => locale.value === 'fa' ? 'در حال بارگذاری خبر...' : 'Loading news...')
const sourceLabel = computed(() => locale.value === 'fa' ? 'منبع:' : 'Source:')
const sourceLinkLabel = computed(() => locale.value === 'fa' ? 'مشاهده فایل مرتبط' : 'View related file')
const viewsLabel = computed(() => locale.value === 'fa' ? 'بازدید' : 'views')

const newsImage = computed(() => {
  return newsItem.value?.image ? getApiUrl(newsItem.value.image) : '/img/news.png'
})

const tagList = computed(() => {
  if (!newsItem.value?.tags) {
    return []
  }
  return newsItem.value.tags.split(',').map((tag) => tag.trim()).filter(Boolean)
})

const renderedContent = computed(() => {
  const content = newsItem.value?.content || ''
  if (!content) {
    return ''
  }

  if (content.includes('<p') || content.includes('<a ') || content.includes('<br')) {
    return content
  }

  return content
    .split('\n')
    .map((paragraph) => paragraph.trim())
    .filter(Boolean)
    .map((paragraph) => `<p>${paragraph}</p>`)
    .join('')
})

const formatDate = (value: string) => {
  const date = new Date(value)
  if (Number.isNaN(date.getTime())) {
    return value
  }

  return new Intl.DateTimeFormat(locale.value === 'fa' ? 'fa-IR' : 'en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  }).format(date)
}

const fetchNewsDetail = async () => {
  const slug = String(route.params.slug || '')
  if (!slug) {
    error.value = locale.value === 'fa' ? 'اسلاگ خبر نامعتبر است.' : 'Invalid news slug.'
    loading.value = false
    return
  }

  loading.value = true
  error.value = null

  try {
    const response = await fetch(getApiUrl(`/api/news/${slug}/`), {
      credentials: 'include',
      cache: 'no-store',
    })

    if (!response.ok) {
      throw new Error(
        locale.value === 'fa'
          ? `خطا در دریافت خبر (${response.status})`
          : `Failed to load news (${response.status})`
      )
    }

    const data = (await response.json()) as NewsDetailResponse
    if (!data.success || !data.news) {
      throw new Error(locale.value === 'fa' ? 'داده خبر نامعتبر است.' : 'Invalid news response.')
    }

    newsItem.value = data.news
  } catch (err: any) {
    error.value = err.message || (locale.value === 'fa' ? 'خطا در دریافت خبر.' : 'Failed to load news.')
  } finally {
    loading.value = false
  }
}

watch(() => route.params.slug, fetchNewsDetail)

onMounted(fetchNewsDetail)
</script>
