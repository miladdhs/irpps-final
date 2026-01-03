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
          <div class="modal-body modal-body-scrollable">
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
                <div class="file-item">
                  <div class="file-item-inner glass-card p-3 d-flex align-items-center">
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
  
  // Handle "Other" products from local files
  if (category === 'products') {
    // Use hardcoded list directly to avoid JSON parsing issues
    files.value = [
      {
        name: 'DOC-20251227-WA0007.pdf',
        url: '/Content/Other/DOC-20251227-WA0007.pdf',
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

const downloadFile = async (file: any) => {
  try {
    // Build URL properly - encode each path segment separately
    const urlParts = file.url.split('/').filter((part: string) => part !== '');
    const encodedParts = urlParts.map((part: string) => {
      // Don't encode if it's already encoded or is a protocol
      if (part.includes('://') || part.startsWith('http')) {
        return part;
      }
      // Encode each part to handle Persian characters and special characters
      return encodeURIComponent(decodeURIComponent(part));
    });
    const encodedUrl = '/' + encodedParts.join('/');
    
    // Fetch the file as blob with proper headers
    const response = await fetch(encodedUrl, {
      method: 'GET',
      headers: {
        'Accept': file.type || 'application/octet-stream'
      }
    });
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    // Check content type - if HTML, file doesn't exist
    const contentType = response.headers.get('content-type') || '';
    if (contentType.includes('text/html')) {
      throw new Error('Server returned HTML instead of file. File may not exist.');
    }
    
    // Get blob
    const blob = await response.blob();
    
    // Verify blob is not empty
    if (blob.size === 0) {
      throw new Error('Downloaded file is empty');
    }
    
    // Create download link with proper MIME type
    const blobUrl = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = blobUrl;
    link.download = file.name;
    link.style.display = 'none';
    link.setAttribute('download', file.name);
    
    // Force download by setting download attribute
    document.body.appendChild(link);
    link.click();
    
    // Clean up immediately
    setTimeout(() => {
      if (document.body.contains(link)) {
        document.body.removeChild(link);
      }
      window.URL.revokeObjectURL(blobUrl);
    }, 100);
  } catch (error: any) {
    console.error('Download error:', error);
    
    // Fallback: create direct download link with download attribute
    try {
      const urlParts = file.url.split('/').filter((part: string) => part !== '');
      const encodedParts = urlParts.map((part: string) => {
        if (part.includes('://') || part.startsWith('http')) {
          return part;
        }
        return encodeURIComponent(decodeURIComponent(part));
      });
      const encodedUrl = '/' + encodedParts.join('/');
      
      // Create link with download attribute to force download
      const link = document.createElement('a');
      link.href = encodedUrl;
      link.download = file.name;
      link.style.display = 'none';
      link.setAttribute('download', file.name);
      document.body.appendChild(link);
      link.click();
      
      setTimeout(() => {
        if (document.body.contains(link)) {
          document.body.removeChild(link);
        }
      }, 100);
    } catch (fallbackError) {
      console.error('Fallback failed:', fallbackError);
      alert(`خطا در دانلود فایل "${file.name}". لطفاً دوباره تلاش کنید.`);
    }
  }
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
  min-width: 50px;
  flex-shrink: 0;
  text-align: center;
}

.modal-dialog {
  max-height: 90vh;
  max-width: 90vw;
  width: 100%;
  margin: 1.75rem auto;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.modal-content {
  border-radius: var(--radius-lg);
  backdrop-filter: blur(20px);
  max-height: 90vh;
  height: auto;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  position: relative;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
}

.modal-header {
  flex-shrink: 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding: 1rem 1.5rem;
  min-height: 60px;
  box-sizing: border-box;
  width: 100%;
}

.modal-body-scrollable {
  flex: 1 1 auto;
  overflow-y: auto;
  overflow-x: hidden;
  padding: 1.5rem;
  min-height: 0;
  max-height: calc(90vh - 60px);
  position: relative;
  width: 100%;
  box-sizing: border-box;
}

.modal-body-scrollable > div {
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
  word-wrap: break-word;
  overflow-wrap: break-word;
}

.modal-body-scrollable .row {
  margin: 0;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
}

.modal-body-scrollable .col-12 {
  padding-left: 0.75rem;
  padding-right: 0.75rem;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
  min-width: 0;
  flex: 0 0 100%;
}

.modal-body-scrollable::-webkit-scrollbar {
  width: 10px;
}

.modal-body-scrollable::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 5px;
}

.modal-body-scrollable::-webkit-scrollbar-thumb {
  background: rgba(13, 110, 253, 0.6);
  border-radius: 5px;
}

.modal-body-scrollable::-webkit-scrollbar-thumb:hover {
  background: rgba(13, 110, 253, 0.8);
}

.file-item {
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
  margin-bottom: 0.75rem;
  min-width: 0;
}

.file-item:last-child {
  margin-bottom: 0;
}

.file-item-inner {
  transition: var(--transition-snappy);
  border: 1px solid rgba(255, 255, 255, 0.2);
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
  min-width: 0;
  word-wrap: break-word;
  overflow-wrap: break-word;
  overflow: hidden;
  display: flex;
  align-items: center;
}

.file-item-inner h6 {
  word-wrap: break-word;
  overflow-wrap: break-word;
  max-width: 100%;
  min-width: 0;
}

.file-item:hover .file-item-inner {
  border-color: rgba(13, 110, 253, 0.3);
  transform: translateX(5px);
}

.file-info {
  min-width: 0;
  flex: 1 1 auto;
  flex-shrink: 1;
  overflow: hidden;
  max-width: 100%;
}

.file-info h6 {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 100%;
  min-width: 0;
}

.file-item-inner .soft-button {
  flex-shrink: 0;
  min-width: fit-content;
  white-space: nowrap;
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

