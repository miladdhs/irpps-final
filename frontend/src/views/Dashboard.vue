<template>
  <div class="min-h-screen bg-gray-50 py-8 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <div class="bg-white rounded-2xl shadow-sm p-6 mb-6">
        <div class="flex items-center justify-between flex-wrap gap-4">
          <div class="flex items-center gap-4">
            <div v-if="profileImage" class="w-20 h-20 rounded-full overflow-hidden border-4 border-blue-100">
              <img :src="profileImage" :alt="greeting" class="w-full h-full object-cover" />
            </div>
            <div v-else class="w-20 h-20 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center text-white text-2xl font-bold">
              {{ userInitials }}
            </div>
            <div>
              <h1 class="text-2xl font-bold text-gray-900">{{ greeting }}</h1>
              <p class="text-gray-600 text-sm">{{ authStore.user?.email }}</p>
              <p class="text-xs text-gray-500">کد ملی: {{ authStore.user?.username }}</p>
            </div>
          </div>
          <button
            @click="handleLogout"
            class="flex items-center gap-2 px-4 py-2 text-red-600 hover:bg-red-50 rounded-lg transition"
          >
            <span class="material-symbols-outlined">logout</span>
            خروج
          </button>
        </div>
      </div>

      <!-- Tabs -->
      <div class="bg-white rounded-2xl shadow-sm mb-6">
        <div class="flex border-b border-gray-200 overflow-x-auto">
          <button
            @click="activeTab = 'profile'"
            :class="[
              'px-6 py-4 font-medium text-sm whitespace-nowrap transition-colors flex items-center gap-2',
              activeTab === 'profile' ? 'text-blue-600 border-b-2 border-blue-600 bg-blue-50' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
            ]"
          >
            <span class="material-symbols-outlined text-sm">person</span>
            اطلاعات حساب
          </button>
          
          <template v-if="authStore.isAdmin">
            <button
              @click="activeTab = 'news'"
              :class="[
                'px-6 py-4 font-medium text-sm whitespace-nowrap transition-colors flex items-center gap-2',
                activeTab === 'news' ? 'text-purple-600 border-b-2 border-purple-600 bg-purple-50' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
              ]"
            >
              <span class="material-symbols-outlined text-sm">newspaper</span>
              مدیریت اخبار
            </button>
            <button
              @click="activeTab = 'announcements'"
              :class="[
                'px-6 py-4 font-medium text-sm whitespace-nowrap transition-colors flex items-center gap-2',
                activeTab === 'announcements' ? 'text-purple-600 border-b-2 border-purple-600 bg-purple-50' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
              ]"
            >
              <span class="material-symbols-outlined text-sm">campaign</span>
              اطلاعیه‌ها
            </button>
            <button
              @click="activeTab = 'events'"
              :class="[
                'px-6 py-4 font-medium text-sm whitespace-nowrap transition-colors flex items-center gap-2',
                activeTab === 'events' ? 'text-purple-600 border-b-2 border-purple-600 bg-purple-50' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
              ]"
            >
              <span class="material-symbols-outlined text-sm">event</span>
              رویدادها
            </button>
            <button
              @click="activeTab = 'members'"
              :class="[
                'px-6 py-4 font-medium text-sm whitespace-nowrap transition-colors flex items-center gap-2',
                activeTab === 'members' ? 'text-purple-600 border-b-2 border-purple-600 bg-purple-50' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
              ]"
            >
              <span class="material-symbols-outlined text-sm">group</span>
              اعضا
            </button>
          </template>
        </div>
      </div>

      <!-- Profile Tab -->
      <div v-show="activeTab === 'profile'" class="bg-white rounded-2xl shadow-sm p-6">
        <h3 class="text-xl font-bold mb-6 flex items-center gap-2">
          <span class="material-symbols-outlined text-blue-600">person</span>
          اطلاعات شخصی
        </h3>
        
        <div v-if="personalInfoMessage" :class="['p-4 rounded-lg mb-6', personalInfoError ? 'bg-red-50 text-red-600' : 'bg-green-50 text-green-600']">
          {{ personalInfoMessage }}
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">نام فارسی</label>
            <input v-model="personalInfo.first_name" type="text" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500" placeholder="نام" />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">نام انگلیسی</label>
            <input v-model="personalInfo.last_name" type="text" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500" placeholder="Full Name" />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">ایمیل</label>
            <input v-model="personalInfo.email" type="email" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500" placeholder="email@example.com" />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">تلفن</label>
            <input v-model="personalInfo.phone" type="tel" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500" placeholder="09123456789" />
          </div>
        </div>
        <button 
          @click="updatePersonalInfo" 
          :disabled="personalInfoLoading"
          class="mt-6 px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition disabled:opacity-50"
        >
          {{ personalInfoLoading ? 'در حال ذخیره...' : 'ذخیره تغییرات' }}
        </button>
      </div>

      <!-- Admin Tabs (iframe) -->
      <div v-if="authStore.isAdmin">
        <div v-show="activeTab === 'news'">
          <iframe src="/admin/news" class="w-full border-0 rounded-2xl shadow-sm bg-white" style="height: calc(100vh - 280px); min-height: 700px;"></iframe>
        </div>
        <div v-show="activeTab === 'announcements'">
          <iframe src="/admin/announcements" class="w-full border-0 rounded-2xl shadow-sm bg-white" style="height: calc(100vh - 280px); min-height: 700px;"></iframe>
        </div>
        <div v-show="activeTab === 'events'">
          <iframe src="/admin/events" class="w-full border-0 rounded-2xl shadow-sm bg-white" style="height: calc(100vh - 280px); min-height: 700px;"></iframe>
        </div>
        <div v-show="activeTab === 'members'">
          <iframe src="/admin/members" class="w-full border-0 rounded-2xl shadow-sm bg-white" style="height: calc(100vh - 280px); min-height: 700px;"></iframe>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { getApiUrl } from '@/utils/api'

const router = useRouter()
const authStore = useAuthStore()

const activeTab = ref('profile')
const profileImage = ref('')
const personalInfoLoading = ref(false)
const personalInfoMessage = ref('')
const personalInfoError = ref(false)

const personalInfo = ref({
  first_name: '',
  last_name: '',
  email: '',
  phone: ''
})

const userInitials = computed(() => {
  if (!authStore.user) return 'U'
  const firstName = personalInfo.value.first_name || ''
  const lastName = personalInfo.value.last_name || ''
  return (firstName.charAt(0) + lastName.charAt(0)).toUpperCase() || authStore.user.username.charAt(0).toUpperCase()
})

const greeting = computed(() => {
  const name = personalInfo.value.first_name || authStore.user?.username || 'کاربر'
  return `سلام، ${name}`
})

async function fetchProfile() {
  try {
    const response = await fetch(getApiUrl('/api/accounts/profile/'), {
      credentials: 'include'
    })

    if (!response.ok) throw new Error('خطا در دریافت اطلاعات')

    const data = await response.json()
    if (data.success && data.user) {
      personalInfo.value = {
        first_name: data.user.first_name || '',
        last_name: data.user.last_name || '',
        email: data.user.email || '',
        phone: data.user.phone || ''
      }

      if (data.user.profile_image) {
        profileImage.value = data.user.profile_image.startsWith('http') 
          ? data.user.profile_image 
          : getApiUrl(data.user.profile_image)
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
      body: JSON.stringify(personalInfo.value)
    })

    const data = await response.json()
    if (data.success) {
      personalInfoMessage.value = 'اطلاعات با موفقیت به‌روزرسانی شد'
      personalInfoError.value = false
      if (authStore.user) {
        authStore.user.first_name = personalInfo.value.first_name
        authStore.user.last_name = personalInfo.value.last_name
        authStore.user.email = personalInfo.value.email
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

onMounted(() => {
  fetchProfile()
})
</script>
