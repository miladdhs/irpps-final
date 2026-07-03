<template>
  <div class="flex min-h-screen items-center justify-center bg-gradient-to-br from-blue-50 via-white to-indigo-50 px-4 py-12 sm:px-6 lg:px-8">
    <div class="w-full max-w-md">
      <div class="mb-8 text-center">
        <img src="/img/logo.png" alt="Association Logo" class="mx-auto mb-4 h-20" />
        <h2 class="mb-2 text-3xl font-bold text-gray-900">{{ $t('auth.loginTitle') }}</h2>
        <p class="text-gray-600">{{ $t('auth.loginDesc') }}</p>
      </div>

      <div class="rounded-2xl bg-white p-8 shadow-xl">
        <form @submit.prevent="handleLogin" class="space-y-6">
          <div v-if="errorMessage" class="rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
            {{ errorMessage }}
          </div>

          <div v-if="successMessage" class="rounded-lg border border-green-200 bg-green-50 px-4 py-3 text-sm text-green-700">
            {{ successMessage }}
          </div>

          <div>
            <label for="username" class="mb-2 block text-sm font-medium text-gray-700">
              {{ $t('auth.username') }}
            </label>
            <input
              id="username"
              v-model="formData.username"
              type="text"
              required
              class="w-full rounded-lg border border-gray-300 px-4 py-3 transition focus:border-transparent focus:ring-2 focus:ring-blue-500"
              :placeholder="$t('auth.usernamePlaceholder')"
            >
          </div>

          <div>
            <label for="password" class="mb-2 block text-sm font-medium text-gray-700">
              {{ $t('auth.password') }}
            </label>
            <input
              id="password"
              v-model="formData.password"
              type="password"
              required
              class="w-full rounded-lg border border-gray-300 px-4 py-3 transition focus:border-transparent focus:ring-2 focus:ring-blue-500"
              :placeholder="$t('auth.passwordPlaceholder')"
            >
          </div>

          <button
            type="submit"
            :disabled="isLoading"
            class="w-full rounded-lg bg-gradient-to-r from-blue-600 to-indigo-600 px-4 py-3 font-medium text-white transition hover:from-blue-700 hover:to-indigo-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
          >
            <span v-if="!isLoading">{{ $t('auth.loginButton') }}</span>
            <span v-else class="flex items-center justify-center gap-2">
              <span class="material-symbols-outlined animate-spin">progress_activity</span>
              {{ $t('auth.loggingIn') }}
            </span>
          </button>
        </form>

        <div class="mt-6 text-center">
          <p class="text-sm text-gray-600">
            {{ locale.value === 'fa' ? 'حساب کاربری ندارید؟' : "Don't have an account?" }}
            <router-link to="/register" class="font-medium text-blue-600 hover:text-blue-700">
              {{ $t('nav.register') }}
            </router-link>
          </p>
        </div>

        <div class="mt-4 text-center">
          <router-link to="/" class="text-sm text-gray-500 hover:text-gray-700">
            {{ locale.value === 'fa' ? 'بازگشت به صفحه اصلی' : 'Back to home' }}
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const { locale } = useI18n()
const authStore = useAuthStore()

const formData = ref({
  username: '',
  password: '',
})

const isLoading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

if (route.query.registered === 'true') {
  successMessage.value = locale.value === 'fa'
    ? 'ثبت نام با موفقیت انجام شد. لطفاً وارد شوید.'
    : 'Registration completed successfully. Please sign in.'
}

async function handleLogin() {
  isLoading.value = true
  errorMessage.value = ''
  successMessage.value = ''

  const result = await authStore.login(formData.value.username, formData.value.password)

  if (result.success) {
    const redirect = route.query.redirect as string || '/'
    await router.push(redirect)
  } else {
    errorMessage.value = result.error || (locale.value === 'fa' ? 'خطا در ورود' : 'Login failed')
  }

  isLoading.value = false
}
</script>
