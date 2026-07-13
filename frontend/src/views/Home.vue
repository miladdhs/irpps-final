<template>
  <div class="bg-background-light text-slate-900">
    <section class="relative w-full overflow-hidden border-b border-slate-200 bg-slate-950">
      <div
        v-for="(item, index) in featuredNews"
        :key="item.id"
        class="absolute inset-0 transition-opacity duration-700"
        :class="activeSlide === index ? 'opacity-100' : 'pointer-events-none opacity-0'"
      >
        <img :src="resolveImageUrl(item.image, '/img/news.png')" :alt="item.title" class="h-full w-full object-cover">
        <div class="absolute inset-0 bg-[linear-gradient(90deg,rgba(2,6,23,0.92)_0%,rgba(2,6,23,0.72)_42%,rgba(2,6,23,0.38)_100%)]"></div>
        <div class="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(14,165,233,0.28),transparent_30%)]"></div>
      </div>

      <div v-if="!featuredNews.length && !newsLoading" class="absolute inset-0 bg-[linear-gradient(135deg,#0f172a,#111827,#1e293b)]"></div>

      <div class="relative mx-auto flex min-h-[72vh] max-w-[1440px] flex-col justify-end px-4 py-10 md:px-8 lg:min-h-[82vh] lg:px-10 lg:py-14">
        <div v-if="newsLoading" class="flex min-h-[420px] items-center justify-center">
          <div class="h-14 w-14 animate-spin rounded-full border-4 border-white/30 border-t-white"></div>
        </div>

        <div v-else-if="activeNews" class="grid items-end gap-8 lg:grid-cols-[minmax(0,1.2fr)_420px]">
          <div class="max-w-4xl">
            <div class="mb-5 inline-flex items-center gap-2 rounded-full border border-white/15 bg-white/10 px-4 py-2 text-xs font-bold uppercase tracking-[0.28em] text-white/90 backdrop-blur-md">
              <span class="material-symbols-outlined text-sm">newsmode</span>
              {{ copy.heroBadge }}
            </div>
            <h1 class="max-w-4xl text-4xl font-black leading-[1.1] tracking-tight text-white md:text-6xl lg:text-7xl">
              {{ activeNews.title }}
            </h1>
            <p class="mt-5 max-w-3xl text-base leading-8 text-white/82 md:text-lg lg:text-xl">
              {{ activeNews.short_content || truncateText(stripHtml(activeNews.content), 230) }}
            </p>

            <div class="mt-7 flex flex-wrap items-center gap-3 text-white/75">
              <div class="inline-flex items-center gap-2 rounded-full border border-white/12 bg-white/8 px-4 py-2 backdrop-blur-sm">
                <span class="material-symbols-outlined text-base">calendar_month</span>
                {{ formatDate(activeNews.created_at) }}
              </div>
              <div class="inline-flex items-center gap-2 rounded-full border border-white/12 bg-white/8 px-4 py-2 backdrop-blur-sm">
                <span class="material-symbols-outlined text-base">visibility</span>
                {{ activeNews.views || 0 }} {{ copy.views }}
              </div>
            </div>

            <div class="mt-8 flex flex-wrap gap-4">
              <router-link :to="`/news/${activeNews.slug}`" class="inline-flex h-14 items-center justify-center rounded-2xl bg-primary px-7 text-base font-bold text-white shadow-[0_18px_40px_-16px_rgba(14,165,233,0.8)] transition hover:-translate-y-0.5 hover:bg-primary/90">
                {{ copy.readNews }}
              </router-link>
              <router-link to="/events" class="inline-flex h-14 items-center justify-center rounded-2xl border border-white/20 bg-white/10 px-7 text-base font-bold text-white backdrop-blur-md transition hover:bg-white/16">
                {{ copy.events }}
              </router-link>
              <router-link to="/team" class="inline-flex h-14 items-center justify-center rounded-2xl border border-white/20 bg-transparent px-7 text-base font-bold text-white transition hover:bg-white/10">
                {{ copy.members }}
              </router-link>
            </div>
          </div>

          <div class="rounded-[32px] border border-white/12 bg-white/10 p-4 shadow-2xl backdrop-blur-xl">
            <div class="mb-3 flex items-center justify-between px-2">
              <div>
                <div class="text-xs font-bold uppercase tracking-[0.26em] text-white/65">{{ copy.latestThree }}</div>
                <div class="mt-1 text-lg font-black text-white">{{ copy.featuredUpdates }}</div>
              </div>
              <div class="flex gap-2">
                <button class="flex h-11 w-11 items-center justify-center rounded-full border border-white/15 bg-white/10 text-white transition hover:bg-white/16" @click="prevSlide">
                  <span class="material-symbols-outlined">{{ isRtl ? 'arrow_forward' : 'arrow_back' }}</span>
                </button>
                <button class="flex h-11 w-11 items-center justify-center rounded-full border border-white/15 bg-white/10 text-white transition hover:bg-white/16" @click="nextSlide">
                  <span class="material-symbols-outlined">{{ isRtl ? 'arrow_back' : 'arrow_forward' }}</span>
                </button>
              </div>
            </div>

            <div class="space-y-3">
              <button
                v-for="(item, index) in featuredNews"
                :key="item.id"
                class="block w-full rounded-[24px] border p-3 text-left transition"
                :class="activeSlide === index ? 'border-white/20 bg-white/14' : 'border-transparent bg-black/10 hover:border-white/10 hover:bg-white/8'"
                @click="activeSlide = index"
              >
                <div class="grid grid-cols-[96px,1fr] gap-3">
                  <img :src="resolveImageUrl(item.image, '/img/news.png')" :alt="item.title" class="h-24 w-full rounded-2xl object-cover">
                  <div class="min-w-0">
                    <div class="text-[11px] font-bold uppercase tracking-[0.24em] text-white/55">0{{ index + 1 }}</div>
                    <div class="mt-2 line-clamp-2 text-sm font-bold leading-6 text-white">{{ item.title }}</div>
                    <div class="mt-2 line-clamp-2 text-xs leading-5 text-white/65">
                      {{ item.short_content || truncateText(stripHtml(item.content), 80) }}
                    </div>
                  </div>
                </div>
              </button>
            </div>
          </div>
        </div>

        <div v-else class="flex min-h-[420px] items-end">
          <div class="max-w-3xl pb-6 text-white">
            <div class="inline-flex items-center gap-2 rounded-full border border-white/15 bg-white/10 px-4 py-2 text-xs font-bold uppercase tracking-[0.28em] backdrop-blur-md">
              IRANIAN PEDIATRIC PULMONOLOGY SOCIETY
            </div>
            <h1 class="mt-5 text-4xl font-black leading-tight md:text-6xl">{{ copy.emptyHeroTitle }}</h1>
            <p class="mt-4 text-lg leading-8 text-white/78">{{ copy.emptyHeroText }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="relative z-10 -mt-10 pb-4">
      <div class="mx-auto max-w-[1440px] px-4 md:px-8 lg:px-10">
        <div class="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
          <router-link to="/events" class="group rounded-[30px] border border-slate-200 bg-white p-6 shadow-[0_30px_60px_-40px_rgba(15,23,42,0.4)] transition hover:-translate-y-1 hover:shadow-[0_35px_70px_-40px_rgba(15,23,42,0.5)]">
            <div class="flex items-center justify-between">
              <span class="material-symbols-outlined text-4xl text-primary">event_upcoming</span>
              <span class="text-xs font-bold uppercase tracking-[0.24em] text-slate-400">{{ copy.quickAccess }}</span>
            </div>
            <h2 class="mt-6 text-2xl font-black text-slate-900">{{ copy.upcomingEvents }}</h2>
            <p class="mt-3 leading-7 text-slate-600">{{ copy.upcomingEventsText }}</p>
          </router-link>

          <router-link to="/news" class="group rounded-[30px] border border-slate-200 bg-white p-6 shadow-[0_30px_60px_-40px_rgba(15,23,42,0.4)] transition hover:-translate-y-1 hover:shadow-[0_35px_70px_-40px_rgba(15,23,42,0.5)]">
            <div class="flex items-center justify-between">
              <span class="material-symbols-outlined text-4xl text-primary">newspaper</span>
              <span class="text-xs font-bold uppercase tracking-[0.24em] text-slate-400">{{ copy.quickAccess }}</span>
            </div>
            <h2 class="mt-6 text-2xl font-black text-slate-900">{{ copy.newsroom }}</h2>
            <p class="mt-3 leading-7 text-slate-600">{{ copy.newsroomText }}</p>
          </router-link>

          <router-link to="/team" class="group rounded-[30px] border border-slate-200 bg-white p-6 shadow-[0_30px_60px_-40px_rgba(15,23,42,0.4)] transition hover:-translate-y-1 hover:shadow-[0_35px_70px_-40px_rgba(15,23,42,0.5)]">
            <div class="flex items-center justify-between">
              <span class="material-symbols-outlined text-4xl text-primary">groups</span>
              <span class="text-xs font-bold uppercase tracking-[0.24em] text-slate-400">{{ copy.quickAccess }}</span>
            </div>
            <h2 class="mt-6 text-2xl font-black text-slate-900">{{ copy.membersDirectory }}</h2>
            <p class="mt-3 leading-7 text-slate-600">{{ copy.membersDirectoryText }}</p>
          </router-link>

          <router-link to="/contact" class="group rounded-[30px] border border-slate-200 bg-[linear-gradient(135deg,#0f172a,#1e293b)] p-6 text-white shadow-[0_30px_60px_-40px_rgba(15,23,42,0.55)] transition hover:-translate-y-1 hover:shadow-[0_35px_70px_-40px_rgba(15,23,42,0.65)]">
            <div class="flex items-center justify-between">
              <span class="material-symbols-outlined text-4xl text-sky-300">support_agent</span>
              <span class="text-xs font-bold uppercase tracking-[0.24em] text-white/50">{{ copy.quickAccess }}</span>
            </div>
            <h2 class="mt-6 text-2xl font-black">{{ copy.contactUs }}</h2>
            <p class="mt-3 leading-7 text-white/72">{{ copy.contactUsText }}</p>
          </router-link>
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-[1440px] px-4 py-14 md:px-8 lg:px-10">
      <div class="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <div class="rounded-[28px] border border-slate-200 bg-white p-6 shadow-sm">
          <span class="material-symbols-outlined text-4xl text-primary">clinical_notes</span>
          <div class="mt-5 text-4xl font-black text-slate-900">{{ stats[0] }}</div>
          <div class="mt-2 text-sm font-medium text-slate-500">{{ $t('home.stat1') }}</div>
        </div>
        <div class="rounded-[28px] border border-slate-200 bg-white p-6 shadow-sm">
          <span class="material-symbols-outlined text-4xl text-primary">groups</span>
          <div class="mt-5 text-4xl font-black text-slate-900">{{ stats[1] }}</div>
          <div class="mt-2 text-sm font-medium text-slate-500">{{ $t('home.stat2') }}</div>
        </div>
        <div class="rounded-[28px] border border-slate-200 bg-white p-6 shadow-sm">
          <span class="material-symbols-outlined text-4xl text-primary">article</span>
          <div class="mt-5 text-4xl font-black text-slate-900">{{ stats[2] }}</div>
          <div class="mt-2 text-sm font-medium text-slate-500">{{ $t('home.stat3') }}</div>
        </div>
        <div class="rounded-[28px] border border-slate-200 bg-white p-6 shadow-sm">
          <span class="material-symbols-outlined text-4xl text-primary">workspace_premium</span>
          <div class="mt-5 text-4xl font-black text-slate-900">{{ stats[3] }}</div>
          <div class="mt-2 text-sm font-medium text-slate-500">{{ $t('home.stat4') }}</div>
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-[1440px] px-4 py-8 md:px-8 lg:px-10">
      <div class="mb-10 flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
        <div>
          <div class="text-sm font-bold uppercase tracking-[0.3em] text-primary">{{ $t('home.servicesTitle') }}</div>
          <h2 class="mt-3 text-3xl font-black text-slate-900 md:text-5xl">{{ $t('home.servicesSubtitle') }}</h2>
        </div>
        <router-link to="/services" class="inline-flex h-12 items-center justify-center rounded-2xl border border-slate-300 bg-white px-5 text-sm font-bold text-slate-900 transition hover:border-primary hover:text-primary">
          {{ copy.allServices }}
        </router-link>
      </div>

      <div class="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
        <article v-for="service in services" :key="service.title" class="group rounded-[30px] border border-slate-200 bg-white p-7 shadow-sm transition hover:-translate-y-1 hover:shadow-xl">
          <div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-primary/10 text-primary transition group-hover:bg-primary group-hover:text-white">
            <span class="material-symbols-outlined text-3xl">{{ service.icon }}</span>
          </div>
          <h3 class="mt-6 text-2xl font-black text-slate-900">{{ service.title }}</h3>
          <p class="mt-3 leading-8 text-slate-600">{{ service.description }}</p>
        </article>
      </div>
    </section>

    <section class="mx-auto max-w-[1440px] px-4 py-14 md:px-8 lg:px-10">
      <div class="grid items-center gap-10 overflow-hidden rounded-[36px] border border-slate-200 bg-[linear-gradient(135deg,#f8fafc_0%,#ffffff_45%,#eef6ff_100%)] p-8 shadow-sm lg:grid-cols-[1fr,0.95fr] lg:p-10">
        <div>
          <div class="text-sm font-bold uppercase tracking-[0.3em] text-primary">{{ $t('about.badge') }}</div>
          <h2 class="mt-4 text-3xl font-black leading-tight text-slate-900 md:text-5xl">
            {{ $t('about.heroTitle') }}
            <span class="text-primary">{{ $t('about.heroHighlight') }}</span>
            {{ $t('about.heroEnd') }}
          </h2>
          <p class="mt-5 text-lg leading-8 text-slate-600">{{ $t('about.heroDescription') }}</p>
          <ul class="mt-8 space-y-4">
            <li class="flex items-start gap-3">
              <span class="material-symbols-outlined mt-1 text-primary">check_circle</span>
              <span class="leading-7 text-slate-700">{{ $t('about.feature1') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="material-symbols-outlined mt-1 text-primary">check_circle</span>
              <span class="leading-7 text-slate-700">{{ $t('about.feature2') }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="material-symbols-outlined mt-1 text-primary">check_circle</span>
              <span class="leading-7 text-slate-700">{{ $t('about.feature3') }}</span>
            </li>
          </ul>
          <div class="mt-8 flex flex-wrap gap-4">
            <router-link to="/about" class="inline-flex h-14 items-center justify-center rounded-2xl bg-slate-900 px-6 text-base font-bold text-white transition hover:bg-slate-800">
              {{ $t('home.learnMore') }}
            </router-link>
            <router-link to="/contact" class="inline-flex h-14 items-center justify-center rounded-2xl border border-slate-300 bg-white px-6 text-base font-bold text-slate-900 transition hover:border-primary hover:text-primary">
              {{ $t('home.contactUs') }}
            </router-link>
          </div>
        </div>

        <div class="relative min-h-[420px] overflow-hidden rounded-[32px] bg-[linear-gradient(135deg,#0f172a,#1e3a8a,#0f766e)] p-8 text-white">
          <div class="absolute -right-16 -top-16 h-52 w-52 rounded-full bg-white/10 blur-3xl"></div>
          <div class="absolute -bottom-16 -left-8 h-52 w-52 rounded-full bg-sky-300/20 blur-3xl"></div>
          <div class="relative z-10 flex h-full flex-col justify-between">
            <div>
              <div class="inline-flex items-center gap-2 rounded-full border border-white/12 bg-white/10 px-4 py-2 text-xs font-bold uppercase tracking-[0.24em]">
                IRANIAN PEDIATRIC PULMONOLOGY SOCIETY
              </div>
              <h3 class="mt-6 text-3xl font-black leading-tight">{{ copy.visionTitle }}</h3>
              <p class="mt-4 leading-8 text-white/80">{{ copy.visionText }}</p>
            </div>
            <div class="grid gap-3 sm:grid-cols-2">
              <div class="rounded-2xl border border-white/10 bg-white/10 p-4 backdrop-blur-md">
                <div class="text-xs font-bold uppercase tracking-[0.2em] text-white/55">{{ copy.focus1Title }}</div>
                <div class="mt-2 text-sm leading-7 text-white/84">{{ copy.focus1Text }}</div>
              </div>
              <div class="rounded-2xl border border-white/10 bg-white/10 p-4 backdrop-blur-md">
                <div class="text-xs font-bold uppercase tracking-[0.2em] text-white/55">{{ copy.focus2Title }}</div>
                <div class="mt-2 text-sm leading-7 text-white/84">{{ copy.focus2Text }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'
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

const { locale, t } = useI18n()
const featuredNews = ref<NewsItem[]>([])
const activeSlide = ref(0)
const newsLoading = ref(true)
let autoSlideTimer: number | null = null

const isRtl = computed(() => locale.value === 'fa')

const copy = computed(() => (
  locale.value === 'fa'
    ? {
        heroBadge: 'سه خبر آخر انجمن',
        views: 'بازدید',
        readNews: 'مشاهده خبر',
        events: 'رویدادها',
        members: 'اعضا',
        latestThree: 'آخرین خبرها',
        featuredUpdates: 'اسلایدر اخبار',
        emptyHeroTitle: 'خانه انجمن با خبرها، رویدادها و دسترسی‌های اصلی آماده است.',
        emptyHeroText: 'به‌محض انتشار خبرهای جدید، اسلایدر بالای صفحه به‌صورت خودکار با سه خبر آخر به‌روزرسانی می‌شود.',
        quickAccess: 'دسترسی سریع',
        upcomingEvents: 'رویدادهای پیش رو',
        upcomingEventsText: 'همایش‌ها، کنگره‌ها و کارگاه‌های جدید را با زمان ثبت‌نام و برگزاری ببینید.',
        newsroom: 'اخبار و اطلاعیه‌ها',
        newsroomText: 'به تازه‌ترین خبرها، اطلاعیه‌ها و گزارش‌های انجمن سریع دسترسی داشته باشید.',
        membersDirectory: 'دایرکتوری اعضا',
        membersDirectoryText: 'رزومه و اطلاعات اعضای انجمن را در یک ساختار حرفه‌ای مرور کنید.',
        contactUs: 'تماس با انجمن',
        contactUsText: 'برای هماهنگی، عضویت، همکاری علمی و پشتیبانی مستقیم با انجمن در ارتباط باشید.',
        allServices: 'مشاهده همه خدمات',
        visionTitle: 'مرکز علمی، آموزشی و حرفه‌ای برای جامعه ریه کودکان',
        visionText: 'این صفحه اصلی به‌صورت کامل طراحی شده تا خبر، دسترسی مهم، معرفی انجمن، خدمات، اعضا و مسیرهای کلیدی را در یک تجربه حرفه‌ای و مدرن کنار هم قرار دهد.',
        focus1Title: 'تمرکز آموزشی',
        focus1Text: 'برگزاری دوره‌ها، کارگاه‌ها و برنامه‌های بازآموزی برای پزشکان و اعضا.',
        focus2Title: 'تمرکز علمی',
        focus2Text: 'پوشش اخبار، انتشارات، فعالیت‌های پژوهشی و شبکه تخصصی اعضای انجمن.',
      }
    : {
        heroBadge: 'Latest Society News',
        views: 'views',
        readNews: 'Read News',
        events: 'Events',
        members: 'Members',
        latestThree: 'Latest News',
        featuredUpdates: 'Featured Updates',
        emptyHeroTitle: 'The homepage is ready with news, events, and all major access points.',
        emptyHeroText: 'As soon as new items are published, the top slider updates automatically with the latest three news posts.',
        quickAccess: 'Quick Access',
        upcomingEvents: 'Upcoming Events',
        upcomingEventsText: 'Review new congresses, seminars, and workshops together with registration and event dates.',
        newsroom: 'Newsroom',
        newsroomText: 'Reach the latest news, announcements, and official society reports immediately.',
        membersDirectory: 'Members Directory',
        membersDirectoryText: 'Browse structured member profiles and resumes in a professional public directory.',
        contactUs: 'Contact the Society',
        contactUsText: 'Reach the society for membership, scientific collaboration, support, and coordination.',
        allServices: 'View All Services',
        visionTitle: 'A scientific, educational, and professional center for pediatric pulmonology',
        visionText: 'This homepage is intentionally designed to unify latest news, major actions, society introduction, services, members, and key navigation in one modern experience.',
        focus1Title: 'Education Focus',
        focus1Text: 'Courses, workshops, retraining programs, and practical learning paths for physicians and members.',
        focus2Title: 'Scientific Focus',
        focus2Text: 'News, publications, research activities, and the specialist member network in one place.',
      }
))

const activeNews = computed(() => featuredNews.value[activeSlide.value] || featuredNews.value[0] || null)
const stats = computed(() => (locale.value === 'fa' ? ['۵۰+', '۱۰۰۰+', '۲۵', '۱۵'] : ['50+', '1000+', '25', '15']))

const services = computed(() => [
  { icon: 'medical_information', title: t('home.service1Title'), description: t('home.service1Desc') },
  { icon: 'healing', title: t('home.service2Title'), description: t('home.service2Desc') },
  { icon: 'health_and_safety', title: t('home.service3Title'), description: t('home.service3Desc') },
  { icon: 'school', title: t('home.service4Title'), description: t('home.service4Desc') },
  { icon: 'biotech', title: t('home.service5Title'), description: t('home.service5Desc') },
  { icon: 'volunteer_activism', title: t('home.service6Title'), description: t('home.service6Desc') },
])

function stripHtml(content: string) {
  return content.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim()
}

function truncateText(content: string, limit: number) {
  if (content.length <= limit) return content
  return `${content.slice(0, limit).trim()}...`
}

function formatDate(value?: string) {
  if (!value) return ''
  return new Intl.DateTimeFormat(locale.value === 'fa' ? 'fa-IR' : 'en-US', {
    dateStyle: 'medium',
  }).format(new Date(value))
}

function nextSlide() {
  if (!featuredNews.value.length) return
  activeSlide.value = (activeSlide.value + 1) % featuredNews.value.length
}

function prevSlide() {
  if (!featuredNews.value.length) return
  activeSlide.value = (activeSlide.value - 1 + featuredNews.value.length) % featuredNews.value.length
}

function stopAutoSlide() {
  if (autoSlideTimer !== null) {
    window.clearInterval(autoSlideTimer)
    autoSlideTimer = null
  }
}

function startAutoSlide() {
  stopAutoSlide()
  if (featuredNews.value.length > 1) {
    autoSlideTimer = window.setInterval(nextSlide, 6500)
  }
}

async function fetchLatestNews() {
  newsLoading.value = true
  try {
    const response = await newsAPI.getNewsList({ page: 1, per_page: 3 })
    featuredNews.value = response.data?.news || []
    activeSlide.value = 0
    startAutoSlide()
  } catch (error) {
    console.error('Failed to load latest news:', error)
    featuredNews.value = []
    stopAutoSlide()
  } finally {
    newsLoading.value = false
  }
}

watch(() => featuredNews.value.length, startAutoSlide)

onMounted(fetchLatestNews)
onBeforeUnmount(stopAutoSlide)
</script>
