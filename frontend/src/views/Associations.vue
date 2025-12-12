<template>
  <div class="associations-view position-relative">
    <section class="page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center">
          <div class="col-md-12 text-center">
            <span class="soft-badge secondary mb-3">
              <i class="fa fa-sitemap"></i>
              {{ $t('nav.associations') }}
            </span>
            <h1 class="display-4 fw-bold mb-4">{{ $t('nav.associations') }}</h1>
            <p class="lead text-muted">انجمن‌های وابسته و مرتبط با انجمن علمی ریه کودکان ایران</p>
          </div>
        </div>
      </div>
    </section>

    <section class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row g-4">
          <div class="col-md-12">
            <div class="glass-card p-5">
              <h2 class="fw-bold mb-4">انجمن‌های مرتبط</h2>
              <p class="text-muted mb-4">انجمن‌های فوق تخصصی و انجمن‌های استان/شهرستان</p>
              <div class="row g-4">
                <div class="col-md-6">
                  <div class="association-card glass-card p-4">
                    <i class="fa fa-hospital-o fa-3x text-primary mb-3"></i>
                    <h4 class="fw-bold mb-3">انجمن‌های فوق تخصصی</h4>
                    <p>انجمن‌های تخصصی مرتبط با ریه کودکان</p>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="association-card glass-card p-4">
                    <i class="fa fa-map-marker fa-3x text-primary mb-3"></i>
                    <h4 class="fw-bold mb-3">انجمن‌های استان/شهرستان</h4>
                    <p>انجمن‌های محلی در استان‌ها و شهرستان‌های مختلف</p>
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
.associations-view {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.association-card {
  transition: var(--transition-snappy);
  text-align: center;
}

.association-card:hover {
  transform: translateY(-5px);
}
</style>

