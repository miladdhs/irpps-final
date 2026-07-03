<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-50 px-4 py-12 dark:from-slate-950 dark:via-slate-900 dark:to-slate-950">
    <div class="mx-auto max-w-2xl">
      <div class="mb-8 text-center">
        <img :src="'/img/logo.png'" :alt="copy.logoAlt" class="mx-auto mb-4 h-20" />
        <h2 class="mb-2 text-3xl font-bold text-gray-900 dark:text-white">{{ copy.title }}</h2>
        <p class="text-gray-600 dark:text-slate-300">{{ copy.subtitle }}</p>
      </div>

      <div class="rounded-2xl bg-white p-8 shadow-xl dark:bg-slate-900">
        <form class="space-y-6" @submit.prevent="handleRegister">
          <div
            v-if="errorMessage"
            class="rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700 dark:border-red-900 dark:bg-red-950 dark:text-red-300"
          >
            {{ errorMessage }}
          </div>

          <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
            <div>
              <label for="first_name" class="mb-2 block text-sm font-medium text-gray-700 dark:text-slate-200">{{ copy.firstNameLabel }}</label>
              <input id="first_name" v-model="formData.first_name" type="text" required class="w-full rounded-lg border border-gray-300 px-4 py-3 transition focus:border-transparent focus:ring-2 focus:ring-blue-500 dark:border-slate-700 dark:bg-slate-800 dark:text-white" :placeholder="copy.firstNamePlaceholder" />
            </div>

            <div>
              <label for="last_name" class="mb-2 block text-sm font-medium text-gray-700 dark:text-slate-200">{{ copy.lastNameLabel }}</label>
              <input id="last_name" v-model="formData.last_name" type="text" required class="w-full rounded-lg border border-gray-300 px-4 py-3 transition focus:border-transparent focus:ring-2 focus:ring-blue-500 dark:border-slate-700 dark:bg-slate-800 dark:text-white" :placeholder="copy.lastNamePlaceholder" />
            </div>

            <div>
              <label for="username" class="mb-2 block text-sm font-medium text-gray-700 dark:text-slate-200">{{ copy.usernameLabel }}</label>
              <input id="username" v-model="formData.username" type="text" required class="w-full rounded-lg border border-gray-300 px-4 py-3 transition focus:border-transparent focus:ring-2 focus:ring-blue-500 dark:border-slate-700 dark:bg-slate-800 dark:text-white" :placeholder="copy.usernamePlaceholder" />
            </div>

            <div>
              <label for="email" class="mb-2 block text-sm font-medium text-gray-700 dark:text-slate-200">{{ copy.emailLabel }}</label>
              <input id="email" v-model="formData.email" type="email" required class="w-full rounded-lg border border-gray-300 px-4 py-3 transition focus:border-transparent focus:ring-2 focus:ring-blue-500 dark:border-slate-700 dark:bg-slate-800 dark:text-white" placeholder="example@email.com" />
            </div>

            <div>
              <label for="phone" class="mb-2 block text-sm font-medium text-gray-700 dark:text-slate-200">{{ copy.phoneLabel }}</label>
              <input id="phone" v-model="formData.phone" type="tel" required class="w-full rounded-lg border border-gray-300 px-4 py-3 transition focus:border-transparent focus:ring-2 focus:ring-blue-500 dark:border-slate-700 dark:bg-slate-800 dark:text-white" placeholder="09123456789" />
            </div>

            <div>
              <label for="password" class="mb-2 block text-sm font-medium text-gray-700 dark:text-slate-200">{{ copy.passwordLabel }}</label>
              <input id="password" v-model="formData.password" type="password" required class="w-full rounded-lg border border-gray-300 px-4 py-3 transition focus:border-transparent focus:ring-2 focus:ring-blue-500 dark:border-slate-700 dark:bg-slate-800 dark:text-white" :placeholder="copy.passwordPlaceholder" />
            </div>

            <div>
              <label for="password_confirm" class="mb-2 block text-sm font-medium text-gray-700 dark:text-slate-200">{{ copy.passwordConfirmLabel }}</label>
              <input id="password_confirm" v-model="formData.password_confirm" type="password" required class="w-full rounded-lg border border-gray-300 px-4 py-3 transition focus:border-transparent focus:ring-2 focus:ring-blue-500 dark:border-slate-700 dark:bg-slate-800 dark:text-white" :placeholder="copy.passwordConfirmPlaceholder" />
            </div>
          </div>

          <div class="rounded-lg border border-blue-200 bg-blue-50 px-4 py-3 text-sm text-blue-700 dark:border-blue-900 dark:bg-blue-950 dark:text-blue-300">
            <span class="material-symbols-outlined ml-2 align-middle text-lg">info</span>
            {{ copy.note }}
          </div>

          <button type="submit" :disabled="isLoading" class="w-full rounded-lg bg-gradient-to-r from-blue-600 to-indigo-600 px-4 py-3 font-medium text-white transition hover:from-blue-700 hover:to-indigo-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50">
            <span v-if="!isLoading">{{ copy.submit }}</span>
            <span v-else class="flex items-center justify-center gap-2">
              <span class="material-symbols-outlined animate-spin">progress_activity</span>
              {{ copy.submitting }}
            </span>
          </button>
        </form>

        <div class="mt-6 text-center">
          <p class="text-sm text-gray-600 dark:text-slate-300">
            {{ copy.hasAccount }}
            <router-link to="/login" class="font-medium text-blue-600 hover:text-blue-700">{{ copy.login }}</router-link>
          </p>
        </div>

        <div class="mt-4 text-center">
          <router-link to="/" class="text-sm text-gray-500 hover:text-gray-700 dark:text-slate-400 dark:hover:text-slate-200">{{ copy.backHome }}</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()
const { locale } = useI18n()

const formData = ref({
  username: '',
  email: '',
  phone: '',
  first_name: '',
  last_name: '',
  password: '',
  password_confirm: '',
})

const isLoading = ref(false)
const errorMessage = ref('')

const copy = computed(() => (locale.value === 'fa'
  ? {
      logoAlt: 'لوگو انجمن',
      title: 'ثبت نام',
      subtitle: 'عضویت در انجمن علمی ریه کودکان',
      firstNameLabel: 'نام (فارسی) *',
      firstNamePlaceholder: 'نام فارسی',
      lastNameLabel: 'نام کامل (انگلیسی) *',
      lastNamePlaceholder: 'Full Name in English',
      usernameLabel: 'نام کاربری *',
      usernamePlaceholder: 'نام کاربری',
      emailLabel: 'ایمیل *',
      phoneLabel: 'شماره تماس *',
      passwordLabel: 'رمز عبور *',
      passwordPlaceholder: 'حداقل 8 کاراکتر',
      passwordConfirmLabel: 'تکرار رمز عبور *',
      passwordConfirmPlaceholder: 'تکرار رمز عبور',
      note: 'پس از ثبت نام، حساب شما توسط مدیریت بررسی و تایید خواهد شد.',
      submit: 'ثبت نام',
      submitting: 'در حال ثبت نام...',
      hasAccount: 'قبلاً ثبت نام کرده‌اید؟',
      login: 'وارد شوید',
      backHome: 'بازگشت به صفحه اصلی',
      passwordMismatch: 'رمزهای عبور مطابقت ندارند',
      genericError: 'خطا در ثبت نام',
    }
  : {
      logoAlt: 'Association logo',
      title: 'Register',
      subtitle: 'Join the Iranian Pediatric Lung Scientific Association',
      firstNameLabel: 'First Name (Persian) *',
      firstNamePlaceholder: 'Persian first name',
      lastNameLabel: 'Full Name (English) *',
      lastNamePlaceholder: 'Full Name in English',
      usernameLabel: 'Username *',
      usernamePlaceholder: 'Username',
      emailLabel: 'Email *',
      phoneLabel: 'Phone Number *',
      passwordLabel: 'Password *',
      passwordPlaceholder: 'At least 8 characters',
      passwordConfirmLabel: 'Confirm Password *',
      passwordConfirmPlaceholder: 'Repeat your password',
      note: 'After registration, your account will be reviewed and approved by the administrator.',
      submit: 'Register',
      submitting: 'Registering...',
      hasAccount: 'Already registered?',
      login: 'Sign in',
      backHome: 'Back to home',
      passwordMismatch: 'Passwords do not match',
      genericError: 'Registration failed',
    }))

async function handleRegister() {
  isLoading.value = true
  errorMessage.value = ''

  if (formData.value.password !== formData.value.password_confirm) {
    errorMessage.value = copy.value.passwordMismatch
    isLoading.value = false
    return
  }

  const result = await authStore.register(formData.value)

  if (result.success) {
    router.push({ path: '/login', query: { registered: 'true' } })
  } else {
    errorMessage.value = result.error || copy.value.genericError
  }

  isLoading.value = false
}
</script>
