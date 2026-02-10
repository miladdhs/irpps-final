import axios, { type AxiosInstance, type AxiosRequestConfig } from 'axios'

// API Base URL - adjust based on environment
// در production از /api استفاده می‌کنیم که nginx به backend proxy می‌کند
const API_BASE_URL = import.meta.env.VITE_API_URL || '/api'

// Create axios instance with default config
const apiClient: AxiosInstance = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true, // Important for CSRF and session cookies
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
})

// Request interceptor to add CSRF token
apiClient.interceptors.request.use(
  (config) => {
    // Get CSRF token from cookie
    const csrfToken = getCookie('csrftoken')
    if (csrfToken) {
      config.headers['X-CSRFToken'] = csrfToken
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor for error handling
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Unauthorized - redirect to login
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

// Helper function to get cookie value
function getCookie(name: string): string | null {
  const value = `; ${document.cookie}`
  const parts = value.split(`; ${name}=`)
  if (parts.length === 2) return parts.pop()?.split(';').shift() || null
  return null
}

// ==================== AUTH API ====================
export const authAPI = {
  login: (username: string, password: string) =>
    apiClient.post('/accounts/login/', { username, password }),
  
  register: (data: {
    username: string
    email: string
    phone: string
    first_name: string
    last_name: string
    password: string
    password_confirm: string
  }) => apiClient.post('/accounts/register/', data),
  
  logout: () => apiClient.post('/accounts/logout/'),
  
  getProfile: () => apiClient.get('/accounts/profile/'),
  
  updateProfile: (data: {
    first_name?: string
    last_name?: string
    email?: string
    phone?: string
  }) => apiClient.put('/accounts/profile/update/', data),
  
  uploadProfileImage: (file: File) => {
    const formData = new FormData()
    formData.append('profile_image', file)
    return apiClient.post('/accounts/profile/image/upload/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })
  },
  
  deleteProfileImage: () => apiClient.post('/accounts/profile/image/delete/'),
  
  updateResume: (data: {
    education?: string
    publications?: string
    awards?: string
    certifications?: string
    research_interests?: string
    languages?: string
    bio?: string
  }) => apiClient.post('/accounts/profile/resume/update/', data),
}

// ==================== MEMBERS API ====================
export const membersAPI = {
  getMembers: () => apiClient.get('/accounts/members/'),
  
  getPendingMembers: () => apiClient.get('/accounts/members/pending/'),
  
  approveMember: (userId: number) =>
    apiClient.post(`/accounts/members/${userId}/approve/`),
  
  rejectMember: (userId: number, reason: string) =>
    apiClient.post(`/accounts/members/${userId}/reject/`, { reason }),
}

// ==================== NEWS API ====================
export const newsAPI = {
  getNewsList: (params?: { page?: number; per_page?: number }) =>
    apiClient.get('/news/', { params }),
  
  getNewsDetail: (slug: string) => apiClient.get(`/news/${slug}/`),
  
  createNews: (data: FormData) =>
    apiClient.post('/news/create/', data, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }),
  
  updateNews: (id: number, data: {
    title?: string
    slug?: string
    content?: string
    is_published?: boolean
  }) => apiClient.put(`/news/${id}/update/`, data),
  
  deleteNews: (id: number) => apiClient.delete(`/news/${id}/delete/`),
}

// ==================== ANNOUNCEMENTS API ====================
export const announcementsAPI = {
  getAnnouncementsList: (params?: { page?: number; per_page?: number }) =>
    apiClient.get('/news/announcements/', { params }),
  
  createAnnouncement: (data: {
    title: string
    slug: string
    content: string
    is_published?: boolean
    is_important?: boolean
  }) => apiClient.post('/news/announcements/create/', data),
}

// ==================== EVENTS API ====================
export const eventsAPI = {
  getEventsList: (params?: { page?: number; per_page?: number; type?: string }) =>
    apiClient.get('/events/', { params }),
  
  getEventDetail: (slug: string) => apiClient.get(`/events/${slug}/`),
  
  registerForEvent: (id: number) => apiClient.post(`/events/${id}/register/`),
  
  createEvent: (data: FormData) =>
    apiClient.post('/events/create/', data, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }),
}

// ==================== PUBLICATIONS API ====================
export const publicationsAPI = {
  getPublicationsFiles: () => apiClient.get('/news/publications/files/'),
}

// ==================== DOCTORS API ====================
export const doctorsAPI = {
  getDoctorsFiles: () => apiClient.get('/doctors/files/'),
}

export default apiClient
