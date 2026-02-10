<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-2xl mx-auto">
      <!-- Logo and Title -->
      <div class="text-center mb-8">
        <img src="/img/logo.png" alt="لوگو" class="h-20 mx-auto mb-4">
        <h2 class="text-3xl font-bold text-gray-900 mb-2">ثبت نام</h2>
        <p class="text-gray-600">عضویت در انجمن علمی ریه کودکان</p>
      </div>

      <!-- Register Form -->
      <div class="bg-white rounded-2xl shadow-xl p-8">
        <form @submit.prevent="handleRegister" class="space-y-6">
          <!-- Error Message -->
          <div v-if="errorMessage" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm">
            {{ errorMessage }}
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- First Name (Persian) -->
            <div>
              <label for="first_name" class="block text-sm font-medium text-gray-700 mb-2">
                نام (فارسی) *
              </label>
              <input
                id="first_name"
                v-model="formData.first_name"
                type="text"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                placeholder="نام فارسی"
              >
            </div>

            <!-- Last Name (English) -->
            <div>
              <label for="last_name" class="block text-sm font-medium text-gray-700 mb-2">
                نام کامل (انگلیسی) *
              </label>
              <input
                id="last_name"
                v-model="formData.last_name"
                type="text"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                placeholder="Full Name in English"
              >
            </div>

            <!-- Username -->
            <div>
              <label for="username" class="block text-sm font-medium text-gray-700 mb-2">
                نام کاربری *
              </label>
              <input
                id="username"
                v-model="formData.username"
                type="text"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                placeholder="نام کاربری"
              >
            </div>

            <!-- Email -->
            <div>
              <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
                ایمیل *
              </label>
              <input
                id="email"
                v-model="formData.email"
                type="email"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                placeholder="example@email.com"
              >
            </div>

            <!-- Phone -->
            <div>
              <label for="phone" class="block text-sm font-medium text-gray-700 mb-2">
                شماره تماس *
              </label>
              <input
                id="phone"
                v-model="formData.phone"
                type="tel"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                placeholder="09123456789"
              >
            </div>

            <!-- Password -->
            <div>
              <label for="password" class="block text-sm font-medium text-gray-700 mb-2">
                رمز عبور *
              </label>
              <input
                id="password"
                v-model="formData.password"
                type="password"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                placeholder="حداقل 8 کاراکتر"
              >
            </div>

            <!-- Confirm Password -->
            <div>
              <label for="password_confirm" class="block text-sm font-medium text-gray-700 mb-2">
                تکرار رمز عبور *
              </label>
              <input
                id="password_confirm"
                v-model="formData.password_confirm"
                type="password"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                placeholder="تکرار رمز عبور"
              >
            </div>
          </div>

          <!-- Info Note -->
          <div class="bg-blue-50 border border-blue-200 text-blue-700 px-4 py-3 rounded-lg text-sm">
            <span class="material-symbols-outlined text-lg align-middle ml-2">info</span>
            پس از ثبت نام، حساب شما توسط مدیریت بررسی و تایید خواهد شد.
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="isLoading"
            class="w-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-3 px-4 rounded-lg font-medium hover:from-blue-700 hover:to-indigo-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span v-if="!isLoading">ثبت نام</span>
            <span v-else class="flex items-center justify-center gap-2">
              <span class="material-symbols-outlined animate-spin">progress_activity</span>
              در حال ثبت نام...
            </span>
          </button>
        </form>

        <!-- Login Link -->
        <div class="mt-6 text-center">
          <p class="text-sm text-gray-600">
            قبلاً ثبت نام کرده‌اید؟
            <router-link to="/login" class="text-blue-600 hover:text-blue-700 font-medium">
              وارد شوید
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
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

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

async function handleRegister() {
  isLoading.value = true
  errorMessage.value = ''

  // Validate passwords match
  if (formData.value.password !== formData.value.password_confirm) {
    errorMessage.value = 'رمزهای عبور مطابقت ندارند'
    isLoading.value = false
    return
  }

  const result = await authStore.register(formData.value)

  if (result.success) {
    // Show success message and redirect to login
    router.push({ path: '/login', query: { registered: 'true' } })
  } else {
    errorMessage.value = result.error || 'خطا در ثبت نام'
  }

  isLoading.value = false
}
</script>
