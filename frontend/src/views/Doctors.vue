<template>
  <div class="doctors-view position-relative">
    <section class="page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center">
          <div class="col-md-12 text-center">
            <span class="soft-badge secondary mb-3">
              <i class="fa fa-user-md"></i>
              بخش پزشکان
            </span>
            <h1 class="display-4 fw-bold mb-4">منابع و محتوای پزشکی</h1>
            <p class="lead text-muted">دسترسی به منابع آموزشی، ویدیوها، کتاب‌ها و محتوای علمی</p>
          </div>
        </div>
      </div>
    </section>

    <section class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row g-4">
          <div class="col-md-12">
            <div class="glass-card p-5">
              <h2 class="fw-bold mb-4">دسته‌بندی محتوا</h2>
              <p class="text-muted mb-4">انتخاب دسته‌بندی مورد نظر برای مشاهده و دانلود فایل‌ها</p>
              <div class="row g-4">
                <!-- SkyRoom -->
                <div class="col-lg-4 col-md-6">
                  <div class="category-card glass-card p-4 text-center h-100" @click="handleCategoryClick('skyroom')">
                    <div class="category-icon mb-3">
                      <i class="fa fa-video-camera fa-3x text-primary"></i>
                    </div>
                    <h5 class="fw-bold mb-2">اسکای روم</h5>
                    <p class="text-muted mb-3">لینک‌های جلسات و وبینارهای اسکای روم</p>
                    <button class="soft-button primary btn-sm">
                      <i class="fa fa-external-link me-1"></i>
                      مشاهده
                    </button>
                  </div>
                </div>

                <!-- Video -->
                <div class="col-lg-4 col-md-6">
                  <div class="category-card glass-card p-4 text-center h-100" @click="handleCategoryClick('video')">
                    <div class="category-icon mb-3">
                      <i class="fa fa-film fa-3x text-primary"></i>
                    </div>
                    <h5 class="fw-bold mb-2">ویدیو</h5>
                    <p class="text-muted mb-3">فایل‌های ویدیویی آموزشی</p>
                    <button class="soft-button primary btn-sm">
                      <i class="fa fa-download me-1"></i>
                      مشاهده و دانلود
                    </button>
                  </div>
                </div>

                <!-- Slides -->
                <div class="col-lg-4 col-md-6">
                  <div class="category-card glass-card p-4 text-center h-100" @click="handleCategoryClick('slides')">
                    <div class="category-icon mb-3">
                      <i class="fa fa-file-powerpoint-o fa-3x text-primary"></i>
                    </div>
                    <h5 class="fw-bold mb-2">اسلایدها</h5>
                    <p class="text-muted mb-3">فایل‌های PDF و PowerPoint</p>
                    <button class="soft-button primary btn-sm">
                      <i class="fa fa-download me-1"></i>
                      مشاهده و دانلود
                    </button>
                  </div>
                </div>

                <!-- Books -->
                <div class="col-lg-4 col-md-6">
                  <div class="category-card glass-card p-4 text-center h-100" @click="handleCategoryClick('books')">
                    <div class="category-icon mb-3">
                      <i class="fa fa-book fa-3x text-primary"></i>
                    </div>
                    <h5 class="fw-bold mb-2">کتاب</h5>
                    <p class="text-muted mb-3">کتاب‌های آموزشی با دسته‌بندی موضوعی</p>
                    <button class="soft-button primary btn-sm">
                      <i class="fa fa-download me-1"></i>
                      مشاهده و دانلود
                    </button>
                  </div>
                </div>

                <!-- Broshour -->
                <div class="col-lg-4 col-md-6">
                  <div class="category-card glass-card p-4 text-center h-100" @click="handleCategoryClick('broshour')">
                    <div class="category-icon mb-3">
                      <i class="fa fa-file-image-o fa-3x text-primary"></i>
                    </div>
                    <h5 class="fw-bold mb-2">بروشور</h5>
                    <p class="text-muted mb-3">بروشورها و تصاویر آموزشی</p>
                    <button class="soft-button primary btn-sm">
                      <i class="fa fa-download me-1"></i>
                      مشاهده و دانلود
                    </button>
                  </div>
                </div>

                <!-- Resources -->
                <div class="col-lg-4 col-md-6">
                  <div class="category-card glass-card p-4 text-center h-100" @click="handleCategoryClick('resources')">
                    <div class="category-icon mb-3">
                      <i class="fa fa-folder-open fa-3x text-primary"></i>
                    </div>
                    <h5 class="fw-bold mb-2">منابع و مدارک</h5>
                    <p class="text-muted mb-3">سایر فایل‌های PDF و منابع علمی</p>
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
            <div v-else>
              <!-- Group by folder for books -->
              <template v-if="currentCategory === 'books' && hasFolders">
                <div v-for="(folderFiles, folder) in groupedFiles" :key="folder" class="mb-4">
                  <h6 class="fw-bold mb-3" v-if="folder">
                    <i class="fa fa-folder me-2 text-primary"></i>{{ folder }}
                  </h6>
                  <div class="row g-3">
                    <div v-for="file in folderFiles" :key="file.name" class="col-12">
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
              </template>
              <!-- Regular list for other categories -->
              <template v-else>
                <div class="row g-3">
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
              </template>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { getApiUrl } from '@/utils/api';

const showFilesModal = ref(false);
const currentCategoryTitle = ref('');
const currentCategory = ref('');
const files = ref<any[]>([]);
const loading = ref(false);

const categoryTitles: Record<string, string> = {
  skyroom: 'اسکای روم',
  video: 'ویدیو',
  slides: 'اسلایدها',
  books: 'کتاب',
  broshour: 'بروشور',
  resources: 'منابع و مدارک'
};

const hasFolders = computed(() => {
  return files.value.some((file: any) => file.folder);
});

const groupedFiles = computed(() => {
  if (!hasFolders.value) return { '': files.value };
  
  const grouped: Record<string, any[]> = {};
  files.value.forEach((file: any) => {
    const folder = file.folder || '';
    if (!grouped[folder]) {
      grouped[folder] = [];
    }
    grouped[folder].push(file);
  });
  return grouped;
});

const handleCategoryClick = async (category: string) => {
  currentCategoryTitle.value = categoryTitles[category] || category;
  currentCategory.value = category;
  showFilesModal.value = true;
  loading.value = true;
  files.value = [];
  
  // Handle "Books" from local files
  if (category === 'books') {
    // Load books from local Content/Books directory
    files.value = [
      // تکامل
      {
        name: '152-games-and-exercises-for-childrens-development.pdf',
        url: '/Content/Books/تکامل/152-games-and-exercises-for-childrens-development.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'تکامل'
      },
      {
        name: 'Childrens-development-book.pdf',
        url: '/Content/Books/تکامل/Childrens-development-book.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'تکامل'
      },
      {
        name: 'تقویت-تکامل-در-اوایل-کودکی-.pdf',
        url: '/Content/Books/تکامل/تقویت-تکامل-در-اوایل-کودکی-.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'تکامل'
      },
      {
        name: 'فعالیت-هایی-برای-ارتقای-تکامل-کودک.pdf',
        url: '/Content/Books/تکامل/فعالیت-هایی-برای-ارتقای-تکامل-کودک.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'تکامل'
      },
      {
        name: 'کتاب-تکامل-دوران-ابتدای-کودکی.pdf',
        url: '/Content/Books/تکامل/کتاب-تکامل-دوران-ابتدای-کودکی.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'تکامل'
      },
      // گفتار خانواده
      {
        name: 'khanevade.pdf',
        url: '/Content/Books/گفتار خانواده/khanevade.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'گفتار خانواده'
      },
      // مراقبت های ادغام ناخوشی های اطفال
      {
        name: 'Final-instructions-implementation.pdf',
        url: '/Content/Books/مراقبت های ادغام ناخوشی های اطفال/Final-instructions-implementation.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'مراقبت های ادغام ناخوشی های اطفال'
      },
      {
        name: 'mana-np.pdf',
        url: '/Content/Books/مراقبت های ادغام ناخوشی های اطفال/mana-np.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'مراقبت های ادغام ناخوشی های اطفال'
      },
      {
        name: 'mana-p.pdf',
        url: '/Content/Books/مراقبت های ادغام ناخوشی های اطفال/mana-p.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'مراقبت های ادغام ناخوشی های اطفال'
      },
      // مراقبت های ادغام یافته‌ی کودک سالم
      {
        name: 'booklet-پزشک-کودک-سالم.pdf',
        url: '/Content/Books/مراقبت های ادغام یافته‌ی کودک سالم/booklet-پزشک-کودک-سالم.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'مراقبت های ادغام یافته‌ی کودک سالم'
      },
      {
        name: 'booklet-غیر-پزشک.pdf',
        url: '/Content/Books/مراقبت های ادغام یافته‌ی کودک سالم/booklet-غیر-پزشک.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'مراقبت های ادغام یافته‌ی کودک سالم'
      },
      {
        name: 'counselling-guide-23-12-1400_compressed.pdf',
        url: '/Content/Books/مراقبت های ادغام یافته‌ی کودک سالم/counselling-guide-23-12-1400_compressed.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'مراقبت های ادغام یافته‌ی کودک سالم'
      },
      {
        name: 'non-physician-guide-25-12-1400_compressed.pdf',
        url: '/Content/Books/مراقبت های ادغام یافته‌ی کودک سالم/non-physician-guide-25-12-1400_compressed.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'مراقبت های ادغام یافته‌ی کودک سالم'
      },
      {
        name: 'physician-guide-30-1-1401_compressed.pdf',
        url: '/Content/Books/مراقبت های ادغام یافته‌ی کودک سالم/physician-guide-30-1-1401_compressed.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'مراقبت های ادغام یافته‌ی کودک سالم'
      },
      {
        name: 'rahnamay-jame-koodak.pdf',
        url: '/Content/Books/مراقبت های ادغام یافته‌ی کودک سالم/rahnamay-jame-koodak.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'مراقبت های ادغام یافته‌ی کودک سالم'
      },
      // هیپوتیروئیدی
      {
        name: 'کتاب-بیماری-کم-کاری-تیرویید-99.pdf',
        url: '/Content/Books/هیپوتیروئیدی/کتاب-بیماری-کم-کاری-تیرویید-99.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'هیپوتیروئیدی'
      },
      // واکسیناسیون
      {
        name: 'برنامه-و-راهنمای-ایمن-سازی-1403.pdf',
        url: '/Content/Books/واکسیناسیون/برنامه-و-راهنمای-ایمن-سازی-1403.pdf',
        type: 'application/pdf',
        size: 0,
        folder: 'واکسیناسیون'
      }
    ];
    loading.value = false;
    return;
  }
  
  // Handle other categories from API
  try {
    const response = await fetch(getApiUrl(`/api/doctors/files/?category=${category}`), {
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

const getFileIcon = (fileType: string) => {
  if (fileType.includes('pdf')) return 'fa fa-file-pdf-o';
  if (fileType.includes('video')) return 'fa fa-file-video-o';
  if (fileType.includes('image')) return 'fa fa-file-image-o';
  if (fileType.includes('powerpoint') || fileType.includes('presentation')) return 'fa fa-file-powerpoint-o';
  if (fileType.includes('word')) return 'fa fa-file-word-o';
  return 'fa fa-file-o';
};

const formatFileSize = (bytes: number) => {
  if (!bytes || bytes === 0) return '';
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
.doctors-view {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.category-card {
  transition: var(--transition-snappy);
  cursor: pointer;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.category-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--glass-shadow-hover);
  border-color: rgba(13, 110, 253, 0.3);
}

.category-icon {
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
  .category-card {
    margin-bottom: 1rem;
  }
  
  .modal-dialog {
    margin: 1rem;
  }
}
</style>

