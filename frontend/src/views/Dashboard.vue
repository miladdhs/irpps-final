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

      <!-- Main Content -->
      <div class="row g-4">
        <div class="col-lg-8">
          <!-- Profile Edit Form (Inline Toggle) -->
          <transition name="fade-slide">
            <div v-if="showProfileForm" class="bg-white rounded-2xl shadow-sm p-6 mb-6">
              <h4 class="text-xl font-bold text-gray-900 mb-6">
                <span class="material-symbols-outlined align-middle ml-2">person_edit</span>
                ویرایش اطلاعات شخصی
              </h4>
              
              <div v-if="personalInfoMessage" :class="[
                'p-4 rounded-lg mb-6',
                personalInfoError ? 'bg-red-50 text-red-600' : 'bg-green-50 text-green-600'
              ]">
                {{ personalInfoMessage }}
              </div>

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

                <div class="flex gap-3">
                  <button
                    type="submit"
                    :disabled="personalInfoLoading"
                    class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition disabled:opacity-50"
                  >
                    <span v-if="personalInfoLoading">در حال ذخیره...</span>
                    <span v-else>ذخیره تغییرات</span>
                  </button>
                  <button
                    type="button"
                    @click="showProfileForm = false"
                    class="px-6 py-3 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition"
                  >
                    انصراف
                  </button>
                </div>
              </form>
            </div>
          </transition>

          <!-- Profile Info Display -->
          <div class="bg-white rounded-2xl shadow-sm p-6">
            <div class="flex justify-between items-center mb-6">
              <h4 class="text-xl font-bold text-gray-900">
                <span class="material-symbols-outlined align-middle ml-2">info</span>
                اطلاعات حساب کاربری
              </h4>
              <button
                v-if="!showProfileForm"
                @click="showProfileForm = true"
                class="px-4 py-2 bg-blue-50 text-blue-600 rounded-lg hover:bg-blue-100 transition"
              >
                <span class="material-symbols-outlined text-sm align-middle ml-1">edit</span>
                ویرایش
              </button>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="flex items-start gap-3">
                <span class="material-symbols-outlined text-blue-600">person</span>
                <div>
                  <p class="text-sm text-gray-500">نام</p>
                  <p class="font-medium">{{ personalInfo.first_name || 'ثبت نشده' }}</p>
                </div>
              </div>
              <div class="flex items-start gap-3">
                <span class="material-symbols-outlined text-blue-600">badge</span>
                <div>
                  <p class="text-sm text-gray-500">نام خانوادگی</p>
                  <p class="font-medium">{{ personalInfo.last_name || 'ثبت نشده' }}</p>
                </div>
              </div>
              <div class="flex items-start gap-3">
                <span class="material-symbols-outlined text-blue-600">email</span>
                <div>
                  <p class="text-sm text-gray-500">ایمیل</p>
                  <p class="font-medium">{{ personalInfo.email || 'ثبت نشده' }}</p>
                </div>
              </div>
              <div class="flex items-start gap-3">
                <span class="material-symbols-outlined text-blue-600">phone</span>
                <div>
                  <p class="text-sm text-gray-500">تلفن</p>
                  <p class="font-medium">{{ personalInfo.phone || 'ثبت نشده' }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Sidebar -->
        <div class="col-lg-4">
          <div class="bg-white rounded-2xl shadow-sm p-6 sticky top-24">
            <!-- Profile Image Display -->
            <div class="text-center mb-6">
              <div v-if="profileImage" class="w-32 h-32 rounded-full overflow-hidden border-4 border-gray-200 mx-auto mb-4">
                <img :src="profileImage" alt="Profile" class="w-full h-full object-cover" />
              </div>
              <div v-else class="w-32 h-32 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center text-white text-4xl font-bold mx-auto mb-4">
                {{ userInitials }}
              </div>
              <h5 class="font-bold text-lg">{{ personalInfo.first_name || authStore.user?.username }}</h5>
              <p class="text-gray-500 text-sm">{{ authStore.user?.username }}</p>
            </div>

            <!-- Action Buttons -->
            <div class="space-y-3">
              <button
                @click="showImageUploadModal = true"
                class="w-full px-4 py-3 bg-blue-50 text-blue-600 rounded-lg hover:bg-blue-100 transition flex items-center justify-center gap-2"
              >
                <span class="material-symbols-outlined">photo_camera</span>
                {{ profileImage ? 'تغییر عکس' : 'افزودن عکس' }}
              </button>

              <button
                v-if="profileImage"
                @click="deleteProfileImage"
                :disabled="photoLoading"
                class="w-full px-4 py-3 bg-red-50 text-red-600 rounded-lg hover:bg-red-100 transition flex items-center justify-center gap-2 disabled:opacity-50"
              >
                <span v-if="photoLoading" class="material-symbols-outlined animate-spin">progress_activity</span>
                <span v-else class="material-symbols-outlined">delete</span>
                {{ photoLoading ? 'در حال حذف...' : 'حذف عکس' }}
              </button>

              <button
                @click="showResumeModal = true"
                class="w-full px-4 py-3 bg-green-50 text-green-600 rounded-lg hover:bg-green-100 transition flex items-center justify-center gap-2"
              >
                <span class="material-symbols-outlined">description</span>
                رزومه و توضیحات
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Image Upload Modal -->
    <div
      v-if="showImageUploadModal"
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4"
      @click.self="showImageUploadModal = false"
    >
      <div class="bg-white rounded-2xl shadow-xl max-w-md w-full">
        <div class="flex items-center justify-between p-6 border-b">
          <h3 class="text-xl font-bold">
            <span class="material-symbols-outlined align-middle ml-2 text-blue-600">photo_camera</span>
            تغییر عکس پروفایل
          </h3>
          <button @click="showImageUploadModal = false" class="text-gray-400 hover:text-gray-600">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>

        <div class="p-6">
          <div v-if="photoMessage" :class="[
            'p-4 rounded-lg mb-6',
            photoError ? 'bg-red-50 text-red-600' : 'bg-green-50 text-green-600'
          ]">
            {{ photoMessage }}
          </div>

          <form @submit.prevent="uploadProfileImage">
            <div class="mb-6">
              <label class="block text-sm font-medium text-gray-700 mb-2">انتخاب عکس</label>
              <input
                ref="fileInput"
                type="file"
                accept="image/*"
                @change="handleFileSelect"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                required
              />
              <p class="text-sm text-gray-500 mt-2">فرمت‌های مجاز: JPG, PNG, GIF</p>
            </div>

            <div v-if="previewUrl" class="mb-6 text-center">
              <img :src="previewUrl" alt="Preview" class="w-48 h-48 rounded-lg object-cover mx-auto border-2 border-gray-200" />
            </div>

            <button
              type="submit"
              :disabled="!selectedFile || photoLoading"
              class="w-full px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition disabled:opacity-50"
            >
              <span v-if="photoLoading">در حال آپلود...</span>
              <span v-else>آپلود عکس</span>
            </button>
          </form>
        </div>
      </div>
    </div>

    <!-- Resume Modal -->
    <div
      v-if="showResumeModal"
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4"
      @click.self="showResumeModal = false"
    >
      <div class="bg-white rounded-2xl shadow-xl max-w-3xl w-full max-h-[90vh] flex flex-col">
        <div class="flex items-center justify-between p-6 border-b flex-shrink-0">
          <h3 class="text-xl font-bold">
            <span class="material-symbols-outlined align-middle ml-2 text-green-600">description</span>
            توضیحات عمومی و رزومه
          </h3>
          <button @click="showResumeModal = false" class="text-gray-400 hover:text-gray-600">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>

        <div class="p-6 overflow-y-auto flex-1">
          <div v-if="resumeMessage" :class="[
            'p-4 rounded-lg mb-6',
            resumeError ? 'bg-red-50 text-red-600' : 'bg-green-50 text-green-600'
          ]">
            {{ resumeMessage }}
          </div>

          <form @submit.prevent="updateResume" class="space-y-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                <span class="material-symbols-outlined text-sm align-middle ml-1">info</span>
                توضیحات عمومی
              </label>
              <textarea
                v-model="resumeInfo.bio"
                rows="3"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                placeholder="توضیحات کوتاه درباره خودتان..."
              ></textarea>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                <span class="material-symbols-outlined text-sm align-middle ml-1">school</span>
                تحصیلات
              </label>
              <textarea
                v-model="resumeInfo.education"
                rows="3"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                placeholder="مدرک تحصیلی، دانشگاه، سال فارغ‌التحصیلی..."
              ></textarea>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                <span class="material-symbols-outlined text-sm align-middle ml-1">menu_book</span>
                مقالات و انتشارات
              </label>
              <textarea
                v-model="resumeInfo.publications"
                rows="4"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                placeholder="مقالات، کتاب‌ها و انتشارات علمی..."
              ></textarea>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                <span class="material-symbols-outlined text-sm align-middle ml-1">emoji_events</span>
                جوایز و افتخارات
              </label>
              <textarea
                v-model="resumeInfo.awards"
                rows="3"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                placeholder="جوایز، افتخارات و دستاوردها..."
              ></textarea>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                <span class="material-symbols-outlined text-sm align-middle ml-1">workspace_premium</span>
                گواهینامه‌ها
              </label>
              <textarea
                v-model="resumeInfo.certifications"
                rows="3"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                placeholder="گواهینامه‌های تخصصی و حرفه‌ای..."
              ></textarea>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                <span class="material-symbols-outlined text-sm align-middle ml-1">science</span>
                علایق پژوهشی
              </label>
              <textarea
                v-model="resumeInfo.research_interests"
                rows="3"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                placeholder="حوزه‌های تحقیقاتی و علایق پژوهشی..."
              ></textarea>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                <span class="material-symbols-outlined text-sm align-middle ml-1">language</span>
                زبان‌ها
              </label>
              <input
                v-model="resumeInfo.languages"
                type="text"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                placeholder="مثال: فارسی، انگلیسی، آلمانی"
              />
            </div>

            <button
              type="submit"
              :disabled="resumeLoading"
              class="w-full px-6 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 transition disabled:opacity-50"
            >
              <span v-if="resumeLoading">در حال ذخیره...</span>
              <span v-else>ذخیره رزومه</span>
            </button>
          </form>
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

// Modals
const showImageUploadModal = ref(false)
const showResumeModal = ref(false)
const showProfileForm = ref(false)

// Profile image
const profileImage = ref('')
const selectedFile = ref<File | null>(null)
const previewUrl = ref('')
const fileInput = ref<HTMLInputElement | null>(null)
const photoLoading = ref(false)
const photoMessage = ref('')
const photoError = ref(false)

// Personal info
const personalInfo = ref({
  first_name: '',
  last_name: '',
  email: '',
  phone: ''
})
const personalInfoLoading = ref(false)
const personalInfoMessage = ref('')
const personalInfoError = ref(false)

// Resume
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
    const response = await fetch(getApiUrl('/api/accounts/profile/update/'), {
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
      setTimeout(() => {
        showProfileForm.value = false
      }, 1500)
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

      setTimeout(() => {
        showImageUploadModal.value = false
        photoMessage.value = ''
      }, 1500)
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

  try {
    const response = await fetch(getApiUrl('/api/accounts/delete-profile-image/'), {
      method: 'DELETE',
      credentials: 'include'
    })

    const data = await response.json()

    if (data.success) {
      profileImage.value = ''
      alert('عکس با موفقیت حذف شد')
    } else {
      alert(data.errors || 'خطا در حذف عکس')
    }
  } catch (error) {
    alert('خطا در ارتباط با سرور')
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
      setTimeout(() => {
        showResumeModal.value = false
        resumeMessage.value = ''
      }, 1500)
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

<style scoped>
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.3s ease;
}

.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}

.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>
