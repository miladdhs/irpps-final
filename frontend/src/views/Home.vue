<template>
  <div class="relative flex min-h-screen w-full flex-col overflow-x-hidden">
    <section class="relative h-[600px] w-full overflow-hidden px-4 text-center flex items-center justify-center">
      <div class="absolute inset-0 z-0">
        <div class="absolute inset-0 z-10 bg-gradient-to-l from-primary/40 to-slate-900/80"></div>
        <img alt="Hero Image" class="h-full w-full object-cover" src="/img/image3-1024x684.webp" />
      </div>
      <div class="relative z-20 flex max-w-3xl flex-col items-center gap-6">
        <h2 class="text-4xl font-black leading-tight tracking-tight text-white md:text-6xl">{{ $t('home.title') }}</h2>
        <p class="max-w-2xl text-lg font-normal leading-relaxed text-white/90 md:text-xl">{{ $t('home.subtitle') }}</p>
        <div class="mt-4 flex flex-wrap justify-center gap-4">
          <router-link to="/about" class="flex h-14 min-w-[160px] items-center justify-center rounded-xl bg-primary text-lg font-bold text-white shadow-lg shadow-primary/30 transition-transform hover:scale-105">
            {{ $t('home.learnMore') }}
          </router-link>
          <router-link to="/contact" class="flex h-14 min-w-[160px] items-center justify-center rounded-xl border border-white/30 bg-white/20 text-lg font-bold text-white backdrop-blur-md transition-all hover:bg-white/30">
            {{ $t('home.contactUs') }}
          </router-link>
        </div>
      </div>
    </section>

    <section class="relative z-30 mx-auto -mt-16 max-w-7xl px-4">
      <div class="grid grid-cols-2 gap-4 md:grid-cols-4 md:gap-6">
        <div class="flex flex-col items-center rounded-xl border-b-4 border-primary bg-white p-8 text-center shadow-xl dark:bg-slate-900">
          <span class="material-symbols-outlined mb-2 text-4xl text-primary">clinical_notes</span>
          <p class="mb-1 text-3xl font-black text-slate-900 dark:text-white">{{ stats[0] }}</p>
          <p class="font-bold text-slate-500 dark:text-slate-400">{{ $t('home.stat1') }}</p>
        </div>
        <div class="flex flex-col items-center rounded-xl border-b-4 border-primary bg-white p-8 text-center shadow-xl dark:bg-slate-900">
          <span class="material-symbols-outlined mb-2 text-4xl text-primary">groups</span>
          <p class="mb-1 text-3xl font-black text-slate-900 dark:text-white">{{ stats[1] }}</p>
          <p class="font-bold text-slate-500 dark:text-slate-400">{{ $t('home.stat2') }}</p>
        </div>
        <div class="flex flex-col items-center rounded-xl border-b-4 border-primary bg-white p-8 text-center shadow-xl dark:bg-slate-900">
          <span class="material-symbols-outlined mb-2 text-4xl text-primary">article</span>
          <p class="mb-1 text-3xl font-black text-slate-900 dark:text-white">{{ stats[2] }}</p>
          <p class="font-bold text-slate-500 dark:text-slate-400">{{ $t('home.stat3') }}</p>
        </div>
        <div class="flex flex-col items-center rounded-xl border-b-4 border-primary bg-white p-8 text-center shadow-xl dark:bg-slate-900">
          <span class="material-symbols-outlined mb-2 text-4xl text-primary">emoji_events</span>
          <p class="mb-1 text-3xl font-black text-slate-900 dark:text-white">{{ stats[3] }}</p>
          <p class="font-bold text-slate-500 dark:text-slate-400">{{ $t('home.stat4') }}</p>
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-7xl px-4 py-20">
      <div class="mb-16 flex flex-col items-center text-center">
        <span class="mb-3 text-sm font-bold uppercase tracking-widest text-primary">{{ $t('home.servicesTitle') }}</span>
        <h2 class="text-3xl font-black text-slate-900 dark:text-white md:text-4xl">{{ $t('home.servicesSubtitle') }}</h2>
        <div class="mt-4 h-1 w-20 rounded-full bg-primary"></div>
      </div>
      <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
        <div class="group rounded-2xl border border-slate-100 bg-white p-8 transition-all hover:-translate-y-2 hover:shadow-2xl dark:border-slate-800 dark:bg-slate-900">
          <div class="mb-6 flex h-14 w-14 items-center justify-center rounded-xl bg-primary/10 text-primary transition-colors group-hover:bg-primary group-hover:text-white">
            <span class="material-symbols-outlined text-3xl">medical_information</span>
          </div>
          <h3 class="mb-3 text-xl font-bold text-slate-900 dark:text-white">{{ $t('home.service1Title') }}</h3>
          <p class="leading-relaxed text-slate-500 dark:text-slate-400">{{ $t('home.service1Desc') }}</p>
        </div>
        <div class="group rounded-2xl border border-slate-100 bg-white p-8 transition-all hover:-translate-y-2 hover:shadow-2xl dark:border-slate-800 dark:bg-slate-900">
          <div class="mb-6 flex h-14 w-14 items-center justify-center rounded-xl bg-primary/10 text-primary transition-colors group-hover:bg-primary group-hover:text-white">
            <span class="material-symbols-outlined text-3xl">healing</span>
          </div>
          <h3 class="mb-3 text-xl font-bold text-slate-900 dark:text-white">{{ $t('home.service2Title') }}</h3>
          <p class="leading-relaxed text-slate-500 dark:text-slate-400">{{ $t('home.service2Desc') }}</p>
        </div>
        <div class="group rounded-2xl border border-slate-100 bg-white p-8 transition-all hover:-translate-y-2 hover:shadow-2xl dark:border-slate-800 dark:bg-slate-900">
          <div class="mb-6 flex h-14 w-14 items-center justify-center rounded-xl bg-primary/10 text-primary transition-colors group-hover:bg-primary group-hover:text-white">
            <span class="material-symbols-outlined text-3xl">health_and_safety</span>
          </div>
          <h3 class="mb-3 text-xl font-bold text-slate-900 dark:text-white">{{ $t('home.service3Title') }}</h3>
          <p class="leading-relaxed text-slate-500 dark:text-slate-400">{{ $t('home.service3Desc') }}</p>
        </div>
        <div class="group rounded-2xl border border-slate-100 bg-white p-8 transition-all hover:-translate-y-2 hover:shadow-2xl dark:border-slate-800 dark:bg-slate-900">
          <div class="mb-6 flex h-14 w-14 items-center justify-center rounded-xl bg-primary/10 text-primary transition-colors group-hover:bg-primary group-hover:text-white">
            <span class="material-symbols-outlined text-3xl">school</span>
          </div>
          <h3 class="mb-3 text-xl font-bold text-slate-900 dark:text-white">{{ $t('home.service4Title') }}</h3>
          <p class="leading-relaxed text-slate-500 dark:text-slate-400">{{ $t('home.service4Desc') }}</p>
        </div>
        <div class="group rounded-2xl border border-slate-100 bg-white p-8 transition-all hover:-translate-y-2 hover:shadow-2xl dark:border-slate-800 dark:bg-slate-900">
          <div class="mb-6 flex h-14 w-14 items-center justify-center rounded-xl bg-primary/10 text-primary transition-colors group-hover:bg-primary group-hover:text-white">
            <span class="material-symbols-outlined text-3xl">biotech</span>
          </div>
          <h3 class="mb-3 text-xl font-bold text-slate-900 dark:text-white">{{ $t('home.service5Title') }}</h3>
          <p class="leading-relaxed text-slate-500 dark:text-slate-400">{{ $t('home.service5Desc') }}</p>
        </div>
        <div class="group rounded-2xl border border-slate-100 bg-white p-8 transition-all hover:-translate-y-2 hover:shadow-2xl dark:border-slate-800 dark:bg-slate-900">
          <div class="mb-6 flex h-14 w-14 items-center justify-center rounded-xl bg-primary/10 text-primary transition-colors group-hover:bg-primary group-hover:text-white">
            <span class="material-symbols-outlined text-3xl">volunteer_activism</span>
          </div>
          <h3 class="mb-3 text-xl font-bold text-slate-900 dark:text-white">{{ $t('home.service6Title') }}</h3>
          <p class="leading-relaxed text-slate-500 dark:text-slate-400">{{ $t('home.service6Desc') }}</p>
        </div>
      </div>
    </section>

    <section class="bg-slate-100 py-24 dark:bg-slate-800/50">
      <div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-16 px-4 lg:grid-cols-2">
        <div class="relative order-2 lg:order-1">
          <div class="absolute -right-4 -top-4 h-32 w-32 rounded-full bg-primary/10 blur-3xl"></div>
          <div class="absolute -bottom-4 -left-4 h-32 w-32 rounded-full bg-primary/20 blur-3xl"></div>
          <img alt="About Image" class="relative z-10 h-[500px] w-full rounded-3xl object-cover shadow-2xl" src="/img/about-us.jpg" />
          <div class="absolute bottom-6 right-6 z-20 flex items-center gap-4 rounded-2xl border border-slate-100 bg-white p-6 shadow-xl dark:border-slate-700 dark:bg-slate-900">
            <div class="flex h-12 w-12 items-center justify-center rounded-full bg-primary text-white">
              <span class="material-symbols-outlined">verified</span>
            </div>
            <div>
              <p class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">{{ $t('about.verifiedBy') }}</p>
              <p class="text-lg font-black text-slate-900 dark:text-white">{{ $t('about.ministry') }}</p>
            </div>
          </div>
        </div>
        <div class="order-1 lg:order-2">
          <span class="mb-3 block text-sm font-bold uppercase tracking-widest text-primary">{{ $t('about.badge') }}</span>
          <h2 class="mb-8 text-3xl font-black leading-tight text-slate-900 dark:text-white md:text-5xl">
            {{ $t('about.heroTitle') }} <span class="text-primary">{{ $t('about.heroHighlight') }}</span> {{ $t('about.heroEnd') }}
          </h2>
          <p class="mb-8 text-lg leading-relaxed text-slate-600 dark:text-slate-300">{{ $t('about.heroDescription') }}</p>
          <ul class="mb-10 space-y-4">
            <li class="flex items-center gap-3">
              <span class="material-symbols-outlined text-primary">check_circle</span>
              <span class="font-medium text-slate-700 dark:text-slate-200">{{ $t('about.feature1') }}</span>
            </li>
            <li class="flex items-center gap-3">
              <span class="material-symbols-outlined text-primary">check_circle</span>
              <span class="font-medium text-slate-700 dark:text-slate-200">{{ $t('about.feature2') }}</span>
            </li>
            <li class="flex items-center gap-3">
              <span class="material-symbols-outlined text-primary">check_circle</span>
              <span class="font-medium text-slate-700 dark:text-slate-200">{{ $t('about.feature3') }}</span>
            </li>
          </ul>
          <button class="h-14 rounded-xl bg-primary px-10 text-lg font-bold text-white transition-all hover:shadow-xl hover:shadow-primary/40">
            {{ $t('home.learnMore') }}
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()
const stats = computed(() => (locale.value === 'fa' ? ['۵۰+', '۱۰۰۰+', '۲۵', '۱۵'] : ['50+', '1000+', '25', '15']))

onMounted(() => {
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function (e) {
      const href = (this as HTMLElement).getAttribute('href')
      if (href && href !== '#' && href.length > 1) {
        e.preventDefault()
        const target = document.querySelector(href)
        if (target) {
          const offset = 80
          const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset
          window.scrollTo({
            top: targetPosition,
            behavior: 'smooth',
          })
        }
      }
    })
  })
})
</script>
