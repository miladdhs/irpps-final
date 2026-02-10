<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100 font-display transition-colors duration-300">
    <div class="relative flex h-auto min-h-screen w-full flex-col overflow-x-hidden">
      <main class="flex-1 max-w-7xl mx-auto w-full px-6 py-12 lg:px-20">
        <!-- Hero Section -->
        <section class="flex flex-col md:flex-row justify-between items-end gap-6 mb-16">
          <div class="flex flex-col gap-4 max-w-2xl">
            <nav class="flex gap-2 text-xs text-slate-500 mb-2">
              <router-link to="/" class="hover:text-primary">{{ $t('nav.home') }}</router-link>
              <span>/</span>
              <span class="text-primary">{{ $t('nav.services') }}</span>
            </nav>
            <h1 class="text-slate-900 dark:text-white text-4xl font-black leading-tight tracking-tight">
              {{ $t('services.title') }}
            </h1>
            <p class="text-slate-600 dark:text-slate-400 text-lg leading-relaxed">
              {{ $t('services.subtitle') }}
            </p>
          </div>
          <button class="flex items-center gap-2 min-w-[160px] cursor-pointer justify-center rounded-xl h-12 px-6 bg-primary/10 text-primary hover:bg-primary/20 transition-all font-bold">
            <span class="material-symbols-outlined">add_task</span>
            <span>{{ $t('services.requestButton') }}</span>
          </button>
        </section>

        <!-- Services Grid -->
        <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Service Card -->
          <div 
            v-for="service in services" 
            :key="service.id"
            class="group flex flex-col gap-6 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-8 shadow-sm hover:shadow-xl hover:border-primary/30 transition-all duration-300"
          >
            <div class="size-16 rounded-xl bg-primary/10 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
              <span class="material-symbols-outlined text-4xl">{{ service.icon }}</span>
            </div>
            <div class="flex flex-col gap-3">
              <h2 class="text-slate-900 dark:text-white text-xl font-bold">{{ service.title }}</h2>
              <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">
                {{ service.description }}
              </p>
            </div>
            <router-link 
              :to="service.link" 
              class="mt-auto flex items-center gap-1 text-primary text-sm font-bold group-hover:translate-x-[-4px] transition-transform"
            >
              {{ service.linkText }}
              <span class="material-symbols-outlined text-sm">arrow_back</span>
            </router-link>
          </div>
        </section>

        <!-- CTA Section -->
        <section class="mt-20 bg-primary/5 dark:bg-primary/10 rounded-3xl p-8 lg:p-16 relative overflow-hidden">
          <div class="relative z-10 flex flex-col items-center text-center max-w-3xl mx-auto gap-8">
            <h2 class="text-slate-900 dark:text-white text-3xl font-black">{{ $t('services.ctaTitle') }}</h2>
            <p class="text-slate-700 dark:text-slate-300 text-lg">
              {{ $t('services.ctaDescription') }}
            </p>
            <div class="flex flex-wrap justify-center gap-4">
              <button class="bg-primary text-white h-14 px-10 rounded-xl font-bold text-lg shadow-xl shadow-primary/30 hover:scale-105 transition-transform">
                {{ $t('services.ctaButton1') }}
              </button>
              <button class="bg-white dark:bg-slate-800 text-slate-900 dark:text-white border border-slate-200 dark:border-slate-700 h-14 px-10 rounded-xl font-bold text-lg hover:bg-slate-50 dark:hover:bg-slate-700 transition-colors">
                {{ $t('services.ctaButton2') }}
              </button>
            </div>
          </div>
          <!-- Decorative Background Elements -->
          <div class="absolute -right-20 -bottom-20 size-64 bg-primary/10 rounded-full blur-3xl"></div>
          <div class="absolute -left-20 -top-20 size-64 bg-primary/10 rounded-full blur-3xl"></div>
        </section>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useI18n } from 'vue-i18n';

const { t } = useI18n();

const services = ref([
  {
    id: 1,
    icon: 'medical_information',
    title: 'مشاوره تخصصی',
    description: 'ارائه مشاوره‌های علمی و تخصصی در زمینه بیماری‌های ریوی نوزادان و کودکان',
    link: '/contact',
    linkText: 'درخواست مشاوره'
  },
  {
    id: 2,
    icon: 'healing',
    title: 'درمان‌های نوین',
    description: 'معرفی و بکارگیری جدیدترین پروتکل‌های درمانی بین‌المللی برای بیماران تنفسی',
    link: '/services',
    linkText: 'اطلاعات بیشتر'
  },
  {
    id: 3,
    icon: 'health_and_safety',
    title: 'پیشگیری و سلامت',
    description: 'برنامه‌های غربالگری و آگاهی‌رسانی جهت جلوگیری از بروز بیماری‌های مزمن ریوی',
    link: '/education',
    linkText: 'برنامه‌های پیشگیری'
  },
  {
    id: 4,
    icon: 'school',
    title: 'آموزش مداوم',
    description: 'برگزاری کارگاه‌ها و کنفرانس‌های علمی برای پزشکان و متخصصان سراسر کشور',
    link: '/events',
    linkText: 'رویدادهای آموزشی'
  },
  {
    id: 5,
    icon: 'biotech',
    title: 'پژوهش علمی',
    description: 'حمایت از پایان‌نامه‌ها و طرح‌های تحقیقاتی در حوزه تنفس و آسم کودکان',
    link: '/publications',
    linkText: 'پروژه‌های تحقیقاتی'
  },
  {
    id: 6,
    icon: 'volunteer_activism',
    title: 'حمایت از بیماران',
    description: 'ارائه خدمات حمایتی و مددکاری برای خانواده‌های دارای کودک با بیماری خاص',
    link: '/contact',
    linkText: 'درخواست حمایت'
  }
]);
</script>
