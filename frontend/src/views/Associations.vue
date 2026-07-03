<template>
  <div class="bg-background-light text-slate-900 dark:bg-background-dark dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex w-fit items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary">
            <span class="material-symbols-outlined text-[20px]">public</span>
            {{ copy.badge }}
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">{{ copy.title }}</h1>
          <p class="max-w-2xl text-lg text-slate-600 dark:text-slate-400">{{ copy.subtitle }}</p>
        </div>

        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
          <a v-for="association in associations" :key="association.href" :href="association.href" target="_blank" rel="noreferrer" class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br p-8 shadow-sm transition-all hover:shadow-2xl dark:border-slate-800 dark:from-slate-900 dark:to-slate-900" :class="association.cardClass">
            <div class="absolute right-0 top-0 h-32 w-32 translate-x-8 -translate-y-8 rounded-full blur-3xl transition-all group-hover:scale-150" :class="association.glowClass"></div>
            <div class="relative">
              <div class="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br shadow-lg transition-transform group-hover:scale-110" :class="association.iconClass">
                <span class="material-symbols-outlined text-5xl text-white">{{ association.icon }}</span>
              </div>
              <h2 class="mb-3 text-2xl font-black">{{ association.name }}</h2>
              <p class="mb-2 text-sm font-medium" :class="association.textClass">{{ association.shortTitle }}</p>
              <p class="mb-6 leading-relaxed text-slate-600 dark:text-slate-400">{{ association.description }}</p>
              <div class="mb-6 flex flex-wrap gap-2">
                <span v-for="tag in association.tags" :key="tag" class="rounded-full px-3 py-1 text-xs font-bold" :class="association.tagClass">{{ tag }}</span>
              </div>
              <div class="flex items-center gap-2 font-bold transition-all group-hover:gap-3" :class="association.textClass">
                <span>{{ copy.visitWebsite }}</span>
                <span class="material-symbols-outlined text-[20px]">open_in_new</span>
              </div>
            </div>
          </a>
        </div>

        <div class="mt-16 rounded-2xl border border-primary/20 bg-gradient-to-br from-primary/5 to-blue-500/5 p-8 dark:from-primary/10 dark:to-blue-500/10 lg:p-12">
          <div class="flex flex-col items-center gap-8 text-center">
            <div class="flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-primary to-blue-600 text-white shadow-lg shadow-primary/30">
              <span class="material-symbols-outlined text-5xl">handshake</span>
            </div>
            <div>
              <h3 class="mb-3 text-2xl font-black">{{ copy.ctaTitle }}</h3>
              <p class="mx-auto max-w-2xl text-slate-600 dark:text-slate-400">{{ copy.ctaDescription }}</p>
            </div>
            <div class="flex flex-wrap justify-center gap-4">
              <div v-for="item in copy.ctaItems" :key="item" class="flex items-center gap-2 rounded-lg bg-white px-4 py-2 dark:bg-slate-900">
                <span class="material-symbols-outlined text-primary">check_circle</span>
                <span class="text-sm font-medium">{{ item }}</span>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()

const copy = computed(() => (locale.value === 'fa'
  ? {
      badge: 'انجمن‌های مرتبط',
      title: 'انجمن‌های وابسته و مرتبط',
      subtitle: 'انجمن‌های ملی و بین‌المللی مرتبط با ریه کودکان و پزشکی اطفال',
      visitWebsite: 'بازدید از وب‌سایت',
      ctaTitle: 'همکاری با انجمن‌های بین‌المللی',
      ctaDescription: 'انجمن علمی ریه کودکان ایران با همکاری نزدیک با انجمن‌های معتبر بین‌المللی، به تبادل دانش و تجربیات علمی می‌پردازد.',
      ctaItems: ['تبادل دانش', 'کنگره‌های مشترک', 'انتشارات علمی'],
      list: [
        { href: 'https://chestnet.ir/fa', icon: 'pulmonology', name: 'انجمن ریه ایران', shortTitle: 'مرجع تخصصی بیماری‌های ریوی در ایران', description: 'انجمن علمی ریه ایران به عنوان مرجع تخصصی بیماری‌های ریوی، فعالیت‌های گسترده‌ای در زمینه آموزش، پژوهش و ارتقای سطح دانش پزشکان انجام می‌دهد.', tags: ['آموزش', 'پژوهش', 'کنگره'] },
        { href: 'https://www.ersnet.org/', icon: 'public', name: 'European Respiratory Society', shortTitle: 'انجمن تنفسی اروپا', description: 'انجمن تنفسی اروپا یکی از بزرگترین و معتبرترین انجمن‌های بین‌المللی در زمینه بیماری‌های تنفسی است که با برگزاری کنگره‌های سالانه و انتشار مجلات علمی، نقش مهمی در پیشرفت این حوزه دارد.', tags: ['بین‌المللی', 'مجلات ISI', 'کنگره سالانه'] },
        { href: 'https://www.thoracic.org/', icon: 'medical_services', name: 'American Thoracic Society', shortTitle: 'انجمن قفسه سینه آمریکا', description: 'انجمن قفسه سینه آمریکا با بیش از 100 سال سابقه، پیشرو در تحقیقات و آموزش بیماری‌های ریوی، قلبی-ریوی و مراقبت‌های ویژه است و راهنماهای بالینی معتبری را منتشر می‌کند.', tags: ['100+ سال سابقه', 'راهنماهای بالینی', 'تحقیقات'] },
        { href: 'https://irpediatrics.com/', icon: 'child_care', name: 'انجمن پزشکان کودکان ایران', shortTitle: 'مرجع تخصصی اطفال در ایران', description: 'انجمن علمی پزشکان کودکان ایران با هدف ارتقای سطح علمی و حرفه‌ای پزشکان اطفال، برگزاری کنگره‌ها، کارگاه‌ها و انتشار مجلات علمی، نقش مهمی در سلامت کودکان کشور ایفا می‌کند.', tags: ['اطفال', 'کنگره', 'مجله علمی'] },
      ],
    }
  : {
      badge: 'Related Associations',
      title: 'Affiliated and Related Associations',
      subtitle: 'National and international associations related to pediatric pulmonology and child health',
      visitWebsite: 'Visit Website',
      ctaTitle: 'Collaboration with International Associations',
      ctaDescription: 'The Iranian Pediatric Lung Scientific Association works closely with reputable international associations to exchange scientific knowledge and experience.',
      ctaItems: ['Knowledge exchange', 'Joint congresses', 'Scientific publications'],
      list: [
        { href: 'https://chestnet.ir/fa', icon: 'pulmonology', name: 'Iranian Chest Society', shortTitle: 'Specialized reference for pulmonary diseases in Iran', description: 'The Iranian Chest Society serves as a leading professional reference in pulmonary medicine, with broad activities in education, research, and physician development.', tags: ['Education', 'Research', 'Congress'] },
        { href: 'https://www.ersnet.org/', icon: 'public', name: 'European Respiratory Society', shortTitle: 'Leading respiratory association in Europe', description: 'The European Respiratory Society is one of the largest and most respected international respiratory organizations, advancing the field through annual congresses and scientific journals.', tags: ['International', 'ISI Journals', 'Annual Congress'] },
        { href: 'https://www.thoracic.org/', icon: 'medical_services', name: 'American Thoracic Society', shortTitle: 'A major authority in thoracic and pulmonary medicine', description: 'With more than 100 years of history, the American Thoracic Society leads research and education in pulmonary, cardiopulmonary, and critical care medicine and publishes trusted clinical guidelines.', tags: ['100+ Years', 'Clinical Guidelines', 'Research'] },
        { href: 'https://irpediatrics.com/', icon: 'child_care', name: 'Iranian Pediatric Society', shortTitle: 'Specialized pediatric reference in Iran', description: 'The Iranian Pediatric Society promotes scientific and professional growth among pediatricians through congresses, workshops, journals, and educational programs.', tags: ['Pediatrics', 'Congress', 'Scientific Journal'] },
      ],
    }))

const palette = [
  { cardClass: 'from-blue-50 to-white hover:border-blue-300', glowClass: 'bg-blue-500/5', iconClass: 'from-blue-500 to-blue-600 shadow-blue-500/30', textClass: 'text-blue-600', tagClass: 'bg-blue-500/10 text-blue-600' },
  { cardClass: 'from-purple-50 to-white hover:border-purple-300', glowClass: 'bg-purple-500/5', iconClass: 'from-purple-500 to-purple-600 shadow-purple-500/30', textClass: 'text-purple-600', tagClass: 'bg-purple-500/10 text-purple-600' },
  { cardClass: 'from-red-50 to-white hover:border-red-300', glowClass: 'bg-red-500/5', iconClass: 'from-red-500 to-red-600 shadow-red-500/30', textClass: 'text-red-600', tagClass: 'bg-red-500/10 text-red-600' },
  { cardClass: 'from-emerald-50 to-white hover:border-emerald-300', glowClass: 'bg-emerald-500/5', iconClass: 'from-emerald-500 to-green-600 shadow-emerald-500/30', textClass: 'text-emerald-600', tagClass: 'bg-emerald-500/10 text-emerald-600' },
]

const associations = computed(() => copy.value.list.map((item, index) => ({ ...item, ...palette[index] })))
</script>
