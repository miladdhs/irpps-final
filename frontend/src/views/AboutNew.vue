<template>
  <div class="relative flex h-auto min-h-screen w-full flex-col overflow-x-hidden">
    <!-- Hero Section -->
    <div class="relative w-full h-[400px] flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0 bg-cover bg-center z-0 bg-gradient-to-l from-primary/80 to-slate-900/90"></div>
      <div class="relative z-10 text-center px-4 max-w-3xl">
        <h1 class="text-white text-4xl md:text-5xl font-black mb-6">{{ $t('about.title') }}</h1>
        <p class="text-blue-100 text-lg md:text-xl font-light leading-relaxed">
          {{ $t('about.subtitle') }}
        </p>
      </div>
    </div>

    <div class="max-w-[1200px] mx-auto px-6 py-16">
      <!-- Introduction -->
      <section class="mb-20 text-center max-w-4xl mx-auto">
        <h2 class="text-primary text-3xl font-bold mb-8">{{ $t('about.introTitle') }}</h2>
        <p class="text-slate-600 dark:text-slate-400 text-lg leading-loose">
          {{ $t('about.introText') }}
        </p>
      </section>

      <!-- Mission & Vision -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-20">
        <div class="flex flex-col gap-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-8 shadow-sm hover:shadow-md transition-shadow">
          <div class="bg-primary/10 w-14 h-14 rounded-lg flex items-center justify-center text-primary mb-2">
            <span class="material-symbols-outlined text-4xl">target</span>
          </div>
          <h3 class="text-slate-900 dark:text-white text-2xl font-bold">{{ $t('about.missionTitle') }}</h3>
          <p class="text-slate-600 dark:text-slate-400 text-base leading-relaxed">
            {{ $t('about.missionDescription') }}
          </p>
        </div>
        <div class="flex flex-col gap-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-8 shadow-sm hover:shadow-md transition-shadow">
          <div class="bg-primary/10 w-14 h-14 rounded-lg flex items-center justify-center text-primary mb-2">
            <span class="material-symbols-outlined text-4xl">visibility</span>
          </div>
          <h3 class="text-slate-900 dark:text-white text-2xl font-bold">{{ $t('about.visionTitle') }}</h3>
          <p class="text-slate-600 dark:text-slate-400 text-base leading-relaxed">
            {{ $t('about.visionDescription') }}
          </p>
        </div>
      </div>

      <!-- Skills/Expertise Section -->
      <section class="mb-24 bg-slate-50 dark:bg-slate-900/50 p-10 rounded-2xl border border-slate-200 dark:border-slate-800">
        <h3 class="text-slate-900 dark:text-white text-2xl font-bold mb-10 text-center">{{ $t('about.expertiseTitle') }}</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-x-16 gap-y-8">
          <div class="space-y-3">
            <div class="flex justify-between text-sm font-bold">
              <span class="text-slate-700 dark:text-slate-300">{{ $t('about.skill1') }}</span>
              <span class="text-primary">۸۵٪</span>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-2.5 rounded-full overflow-hidden">
              <div class="bg-primary h-full rounded-full" style="width: 85%"></div>
            </div>
          </div>
          <div class="space-y-3">
            <div class="flex justify-between text-sm font-bold">
              <span class="text-slate-700 dark:text-slate-300">{{ $t('about.skill2') }}</span>
              <span class="text-primary">۹۲٪</span>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-2.5 rounded-full overflow-hidden">
              <div class="bg-primary h-full rounded-full" style="width: 92%"></div>
            </div>
          </div>
          <div class="space-y-3">
            <div class="flex justify-between text-sm font-bold">
              <span class="text-slate-700 dark:text-slate-300">{{ $t('about.skill3') }}</span>
              <span class="text-primary">۷۸٪</span>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-2.5 rounded-full overflow-hidden">
              <div class="bg-primary h-full rounded-full" style="width: 78%"></div>
            </div>
          </div>
          <div class="space-y-3">
            <div class="flex justify-between text-sm font-bold">
              <span class="text-slate-700 dark:text-slate-300">{{ $t('about.skill4') }}</span>
              <span class="text-primary">۸۸٪</span>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-2.5 rounded-full overflow-hidden">
              <div class="bg-primary h-full rounded-full" style="width: 88%"></div>
            </div>
          </div>
        </div>
      </section>

      <!-- Objectives List -->
      <section class="mb-24">
        <div class="text-center mb-12">
          <h3 class="text-slate-900 dark:text-white text-3xl font-bold mb-4">{{ $t('about.goalsTitle') }}</h3>
          <div class="w-20 h-1.5 bg-primary mx-auto rounded-full"></div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div v-for="(goal, index) in goals" :key="index" class="flex items-start gap-4 p-4 hover:bg-white dark:hover:bg-slate-900 rounded-lg transition-colors">
            <span class="material-symbols-outlined text-primary mt-1">check_circle</span>
            <p class="text-slate-700 dark:text-slate-300 leading-relaxed">{{ $t(`about.goal${index + 1}`) }}</p>
          </div>
        </div>
      </section>

      <!-- Founders Section -->
      <section class="mb-10">
        <div class="text-center mb-16">
          <h3 class="text-slate-900 dark:text-white text-3xl font-bold mb-4">{{ $t('about.foundersTitle') }}</h3>
          <p class="text-slate-500 dark:text-slate-400">{{ $t('about.foundersSubtitle') }}</p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
          <div v-for="(founder, index) in founders" :key="index" class="group text-center">
            <div class="relative w-48 h-48 mx-auto mb-6 rounded-full overflow-hidden border-4 border-white dark:border-slate-800 shadow-lg group-hover:border-primary transition-all">
              <img :alt="founder.name" class="w-full h-full object-cover" :src="founder.image" />
            </div>
            <h4 class="text-slate-900 dark:text-white text-xl font-bold mb-1">{{ founder.name }}</h4>
            <p class="text-primary font-medium text-sm mb-2">{{ founder.position }}</p>
            <p class="text-slate-500 dark:text-slate-400 text-sm">{{ founder.specialty }}</p>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const goals = ref(Array.from({ length: 10 }, (_, i) => i));

const founders = ref([
  {
    name: 'دکتر احمد رضایی',
    position: 'رئیس هیئت مدیره',
    specialty: 'فوق تخصص ریه کودکان، استاد دانشگاه',
    image: '/img/founder1.jpg'
  },
  {
    name: 'دکتر مریم سعیدی',
    position: 'نایب رئیس',
    specialty: 'متخصص اطفال، پژوهشگر ارشد ریه',
    image: '/img/founder2.jpg'
  },
  {
    name: 'دکتر علی کریمی',
    position: 'دبیر انجمن',
    specialty: 'فوق تخصص بیماری‌های عفونی و تنفسی',
    image: '/img/founder3.jpg'
  },
  {
    name: 'دکتر سارا ناصری',
    position: 'خزانه‌دار',
    specialty: 'متخصص ریه و آلرژی کودکان',
    image: '/img/founder4.jpg'
  }
]);
</script>
