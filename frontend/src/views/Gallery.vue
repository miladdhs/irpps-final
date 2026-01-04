<template>
  <div class="gallery-view position-relative">
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
              <div class="row g-4">
                <div 
                  class="col-lg-4 col-md-6" 
                  v-for="(image, index) in galleryImages" 
                  :key="index"
                  @click="openLightbox(index)"
                >
                  <div class="gallery-item glass-card overflow-hidden">
                    <img 
                      :src="image.url" 
                      :alt="image.alt"
                      class="gallery-image"
                      loading="lazy"
                    />
                    <div class="gallery-overlay">
                      <i class="fa fa-search-plus fa-2x"></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Lightbox Modal -->
    <div 
      v-if="lightboxOpen" 
      class="lightbox-modal" 
      @click="closeLightbox"
    >
      <div class="lightbox-content" @click.stop>
        <button class="lightbox-close" @click="closeLightbox">
          <i class="fa fa-times"></i>
        </button>
        <button 
          class="lightbox-nav lightbox-prev" 
          @click="previousImage"
          v-if="galleryImages.length > 1"
        >
          <i class="fa fa-chevron-right"></i>
        </button>
        <button 
          class="lightbox-nav lightbox-next" 
          @click="nextImage"
          v-if="galleryImages.length > 1"
        >
          <i class="fa fa-chevron-left"></i>
        </button>
        <img 
          :src="galleryImages[currentImageIndex].url" 
          :alt="galleryImages[currentImageIndex].alt"
          class="lightbox-image"
        />
        <div class="lightbox-counter" v-if="galleryImages.length > 1">
          {{ currentImageIndex + 1 }} / {{ galleryImages.length }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';

const galleryImages = ref([
  {
    url: '/Content/lAST/photo_2026-01-04_12-05-58.jpg',
    alt: 'فعالیت‌های انجمن علمی ریه کودکان ایران'
  },
  {
    url: '/Content/lAST/IMG_1518.JPG',
    alt: 'همایش‌ها و کنگره‌های انجمن'
  },
  {
    url: '/Content/lAST/IMG_1532.JPG',
    alt: 'کارگاه‌های آموزشی انجمن'
  }
]);

const lightboxOpen = ref(false);
const currentImageIndex = ref(0);

const openLightbox = (index: number) => {
  currentImageIndex.value = index;
  lightboxOpen.value = true;
  document.body.style.overflow = 'hidden';
};

const closeLightbox = () => {
  lightboxOpen.value = false;
  document.body.style.overflow = '';
};

const nextImage = () => {
  currentImageIndex.value = (currentImageIndex.value + 1) % galleryImages.value.length;
};

const previousImage = () => {
  currentImageIndex.value = (currentImageIndex.value - 1 + galleryImages.value.length) % galleryImages.value.length;
};

const handleKeyPress = (e: KeyboardEvent) => {
  if (!lightboxOpen.value) return;
  
  if (e.key === 'Escape') {
    closeLightbox();
  } else if (e.key === 'ArrowRight') {
    nextImage();
  } else if (e.key === 'ArrowLeft') {
    previousImage();
  }
};

onMounted(() => {
  window.scrollTo(0, 0);
  window.addEventListener('keydown', handleKeyPress);
});

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeyPress);
  document.body.style.overflow = '';
});
</script>

<style scoped>
.gallery-view {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.gallery-item {
  position: relative;
  cursor: pointer;
  border-radius: 16px;
  overflow: hidden;
  aspect-ratio: 4/3;
  transition: var(--transition-snappy);
}

.gallery-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.gallery-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.gallery-item:hover .gallery-image {
  transform: scale(1.05);
}

.gallery-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  color: white;
}

.gallery-item:hover .gallery-overlay {
  opacity: 1;
}

/* Lightbox Styles */
.lightbox-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.95);
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.lightbox-content {
  position: relative;
  max-width: 90vw;
  max-height: 90vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.lightbox-image {
  max-width: 100%;
  max-height: 90vh;
  object-fit: contain;
  border-radius: 8px;
}

.lightbox-close {
  position: absolute;
  top: -50px;
  right: 0;
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 1.2rem;
  transition: background 0.3s ease;
}

.lightbox-close:hover {
  background: rgba(255, 255, 255, 0.3);
}

.lightbox-nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 1.5rem;
  transition: background 0.3s ease;
}

.lightbox-nav:hover {
  background: rgba(255, 255, 255, 0.3);
}

.lightbox-prev {
  right: calc(100% + 20px);
}

.lightbox-next {
  left: calc(100% + 20px);
}

.lightbox-counter {
  position: absolute;
  bottom: -50px;
  left: 50%;
  transform: translateX(-50%);
  color: white;
  font-size: 1rem;
  background: rgba(0, 0, 0, 0.5);
  padding: 0.5rem 1rem;
  border-radius: 20px;
}

@media (max-width: 768px) {
  .lightbox-nav {
    width: 40px;
    height: 40px;
    font-size: 1.2rem;
  }
  
  .lightbox-prev {
    right: calc(100% + 10px);
  }
  
  .lightbox-next {
    left: calc(100% + 10px);
  }
  
  .lightbox-close {
    top: -40px;
  }
}
</style>

