<template>
  <div class="page-shell gallery-view position-relative">
    <section class="page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center">
          <div class="col-md-12 text-center">
            <span class="soft-badge secondary mb-3">
              <i class="fa fa-image"></i>
              {{ $t('nav.aboutGallery') }}
            </span>
            <h1 class="display-4 fw-bold mb-4">{{ $t('nav.aboutGallery') }}</h1>
            <p class="lead text-muted">گالری تصاویر فعالیت‌ها و رویدادهای انجمن علمی ریه کودکان ایران</p>
          </div>
        </div>
      </div>
    </section>

    <section class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row g-4">
          <div class="col-md-12">
            <div class="glass-card p-5">
              <h2 class="fw-bold mb-4">گالری تصاویر</h2>
              <p class="text-muted mb-4">تصاویر مربوط به همایش‌ها، کارگاه‌ها و فعالیت‌های انجمن</p>
              <div class="row g-3">
                <div class="col-md-4">
                  <div class="gallery-item glass-card p-3 text-center">
                    <i class="fa fa-image fa-4x text-primary mb-3"></i>
                    <p class="mb-0">همایش‌ها و کنگره‌ها</p>
                  </div>
                </div>
                <div class="col-md-4">
                  <div class="gallery-item glass-card p-3 text-center">
                    <i class="fa fa-image fa-4x text-primary mb-3"></i>
                    <p class="mb-0">کارگاه‌های آموزشی</p>
                  </div>
                </div>
                <div class="col-md-4">
                  <div class="gallery-item glass-card p-3 text-center">
                    <i class="fa fa-image fa-4x text-primary mb-3"></i>
                    <p class="mb-0">فعالیت‌های علمی</p>
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
.gallery-view {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.gallery-item {
  transition: var(--transition-snappy);
  min-height: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.gallery-item:hover {
  transform: translateY(-5px);
}
</style>

