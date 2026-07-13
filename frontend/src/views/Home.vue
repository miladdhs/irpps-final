<template>
  <div class="bg-background-light text-slate-900">
    <section class="relative w-full overflow-hidden border-b border-slate-200 bg-slate-950">
      <div
        v-for="(item, index) in featuredSlides"
        :key="item.key"
        class="absolute inset-0 transition-opacity duration-700"
        :class="activeSlide === index ? 'opacity-100' : 'pointer-events-none opacity-0'"
      >
        <img :src="item.image" :alt="item.title" class="h-full w-full object-cover">
        <div class="absolute inset-0 bg-[linear-gradient(90deg,rgba(2,6,23,0.94)_0%,rgba(2,6,23,0.78)_45%,rgba(2,6,23,0.46)_100%)]"></div>
        <div class="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(14,165,233,0.26),transparent_32%)]"></div>
      </div>

      <div v-if="!featuredSlides.length && !slidesLoading" class="absolute inset-0 bg-[linear-gradient(135deg,#0f172a,#111827,#1e293b)]"></div>

      <div class="relative mx-auto flex min-h-[76vh] max-w-[1440px] flex-col justify-end px-4 py-10 md:px-8 lg:min-h-[84vh] lg:px-10 lg:py-14">
        <div v-if="slidesLoading" class="flex min-h-[420px] items-center justify-center">
          <div class="h-14 w-14 animate-spin rounded-full border-4 border-white/30 border-t-white"></div>
        </div>

        <div v-else-if="activeItem" class="max-w-4xl">
          <div class="mb-5 inline-flex items-center gap-2 rounded-full border border-white/15 bg-white/10 px-4 py-2 text-xs font-bold tracking-[0.18em] text-white/90 backdrop-blur-md">
            <span class="material-symbols-outlined text-sm">{{ activeItem.icon }}</span>
            {{ activeItem.badge }}
          </div>
          <h1 class="max-w-4xl text-4xl font-black leading-[1.1] tracking-tight text-white md:text-6xl lg:text-7xl">
            {{ activeItem.title }}
          </h1>
          <p class="mt-5 max-w-3xl text-base leading-8 text-white/82 md:text-lg lg:text-xl">
            {{ activeItem.summary }}
          </p>

          <div class="mt-7 flex flex-wrap items-center gap-3 text-white/75">
            <div class="inline-flex items-center gap-2 rounded-full border border-white/12 bg-white/8 px-4 py-2 backdrop-blur-sm">
              <span class="material-symbols-outlined text-base">calendar_month</span>
              {{ activeItem.dateLabel }}
            </div>
            <div v-if="activeItem.secondaryMeta" class="inline-flex items-center gap-2 rounded-full border border-white/12 bg-white/8 px-4 py-2 backdrop-blur-sm">
              <span class="material-symbols-outlined text-base">{{ activeItem.secondaryIcon }}</span>
              {{ activeItem.secondaryMeta }}
            </div>
          </div>

          <div class="mt-8 flex flex-wrap items-center gap-4">
            <router-link :to="activeItem.href" class="inline-flex h-14 items-center justify-center rounded-2xl bg-primary px-7 text-base font-bold text-white shadow-[0_18px_40px_-16px_rgba(14,165,233,0.8)] transition hover:-translate-y-0.5 hover:bg-primary/90">
              {{ activeItem.cta }}
            </router-link>

            <div class="flex items-center gap-3">
              <button class="flex h-14 w-14 items-center justify-center rounded-2xl border border-white/20 bg-white/10 text-white backdrop-blur-md transition hover:bg-white/16" @click="prevSlide" :aria-label="copy.previous">
                <span class="material-symbols-outlined text-3xl leading-none">{{ isRtl ? 'chevron_right' : 'chevron_left' }}</span>
              </button>
              <button class="flex h-14 w-14 items-center justify-center rounded-2xl border border-white/20 bg-white/10 text-white backdrop-blur-md transition hover:bg-white/16" @click="nextSlide" :aria-label="copy.next">
                <span class="material-symbols-outlined text-3xl leading-none">{{ isRtl ? 'chevron_left' : 'chevron_right' }}</span>
              </button>
            </div>
          </div>
        </div>

        <div v-else class="flex min-h-[420px] items-end">
          <div class="max-w-3xl pb-6 text-white">
            <div class="inline-flex items-center gap-2 rounded-full border border-white/15 bg-white/10 px-4 py-2 text-xs font-bold tracking-[0.18em] backdrop-blur-md">
              {{ copy.societyName }}
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
              <span class="text-xs font-bold tracking-[0.2em] text-slate-400">{{ copy.quickAccess }}</span>
            </div>
            <h2 class="mt-6 text-2xl font-black text-slate-900">{{ copy.upcomingEvents }}</h2>
            <p class="mt-3 leading-7 text-slate-600">{{ copy.upcomingEventsText }}</p>
          </router-link>

          <router-link to="/news" class="group rounded-[30px] border border-slate-200 bg-white p-6 shadow-[0_30px_60px_-40px_rgba(15,23,42,0.4)] transition hover:-translate-y-1 hover:shadow-[0_35px_70px_-40px_rgba(15,23,42,0.5)]">
            <div class="flex items-center justify-between">
              <span class="material-symbols-outlined text-4xl text-primary">newspaper</span>
              <span class="text-xs font-bold tracking-[0.2em] text-slate-400">{{ copy.quickAccess }}</span>
            </div>
            <h2 class="mt-6 text-2xl font-black text-slate-900">{{ copy.newsroom }}</h2>
            <p class="mt-3 leading-7 text-slate-600">{{ copy.newsroomText }}</p>
          </router-link>

          <router-link to="/team" class="group rounded-[30px] border border-slate-200 bg-white p-6 shadow-[0_30px_60px_-40px_rgba(15,23,42,0.4)] transition hover:-translate-y-1 hover:shadow-[0_35px_70px_-40px_rgba(15,23,42,0.5)]">
            <div class="flex items-center justify-between">
              <span class="material-symbols-outlined text-4xl text-primary">groups</span>
              <span class="text-xs font-bold tracking-[0.2em] text-slate-400">{{ copy.quickAccess }}</span>
            </div>
            <h2 class="mt-6 text-2xl font-black text-slate-900">{{ copy.membersDirectory }}</h2>
            <p class="mt-3 leading-7 text-slate-600">{{ copy.membersDirectoryText }}</p>
          </router-link>

          <router-link to="/contact" class="group rounded-[30px] border border-slate-200 bg-[linear-gradient(135deg,#0f172a,#1e293b)] p-6 text-white shadow-[0_30px_60px_-40px_rgba(15,23,42,0.55)] transition hover:-translate-y-1 hover:shadow-[0_35px_70px_-40px_rgba(15,23,42,0.65)]">
            <div class="flex items-center justify-between">
              <span class="material-symbols-outlined text-4xl text-sky-300">support_agent</span>
              <span class="text-xs font-bold tracking-[0.2em] text-white/50">{{ copy.quickAccess }}</span>
            </div>
            <h2 class="mt-6 text-2xl font-black">{{ copy.contactUs }}</h2>
            <p class="mt-3 leading-7 text-white/72">{{ copy.contactUsText }}</p>
          </router-link>
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-[1440px] px-4 py-8 md:px-8 lg:px-10">
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
          <div class="text-sm font-bold tracking-[0.22em] text-primary">{{ $t('home.servicesTitle') }}</div>
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
          <div class="text-sm font-bold tracking-[0.22em] text-primary">{{ $t('about.badge') }}</div>
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
              <div class="inline-flex items-center gap-2 rounded-full border border-white/12 bg-white/10 px-4 py-2 text-xs font-bold tracking-[0.18em]">
                {{ copy.societyName }}
              </div>
              <h3 class="mt-6 text-3xl font-black leading-tight">{{ copy.visionTitle }}</h3>
              <p class="mt-4 leading-8 text-white/80">{{ copy.visionText }}</p>
            </div>
            <div class="grid gap-3 sm:grid-cols-2">
              <div class="rounded-2xl border border-white/10 bg-white/10 p-4 backdrop-blur-md">
                <div class="text-xs font-bold text-white/55">{{ copy.focus1Title }}</div>
                <div class="mt-2 text-sm leading-7 text-white/84">{{ copy.focus1Text }}</div>
              </div>
              <div class="rounded-2xl border border-white/10 bg-white/10 p-4 backdrop-blur-md">
                <div class="text-xs font-bold text-white/55">{{ copy.focus2Title }}</div>
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
import { eventsAPI, newsAPI } from '@/services/api'
import { DEFAULT_EVENT_IMAGE, DEFAULT_NEWS_IMAGE, resolveImageUrl } from '@/utils/assets'

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

interface EventItem {
  id: number
  title: string
  slug: string
  description: string
  short_description?: string
  image: string | null
  location: string
  event_date: string | null
  registration_date: string | null
  registration_deadline?: string | null
}

interface SlideItem {
  key: string
  title: string
  summary: string
  image: string
  href: string
  badge: string
  icon: string
  cta: string
  dateLabel: string
  secondaryMeta?: string
  secondaryIcon?: string
  sortDate: number
}

const { locale, t } = useI18n()
const featuredSlides = ref<SlideItem[]>([])
const activeSlide = ref(0)
const slidesLoading = ref(true)
let autoSlideTimer: number | null = null

const isRtl = computed(() => locale.value === 'fa')

const copy = computed(() => (
  locale.value === 'fa'
    ? {
        newsBadge: 'خبر',
        eventBadge: 'رویداد',
        newsCta: 'مشاهده خبر',
        eventCta: 'مشاهده رویداد',
        previous: 'اسلاید قبلی',
        next: 'اسلاید بعدی',
        eventDate: 'تاریخ برگزاری',
        registrationDate: 'تاریخ ثبت‌نام',
        societyName: 'انجمن علمی ریه کودکان ایران',
        emptyHeroTitle: 'صفحه اصلی انجمن آماده نمایش خبرها، رویدادها و مسیرهای اصلی است.',
        emptyHeroText: 'با انتشار اخبار و رویدادهای جدید، اسلایدر صفحه اصلی به‌صورت خودکار به‌روزرسانی می‌شود.',
        quickAccess: 'دسترسی سریع',
        upcomingEvents: 'رویدادهای پیش رو',
        upcomingEventsText: 'همایش‌ها، کنگره‌ها و کارگاه‌های جدید را همراه با تاریخ ثبت‌نام و برگزاری ببینید.',
        newsroom: 'اخبار و اطلاعیه‌ها',
        newsroomText: 'به تازه‌ترین خبرها، اطلاعیه‌ها و گزارش‌های رسمی انجمن سریع دسترسی داشته باشید.',
        membersDirectory: 'فهرست اعضا',
        membersDirectoryText: 'رزومه و اطلاعات اعضای انجمن را در یک ساختار حرفه‌ای و مرتب مرور کنید.',
        contactUs: 'تماس با انجمن',
        contactUsText: 'برای هماهنگی، عضویت، همکاری علمی و پشتیبانی مستقیم با انجمن در ارتباط باشید.',
        allServices: 'مشاهده همه خدمات',
        visionTitle: 'مرکز علمی، آموزشی و حرفه‌ای برای جامعه ریه کودکان',
        visionText: 'این صفحه اصلی طوری طراحی شده که خبر، دسترسی‌های مهم، معرفی انجمن، خدمات، اعضا و مسیرهای کلیدی را در یک تجربه روشن و حرفه‌ای کنار هم قرار دهد.',
        focus1Title: 'تمرکز آموزشی',
        focus1Text: 'برگزاری دوره‌ها، کارگاه‌ها و برنامه‌های بازآموزی برای پزشکان و اعضا.',
        focus2Title: 'تمرکز علمی',
        focus2Text: 'پوشش خبرها، انتشارات، فعالیت‌های پژوهشی و شبکه تخصصی اعضای انجمن.',
      }
    : {
        newsBadge: 'News',
        eventBadge: 'Event',
        newsCta: 'Read News',
        eventCta: 'View Event',
        previous: 'Previous slide',
        next: 'Next slide',
        eventDate: 'Event Date',
        registrationDate: 'Registration Date',
        societyName: 'Iranian Pediatric Pulmonology Society',
        emptyHeroTitle: 'The homepage is ready to present news, events, and primary site pathways.',
        emptyHeroText: 'As new news and events are published, the homepage slider updates automatically.',
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
        visionText: 'This homepage is designed to unify latest news, major actions, society introduction, services, members, and key navigation in one clear modern experience.',
        focus1Title: 'Education Focus',
        focus1Text: 'Courses, workshops, retraining programs, and practical learning paths for physicians and members.',
        focus2Title: 'Scientific Focus',
        focus2Text: 'News, publications, research activities, and the specialist member network in one place.',
      }
))

const activeItem = computed(() => featuredSlides.value[activeSlide.value] || featuredSlides.value[0] || null)
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

function formatDate(value?: string | null) {
  if (!value) return ''
  return new Intl.DateTimeFormat(locale.value === 'fa' ? 'fa-IR' : 'en-US', {
    dateStyle: 'medium',
  }).format(new Date(value))
}

function nextSlide() {
  if (!featuredSlides.value.length) return
  activeSlide.value = (activeSlide.value + 1) % featuredSlides.value.length
}

function prevSlide() {
  if (!featuredSlides.value.length) return
  activeSlide.value = (activeSlide.value - 1 + featuredSlides.value.length) % featuredSlides.value.length
}

function stopAutoSlide() {
  if (autoSlideTimer !== null) {
    window.clearInterval(autoSlideTimer)
    autoSlideTimer = null
  }
}

function startAutoSlide() {
  stopAutoSlide()
  if (featuredSlides.value.length > 1) {
    autoSlideTimer = window.setInterval(nextSlide, 6500)
  }
}

function mapNewsToSlide(item: NewsItem): SlideItem {
  return {
    key: `news-${item.id}`,
    title: item.title,
    summary: item.short_content || truncateText(stripHtml(item.content), 230),
    image: resolveImageUrl(item.image, DEFAULT_NEWS_IMAGE),
    href: `/news/${item.slug}`,
    badge: copy.value.newsBadge,
    icon: 'newsmode',
    cta: copy.value.newsCta,
    dateLabel: formatDate(item.created_at),
    secondaryMeta: item.views ? `${item.views}` : undefined,
    secondaryIcon: 'visibility',
    sortDate: new Date(item.created_at).getTime(),
  }
}

function mapEventToSlide(item: EventItem): SlideItem {
  const registrationDate = item.registration_date || item.registration_deadline || ''
  const eventDate = item.event_date || registrationDate
  return {
    key: `event-${item.id}`,
    title: item.title,
    summary: item.short_description || truncateText(stripHtml(item.description || ''), 230),
    image: resolveImageUrl(item.image, DEFAULT_EVENT_IMAGE),
    href: `/events/${item.slug}`,
    badge: copy.value.eventBadge,
    icon: 'event',
    cta: copy.value.eventCta,
    dateLabel: `${copy.value.eventDate}: ${formatDate(eventDate)}`,
    secondaryMeta: registrationDate ? `${copy.value.registrationDate}: ${formatDate(registrationDate)}` : undefined,
    secondaryIcon: 'edit_calendar',
    sortDate: new Date(eventDate || Date.now()).getTime(),
  }
}

async function fetchSlides() {
  slidesLoading.value = true
  try {
    const [newsResponse, eventsResponse] = await Promise.all([
      newsAPI.getNewsList({ page: 1, per_page: 3 }),
      eventsAPI.getEventsList({ page: 1, per_page: 3 }),
    ])

    const newsSlides = Array.isArray(newsResponse.data?.news) ? newsResponse.data.news.map(mapNewsToSlide) : []
    const eventSlides = Array.isArray(eventsResponse.data?.events) ? eventsResponse.data.events.map(mapEventToSlide) : []

    featuredSlides.value = [...newsSlides, ...eventSlides].sort((a, b) => b.sortDate - a.sortDate)
    activeSlide.value = 0
    startAutoSlide()
  } catch (error) {
    console.error('Failed to load homepage slides:', error)
    featuredSlides.value = []
    stopAutoSlide()
  } finally {
    slidesLoading.value = false
  }
}

watch(() => featuredSlides.value.length, startAutoSlide)

onMounted(fetchSlides)
onBeforeUnmount(stopAutoSlide)
</script>
