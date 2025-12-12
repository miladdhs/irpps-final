<template>
  <div class="page-shell history-view position-relative overflow-x-hidden">
    <section class="page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center">
          <div class="col-md-12 text-center">
            <span class="soft-badge secondary mb-3">
              <i class="fa fa-history"></i>
              {{ $t('nav.aboutHistory') }}
            </span>
            <h1 class="display-4 fw-bold mb-4">{{ $t('nav.aboutHistory') }}</h1>
            <p class="lead text-muted">تاریخچه تأسیس و فعالیت‌های انجمن علمی ریه کودکان ایران</p>
          </div>
        </div>
      </div>
    </section>

    <section class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row">
          <div class="col-md-12">
            <div class="glass-card p-5">
              <h2 class="fw-bold mb-4">تاریخچه انجمن</h2>
              <p class="lead mb-4">
                انجمن علمی ریه کودکان ایران در تاریخ ۱۶ آذر ۱۳۹۵ با هدف ارتقای دانش و آگاهی در زمینه بیماری‌های ریوی کودکان تأسیس شد.
              </p>
              <div class="timeline">
                <div class="timeline-item mb-4">
                  <div class="d-flex align-items-start">
                    <div class="timeline-marker me-3">
                      <i class="fa fa-calendar-check-o fa-2x text-primary"></i>
                    </div>
                    <div>
                      <h4 class="fw-bold">۱۳۹۵ - تأسیس انجمن</h4>
                      <p>انجمن علمی ریه کودکان ایران با همکاری متخصصان برجسته ریه کودکان تأسیس شد.</p>
                    </div>
                  </div>
                </div>
                <div class="timeline-item mb-4">
                  <div class="d-flex align-items-start">
                    <div class="timeline-marker me-3">
                      <i class="fa fa-users fa-2x text-primary"></i>
                    </div>
                    <div>
                      <h4 class="fw-bold">۱۳۹۶ - تشکیل هیئت مدیره اول</h4>
                      <p>اولین هیئت مدیره انجمن با حضور متخصصان مجرب تشکیل شد.</p>
                    </div>
                  </div>
                </div>
                <div class="timeline-item mb-4">
                  <div class="d-flex align-items-start">
                    <div class="timeline-marker me-3">
                      <i class="fa fa-graduation-cap fa-2x text-primary"></i>
                    </div>
                    <div>
                      <h4 class="fw-bold">۱۳۹۷ - شروع فعالیت‌های آموزشی</h4>
                      <p>برگزاری اولین کارگاه‌ها و سمینارهای آموزشی برای پزشکان و پرستاران.</p>
                    </div>
                  </div>
                </div>
                <div class="timeline-item mb-4">
                  <div class="d-flex align-items-start">
                    <div class="timeline-marker me-3">
                      <i class="fa fa-book fa-2x text-primary"></i>
                    </div>
                    <div>
                      <h4 class="fw-bold">۱۳۹۸ - انتشارات علمی</h4>
                      <p>شروع انتشار مجلات و مقالات علمی در زمینه بیماری‌های ریوی کودکان.</p>
                    </div>
                  </div>
                </div>
                <div class="timeline-item">
                  <div class="d-flex align-items-start">
                    <div class="timeline-marker me-3">
                      <i class="fa fa-globe fa-2x text-primary"></i>
                    </div>
                    <div>
                      <h4 class="fw-bold">۱۴۰۰ - گسترش فعالیت‌های بین‌المللی</h4>
                      <p>برگزاری کنگره‌ها و همایش‌های بین‌المللی با حضور متخصصان از سراسر جهان.</p>
                    </div>
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
.history-view {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.timeline-marker {
  min-width: 60px;
  text-align: center;
}
</style>

