<template>
  <div class="relative flex h-auto min-h-screen w-full flex-col overflow-x-hidden">
    <div class="relative flex h-[400px] w-full items-center justify-center overflow-hidden">
      <div class="absolute inset-0 z-0 bg-cover bg-center bg-gradient-to-l from-primary/80 to-slate-900/90"></div>
      <div class="relative z-10 max-w-3xl px-4 text-center">
        <h1 class="mb-6 text-4xl font-black text-white md:text-5xl">{{ $t('about.title') }}</h1>
        <p class="text-lg font-light leading-relaxed text-blue-100 md:text-xl">{{ $t('about.subtitle') }}</p>
      </div>
    </div>

    <div class="mx-auto max-w-[1200px] px-6 py-16">
      <section class="mx-auto mb-20 max-w-4xl text-center">
        <h2 class="mb-8 text-3xl font-bold text-primary">{{ $t('about.introTitle') }}</h2>
        <p class="text-lg leading-loose text-slate-600 dark:text-slate-400">{{ $t('about.introText') }}</p>
      </section>

      <div class="mb-20 grid grid-cols-1 gap-8 md:grid-cols-2">
        <div class="flex flex-col gap-4 rounded-xl border border-slate-200 bg-white p-8 shadow-sm transition-shadow hover:shadow-md dark:border-slate-800 dark:bg-slate-900">
          <div class="mb-2 flex h-14 w-14 items-center justify-center rounded-lg bg-primary/10 text-primary">
            <span class="material-symbols-outlined text-4xl">target</span>
          </div>
          <h3 class="text-2xl font-bold text-slate-900 dark:text-white">{{ $t('about.missionTitle') }}</h3>
          <p class="text-base leading-relaxed text-slate-600 dark:text-slate-400">{{ $t('about.missionDescription') }}</p>
        </div>
        <div class="flex flex-col gap-4 rounded-xl border border-slate-200 bg-white p-8 shadow-sm transition-shadow hover:shadow-md dark:border-slate-800 dark:bg-slate-900">
          <div class="mb-2 flex h-14 w-14 items-center justify-center rounded-lg bg-primary/10 text-primary">
            <span class="material-symbols-outlined text-4xl">visibility</span>
          </div>
          <h3 class="text-2xl font-bold text-slate-900 dark:text-white">{{ $t('about.visionTitle') }}</h3>
          <p class="text-base leading-relaxed text-slate-600 dark:text-slate-400">{{ $t('about.visionDescription') }}</p>
        </div>
      </div>

      <section class="mb-24 rounded-2xl border border-slate-200 bg-slate-50 p-10 dark:border-slate-800 dark:bg-slate-900/50">
        <h3 class="mb-10 text-center text-2xl font-bold text-slate-900 dark:text-white">{{ $t('about.expertiseTitle') }}</h3>
        <div class="grid grid-cols-1 gap-x-16 gap-y-8 md:grid-cols-2">
          <div class="space-y-3">
            <div class="flex justify-between text-sm font-bold">
              <span class="text-slate-700 dark:text-slate-300">{{ $t('about.skill1') }}</span>
              <span class="text-primary">{{ percentages[0] }}</span>
            </div>
            <div class="h-2.5 w-full overflow-hidden rounded-full bg-slate-200 dark:bg-slate-700">
              <div class="h-full rounded-full bg-primary" style="width: 85%"></div>
            </div>
          </div>
          <div class="space-y-3">
            <div class="flex justify-between text-sm font-bold">
              <span class="text-slate-700 dark:text-slate-300">{{ $t('about.skill2') }}</span>
              <span class="text-primary">{{ percentages[1] }}</span>
            </div>
            <div class="h-2.5 w-full overflow-hidden rounded-full bg-slate-200 dark:bg-slate-700">
              <div class="h-full rounded-full bg-primary" style="width: 92%"></div>
            </div>
          </div>
          <div class="space-y-3">
            <div class="flex justify-between text-sm font-bold">
              <span class="text-slate-700 dark:text-slate-300">{{ $t('about.skill3') }}</span>
              <span class="text-primary">{{ percentages[2] }}</span>
            </div>
            <div class="h-2.5 w-full overflow-hidden rounded-full bg-slate-200 dark:bg-slate-700">
              <div class="h-full rounded-full bg-primary" style="width: 78%"></div>
            </div>
          </div>
          <div class="space-y-3">
            <div class="flex justify-between text-sm font-bold">
              <span class="text-slate-700 dark:text-slate-300">{{ $t('about.skill4') }}</span>
              <span class="text-primary">{{ percentages[3] }}</span>
            </div>
            <div class="h-2.5 w-full overflow-hidden rounded-full bg-slate-200 dark:bg-slate-700">
              <div class="h-full rounded-full bg-primary" style="width: 88%"></div>
            </div>
          </div>
        </div>
      </section>

      <section class="mb-24">
        <div class="mb-12 text-center">
          <h3 class="mb-4 text-3xl font-bold text-slate-900 dark:text-white">{{ $t('about.goalsTitle') }}</h3>
          <div class="mx-auto h-1.5 w-20 rounded-full bg-primary"></div>
        </div>
        <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
          <div v-for="goal in goals" :key="goal" class="flex items-start gap-4 rounded-lg p-4 transition-colors hover:bg-white dark:hover:bg-slate-900">
            <span class="material-symbols-outlined mt-1 text-primary">check_circle</span>
            <p class="leading-relaxed text-slate-700 dark:text-slate-300">{{ $t(`about.goal${goal + 1}`) }}</p>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()
const goals = ref(Array.from({ length: 10 }, (_, i) => i))
const percentages = computed(() => (locale.value === 'fa' ? ['۸۵٪', '۹۲٪', '۷۸٪', '۸۸٪'] : ['85%', '92%', '78%', '88%']))
</script>
