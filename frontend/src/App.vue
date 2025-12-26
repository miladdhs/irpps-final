<template>
  <div class="page-shell">
    <div class="app-frame">
    <header id="header" class="app-header">
      <nav class="glass-navbar navbar navbar-expand-md pt-3 pb-3" id="navbar_sticky">
        <div class="container-xl">
          <router-link class="navbar-brand d-flex align-items-center gap-2" to="/">
            <span class="navbar-logo-wrapper">
              <img :src="getAssetUrl('img/image.png')" :alt="$t('home.title')" class="navbar-logo">
            </span>
            <span class="brand-title">{{ $t('home.title') }}</span>
          </router-link>
          <button class="navbar-toggler soft-button outline" type="button" @click="toggleMobileMenu" :aria-expanded="isMobileMenuOpen" aria-label="Toggle navigation">
            <i class="fa" :class="isMobileMenuOpen ? 'fa-times' : 'fa-bars'"></i>
          </button>
          <div class="navbar-collapse mobile-menu" :class="{ 'mobile-menu-open': isMobileMenuOpen || windowWidth >= 768 }" id="navbarSupportedContent">
            <ul class="navbar-nav menu-links mb-0 ms-auto align-items-md-center">
              <li class="nav-item"><router-link class="nav-link" :class="{ active: $route.path === '/' }" to="/" @click="closeMobileMenu">{{ $t('nav.home') }}</router-link></li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="aboutDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  {{ $t('nav.about') }}
                </a>
                <ul class="dropdown-menu" aria-labelledby="aboutDropdown">
                  <li><router-link class="dropdown-item" to="/about" @click="closeMobileMenu">{{ $t('nav.aboutForum') }}</router-link></li>
                  <li><router-link class="dropdown-item" to="/about/history" @click="closeMobileMenu">{{ $t('nav.aboutHistory') }}</router-link></li>
                  <li><router-link class="dropdown-item" to="/about/gallery" @click="closeMobileMenu">{{ $t('nav.aboutGallery') }}</router-link></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><router-link class="dropdown-item" to="/about/board-third" @click="closeMobileMenu">{{ $t('nav.boardThird') }}</router-link></li>
                  <li><router-link class="dropdown-item" to="/about/board-second" @click="closeMobileMenu">{{ $t('nav.boardSecond') }}</router-link></li>
                  <li><router-link class="dropdown-item" to="/about/board-first" @click="closeMobileMenu">{{ $t('nav.boardFirst') }}</router-link></li>
                </ul>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="newsEventsDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  {{ $t('nav.news') }}
                </a>
                <ul class="dropdown-menu" aria-labelledby="newsEventsDropdown">
                  <li><router-link class="dropdown-item" to="/news" @click="closeMobileMenu">{{ $t('nav.newsItem') }}</router-link></li>
                  <li><router-link class="dropdown-item" to="/events" @click="closeMobileMenu">{{ $t('nav.eventsItem') }}</router-link></li>
                </ul>
              </li>
              <li class="nav-item"><router-link class="nav-link" :class="{ active: $route.path === '/team' }" to="/team" @click="closeMobileMenu">{{ $t('nav.team') }}</router-link></li>
              <li class="nav-item"><router-link class="nav-link" :class="{ active: $route.path === '/contact' }" to="/contact" @click="closeMobileMenu">{{ $t('nav.contact') }}</router-link></li>
            </ul>
            <ul class="navbar-nav ms-md-4 flex-row gap-2 align-items-center social-links">
              <li class="nav-item"><a class="nav-link icon-link" href="https://www.instagram.com/pediatricpulmonarysociety" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><i class="fa fa-instagram"></i></a></li>
              <li class="nav-item ms-2">
                <button class="btn-lang" @click="toggleLanguage" :title="currentLocale === 'fa' ? '' : 'تغییر به فارسی'">
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
                <router-link class="soft-button outline btn-login" to="/dashboard" @click="closeMobileMenu">
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
            <ul class="nav nav-tabs border-0 w-100" role="tablist">
              <li class="nav-item" role="presentation">
                <button class="nav-link" :class="{ active: !showRegisterTab }" @click="showRegisterTab = false" type="button">
                  {{ $t('auth.loginTitle') }}
                </button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" :class="{ active: showRegisterTab }" @click="showRegisterTab = true" type="button">
                  درخواست عضویت
                </button>
              </li>
            </ul>
            <button type="button" class="btn-close" @click="showLoginModal = false"></button>
          </div>
          <div class="modal-body pt-0">
            <!-- Login Tab -->
            <div v-if="!showRegisterTab">
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
            
            <!-- Register Tab -->
            <div v-else>
              <div class="text-center mb-4">
                <div class="modal-icon">
                  <i class="fa fa-user-plus"></i>
                </div>
                <h5 class="modal-title">درخواست عضویت</h5>
                <p class="text-muted small">ثبت درخواست عضویت در انجمن علمی ریه کودکان</p>
              </div>
              <div v-if="registerMessage" :class="'alert alert-' + (registerSuccess ? 'success' : 'danger') + ' alert-dismissible fade show'" role="alert">
                <i :class="(registerSuccess ? 'fa fa-check-circle' : 'fa fa-exclamation-circle') + ' me-2'"></i>{{ registerMessage }}
                <button type="button" class="btn-close" @click="registerMessage = ''"></button>
              </div>
              <form @submit.prevent="handleRegister" class="modern-form">
                <div class="row">
                  <div class="col-md-6 mb-3">
                    <label for="registerFirstName" class="form-label"><i class="fa fa-user me-2 col_blue"></i>نام</label>
                    <input type="text" class="form-control modern-input" id="registerFirstName" v-model="registerForm.first_name" placeholder="نام" required>
                  </div>
                  <div class="col-md-6 mb-3">
                    <label for="registerLastName" class="form-label"><i class="fa fa-user me-2 col_blue"></i>نام خانوادگی</label>
                    <input type="text" class="form-control modern-input" id="registerLastName" v-model="registerForm.last_name" placeholder="نام خانوادگی" required>
                  </div>
                </div>
                <div class="mb-3">
                  <label for="registerUsername" class="form-label"><i class="fa fa-at me-2 col_blue"></i>نام کاربری</label>
                  <input type="text" class="form-control modern-input" id="registerUsername" v-model="registerForm.username" placeholder="نام کاربری" required>
                </div>
                <div class="mb-3">
                  <label for="registerEmail" class="form-label"><i class="fa fa-envelope me-2 col_blue"></i>ایمیل (اختیاری)</label>
                  <input type="email" class="form-control modern-input" id="registerEmail" v-model="registerForm.email" placeholder="ایمیل">
                </div>
                <div class="mb-3">
                  <label for="registerPhone" class="form-label"><i class="fa fa-phone me-2 col_blue"></i>شماره تلفن (اختیاری)</label>
                  <input type="text" class="form-control modern-input" id="registerPhone" v-model="registerForm.phone" placeholder="شماره تلفن">
                </div>
                <div class="row">
                  <div class="col-md-6 mb-3">
                    <label for="registerPassword" class="form-label"><i class="fa fa-lock me-2 col_blue"></i>رمز عبور</label>
                    <input type="password" class="form-control modern-input" id="registerPassword" v-model="registerForm.password" placeholder="رمز عبور" required>
                  </div>
                  <div class="col-md-6 mb-3">
                    <label for="registerPasswordConfirm" class="form-label"><i class="fa fa-lock me-2 col_blue"></i>تکرار رمز عبور</label>
                    <input type="password" class="form-control modern-input" id="registerPasswordConfirm" v-model="registerForm.password_confirm" placeholder="تکرار رمز عبور" required>
                  </div>
                </div>
                <div class="d-grid gap-2">
                  <button type="submit" class="soft-button primary w-100" :disabled="registerLoading">
                    <i v-if="registerLoading" class="fa fa-spinner fa-spin me-2"></i>
                    <i v-else class="fa fa-user-plus me-2"></i>
                    {{ registerLoading ? 'در حال ثبت...' : 'ثبت درخواست' }}
                  </button>
                </div>
              </form>
            </div>
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
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch, nextTick } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { getAssetUrl } from '@/utils/assets';
import { getApiUrl } from '@/utils/api';

const route = useRoute();
const router = useRouter();
const { locale } = useI18n();

const isMobileMenuOpen = ref(false);
const windowWidth = ref(typeof window !== 'undefined' ? window.innerWidth : 1024);

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};

const closeMobileMenu = () => {
  if (windowWidth.value < 768) {
    isMobileMenuOpen.value = false;
  }
};

// Watch route changes to close menu
watch(() => route.path, () => {
  closeMobileMenu();
});

// Handle window resize for menu
if (typeof window !== 'undefined') {
  const handleResize = () => {
    windowWidth.value = window.innerWidth;
    if (windowWidth.value >= 768) {
      isMobileMenuOpen.value = true;
    } else {
      isMobileMenuOpen.value = false;
    }
  };
  window.addEventListener('resize', handleResize);
  // Initialize based on screen size
  if (windowWidth.value >= 768) {
    isMobileMenuOpen.value = true;
  }
}

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
const showRegisterTab = ref(false);
const loginForm = ref({
  username: '',
  password: ''
});
const loginLoading = ref(false);
const loginMessage = ref('');
const loginSuccess = ref(false);
const registerForm = ref({
  username: '',
  email: '',
  phone: '',
  first_name: '',
  last_name: '',
  password: '',
  password_confirm: ''
});
const registerLoading = ref(false);
const registerMessage = ref('');
const registerSuccess = ref(false);
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

const handleRegister = async () => {
  if (registerForm.value.password !== registerForm.value.password_confirm) {
    registerMessage.value = 'رمزهای عبور مطابقت ندارند';
    registerSuccess.value = false;
    return;
  }
  
  registerLoading.value = true;
  registerMessage.value = '';
  
  try {
    const response = await fetch(getApiUrl('/api/accounts/register/'), {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      credentials: 'include',
      body: JSON.stringify(registerForm.value)
    });
    
    const data = await response.json();
    
    if (data.success) {
      registerSuccess.value = true;
      registerMessage.value = data.message || 'درخواست عضویت شما ثبت شد. لطفاً منتظر تایید مدیریت باشید.';
      
      // Reset form
      registerForm.value = {
        username: '',
        email: '',
        phone: '',
        first_name: '',
        last_name: '',
        password: '',
        password_confirm: ''
      };
      
      // Don't close modal immediately, let user see the success message
      setTimeout(() => {
        showRegisterTab.value = false;
      }, 3000);
    } else {
      registerSuccess.value = false;
      if (data.errors) {
        if (typeof data.errors === 'string') {
          registerMessage.value = data.errors;
        } else {
          const firstError = Object.values(data.errors)[0];
          registerMessage.value = Array.isArray(firstError) ? firstError[0] : firstError;
        }
      } else {
        registerMessage.value = 'خطا در ثبت درخواست';
      }
    }
  } catch (error) {
    registerSuccess.value = false;
    registerMessage.value = 'خطا در ارتباط با سرور';
  } finally {
    registerLoading.value = false;
  }
};

onMounted(() => {
  // Check authentication status on mount
  checkAuthStatus();
  
  // Set initial direction based on locale
  document.documentElement.dir = locale.value === 'fa' ? 'rtl' : 'ltr';
  document.documentElement.lang = locale.value;
  
  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
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
          closeMobileMenu();
        }
      }
    });
  });
  
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
  
  window.addEventListener('scroll', onScroll, { passive: true });
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
  overflow: visible !important;
  width: 100%;
  position: relative;
}

.app-header {
  position: sticky;
  top: 0;
  z-index: 1020;
  padding: 0.75rem 0;
  overflow: visible !important;
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
  flex: 1 0 auto;
  display: block;
  padding-bottom: 2rem;
  overflow: visible !important;
  width: 100%;
}

.auth-modal {
  border-radius: var(--radius-lg);
  padding: 1.5rem 1.75rem 1.75rem;
}

.nav-tabs {
  border-bottom: 2px solid rgba(0, 0, 0, 0.1);
}

.nav-tabs .nav-link {
  border: none;
  border-bottom: 2px solid transparent;
  color: rgba(17, 24, 39, 0.6);
  padding: 0.75rem 1.5rem;
  transition: var(--transition-snappy);
}

.nav-tabs .nav-link:hover {
  border-color: transparent;
  color: var(--brand-primary);
}

.nav-tabs .nav-link.active {
  color: var(--brand-primary);
  border-bottom-color: var(--brand-primary);
  background: transparent;
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
  padding-top: 3rem;
  padding-bottom: 2rem;
  margin-top: auto;
  width: 100%;
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

/* Mobile Menu Styles */
.navbar-collapse.mobile-menu {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

@media (min-width: 768px) {
  .navbar-collapse.mobile-menu {
    display: flex !important;
  }
}

@media (max-width: 767.98px) {
  .navbar-collapse.mobile-menu {
    display: none !important;
    opacity: 0;
    max-height: 0;
    overflow: hidden;
    margin-top: 1rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }
  
  .navbar-collapse.mobile-menu.mobile-menu-open {
    display: block !important;
    opacity: 1;
    max-height: 2000px;
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(20px);
    border-radius: 16px;
    padding: 1rem;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
    z-index: 1025;
  }
  
  .menu-links .nav-link {
    padding: 0.75rem 1rem;
    font-size: 0.95rem;
  }
  
  .navbar-nav.menu-links {
    gap: 0.25rem;
  }
  
  .dropdown-menu {
    border: none;
    box-shadow: none;
    background: rgba(248, 250, 255, 0.8);
    border-radius: 12px;
    margin-top: 0.5rem;
    padding: 0.5rem 0;
  }
  
  .dropdown-item {
    padding: 0.6rem 1rem;
    font-size: 0.9rem;
    border-radius: 8px;
    margin: 0.15rem 0.5rem;
  }
  
  .dropdown-item:hover {
    background: rgba(13, 110, 253, 0.1);
  }
  
  .social-links {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(0, 0, 0, 0.1);
    justify-content: center;
  }
  
  .btn-login {
    width: 100%;
    justify-content: center;
  }
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
    padding: 1rem 0;
  }

  .footer-upper {
    padding: 1.5rem;
  }
  
  .app-header {
    padding: 0.5rem 0;
  }
  
  .navbar-toggler {
    padding: 0.5rem 0.75rem !important;
    font-size: 1rem;
  }
  
  .btn-lang {
    width: 40px;
    height: 40px;
    font-size: 0.8rem;
  }
  
  .btn-login {
    padding: 0.5rem 1rem !important;
    font-size: 0.85rem;
    min-width: auto;
  }
  
  .modal-dialog {
    margin: 0.5rem;
    max-width: calc(100% - 1rem);
  }
  
  .auth-modal {
    padding: 1.25rem 1.5rem !important;
  }
  
  .modal-title {
    font-size: 1.25rem;
  }
  
  .modal-icon {
    width: 60px;
    height: 60px;
    font-size: 1.4rem;
  }
}
</style>
