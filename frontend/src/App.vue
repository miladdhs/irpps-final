<template>
  <div class="page-shell bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100 font-display transition-colors duration-200">
    <div class="app-frame">
      <!-- Header -->
      <header class="sticky top-0 z-50 w-full border-b border-solid border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-background-dark/80 backdrop-blur-md px-4 md:px-10 lg:px-20 py-3">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
          <div class="flex items-center gap-6 lg:gap-12">
            <!-- Logo Section -->
            <router-link to="/" class="flex items-center gap-3">
              <img src="/img/logo.png" alt="لوگو انجمن علمی ریه کودکان" class="h-12 w-auto">
              <h1 class="text-primary text-xl font-black leading-tight tracking-tight hidden md:block">
                {{ $t('home.title') }}
              </h1>
            </router-link>
            <!-- Navigation -->
            <nav class="hidden lg:flex items-center gap-8">
              <router-link class="text-sm font-medium leading-normal hover:text-primary transition-colors" :class="{ 'text-primary font-bold': $route.path === '/' }" to="/">{{ $t('nav.home') }}</router-link>
              <div class="relative group">
                <button class="text-sm font-medium leading-normal hover:text-primary transition-colors flex items-center gap-1">
                  {{ $t('nav.about') }}
                  <span class="material-symbols-outlined text-sm">expand_more</span>
                </button>
                <div class="absolute top-full right-0 mt-2 w-56 bg-white dark:bg-slate-900 rounded-lg shadow-xl border border-slate-200 dark:border-slate-800 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all">
                  <router-link class="block px-4 py-3 text-sm hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors" to="/about">{{ $t('nav.aboutForum') }}</router-link>
                  <router-link class="block px-4 py-3 text-sm hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors" to="/about/history">{{ $t('nav.aboutHistory') }}</router-link>
                  <router-link class="block px-4 py-3 text-sm hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors" to="/about/gallery">{{ $t('nav.aboutGallery') }}</router-link>
                  <div class="border-t border-slate-100 dark:border-slate-800"></div>
                  <router-link class="block px-4 py-3 text-sm hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors" to="/about/board-third">{{ $t('nav.boardThird') }}</router-link>
                  <router-link class="block px-4 py-3 text-sm hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors" to="/about/board-second">{{ $t('nav.boardSecond') }}</router-link>
                  <router-link class="block px-4 py-3 text-sm hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors" to="/about/board-first">{{ $t('nav.boardFirst') }}</router-link>
                </div>
              </div>
              <router-link class="text-sm font-medium leading-normal hover:text-primary transition-colors" to="/services">{{ $t('nav.services') }}</router-link>
              <router-link class="text-sm font-medium leading-normal hover:text-primary transition-colors" to="/team">اعضا</router-link>
              <div class="relative group">
                <button class="text-sm font-medium leading-normal hover:text-primary transition-colors flex items-center gap-1">
                  {{ $t('nav.news') }}
                  <span class="material-symbols-outlined text-sm">expand_more</span>
                </button>
                <div class="absolute top-full right-0 mt-2 w-48 bg-white dark:bg-slate-900 rounded-lg shadow-xl border border-slate-200 dark:border-slate-800 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all">
                  <router-link class="block px-4 py-3 text-sm hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors" to="/news">{{ $t('nav.newsItem') }}</router-link>
                  <router-link class="block px-4 py-3 text-sm hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors" to="/events">{{ $t('nav.eventsItem') }}</router-link>
                </div>
              </div>
              <router-link class="text-sm font-medium leading-normal hover:text-primary transition-colors" to="/contact">{{ $t('nav.contact') }}</router-link>
            </nav>
          </div>
          <div class="flex items-center gap-4">
            <button class="flex items-center justify-center rounded-lg h-10 w-10 bg-primary/10 text-primary lg:hidden" @click="toggleMobileMenu">
              <span class="material-symbols-outlined">{{ isMobileMenuOpen ? 'close' : 'menu' }}</span>
            </button>
            <router-link v-if="!isLoggedIn" to="/login" class="flex items-center justify-center rounded-lg h-10 px-4 bg-primary text-white font-bold text-sm hover:bg-primary/90 transition-all">
              {{ $t('nav.login') }}
            </router-link>
            <router-link v-else to="/dashboard" class="flex items-center justify-center rounded-lg h-10 px-4 bg-primary text-white font-bold text-sm hover:bg-primary/90 transition-all">
              <span class="material-symbols-outlined text-sm mr-1">person</span>
              {{ userDisplayName }}
            </router-link>
          </div>
        </div>
        
        <!-- Mobile Menu -->
        <div v-if="isMobileMenuOpen" class="lg:hidden mt-4 pb-4 border-t border-slate-200 dark:border-slate-800 pt-4">
          <nav class="flex flex-col gap-2">
            <router-link class="px-4 py-2 text-sm font-medium rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors" to="/" @click="closeMobileMenu">{{ $t('nav.home') }}</router-link>
            <router-link class="px-4 py-2 text-sm font-medium rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors" to="/about" @click="closeMobileMenu">{{ $t('nav.about') }}</router-link>
            <router-link class="px-4 py-2 text-sm font-medium rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors" to="/services" @click="closeMobileMenu">{{ $t('nav.services') }}</router-link>
            <router-link class="px-4 py-2 text-sm font-medium rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors" to="/team" @click="closeMobileMenu">اعضا</router-link>
            <router-link class="px-4 py-2 text-sm font-medium rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors" to="/news" @click="closeMobileMenu">{{ $t('nav.newsItem') }}</router-link>
            <router-link class="px-4 py-2 text-sm font-medium rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors" to="/events" @click="closeMobileMenu">{{ $t('nav.eventsItem') }}</router-link>
            <router-link class="px-4 py-2 text-sm font-medium rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors" to="/contact" @click="closeMobileMenu">{{ $t('nav.contact') }}</router-link>
          </nav>
        </div>
      </header>

      <main class="app-main flex-1">
        <router-view />
      </main>

      <!-- Footer -->
      <footer class="bg-slate-900 text-white pt-20 pb-10">
        <div class="max-w-7xl mx-auto px-4">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 pb-16 border-b border-slate-800">
            <div class="col-span-1 lg:col-span-1">
              <div class="flex items-center gap-3 mb-6">
                <span class="material-symbols-outlined text-primary text-4xl">pulmonology</span>
                <h2 class="text-xl font-black">{{ $t('footer.brandTitle') }}</h2>
              </div>
              <p class="text-slate-400 leading-relaxed mb-6">
                {{ $t('footer.brandDesc') }}
              </p>
              <div class="flex gap-4">
                <a class="w-10 h-10 rounded-lg bg-slate-800 flex items-center justify-center hover:bg-primary transition-colors" href="https://www.instagram.com/pediatricpulmonarysociety" target="_blank" rel="noopener noreferrer">
                  <span class="material-symbols-outlined">share</span>
                </a>
                <a class="w-10 h-10 rounded-lg bg-slate-800 flex items-center justify-center hover:bg-primary transition-colors" href="#">
                  <span class="material-symbols-outlined">public</span>
                </a>
                <a class="w-10 h-10 rounded-lg bg-slate-800 flex items-center justify-center hover:bg-primary transition-colors" href="#">
                  <span class="material-symbols-outlined">mail</span>
                </a>
              </div>
            </div>
            <div>
              <h3 class="text-lg font-bold mb-8 relative after:content-[''] after:absolute after:bottom-[-10px] after:right-0 after:w-10 after:h-1 after:bg-primary">{{ $t('footer.quickAccess') }}</h3>
              <ul class="space-y-4">
                <li><router-link class="text-slate-400 hover:text-white transition-colors" to="/">{{ $t('nav.home') }}</router-link></li>
                <li><router-link class="text-slate-400 hover:text-white transition-colors" to="/about">{{ $t('nav.about') }}</router-link></li>
                <li><router-link class="text-slate-400 hover:text-white transition-colors" to="/services">{{ $t('nav.services') }}</router-link></li>
                <li><router-link class="text-slate-400 hover:text-white transition-colors" to="/team">{{ $t('nav.team') }}</router-link></li>
                <li><router-link class="text-slate-400 hover:text-white transition-colors" to="/education">{{ $t('nav.education') }}</router-link></li>
                <li><router-link class="text-slate-400 hover:text-white transition-colors" to="/publications">{{ $t('nav.publications') }}</router-link></li>
                <li><router-link class="text-slate-400 hover:text-white transition-colors" to="/associations">انجمن‌های علمی</router-link></li>
              </ul>
            </div>
            <div>
              <h3 class="text-lg font-bold mb-8 relative after:content-[''] after:absolute after:bottom-[-10px] after:right-0 after:w-10 after:h-1 after:bg-primary">{{ $t('footer.quickContact') }}</h3>
              <ul class="space-y-4">
                <li><router-link class="text-slate-400 hover:text-white transition-colors" to="/contact">{{ $t('nav.contact') }}</router-link></li>
              </ul>
            </div>
            <div>
              <h3 class="text-lg font-bold mb-8 relative after:content-[''] after:absolute after:bottom-[-10px] after:right-0 after:w-10 after:h-1 after:bg-primary">{{ $t('footer.socialMedia') }}</h3>
              <ul class="space-y-6">
                <li class="flex items-start gap-3">
                  <span class="material-symbols-outlined text-primary mt-1">location_on</span>
                  <span class="text-slate-400 leading-relaxed">{{ $t('footer.address') }}</span>
                </li>
                <li class="flex items-center gap-3">
                  <span class="material-symbols-outlined text-primary">call</span>
                  <span class="text-slate-400 dir-ltr">{{ $t('footer.phone') }}</span>
                </li>
                <li class="flex items-center gap-3">
                  <span class="material-symbols-outlined text-primary">mail</span>
                  <span class="text-slate-400">{{ $t('footer.email') }}</span>
                </li>
              </ul>
            </div>
          </div>
          <div class="pt-10 flex flex-col md:flex-row justify-between items-center gap-4 text-slate-500 text-sm">
            <p>{{ $t('footer.copyright') }}</p>
            <div class="flex gap-8">
              <a class="hover:text-white transition-colors" href="#">{{ $t('footer.privacy') }}</a>
              <a class="hover:text-white transition-colors" href="#">{{ $t('footer.terms') }}</a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { useAuthStore } from '@/stores/auth';

const route = useRoute();
const router = useRouter();
const { t } = useI18n();
const authStore = useAuthStore();

const isMobileMenuOpen = ref(false);

const isLoggedIn = computed(() => authStore.isAuthenticated);
const userDisplayName = computed(() => {
  if (!authStore.user) return t('auth.user');
  return authStore.user.first_name || authStore.user.username;
});

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};

const closeMobileMenu = () => {
  isMobileMenuOpen.value = false;
};

watch(() => route.path, () => {
  closeMobileMenu();
});

onMounted(async () => {
  // Try to fetch profile on app mount
  if (!authStore.isAuthenticated) {
    await authStore.fetchProfile();
  }
});
</script>

<style scoped>
.app-frame {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-main {
  flex: 1 0 auto;
}
</style>
