<template>
  <div class="app-frame page-shell">
    <header id="header" class="app-header">
      <nav class="glass-navbar navbar navbar-expand-md pt-3 pb-3" id="navbar_sticky">
        <div class="container-xl">
          <router-link class="navbar-brand d-flex align-items-center gap-2" to="/">
            <span class="navbar-logo-wrapper">
              <img :src="getAssetUrl('img/image.png')" :alt="$t('home.title')" class="navbar-logo">
            </span>
            <span class="brand-title">{{ $t('home.title') }}</span>
          </router-link>
          <button class="navbar-toggler soft-button outline" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <i class="fa fa-bars"></i>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav menu-links mb-0 ms-auto align-items-md-center">
              <li class="nav-item"><router-link class="nav-link" :class="{ active: $route.path === '/' }" to="/">{{ $t('nav.home') }}</router-link></li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="aboutDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  {{ $t('nav.about') }}
                </a>
                <ul class="dropdown-menu" aria-labelledby="aboutDropdown">
                  <li><router-link class="dropdown-item" to="/about">{{ $t('nav.aboutForum') }}</router-link></li>
                  <li><router-link class="dropdown-item" to="/about/history">{{ $t('nav.aboutHistory') }}</router-link></li>
                  <li><router-link class="dropdown-item" to="/about/gallery">{{ $t('nav.aboutGallery') }}</router-link></li>
                </ul>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="newsEventsDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  {{ $t('nav.news') }}
                </a>
                <ul class="dropdown-menu" aria-labelledby="newsEventsDropdown">
                  <li><router-link class="dropdown-item" to="/services?tab=news">{{ $t('nav.newsItem') }}</router-link></li>
                  <li><router-link class="dropdown-item" to="/services?tab=events">{{ $t('nav.eventsItem') }}</router-link></li>
                </ul>
              </li>
              <li class="nav-item"><router-link class="nav-link" :class="{ active: $route.path === '/team' }" to="/team">{{ $t('nav.team') }}</router-link></li>
              <li class="nav-item"><router-link class="nav-link" :class="{ active: $route.path === '/contact' }" to="/contact">{{ $t('nav.contact') }}</router-link></li>
              <li class="nav-item"><a class="nav-link" href="/english">{{ $t('nav.english') }}</a></li>
            </ul>
            <ul class="navbar-nav ms-md-4 flex-row gap-2 align-items-center social-links">
              <li class="nav-item"><a class="nav-link icon-link" href="https://www.instagram.com/pediatricpulmonarysociety" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><i class="fa fa-instagram"></i></a></li>
              <li class="nav-item ms-2">
                <button class="btn-lang" @click="toggleLanguage" :title="currentLocale === 'fa' ? 'Switch to English' : 'تغییر به فارسی'">
                  <span class="lang-icon">{{ currentLocale === 'fa' ? 'EN' : 'FA' }}</span>
                </button>
              </li>
              <li class="nav-item ms-2" v-if="!isLoggedIn">
                <button class="soft-button primary btn-login" @click="showLoginModal = true">
                  <i class="fa fa-sign-in me-1"></i>
                  {{ $t('nav.login') }}
                </button>
              </li>
              <li class="nav-item ms-3" v-else>
                <router-link class="soft-button outline btn-login" to="/dashboard">
                  <i class="fa fa-user me-1"></i>
                  {{ userDisplayName }}
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>

    <main class="app-main">
      <router-view />
    </main>

    <div v-if="showLoginModal" class="modal fade show d-block" tabindex="-1" style="background: rgba(0,0,0,0.5);" @click.self="showLoginModal = false">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content auth-modal glass-card border-0">
          <div class="modal-header border-0 pb-0">
            <button type="button" class="btn-close" @click="showLoginModal = false"></button>
          </div>
          <div class="modal-body pt-0">
            <div class="text-center mb-4">
              <div class="modal-icon">
                <i class="fa fa-heartbeat"></i>
              </div>
              <h5 class="modal-title">{{ $t('auth.loginTitle') }}</h5>
              <p class="text-muted small">{{ $t('auth.loginDesc') }}</p>
            </div>
            <div v-if="loginMessage" :class="'alert alert-' + (loginSuccess ? 'success' : 'danger') + ' alert-dismissible fade show'" role="alert">
              <i :class="(loginSuccess ? 'fa fa-check-circle' : 'fa fa-exclamation-circle') + ' me-2'"></i>{{ loginMessage }}
              <button type="button" class="btn-close" @click="loginMessage = ''"></button>
            </div>
            <form @submit.prevent="handleLogin" class="modern-form">
              <div class="mb-3">
                <label for="loginUsername" class="form-label"><i class="fa fa-user me-2 col_blue"></i>{{ $t('auth.username') }}</label>
                <input type="text" class="form-control modern-input" id="loginUsername" v-model="loginForm.username" :placeholder="$t('auth.usernamePlaceholder')" required>
              </div>
              <div class="mb-3">
                <label for="loginPassword" class="form-label"><i class="fa fa-lock me-2 col_blue"></i>{{ $t('auth.password') }}</label>
                <input type="password" class="form-control modern-input" id="loginPassword" v-model="loginForm.password" :placeholder="$t('auth.passwordPlaceholder')" required>
              </div>
              <div class="d-grid gap-2">
                <button type="submit" class="soft-button primary w-100" :disabled="loginLoading">
                  <i v-if="loginLoading" class="fa fa-spinner fa-spin me-2"></i>
                  <i v-else class="fa fa-sign-in me-2"></i>
                  {{ loginLoading ? $t('auth.loggingIn') : $t('auth.loginButton') }}
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>

    <footer class="app-footer">
      <div class="container-xl">
        <div class="footer-upper glass-card">
          <div class="row g-4 align-items-center">
            <div class="col-lg-4">
              <div class="footer-brand">
                <router-link class="footer-logo d-flex align-items-center gap-2" to="/">
                  <span class="footer-logo-icon">
                    <i class="fa fa-heartbeat"></i>
                  </span>
                  <span>{{ $t('footer.brandTitle') }}</span>
                </router-link>
                <p class="text-muted mt-3 mb-0">{{ $t('footer.brandDesc') }}</p>
              </div>
            </div>
            <div class="col-lg-8">
              <div class="footer-links row">
                <div class="col-sm-6 col-md-3">
                  <h6>{{ $t('footer.quickAccess') }}</h6>
                  <ul class="list-unstyled">
                    <li><router-link to="/">{{ $t('nav.home') }}</router-link></li>
                    <li><router-link to="/about">{{ $t('nav.about') }}</router-link></li>
                    <li><router-link to="/services">{{ $t('nav.news') }}</router-link></li>
                    <li><router-link to="/team">{{ $t('nav.team') }}</router-link></li>
                  </ul>
                </div>
                <div class="col-sm-6 col-md-3">
                  <h6>{{ $t('footer.quickContact') }}</h6>
                  <ul class="list-unstyled">
                    <li><router-link to="/contact">{{ $t('nav.contact') }}</router-link></li>
                    <li><a href="#">{{ $t('footer.faq') }}</a></li>
                  </ul>
                </div>
                <div class="col-sm-6 col-md-3">
                  <h6>{{ $t('footer.additionalLinks') }}</h6>
                  <ul class="list-unstyled">
                    <li><router-link to="/education">{{ $t('nav.education') }}</router-link></li>
                    <li><router-link to="/publications">{{ $t('nav.publications') }}</router-link></li>
                    <li><router-link to="/associations">{{ $t('nav.associations') }}</router-link></li>
                    <li><router-link to="/advertising">{{ $t('nav.advertising') }}</router-link></li>
                  </ul>
                </div>
                <div class="col-sm-6 col-md-3">
                  <h6>{{ $t('footer.socialMedia') }}</h6>
                  <div class="d-flex gap-2 flex-wrap">
                    <a class="footer-social" href="https://www.instagram.com/pediatricpulmonarysociety" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><i class="fa fa-instagram"></i></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="footer-lower text-center text-muted mt-4">
          <p class="mb-1">{{ $t('footer.copyright') }}</p>
          <p class="mb-0">
            <small>{{ $t('footer.developedBy') }} <a href="https://t.me/DHS_Team" class="text-primary text-decoration-none" target="_blank"><i class="fa fa-telegram me-1"></i>DHS DEVELOPMENT TEAM</a></small>
          </p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { getAssetUrl } from '@/utils/assets';
import { getApiUrl } from '@/utils/api';

const route = useRoute();
const router = useRouter();
const { locale } = useI18n();

const currentLocale = computed(() => locale.value);

const toggleLanguage = () => {
  const newLocale = locale.value === 'fa' ? 'en' : 'fa';
  locale.value = newLocale;
  localStorage.setItem('locale', newLocale);
  
  // Change document direction
  document.documentElement.dir = newLocale === 'fa' ? 'rtl' : 'ltr';
  document.documentElement.lang = newLocale;
};

const showLoginModal = ref(false);
const loginForm = ref({
  username: '',
  password: ''
});
const loginLoading = ref(false);
const loginMessage = ref('');
const loginSuccess = ref(false);
const isLoggedIn = ref(false);
const userInfo = ref<any>(null);

const { t } = useI18n();

const userDisplayName = computed(() => {
  if (!userInfo.value) return t('auth.user');
  return userInfo.value.first_name || userInfo.value.username;
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
    } else {
      isLoggedIn.value = false;
      userInfo.value = null;
    }
  } catch (error) {
    isLoggedIn.value = false;
    userInfo.value = null;
  }
};

const handleLogin = async () => {
  loginLoading.value = true;
  loginMessage.value = '';
  
  try {
    const response = await fetch(getApiUrl('/api/accounts/login/'), {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      credentials: 'include',
      body: JSON.stringify(loginForm.value)
    });
    
    const data = await response.json();
    
    if (data.success) {
      loginSuccess.value = true;
      loginMessage.value = data.message || t('auth.loginSuccess');
      
      // Update auth status
      await checkAuthStatus();
      
      setTimeout(() => {
        showLoginModal.value = false;
        loginForm.value = { username: '', password: '' };
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
  // Check authentication status on mount
  checkAuthStatus();
  
  // Set initial direction based on locale
  document.documentElement.dir = locale.value === 'fa' ? 'rtl' : 'ltr';
  document.documentElement.lang = locale.value;
  
  const navbarSticky = document.getElementById('navbar_sticky');
  if (!navbarSticky) return;
  const navbarHeight = document.querySelector('.navbar')?.clientHeight || 0;
  const sticky = navbarSticky.offsetTop;
  
  function onScroll() {
    if (!navbarSticky) return;
    if (window.pageYOffset >= sticky + navbarHeight) {
      navbarSticky.classList.add('sticky');
      document.body.style.paddingTop = navbarHeight + 'px';
    } else {
      navbarSticky.classList.remove('sticky');
      document.body.style.paddingTop = '0';
    }
  }
  
  window.addEventListener('scroll', onScroll);
});
</script>

<style scoped>
.router-link-active,
.router-link-active.nav-link {
  color: var(--brand-primary) !important;
  font-weight: 700;
}

.app-frame {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-y: visible;
}

.app-header {
  position: sticky;
  top: 0;
  z-index: 1020;
  padding: 0.75rem 0;
}

.glass-navbar {
  border-radius: var(--radius-lg);
  background: rgba(255, 255, 255, 0.88);
  border: 1px solid rgba(255, 255, 255, 0.45);
  box-shadow: var(--glass-shadow);
  backdrop-filter: blur(18px);
  transition: var(--transition-snappy);
}

.glass-navbar:hover {
  box-shadow: var(--glass-shadow-hover);
}

.navbar-brand {
  font-weight: 800;
  font-size: 1.1rem;
  color: #14233c !important;
}

.navbar-logo-wrapper {
  width: 42px;
  height: 42px;
  border-radius: 14px;
  background: linear-gradient(135deg, rgba(13,110,253,0.15), rgba(132,94,247,0.15));
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.2);
}

.navbar-logo {
  height: 28px;
  width: auto;
  object-fit: contain;
}

.brand-title {
  letter-spacing: 0.02em;
}

.menu-links .nav-link {
  position: relative;
  padding: 0.65rem 1.1rem;
  border-radius: var(--radius-sm);
  color: rgba(17, 24, 39, 0.75);
  transition: var(--transition-snappy);
}

.menu-links .nav-link::after {
  content: '';
  position: absolute;
  right: 1.1rem;
  bottom: 0.25rem;
  width: 0;
  height: 2px;
  background: linear-gradient(135deg, var(--brand-primary), var(--brand-secondary));
  transition: var(--transition-snappy);
  border-radius: 999px;
}

.menu-links .nav-link:hover {
  color: var(--brand-primary);
  background: rgba(13, 110, 253, 0.08);
}

.menu-links .nav-link:hover::after,
.menu-links .nav-link.router-link-active::after {
  width: calc(100% - 2.2rem);
}

.menu-links .nav-link.router-link-active {
  color: var(--brand-primary);
  background: rgba(13, 110, 253, 0.12);
  font-weight: 700;
}

.social-links .icon-link {
  color: rgba(17, 24, 39, 0.55);
  border-radius: 12px;
  padding: 0.45rem;
  transition: var(--transition-snappy);
}

.social-links .icon-link:hover {
  color: var(--brand-primary);
  background: rgba(13, 110, 253, 0.08);
}

.btn-login {
  min-width: 120px;
}

.btn-lang {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  border: none;
  background: linear-gradient(135deg, rgba(13,110,253,0.12), rgba(132,94,247,0.12));
  color: var(--brand-primary);
  font-weight: 700;
  font-size: 0.85rem;
  transition: var(--transition-snappy);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.btn-lang:hover {
  background: linear-gradient(135deg, rgba(13,110,253,0.25), rgba(132,94,247,0.25));
  transform: translateY(-2px);
}

.lang-icon {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  letter-spacing: 0.5px;
}

.app-main {
  flex: 1;
  display: block;
  padding-bottom: 0;
  overflow-y: auto;
}

.auth-modal {
  border-radius: var(--radius-lg);
  padding: 1.5rem 1.75rem 1.75rem;
}

.modal-icon {
  width: 70px;
  height: 70px;
  border-radius: 20px;
  margin: 0 auto 1rem;
  background: linear-gradient(135deg, rgba(13,110,253,0.18), rgba(132,94,247,0.18));
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--brand-primary);
  font-size: 1.6rem;
}

.app-footer {
  padding-top: 5%;
  padding-bottom: 2%;
}

.footer-upper {
  border-radius: var(--radius-lg);
  padding: 2rem;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.42);
  box-shadow: var(--glass-shadow);
}

.footer-brand .footer-logo {
  font-weight: 700;
  color: #14233c;
  font-size: 1.05rem;
}

.footer-logo-icon {
  width: 44px;
  height: 44px;
  border-radius: 16px;
  background: linear-gradient(135deg, rgba(13,110,253,0.18), rgba(132,94,247,0.18));
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--brand-primary);
}

.footer-links h6 {
  font-weight: 700;
  margin-bottom: 0.7rem;
}

.footer-links a {
  color: rgba(24, 37, 58, 0.7);
  transition: var(--transition-snappy);
}

.footer-links a:hover {
  color: var(--brand-primary);
}

.footer-social {
  width: 40px;
  height: 40px;
  border-radius: 14px;
  background: rgba(13,110,253,0.1);
  color: var(--brand-primary);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition-snappy);
}

.footer-social:hover {
  transform: translateY(-3px);
  background: linear-gradient(135deg, rgba(13,110,253,0.25), rgba(132,94,247,0.25));
  color: #fff;
}

@media (max-width: 991.98px) {
  .menu-links .nav-link {
    padding: 0.6rem 0.9rem;
  }

  .glass-navbar {
    border-radius: 18px;
  }
}

@media (max-width: 575.98px) {
  .app-main {
    padding: 1.5rem 0;
  }

  .footer-upper {
    padding: 2rem;
  }
}
</style>
