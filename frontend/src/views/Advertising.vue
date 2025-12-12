<template>
  <div class="page-shell advertising-view position-relative overflow-x-hidden">
    <section class="page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center">
          <div class="col-md-12 text-center">
            <span class="soft-badge secondary mb-3">
              <i class="fa fa-bullhorn"></i>
              {{ $t('nav.advertising') }}
            </span>
            <h1 class="display-4 fw-bold mb-4">{{ $t('nav.advertising') }}</h1>
            <p class="lead text-muted">فرصت‌های تبلیغاتی و همکاری با انجمن علمی ریه کودکان ایران</p>
          </div>
        </div>
      </div>
    </section>

    <section class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row g-4">
          <div class="col-md-12">
            <div class="glass-card p-5">
              <h2 class="fw-bold mb-4">فرصت‌های تبلیغاتی</h2>
              <p class="text-muted mb-4">برای اطلاع از فرصت‌های تبلیغاتی و همکاری با انجمن، با ما تماس بگیرید</p>
              <div class="row g-4">
                <div class="col-md-6">
                  <div class="advertising-card glass-card p-4">
                    <i class="fa fa-phone fa-3x text-primary mb-3"></i>
                    <h4 class="fw-bold mb-3">تماس با ما</h4>
                    <p>برای اطلاعات بیشتر در مورد فرصت‌های تبلیغاتی با دفتر انجمن تماس بگیرید</p>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="advertising-card glass-card p-4">
                    <i class="fa fa-envelope fa-3x text-primary mb-3"></i>
                    <h4 class="fw-bold mb-3">ارسال ایمیل</h4>
                    <p>درخواست خود را از طریق ایمیل برای ما ارسال کنید</p>
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
.advertising-view {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.advertising-card {
  transition: var(--transition-snappy);
  text-align: center;
}

.advertising-card:hover {
  transform: translateY(-5px);
}
</style>

