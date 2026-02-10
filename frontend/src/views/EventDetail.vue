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

        <div v-if="eventLoading" class="p-12 text-center">
          <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
          <p class="mt-4 text-slate-500">در حال بارگذاری...</p>
        </div>

        <div v-else-if="eventError" class="p-6">
          <div class="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-xl p-6 text-center">
            <span class="material-symbols-outlined text-red-600 text-4xl mb-2">error</span>
            <p class="text-red-600 dark:text-red-400">{{ eventError }}</p>
          </div>
        </div>

        <div v-else-if="event" class="grid grid-cols-1 gap-8 lg:grid-cols-3">
          <!-- Main Content -->
          <div class="lg:col-span-2">
            <article class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
              <!-- Event Header -->
              <div class="mb-6">
                <div v-if="event.is_registration_open" class="mb-4 inline-block rounded-full bg-green-100 px-4 py-2 text-sm font-bold text-green-600">
                  در حال ثبت‌نام
                </div>
                <div v-else class="mb-4 inline-block rounded-full bg-gray-100 px-4 py-2 text-sm font-bold text-gray-600">
                  ثبت‌نام بسته
                </div>
                <h1 class="mb-4 text-3xl font-black leading-tight md:text-4xl">
                  {{ event.title }}
                </h1>
              </div>

              <!-- Featured Image -->
              <div class="mb-8 aspect-video overflow-hidden rounded-xl bg-slate-100 dark:bg-slate-800">
                <img 
                  :src="event.image || '/img/events.png'" 
                  :alt="event.title" 
                  class="h-full w-full object-cover"
                />
              </div>

              <!-- Event Description -->
              <div class="prose prose-slate max-w-none dark:prose-invert">
                <h2 class="mb-4 text-2xl font-bold">درباره رویداد</h2>
                <div v-html="event.description" class="leading-relaxed"></div>
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
                      <div class="font-medium">{{ formatDate(event.start_date) }}</div>
                    </div>
                  </div>
                  
                  <div class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-primary">location_on</span>
                    <div>
                      <div class="text-sm font-medium text-slate-500 dark:text-slate-400">مکان</div>
                      <div class="font-medium">{{ event.location }}</div>
                    </div>
                  </div>
                  
                  <div v-if="event.max_participants" class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-primary">group</span>
                    <div>
                      <div class="text-sm font-medium text-slate-500 dark:text-slate-400">ظرفیت</div>
                      <div class="font-medium">{{ event.max_participants }} نفر</div>
                    </div>
                  </div>

                  <!-- Retraining Number Display -->
                  <div v-if="event.retraining_number" class="flex items-start gap-3">
                    <span class="material-symbols-outlined text-primary">badge</span>
                    <div>
                      <div class="text-sm font-medium text-slate-500 dark:text-slate-400">شماره بازآموزی</div>
                      <div class="font-bold text-lg text-primary">{{ event.retraining_number }}</div>
                    </div>
                  </div>
                </div>

                <!-- Show registration button only if NO retraining number -->
                <button 
                  v-if="!event.retraining_number && event.is_registration_open"
                  @click="showRegistrationForm = true"
                  class="mt-6 w-full rounded-lg bg-primary py-3 font-bold text-white transition-colors hover:bg-primary/90"
                >
                  ثبت‌نام در رویداد
                </button>
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
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { getApiUrl } from '@/utils/api';

const route = useRoute();
const showRegistrationForm = ref(false);
const isSubmitting = ref(false);
const event = ref<any>(null);
const eventLoading = ref(true);
const eventError = ref<string | null>(null);

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

const formatDate = (isoDate: string | null) => {
  if (!isoDate) return '';
  try {
    return new Date(isoDate).toLocaleDateString('fa-IR', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });
  } catch (error) {
    return isoDate;
  }
};

const fetchEvent = async () => {
  eventLoading.value = true;
  eventError.value = null;

  try {
    const slug = route.params.slug as string;
    const response = await fetch(getApiUrl(`/api/events/${slug}/`), {
      credentials: 'include',
    });

    if (!response.ok) {
      throw new Error(`خطا در دریافت رویداد از سرور (${response.status})`);
    }

    const data = await response.json();

    if (!data.success || !data.event) {
      throw new Error('ساختار داده رویداد نامعتبر است');
    }

    event.value = {
      ...data.event,
      image: data.event.image ? getApiUrl(data.event.image) : '/img/events.png'
    };
  } catch (error: any) {
    console.error('Failed to load event:', error);
    eventError.value = error.message || 'خطای ناشناخته هنگام دریافت رویداد';
  } finally {
    eventLoading.value = false;
  }
};

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

onMounted(() => {
  fetchEvent();
});
</script>
