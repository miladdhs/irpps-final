<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-50 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full">
      <!-- Logo and Title -->
      <div class="text-center mb-8">
        <img src="/img/logo.png" alt="لوگو" class="h-20 mx-auto mb-4">
        <h2 class="text-3xl font-bold text-gray-900 mb-2">ورود به سیستم</h2>
        <p class="text-gray-600">به انجمن علمی ریه کودکان خوش آمدید</p>
      </div>

      <!-- Login Form -->
      <div class="bg-white rounded-2xl shadow-xl p-8">
        <form @submit.prevent="handleLogin" class="space-y-6">
          <!-- Error Message -->
          <div v-if="errorMessage" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm">
            {{ errorMessage }}
          </div>

          <!-- Success Message -->
          <div v-if="successMessage" class="bg-green-50 border border-green-200 text-green-700 px-4 py-3 rounded-lg text-sm">
            {{ successMessage }}
          </div>

          <!-- Username -->
          <div>
            <label for="username" class="block text-sm font-medium text-gray-700 mb-2">
              نام کاربری
            </label>
            <input
              id="username"
              v-model="formData.username"
              type="text"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
              placeholder="نام کاربری خود را وارد کنید"
            >
          </div>

          <!-- Password -->
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700 mb-2">
              رمز عبور
            </label>
            <input
              id="password"
              v-model="formData.password"
              type="password"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
              placeholder="رمز عبور خود را وارد کنید"
            >
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="isLoading"
            class="w-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-3 px-4 rounded-lg font-medium hover:from-blue-700 hover:to-indigo-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span v-if="!isLoading">ورود</span>
            <span v-else class="flex items-center justify-center gap-2">
              <span class="material-symbols-outlined animate-spin">progress_activity</span>
              در حال ورود...
            </span>
          </button>
        </form>

        <!-- Register Link -->
        <div class="mt-6 text-center">
          <p class="text-sm text-gray-600">
            حساب کاربری ندارید؟
            <router-link to="/register" class="text-blue-600 hover:text-blue-700 font-medium">
              ثبت نام کنید
            </router-link>
          </p>
        </div>

        <!-- Back to Home -->
        <div class="mt-4 text-center">
          <router-link to="/" class="text-sm text-gray-500 hover:text-gray-700">
            بازگشت به صفحه اصلی
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const formData = ref({
  username: '',
  password: '',
})

const isLoading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

// Check for success message from registration
if (route.query.registered === 'true') {
  successMessage.value = 'ثبت نام با موفقیت انجام شد. لطفاً وارد شوید.'
}

async function handleLogin() {
  isLoading.value = true
  errorMessage.value = ''
  successMessage.value = ''

  const result = await authStore.login(formData.value.username, formData.value.password)

  if (result.success) {
    // Redirect to dashboard or home
    const redirect = route.query.redirect as string || '/'
    router.push(redirect)
  } else {
    errorMessage.value = result.error || 'خطا در ورود'
  }

  isLoading.value = false
}
</script>
