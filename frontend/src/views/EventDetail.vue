<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1024px] grow px-6 py-8 lg:px-10">
        <!-- Breadcrumb -->
        <nav class="mb-6 flex items-center gap-2 text-sm text-slate-500">
          <router-link to="/" class="hover:text-primary">{{ $t('nav.home') }}</router-link>
          <span class="material-symbols-outlined text-[16px]">chevron_left</span>
          <router-link to="/events" class="hover:text-primary">{{ $t('nav.events') }}</router-link>
          <span class="material-symbols-outlined text-[16px]">chevron_left</span>
          <span class="text-slate-900 dark:text-white">جزئیات رویداد</span>
        </nav>

        <div class="grid grid-cols-1 gap-8 lg:grid-cols-3">
          <!-- Main Content -->
          <div class="lg:col-span-2">
            <article class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
              <!-- Event Header -->
              <div class="mb-6">
                <div class="mb-4 inline-block rounded-full bg-green-100 px-4 py-2 text-sm font-bold text-green-600">
                  در حال ثبت‌نام
                </div>
                <h1 class="mb-4 text-3xl font-black leading-tight md:text-4xl">
                  نهمین کنگره بیماری‌های ریوی کودکان و نوزادان ایران
                </h1>
              </div>

              <!-- Featured Image -->
              <div class="mb-8 aspect-video overflow-hidden rounded-xl bg-slate-100 dark:bg-slate-800">
                <img 
                  src="/Content/photo_2025-12-05_21-18-04.jpg" 
                  alt="کنگره" 
                  class="h-full w-full object-cover"
                />
              </div>

              <!-- Event Description -->
              <div class="prose prose-slate max-w-none dark:prose-invert">
                <h2 class="mb-4 text-2xl font-bold">درباره رویداد</h2>
                <p class="leading-relaxed">
                  نهمین کنگره بیماری‌های ریوی کودکان و نوزادان ایران با هدف ارتقای دانش و مهارت‌های تشخیصی و درمانی پزشکان و متخصصان در زمینه بیماری‌های تنفسی اطفال برگزار می‌شود.
                </p>

                <h3 class="mt-6 mb-3 text-xl font-bold">موضوعات کنگره:</h3>
                <ul class="list-disc pr-6 space-y-2">
                  <li>آسم و آلرژی‌های تنفسی در کودکان</li>
                  <li>عفونت‌های ریوی و مدیریت آنتی‌بیوتیک</li>
                  <li>فیبروز سیستیک و بیماری‌های ژنتیکی ریه</li>
                  <li>مراقبت‌های ویژه تنفسی نوزادان</li>
                  <li>تکنیک‌های تشخیصی پیشرفته</li>
                </ul>

                <h3 class="mt-6 mb-3 text-xl font-bold">سخنرانان:</h3>
                <p class="leading-relaxed">
                  برجسته‌ترین اساتید و متخصصان ریه کودکان از سراسر کشور و همچنین سخنرانان بین‌المللی مدعو در این کنگره حضور خواهند داشت.
                </p>
              </div>
            </article>
          </div>

          <!-- Sidebar -->
          <div class="lg:col-span-1">
            <div class="sticky top-24 flex flex-col gap-6">
              <!-- Event Info Card -->
              <div class="rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                <h3 class="mb-4 text-lg font-bold">اطلاعات رویداد</h3>
                <div class="flex flex-col gap-4">
                  <div class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-primary">calendar_month</span>
                    <div>
                      <div class="text-sm font-medium text-slate-500 dark:text-slate-400">تاریخ</div>
                      <div class="font-medium">۲۵ لغایت ۲۷ مهر ۱۴۰۳</div>
                    </div>
                  </div>
                  
                  <div class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-primary">schedule</span>
                    <div>
                      <div class="text-sm font-medium text-slate-500 dark:text-slate-400">ساعت</div>
                      <div class="font-medium">۸:۰۰ صبح تا ۶:۰۰ عصر</div>
                    </div>
                  </div>
                  
                  <div class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-primary">location_on</span>
                    <div>
                      <div class="text-sm font-medium text-slate-500 dark:text-slate-400">مکان</div>
                      <div class="font-medium">تهران، مرکز طبی کودکان - تالار همایش‌ها</div>
                    </div>
                  </div>
                  
                  <div class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-primary">payments</span>
                    <div>
                      <div class="text-sm font-medium text-slate-500 dark:text-slate-400">هزینه ثبت‌نام</div>
                      <div class="font-medium">۲,۵۰۰,۰۰۰ تومان</div>
                    </div>
                  </div>
                  
                  <div class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-primary">group</span>
                    <div>
                      <div class="text-sm font-medium text-slate-500 dark:text-slate-400">ظرفیت</div>
                      <div class="font-medium">۲۰۰ نفر</div>
                    </div>
                  </div>
                </div>

                <button 
                  @click="showRegistrationForm = true"
                  class="mt-6 w-full rounded-lg bg-primary py-3 font-bold text-white transition-colors hover:bg-primary/90"
                >
                  ثبت‌نام در کنگره
                </button>
              </div>

              <!-- Countdown Card -->
              <div class="rounded-xl border border-primary/20 bg-primary/5 p-6 dark:bg-primary/10">
                <h3 class="mb-4 text-center text-lg font-bold">زمان باقی‌مانده تا شروع</h3>
                <div class="grid grid-cols-3 gap-3 text-center">
                  <div>
                    <div class="text-2xl font-black text-primary">۴۵</div>
                    <div class="text-xs text-slate-500">روز</div>
                  </div>
                  <div>
                    <div class="text-2xl font-black text-primary">۱۲</div>
                    <div class="text-xs text-slate-500">ساعت</div>
                  </div>
                  <div>
                    <div class="text-2xl font-black text-primary">۳۰</div>
                    <div class="text-xs text-slate-500">دقیقه</div>
                  </div>
                </div>
              </div>

              <!-- Share Card -->
              <div class="rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                <h3 class="mb-4 text-lg font-bold">اشتراک‌گذاری</h3>
                <div class="flex gap-2">
                  <button class="flex h-10 w-10 items-center justify-center rounded-full bg-slate-100 hover:bg-primary hover:text-white transition-colors dark:bg-slate-800">
                    <span class="material-symbols-outlined text-[20px]">share</span>
                  </button>
                  <button class="flex h-10 w-10 items-center justify-center rounded-full bg-slate-100 hover:bg-primary hover:text-white transition-colors dark:bg-slate-800">
                    <span class="material-symbols-outlined text-[20px]">link</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>

    <!-- Registration Modal -->
    <div 
      v-if="showRegistrationForm" 
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4"
      @click.self="showRegistrationForm = false"
    >
      <div class="max-h-[90vh] w-full max-w-2xl overflow-y-auto rounded-xl border border-slate-200 bg-white shadow-xl dark:border-slate-800 dark:bg-slate-900">
        <div class="sticky top-0 flex items-center justify-between border-b border-slate-200 bg-white p-6 dark:border-slate-800 dark:bg-slate-900">
          <h2 class="text-2xl font-bold">ثبت‌نام در کنگره</h2>
          <button @click="showRegistrationForm = false" class="rounded-lg p-2 hover:bg-slate-100 dark:hover:bg-slate-800">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>
        
        <form @submit.prevent="submitRegistration" class="p-6">
          <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
            <!-- Full Name -->
            <div class="md:col-span-2">
              <label class="mb-2 block text-sm font-medium">نام و نام خانوادگی *</label>
              <input 
                v-model="registrationForm.fullName"
                type="text" 
                required
                class="w-full rounded-lg border border-slate-300 bg-white px-4 py-3 text-slate-900 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 dark:border-slate-700 dark:bg-slate-800 dark:text-white"
                placeholder="نام و نام خانوادگی خود را وارد کنید"
              />
            </div>

            <!-- Email -->
            <div>
              <label class="mb-2 block text-sm font-medium">ایمیل *</label>
              <input 
                v-model="registrationForm.email"
                type="email" 
                required
                class="w-full rounded-lg border border-slate-300 bg-white px-4 py-3 text-slate-900 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 dark:border-slate-700 dark:bg-slate-800 dark:text-white"
                placeholder="example@email.com"
              />
            </div>

            <!-- Phone -->
            <div>
              <label class="mb-2 block text-sm font-medium">شماره تماس *</label>
              <input 
                v-model="registrationForm.phone"
                type="tel" 
                required
                class="w-full rounded-lg border border-slate-300 bg-white px-4 py-3 text-slate-900 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 dark:border-slate-700 dark:bg-slate-800 dark:text-white"
                placeholder="09123456789"
              />
            </div>

            <!-- Medical Code -->
            <div>
              <label class="mb-2 block text-sm font-medium">کد نظام پزشکی *</label>
              <input 
                v-model="registrationForm.medicalCode"
                type="text" 
                required
                class="w-full rounded-lg border border-slate-300 bg-white px-4 py-3 text-slate-900 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 dark:border-slate-700 dark:bg-slate-800 dark:text-white"
                placeholder="کد نظام پزشکی"
              />
            </div>

            <!-- Specialty -->
            <div>
              <label class="mb-2 block text-sm font-medium">تخصص *</label>
              <select 
                v-model="registrationForm.specialty"
                required
                class="w-full rounded-lg border border-slate-300 bg-white px-4 py-3 text-slate-900 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 dark:border-slate-700 dark:bg-slate-800 dark:text-white"
              >
                <option value="">انتخاب کنید</option>
                <option value="pediatric_pulmonology">ریه کودکان</option>
                <option value="pediatrics">اطفال</option>
                <option value="neonatology">نوزادان</option>
                <option value="allergy">آلرژی و ایمونولوژی</option>
                <option value="other">سایر</option>
              </select>
            </div>

            <!-- City -->
            <div>
              <label class="mb-2 block text-sm font-medium">شهر *</label>
              <input 
                v-model="registrationForm.city"
                type="text" 
                required
                class="w-full rounded-lg border border-slate-300 bg-white px-4 py-3 text-slate-900 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 dark:border-slate-700 dark:bg-slate-800 dark:text-white"
                placeholder="شهر محل سکونت"
              />
            </div>

            <!-- Organization -->
            <div>
              <label class="mb-2 block text-sm font-medium">محل کار</label>
              <input 
                v-model="registrationForm.organization"
                type="text" 
                class="w-full rounded-lg border border-slate-300 bg-white px-4 py-3 text-slate-900 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 dark:border-slate-700 dark:bg-slate-800 dark:text-white"
                placeholder="بیمارستان یا مرکز درمانی"
              />
            </div>

            <!-- Accommodation -->
            <div class="md:col-span-2">
              <label class="mb-2 block text-sm font-medium">نیاز به اقامت</label>
              <div class="flex gap-4">
                <label class="flex items-center gap-2">
                  <input 
                    v-model="registrationForm.needsAccommodation"
                    type="radio" 
                    :value="true"
                    class="h-4 w-4 text-primary focus:ring-2 focus:ring-primary/20"
                  />
                  <span>بله</span>
                </label>
                <label class="flex items-center gap-2">
                  <input 
                    v-model="registrationForm.needsAccommodation"
                    type="radio" 
                    :value="false"
                    class="h-4 w-4 text-primary focus:ring-2 focus:ring-primary/20"
                  />
                  <span>خیر</span>
                </label>
              </div>
            </div>

            <!-- Notes -->
            <div class="md:col-span-2">
              <label class="mb-2 block text-sm font-medium">توضیحات</label>
              <textarea 
                v-model="registrationForm.notes"
                rows="3"
                class="w-full rounded-lg border border-slate-300 bg-white px-4 py-3 text-slate-900 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 dark:border-slate-700 dark:bg-slate-800 dark:text-white"
                placeholder="توضیحات اضافی (اختیاری)"
              ></textarea>
            </div>
          </div>

          <!-- Submit Button -->
          <div class="mt-6 flex gap-3">
            <button 
              type="submit"
              :disabled="isSubmitting"
              class="flex-1 rounded-lg bg-primary py-3 font-bold text-white transition-colors hover:bg-primary/90 disabled:opacity-50"
            >
              <span v-if="!isSubmitting">ثبت‌نام</span>
              <span v-else>در حال ارسال...</span>
            </button>
            <button 
              type="button"
              @click="showRegistrationForm = false"
              class="rounded-lg border border-slate-300 px-6 py-3 font-bold transition-colors hover:bg-slate-100 dark:border-slate-700 dark:hover:bg-slate-800"
            >
              انصراف
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const showRegistrationForm = ref(false);
const isSubmitting = ref(false);

const registrationForm = ref({
  fullName: '',
  email: '',
  phone: '',
  medicalCode: '',
  specialty: '',
  city: '',
  organization: '',
  needsAccommodation: false,
  notes: ''
});

const submitRegistration = async () => {
  isSubmitting.value = true;
  
  try {
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    alert('ثبت‌نام شما با موفقیت انجام شد. اطلاعات تکمیلی به ایمیل شما ارسال خواهد شد.');
    showRegistrationForm.value = false;
    
    // Reset form
    registrationForm.value = {
      fullName: '',
      email: '',
      phone: '',
      medicalCode: '',
      specialty: '',
      city: '',
      organization: '',
      needsAccommodation: false,
      notes: ''
    };
  } catch (error) {
    alert('خطا در ثبت‌نام. لطفاً دوباره تلاش کنید.');
  } finally {
    isSubmitting.value = false;
  }
};
</script>
