<template>
  <div class="services-view position-relative">
    <span class="services-bubble bubble-1 blurred-bubble"></span>
    <span class="services-bubble bubble-2 blurred-bubble"></span>

    <section id="services-hero" class="services-hero-section page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center min-vh-80">
          <div class="col-md-6">
            <div class="services-hero-content animate__animated animate__fadeInRight">
              <span class="soft-badge mb-3"><i class="fa fa-calendar"></i> {{ $t('services.badge') }}</span>
              <h1 class="display-4 fw-bold mb-4">{{ $t('services.title') }}</h1>
              <p class="lead mb-4">{{ $t('services.subtitle') }}</p>
              <p class="mb-4 text-muted">{{ $t('services.description') }}</p>
              <div class="services-hero-buttons d-flex flex-wrap gap-2">
                <router-link to="/news" class="soft-button primary animate__animated animate__pulse">
                  <i class="fa fa-newspaper"></i>
                  {{ $t('services.news') }}
                </router-link>
                <router-link to="/events" class="soft-button outline">
                  <i class="fa fa-calendar"></i>
                  {{ $t('services.events') }}
                </router-link>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="services-hero-image animate__animated animate__fadeInLeft">
              <div class="services-hero-image-wrapper image-frame image-frame--wide">
                <img :src="getAssetUrl('img/hero-events.svg')" class="img-fluid" alt="خدمات انجمن">
                <div class="floating-elements">
                  <div class="floating-icon floating-icon-1">
                    <i class="fa fa-newspaper"></i>
                  </div>
                  <div class="floating-icon floating-icon-3">
                    <i class="fa fa-calendar"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row text-center mb-5 section-heading">
          <div class="col-md-12">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">{{ $t('services.servicesTitle') }}</h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('services.servicesSubtitle') }}</p>
          </div>
        </div>
        <div class="row g-4">
          <div class="col-md-6 col-lg-4" v-for="(service, index) in serviceCards" :key="service.title">
            <div class="service-card glass-card p-4 animate__animated animate__fadeInUp" :class="'animate__delay-' + (index + 2) + 's'">
              <div class="service-icon mb-4">
                <i :class="'fa fa-2x col_blue ' + service.icon"></i>
              </div>
              <h5 class="fw-bold mb-3">{{ service.title }}</h5>
              <p class="text-muted">{{ service.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>


  </div>
</template>

<script setup lang="ts">
import { onMounted, computed } from 'vue';
import { useI18n } from 'vue-i18n';
import { getAssetUrl } from '@/utils/assets';

const { t } = useI18n();


const serviceCards = computed(() => [
  {
    icon: 'fa-graduation-cap',
    title: t('services.service1'),
    description: t('services.service1Desc')
  },
  {
    icon: 'fa-microphone',
    title: t('services.service2'),
    description: t('services.service2Desc')
  },
  {
    icon: 'fa-users',
    title: t('services.service3'),
    description: t('services.service3Desc')
  },
  {
    icon: 'fa-book',
    title: t('services.service4'),
    description: t('services.service4Desc')
  },
  {
    icon: 'fa-flask',
    title: t('services.service5'),
    description: t('services.service5Desc')
  },
  {
    icon: 'fa-certificate',
    title: t('services.service6'),
    description: t('services.service6Desc')
  }
]);

onMounted(() => {

  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate__animated');
      }
    });
  }, observerOptions);

  document.querySelectorAll('.animate__fadeInUp, .animate__fadeInLeft, .animate__fadeInRight').forEach(el => {
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

<style scoped>
</style>
