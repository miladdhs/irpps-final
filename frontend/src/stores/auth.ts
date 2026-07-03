import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import { authAPI } from '@/services/api'
import i18n from '@/i18n'

export interface User {
  id: number
  username: string
  first_name: string
  last_name: string
  email: string
  phone: string
  is_staff: boolean
  profile_image?: string
  education?: string
  publications?: string
  awards?: string
  certifications?: string
  research_interests?: string
  languages?: string
  date_joined?: string
}

export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(null)
  const isAuthenticated = ref(false)
  const isLoading = ref(false)
  const error = ref<string | null>(null)
  const hasInitialized = ref(false)

  const isAdmin = computed(() => user.value?.is_staff || false)
  const t = (fa: string, en: string) => (i18n.global.locale.value === 'fa' ? fa : en)

  async function login(username: string, password: string) {
    isLoading.value = true
    error.value = null

    try {
      const response = await authAPI.login(username, password)
      if (!response.data.success) {
        error.value = response.data.errors
        return { success: false, error: response.data.errors }
      }

      await fetchProfile(true)
      return { success: true, message: response.data.message }
    } catch (err: any) {
      const errorMessage = err.response?.data?.errors || t('خطا در ورود', 'Login failed')
      error.value = errorMessage
      return { success: false, error: errorMessage }
    } finally {
      isLoading.value = false
    }
  }

  async function register(data: {
    username: string
    email: string
    phone: string
    first_name: string
    last_name: string
    password: string
    password_confirm: string
  }) {
    isLoading.value = true
    error.value = null

    try {
      const response = await authAPI.register(data)
      if (response.data.success) {
        return { success: true, message: response.data.message }
      }

      error.value = response.data.errors
      return { success: false, error: response.data.errors }
    } catch (err: any) {
      const errorMessage = err.response?.data?.errors || t('خطا در ثبت نام', 'Registration failed')
      error.value = errorMessage
      return { success: false, error: errorMessage }
    } finally {
      isLoading.value = false
    }
  }

  async function logout() {
    isLoading.value = true

    try {
      await authAPI.logout()
    } catch (err) {
      console.error('Logout error:', err)
    } finally {
      user.value = null
      isAuthenticated.value = false
      hasInitialized.value = true
      isLoading.value = false
    }
  }

  async function fetchProfile(force = false) {
    if (isLoading.value && !force) {
      return { success: isAuthenticated.value }
    }

    isLoading.value = true
    error.value = null

    try {
      const response = await authAPI.getProfile()
      if (response.data.success) {
        user.value = response.data.user
        isAuthenticated.value = true
        hasInitialized.value = true
        return { success: true }
      }

      user.value = null
      isAuthenticated.value = false
      hasInitialized.value = true
      return { success: false }
    } catch (err: any) {
      if (err.response?.status !== 401) {
        error.value = t('خطا در دریافت اطلاعات کاربر', 'Failed to load user profile')
      }

      user.value = null
      isAuthenticated.value = false
      hasInitialized.value = true
      return { success: false }
    } finally {
      isLoading.value = false
    }
  }

  async function updateProfile(data: {
    first_name?: string
    last_name?: string
    email?: string
    phone?: string
  }) {
    isLoading.value = true
    error.value = null

    try {
      const response = await authAPI.updateProfile(data)
      if (response.data.success) {
        user.value = response.data.user
        return { success: true, message: response.data.message }
      }
      return { success: false, error: response.data.errors }
    } catch (err: any) {
      const errorMessage = err.response?.data?.errors || t('خطا در بروزرسانی پروفایل', 'Profile update failed')
      error.value = errorMessage
      return { success: false, error: errorMessage }
    } finally {
      isLoading.value = false
    }
  }

  async function uploadProfileImage(file: File) {
    isLoading.value = true
    error.value = null

    try {
      const response = await authAPI.uploadProfileImage(file)
      if (response.data.success) {
        if (response.data.user) {
          user.value = response.data.user
        } else if (user.value) {
          user.value.profile_image = response.data.profile_image_url
        }
        return { success: true, message: response.data.message }
      }
      return { success: false, error: response.data.errors }
    } catch (err: any) {
      const errorMessage = err.response?.data?.errors || t('خطا در آپلود تصویر', 'Image upload failed')
      error.value = errorMessage
      return { success: false, error: errorMessage }
    } finally {
      isLoading.value = false
    }
  }

  async function deleteProfileImage() {
    isLoading.value = true
    error.value = null

    try {
      const response = await authAPI.deleteProfileImage()
      if (response.data.success) {
        if (response.data.user) {
          user.value = response.data.user
        } else if (user.value) {
          user.value.profile_image = ''
        }
        return { success: true, message: response.data.message }
      }
      return { success: false, error: response.data.errors }
    } catch (err: any) {
      const errorMessage = err.response?.data?.errors || t('خطا در حذف تصویر', 'Image deletion failed')
      error.value = errorMessage
      return { success: false, error: errorMessage }
    } finally {
      isLoading.value = false
    }
  }

  async function updateResume(data: {
    education?: string
    publications?: string
    awards?: string
    certifications?: string
    research_interests?: string
    languages?: string
    bio?: string
  }) {
    isLoading.value = true
    error.value = null

    try {
      const response = await authAPI.updateResume(data)
      if (response.data.success) {
        if (user.value) {
          Object.assign(user.value, response.data.resume)
        }
        return { success: true, message: response.data.message }
      }
      return { success: false, error: response.data.errors }
    } catch (err: any) {
      const errorMessage = err.response?.data?.errors || t('خطا در بروزرسانی رزومه', 'Resume update failed')
      error.value = errorMessage
      return { success: false, error: errorMessage }
    } finally {
      isLoading.value = false
    }
  }

  return {
    user,
    isAuthenticated,
    isLoading,
    error,
    hasInitialized,
    isAdmin,
    login,
    register,
    logout,
    fetchProfile,
    updateProfile,
    uploadProfileImage,
    deleteProfileImage,
    updateResume,
  }
})
