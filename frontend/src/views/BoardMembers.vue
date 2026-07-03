<template>
  <div class="relative flex min-h-screen w-full flex-col overflow-x-hidden bg-background-light dark:bg-background-dark">
    <div class="relative flex h-[400px] w-full items-center justify-center overflow-hidden">
      <div class="absolute inset-0 z-0 bg-gradient-to-l from-primary/80 to-slate-900/90"></div>
      <div class="relative z-10 max-w-3xl px-4 text-center">
        <h1 class="mb-6 text-4xl font-black text-white md:text-5xl">{{ pageTitle }}</h1>
        <p class="text-lg font-light leading-relaxed text-blue-100 md:text-xl">
          {{ pageSubtitle }}
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
        <p class="mt-4 text-slate-500 dark:text-slate-400">{{ loadingText }}</p>
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
            <p class="text-slate-500 dark:text-slate-400">{{ emptyText }}</p>
          </div>

          <div v-else class="grid grid-cols-2 gap-8 sm:grid-cols-3 lg:grid-cols-4">
            <div v-for="member in membersByPeriod(period.value)" :key="member.username" class="group text-center">
              <div class="relative mx-auto mb-4 h-40 w-40 overflow-hidden rounded-full border-4 border-white shadow-lg transition-all group-hover:border-primary dark:border-slate-800">
                <img
                  v-if="member.profile_image"
                  :src="getApiUrl(member.profile_image)"
                  :alt="getMemberName(member)"
                  class="h-full w-full object-cover"
                />
                <div v-else class="flex h-full w-full items-center justify-center bg-gradient-to-br from-primary/20 to-primary/5">
                  <span class="material-symbols-outlined text-6xl text-primary/40">person</span>
                </div>
              </div>
              <h3 class="mb-1 text-lg font-bold text-slate-900 dark:text-white">{{ getMemberName(member) }}</h3>
              <p class="mb-1 text-sm font-medium text-primary">{{ getMemberPosition(member) }}</p>
              <p class="text-xs text-slate-500 dark:text-slate-400">{{ member.specialty }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="mt-16 rounded-xl border border-slate-200 bg-slate-50 p-8 dark:border-slate-800 dark:bg-slate-900/50">
        <div class="flex items-start gap-4">
          <span class="material-symbols-outlined text-3xl text-primary">info</span>
          <div>
            <h4 class="mb-2 text-lg font-bold text-slate-900 dark:text-white">{{ infoTitle }}</h4>
            <p class="leading-relaxed text-slate-600 dark:text-slate-400">
              {{ infoBody }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { getApiUrl } from '@/utils/api'

type BoardMember = {
  id: number | null
  username: string
  persian_name?: string
  english_name?: string
  display_name: string
  position: string
  role?: string
  specialty: string
  profile_image: string
}

type BoardResponse = {
  success: boolean
  board_members: Record<string, BoardMember[]>
  errors?: string
}

const { locale } = useI18n()
const route = useRoute()
const router = useRouter()
const validPeriods = ['1403', '1400', '1395'] as const
const getPeriodFromRoute = () => {
  const period = typeof route.query.period === 'string' ? route.query.period : ''
  return validPeriods.includes(period as (typeof validPeriods)[number]) ? period : '1403'
}

const activePeriod = ref(getPeriodFromRoute())
const boardLoading = ref(true)
const boardError = ref<string | null>(null)
const boardMembers = ref<Record<string, BoardMember[]>>({})

const pageTitle = computed(() => locale.value === 'fa' ? 'اعضای هیئت مدیره' : 'Board Members')
const pageSubtitle = computed(() => locale.value === 'fa' ? 'هیئت مدیره انجمن علمی ریه کودکان ایران در دوره‌های مختلف' : 'Board members of the Iranian Pediatric Lung Scientific Association across different terms')
const loadingText = computed(() => locale.value === 'fa' ? 'در حال بارگذاری اعضای هیئت مدیره...' : 'Loading board members...')
const emptyText = computed(() => locale.value === 'fa' ? 'عضوی برای این دوره ثبت نشده است.' : 'No members are registered for this term.')
const infoTitle = computed(() => locale.value === 'fa' ? 'درباره هیئت مدیره' : 'About the Board')
const infoBody = computed(() => locale.value === 'fa'
  ? 'هیئت مدیره انجمن علمی ریه کودکان ایران از برجسته‌ترین متخصصان و پژوهشگران این حوزه تشکیل شده است. اعضای هیئت مدیره با رأی اعضای انجمن برای دوره‌های مختلف انتخاب می‌شوند.'
  : 'The board is composed of leading specialists and researchers in pediatric pulmonology. Board members are elected by the association members for each term.')

const roleLabelsEn: Record<string, string> = {
  president: 'President',
  vice_president: 'Vice President',
  secretary: 'Secretary',
  treasurer: 'Treasurer',
  board_member: 'Board Member',
  alternate_board_member: 'Alternate Board Member',
  main_inspector: 'Main Inspector',
  alternate_inspector: 'Alternate Inspector',
}

const periods = computed(() => [
  {
    value: '1403',
    label: locale.value === 'fa' ? 'دوره ۱۴۰۳ (فعلی)' : 'Term 1403 (Current)',
    title: locale.value === 'fa' ? 'هیئت مدیره دوره ۱۴۰۳' : 'Board of Directors - Term 1403',
    subtitle: locale.value === 'fa' ? 'پس از انتخابات دوره جدید' : 'Current elected board members',
  },
  {
    value: '1400',
    label: locale.value === 'fa' ? 'دوره ۱۴۰۰' : 'Term 1400',
    title: locale.value === 'fa' ? 'هیئت مدیره دوره ۱۴۰۰' : 'Board of Directors - Term 1400',
    subtitle: locale.value === 'fa' ? 'اعضای منتخب آن دوره' : 'Members elected for that term',
  },
  {
    value: '1395',
    label: locale.value === 'fa' ? 'مؤسسین (۱۳۹۵)' : 'Founders (1395)',
    title: locale.value === 'fa' ? 'مؤسسین انجمن - دوره ۱۳۹۵' : 'Association Founders - 1395',
    subtitle: locale.value === 'fa' ? 'تاریخ تأسیس: ۱۶ آذر ۱۳۹۵' : 'Foundation term',
  },
])

watch(
  () => route.query.period,
  () => {
    activePeriod.value = getPeriodFromRoute()
  }
)

watch(activePeriod, (period) => {
  if (route.query.period !== period) {
    router.replace({
      name: 'board-members',
      query: { ...route.query, period },
    })
  }
})

const membersByPeriod = (period: string) => boardMembers.value[period] || []

const getMemberName = (member: BoardMember) => {
  if (locale.value === 'fa') {
    return member.persian_name || member.display_name || member.english_name || member.username
  }
  return member.english_name || member.persian_name || member.display_name || member.username
}

const getMemberPosition = (member: BoardMember) => {
  if (locale.value === 'fa') {
    return member.position
  }
  return roleLabelsEn[member.role || ''] || member.position
}

const fetchBoardMembers = async () => {
  boardLoading.value = true
  boardError.value = null

  try {
    const response = await fetch(getApiUrl('/api/accounts/board-members/'), {
      credentials: 'include',
      cache: 'no-store',
    })

    if (!response.ok) {
      throw new Error(locale.value === 'fa' ? `خطا در دریافت هیئت مدیره (${response.status})` : `Failed to load board members (${response.status})`)
    }

    const data = (await response.json()) as BoardResponse
    if (!data.success || !data.board_members) {
      throw new Error(data.errors || (locale.value === 'fa' ? 'ساختار داده هیئت مدیره نامعتبر است' : 'Invalid board members response'))
    }

    boardMembers.value = data.board_members
  } catch (error: any) {
    boardError.value = error.message || (locale.value === 'fa' ? 'خطا در دریافت اعضای هیئت مدیره' : 'Failed to load board members')
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
