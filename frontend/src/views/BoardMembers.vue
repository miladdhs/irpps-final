<template>
  <div class="relative flex h-auto min-h-screen w-full flex-col overflow-x-hidden bg-background-light dark:bg-background-dark">
    <!-- Hero Section -->
    <div class="relative w-full h-[400px] flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0 bg-cover bg-center z-0 bg-gradient-to-l from-primary/80 to-slate-900/90"></div>
      <div class="relative z-10 text-center px-4 max-w-3xl">
        <h1 class="text-white text-4xl md:text-5xl font-black mb-6">اعضای هیئت مدیره</h1>
        <p class="text-blue-100 text-lg md:text-xl font-light leading-relaxed">
          هیئت مدیره انجمن علمی ریه کودکان ایران در دوره‌های مختلف
        </p>
      </div>
    </div>

    <div class="max-w-[1200px] mx-auto px-6 py-16">
      <!-- Navigation Tabs -->
      <div class="flex justify-center mb-12">
        <div class="inline-flex rounded-lg border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-1">
          <button
            v-for="period in periods"
            :key="period.value"
            @click="activePeriod = period.value"
            :class="[
              'px-6 py-3 rounded-md text-sm font-medium transition-all',
              activePeriod === period.value
                ? 'bg-primary text-white shadow-sm'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
            ]"
          >
            {{ period.label }}
          </button>
        </div>
      </div>

      <!-- Board Members Content -->
      <div class="space-y-16">
        <!-- دوره 1403 (فعلی) -->
        <div v-show="activePeriod === '1403'" class="animate-fade-in">
          <div class="text-center mb-12">
            <h2 class="text-3xl font-bold text-slate-900 dark:text-white mb-3">
              هیئت مدیره دوره ۱۴۰۳
            </h2>
            <p class="text-slate-500 dark:text-slate-400">{{ $t('about.afterElection') }}</p>
          </div>
          <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-8">
            <div v-for="(member, index) in board1403" :key="index" class="group text-center">
              <div class="relative w-40 h-40 mx-auto mb-4 rounded-full overflow-hidden border-4 border-white dark:border-slate-800 shadow-lg group-hover:border-primary transition-all">
                <div class="w-full h-full bg-gradient-to-br from-primary/20 to-primary/5 flex items-center justify-center">
                  <span class="material-symbols-outlined text-6xl text-primary/40">person</span>
                </div>
              </div>
              <h3 class="text-slate-900 dark:text-white text-lg font-bold mb-1">{{ member.name }}</h3>
              <p class="text-primary font-medium text-sm mb-1">{{ member.position }}</p>
              <p class="text-slate-500 dark:text-slate-400 text-xs">{{ member.specialty }}</p>
            </div>
          </div>
        </div>

        <!-- دوره 1400 -->
        <div v-show="activePeriod === '1400'" class="animate-fade-in">
          <div class="text-center mb-12">
            <h2 class="text-3xl font-bold text-slate-900 dark:text-white mb-3">
              هیئت مدیره دوره ۱۴۰۰
            </h2>
            <p class="text-slate-500 dark:text-slate-400">{{ $t('about.afterElection') }}</p>
          </div>
          <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-8">
            <div v-for="(member, index) in board1400" :key="index" class="group text-center">
              <div class="relative w-40 h-40 mx-auto mb-4 rounded-full overflow-hidden border-4 border-white dark:border-slate-800 shadow-lg group-hover:border-primary transition-all">
                <div class="w-full h-full bg-gradient-to-br from-primary/20 to-primary/5 flex items-center justify-center">
                  <span class="material-symbols-outlined text-6xl text-primary/40">person</span>
                </div>
              </div>
              <h3 class="text-slate-900 dark:text-white text-lg font-bold mb-1">{{ member.name }}</h3>
              <p class="text-primary font-medium text-sm mb-1">{{ member.position }}</p>
              <p class="text-slate-500 dark:text-slate-400 text-xs">{{ member.specialty }}</p>
            </div>
          </div>
        </div>

        <!-- دوره 1395 (موسسین) -->
        <div v-show="activePeriod === '1395'" class="animate-fade-in">
          <div class="text-center mb-12">
            <h2 class="text-3xl font-bold text-slate-900 dark:text-white mb-3">
              موسسین انجمن - دوره ۱۳۹۵
            </h2>
            <p class="text-slate-500 dark:text-slate-400">تاریخ تأسیس: ۱۶ آذر ۱۳۹۵</p>
          </div>
          <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-8">
            <div v-for="(member, index) in founders1395" :key="index" class="group text-center">
              <div class="relative w-40 h-40 mx-auto mb-4 rounded-full overflow-hidden border-4 border-white dark:border-slate-800 shadow-lg group-hover:border-primary transition-all">
                <div class="w-full h-full bg-gradient-to-br from-primary/20 to-primary/5 flex items-center justify-center">
                  <span class="material-symbols-outlined text-6xl text-primary/40">person</span>
                </div>
              </div>
              <h3 class="text-slate-900 dark:text-white text-lg font-bold mb-1">{{ member.name }}</h3>
              <p class="text-primary font-medium text-sm mb-1">{{ member.position }}</p>
              <p class="text-slate-500 dark:text-slate-400 text-xs">{{ member.specialty }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Info Box -->
      <div class="mt-16 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-900/50 p-8">
        <div class="flex items-start gap-4">
          <span class="material-symbols-outlined text-primary text-3xl">info</span>
          <div>
            <h4 class="text-slate-900 dark:text-white text-lg font-bold mb-2">درباره هیئت مدیره</h4>
            <p class="text-slate-600 dark:text-slate-400 leading-relaxed">
              هیئت مدیره انجمن علمی ریه کودکان ایران از برجسته‌ترین متخصصان و پژوهشگران این حوزه تشکیل شده است. 
              اعضای هیئت مدیره با برگزاری انتخابات الکترونیکی و با رأی اعضای انجمن برای مدت چهار سال انتخاب می‌شوند.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useI18n } from 'vue-i18n';

const { t } = useI18n();

const activePeriod = ref('1403');

const periods = [
  { value: '1403', label: 'دوره ۱۴۰۳ (فعلی)' },
  { value: '1400', label: 'دوره ۱۴۰۰' },
  { value: '1395', label: 'موسسین (۱۳۹۵)' }
];

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

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
