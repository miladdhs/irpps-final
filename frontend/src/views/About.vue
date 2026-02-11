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

      <!-- Board Members Section -->
      <section class="mb-10">
        <div class="text-center mb-16">
          <h3 class="text-slate-900 dark:text-white text-3xl font-bold mb-4">{{ $t('about.foundersTitle') }}</h3>
          <p class="text-slate-500 dark:text-slate-400">{{ $t('about.foundersSubtitle') }}</p>
        </div>

        <div class="space-y-16">
          <!-- هیئت مدیره فعلی - دوره 1403 -->
          <div>
            <h4 class="text-center text-2xl font-bold text-slate-900 dark:text-white mb-8">
              {{ $t('about.boardMembers1403Title') }}
            </h4>
            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6">
              <div v-for="(member, index) in board1403" :key="index" class="group text-center">
                <div class="relative w-32 h-32 mx-auto mb-3 rounded-full overflow-hidden border-4 border-white dark:border-slate-800 shadow-lg group-hover:border-primary transition-all">
                  <div class="w-full h-full bg-gradient-to-br from-primary/20 to-primary/5 flex items-center justify-center">
                    <span class="material-symbols-outlined text-5xl text-primary/40">person</span>
                  </div>
                </div>
                <h5 class="text-slate-900 dark:text-white text-base font-bold mb-1">{{ member.name }}</h5>
                <p class="text-primary font-medium text-sm mb-1">{{ member.position }}</p>
                <p class="text-slate-500 dark:text-slate-400 text-xs">{{ member.specialty }}</p>
              </div>
            </div>
          </div>

          <!-- هیئت مدیره دوره 1400 -->
          <div>
            <h4 class="text-center text-2xl font-bold text-slate-900 dark:text-white mb-8">
              {{ $t('about.boardMembers1400Title') }}
            </h4>
            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6">
              <div v-for="(member, index) in board1400" :key="index" class="group text-center">
                <div class="relative w-32 h-32 mx-auto mb-3 rounded-full overflow-hidden border-4 border-white dark:border-slate-800 shadow-lg group-hover:border-primary transition-all">
                  <div class="w-full h-full bg-gradient-to-br from-primary/20 to-primary/5 flex items-center justify-center">
                    <span class="material-symbols-outlined text-5xl text-primary/40">person</span>
                  </div>
                </div>
                <h5 class="text-slate-900 dark:text-white text-base font-bold mb-1">{{ member.name }}</h5>
                <p class="text-primary font-medium text-sm mb-1">{{ member.position }}</p>
                <p class="text-slate-500 dark:text-slate-400 text-xs">{{ member.specialty }}</p>
              </div>
            </div>
          </div>

          <!-- موسسین انجمن - دوره 1395 -->
          <div>
            <h4 class="text-center text-2xl font-bold text-slate-900 dark:text-white mb-8">
              موسسین انجمن (۱۳۹۵)
            </h4>
            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6">
              <div v-for="(member, index) in founders1395" :key="index" class="group text-center">
                <div class="relative w-32 h-32 mx-auto mb-3 rounded-full overflow-hidden border-4 border-white dark:border-slate-800 shadow-lg group-hover:border-primary transition-all">
                  <div class="w-full h-full bg-gradient-to-br from-primary/20 to-primary/5 flex items-center justify-center">
                    <span class="material-symbols-outlined text-5xl text-primary/40">person</span>
                  </div>
                </div>
                <h5 class="text-slate-900 dark:text-white text-base font-bold mb-1">{{ member.name }}</h5>
                <p class="text-primary font-medium text-sm mb-1">{{ member.position }}</p>
                <p class="text-slate-500 dark:text-slate-400 text-xs">{{ member.specialty }}</p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const goals = ref(Array.from({ length: 10 }, (_, i) => i));

// هیئت مدیره فعلی - دوره 1403
const board1403 = ref([
  {
    name: 'دکتر قمر تاج خانبابائی',
    position: 'رئیس انجمن',
    specialty: 'فوق تخصص آسم و آلرژی کودکان'
  },
  {
    name: 'دکتر سهیلا خلیل زاده',
    position: 'نائب رئیس',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر محمد رضائی',
    position: 'دبیر انجمن',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر نازنین فرحبخش',
    position: 'خزانه دار',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر امیر رضائی',
    position: 'عضو هیئت مدیره',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر ذلفا مدرسی',
    position: 'عضو هیئت مدیره',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر علیرضا عشقی',
    position: 'عضو هیئت مدیره',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر معصومه قاسمپور علمداری',
    position: 'بازرس اصلی',
    specialty: 'فوق تخصص ریه کودکان'
  }
]);

// هیئت مدیره دوره 1400
const board1400 = ref([
  {
    name: 'دکتر مجید کیوانفر',
    position: 'رئیس انجمن',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر محمد رضائی',
    position: 'نائب رئیس',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر امیر رضائی',
    position: 'دبیر انجمن',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر علیرضا عشقی',
    position: 'خزانه دار',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر سید محمد رضا میرکریمی',
    position: 'عضو هیئت مدیره',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر بابک قالیباف',
    position: 'عضو هیئت مدیره',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر سید حسین میر لوحی',
    position: 'عضو هیئت مدیره',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر لعبت شاهکار',
    position: 'بازرس اصلی',
    specialty: 'فوق تخصص ریه کودکان'
  }
]);

// موسسین انجمن - دوره 1395
const founders1395 = ref([
  {
    name: 'دکتر سهیلا خلیل زاده',
    position: 'رئیس انجمن',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر قمر تاج خانبابائی',
    position: 'نائب رئیس',
    specialty: 'فوق تخصص آسم و آلرژی کودکان'
  },
  {
    name: 'دکتر محمد رضائی',
    position: 'دبیر انجمن',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر مجید کیوانفر',
    position: 'خزانه دار',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر سید احمد طباطبائی',
    position: 'عضو هیئت مدیره',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر محسن علی سمیر',
    position: 'عضو هیئت مدیره',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر حسینعلی غفاری پور',
    position: 'عضو هیئت مدیره',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر محمد رضا مدرسی',
    position: 'عضو هیئت مدیره علی البدل',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر سید جواد سیدی',
    position: 'عضو هیئت مدیره علی البدل',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر روح الله شیرزادی',
    position: 'بازرس اصلی',
    specialty: 'فوق تخصص ریه کودکان'
  },
  {
    name: 'دکتر علیرضا اسدی',
    position: 'بازرس علی البدل',
    specialty: 'فوق تخصص ریه کودکان'
  }
]);
</script>
