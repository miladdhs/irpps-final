<template>
  <div class="education-view position-relative">
    <section class="page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center">
          <div class="col-md-12 text-center">
            <span class="soft-badge secondary mb-3">
              <i class="fa fa-graduation-cap"></i>
              {{ $t('nav.education') }}
            </span>
            <h1 class="display-4 fw-bold mb-4">{{ $t('nav.education') }}</h1>
            <p class="lead text-muted">محتوای آموزشی و دوره‌های تخصصی انجمن علمی ریه کودکان ایران</p>
          </div>
        </div>
      </div>
    </section>

    <section class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row g-4">
          <div class="col-md-12">
            <div class="glass-card p-5">
              <h2 class="fw-bold mb-4">محتوای آموزشی</h2>
              <p class="text-muted mb-4">دوره‌ها، کارگاه‌ها و محتوای آموزشی تخصصی برای پزشکان و خانواده‌ها</p>
              <div class="row g-4">
                <div class="col-md-6">
                  <div class="education-card glass-card p-4">
                    <i class="fa fa-user-md fa-3x text-primary mb-3"></i>
                    <h4 class="fw-bold mb-3">آموزش پزشکان</h4>
                    <p>دوره‌ها و کارگاه‌های تخصصی برای پزشکان و متخصصان ریه کودکان</p>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="education-card glass-card p-4">
                    <i class="fa fa-users fa-3x text-primary mb-3"></i>
                    <h4 class="fw-bold mb-3">همراه والدین</h4>
                    <p>آموزش و راهنمایی برای خانواده‌های کودکان مبتلا به بیماری‌های ریوی</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';

onMounted(() => {
  window.scrollTo(0, 0);
});
</script>

<style scoped>
.education-view {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.education-card {
  transition: var(--transition-snappy);
  text-align: center;
}

.education-card:hover {
  transform: translateY(-5px);
}
</style>

