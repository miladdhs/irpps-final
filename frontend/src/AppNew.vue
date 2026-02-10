<template>
  <div class="page-shell bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100 font-display transition-colors duration-200">
    <div class="app-frame">
      <!-- Header -->
      <header class="sticky top-0 z-50 w-full border-b border-solid border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-background-dark/80 backdrop-blur-md px-4 md:px-10 lg:px-20 py-3">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
          <div class="flex items-center gap-6 lg:gap-12">
            <!-- Logo Section -->
            <div class="flex items-center gap-3">
              <div class="p-2 bg-primary/10 rounded-lg">
                <span class="material-symbols-outlined text-primary text-3xl">pulmonology</span>
              </div>
              <h1 class="text-primary text-xl font-black leading-tight tracking-tight hidden md:block">
                {{ $t('home.title') }}
              </h1>
            </div>
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
            <label class="hidden sm:flex flex-col min-w-40 h-10 max-w-64">
              <div class="flex w-full flex-1 items-stretch rounded-lg h-full bg-slate-100 dark:bg-slate-800">
                <div class="text-slate-500 flex items-center justify-center pr-3">
                  <span class="material-symbols-outlined text-xl">search</span>
                </div>
                <input class="form-input flex w-full min-w-0 flex-1 border-none bg-transparent focus:outline-0 focus:ring-0 text-slate-900 dark:text-slate-100 placeholder:text-slate-400 text-sm font-normal pr-2" :placeholder="$t('nav.search')" value=""/>
              </div>
            </label>
            <button class="flex items-center justify-center rounded-lg h-10 w-10 bg-primary/10 text-primary lg:hidden" @click="toggleMobileMenu">
              <span class="material-symbols-outlined">{{ isMobileMenuOpen ? 'close' : 'menu' }}</span>
            </button>
            <button v-if="!isLoggedIn" class="hidden sm:flex items-center justify-center rounded-lg h-10 px-4 bg-primary text-white font-bold text-sm hover:bg-primary/90 transition-all" @click="showLoginModal = true">
              {{ $t('nav.login') }}
            </button>
            <router-link v-else class="hidden sm:flex items-center justify-center rounded-lg h-10 px-4 bg-primary text-white font-bold text-sm hover:bg-primary/90 transition-all" to="/dashboard">
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
              </ul>
            </div>
            <div>
              <h3 class="text-lg font-bold mb-8 relative after:content-[''] after:absolute after:bottom-[-10px] after:right-0 after:w-10 after:h-1 after:bg-primary">{{ $t('footer.quickContact') }}</h3>
              <ul class="space-y-4">
                <li><router-link class="text-slate-400 hover:text-white transition-colors" to="/contact">{{ $t('nav.contact') }}</router-link></li>
                <li><a class="text-slate-400 hover:text-white transition-colors" href="#">{{ $t('footer.faq') }}</a></li>
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

    <!-- Login Modal -->
    <div v-if="showLoginModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50" @click.self="showLoginModal = false">
      <div class="bg-white dark:bg-slate-900 rounded-2xl p-8 max-w-md w-full mx-4 shadow-2xl">
        <div class="flex justify-between items-center mb-6">
          <h3 class="text-2xl font-bold">{{ $t('auth.loginTitle') }}</h3>
          <button @click="showLoginModal = false" class="text-slate-400 hover:text-slate-600">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>
        <div v-if="loginMessage" :class="'mb-4 p-4 rounded-lg ' + (loginSuccess ? 'bg-green-50 text-green-800' : 'bg-red-50 text-red-800')">
          {{ loginMessage }}
        </div>
        <form @submit.prevent="handleLogin" class="space-y-4">
          <div>
            <label class="block text-sm font-medium mb-2">{{ $t('auth.username') }}</label>
            <input type="text" v-model="loginForm.username" class="w-full px-4 py-3 rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 focus:ring-2 focus:ring-primary focus:border-transparent" :placeholder="$t('auth.usernamePlaceholder')" required>
          </div>
          <div>
            <label class="block text-sm font-medium mb-2">{{ $t('auth.password') }}</label>
            <input type="password" v-model="loginForm.password" class="w-full px-4 py-3 rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 focus:ring-2 focus:ring-primary focus:border-transparent" :placeholder="$t('auth.passwordPlaceholder')" required>
          </div>
          <button type="submit" class="w-full bg-primary text-white py-3 rounded-lg font-bold hover:bg-primary/90 transition-all" :disabled="loginLoading">
            {{ loginLoading ? $t('auth.loggingIn') : $t('auth.loginButton') }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { getApiUrl } from '@/utils/api';

const route = useRoute();
const router = useRouter();
const { t } = useI18n();

const isMobileMenuOpen = ref(false);
const showLoginModal = ref(false);
const loginForm = ref({ username: '', password: '' });
const loginLoading = ref(false);
const loginMessage = ref('');
const loginSuccess = ref(false);
const isLoggedIn = ref(false);
const userInfo = ref<any>(null);

const userDisplayName = computed(() => {
  if (!userInfo.value) return t('auth.user');
  return userInfo.value.first_name || userInfo.value.username;
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

const checkAuthStatus = async () => {
  try {
    const response = await fetch(getApiUrl('/api/accounts/profile/'), {
      credentials: 'include'
    });
    const data = await response.json();
    if (data.success) {
      isLoggedIn.value = true;
      userInfo.value = data.user;
    }
  } catch (error) {
    isLoggedIn.value = false;
  }
};

const handleLogin = async () => {
  loginLoading.value = true;
  loginMessage.value = '';
  
  try {
    const response = await fetch(getApiUrl('/api/accounts/login/'), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify(loginForm.value)
    });
    
    const data = await response.json();
    
    if (data.success) {
      loginSuccess.value = true;
      loginMessage.value = data.message || t('auth.loginSuccess');
      await checkAuthStatus();
      setTimeout(() => {
        showLoginModal.value = false;
        router.push('/dashboard');
      }, 1000);
    } else {
      loginSuccess.value = false;
      loginMessage.value = data.errors || t('auth.loginError');
    }
  } catch (error) {
    loginSuccess.value = false;
    loginMessage.value = t('auth.connectionError');
  } finally {
    loginLoading.value = false;
  }
};

onMounted(() => {
  checkAuthStatus();
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
