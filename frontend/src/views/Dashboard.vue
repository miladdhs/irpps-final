<template>
  <div class="min-h-screen bg-gray-50 px-4 py-8">
    <div class="mx-auto max-w-7xl">
      <div class="mb-6 rounded-2xl bg-white p-6 shadow-sm">
        <div class="flex flex-wrap items-center justify-between gap-4">
          <div class="flex items-center gap-4">
            <div v-if="profileImage" class="h-20 w-20 overflow-hidden rounded-full border-4 border-blue-100">
              <img :src="profileImage" :alt="greeting" class="h-full w-full object-cover">
            </div>
            <div v-else class="flex h-20 w-20 items-center justify-center rounded-full bg-gray-100">
              <img src="/iconly/Svg/Light/Profile.svg" alt="" aria-hidden="true" class="h-10 w-10 opacity-60">
            </div>
            <div>
              <h1 class="text-2xl font-bold text-gray-900">{{ greeting }}</h1>
              <p class="text-sm text-gray-600">{{ authStore.user?.email }}</p>
              <p class="text-xs text-gray-500">کد ملی: {{ authStore.user?.username }}</p>
            </div>
          </div>

          <div class="flex flex-wrap items-center gap-3">
            <router-link
              to="/profile"
              class="flex items-center gap-2 rounded-lg bg-blue-600 px-4 py-2 text-sm font-medium text-white transition hover:bg-blue-700"
            >
              <span class="material-symbols-outlined text-sm">description</span>
              رزومه و پروفایل
            </router-link>
            <button
              @click="handleLogout"
              class="flex items-center gap-2 rounded-lg px-4 py-2 text-red-600 transition hover:bg-red-50"
            >
              <span class="material-symbols-outlined">logout</span>
              خروج
            </button>
          </div>
        </div>
      </div>

      <div class="mb-6 rounded-2xl bg-white shadow-sm">
        <div class="flex overflow-x-auto border-b border-gray-200">
          <button
            @click="activeTab = 'profile'"
            :class="[
              'flex items-center gap-2 whitespace-nowrap px-6 py-4 text-sm font-medium transition-colors',
              activeTab === 'profile' ? 'border-b-2 border-blue-600 bg-blue-50 text-blue-600' : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
            ]"
          >
            <span class="material-symbols-outlined text-sm">person</span>
            اطلاعات حساب
          </button>

          <template v-if="authStore.isAdmin">
            <button
              @click="activeTab = 'news'"
              :class="[
                'flex items-center gap-2 whitespace-nowrap px-6 py-4 text-sm font-medium transition-colors',
                activeTab === 'news' ? 'border-b-2 border-purple-600 bg-purple-50 text-purple-600' : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
              ]"
            >
              <span class="material-symbols-outlined text-sm">newspaper</span>
              مدیریت اخبار
            </button>
            <button
              @click="activeTab = 'announcements'"
              :class="[
                'flex items-center gap-2 whitespace-nowrap px-6 py-4 text-sm font-medium transition-colors',
                activeTab === 'announcements' ? 'border-b-2 border-purple-600 bg-purple-50 text-purple-600' : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
              ]"
            >
              <span class="material-symbols-outlined text-sm">campaign</span>
              اطلاعیه‌ها
            </button>
            <button
              @click="activeTab = 'events'"
              :class="[
                'flex items-center gap-2 whitespace-nowrap px-6 py-4 text-sm font-medium transition-colors',
                activeTab === 'events' ? 'border-b-2 border-purple-600 bg-purple-50 text-purple-600' : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
              ]"
            >
              <span class="material-symbols-outlined text-sm">event</span>
              رویدادها
            </button>
            <button
              @click="activeTab = 'members'"
              :class="[
                'flex items-center gap-2 whitespace-nowrap px-6 py-4 text-sm font-medium transition-colors',
                activeTab === 'members' ? 'border-b-2 border-purple-600 bg-purple-50 text-purple-600' : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
              ]"
            >
              <span class="material-symbols-outlined text-sm">group</span>
              اعضا
            </button>
          </template>
        </div>
      </div>

      <div v-show="activeTab === 'profile'" class="rounded-2xl bg-white p-6 shadow-sm">
        <h3 class="mb-6 flex items-center gap-2 text-xl font-bold">
          <span class="material-symbols-outlined text-blue-600">person</span>
          اطلاعات شخصی
        </h3>

        <div class="mb-6 rounded-xl border border-blue-100 bg-blue-50 p-5">
          <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
            <div>
              <div class="text-sm font-bold text-blue-900">بخش رزومه</div>
              <div class="mt-1 text-sm text-blue-700">
                برای ویرایش تحصیلات، سوابق کاری، تخصص‌ها، محل کار و سایر بخش‌های رزومه روی دکمه زیر بزنید.
              </div>
            </div>
            <router-link
              to="/profile"
              class="inline-flex items-center justify-center gap-2 rounded-lg bg-blue-600 px-5 py-3 text-sm font-medium text-white transition hover:bg-blue-700"
            >
              <span class="material-symbols-outlined text-sm">edit_note</span>
              باز کردن صفحه رزومه
            </router-link>
          </div>
        </div>

        <div v-if="personalInfoMessage" :class="['mb-6 rounded-lg p-4', personalInfoError ? 'bg-red-50 text-red-600' : 'bg-green-50 text-green-600']">
          {{ personalInfoMessage }}
        </div>

        <div class="mb-6 rounded-xl border border-gray-200 p-5">
          <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
            <div class="flex items-center gap-4">
              <div v-if="profileImage" class="h-24 w-24 overflow-hidden rounded-full border-4 border-blue-100">
                <img :src="profileImage" :alt="greeting" class="h-full w-full object-cover" @error="handleProfileImageError">
              </div>
              <div v-else class="flex h-24 w-24 items-center justify-center rounded-full bg-gray-100">
                <img src="/iconly/Svg/Light/Profile.svg" alt="" aria-hidden="true" class="h-14 w-14 opacity-60">
              </div>
              <div class="text-sm text-gray-500">
                عکس پروفایل شما در کارت اعضا و پنل کاربری نمایش داده می‌شود.
              </div>
            </div>
            <div class="flex flex-col gap-3 md:w-64">
              <input ref="profileImageInput" type="file" accept="image/*" class="hidden" @change="handleProfileImageUpload">
              <button type="button" class="rounded-lg bg-blue-600 px-4 py-3 text-sm font-medium text-white transition hover:bg-blue-700 disabled:opacity-50" :disabled="profileImageLoading" @click="openProfileImagePicker">
                {{ profileImageLoading ? 'در حال آپلود...' : 'تغییر عکس پروفایل' }}
              </button>
              <button type="button" class="rounded-lg border border-gray-300 px-4 py-3 text-sm font-medium text-gray-700 transition hover:bg-gray-50 disabled:opacity-50" :disabled="profileImageLoading || !profileImage" @click="deleteProfileImage">
                حذف عکس
              </button>
            </div>
          </div>
        </div>

        <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
          <div>
            <label class="mb-2 block text-sm font-medium text-gray-700">نام فارسی</label>
            <input v-model="personalInfo.first_name" type="text" class="w-full rounded-lg border border-gray-300 px-4 py-3 focus:ring-2 focus:ring-blue-500" placeholder="نام">
          </div>
          <div>
            <label class="mb-2 block text-sm font-medium text-gray-700">نام انگلیسی</label>
            <input v-model="personalInfo.last_name" type="text" class="w-full rounded-lg border border-gray-300 px-4 py-3 focus:ring-2 focus:ring-blue-500" placeholder="Full Name">
          </div>
          <div>
            <label class="mb-2 block text-sm font-medium text-gray-700">ایمیل</label>
            <input v-model="personalInfo.email" type="email" class="w-full rounded-lg border border-gray-300 px-4 py-3 focus:ring-2 focus:ring-blue-500" placeholder="email@example.com">
          </div>
          <div>
            <label class="mb-2 block text-sm font-medium text-gray-700">تلفن</label>
            <input v-model="personalInfo.phone" type="tel" class="w-full rounded-lg border border-gray-300 px-4 py-3 focus:ring-2 focus:ring-blue-500" placeholder="09123456789">
          </div>
        </div>
        <button
          @click="updatePersonalInfo"
          :disabled="personalInfoLoading"
          class="mt-6 rounded-lg bg-blue-600 px-6 py-3 text-white transition hover:bg-blue-700 disabled:opacity-50"
        >
          {{ personalInfoLoading ? 'در حال ذخیره...' : 'ذخیره تغییرات' }}
        </button>
      </div>

      <div v-if="authStore.isAdmin">
        <div v-show="activeTab === 'news'">
          <iframe src="/admin/news" class="w-full rounded-2xl border-0 bg-white shadow-sm" style="height: calc(100vh - 280px); min-height: 700px;"></iframe>
        </div>
        <div v-show="activeTab === 'announcements'">
          <iframe src="/admin/announcements" class="w-full rounded-2xl border-0 bg-white shadow-sm" style="height: calc(100vh - 280px); min-height: 700px;"></iframe>
        </div>
        <div v-show="activeTab === 'events'">
          <iframe src="/admin/events" class="w-full rounded-2xl border-0 bg-white shadow-sm" style="height: calc(100vh - 280px); min-height: 700px;"></iframe>
        </div>
        <div v-show="activeTab === 'members'">
          <iframe src="/admin/members" class="w-full rounded-2xl border-0 bg-white shadow-sm" style="height: calc(100vh - 280px); min-height: 700px;"></iframe>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { getApiUrl } from '@/utils/api'

const router = useRouter()
const authStore = useAuthStore()

const activeTab = ref('profile')
const profileImage = ref('')
const profileImageInput = ref<HTMLInputElement | null>(null)
const profileImageLoading = ref(false)
const personalInfoLoading = ref(false)
const personalInfoMessage = ref('')
const personalInfoError = ref(false)

const personalInfo = ref({
  first_name: '',
  last_name: '',
  email: '',
  phone: '',
})

const greeting = computed(() => {
  const name = personalInfo.value.first_name || authStore.user?.username || 'کاربر'
  return `سلام، ${name}`
})

async function fetchProfile() {
  try {
    const response = await fetch(getApiUrl('/api/accounts/profile/'), {
      credentials: 'include',
    })
    if (!response.ok) throw new Error('خطا در دریافت اطلاعات')

    const data = await response.json()
    if (data.success && data.user) {
      personalInfo.value = {
        first_name: data.user.first_name || '',
        last_name: data.user.last_name || '',
        email: data.user.email || '',
        phone: data.user.phone || '',
      }

      if (data.user.profile_image) {
        profileImage.value = data.user.profile_image.startsWith('http')
          ? data.user.profile_image
          : getApiUrl(data.user.profile_image)
      } else {
        profileImage.value = ''
      }
    }
  } catch (error) {
    console.error('Error fetching profile:', error)
  }
}

async function updatePersonalInfo() {
  personalInfoLoading.value = true
  personalInfoMessage.value = ''
  personalInfoError.value = false

  try {
    const response = await fetch(getApiUrl('/api/accounts/profile/update/'), {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify(personalInfo.value),
    })

    const data = await response.json()
    if (data.success) {
      personalInfoMessage.value = 'اطلاعات با موفقیت به‌روزرسانی شد'
      if (authStore.user) {
        authStore.user.first_name = personalInfo.value.first_name
        authStore.user.last_name = personalInfo.value.last_name
        authStore.user.email = personalInfo.value.email
        authStore.user.phone = personalInfo.value.phone
      }
    } else {
      personalInfoMessage.value = data.errors || 'خطا در به‌روزرسانی'
      personalInfoError.value = true
    }
  } catch (error) {
    personalInfoMessage.value = 'خطا در ارتباط با سرور'
    personalInfoError.value = true
  } finally {
    personalInfoLoading.value = false
  }
}

async function handleLogout() {
  await authStore.logout()
  router.push('/')
}

function openProfileImagePicker() {
  profileImageInput.value?.click()
}

async function handleProfileImageUpload(event: Event) {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  if (!file) return

  profileImageLoading.value = true
  personalInfoMessage.value = ''
  personalInfoError.value = false

  const result = await authStore.uploadProfileImage(file)
  if (result.success) {
    profileImage.value = authStore.user?.profile_image
      ? (authStore.user.profile_image.startsWith('http') ? authStore.user.profile_image : getApiUrl(authStore.user.profile_image))
      : ''
    personalInfoMessage.value = result.message || 'عکس پروفایل با موفقیت به‌روزرسانی شد'
  } else {
    personalInfoMessage.value = result.error || 'خطا در آپلود عکس پروفایل'
    personalInfoError.value = true
  }

  target.value = ''
  profileImageLoading.value = false
}

async function deleteProfileImage() {
  profileImageLoading.value = true
  personalInfoMessage.value = ''
  personalInfoError.value = false

  const result = await authStore.deleteProfileImage()
  if (result.success) {
    profileImage.value = ''
    personalInfoMessage.value = result.message || 'عکس پروفایل حذف شد'
  } else {
    personalInfoMessage.value = result.error || 'خطا در حذف عکس پروفایل'
    personalInfoError.value = true
  }

  profileImageLoading.value = false
}

function handleProfileImageError() {
  profileImage.value = ''
}

onMounted(fetchProfile)
</script>
