<template>
  <div class="min-h-screen bg-gray-50 py-12 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- Header with Profile Image -->
      <div class="bg-white rounded-2xl shadow-sm p-8 mb-8">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-6">
            <!-- Profile Image -->
            <div class="relative">
              <div v-if="profileImage" class="w-24 h-24 rounded-full overflow-hidden border-4 border-blue-100">
                <img :src="profileImage" :alt="greeting" class="w-full h-full object-cover" />
              </div>
              <div v-else class="w-24 h-24 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center text-white text-3xl font-bold">
                {{ userInitials }}
              </div>
            </div>
            <div>
              <h1 class="text-2xl font-bold text-gray-900">{{ greeting }}</h1>
              <p class="text-gray-600">{{ authStore.user?.email }}</p>
              <p class="text-sm text-gray-500 mt-1">کد ملی: {{ authStore.user?.username }}</p>
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
      <div class="bg-white rounded-2xl shadow-sm mb-8">
        <div class="flex border-b border-gray-200">
          <button
            @click="activeTab = 'info'"
            :class="[
              'flex-1 px-6 py-4 text-center font-medium transition',
              activeTab === 'info' 
                ? 'text-blue-600 border-b-2 border-blue-600' 
                : 'text-gray-500 hover:text-gray-700'
            ]"
          >
            <span class="material-symbols-outlined text-xl align-middle ml-2">person</span>
            اطلاعات شخصی
          </button>
          <button
            @click="activeTab = 'photo'"
            :class="[
              'flex-1 px-6 py-4 text-center font-medium transition',
              activeTab === 'photo' 
                ? 'text-blue-600 border-b-2 border-blue-600' 
                : 'text-gray-500 hover:text-gray-700'
            ]"
          >
            <span class="material-symbols-outlined text-xl align-middle ml-2">photo_camera</span>
            عکس پروفایل
          </button>
          <button
            @click="activeTab = 'resume'"
            :class="[
              'flex-1 px-6 py-4 text-center font-medium transition',
              activeTab === 'resume' 
                ? 'text-blue-600 border-b-2 border-blue-600' 
                : 'text-gray-500 hover:text-gray-700'
            ]"
          >
            <span class="material-symbols-outlined text-xl align-middle ml-2">description</span>
            رزومه
          </button>
        </div>

        <!-- Tab Content -->
        <div class="p-8">
          <!-- Personal Info Tab -->
          <div v-if="activeTab === 'info'">
            <h2 class="text-xl font-bold text-gray-900 mb-6">ویرایش اطلاعات شخصی</h2>
            <form @submit.prevent="updatePersonalInfo" class="space-y-6">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">نام فارسی</label>
                  <input
                    v-model="personalInfo.first_name"
                    type="text"
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="نام خود را وارد کنید"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">نام انگلیسی</label>
                  <input
                    v-model="personalInfo.last_name"
                    type="text"
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="Full Name in English"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">ایمیل</label>
                  <input
                    v-model="personalInfo.email"
                    type="email"
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="email@example.com"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">تلفن</label>
                  <input
                    v-model="personalInfo.phone"
                    type="tel"
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="09123456789"
                  />
                </div>
              </div>

              <!-- Success/Error Messages -->
              <div v-if="personalInfoMessage" :class="[
                'p-4 rounded-lg',
                personalInfoError ? 'bg-red-50 text-red-600' : 'bg-green-50 text-green-600'
              ]">
                {{ personalInfoMessage }}
              </div>

              <button
                type="submit"
                :disabled="personalInfoLoading"
                class="w-full md:w-auto px-8 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span v-if="personalInfoLoading">در حال ذخیره...</span>
                <span v-else>ذخیره تغییرات</span>
              </button>
            </form>
          </div>

          <!-- Photo Upload Tab -->
          <div v-if="activeTab === 'photo'">
            <h2 class="text-xl font-bold text-gray-900 mb-6">مدیریت عکس پروفایل</h2>
            
            <!-- Current Photo -->
            <div class="mb-8 text-center">
              <div v-if="profileImage" class="inline-block">
                <img :src="profileImage" alt="Profile" class="w-48 h-48 rounded-full object-cover border-4 border-gray-200 mb-4" />
                <button
                  @click="deleteProfileImage"
                  :disabled="photoLoading"
                  class="block mx-auto px-6 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition disabled:opacity-50"
                >
                  <span v-if="photoLoading">در حال حذف...</span>
                  <span v-else>حذف عکس</span>
                </button>
              </div>
              <div v-else class="inline-block">
                <div class="w-48 h-48 rounded-full bg-gray-200 flex items-center justify-center text-gray-400 text-6xl mb-4 mx-auto">
                  <span class="material-symbols-outlined text-8xl">person</span>
                </div>
                <p class="text-gray-500">عکس پروفایل آپلود نشده است</p>
              </div>
            </div>

            <!-- Upload Form -->
            <form @submit.prevent="uploadProfileImage" class="max-w-md mx-auto">
              <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-2">انتخاب عکس جدید</label>
                <input
                  ref="fileInput"
                  type="file"
                  accept="image/*"
                  @change="handleFileSelect"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                />
                <p class="text-sm text-gray-500 mt-2">فرمت‌های مجاز: JPG, PNG, GIF</p>
              </div>

              <!-- Preview -->
              <div v-if="selectedFile" class="mb-6">
                <p class="text-sm font-medium text-gray-700 mb-2">پیش‌نمایش:</p>
                <img :src="previewUrl" alt="Preview" class="w-32 h-32 rounded-full object-cover border-2 border-gray-300 mx-auto" />
              </div>

              <!-- Success/Error Messages -->
              <div v-if="photoMessage" :class="[
                'p-4 rounded-lg mb-6',
                photoError ? 'bg-red-50 text-red-600' : 'bg-green-50 text-green-600'
              ]">
                {{ photoMessage }}
              </div>

              <button
                type="submit"
                :disabled="!selectedFile || photoLoading"
                class="w-full px-8 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span v-if="photoLoading">در حال آپلود...</span>
                <span v-else>آپلود عکس</span>
              </button>
            </form>
          </div>

          <!-- Resume Tab -->
          <div v-if="activeTab === 'resume'">
            <h2 class="text-xl font-bold text-gray-900 mb-6">ویرایش رزومه</h2>
            <form @submit.prevent="updateResume" class="space-y-6">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">تحصیلات</label>
                <textarea
                  v-model="resumeInfo.education"
                  rows="4"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="مثال: دکترای تخصصی ریه کودکان از دانشگاه تهران - 1395"
                ></textarea>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">مقالات و انتشارات</label>
                <textarea
                  v-model="resumeInfo.publications"
                  rows="4"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="لیست مقالات و انتشارات علمی خود را وارد کنید"
                ></textarea>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">جوایز و افتخارات</label>
                <textarea
                  v-model="resumeInfo.awards"
                  rows="3"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="جوایز و افتخارات علمی خود را وارد کنید"
                ></textarea>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">گواهینامه‌ها</label>
                <textarea
                  v-model="resumeInfo.certifications"
                  rows="3"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="گواهینامه‌ها و مدارک تخصصی خود را وارد کنید"
                ></textarea>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">علایق پژوهشی</label>
                <textarea
                  v-model="resumeInfo.research_interests"
                  rows="3"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="حوزه‌های علاقه‌مندی پژوهشی خود را وارد کنید"
                ></textarea>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">زبان‌ها</label>
                <input
                  v-model="resumeInfo.languages"
                  type="text"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="مثال: فارسی، انگلیسی، عربی"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">بیوگرافی</label>
                <textarea
                  v-model="resumeInfo.bio"
                  rows="4"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="توضیحات کوتاهی درباره خود و فعالیت‌های حرفه‌ای خود بنویسید"
                ></textarea>
              </div>

              <!-- Success/Error Messages -->
              <div v-if="resumeMessage" :class="[
                'p-4 rounded-lg',
                resumeError ? 'bg-red-50 text-red-600' : 'bg-green-50 text-green-600'
              ]">
                {{ resumeMessage }}
              </div>

              <button
                type="submit"
                :disabled="resumeLoading"
                class="w-full md:w-auto px-8 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span v-if="resumeLoading">در حال ذخیره...</span>
                <span v-else>ذخیره رزومه</span>
              </button>
            </form>
          </div>
        </div>
      </div>

      <!-- Quick Links -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <router-link
          to="/team"
          class="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition group"
        >
          <div class="w-12 h-12 rounded-lg bg-blue-100 text-blue-600 flex items-center justify-center mb-4 group-hover:scale-110 transition">
            <span class="material-symbols-outlined text-2xl">groups</span>
          </div>
          <h3 class="font-bold text-gray-900 mb-1">مشاهده اعضا</h3>
          <p class="text-sm text-gray-600">مشاهده پروفایل سایر اعضا</p>
        </router-link>

        <router-link
          to="/events"
          class="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition group"
        >
          <div class="w-12 h-12 rounded-lg bg-green-100 text-green-600 flex items-center justify-center mb-4 group-hover:scale-110 transition">
            <span class="material-symbols-outlined text-2xl">event</span>
          </div>
          <h3 class="font-bold text-gray-900 mb-1">رویدادها</h3>
          <p class="text-sm text-gray-600">مشاهده و ثبت نام</p>
        </router-link>

        <router-link
          to="/news"
          class="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition group"
        >
          <div class="w-12 h-12 rounded-lg bg-purple-100 text-purple-600 flex items-center justify-center mb-4 group-hover:scale-110 transition">
            <span class="material-symbols-outlined text-2xl">newspaper</span>
          </div>
          <h3 class="font-bold text-gray-900 mb-1">اخبار</h3>
          <p class="text-sm text-gray-600">آخرین اخبار انجمن</p>
        </router-link>

        <router-link
          to="/education/doctors"
          class="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition group"
        >
          <div class="w-12 h-12 rounded-lg bg-orange-100 text-orange-600 flex items-center justify-center mb-4 group-hover:scale-110 transition">
            <span class="material-symbols-outlined text-2xl">school</span>
          </div>
          <h3 class="font-bold text-gray-900 mb-1">آموزش</h3>
          <p class="text-sm text-gray-600">منابع آموزشی</p>
        </router-link>
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

const activeTab = ref('info')
const profileImage = ref('')
const selectedFile = ref<File | null>(null)
const previewUrl = ref('')
const fileInput = ref<HTMLInputElement | null>(null)

const personalInfo = ref({
  first_name: '',
  last_name: '',
  email: '',
  phone: ''
})
const personalInfoLoading = ref(false)
const personalInfoMessage = ref('')
const personalInfoError = ref(false)

const photoLoading = ref(false)
const photoMessage = ref('')
const photoError = ref(false)

const resumeInfo = ref({
  education: '',
  publications: '',
  awards: '',
  certifications: '',
  research_interests: '',
  languages: '',
  bio: ''
})
const resumeLoading = ref(false)
const resumeMessage = ref('')
const resumeError = ref(false)

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

      resumeInfo.value = {
        education: data.user.education || '',
        publications: data.user.publications || '',
        awards: data.user.awards || '',
        certifications: data.user.certifications || '',
        research_interests: data.user.research_interests || '',
        languages: data.user.languages || '',
        bio: data.user.bio || ''
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
    const response = await fetch(getApiUrl('/api/accounts/update-profile/'), {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
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
      personalInfoMessage.value = data.errors || 'خطا در به‌روزرسانی اطلاعات'
      personalInfoError.value = true
    }
  } catch (error) {
    personalInfoMessage.value = 'خطا در ارتباط با سرور'
    personalInfoError.value = true
  } finally {
    personalInfoLoading.value = false
  }
}

function handleFileSelect(event: Event) {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  
  if (file) {
    selectedFile.value = file
    previewUrl.value = URL.createObjectURL(file)
  }
}

async function uploadProfileImage() {
  if (!selectedFile.value) return

  photoLoading.value = true
  photoMessage.value = ''
  photoError.value = false

  try {
    const formData = new FormData()
    formData.append('profile_image', selectedFile.value)

    const response = await fetch(getApiUrl('/api/accounts/upload-profile-image/'), {
      method: 'POST',
      credentials: 'include',
      body: formData
    })

    const data = await response.json()

    if (data.success) {
      photoMessage.value = 'عکس با موفقیت آپلود شد'
      photoError.value = false
      
      profileImage.value = data.profile_image_url.startsWith('http') 
        ? data.profile_image_url 
        : getApiUrl(data.profile_image_url)
      
      selectedFile.value = null
      previewUrl.value = ''
      if (fileInput.value) fileInput.value.value = ''
    } else {
      photoMessage.value = data.errors || 'خطا در آپلود عکس'
      photoError.value = true
    }
  } catch (error) {
    photoMessage.value = 'خطا در ارتباط با سرور'
    photoError.value = true
  } finally {
    photoLoading.value = false
  }
}

async function deleteProfileImage() {
  if (!confirm('آیا از حذف عکس پروفایل اطمینان دارید؟')) return

  photoLoading.value = true
  photoMessage.value = ''
  photoError.value = false

  try {
    const response = await fetch(getApiUrl('/api/accounts/delete-profile-image/'), {
      method: 'DELETE',
      credentials: 'include'
    })

    const data = await response.json()

    if (data.success) {
      photoMessage.value = 'عکس با موفقیت حذف شد'
      photoError.value = false
      profileImage.value = ''
    } else {
      photoMessage.value = data.errors || 'خطا در حذف عکس'
      photoError.value = true
    }
  } catch (error) {
    photoMessage.value = 'خطا در ارتباط با سرور'
    photoError.value = true
  } finally {
    photoLoading.value = false
  }
}

async function updateResume() {
  resumeLoading.value = true
  resumeMessage.value = ''
  resumeError.value = false

  try {
    const response = await fetch(getApiUrl('/api/accounts/update-resume/'), {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      credentials: 'include',
      body: JSON.stringify(resumeInfo.value)
    })

    const data = await response.json()

    if (data.success) {
      resumeMessage.value = 'رزومه با موفقیت به‌روزرسانی شد'
      resumeError.value = false
    } else {
      resumeMessage.value = data.errors || 'خطا در به‌روزرسانی رزومه'
      resumeError.value = true
    }
  } catch (error) {
    resumeMessage.value = 'خطا در ارتباط با سرور'
    resumeError.value = true
  } finally {
    resumeLoading.value = false
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
