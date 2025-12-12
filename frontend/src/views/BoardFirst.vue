<template>
  <div class="page-shell board-view position-relative overflow-x-hidden">
    <section class="page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center">
          <div class="col-md-12 text-center">
            <span class="soft-badge secondary mb-3">
              <i class="fa fa-users"></i>
              {{ $t('nav.boardFirst') }}
            </span>
            <h1 class="display-4 fw-bold mb-4">{{ $t('nav.boardFirst') }}</h1>
            <p class="lead text-muted">{{ $t('about.foundersSubtitle') }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row g-4">
          <div class="col-md-12">
            <div class="board-members-card glass-card p-5">
              <div class="row g-4">
                <div class="col-md-6 col-lg-3">
                  <div class="member-item text-center p-4 glass-chip">
                    <i class="fa fa-user-md col_blue fa-3x mb-3"></i>
                    <h5 class="fw-bold mb-2">دکتر سهیلا خلیل زاده</h5>
                    <span class="badge bg-primary">{{ $t('about.president') }}</span>
                  </div>
                </div>
                <div class="col-md-6 col-lg-3">
                  <div class="member-item text-center p-4 glass-chip">
                    <i class="fa fa-user-md col_blue fa-3x mb-3"></i>
                    <h5 class="fw-bold mb-2">دکتر قمر تاج خانبابائی</h5>
                    <span class="badge bg-success">{{ $t('about.vicePresident') }}</span>
                  </div>
                </div>
                <div class="col-md-6 col-lg-3">
                  <div class="member-item text-center p-4 glass-chip">
                    <i class="fa fa-user-md col_blue fa-3x mb-3"></i>
                    <h5 class="fw-bold mb-2">دکتر محمدرضائی</h5>
                    <span class="badge bg-info">{{ $t('about.secretary') }}</span>
                  </div>
                </div>
                <div class="col-md-6 col-lg-3">
                  <div class="member-item text-center p-4 glass-chip">
                    <i class="fa fa-user-md col_blue fa-3x mb-3"></i>
                    <h5 class="fw-bold mb-2">دکتر علیرضا عشقی</h5>
                    <span class="badge bg-warning text-dark">{{ $t('about.treasurer') }}</span>
                  </div>
                </div>
                <div class="col-md-6 col-lg-3">
                  <div class="member-item text-center p-4 glass-chip">
                    <i class="fa fa-user-md col_blue fa-3x mb-3"></i>
                    <h5 class="fw-bold mb-2">دکتر سید محمد رضا میرکریمی</h5>
                    <span class="badge bg-secondary">{{ $t('about.boardMember') }}</span>
                  </div>
                </div>
                <div class="col-md-6 col-lg-3">
                  <div class="member-item text-center p-4 glass-chip">
                    <i class="fa fa-user-md col_blue fa-3x mb-3"></i>
                    <h5 class="fw-bold mb-2">دکتر بابک قالیباف</h5>
                    <span class="badge bg-secondary">{{ $t('about.boardMember') }}</span>
                  </div>
                </div>
                <div class="col-md-6 col-lg-3">
                  <div class="member-item text-center p-4 glass-chip">
                    <i class="fa fa-user-md col_blue fa-3x mb-3"></i>
                    <h5 class="fw-bold mb-2">دکتر سید حسین میر لوحی</h5>
                    <span class="badge bg-secondary">{{ $t('about.boardMember') }}</span>
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
.board-view {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.member-item {
  transition: var(--transition-snappy);
}

.member-item:hover {
  transform: translateY(-5px);
}
</style>

