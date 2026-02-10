import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authAPI } from '@/services/api'

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

  const isAdmin = computed(() => user.value?.is_staff || false)

  // Login
  async function login(username: string, password: string) {
    isLoading.value = true
    error.value = null
    try {
      const response = await authAPI.login(username, password)
      if (response.data.success) {
        user.value = response.data.user
        isAuthenticated.value = true
        return { success: true, message: response.data.message }
      } else {
        error.value = response.data.errors
        return { success: false, error: response.data.errors }
      }
    } catch (err: any) {
      const errorMessage = err.response?.data?.errors || 'خطا در ورود'
      error.value = errorMessage
      return { success: false, error: errorMessage }
    } finally {
      isLoading.value = false
    }
  }

  // Register
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
        // Don't auto-login after registration (pending approval)
        return { success: true, message: response.data.message }
      } else {
        error.value = response.data.errors
        return { success: false, error: response.data.errors }
      }
    } catch (err: any) {
      const errorMessage = err.response?.data?.errors || 'خطا در ثبت نام'
      error.value = errorMessage
      return { success: false, error: errorMessage }
    } finally {
      isLoading.value = false
    }
  }

  // Logout
  async function logout() {
    isLoading.value = true
    try {
      await authAPI.logout()
      user.value = null
      isAuthenticated.value = false
    } catch (err) {
      console.error('Logout error:', err)
    } finally {
      isLoading.value = false
    }
  }

  // Get profile
  async function fetchProfile() {
    isLoading.value = true
    error.value = null
    try {
      const response = await authAPI.getProfile()
      if (response.data.success) {
        user.value = response.data.user
        isAuthenticated.value = true
        return { success: true }
      }
    } catch (err: any) {
      if (err.response?.status !== 401) {
        error.value = 'خطا در دریافت اطلاعات کاربر'
      }
      user.value = null
      isAuthenticated.value = false
      return { success: false }
    } finally {
      isLoading.value = false
    }
  }

  // Update profile
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
    } catch (err: any) {
      const errorMessage = err.response?.data?.errors || 'خطا در بروزرسانی پروفایل'
      error.value = errorMessage
      return { success: false, error: errorMessage }
    } finally {
      isLoading.value = false
    }
  }

  // Upload profile image
  async function uploadProfileImage(file: File) {
    isLoading.value = true
    error.value = null
    try {
      const response = await authAPI.uploadProfileImage(file)
      if (response.data.success) {
        if (user.value) {
          user.value.profile_image = response.data.profile_image_url
        }
        return { success: true, message: response.data.message }
      }
    } catch (err: any) {
      const errorMessage = err.response?.data?.errors || 'خطا در آپلود تصویر'
      error.value = errorMessage
      return { success: false, error: errorMessage }
    } finally {
      isLoading.value = false
    }
  }

  // Delete profile image
  async function deleteProfileImage() {
    isLoading.value = true
    error.value = null
    try {
      const response = await authAPI.deleteProfileImage()
      if (response.data.success) {
        if (user.value) {
          user.value.profile_image = undefined
        }
        return { success: true, message: response.data.message }
      }
    } catch (err: any) {
      const errorMessage = err.response?.data?.errors || 'خطا در حذف تصویر'
      error.value = errorMessage
      return { success: false, error: errorMessage }
    } finally {
      isLoading.value = false
    }
  }

  // Update resume
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
        // Update user with resume data
        if (user.value) {
          Object.assign(user.value, response.data.resume)
        }
        return { success: true, message: response.data.message }
      }
    } catch (err: any) {
      const errorMessage = err.response?.data?.errors || 'خطا در بروزرسانی رزومه'
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
