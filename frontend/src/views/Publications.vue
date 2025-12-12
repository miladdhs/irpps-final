<template>
  <div class="page-shell publications-view position-relative overflow-x-hidden">
    <section class="page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center">
          <div class="col-md-12 text-center">
            <span class="soft-badge secondary mb-3">
              <i class="fa fa-book"></i>
              {{ $t('nav.publications') }}
            </span>
            <h1 class="display-4 fw-bold mb-4">{{ $t('nav.publications') }}</h1>
            <p class="lead text-muted">انتشارات علمی و مجلات انجمن علمی ریه کودکان ایران</p>
          </div>
        </div>
      </div>
    </section>

    <section class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row g-4">
          <div class="col-md-12">
            <div class="glass-card p-5">
              <h2 class="fw-bold mb-4">انتشارات انجمن</h2>
              <p class="text-muted mb-4">مجلات، کتاب‌ها و مقالات علمی منتشر شده توسط انجمن</p>
              <div class="row g-4">
                <div class="col-md-4">
                  <div class="publication-card glass-card p-4 text-center">
                    <i class="fa fa-newspaper-o fa-3x text-primary mb-3"></i>
                    <h5 class="fw-bold mb-2">خبرنامه‌ها</h5>
                    <p class="text-muted">خبرنامه‌های سالانه انجمن</p>
                  </div>
                </div>
                <div class="col-md-4">
                  <div class="publication-card glass-card p-4 text-center">
                    <i class="fa fa-book fa-3x text-primary mb-3"></i>
                    <h5 class="fw-bold mb-2">کتابچه کنگره‌ها</h5>
                    <p class="text-muted">کتابچه‌های کنگره‌ها و همایش‌ها</p>
                  </div>
                </div>
                <div class="col-md-4">
                  <div class="publication-card glass-card p-4 text-center">
                    <i class="fa fa-file-text fa-3x text-primary mb-3"></i>
                    <h5 class="fw-bold mb-2">مجله انجمن</h5>
                    <p class="text-muted">مجله علمی انجمن</p>
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
.publications-view {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.publication-card {
  transition: var(--transition-snappy);
}

.publication-card:hover {
  transform: translateY(-5px);
}
</style>

