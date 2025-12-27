<template>
  <div class="publications-view position-relative">
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
                <!-- Newsletters -->
                <div class="col-lg-4 col-md-6">
                  <div class="publication-card glass-card p-4 text-center h-100" @click="handleCategoryClick('newsletters')">
                    <div class="publication-icon mb-3">
                      <i class="fa fa-newspaper-o fa-3x text-primary"></i>
                    </div>
                    <h5 class="fw-bold mb-2">خبرنامه‌ها</h5>
                    <p class="text-muted mb-3">خبرنامه‌های سالانه انجمن</p>
                    <button class="soft-button primary btn-sm">
                      <i class="fa fa-download me-1"></i>
                      مشاهده و دانلود
                    </button>
                  </div>
                </div>

                <!-- Congress Booklets -->
                <div class="col-lg-4 col-md-6">
                  <div class="publication-card glass-card p-4 text-center h-100" @click="handleCategoryClick('congress')">
                    <div class="publication-icon mb-3">
                      <i class="fa fa-book fa-3x text-primary"></i>
                    </div>
                    <h5 class="fw-bold mb-2">کتابچه کنگره‌ها و همایش‌ها</h5>
                    <p class="text-muted mb-3">کتابچه‌های کنگره‌ها و همایش‌های علمی</p>
                    <button class="soft-button primary btn-sm">
                      <i class="fa fa-download me-1"></i>
                      مشاهده و دانلود
                    </button>
                  </div>
                </div>

                <!-- Association Journal -->
                <div class="col-lg-4 col-md-6">
                  <div class="publication-card glass-card p-4 text-center h-100" @click="handleJournalClick">
                    <div class="publication-icon mb-3">
                      <i class="fa fa-file-text fa-3x text-primary"></i>
                    </div>
                    <h5 class="fw-bold mb-2">مجله انجمن</h5>
                    <p class="text-muted mb-3">مجله علمی انجمن در سایت Brieflands</p>
                    <button class="soft-button primary btn-sm">
                      <i class="fa fa-external-link me-1"></i>
                      مشاهده در سایت
                    </button>
                  </div>
                </div>

                <!-- Other Products -->
                <div class="col-lg-4 col-md-6">
                  <div class="publication-card glass-card p-4 text-center h-100" @click="handleCategoryClick('products')">
                    <div class="publication-icon mb-3">
                      <i class="fa fa-archive fa-3x text-primary"></i>
                    </div>
                    <h5 class="fw-bold mb-2">سایر محصولات</h5>
                    <p class="text-muted mb-3">سایر انتشارات و محصولات علمی</p>
                    <button class="soft-button primary btn-sm">
                      <i class="fa fa-download me-1"></i>
                      مشاهده و دانلود
                    </button>
                  </div>
                </div>

                <!-- Research -->
                <div class="col-lg-4 col-md-6">
                  <div class="publication-card glass-card p-4 text-center h-100" @click="handleCategoryClick('research')">
                    <div class="publication-icon mb-3">
                      <i class="fa fa-flask fa-3x text-primary"></i>
                    </div>
                    <h5 class="fw-bold mb-2">تحقیقات و پژوهش</h5>
                    <p class="text-muted mb-3">مقالات و تحقیقات علمی انجمن</p>
                    <button class="soft-button primary btn-sm">
                      <i class="fa fa-download me-1"></i>
                      مشاهده و دانلود
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Files Modal -->
    <div v-if="showFilesModal" class="modal fade show d-block" tabindex="-1" style="background: rgba(0,0,0,0.5);" @click.self="showFilesModal = false">
      <div class="modal-dialog modal-lg modal-dialog-centered">
        <div class="modal-content glass-card border-0">
          <div class="modal-header border-0">
            <h5 class="modal-title">{{ currentCategoryTitle }}</h5>
            <button type="button" class="btn-close" @click="showFilesModal = false"></button>
          </div>
          <div class="modal-body">
            <div v-if="loading" class="text-center py-4">
              <i class="fa fa-spinner fa-spin fa-2x text-primary"></i>
              <p class="mt-2">در حال بارگذاری...</p>
            </div>
            <div v-else-if="files.length === 0" class="text-center py-4">
              <i class="fa fa-folder-open fa-2x text-muted"></i>
              <p class="mt-2 text-muted">فایلی در این دسته یافت نشد</p>
            </div>
            <div v-else class="row g-3">
              <div v-for="file in files" :key="file.name" class="col-12">
                <div class="file-item glass-card p-3 d-flex align-items-center">
                  <div class="file-icon me-3">
                    <i :class="getFileIcon(file.type)" class="fa-2x text-primary"></i>
                  </div>
                  <div class="file-info flex-grow-1">
                    <h6 class="mb-1">{{ file.name }}</h6>
                    <small v-if="file.size > 0" class="text-muted">{{ formatFileSize(file.size) }}</small>
                  </div>
                  <button @click="downloadFile(file)" class="soft-button primary btn-sm">
                    <i class="fa fa-download me-1"></i>
                    دانلود
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { getApiUrl } from '@/utils/api';

const showFilesModal = ref(false);
const currentCategoryTitle = ref('');
const files = ref<any[]>([]);
const loading = ref(false);

const categoryTitles: Record<string, string> = {
  newsletters: 'خبرنامه‌ها',
  congress: 'کتابچه کنگره‌ها و همایش‌ها',
  products: 'سایر محصولات',
  research: 'تحقیقات و پژوهش'
};

const handleCategoryClick = async (category: string) => {
  currentCategoryTitle.value = categoryTitles[category];
  showFilesModal.value = true;
  loading.value = true;
  files.value = [];
  
  // Handle "Congress" booklets from local files
  if (category === 'congress') {
    // Use hardcoded list directly to avoid JSON parsing issues
    files.value = [
      {
        name: '1_23033290624.pdf',
        url: '/Content/Other/1_23033290624.pdf',
        type: 'application/pdf',
        size: 0
      }
    ];
    loading.value = false;
    return;
  }
  
  // Handle "Other" products from local files
  if (category === 'products') {
    // Use hardcoded list directly to avoid JSON parsing issues
    files.value = [
      {
        name: 'DOC-20251227-WA0007.pdf',
        url: '/Content/Other/DOC-20251227-WA0007.pdf',
        type: 'application/pdf',
        size: 0
      },
      {
        name: 'خلاصه مقالات 5 همایش 403.pdf',
        url: '/Content/Other/خلاصه مقالات 5 همایش 403.pdf',
        type: 'application/pdf',
        size: 0
      }
    ];
    loading.value = false;
    return;
  }
  
  // Handle other categories from API
  try {
    const response = await fetch(getApiUrl(`/api/news/publications/files/?category=${category}`), {
      credentials: 'include'
    });
    
    const data = await response.json();
    
    if (data.success) {
      files.value = data.files || [];
    } else {
      console.error('Error loading files:', data.errors);
      files.value = [];
    }
  } catch (error) {
    console.error('Error loading files:', error);
    files.value = [];
  } finally {
    loading.value = false;
  }
};

const handleJournalClick = () => {
  // Redirect to external journal website
  window.open('https://brieflands.com/journals/jcp', '_blank');
};

const getFileIcon = (fileType: string) => {
  if (fileType.includes('pdf')) return 'fa fa-file-pdf-o';
  if (fileType.includes('doc')) return 'fa fa-file-word-o';
  if (fileType.includes('image')) return 'fa fa-file-image-o';
  return 'fa fa-file-o';
};

const formatFileSize = (bytes: number) => {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
};

const downloadFile = (file: any) => {
  // Create a temporary anchor element to trigger download
  const link = document.createElement('a');
  link.href = file.url;
  link.download = file.name;
  link.target = '_blank';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};

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
  cursor: pointer;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.publication-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--glass-shadow-hover);
  border-color: rgba(13, 110, 253, 0.3);
}

.publication-icon {
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.file-item {
  transition: var(--transition-snappy);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.file-item:hover {
  border-color: rgba(13, 110, 253, 0.3);
  transform: translateX(5px);
}

.file-icon {
  width: 50px;
  text-align: center;
}

.modal-content {
  border-radius: var(--radius-lg);
  backdrop-filter: blur(20px);
}

@media (max-width: 768px) {
  .publication-card {
    margin-bottom: 1rem;
  }
  
  .modal-dialog {
    margin: 1rem;
  }
}
</style>

