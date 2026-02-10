<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <!-- Header Section -->
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary w-fit">
            <span class="material-symbols-outlined text-[20px]">mail</span>
            {{ $t('contact.badge') }}
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">{{ $t('contact.title') }}</h1>
          <p class="text-lg text-slate-600 dark:text-slate-400 max-w-2xl">{{ $t('contact.subtitle') }}</p>
        </div>

        <!-- Contact Info Cards -->
        <div class="grid grid-cols-1 gap-6 mb-12 md:grid-cols-3">
          <!-- Phone Card -->
          <div class="flex flex-col gap-4 rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="flex h-14 w-14 items-center justify-center rounded-xl bg-primary/10">
              <span class="material-symbols-outlined text-primary text-3xl">call</span>
            </div>
            <div>
              <h3 class="mb-2 text-lg font-bold">{{ $t('contact.phoneTitle') }}</h3>
              <p class="mb-3 text-sm text-slate-500 dark:text-slate-400">{{ $t('contact.phoneSubtitle') }}</p>
              <p class="text-sm font-medium text-slate-900 dark:text-white">{{ $t('footer.phone') }}</p>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">{{ $t('contact.phoneHours') }}</p>
            </div>
          </div>

          <!-- Email Card -->
          <div class="flex flex-col gap-4 rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="flex h-14 w-14 items-center justify-center rounded-xl bg-primary/10">
              <span class="material-symbols-outlined text-primary text-3xl">mail</span>
            </div>
            <div>
              <h3 class="mb-2 text-lg font-bold">{{ $t('contact.emailTitle') }}</h3>
              <p class="mb-3 text-sm text-slate-500 dark:text-slate-400">{{ $t('contact.emailSubtitle') }}</p>
              <p class="text-sm font-medium text-slate-900 dark:text-white">{{ $t('footer.email') }}</p>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">{{ $t('contact.emailResponse') }}</p>
            </div>
          </div>

          <!-- Address Card -->
          <div class="flex flex-col gap-4 rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="flex h-14 w-14 items-center justify-center rounded-xl bg-primary/10">
              <span class="material-symbols-outlined text-primary text-3xl">location_on</span>
            </div>
            <div>
              <h3 class="mb-2 text-lg font-bold">{{ $t('contact.addressTitle') }}</h3>
              <p class="mb-3 text-sm text-slate-500 dark:text-slate-400">{{ $t('contact.addressSubtitle') }}</p>
              <p class="text-sm leading-relaxed text-slate-900 dark:text-white">{{ $t('footer.address') }}</p>
            </div>
          </div>
        </div>

        <!-- Contact Form -->
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
          <!-- Form -->
          <div class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <h2 class="mb-6 text-2xl font-bold">{{ $t('contact.contactFormTitle') }}</h2>
            <form @submit.prevent="handleSubmit" class="flex flex-col gap-4">
              <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                <div>
                  <label class="mb-2 block text-sm font-medium" for="firstName">{{ $t('contact.firstName') }}</label>
                  <input 
                    v-model="form.firstName"
                    class="w-full rounded-lg border border-slate-200 bg-slate-50 px-4 py-3 text-sm focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 dark:border-slate-700 dark:bg-slate-800" 
                    :placeholder="$t('contact.firstNamePlaceholder')" 
                    type="text"
                    id="firstName"
                    required
                  />
                </div>
                <div>
                  <label class="mb-2 block text-sm font-medium" for="lastName">{{ $t('contact.lastName') }}</label>
                  <input 
                    v-model="form.lastName"
                    class="w-full rounded-lg border border-slate-200 bg-slate-50 px-4 py-3 text-sm focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 dark:border-slate-700 dark:bg-slate-800" 
                    :placeholder="$t('contact.lastNamePlaceholder')" 
                    type="text"
                    id="lastName"
                    required
                  />
                </div>
              </div>
              
              <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                <div>
                  <label class="mb-2 block text-sm font-medium" for="email">{{ $t('contact.emailAddress') }}</label>
                  <input 
                    v-model="form.email"
                    class="w-full rounded-lg border border-slate-200 bg-slate-50 px-4 py-3 text-sm focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 dark:border-slate-700 dark:bg-slate-800" 
                    :placeholder="$t('contact.emailPlaceholder')" 
                    type="email"
                    id="email"
                    required
                  />
                </div>
                <div>
                  <label class="mb-2 block text-sm font-medium" for="phone">{{ $t('contact.phoneNumber') }}</label>
                  <input 
                    v-model="form.phone"
                    class="w-full rounded-lg border border-slate-200 bg-slate-50 px-4 py-3 text-sm focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 dark:border-slate-700 dark:bg-slate-800" 
                    :placeholder="$t('contact.phonePlaceholder')" 
                    type="tel"
                    id="phone"
                    required
                  />
                </div>
              </div>

              <div>
                <label class="mb-2 block text-sm font-medium" for="subject">{{ $t('contact.subject') }}</label>
                <select 
                  v-model="form.subject"
                  class="w-full rounded-lg border border-slate-200 bg-slate-50 px-4 py-3 text-sm focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 dark:border-slate-700 dark:bg-slate-800"
                  id="subject"
                  required
                >
                  <option value="">{{ $t('contact.subjectPlaceholder') }}</option>
                  <option value="consultation">{{ $t('contact.subjectConsultation') }}</option>
                  <option value="membership">{{ $t('contact.subjectMembership') }}</option>
                  <option value="events">{{ $t('contact.subjectEvents') }}</option>
                  <option value="education">{{ $t('contact.subjectEducation') }}</option>
                  <option value="research">{{ $t('contact.subjectResearch') }}</option>
                  <option value="other">{{ $t('contact.subjectOther') }}</option>
                </select>
              </div>

              <div>
                <label class="mb-2 block text-sm font-medium" for="message">{{ $t('contact.message') }}</label>
                <textarea 
                  v-model="form.message"
                  class="w-full rounded-lg border border-slate-200 bg-slate-50 px-4 py-3 text-sm focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 dark:border-slate-700 dark:bg-slate-800" 
                  :placeholder="$t('contact.messagePlaceholder')" 
                  rows="5"
                  id="message"
                  required
                ></textarea>
              </div>

              <div class="flex items-start gap-2">
                <input 
                  v-model="form.privacy"
                  type="checkbox" 
                  class="mt-1 h-4 w-4 rounded border-slate-300 text-primary focus:ring-2 focus:ring-primary/20" 
                  id="privacy"
                  required
                />
                <label class="text-sm text-slate-600 dark:text-slate-400" for="privacy">
                  {{ $t('contact.privacyAgreement') }} <a href="#" class="text-primary hover:underline">{{ $t('contact.termsAndConditions') }}</a>
                </label>
              </div>

              <button 
                type="submit" 
                class="flex items-center justify-center gap-2 rounded-lg bg-primary px-6 py-3 font-bold text-white transition-colors hover:bg-primary/90 disabled:opacity-50"
                :disabled="isSubmitting"
              >
                <span class="material-symbols-outlined text-[20px]">send</span>
                {{ isSubmitting ? $t('contact.sending') : $t('contact.send') }}
              </button>
            </form>
          </div>

          <!-- FAQ Section -->
          <div class="flex flex-col gap-6">
            <div class="rounded-xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
              <h2 class="mb-6 text-2xl font-bold">{{ $t('contact.faqTitle') }}</h2>
              <div class="flex flex-col gap-4">
                <details class="group rounded-lg border border-slate-200 dark:border-slate-700">
                  <summary class="flex cursor-pointer items-center justify-between p-4 font-medium">
                    <span>{{ $t('contact.faq1Question') }}</span>
                    <span class="material-symbols-outlined transition-transform group-open:rotate-180">expand_more</span>
                  </summary>
                  <div class="border-t border-slate-200 p-4 text-sm leading-relaxed text-slate-600 dark:border-slate-700 dark:text-slate-400">
                    {{ $t('contact.faq1Answer') }}
                  </div>
                </details>

                <details class="group rounded-lg border border-slate-200 dark:border-slate-700">
                  <summary class="flex cursor-pointer items-center justify-between p-4 font-medium">
                    <span>{{ $t('contact.faq2Question') }}</span>
                    <span class="material-symbols-outlined transition-transform group-open:rotate-180">expand_more</span>
                  </summary>
                  <div class="border-t border-slate-200 p-4 text-sm leading-relaxed text-slate-600 dark:border-slate-700 dark:text-slate-400">
                    {{ $t('contact.faq2Answer') }}
                  </div>
                </details>

                <details class="group rounded-lg border border-slate-200 dark:border-slate-700">
                  <summary class="flex cursor-pointer items-center justify-between p-4 font-medium">
                    <span>{{ $t('contact.faq3Question') }}</span>
                    <span class="material-symbols-outlined transition-transform group-open:rotate-180">expand_more</span>
                  </summary>
                  <div class="border-t border-slate-200 p-4 text-sm leading-relaxed text-slate-600 dark:border-slate-700 dark:text-slate-400">
                    {{ $t('contact.faq3Answer') }}
                  </div>
                </details>

                <details class="group rounded-lg border border-slate-200 dark:border-slate-700">
                  <summary class="flex cursor-pointer items-center justify-between p-4 font-medium">
                    <span>{{ $t('contact.faq4Question') }}</span>
                    <span class="material-symbols-outlined transition-transform group-open:rotate-180">expand_more</span>
                  </summary>
                  <div class="border-t border-slate-200 p-4 text-sm leading-relaxed text-slate-600 dark:border-slate-700 dark:text-slate-400">
                    {{ $t('contact.faq4Answer') }}
                  </div>
                </details>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue';

const form = reactive({
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  subject: '',
  message: '',
  privacy: false
});

const isSubmitting = ref(false);

function handleSubmit() {
  isSubmitting.value = true;
  setTimeout(() => {
    alert('پیام شما با موفقیت ارسال شد!');
    Object.assign(form, {
      firstName: '',
      lastName: '',
      email: '',
      phone: '',
      subject: '',
      message: '',
      privacy: false
    });
    isSubmitting.value = false;
  }, 1000);
}
</script>
