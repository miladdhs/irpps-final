<template>
  <div class="page-shell home-view position-relative">
    <span class="home-bubble bubble-1 blurred-bubble"></span>
    <span class="home-bubble bubble-2 blurred-bubble"></span>
    <span class="home-bubble bubble-3 blurred-bubble"></span>

    <section id="hero" class="hero-section page-hero glass-section py-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center min-vh-80">
          <div class="col-md-6">
            <div class="hero-content animate__animated animate__fadeInRight">
              <span class="soft-badge secondary mb-3">
                <i class="fa fa-heartbeat"></i>
                {{ $t('home.badge') }}
              </span>
              <h1 class="display-4 fw-bold mb-4 text-primary">{{ $t('home.title') }}</h1>
              <p class="lead mb-4">{{ $t('home.subtitle') }}</p>
              <p class="mb-4 text-muted">{{ $t('home.description') }}</p>
              <div class="hero-buttons">
                <a class="soft-button primary hero-cta animate__animated animate__pulse" href="#about">
                  <i class="fa fa-arrow-right"></i>
                  {{ $t('home.learnMore') }}
                </a>
                <a class="soft-button outline hero-cta" href="#contact">
                  <i class="fa fa-phone"></i>
                  {{ $t('home.contactUs') }}
                </a>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="hero-image animate__animated animate__fadeInLeft">
              <div class="hero-image-wrapper image-frame image-frame--compact">
                <img :src="getAssetUrl('img/hero-home.svg')" class="img-fluid rounded-4 shadow-lg" :alt="$t('home.title')">
                <div class="floating-elements">
                  <div class="floating-icon floating-icon-1">
                    <i class="fa fa-heartbeat"></i>
                  </div>
                  <div class="floating-icon floating-icon-2">
                    <i class="fa fa-stethoscope"></i>
                  </div>
                  <div class="floating-icon floating-icon-3">
                    <i class="fa fa-user-md"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="about" class="p_3 home-section glass-section">
      <div class="container-xl">
        <div class="row">
          <div class="col-md-12 text-center mb-5 section-heading">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">{{ $t('home.aboutTitle') }}</h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('home.aboutSubtitle') }}</p>
          </div>
        </div>
        <div class="row g-4">
          <div class="col-md-4">
            <div class="feature-card glass-card text-center border-0 p-5 h-100 animate__animated animate__fadeInUp animate__delay-2s">
              <div class="feature-icon mb-4">
                <i class="fa fa-heartbeat fa-3x col_blue"></i>
              </div>
              <h5 class="fw-bold mb-3">{{ $t('home.feature1Title') }}</h5>
              <p class="text-muted">{{ $t('home.feature1Desc') }}</p>
            </div>
          </div>
          <div class="col-md-4">
            <div class="feature-card glass-card text-center border-0 p-5 h-100 animate__animated animate__fadeInUp animate__delay-3s">
              <div class="feature-icon mb-4">
                <i class="fa fa-graduation-cap fa-3x col_blue"></i>
              </div>
              <h5 class="fw-bold mb-3">{{ $t('home.feature2Title') }}</h5>
              <p class="text-muted">{{ $t('home.feature2Desc') }}</p>
            </div>
          </div>
          <div class="col-md-4">
            <div class="feature-card glass-card text-center border-0 p-5 h-100 animate__animated animate__fadeInUp animate__delay-4s">
              <div class="feature-icon mb-4">
                <i class="fa fa-users fa-3x col_blue"></i>
              </div>
              <h5 class="fw-bold mb-3">{{ $t('home.feature3Title') }}</h5>
              <p class="text-muted">{{ $t('home.feature3Desc') }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="stats" class="p_3 home-stats-section">
      <div class="container-xl">
        <div class="row text-center">
          <div class="col-md-3 col-sm-6 mb-4">
            <div class="stat-item glass-card animate__animated animate__fadeInUp">
              <div class="stat-icon mb-3">
                <i class="fa fa-user-md fa-2x"></i>
              </div>
              <h2 class="fw-bold counter" ref="counter1" data-target="50">0</h2>
              <p class="mb-0">{{ $t('home.stat1') }}</p>
            </div>
          </div>
          <div class="col-md-3 col-sm-6 mb-4">
            <div class="stat-item glass-card animate__animated animate__fadeInUp animate__delay-1s">
              <div class="stat-icon mb-3">
                <i class="fa fa-heart fa-2x"></i>
              </div>
              <h2 class="fw-bold counter" ref="counter2" data-target="1000">0</h2>
              <p class="mb-0">{{ $t('home.stat2') }}</p>
            </div>
          </div>
          <div class="col-md-3 col-sm-6 mb-4">
            <div class="stat-item glass-card animate__animated animate__fadeInUp animate__delay-2s">
              <div class="stat-icon mb-3">
                <i class="fa fa-book fa-2x"></i>
              </div>
              <h2 class="fw-bold counter" ref="counter3" data-target="25">0</h2>
              <p class="mb-0">{{ $t('home.stat3') }}</p>
            </div>
          </div>
          <div class="col-md-3 col-sm-6 mb-4">
            <div class="stat-item glass-card animate__animated animate__fadeInUp animate__delay-3s">
              <div class="stat-icon mb-3">
                <i class="fa fa-trophy fa-2x"></i>
              </div>
              <h2 class="fw-bold counter" ref="counter4" data-target="15">0</h2>
              <p class="mb-0">{{ $t('home.stat4') }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="services" class="p_3 home-section glass-section">
      <div class="container-xl">
        <div class="row text-center mb-5 section-heading">
          <div class="col-md-12">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">{{ $t('home.servicesTitle') }}</h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('home.servicesSubtitle') }}</p>
          </div>
        </div>
        <div class="row g-4">
          <div class="col-md-6 col-lg-4">
            <div class="service-card glass-card p-4 h-100 animate__animated animate__fadeInUp animate__delay-2s">
              <div class="service-icon mb-4">
                <i class="fa fa-stethoscope fa-2x col_blue"></i>
              </div>
              <h5 class="fw-bold mb-3">{{ $t('home.service1Title') }}</h5>
              <p class="text-muted">{{ $t('home.service1Desc') }}</p>
            </div>
          </div>
          <div class="col-md-6 col-lg-4">
            <div class="service-card glass-card p-4 h-100 animate__animated animate__fadeInUp animate__delay-3s">
              <div class="service-icon mb-4">
                <i class="fa fa-medkit fa-2x col_blue"></i>
              </div>
              <h5 class="fw-bold mb-3">{{ $t('home.service2Title') }}</h5>
              <p class="text-muted">{{ $t('home.service2Desc') }}</p>
            </div>
          </div>
          <div class="col-md-6 col-lg-4">
            <div class="service-card glass-card p-4 h-100 animate__animated animate__fadeInUp animate__delay-4s">
              <div class="service-icon mb-4">
                <i class="fa fa-heart fa-2x col_blue"></i>
              </div>
              <h5 class="fw-bold mb-3">{{ $t('home.service3Title') }}</h5>
              <p class="text-muted">{{ $t('home.service3Desc') }}</p>
            </div>
          </div>
          <div class="col-md-6 col-lg-4">
            <div class="service-card glass-card p-4 h-100 animate__animated animate__fadeInUp animate__delay-5s">
              <div class="service-icon mb-4">
                <i class="fa fa-graduation-cap fa-2x col_blue"></i>
              </div>
              <h5 class="fw-bold mb-3">{{ $t('home.service4Title') }}</h5>
              <p class="text-muted">{{ $t('home.service4Desc') }}</p>
            </div>
          </div>
          <div class="col-md-6 col-lg-4">
            <div class="service-card glass-card p-4 h-100 animate__animated animate__fadeInUp animate__delay-6s">
              <div class="service-icon mb-4">
                <i class="fa fa-microscope fa-2x col_blue"></i>
              </div>
              <h5 class="fw-bold mb-3">{{ $t('home.service5Title') }}</h5>
              <p class="text-muted">{{ $t('home.service5Desc') }}</p>
            </div>
          </div>
          <div class="col-md-6 col-lg-4">
            <div class="service-card glass-card p-4 h-100 animate__animated animate__fadeInUp animate__delay-7s">
              <div class="service-icon mb-4">
                <i class="fa fa-phone fa-2x col_blue"></i>
              </div>
              <h5 class="fw-bold mb-3">{{ $t('home.service6Title') }}</h5>
              <p class="text-muted">{{ $t('home.service6Desc') }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { getAssetUrl } from '@/utils/assets';

const counter1 = ref<HTMLElement | null>(null);
const counter2 = ref<HTMLElement | null>(null);
const counter3 = ref<HTMLElement | null>(null);
const counter4 = ref<HTMLElement | null>(null);

function animateCounter(element: HTMLElement) {
  const target = parseInt(element.getAttribute('data-target') || '0');
  const duration = 1200;
  const increment = target / (duration / 16);
  let current = 0;
  
  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      current = target;
      clearInterval(timer);
    }
    element.textContent = Math.floor(current).toString();
  }, 16);
}

onMounted(() => {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate__animated');
        if (entry.target.classList.contains('counter')) {
          animateCounter(entry.target as HTMLElement);
          observer.unobserve(entry.target);
        }
      }
    });
  }, observerOptions);

  document.querySelectorAll('.animate__fadeInUp, .animate__fadeInLeft, .animate__fadeInRight, .counter').forEach(el => {
    observer.observe(el);
  });

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector((this as HTMLElement).getAttribute('href') || '');
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
});
</script>

