<template>
  <div class="bg-background-light text-slate-900 dark:bg-background-dark dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex w-fit items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary">
            <span class="material-symbols-outlined text-[20px]">help</span>
            {{ copy.badge }}
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">{{ copy.title }}</h1>
          <p class="max-w-2xl text-lg text-slate-600 dark:text-slate-400">{{ copy.subtitle }}</p>
        </div>

        <div class="grid grid-cols-1 gap-8">
          <section class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-6 flex items-center gap-3">
              <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-blue-500/10">
                <span class="material-symbols-outlined text-2xl text-blue-600">rocket_launch</span>
              </div>
              <h2 class="text-2xl font-bold">{{ copy.gettingStartedTitle }}</h2>
            </div>
            <div class="prose prose-slate max-w-none dark:prose-invert">
              <p class="leading-relaxed">{{ copy.gettingStartedText }}</p>
              <ul class="space-y-2">
                <li v-for="item in copy.gettingStartedItems" :key="item">{{ item }}</li>
              </ul>
            </div>
          </section>

          <section class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-6 flex items-center gap-3">
              <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-emerald-500/10">
                <span class="material-symbols-outlined text-2xl text-emerald-600">dashboard</span>
              </div>
              <h2 class="text-2xl font-bold">{{ copy.sectionsTitle }}</h2>
            </div>
            <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
              <div v-for="section in copy.sections" :key="section.title" class="rounded-lg border border-slate-200 p-4 dark:border-slate-800">
                <div class="mb-2 flex items-center gap-2">
                  <span class="material-symbols-outlined text-primary">{{ section.icon }}</span>
                  <h3 class="font-bold">{{ section.title }}</h3>
                </div>
                <p class="text-sm text-slate-600 dark:text-slate-400">{{ section.description }}</p>
              </div>
            </div>
          </section>

          <section class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-6 flex items-center gap-3">
              <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-purple-500/10">
                <span class="material-symbols-outlined text-2xl text-purple-600">person_add</span>
              </div>
              <h2 class="text-2xl font-bold">{{ copy.registerTitle }}</h2>
            </div>
            <div class="prose prose-slate max-w-none dark:prose-invert">
              <p class="mb-4 leading-relaxed">{{ copy.registerText }}</p>
              <ol class="space-y-3">
                <li v-for="item in copy.registerItems" :key="item">{{ item }}</li>
              </ol>
            </div>
          </section>

          <section class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-6 flex items-center gap-3">
              <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-orange-500/10">
                <span class="material-symbols-outlined text-2xl text-orange-600">download</span>
              </div>
              <h2 class="text-2xl font-bold">{{ copy.downloadTitle }}</h2>
            </div>
            <div class="prose prose-slate max-w-none dark:prose-invert">
              <p class="mb-4 leading-relaxed">{{ copy.downloadText }}</p>
              <ul class="space-y-2">
                <li v-for="item in copy.downloadItems" :key="item">{{ item }}</li>
              </ul>
            </div>
          </section>

          <section class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-6 flex items-center gap-3">
              <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-red-500/10">
                <span class="material-symbols-outlined text-2xl text-red-600">support_agent</span>
              </div>
              <h2 class="text-2xl font-bold">{{ copy.supportTitle }}</h2>
            </div>
            <div class="prose prose-slate max-w-none dark:prose-invert">
              <p class="mb-4 leading-relaxed">{{ copy.supportText }}</p>
              <ul class="space-y-2">
                <li v-for="item in copy.supportItems" :key="item">{{ item }}</li>
              </ul>
            </div>
          </section>
        </div>

        <section class="mt-16 rounded-xl border border-primary/20 bg-primary/5 p-8 dark:bg-primary/10">
          <div class="mb-6 text-center">
            <h2 class="mb-2 text-2xl font-bold">{{ copy.faqTitle }}</h2>
            <p class="text-slate-600 dark:text-slate-400">{{ copy.faqSubtitle }}</p>
          </div>
          <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
            <div v-for="faq in copy.faqs" :key="faq.question" class="rounded-lg border border-slate-200 bg-white p-4 dark:border-slate-800 dark:bg-slate-900">
              <h3 class="mb-2 font-bold">{{ faq.question }}</h3>
              <p class="text-sm text-slate-600 dark:text-slate-400">{{ faq.answer }}</p>
            </div>
          </div>
        </section>
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
      badge: 'راهنمای سایت',
      title: 'راهنمای استفاده از سایت',
      subtitle: 'راهنمای کامل استفاده از امکانات و بخش‌های مختلف سایت انجمن',
      gettingStartedTitle: 'شروع کار',
      gettingStartedText: 'سایت انجمن علمی ریه کودکان ایران یک پلتفرم جامع برای پزشکان، محققان و علاقه‌مندان به حوزه بیماری‌های تنفسی کودکان است. در این سایت می‌توانید:',
      gettingStartedItems: ['به منابع آموزشی و علمی دسترسی داشته باشید', 'در رویدادها و کنگره‌ها ثبت‌نام کنید', 'آخرین اخبار و مقالات علمی را مطالعه کنید', 'با اعضای انجمن ارتباط برقرار کنید'],
      sectionsTitle: 'بخش‌های اصلی سایت',
      sections: [
        { icon: 'home', title: 'صفحه اصلی', description: 'نمای کلی از انجمن، آخرین اخبار و رویدادها' },
        { icon: 'info', title: 'درباره ما', description: 'تاریخچه، اهداف و فعالیت‌های انجمن' },
        { icon: 'school', title: 'آموزش', description: 'منابع آموزشی، کتاب‌ها و راهنماهای پزشکی' },
        { icon: 'article', title: 'انتشارات', description: 'مجلات، کتابچه کنگره‌ها و مقالات علمی' },
        { icon: 'event', title: 'رویدادها', description: 'کنگره‌ها، همایش‌ها و کارگاه‌های آموزشی' },
        { icon: 'groups', title: 'اعضا', description: 'لیست اعضای انجمن و هیئت مدیره' },
      ],
      registerTitle: 'نحوه ثبت‌نام',
      registerText: 'برای ثبت‌نام در رویدادها و استفاده از امکانات ویژه، مراحل زیر را دنبال کنید:',
      registerItems: ['روی دکمه "ثبت‌نام" در منوی بالای سایت کلیک کنید', 'فرم ثبت‌نام را با اطلاعات صحیح تکمیل کنید', 'ایمیل تأیید را چک کنید و لینک فعال‌سازی را کلیک کنید', 'با نام کاربری و رمز عبور خود وارد شوید', 'پروفایل خود را تکمیل کنید'],
      downloadTitle: 'دانلود منابع',
      downloadText: 'برای دانلود کتاب‌ها، مقالات و سایر منابع:',
      downloadItems: ['به بخش "آموزش" یا "انتشارات" بروید', 'دسته‌بندی مورد نظر را انتخاب کنید', 'روی دکمه "دانلود" کنار هر فایل کلیک کنید', 'فایل به صورت خودکار دانلود می‌شود'],
      supportTitle: 'پشتیبانی',
      supportText: 'در صورت بروز مشکل یا نیاز به راهنمایی:',
      supportItems: ['از بخش "تماس با ما" پیام ارسال کنید', 'با شماره تلفن 09013684856 تماس بگیرید', 'ایمیل خود را به info@irspp.ir ارسال کنید'],
      faqTitle: 'سوالات متداول',
      faqSubtitle: 'پاسخ سوالات رایج کاربران',
      faqs: [
        { question: 'آیا ثبت‌نام در سایت رایگان است؟', answer: 'بله، ثبت‌نام در سایت کاملاً رایگان است.' },
        { question: 'چگونه می‌توانم عضو انجمن شوم؟', answer: 'از طریق بخش "تماس با ما" درخواست عضویت خود را ارسال کنید.' },
        { question: 'آیا منابع آموزشی رایگان هستند؟', answer: 'بله، تمام منابع آموزشی به صورت رایگان در دسترس است.' },
        { question: 'چگونه در کنگره‌ها شرکت کنم؟', answer: 'از بخش "رویدادها" رویداد مورد نظر را انتخاب و ثبت‌نام کنید.' },
      ],
    }
  : {
      badge: 'Site Guide',
      title: 'How to Use the Website',
      subtitle: 'A complete guide to the association website sections and features',
      gettingStartedTitle: 'Getting Started',
      gettingStartedText: 'The Iranian Pediatric Lung Scientific Association website is a comprehensive platform for physicians, researchers, and everyone interested in pediatric respiratory medicine. On this website you can:',
      gettingStartedItems: ['Access educational and scientific resources', 'Register for events and congresses', 'Read the latest scientific news and articles', 'Connect with association members'],
      sectionsTitle: 'Main Website Sections',
      sections: [
        { icon: 'home', title: 'Home', description: 'An overview of the association, latest news, and upcoming events' },
        { icon: 'info', title: 'About Us', description: 'Association history, goals, and activities' },
        { icon: 'school', title: 'Education', description: 'Educational resources, books, and medical guides' },
        { icon: 'article', title: 'Publications', description: 'Journals, congress booklets, and scientific articles' },
        { icon: 'event', title: 'Events', description: 'Congresses, conferences, and educational workshops' },
        { icon: 'groups', title: 'Members', description: 'Association members and board members directory' },
      ],
      registerTitle: 'How to Register',
      registerText: 'To register for events and use special features, follow these steps:',
      registerItems: ['Click the "Register" button in the top navigation menu', 'Complete the registration form with accurate information', 'Check your confirmation email and click the activation link', 'Sign in with your username and password', 'Complete your profile'],
      downloadTitle: 'Downloading Resources',
      downloadText: 'To download books, articles, and other resources:',
      downloadItems: ['Go to the "Education" or "Publications" section', 'Choose the category you need', 'Click the "Download" button next to each file', 'The file will start downloading automatically'],
      supportTitle: 'Support',
      supportText: 'If you face any issue or need guidance:',
      supportItems: ['Send a message through the "Contact Us" section', 'Call 09013684856', 'Send your email to info@irspp.ir'],
      faqTitle: 'Frequently Asked Questions',
      faqSubtitle: 'Answers to common user questions',
      faqs: [
        { question: 'Is registration on the website free?', answer: 'Yes, website registration is completely free.' },
        { question: 'How can I become a member of the association?', answer: 'Send your membership request through the "Contact Us" section.' },
        { question: 'Are educational resources free?', answer: 'Yes, all educational resources are available free of charge.' },
        { question: 'How do I participate in congresses?', answer: 'Open the "Events" section, choose the event you want, and register there.' },
      ],
    }))
</script>
