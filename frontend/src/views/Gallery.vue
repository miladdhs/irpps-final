<template>
  <div class="bg-background-light text-slate-900 dark:bg-background-dark dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex w-fit items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary">
            <span class="material-symbols-outlined text-[20px]">photo_library</span>
            {{ copy.badge }}
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">{{ copy.title }}</h1>
          <p class="max-w-2xl text-lg text-slate-600 dark:text-slate-400">{{ copy.subtitle }}</p>
        </div>

        <div class="mb-8 flex flex-wrap gap-2">
          <button
            v-for="category in categories"
            :key="category.id"
            @click="selectedCategory = category.id"
            class="rounded-full px-6 py-2 text-sm font-medium transition-all"
            :class="selectedCategory === category.id
              ? 'bg-primary text-white shadow-lg'
              : 'border border-slate-200 bg-white text-slate-600 hover:border-primary/30 dark:border-slate-800 dark:bg-slate-900 dark:text-slate-400'"
          >
            {{ category.name }}
          </button>
        </div>

        <div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
          <div
            v-for="(image, index) in filteredImages"
            :key="image.id"
            class="group relative aspect-[4/3] cursor-pointer overflow-hidden rounded-xl bg-slate-100 dark:bg-slate-800"
            @click="openLightbox(index)"
          >
            <img
              :src="image.url"
              :alt="image.title"
              class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-110"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 transition-opacity group-hover:opacity-100">
              <div class="absolute bottom-0 left-0 right-0 p-4">
                <h3 class="text-lg font-bold text-white">{{ image.title }}</h3>
                <p class="text-sm text-white/80">{{ image.date }}</p>
              </div>
            </div>
            <div class="absolute right-4 top-4 rounded-full bg-white/90 p-2 opacity-0 transition-opacity group-hover:opacity-100">
              <span class="material-symbols-outlined text-primary">zoom_in</span>
            </div>
          </div>
        </div>

        <div v-if="filteredImages.length === 0" class="flex flex-col items-center justify-center py-20">
          <span class="material-symbols-outlined mb-4 text-6xl text-slate-300">photo_library</span>
          <p class="text-slate-500">{{ copy.empty }}</p>
        </div>
      </main>
    </div>

    <div
      v-if="showLightbox"
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/90 p-4"
      @click="closeLightbox"
    >
      <button
        @click="closeLightbox"
        class="absolute right-4 top-4 rounded-full bg-white/10 p-3 text-white hover:bg-white/20"
      >
        <span class="material-symbols-outlined">close</span>
      </button>

      <button
        v-if="currentImageIndex > 0"
        @click.stop="previousImage"
        class="absolute left-4 rounded-full bg-white/10 p-3 text-white hover:bg-white/20"
      >
        <span class="material-symbols-outlined">chevron_left</span>
      </button>

      <button
        v-if="currentImageIndex < filteredImages.length - 1"
        @click.stop="nextImage"
        class="absolute right-4 rounded-full bg-white/10 p-3 text-white hover:bg-white/20"
      >
        <span class="material-symbols-outlined">chevron_right</span>
      </button>

      <div class="max-h-[90vh] max-w-[90vw]" @click.stop>
        <img
          :src="filteredImages[currentImageIndex]?.url"
          :alt="filteredImages[currentImageIndex]?.title"
          class="max-h-[90vh] max-w-full rounded-lg"
        />
        <div class="mt-4 text-center text-white">
          <h3 class="text-xl font-bold">{{ filteredImages[currentImageIndex]?.title }}</h3>
          <p class="text-sm text-white/80">{{ filteredImages[currentImageIndex]?.date }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()

const selectedCategory = ref('all')
const showLightbox = ref(false)
const currentImageIndex = ref(0)

const copy = computed(() => locale.value === 'fa'
  ? {
      badge: 'گالری تصاویر',
      title: 'گالری تصاویر انجمن',
      subtitle: 'تصاویر رویدادها، کنگره‌ها و فعالیت‌های انجمن علمی ریه کودکان ایران',
      empty: 'تصویری در این دسته‌بندی موجود نیست',
      all: 'همه',
      image1: 'فعالیت انجمن',
      image2: 'رویداد علمی',
      image3: 'همایش تخصصی',
      year: '۱۴۰۳',
    }
  : {
      badge: 'Image Gallery',
      title: 'Association Gallery',
      subtitle: 'Images from events, congresses, and activities of the Iranian Pediatric Lung Scientific Association',
      empty: 'No images are available in this category',
      all: 'All',
      image1: 'Association Activity',
      image2: 'Scientific Event',
      image3: 'Specialized Conference',
      year: '2024',
    })

const categories = computed(() => [
  { id: 'all', name: copy.value.all },
])

const images = computed(() => [
  { id: 1, url: '/Content/lAST/IMG_1518.JPG', title: copy.value.image1, date: copy.value.year, category: 'all' },
  { id: 2, url: '/Content/lAST/IMG_1532.JPG', title: copy.value.image2, date: copy.value.year, category: 'all' },
  { id: 3, url: '/Content/lAST/photo_2026-01-04_12-05-58.jpg', title: copy.value.image3, date: copy.value.year, category: 'all' },
])

const filteredImages = computed(() => {
  if (selectedCategory.value === 'all') {
    return images.value
  }
  return images.value.filter((img) => img.category === selectedCategory.value)
})

function openLightbox(index: number) {
  currentImageIndex.value = index
  showLightbox.value = true
  document.body.style.overflow = 'hidden'
}

function closeLightbox() {
  showLightbox.value = false
  document.body.style.overflow = 'auto'
}

function nextImage() {
  if (currentImageIndex.value < filteredImages.value.length - 1) {
    currentImageIndex.value += 1
  }
}

function previousImage() {
  if (currentImageIndex.value > 0) {
    currentImageIndex.value -= 1
  }
}
</script>
