<template>
  <div class="relative flex min-h-screen w-full flex-col overflow-x-hidden">
    <!-- Hero Section -->
    <section class="relative h-[600px] w-full flex items-center justify-center text-center px-4 overflow-hidden">
      <div class="absolute inset-0 z-0">
        <div class="absolute inset-0 bg-gradient-to-l from-primary/40 to-slate-900/80 z-10"></div>
        <img 
          alt="Hero Image" 
          class="w-full h-full object-cover" 
          src="/img/image3-1024x684.webp"
        />
      </div>
      <div class="relative z-20 max-w-3xl flex flex-col items-center gap-6">
        <h2 class="text-white text-4xl md:text-6xl font-black leading-tight tracking-tight">
          {{ $t('home.title') }}
        </h2>
        <p class="text-white/90 text-lg md:text-xl font-normal max-w-2xl leading-relaxed">
          {{ $t('home.subtitle') }}
        </p>
        <div class="flex flex-wrap gap-4 justify-center mt-4">
          <router-link to="/about" class="min-w-[160px] h-14 rounded-xl bg-primary text-white text-lg font-bold shadow-lg shadow-primary/30 hover:scale-105 transition-transform flex items-center justify-center">
            {{ $t('home.learnMore') }}
          </router-link>
          <router-link to="/contact" class="min-w-[160px] h-14 rounded-xl bg-white/20 backdrop-blur-md border border-white/30 text-white text-lg font-bold hover:bg-white/30 transition-all flex items-center justify-center">
            {{ $t('home.contactUs') }}
          </router-link>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="max-w-7xl mx-auto px-4 -mt-16 relative z-30">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
        <div class="bg-white dark:bg-slate-900 p-8 rounded-xl shadow-xl border-b-4 border-primary flex flex-col items-center text-center">
          <span class="material-symbols-outlined text-primary text-4xl mb-2">clinical_notes</span>
          <p class="text-3xl font-black text-slate-900 dark:text-white mb-1">۵۰+</p>
          <p class="text-slate-500 dark:text-slate-400 font-bold">{{ $t('home.stat1') }}</p>
        </div>
        <div class="bg-white dark:bg-slate-900 p-8 rounded-xl shadow-xl border-b-4 border-primary flex flex-col items-center text-center">
          <span class="material-symbols-outlined text-primary text-4xl mb-2">groups</span>
          <p class="text-3xl font-black text-slate-900 dark:text-white mb-1">۱۰۰۰+</p>
          <p class="text-slate-500 dark:text-slate-400 font-bold">{{ $t('home.stat2') }}</p>
        </div>
        <div class="bg-white dark:bg-slate-900 p-8 rounded-xl shadow-xl border-b-4 border-primary flex flex-col items-center text-center">
          <span class="material-symbols-outlined text-primary text-4xl mb-2">article</span>
          <p class="text-3xl font-black text-slate-900 dark:text-white mb-1">۲۵</p>
          <p class="text-slate-500 dark:text-slate-400 font-bold">{{ $t('home.stat3') }}</p>
        </div>
        <div class="bg-white dark:bg-slate-900 p-8 rounded-xl shadow-xl border-b-4 border-primary flex flex-col items-center text-center">
          <span class="material-symbols-outlined text-primary text-4xl mb-2">emoji_events</span>
          <p class="text-3xl font-black text-slate-900 dark:text-white mb-1">۱۵</p>
          <p class="text-slate-500 dark:text-slate-400 font-bold">{{ $t('home.stat4') }}</p>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section class="max-w-7xl mx-auto px-4 py-20">
      <div class="flex flex-col items-center text-center mb-16">
        <span class="text-primary font-bold tracking-widest uppercase text-sm mb-3">{{ $t('home.servicesTitle') }}</span>
        <h2 class="text-slate-900 dark:text-white text-3xl md:text-4xl font-black">{{ $t('home.servicesSubtitle') }}</h2>
        <div class="h-1 w-20 bg-primary mt-4 rounded-full"></div>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Service 1 -->
        <div class="group bg-white dark:bg-slate-900 p-8 rounded-2xl border border-slate-100 dark:border-slate-800 hover:shadow-2xl hover:-translate-y-2 transition-all">
          <div class="w-14 h-14 bg-primary/10 text-primary rounded-xl flex items-center justify-center mb-6 group-hover:bg-primary group-hover:text-white transition-colors">
            <span class="material-symbols-outlined text-3xl">medical_information</span>
          </div>
          <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3">{{ $t('home.service1Title') }}</h3>
          <p class="text-slate-500 dark:text-slate-400 leading-relaxed">{{ $t('home.service1Desc') }}</p>
        </div>
        <!-- Service 2 -->
        <div class="group bg-white dark:bg-slate-900 p-8 rounded-2xl border border-slate-100 dark:border-slate-800 hover:shadow-2xl hover:-translate-y-2 transition-all">
          <div class="w-14 h-14 bg-primary/10 text-primary rounded-xl flex items-center justify-center mb-6 group-hover:bg-primary group-hover:text-white transition-colors">
            <span class="material-symbols-outlined text-3xl">healing</span>
          </div>
          <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3">{{ $t('home.service2Title') }}</h3>
          <p class="text-slate-500 dark:text-slate-400 leading-relaxed">{{ $t('home.service2Desc') }}</p>
        </div>
        <!-- Service 3 -->
        <div class="group bg-white dark:bg-slate-900 p-8 rounded-2xl border border-slate-100 dark:border-slate-800 hover:shadow-2xl hover:-translate-y-2 transition-all">
          <div class="w-14 h-14 bg-primary/10 text-primary rounded-xl flex items-center justify-center mb-6 group-hover:bg-primary group-hover:text-white transition-colors">
            <span class="material-symbols-outlined text-3xl">health_and_safety</span>
          </div>
          <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3">{{ $t('home.service3Title') }}</h3>
          <p class="text-slate-500 dark:text-slate-400 leading-relaxed">{{ $t('home.service3Desc') }}</p>
        </div>
        <!-- Service 4 -->
        <div class="group bg-white dark:bg-slate-900 p-8 rounded-2xl border border-slate-100 dark:border-slate-800 hover:shadow-2xl hover:-translate-y-2 transition-all">
          <div class="w-14 h-14 bg-primary/10 text-primary rounded-xl flex items-center justify-center mb-6 group-hover:bg-primary group-hover:text-white transition-colors">
            <span class="material-symbols-outlined text-3xl">school</span>
          </div>
          <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3">{{ $t('home.service4Title') }}</h3>
          <p class="text-slate-500 dark:text-slate-400 leading-relaxed">{{ $t('home.service4Desc') }}</p>
        </div>
        <!-- Service 5 -->
        <div class="group bg-white dark:bg-slate-900 p-8 rounded-2xl border border-slate-100 dark:border-slate-800 hover:shadow-2xl hover:-translate-y-2 transition-all">
          <div class="w-14 h-14 bg-primary/10 text-primary rounded-xl flex items-center justify-center mb-6 group-hover:bg-primary group-hover:text-white transition-colors">
            <span class="material-symbols-outlined text-3xl">biotech</span>
          </div>
          <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3">{{ $t('home.service5Title') }}</h3>
          <p class="text-slate-500 dark:text-slate-400 leading-relaxed">{{ $t('home.service5Desc') }}</p>
        </div>
        <!-- Service 6 -->
        <div class="group bg-white dark:bg-slate-900 p-8 rounded-2xl border border-slate-100 dark:border-slate-800 hover:shadow-2xl hover:-translate-y-2 transition-all">
          <div class="w-14 h-14 bg-primary/10 text-primary rounded-xl flex items-center justify-center mb-6 group-hover:bg-primary group-hover:text-white transition-colors">
            <span class="material-symbols-outlined text-3xl">volunteer_activism</span>
          </div>
          <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3">{{ $t('home.service6Title') }}</h3>
          <p class="text-slate-500 dark:text-slate-400 leading-relaxed">{{ $t('home.service6Desc') }}</p>
        </div>
      </div>
    </section>

    <!-- About Summary Section -->
    <section class="bg-slate-100 dark:bg-slate-800/50 py-24">
      <div class="max-w-7xl mx-auto px-4 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
        <div class="order-2 lg:order-1 relative">
          <div class="absolute -top-4 -right-4 w-32 h-32 bg-primary/10 rounded-full blur-3xl"></div>
          <div class="absolute -bottom-4 -left-4 w-32 h-32 bg-primary/20 rounded-full blur-3xl"></div>
          <img 
            alt="About Image" 
            class="rounded-3xl shadow-2xl relative z-10 w-full object-cover h-[500px]" 
            src="/img/about us.webp"
          />
          <div class="absolute bottom-6 right-6 bg-white dark:bg-slate-900 p-6 rounded-2xl shadow-xl z-20 flex items-center gap-4 border border-slate-100 dark:border-slate-700">
            <div class="w-12 h-12 bg-primary rounded-full flex items-center justify-center text-white">
              <span class="material-symbols-outlined">verified</span>
            </div>
            <div>
              <p class="text-xs text-slate-500 dark:text-slate-400 font-bold uppercase tracking-wider">{{ $t('about.verifiedBy') }}</p>
              <p class="text-lg font-black text-slate-900 dark:text-white">{{ $t('about.ministry') }}</p>
            </div>
          </div>
        </div>
        <div class="order-1 lg:order-2">
          <span class="text-primary font-bold tracking-widest uppercase text-sm mb-3 block">{{ $t('about.badge') }}</span>
          <h2 class="text-slate-900 dark:text-white text-3xl md:text-5xl font-black leading-tight mb-8">
            {{ $t('about.heroTitle') }} <span class="text-primary">{{ $t('about.heroHighlight') }}</span> {{ $t('about.heroEnd') }}
          </h2>
          <p class="text-slate-600 dark:text-slate-300 text-lg leading-relaxed mb-8">
            {{ $t('about.heroDescription') }}
          </p>
          <ul class="space-y-4 mb-10">
            <li class="flex items-center gap-3">
              <span class="material-symbols-outlined text-primary">check_circle</span>
              <span class="text-slate-700 dark:text-slate-200 font-medium">{{ $t('about.feature1') }}</span>
            </li>
            <li class="flex items-center gap-3">
              <span class="material-symbols-outlined text-primary">check_circle</span>
              <span class="text-slate-700 dark:text-slate-200 font-medium">{{ $t('about.feature2') }}</span>
            </li>
            <li class="flex items-center gap-3">
              <span class="material-symbols-outlined text-primary">check_circle</span>
              <span class="text-slate-700 dark:text-slate-200 font-medium">{{ $t('about.feature3') }}</span>
            </li>
          </ul>
          <button class="px-10 h-14 bg-primary text-white rounded-xl font-bold text-lg hover:shadow-xl hover:shadow-primary/40 transition-all">
            {{ $t('home.learnMore') }}
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';

onMounted(() => {
  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = (this as HTMLElement).getAttribute('href');
      if (href && href !== '#' && href.length > 1) {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          const offset = 80;
          const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
          window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
          });
        }
      }
    });
  });
});
</script>
