<template>
  <div class="min-h-screen bg-gray-50 py-12 px-4">
    <div class="max-w-4xl mx-auto">
      <!-- Header -->
      <div class="mb-8">
        <router-link to="/dashboard" class="inline-flex items-center gap-2 text-gray-600 hover:text-gray-900 mb-4">
          <span class="material-symbols-outlined">arrow_back</span>
          بازگشت به داشبورد
        </router-link>
        <h1 class="text-3xl font-bold text-gray-900">پروفایل من</h1>
      </div>

      <!-- Success/Error Messages -->
      <div v-if="successMessage" class="bg-green-50 border border-green-200 text-green-700 px-4 py-3 rounded-lg mb-6">
        {{ successMessage }}
      </div>
      <div v-if="errorMessage" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg mb-6">
        {{ errorMessage }}
      </div>

      <!-- Profile Info -->
      <div class="bg-white rounded-2xl shadow-sm p-8 mb-6">
        <h2 class="text-xl font-bold text-gray-900 mb-6">اطلاعات شخصی</h2>
        <form @submit.prevent="handleUpdateProfile" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">نام (فارسی)</label>
              <input
                v-model="profileForm.first_name"
                type="text"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">نام کامل (انگلیسی)</label>
              <input
                v-model="profileForm.last_name"
                type="text"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">ایمیل</label>
              <input
                v-model="profileForm.email"
                type="email"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">شماره تماس</label>
              <input
                v-model="profileForm.phone"
                type="tel"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
            </div>
          </div>
          <button
            type="submit"
            :disabled="isLoading"
            class="bg-blue-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-blue-700 transition disabled:opacity-50"
          >
            <span v-if="!isLoading">ذخیره تغییرات</span>
            <span v-else>در حال ذخیره...</span>
          </button>
        </form>
      </div>

      <!-- Account Info -->
      <div class="bg-white rounded-2xl shadow-sm p-8">
        <h2 class="text-xl font-bold text-gray-900 mb-6">اطلاعات حساب</h2>
        <div class="space-y-4">
          <div class="flex justify-between items-center py-3 border-b border-gray-100">
            <span class="text-gray-600">نام کاربری</span>
            <span class="font-medium">{{ authStore.user?.username }}</span>
          </div>
          <div class="flex justify-between items-center py-3 border-b border-gray-100">
            <span class="text-gray-600">تاریخ عضویت</span>
            <span class="font-medium">{{ formatDate(authStore.user?.date_joined) }}</span>
          </div>
          <div class="flex justify-between items-center py-3">
            <span class="text-gray-600">نقش</span>
            <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium" :class="authStore.isAdmin ? 'bg-purple-100 text-purple-700' : 'bg-blue-100 text-blue-700'">
              {{ authStore.isAdmin ? 'مدیر' : 'کاربر' }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

const profileForm = ref({
  first_name: '',
  last_name: '',
  email: '',
  phone: '',
})

const isLoading = ref(false)
const successMessage = ref('')
const errorMessage = ref('')

onMounted(() => {
  if (authStore.user) {
    profileForm.value = {
      first_name: authStore.user.first_name || '',
      last_name: authStore.user.last_name || '',
      email: authStore.user.email || '',
      phone: authStore.user.phone || '',
    }
  }
})

async function handleUpdateProfile() {
  isLoading.value = true
  successMessage.value = ''
  errorMessage.value = ''

  const result = await authStore.updateProfile(profileForm.value)

  if (result.success) {
    successMessage.value = result.message || 'پروفایل با موفقیت بروزرسانی شد'
  } else {
    errorMessage.value = result.error || 'خطا در بروزرسانی پروفایل'
  }

  isLoading.value = false
}

function formatDate(dateString?: string) {
  if (!dateString) return '-'
  const date = new Date(dateString)
  return new Intl.DateTimeFormat('fa-IR').format(date)
}
</script>
