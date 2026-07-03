<template>
  <div class="relative flex h-auto min-h-screen w-full flex-col overflow-x-hidden bg-background-light dark:bg-background-dark">
    <div class="relative flex h-[400px] w-full items-center justify-center overflow-hidden">
      <div class="absolute inset-0 z-0 bg-gradient-to-l from-primary/80 to-slate-900/90"></div>
      <div class="relative z-10 max-w-3xl px-4 text-center">
        <h1 class="mb-6 text-4xl font-black text-white md:text-5xl">اعضای هیئت مدیره</h1>
        <p class="text-lg font-light leading-relaxed text-blue-100 md:text-xl">
          هیئت مدیره انجمن علمی ریه کودکان ایران در دوره‌های مختلف
        </p>
      </div>
    </div>

    <div class="mx-auto max-w-[1200px] px-6 py-16">
      <div class="mb-12 flex justify-center">
        <div class="inline-flex rounded-lg border border-slate-200 bg-white p-1 dark:border-slate-800 dark:bg-slate-900">
          <button
            v-for="period in periods"
            :key="period.value"
            @click="activePeriod = period.value"
            :class="[
              'rounded-md px-6 py-3 text-sm font-medium transition-all',
              activePeriod === period.value
                ? 'bg-primary text-white shadow-sm'
                : 'text-slate-600 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white'
            ]"
          >
            {{ period.label }}
          </button>
        </div>
      </div>

      <div v-if="boardLoading" class="rounded-xl bg-slate-50 p-12 text-center dark:bg-slate-900/50">
        <div class="mx-auto inline-block h-12 w-12 animate-spin rounded-full border-b-2 border-primary"></div>
        <p class="mt-4 text-slate-500 dark:text-slate-400">در حال بارگذاری اعضای هیئت مدیره...</p>
      </div>

      <div v-else-if="boardError" class="rounded-xl border border-red-200 bg-red-50 p-6 text-center dark:border-red-800 dark:bg-red-900/20">
        <span class="material-symbols-outlined mb-2 text-4xl text-red-600">error</span>
        <p class="text-red-600 dark:text-red-400">{{ boardError }}</p>
      </div>

      <div v-else class="space-y-16">
        <div v-for="period in periods" :key="period.value" v-show="activePeriod === period.value" class="animate-fade-in">
          <div class="mb-12 text-center">
            <h2 class="mb-3 text-3xl font-bold text-slate-900 dark:text-white">
              {{ period.title }}
            </h2>
            <p class="text-slate-500 dark:text-slate-400">{{ period.subtitle }}</p>
          </div>

          <div v-if="membersByPeriod(period.value).length === 0" class="rounded-xl bg-slate-50 p-10 text-center dark:bg-slate-900/50">
            <p class="text-slate-500 dark:text-slate-400">عضوی برای این دوره ثبت نشده است.</p>
          </div>

          <div v-else class="grid grid-cols-2 gap-8 sm:grid-cols-3 lg:grid-cols-4">
            <div v-for="member in membersByPeriod(period.value)" :key="member.username" class="group text-center">
              <div class="relative mx-auto mb-4 h-40 w-40 overflow-hidden rounded-full border-4 border-white shadow-lg transition-all group-hover:border-primary dark:border-slate-800">
                <img
                  v-if="member.profile_image"
                  :src="getApiUrl(member.profile_image)"
                  :alt="member.display_name"
                  class="h-full w-full object-cover"
                />
                <div v-else class="flex h-full w-full items-center justify-center bg-gradient-to-br from-primary/20 to-primary/5">
                  <span class="material-symbols-outlined text-6xl text-primary/40">person</span>
                </div>
              </div>
              <h3 class="mb-1 text-lg font-bold text-slate-900 dark:text-white">{{ member.display_name }}</h3>
              <p class="mb-1 text-sm font-medium text-primary">{{ member.position }}</p>
              <p class="text-xs text-slate-500 dark:text-slate-400">{{ member.specialty }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="mt-16 rounded-xl border border-slate-200 bg-slate-50 p-8 dark:border-slate-800 dark:bg-slate-900/50">
        <div class="flex items-start gap-4">
          <span class="material-symbols-outlined text-3xl text-primary">info</span>
          <div>
            <h4 class="mb-2 text-lg font-bold text-slate-900 dark:text-white">درباره هیئت مدیره</h4>
            <p class="leading-relaxed text-slate-600 dark:text-slate-400">
              هیئت مدیره انجمن علمی ریه کودکان ایران از برجسته‌ترین متخصصان و پژوهشگران این حوزه تشکیل شده است.
              اعضای هیئت مدیره با برگزاری انتخابات الکترونیکی و با رأی اعضای انجمن برای مدت چهار سال انتخاب می‌شوند.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { getApiUrl } from '@/utils/api'

type BoardMember = {
  id: number | null
  username: string
  display_name: string
  position: string
  specialty: string
  profile_image: string
}

type BoardResponse = {
  success: boolean
  board_members: Record<string, BoardMember[]>
  errors?: string
}

const activePeriod = ref('1403')
const boardLoading = ref(true)
const boardError = ref<string | null>(null)
const boardMembers = ref<Record<string, BoardMember[]>>({})

const periods = [
  { value: '1403', label: 'دوره ۱۴۰۳ (فعلی)', title: 'هیئت مدیره دوره ۱۴۰۳', subtitle: 'پس از انتخابات دوره جدید' },
  { value: '1400', label: 'دوره ۱۴۰۰', title: 'هیئت مدیره دوره ۱۴۰۰', subtitle: 'اعضای منتخب آن دوره' },
  { value: '1395', label: 'موسسین (۱۳۹۵)', title: 'موسسین انجمن - دوره ۱۳۹۵', subtitle: 'تاریخ تأسیس: ۱۶ آذر ۱۳۹۵' },
]

const membersByPeriod = (period: string) => boardMembers.value[period] || []

const fetchBoardMembers = async () => {
  boardLoading.value = true
  boardError.value = null

  try {
    const response = await fetch(getApiUrl('/api/accounts/board-members/'), {
      credentials: 'include',
    })

    if (!response.ok) {
      throw new Error(`خطا در دریافت هیئت مدیره از سرور (${response.status})`)
    }

    const data = (await response.json()) as BoardResponse
    if (!data.success || !data.board_members) {
      throw new Error(data.errors || 'ساختار داده هیئت مدیره نامعتبر است')
    }

    boardMembers.value = data.board_members
  } catch (error: any) {
    boardError.value = error.message || 'خطای ناشناخته هنگام دریافت اعضای هیئت مدیره'
  } finally {
    boardLoading.value = false
  }
}

onMounted(() => {
  fetchBoardMembers()
})
</script>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
