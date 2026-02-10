<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <!-- Header Section -->
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary w-fit">
            <span class="material-symbols-outlined text-[20px]">badge</span>
            هیئت مدیره
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">{{ $t('nav.boardFirst') }}</h1>
          <p class="text-lg text-slate-600 dark:text-slate-400 max-w-2xl">اعضای هیئت مدیره دوره اول انجمن علمی ریه کودکان ایران</p>
        </div>

        <!-- Board Members Grid -->
        <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          <div 
            v-for="member in boardMembers" 
            :key="member.id"
            class="flex flex-col gap-4 rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900"
          >
            <div class="flex items-center gap-4">
              <div class="flex h-16 w-16 shrink-0 items-center justify-center rounded-full bg-primary/10">
                <span class="material-symbols-outlined text-primary text-3xl">person</span>
              </div>
              <div>
                <div class="mb-1 inline-block rounded-full bg-primary/10 px-3 py-1 text-xs font-bold text-primary">
                  {{ member.position }}
                </div>
                <h3 class="text-lg font-bold">{{ member.name }}</h3>
              </div>
            </div>
            <p v-if="member.specialty" class="text-sm text-slate-600 dark:text-slate-400">
              <span class="font-medium">تخصص:</span> {{ member.specialty }}
            </p>
          </div>
        </div>

        <!-- Info Box -->
        <div class="mt-12 rounded-xl border border-primary/20 bg-primary/5 p-6 dark:bg-primary/10">
          <div class="flex items-start gap-4">
            <span class="material-symbols-outlined text-primary text-3xl">info</span>
            <div>
              <h3 class="mb-2 text-lg font-bold">درباره هیئت مدیره دوره اول</h3>
              <p class="leading-relaxed text-slate-600 dark:text-slate-400">
                هیئت مدیره دوره اول انجمن علمی ریه کودکان ایران در سال ۱۳۹۶ تشکیل شد و مسئولیت هدایت و برنامه‌ریزی فعالیت‌های انجمن را بر عهده داشت. این دوره با تلاش و همکاری اعضای محترم، پایه‌های اساسی انجمن را بنا نهاد.
              </p>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const boardMembers = ref([
  { id: 1, name: 'دکتر سهیلا خلیل زاده', position: 'رئیس', specialty: 'متخصص ریه کودکان' },
  { id: 2, name: 'دکتر قمر تاج خانبابائی', position: 'نائب رئیس', specialty: 'متخصص ریه کودکان' },
  { id: 3, name: 'دکتر محمد رضائی', position: 'دبیر', specialty: 'متخصص ریه کودکان' },
  { id: 4, name: 'دکتر مجید کیوانفر', position: 'خزانه‌دار', specialty: 'متخصص ریه کودکان' },
  { id: 5, name: 'دکتر سید احمد طباطبائی', position: 'عضو هیئت مدیره', specialty: 'متخصص ریه کودکان' },
  { id: 6, name: 'دکتر محسن علی سمیر', position: 'عضو هیئت مدیره', specialty: 'متخصص ریه کودکان' },
  { id: 7, name: 'دکتر حسینعلی غفاری پور', position: 'عضو هیئت مدیره', specialty: 'متخصص ریه کودکان' },
  { id: 8, name: 'دکتر محمد رضا مدرسی', position: 'عضو علی‌البدل', specialty: 'متخصص ریه کودکان' },
  { id: 9, name: 'دکتر سید جواد سیدی', position: 'عضو علی‌البدل', specialty: 'متخصص ریه کودکان' },
  { id: 10, name: 'دکتر روح الله شیرزادی', position: 'بازرس اصلی', specialty: 'متخصص ریه کودکان' },
  { id: 11, name: 'دکتر علیرضا اسدی', position: 'بازرس علی‌البدل', specialty: 'متخصص ریه کودکان' }
]);
</script>
