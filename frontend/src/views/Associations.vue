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
              <p class="text-muted mb-4">انجمن‌های ملی و بین‌المللی مرتبط با ریه کودکان و پزشکی اطفال</p>
              <div class="row g-4">
                <div 
                  class="col-lg-6 col-md-6" 
                  v-for="association in associations" 
                  :key="association.id"
                >
                  <a 
                    :href="association.url" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    class="association-link text-decoration-none"
                  >
                    <div class="association-card glass-card p-4 h-100">
                      <div class="association-icon mb-3">
                        <i :class="association.icon"></i>
                      </div>
                      <h4 class="fw-bold mb-3">{{ association.name }}</h4>
                      <p class="text-muted mb-0">{{ association.description }}</p>
                      <div class="association-arrow mt-3">
                        <i class="fa fa-external-link"></i>
                        <span class="ms-2">بازدید از وب‌سایت</span>
                      </div>
                    </div>
                  </a>
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
import { ref, onMounted } from 'vue';

type Association = {
  id: number;
  name: string;
  description: string;
  url: string;
  icon: string;
};

const associations = ref<Association[]>([
  {
    id: 1,
    name: 'انجمن ریه ایران',
    description: 'انجمن علمی ریه ایران - مرجع تخصصی بیماری‌های ریوی',
    url: 'https://chestnet.ir/fa',
    icon: 'fa fa-lungs fa-3x text-primary'
  },
  {
    id: 2,
    name: 'European Respiratory Society',
    description: 'انجمن تنفسی اروپا - مرجع بین‌المللی بیماری‌های ریوی',
    url: 'https://www.ersnet.org/',
    icon: 'fa fa-globe fa-3x text-primary'
  },
  {
    id: 3,
    name: 'American Thoracic Society',
    description: 'انجمن قفسه سینه آمریکا - مرجع علمی بیماری‌های ریوی',
    url: 'https://site.thoracic.org/',
    icon: 'fa fa-stethoscope fa-3x text-primary'
  },
  {
    id: 4,
    name: 'انجمن پزشکان کودکان ایران',
    description: 'انجمن علمی پزشکان کودکان ایران - مرجع تخصصی اطفال',
    url: 'https://irpediatrics.com/',
    icon: 'fa fa-child fa-3x text-primary'
  }
]);

onMounted(() => {
  window.scrollTo(0, 0);
});
</script>

<style scoped>
.associations-view {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.association-link {
  display: block;
  color: inherit;
}

.association-link:hover {
  color: inherit;
  text-decoration: none;
}

.association-card {
  transition: var(--transition-snappy);
  text-align: center;
  display: flex;
  flex-direction: column;
  cursor: pointer;
}

.association-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}

.association-icon {
  color: var(--col_blue, #2563eb);
}

.association-arrow {
  color: var(--col_blue, #2563eb);
  font-size: 0.9rem;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.association-card:hover .association-arrow {
  opacity: 1;
}

.association-card h4 {
  color: #14233c;
  transition: color 0.3s ease;
}

.association-card:hover h4 {
  color: var(--col_blue, #2563eb);
}
</style>

