<template>
  <div class="min-h-screen bg-gray-50 px-4 py-12">
    <div class="mx-auto max-w-4xl">
      <div class="mb-8">
        <router-link to="/dashboard" class="mb-4 inline-flex items-center gap-2 text-gray-600 hover:text-gray-900">
          <span class="material-symbols-outlined">arrow_back</span>
          بازگشت به داشبورد
        </router-link>
        <h1 class="text-3xl font-bold text-gray-900">پروفایل من</h1>
      </div>

      <div v-if="successMessage" class="mb-6 rounded-lg border border-green-200 bg-green-50 px-4 py-3 text-green-700">
        {{ successMessage }}
      </div>
      <div v-if="errorMessage" class="mb-6 rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-red-700">
        {{ errorMessage }}
      </div>

      <div class="mb-6 grid gap-6 lg:grid-cols-[320px,1fr]">
        <div class="rounded-2xl bg-white p-8 shadow-sm">
          <h2 class="mb-6 text-xl font-bold text-gray-900">عکس پروفایل</h2>
          <div class="flex flex-col items-center gap-4">
            <div class="flex h-40 w-40 items-center justify-center overflow-hidden rounded-full bg-gray-100">
              <img
                v-if="currentProfileImage && !imageBroken"
                :src="currentProfileImage"
                alt="Profile"
                class="h-full w-full object-cover"
                @error="handleProfileImageError"
              >
              <span v-else class="material-symbols-outlined text-7xl text-gray-400">person</span>
            </div>

            <input
              ref="imageInput"
              type="file"
              accept="image/*"
              class="hidden"
              @change="handleFileSelection"
            >

            <div class="w-full space-y-3">
              <button
                type="button"
                class="w-full rounded-lg bg-blue-600 px-4 py-3 font-medium text-white transition hover:bg-blue-700 disabled:opacity-50"
                :disabled="isImageLoading"
                @click="openFilePicker"
              >
                {{ isImageLoading ? 'در حال آپلود...' : 'انتخاب یا تغییر عکس' }}
              </button>
              <button
                type="button"
                class="w-full rounded-lg border border-gray-300 px-4 py-3 font-medium text-gray-700 transition hover:bg-gray-50 disabled:opacity-50"
                :disabled="isImageLoading || !authStore.user?.profile_image"
                @click="handleDeleteProfileImage"
              >
                حذف عکس
              </button>
              <p class="text-sm text-gray-500">
                اگر عکس نداشته باشید، آیکون پیش‌فرض در کارت اعضا نمایش داده می‌شود.
              </p>
            </div>
          </div>
        </div>

        <div class="rounded-2xl bg-white p-8 shadow-sm">
          <h2 class="mb-6 text-xl font-bold text-gray-900">اطلاعات شخصی</h2>
          <form class="space-y-6" @submit.prevent="handleUpdateProfile">
            <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
              <div>
                <label class="mb-2 block text-sm font-medium text-gray-700">نام (فارسی)</label>
                <input
                  v-model="profileForm.first_name"
                  type="text"
                  class="w-full rounded-lg border border-gray-300 px-4 py-3 focus:border-transparent focus:ring-2 focus:ring-blue-500"
                >
              </div>
              <div>
                <label class="mb-2 block text-sm font-medium text-gray-700">نام کامل دوم</label>
                <input
                  v-model="profileForm.last_name"
                  type="text"
                  class="w-full rounded-lg border border-gray-300 px-4 py-3 focus:border-transparent focus:ring-2 focus:ring-blue-500"
                >
              </div>
              <div>
                <label class="mb-2 block text-sm font-medium text-gray-700">ایمیل</label>
                <input
                  v-model="profileForm.email"
                  type="email"
                  class="w-full rounded-lg border border-gray-300 px-4 py-3 focus:border-transparent focus:ring-2 focus:ring-blue-500"
                >
              </div>
              <div>
                <label class="mb-2 block text-sm font-medium text-gray-700">شماره تماس</label>
                <input
                  v-model="profileForm.phone"
                  type="tel"
                  class="w-full rounded-lg border border-gray-300 px-4 py-3 focus:border-transparent focus:ring-2 focus:ring-blue-500"
                >
              </div>
            </div>

            <button
              type="submit"
              :disabled="isLoading"
              class="rounded-lg bg-blue-600 px-6 py-3 font-medium text-white transition hover:bg-blue-700 disabled:opacity-50"
            >
              <span v-if="!isLoading">ذخیره تغییرات</span>
              <span v-else>در حال ذخیره...</span>
            </button>
          </form>
        </div>
      </div>

      <div class="rounded-2xl bg-white p-8 shadow-sm">
        <h2 class="mb-6 text-xl font-bold text-gray-900">اطلاعات حساب</h2>
        <div class="space-y-4">
          <div class="flex items-center justify-between border-b border-gray-100 py-3">
            <span class="text-gray-600">نام کاربری</span>
            <span class="font-medium">{{ authStore.user?.username }}</span>
          </div>
          <div class="flex items-center justify-between border-b border-gray-100 py-3">
            <span class="text-gray-600">تاریخ عضویت</span>
            <span class="font-medium">{{ formatDate(authStore.user?.date_joined) }}</span>
          </div>
          <div class="flex items-center justify-between py-3">
            <span class="text-gray-600">نقش</span>
            <span class="inline-flex items-center rounded-full px-3 py-1 text-sm font-medium" :class="authStore.isAdmin ? 'bg-purple-100 text-purple-700' : 'bg-blue-100 text-blue-700'">
              {{ authStore.isAdmin ? 'مدیر' : 'کاربر' }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

const profileForm = ref({
  first_name: '',
  last_name: '',
  email: '',
  phone: '',
})

const isLoading = ref(false)
const isImageLoading = ref(false)
const successMessage = ref('')
const errorMessage = ref('')
const imageInput = ref<HTMLInputElement | null>(null)
const imageBroken = ref(false)

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

const currentProfileImage = computed(() => {
  const image = authStore.user?.profile_image
  if (!image) {
    return ''
  }
  return image.startsWith('http://') || image.startsWith('https://') || image.startsWith('/')
    ? image
    : `/${image}`
})

async function handleUpdateProfile() {
  isLoading.value = true
  successMessage.value = ''
  errorMessage.value = ''

  const result = await authStore.updateProfile(profileForm.value)

  if (result.success) {
    successMessage.value = result.message || 'پروفایل با موفقیت به‌روزرسانی شد'
  } else {
    errorMessage.value = result.error || 'خطا در به‌روزرسانی پروفایل'
  }

  isLoading.value = false
}

function openFilePicker() {
  imageInput.value?.click()
}

async function handleFileSelection(event: Event) {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  if (!file) {
    return
  }

  isImageLoading.value = true
  imageBroken.value = false
  successMessage.value = ''
  errorMessage.value = ''

  const result = await authStore.uploadProfileImage(file)
  if (result.success) {
    successMessage.value = result.message || 'عکس پروفایل با موفقیت به‌روزرسانی شد'
  } else {
    errorMessage.value = result.error || 'خطا در آپلود عکس پروفایل'
  }

  target.value = ''
  isImageLoading.value = false
}

async function handleDeleteProfileImage() {
  isImageLoading.value = true
  successMessage.value = ''
  errorMessage.value = ''

  const result = await authStore.deleteProfileImage()
  if (result.success) {
    imageBroken.value = false
    successMessage.value = result.message || 'عکس پروفایل حذف شد'
  } else {
    errorMessage.value = result.error || 'خطا در حذف عکس پروفایل'
  }

  isImageLoading.value = false
}

function handleProfileImageError() {
  imageBroken.value = true
}

function formatDate(dateString?: string) {
  if (!dateString) return '-'
  const date = new Date(dateString)
  return new Intl.DateTimeFormat('fa-IR').format(date)
}
</script>
