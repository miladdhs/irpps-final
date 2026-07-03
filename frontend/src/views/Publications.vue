<template>
  <div class="bg-background-light text-slate-900 dark:bg-background-dark dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex w-fit items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary">
            <span class="material-symbols-outlined text-[20px]">article</span>
            {{ copy.badge }}
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">{{ copy.title }}</h1>
          <p class="max-w-2xl text-lg text-slate-600 dark:text-slate-400">{{ copy.subtitle }}</p>
        </div>

        <div class="grid grid-cols-1 gap-6 lg:grid-cols-2">
          <div class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-blue-50 to-white p-8 shadow-sm transition-all hover:border-blue-300 hover:shadow-2xl dark:border-slate-800 dark:from-slate-900 dark:to-slate-900">
            <div class="absolute right-0 top-0 h-32 w-32 translate-x-8 -translate-y-8 rounded-full bg-blue-500/5 blur-3xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-blue-500 to-blue-600 shadow-lg shadow-blue-500/30 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-5xl text-white">newspaper</span>
              </div>
              <h3 class="mb-3 text-2xl font-black">{{ copy.newslettersTitle }}</h3>
              <p class="mb-6 text-slate-600 dark:text-slate-400">{{ copy.newslettersDesc }}</p>
              <div class="mb-6 flex flex-wrap gap-2">
                <span class="rounded-full bg-blue-500/10 px-3 py-1 text-xs font-bold text-blue-600">{{ copy.newslettersTag1 }}</span>
                <span class="rounded-full bg-blue-500/10 px-3 py-1 text-xs font-bold text-blue-600">{{ copy.newslettersTag2 }}</span>
                <span class="rounded-full bg-blue-500/10 px-3 py-1 text-xs font-bold text-blue-600">{{ copy.newslettersTag3 }}</span>
              </div>
              <div class="inline-flex items-center gap-2 rounded-full bg-amber-500/10 px-4 py-2 text-sm font-bold text-amber-600">
                <span class="material-symbols-outlined text-[18px]">schedule</span>
                {{ copy.comingSoon }}
              </div>
            </div>
          </div>

          <div
            @click="openModal('congress')"
            class="group relative cursor-pointer overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-emerald-50 to-white p-8 shadow-sm transition-all hover:border-emerald-300 hover:shadow-2xl dark:border-slate-800 dark:from-slate-900 dark:to-slate-900"
          >
            <div class="absolute right-0 top-0 h-32 w-32 translate-x-8 -translate-y-8 rounded-full bg-emerald-500/5 blur-3xl transition-all group-hover:scale-150"></div>
            <div class="relative">
              <div class="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-emerald-500 to-green-600 shadow-lg shadow-emerald-500/30 transition-transform group-hover:scale-110">
                <span class="material-symbols-outlined text-5xl text-white">book</span>
              </div>
              <h3 class="mb-3 text-2xl font-black">{{ copy.congressTitle }}</h3>
              <p class="mb-6 text-slate-600 dark:text-slate-400">{{ copy.congressDesc }}</p>
              <div class="mb-6 flex flex-wrap gap-2">
                <span class="rounded-full bg-emerald-500/10 px-3 py-1 text-xs font-bold text-emerald-600">{{ copy.congressTag1 }}</span>
                <span class="rounded-full bg-emerald-500/10 px-3 py-1 text-xs font-bold text-emerald-600">PDF</span>
                <span class="rounded-full bg-emerald-500/10 px-3 py-1 text-xs font-bold text-emerald-600">{{ copy.congressTag3 }}</span>
              </div>
              <div class="flex items-center gap-2 font-bold text-emerald-600 transition-all group-hover:gap-3">
                <span>{{ copy.congressAction }}</span>
                <span class="material-symbols-outlined">download</span>
              </div>
            </div>
          </div>
        </div>

        <div class="mt-8">
          <div class="group rounded-2xl border border-slate-200 bg-gradient-to-br from-pink-50 to-white p-8 shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:from-slate-900 dark:to-slate-900">
            <div class="flex flex-col gap-6 md:flex-row md:items-center">
              <div class="flex h-20 w-20 shrink-0 items-center justify-center rounded-2xl bg-gradient-to-br from-pink-500 to-pink-600 shadow-lg shadow-pink-500/30">
                <span class="material-symbols-outlined text-5xl text-white">science</span>
              </div>
              <div class="flex-1">
                <h3 class="mb-2 text-2xl font-black">{{ copy.researchTitle }}</h3>
                <p class="mb-4 text-slate-600 dark:text-slate-400">{{ copy.researchDesc }}</p>
                <div class="flex flex-wrap gap-2">
                  <span class="rounded-full bg-pink-500/10 px-3 py-1 text-xs font-bold text-pink-600">{{ copy.researchTag1 }}</span>
                  <span class="rounded-full bg-pink-500/10 px-3 py-1 text-xs font-bold text-pink-600">{{ copy.researchTag2 }}</span>
                  <span class="rounded-full bg-pink-500/10 px-3 py-1 text-xs font-bold text-pink-600">{{ copy.researchTag3 }}</span>
                </div>
              </div>
              <div class="inline-flex items-center gap-2 rounded-full bg-amber-500/10 px-4 py-2 text-sm font-bold text-amber-600">
                <span class="material-symbols-outlined text-[18px]">schedule</span>
                {{ copy.comingSoon }}
              </div>
            </div>
          </div>
        </div>

        <div class="mt-16 grid grid-cols-2 gap-6 md:grid-cols-4">
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">article</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">100+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">{{ copy.stat1 }}</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">book</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">15+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">{{ copy.stat2 }}</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">event</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">9</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">{{ copy.stat3 }}</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">groups</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">500+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">{{ copy.stat4 }}</div>
          </div>
        </div>
      </main>
    </div>

    <div
      v-if="showModal"
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4"
      @click.self="closeModal"
    >
      <div class="max-h-[80vh] w-full max-w-2xl overflow-y-auto rounded-2xl border border-slate-200 bg-white shadow-2xl dark:border-slate-800 dark:bg-slate-900">
        <div class="sticky top-0 flex items-center justify-between border-b border-slate-200 bg-white p-6 dark:border-slate-800 dark:bg-slate-900">
          <h2 class="text-2xl font-black">{{ modalTitle }}</h2>
          <button @click="closeModal" class="rounded-lg p-2 transition-colors hover:bg-slate-100 dark:hover:bg-slate-800">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>
        <div class="p-6">
          <div class="flex flex-col gap-3">
            <a
              v-for="file in modalFiles"
              :key="file.path"
              :href="file.path"
              target="_blank"
              class="group flex items-center justify-between rounded-xl border border-slate-200 p-4 transition-all hover:border-primary/30 hover:bg-slate-50 hover:shadow-md dark:border-slate-800 dark:hover:bg-slate-800"
            >
              <div class="flex items-center gap-4">
                <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary/10">
                  <span class="material-symbols-outlined text-2xl text-primary">picture_as_pdf</span>
                </div>
                <div>
                  <div class="font-bold transition-colors group-hover:text-primary">{{ file.name }}</div>
                  <div class="text-sm text-slate-500">{{ file.size }}</div>
                </div>
              </div>
              <span class="material-symbols-outlined text-slate-400 transition-colors group-hover:text-primary">download</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()

const showModal = ref(false)
const modalType = ref('')

const copy = computed(() => locale.value === 'fa'
  ? {
      badge: 'انتشارات',
      title: 'انتشارات علمی',
      subtitle: 'مجلات، کتاب‌ها و مقالات علمی منتشر شده توسط انجمن',
      newslettersTitle: 'خبرنامه‌ها',
      newslettersDesc: 'خبرنامه‌های سالانه انجمن با آخرین اخبار و دستاوردهای علمی',
      newslettersTag1: 'سالانه',
      newslettersTag2: 'اخبار علمی',
      newslettersTag3: 'دستاوردها',
      comingSoon: 'به زودی',
      congressTitle: 'کتابچه کنگره‌ها و همایش‌ها',
      congressDesc: 'کتابچه‌های کنگره‌ها و همایش‌های علمی با خلاصه مقالات',
      congressTag1: '3 فایل',
      congressTag3: 'دانلود رایگان',
      congressAction: 'مشاهده و دانلود',
      researchTitle: 'تحقیقات و پژوهش',
      researchDesc: 'مقالات و تحقیقات علمی اعضای انجمن در مجلات معتبر داخلی و بین‌المللی',
      researchTag1: 'مقالات ISI',
      researchTag2: 'پایان‌نامه‌ها',
      researchTag3: 'پروژه‌های تحقیقاتی',
      stat1: 'مقاله منتشر شده',
      stat2: 'کتاب منتشر شده',
      stat3: 'کنگره برگزار شده',
      stat4: 'محقق و نویسنده',
      modalTitle: 'کتابچه کنگره‌ها و همایش‌ها',
      file1: 'کتابچه کنگره',
      file2: 'خلاصه مقالات پنجمین همایش 1403',
      file3: 'سند علمی',
    }
  : {
      badge: 'Publications',
      title: 'Scientific Publications',
      subtitle: 'Journals, books, and scientific articles published by the association',
      newslettersTitle: 'Newsletters',
      newslettersDesc: 'Annual newsletters featuring the latest scientific news and achievements of the association',
      newslettersTag1: 'Annual',
      newslettersTag2: 'Scientific News',
      newslettersTag3: 'Achievements',
      comingSoon: 'Coming Soon',
      congressTitle: 'Congress and Conference Booklets',
      congressDesc: 'Scientific congress and conference booklets containing paper abstracts',
      congressTag1: '3 Files',
      congressTag3: 'Free Download',
      congressAction: 'View and Download',
      researchTitle: 'Research and Studies',
      researchDesc: 'Scientific papers and research by association members in reputable domestic and international journals',
      researchTag1: 'ISI Articles',
      researchTag2: 'Theses',
      researchTag3: 'Research Projects',
      stat1: 'Published Articles',
      stat2: 'Published Books',
      stat3: 'Held Congresses',
      stat4: 'Researchers and Authors',
      modalTitle: 'Congress and Conference Booklets',
      file1: 'Congress Booklet',
      file2: 'Abstracts of the Fifth Conference 2024',
      file3: 'Scientific Document',
    })

const files = computed(() => ({
  congress: [
    { name: copy.value.file1, path: '/Content/Other/1_23033290624.pdf', size: '5.2 MB' },
    { name: copy.value.file2, path: '/Content/Other/خلاصه مقالات 5 همایش 403.pdf', size: '3.7 MB' },
    { name: copy.value.file3, path: '/Content/Other/DOC-20251227-WA0007.pdf', size: '1.2 MB' },
  ],
}))

const modalTitle = computed(() => {
  if (modalType.value === 'congress') {
    return copy.value.modalTitle
  }
  return ''
})

const modalFiles = computed(() => files.value[modalType.value as keyof typeof files.value] || [])

function openModal(type: string) {
  modalType.value = type
  showModal.value = true
  document.body.style.overflow = 'hidden'
}

function closeModal() {
  showModal.value = false
  document.body.style.overflow = 'auto'
}
</script>
