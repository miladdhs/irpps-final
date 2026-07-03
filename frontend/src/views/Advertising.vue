<template>
  <div class="bg-background-light text-slate-900 dark:bg-background-dark dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex w-fit items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary">
            <span class="material-symbols-outlined text-[20px]">campaign</span>
            {{ copy.badge }}
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">{{ copy.title }}</h1>
          <p class="max-w-2xl text-lg text-slate-600 dark:text-slate-400">{{ copy.subtitle }}</p>
        </div>

        <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          <div v-for="option in advertisingOptions" :key="option.title" class="group relative overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br p-8 shadow-sm transition-all hover:shadow-xl dark:border-slate-800 dark:from-slate-900 dark:to-slate-900" :class="option.cardClass">
            <div class="absolute right-0 top-0 h-24 w-24 translate-x-6 -translate-y-6 rounded-full blur-2xl" :class="option.glowClass"></div>
            <div class="relative">
              <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-xl bg-gradient-to-br shadow-lg transition-transform group-hover:scale-110" :class="option.iconClass">
                <span class="material-symbols-outlined text-4xl text-white">{{ option.icon }}</span>
              </div>
              <h3 class="mb-3 text-xl font-black">{{ option.title }}</h3>
              <p class="mb-6 text-sm leading-relaxed text-slate-600 dark:text-slate-400">{{ option.description }}</p>
              <ul class="space-y-2 text-sm">
                <li v-for="feature in option.features" :key="feature" class="flex items-center gap-2 text-slate-600 dark:text-slate-400">
                  <span class="material-symbols-outlined text-[18px]" :class="option.textClass">check_circle</span>
                  <span>{{ feature }}</span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="mt-16 rounded-2xl border border-primary/20 bg-gradient-to-br from-primary/5 to-blue-500/5 p-8 dark:from-primary/10 dark:to-blue-500/10 lg:p-12">
          <div class="flex flex-col items-center gap-8 text-center lg:flex-row lg:text-right">
            <div class="flex h-20 w-20 shrink-0 items-center justify-center rounded-2xl bg-gradient-to-br from-primary to-blue-600 text-white shadow-lg shadow-primary/30">
              <span class="material-symbols-outlined text-5xl">contact_phone</span>
            </div>
            <div class="flex-1">
              <h3 class="mb-3 text-2xl font-black">{{ copy.contactTitle }}</h3>
              <p class="mb-6 text-slate-600 dark:text-slate-400">{{ copy.contactDescription }}</p>
              <div class="flex flex-col gap-4 sm:flex-row sm:justify-center lg:justify-start">
                <router-link to="/contact" class="flex items-center justify-center gap-2 rounded-xl bg-primary px-8 py-4 font-bold text-white shadow-lg shadow-primary/30 transition-all hover:bg-primary/90 hover:shadow-xl">
                  <span class="material-symbols-outlined">mail</span>
                  <span>{{ copy.contactAction }}</span>
                </router-link>
                <a href="tel:09013684856" class="flex items-center justify-center gap-2 rounded-xl border-2 border-primary bg-white px-8 py-4 font-bold text-primary transition-all hover:bg-primary/5 dark:bg-slate-900">
                  <span class="material-symbols-outlined">call</span>
                  <span>09013684856</span>
                </a>
              </div>
            </div>
          </div>
        </div>

        <div class="mt-16 grid grid-cols-2 gap-6 md:grid-cols-4">
          <div v-for="stat in copy.stats" :key="stat.label" class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm transition-all hover:shadow-lg dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">{{ stat.icon }}</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">{{ stat.value }}</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">{{ stat.label }}</div>
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
      badge: 'تبلیغات',
      title: 'فرصت‌های تبلیغاتی',
      subtitle: 'فرصت‌های تبلیغاتی و همکاری با انجمن علمی ریه کودکان ایران',
      contactTitle: 'برای اطلاعات بیشتر با ما تماس بگیرید',
      contactDescription: 'تیم ما آماده است تا بهترین پکیج تبلیغاتی را متناسب با نیاز شما طراحی کند.',
      contactAction: 'تماس با ما',
      options: [
        { icon: 'web', title: 'تبلیغات در وب‌سایت', description: 'نمایش تبلیغات شما در صفحات مختلف وب‌سایت انجمن با بازدید بالا', features: ['بازدید ماهانه بالا', 'مخاطبان تخصصی', 'موقعیت‌های متنوع'] },
        { icon: 'event', title: 'تبلیغات در کنگره‌ها', description: 'حضور برند شما در کنگره‌ها و همایش‌های علمی انجمن', features: ['غرفه نمایشگاهی', 'بنر و پوستر', 'اسپانسرشیپ'] },
        { icon: 'article', title: 'تبلیغات در انتشارات', description: 'درج تبلیغات در مجلات، خبرنامه‌ها و کتابچه‌های انجمن', features: ['مجله علمی', 'خبرنامه', 'کتابچه کنگره'] },
        { icon: 'mail', title: 'ایمیل مارکتینگ', description: 'ارسال پیام تبلیغاتی به اعضای انجمن از طریق ایمیل', features: ['دسترسی مستقیم', 'مخاطبان هدفمند', 'گزارش عملکرد'] },
        { icon: 'share', title: 'شبکه‌های اجتماعی', description: 'تبلیغات در کانال‌ها و صفحات اجتماعی انجمن', features: ['پست‌های تبلیغاتی', 'استوری', 'دسترسی گسترده'] },
        { icon: 'package', title: 'پکیج‌های سفارشی', description: 'طراحی پکیج تبلیغاتی متناسب با نیاز شما', features: ['ترکیب روش‌ها', 'قیمت ویژه', 'مشاوره رایگان'] },
      ],
      stats: [
        { icon: 'visibility', value: '10K+', label: 'بازدید ماهانه' },
        { icon: 'groups', value: '500+', label: 'عضو فعال' },
        { icon: 'event', value: '20+', label: 'رویداد سالانه' },
        { icon: 'trending_up', value: '95%', label: 'رضایت مشتریان' },
      ],
    }
  : {
      badge: 'Advertising',
      title: 'Advertising Opportunities',
      subtitle: 'Advertising and partnership opportunities with the Iranian Pediatric Lung Scientific Association',
      contactTitle: 'Contact Us for More Information',
      contactDescription: 'Our team is ready to design the best advertising package based on your needs.',
      contactAction: 'Contact Us',
      options: [
        { icon: 'web', title: 'Website Advertising', description: 'Display your advertising across high-traffic pages of the association website', features: ['High monthly traffic', 'Specialized audience', 'Multiple placements'] },
        { icon: 'event', title: 'Congress Advertising', description: 'Present your brand at association congresses and scientific meetings', features: ['Exhibition booth', 'Banners and posters', 'Sponsorship'] },
        { icon: 'article', title: 'Publication Advertising', description: 'Place advertisements in association journals, newsletters, and booklets', features: ['Scientific journal', 'Newsletter', 'Congress booklet'] },
        { icon: 'mail', title: 'Email Marketing', description: 'Send targeted promotional messages to association members by email', features: ['Direct reach', 'Targeted audience', 'Performance reports'] },
        { icon: 'share', title: 'Social Media', description: 'Advertise through the association social media channels and pages', features: ['Sponsored posts', 'Stories', 'Wide reach'] },
        { icon: 'package', title: 'Custom Packages', description: 'Create a custom advertising package tailored to your goals', features: ['Combined channels', 'Special pricing', 'Free consultation'] },
      ],
      stats: [
        { icon: 'visibility', value: '10K+', label: 'Monthly Visits' },
        { icon: 'groups', value: '500+', label: 'Active Members' },
        { icon: 'event', value: '20+', label: 'Annual Events' },
        { icon: 'trending_up', value: '95%', label: 'Client Satisfaction' },
      ],
    }))

const palette = [
  ['from-blue-50 to-white hover:border-blue-300', 'bg-blue-500/5', 'from-blue-500 to-blue-600 shadow-blue-500/20', 'text-blue-600'],
  ['from-emerald-50 to-white hover:border-emerald-300', 'bg-emerald-500/5', 'from-emerald-500 to-green-600 shadow-emerald-500/20', 'text-emerald-600'],
  ['from-purple-50 to-white hover:border-purple-300', 'bg-purple-500/5', 'from-purple-500 to-purple-600 shadow-purple-500/20', 'text-purple-600'],
  ['from-orange-50 to-white hover:border-orange-300', 'bg-orange-500/5', 'from-orange-500 to-orange-600 shadow-orange-500/20', 'text-orange-600'],
  ['from-pink-50 to-white hover:border-pink-300', 'bg-pink-500/5', 'from-pink-500 to-pink-600 shadow-pink-500/20', 'text-pink-600'],
  ['from-amber-50 to-white hover:border-amber-300', 'bg-amber-500/5', 'from-amber-500 to-amber-600 shadow-amber-500/20', 'text-amber-600'],
]

const advertisingOptions = computed(() => copy.value.options.map((item, index) => ({
  ...item,
  cardClass: palette[index][0],
  glowClass: palette[index][1],
  iconClass: palette[index][2],
  textClass: palette[index][3],
})))
</script>
