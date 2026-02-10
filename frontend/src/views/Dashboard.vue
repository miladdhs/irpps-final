<template>
  <div class="min-h-screen bg-gray-50 py-12 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <div class="bg-white rounded-2xl shadow-sm p-8 mb-8">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-4">
            <div class="w-20 h-20 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center text-white text-2xl font-bold">
              {{ userInitials }}
            </div>
            <div>
              <h1 class="text-2xl font-bold text-gray-900">{{ greeting }}</h1>
              <p class="text-gray-600">{{ authStore.user?.email }}</p>
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

      <!-- Quick Actions -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <router-link
          to="/profile"
          class="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition group"
        >
          <div class="w-12 h-12 rounded-lg bg-blue-100 text-blue-600 flex items-center justify-center mb-4 group-hover:scale-110 transition">
            <span class="material-symbols-outlined text-2xl">person</span>
          </div>
          <h3 class="font-bold text-gray-900 mb-1">پروفایل من</h3>
          <p class="text-sm text-gray-600">مشاهده و ویرایش اطلاعات</p>
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

      <!-- Admin Panel (if admin) -->
      <div v-if="authStore.isAdmin" class="bg-gradient-to-r from-indigo-600 to-purple-600 rounded-2xl shadow-lg p-8 text-white mb-8">
        <h2 class="text-2xl font-bold mb-4">پنل مدیریت</h2>
        <p class="mb-6 opacity-90">به عنوان مدیر، شما می‌توانید محتوای سایت را مدیریت کنید</p>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <router-link
            to="/admin/news"
            class="bg-white/10 backdrop-blur-sm rounded-lg p-4 hover:bg-white/20 transition"
          >
            <span class="material-symbols-outlined text-3xl mb-2">article</span>
            <h3 class="font-bold">مدیریت اخبار</h3>
          </router-link>
          <router-link
            to="/admin/events"
            class="bg-white/10 backdrop-blur-sm rounded-lg p-4 hover:bg-white/20 transition"
          >
            <span class="material-symbols-outlined text-3xl mb-2">event</span>
            <h3 class="font-bold">مدیریت رویدادها</h3>
          </router-link>
          <router-link
            to="/admin/members"
            class="bg-white/10 backdrop-blur-sm rounded-lg p-4 hover:bg-white/20 transition"
          >
            <span class="material-symbols-outlined text-3xl mb-2">group</span>
            <h3 class="font-bold">مدیریت اعضا</h3>
          </router-link>
        </div>
      </div>

      <!-- Recent Activity -->
      <div class="bg-white rounded-2xl shadow-sm p-8">
        <h2 class="text-xl font-bold text-gray-900 mb-6">فعالیت‌های اخیر</h2>
        <div class="text-center py-12 text-gray-500">
          <span class="material-symbols-outlined text-6xl mb-4 opacity-20">inbox</span>
          <p>فعالیتی برای نمایش وجود ندارد</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const userInitials = computed(() => {
  if (!authStore.user) return 'U'
  const firstName = authStore.user.first_name || ''
  const lastName = authStore.user.last_name || ''
  return (firstName.charAt(0) + lastName.charAt(0)).toUpperCase() || authStore.user.username.charAt(0).toUpperCase()
})

const greeting = computed(() => {
  const name = authStore.user?.first_name || authStore.user?.username || 'کاربر'
  return `سلام، ${name}`
})

async function handleLogout() {
  await authStore.logout()
  router.push('/')
}
</script>
