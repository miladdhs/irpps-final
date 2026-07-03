<template>
  <div class="bg-background-light font-display text-slate-900 transition-colors duration-300 dark:bg-background-dark dark:text-slate-100">
    <div class="relative flex h-auto min-h-screen w-full flex-col overflow-x-hidden">
      <main class="mx-auto flex max-w-7xl flex-1 w-full px-6 py-12 lg:px-20">
        <div class="w-full">
          <section class="mb-16 flex flex-col items-end justify-between gap-6 md:flex-row">
            <div class="flex max-w-2xl flex-col gap-4">
              <nav class="mb-2 flex gap-2 text-xs text-slate-500">
                <router-link to="/" class="hover:text-primary">{{ $t('nav.home') }}</router-link>
                <span>/</span>
                <span class="text-primary">{{ $t('nav.services') }}</span>
              </nav>
              <h1 class="text-4xl font-black leading-tight tracking-tight text-slate-900 dark:text-white">
                {{ $t('services.title') }}
              </h1>
              <p class="text-lg leading-relaxed text-slate-600 dark:text-slate-400">
                {{ $t('services.subtitle') }}
              </p>
            </div>
          </section>

          <section class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
            <div
              v-for="service in services"
              :key="service.id"
              class="group flex flex-col gap-6 rounded-2xl border border-slate-200 bg-white p-8 shadow-sm transition-all duration-300 hover:border-primary/30 hover:shadow-xl dark:border-slate-800 dark:bg-slate-900"
            >
              <div class="flex size-16 items-center justify-center rounded-xl bg-primary/10 text-primary transition-colors group-hover:bg-primary group-hover:text-white">
                <span class="material-symbols-outlined text-4xl">{{ service.icon }}</span>
              </div>
              <div class="flex flex-col gap-3">
                <h2 class="text-xl font-bold text-slate-900 dark:text-white">{{ service.title }}</h2>
                <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                  {{ service.description }}
                </p>
              </div>
              <router-link
                :to="service.link"
                class="mt-auto flex items-center gap-1 text-sm font-bold text-primary transition-transform group-hover:translate-x-[-4px]"
              >
                {{ service.linkText }}
                <span class="material-symbols-outlined text-sm">arrow_back</span>
              </router-link>
            </div>
          </section>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const services = computed(() => [
  {
    id: 1,
    icon: 'medical_information',
    title: t('home.service1Title'),
    description: t('home.service1Desc'),
    link: '/contact',
    linkText: t('home.contactUs'),
  },
  {
    id: 2,
    icon: 'healing',
    title: t('home.service2Title'),
    description: t('home.service2Desc'),
    link: '/publications',
    linkText: t('services.viewDetails'),
  },
  {
    id: 3,
    icon: 'health_and_safety',
    title: t('home.service3Title'),
    description: t('home.service3Desc'),
    link: '/education',
    linkText: t('services.viewDetails'),
  },
  {
    id: 4,
    icon: 'school',
    title: t('home.service4Title'),
    description: t('home.service4Desc'),
    link: '/events',
    linkText: t('nav.eventsItem'),
  },
  {
    id: 5,
    icon: 'biotech',
    title: t('home.service5Title'),
    description: t('home.service5Desc'),
    link: '/publications',
    linkText: t('nav.publications'),
  },
  {
    id: 6,
    icon: 'volunteer_activism',
    title: t('home.service6Title'),
    description: t('home.service6Desc'),
    link: '/contact',
    linkText: t('services.ctaButton1'),
  },
])
</script>
