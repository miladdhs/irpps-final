<template>
  <div class="relative flex min-h-screen w-full flex-col overflow-x-hidden bg-white text-slate-900">
    <section class="relative overflow-hidden border-b border-slate-200 bg-[linear-gradient(135deg,#eff6ff_0%,#ffffff_42%,#f8fafc_100%)]">
      <div class="mx-auto grid max-w-7xl gap-10 px-4 py-8 lg:grid-cols-[1.1fr,0.9fr] lg:px-8 lg:py-12">
        <div class="flex flex-col justify-center">
          <div class="inline-flex w-fit items-center gap-2 rounded-full border border-primary/15 bg-primary/10 px-4 py-2 text-sm font-bold text-primary">
            <span class="material-symbols-outlined text-base">breaking_news</span>
            Latest updates
          </div>

          <div v-if="newsLoading" class="mt-6 flex h-[320px] items-center justify-center rounded-[32px] border border-slate-200 bg-white/70">
            <div class="h-12 w-12 animate-spin rounded-full border-4 border-primary border-t-transparent"></div>
          </div>

          <div v-else-if="featuredNews.length" class="mt-6">
            <div class="relative overflow-hidden rounded-[32px] border border-slate-200 bg-white shadow-[0_24px_70px_-40px_rgba(15,23,42,0.45)]">
              <div class="absolute inset-0 bg-[radial-gradient(circle_at_top_right,_rgba(14,165,233,0.14),_transparent_40%)]"></div>
              <div class="relative grid min-h-[320px] gap-6 p-6 md:grid-cols-[1.15fr,0.85fr] md:p-8">
                <div class="space-y-5">
                  <div class="flex flex-wrap items-center gap-3">
                    <span class="rounded-full bg-primary/10 px-3 py-1 text-xs font-bold uppercase tracking-[0.25em] text-primary">News</span>
                    <span class="text-xs font-medium text-slate-400">{{ formatDate(activeNews.created_at) }}</span>
                  </div>
                  <h1 class="max-w-2xl text-3xl font-black leading-tight text-slate-900 md:text-5xl">{{ activeNews.title }}</h1>
                  <p class="max-w-2xl text-base leading-8 text-slate-600 md:text-lg">{{ activeNews.short_content || truncateText(stripHtml(activeNews.content), 180) }}</p>
                  <div class="flex flex-wrap items-center gap-3">
                    <router-link :to="`/news/${activeNews.slug}`" class="inline-flex items-center gap-2 rounded-2xl bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-slate-800">
                      Read article
                      <span class="material-symbols-outlined text-base">arrow_forward</span>
                    </router-link>
                    <div class="flex items-center gap-2 rounded-2xl border border-slate-200 px-4 py-3 text-sm text-slate-500">
                      <span class="material-symbols-outlined text-base text-primary">visibility</span>
                      {{ activeNews.views || 0 }} views
                    </div>
                  </div>
                </div>

                <div class="relative overflow-hidden rounded-[28px] bg-slate-100">
                  <img :src="resolveImageUrl(activeNews.image, '/img/news.png')" :alt="activeNews.title" class="h-full min-h-[220px] w-full object-cover">
                </div>
              </div>

              <div class="relative flex items-center justify-between border-t border-slate-200 bg-slate-50/80 px-6 py-4">
                <div class="flex gap-2">
                  <button class="flex h-11 w-11 items-center justify-center rounded-full border border-slate-200 bg-white text-slate-700 transition hover:border-primary hover:text-primary" @click="prevSlide">
                    <span class="material-symbols-outlined">arrow_back</span>
                  </button>
                  <button class="flex h-11 w-11 items-center justify-center rounded-full border border-slate-200 bg-white text-slate-700 transition hover:border-primary hover:text-primary" @click="nextSlide">
                    <span class="material-symbols-outlined">arrow_forward</span>
                  </button>
                </div>

                <div class="hidden items-center gap-3 md:flex">
                  <button
                    v-for="(item, index) in featuredNews"
                    :key="item.id"
                    class="group max-w-[220px] rounded-2xl px-4 py-3 text-left transition"
                    :class="activeSlide === index ? 'bg-white shadow-sm ring-1 ring-slate-200' : 'text-slate-500 hover:bg-white/80'"
                    @click="activeSlide = index"
                  >
                    <div class="text-xs font-bold uppercase tracking-[0.2em]" :class="activeSlide === index ? 'text-primary' : 'text-slate-400'">0{{ index + 1 }}</div>
                    <div class="mt-2 line-clamp-2 text-sm font-semibold text-slate-800">{{ item.title }}</div>
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div v-else class="mt-6 rounded-[32px] border border-slate-200 bg-white p-8 text-slate-500 shadow-sm">
            No published news is available yet.
          </div>
        </div>

        <div class="flex flex-col justify-center gap-6 lg:pl-6">
          <div class="inline-flex items-center gap-2 rounded-full bg-slate-900 px-4 py-2 text-sm font-bold text-white">
            <span class="material-symbols-outlined text-base">air</span>
            IRANIAN PEDIATRIC PULMONOLOGY SOCIETY
          </div>
          <h2 class="text-4xl font-black leading-tight tracking-tight text-slate-900 md:text-6xl">Advancing pediatric respiratory care, education, and research across Iran.</h2>
          <p class="max-w-2xl text-lg leading-8 text-slate-600">A modern professional platform for scientific events, member profiles, academic updates, and collaborative medical knowledge.</p>
          <div class="flex flex-wrap gap-4">
            <router-link to="/about" class="flex h-14 min-w-[170px] items-center justify-center rounded-2xl bg-primary px-6 text-base font-bold text-white shadow-lg shadow-primary/20 transition hover:-translate-y-0.5">About the Society</router-link>
            <router-link to="/events" class="flex h-14 min-w-[170px] items-center justify-center rounded-2xl border border-slate-300 bg-white px-6 text-base font-bold text-slate-900 transition hover:border-primary hover:text-primary">Upcoming Events</router-link>
          </div>
        </div>
      </div>
    </section>

    <section class="mx-auto -mt-8 grid max-w-7xl grid-cols-2 gap-4 px-4 pb-6 md:grid-cols-4 lg:px-8">
      <div class="rounded-[28px] border border-slate-200 bg-white p-6 text-center shadow-sm">
        <span class="material-symbols-outlined mb-3 text-4xl text-primary">groups</span>
        <div class="text-3xl font-black text-slate-900">1000+</div>
        <div class="mt-1 text-sm font-medium text-slate-500">Members and colleagues</div>
      </div>
      <div class="rounded-[28px] border border-slate-200 bg-white p-6 text-center shadow-sm">
        <span class="material-symbols-outlined mb-3 text-4xl text-primary">school</span>
        <div class="text-3xl font-black text-slate-900">25+</div>
        <div class="mt-1 text-sm font-medium text-slate-500">Years of education</div>
      </div>
      <div class="rounded-[28px] border border-slate-200 bg-white p-6 text-center shadow-sm">
        <span class="material-symbols-outlined mb-3 text-4xl text-primary">article</span>
        <div class="text-3xl font-black text-slate-900">50+</div>
        <div class="mt-1 text-sm font-medium text-slate-500">Scientific publications</div>
      </div>
      <div class="rounded-[28px] border border-slate-200 bg-white p-6 text-center shadow-sm">
        <span class="material-symbols-outlined mb-3 text-4xl text-primary">event</span>
        <div class="text-3xl font-black text-slate-900">Year-round</div>
        <div class="mt-1 text-sm font-medium text-slate-500">Events and congresses</div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import { newsAPI } from '@/services/api'
import { resolveImageUrl } from '@/utils/assets'

interface NewsItem {
  id: number
  title: string
  slug: string
  short_content: string
  content: string
  image: string
  views: number
  created_at: string
}

const featuredNews = ref<NewsItem[]>([])
const activeSlide = ref(0)
const newsLoading = ref(true)
let autoSlideTimer: number | null = null

const activeNews = computed(() => featuredNews.value[activeSlide.value] || featuredNews.value[0])

function stripHtml(content: string) {
  return content.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim()
}

function truncateText(content: string, limit: number) {
  if (content.length <= limit) return content
  return `${content.slice(0, limit).trim()}...`
}

function formatDate(value?: string) {
  if (!value) return ''
  return new Intl.DateTimeFormat('en-US', { dateStyle: 'medium' }).format(new Date(value))
}

function nextSlide() {
  if (!featuredNews.value.length) return
  activeSlide.value = (activeSlide.value + 1) % featuredNews.value.length
}

function prevSlide() {
  if (!featuredNews.value.length) return
  activeSlide.value = (activeSlide.value - 1 + featuredNews.value.length) % featuredNews.value.length
}

function startAutoSlide() {
  stopAutoSlide()
  autoSlideTimer = window.setInterval(nextSlide, 7000)
}

function stopAutoSlide() {
  if (autoSlideTimer !== null) {
    window.clearInterval(autoSlideTimer)
    autoSlideTimer = null
  }
}

async function fetchLatestNews() {
  newsLoading.value = true
  try {
    const response = await newsAPI.getNewsList({ page: 1, per_page: 3 })
    featuredNews.value = response.data?.news || []
    activeSlide.value = 0
    if (featuredNews.value.length > 1) startAutoSlide()
  } catch (error) {
    console.error('Failed to load latest news:', error)
    featuredNews.value = []
  } finally {
    newsLoading.value = false
  }
}

onMounted(fetchLatestNews)
onBeforeUnmount(stopAutoSlide)
</script>
