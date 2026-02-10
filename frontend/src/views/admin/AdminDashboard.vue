<template>
  <div class="min-h-screen bg-gray-50 p-8">
    <div class="max-w-7xl mx-auto">
      <h1 class="text-3xl font-bold mb-8">پنل مدیریت</h1>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <router-link to="/admin/news" class="bg-white p-6 rounded-lg shadow hover:shadow-lg transition">
          <h2 class="text-xl font-bold mb-2">مدیریت اخبار</h2>
          <p class="text-gray-600">افزودن، ویرایش و حذف اخبار</p>
        </router-link>
        <router-link to="/admin/announcements" class="bg-white p-6 rounded-lg shadow hover:shadow-lg transition">
          <h2 class="text-xl font-bold mb-2">مدیریت اطلاعیه‌ها</h2>
          <p class="text-gray-600">افزودن، ویرایش و حذف اطلاعیه‌ها</p>
        </router-link>
        <router-link to="/admin/events" class="bg-white p-6 rounded-lg shadow hover:shadow-lg transition">
          <h2 class="text-xl font-bold mb-2">مدیریت رویدادها</h2>
          <p class="text-gray-600">افزودن، ویرایش و حذف رویدادها</p>
        </router-link>
        <router-link to="/admin/members" class="bg-white p-6 rounded-lg shadow hover:shadow-lg transition">
          <h2 class="text-xl font-bold mb-2">مدیریت اعضا</h2>
          <p class="text-gray-600">تایید و مدیریت اعضا</p>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Admin Dashboard
</script>
