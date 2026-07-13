<template>
  <div class="bg-background-light text-slate-900">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1320px] px-6 py-10 lg:px-10">
        <section class="relative overflow-hidden rounded-[36px] border border-slate-200 bg-white px-8 py-10 shadow-sm">
          <div class="absolute inset-y-0 right-0 w-80 bg-[radial-gradient(circle_at_top_right,_rgba(14,165,233,0.20),_transparent_55%)]"></div>
          <div class="relative z-10 flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
            <div class="max-w-3xl">
              <div class="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary">
                <span class="material-symbols-outlined text-[20px]">groups</span>
                {{ copy.badge }}
              </div>
              <h1 class="mt-4 text-4xl font-black tracking-tight text-slate-900 md:text-5xl">{{ copy.title }}</h1>
              <p class="mt-3 text-lg leading-relaxed text-slate-600">{{ copy.subtitle }}</p>
            </div>

            <div class="w-full max-w-xl overflow-hidden rounded-2xl border border-slate-200 bg-slate-50">
              <div class="flex items-center px-4">
                <span class="material-symbols-outlined text-slate-400">search</span>
                <input v-model="searchQuery" class="w-full border-none bg-transparent py-4 text-sm outline-none" :placeholder="copy.searchPlaceholder" type="text">
                <button v-if="searchQuery" class="rounded-full p-2 text-slate-400 transition hover:bg-white hover:text-slate-700" @click="searchQuery = ''">
                  <span class="material-symbols-outlined text-base">close</span>
                </button>
              </div>
            </div>
          </div>
        </section>

        <div v-if="loading" class="flex items-center justify-center py-24">
          <div class="flex flex-col items-center gap-4">
            <div class="h-12 w-12 animate-spin rounded-full border-4 border-primary border-t-transparent"></div>
            <p class="text-slate-500">{{ copy.loading }}</p>
          </div>
        </div>

        <div v-else-if="memberError" class="mt-8 rounded-2xl border border-red-200 bg-red-50 p-6 text-red-700">
          {{ memberError }}
        </div>

        <section v-else class="mt-8">
          <div v-if="filteredMembers.length > 0" class="grid grid-cols-2 gap-4 md:grid-cols-4 xl:grid-cols-6">
            <article v-for="member in filteredMembers" :key="member.id" class="group cursor-pointer overflow-hidden rounded-[28px] border border-slate-200 bg-white shadow-sm transition-all hover:-translate-y-1 hover:border-primary/30 hover:shadow-xl" @click="openMemberModal(member)">
              <div class="aspect-[4/5] overflow-hidden bg-slate-100">
                <img v-if="getMemberImage(member)" :src="getMemberImage(member)!" :alt="getMemberName(member)" :data-member-id="member.id" class="h-full w-full object-cover transition duration-500 group-hover:scale-105" @error="handleImageError($event)">
                <div v-else class="flex h-full w-full items-center justify-center bg-[radial-gradient(circle_at_top,_rgba(14,165,233,0.15),_transparent_55%)] p-6">
                  <img v-if="!defaultIconBroken" src="/iconly/Svg/Light/Profile.svg" alt="" aria-hidden="true" class="h-16 w-16 opacity-60" @error="defaultIconBroken = true">
                  <span v-else class="material-symbols-outlined text-5xl text-slate-400">person</span>
                </div>
              </div>
              <div class="space-y-2 p-4">
                <h3 class="line-clamp-2 text-sm font-black text-slate-900">{{ getMemberName(member) }}</h3>
                <p v-if="member.current_position" class="line-clamp-2 text-xs font-medium text-slate-500">{{ member.current_position }}</p>
                <p v-else-if="member.specialty" class="line-clamp-2 text-xs font-medium text-slate-500">{{ member.specialty }}</p>
              </div>
            </article>
          </div>

          <div v-else class="flex flex-col items-center justify-center rounded-[28px] border border-dashed border-slate-300 bg-white px-6 py-20 text-center">
            <span class="material-symbols-outlined mb-4 text-6xl text-slate-300">person_search</span>
            <p class="text-slate-500">{{ copy.empty }}</p>
          </div>
        </section>
      </main>
    </div>

    <div v-if="showModal && selectedMember" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/60 p-4 backdrop-blur-sm" @click.self="closeModal">
      <div class="max-h-[92vh] w-full max-w-6xl overflow-y-auto rounded-[36px] bg-white shadow-2xl ring-1 ring-slate-200">
        <div class="sticky top-0 z-10 overflow-hidden border-b border-slate-200 bg-white/95 backdrop-blur">
          <div class="absolute inset-0 bg-[radial-gradient(circle_at_top_right,_rgba(14,165,233,0.16),_transparent_38%)]"></div>
          <div class="relative flex items-center justify-between px-7 py-5">
            <div>
              <div class="inline-flex items-center gap-2 rounded-full bg-primary/10 px-3 py-1.5 text-xs font-bold text-primary">
                <span class="material-symbols-outlined text-sm">badge</span>
                {{ copy.resumeCard }}
              </div>
              <h2 class="mt-3 text-2xl font-black text-slate-900">{{ getMemberName(selectedMember) }}</h2>
              <p class="mt-1 text-sm text-slate-500">{{ [selectedMember.current_position, selectedMember.workplace].filter(Boolean).join(' • ') }}</p>
            </div>
            <button class="rounded-full p-2 text-slate-500 transition hover:bg-slate-100 hover:text-slate-900" @click="closeModal">
              <span class="material-symbols-outlined">close</span>
            </button>
          </div>
        </div>

        <div class="grid gap-8 p-7 lg:grid-cols-[320px,1fr]">
          <aside class="space-y-6">
            <div class="overflow-hidden rounded-[28px] border border-slate-200 bg-slate-50">
              <div class="aspect-[4/5] bg-slate-100">
                <img v-if="getMemberImage(selectedMember)" :src="getMemberImage(selectedMember)!" :alt="getMemberName(selectedMember)" :data-member-id="selectedMember.id" class="h-full w-full object-cover" @error="handleImageError($event)">
                <div v-else class="flex h-full w-full items-center justify-center p-8">
                  <img v-if="!defaultIconBroken" src="/iconly/Svg/Light/Profile.svg" alt="" aria-hidden="true" class="h-24 w-24 opacity-60" @error="defaultIconBroken = true">
                  <span v-else class="material-symbols-outlined text-7xl text-slate-400">person</span>
                </div>
              </div>
            </div>

            <div class="rounded-[28px] border border-slate-200 bg-[linear-gradient(180deg,#f8fafc_0%,#ffffff_100%)] p-5">
              <h3 class="text-sm font-black tracking-[0.2em] text-slate-500">{{ copy.overview }}</h3>
              <div class="mt-4 space-y-4">
                <div v-for="item in overviewItems(selectedMember)" :key="item.label" class="flex items-start gap-3">
                  <span class="material-symbols-outlined mt-0.5 rounded-2xl bg-primary/10 p-2 text-primary">{{ item.icon }}</span>
                  <div>
                    <div class="text-xs font-semibold tracking-wide text-slate-400">{{ item.label }}</div>
                    <div class="mt-1 whitespace-pre-line text-sm font-medium text-slate-800">{{ item.value }}</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="grid gap-3 sm:grid-cols-2 lg:grid-cols-1">
              <div class="rounded-[24px] border border-slate-200 bg-white p-4 shadow-sm">
                <div class="text-xs font-bold text-slate-400">{{ copy.resumeStatus }}</div>
                <div class="mt-2 text-lg font-black text-slate-900">{{ memberSections(selectedMember).length }}</div>
                <div class="mt-1 text-sm text-slate-500">{{ copy.resumeSections }}</div>
              </div>
              <div class="rounded-[24px] border border-slate-200 bg-white p-4 shadow-sm">
                <div class="text-xs font-bold text-slate-400">{{ copy.profileStatus }}</div>
                <div class="mt-2 text-lg font-black text-slate-900">{{ overviewItems(selectedMember).length }}</div>
                <div class="mt-1 text-sm text-slate-500">{{ copy.publicFields }}</div>
              </div>
            </div>
          </aside>

          <section class="space-y-5">
            <article v-for="section in memberSections(selectedMember)" :key="section.label" class="rounded-[28px] border border-slate-200 bg-[linear-gradient(180deg,#ffffff_0%,#fbfdff_100%)] p-6 shadow-sm transition hover:shadow-md">
              <h3 class="text-lg font-black text-slate-900">{{ section.label }}</h3>
              <div class="mt-3 whitespace-pre-line text-sm leading-7 text-slate-600">{{ section.value }}</div>
            </article>
            <div v-if="memberSections(selectedMember).length === 0" class="rounded-[28px] border border-dashed border-slate-300 bg-slate-50 p-10 text-center text-slate-500">
              {{ copy.noResume }}
            </div>
          </section>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { getApiUrl } from '@/utils/api'
import { resolveImageUrl } from '@/utils/assets'

interface Member {
  id: number
  persian_name: string
  english_name: string
  display_name: string
  email: string
  phone: string
  city: string
  specialty: string
  experience: number
  bio: string
  workplace: string
  current_position: string
  expertise_areas: string
  work_experience: string
  profile_image: string
  education: string
  publications: string
  awards: string
  certifications: string
  research_interests: string
  languages: string
}

const members = ref<Member[]>([])
const loading = ref(true)
const memberError = ref<string | null>(null)
const searchQuery = ref('')
const selectedMember = ref<Member | null>(null)
const showModal = ref(false)
const brokenImages = ref<Set<number>>(new Set())
const defaultIconBroken = ref(false)
const { locale } = useI18n()

const copy = computed(() => (
  locale.value === 'fa'
    ? {
        badge: 'فهرست اعضای انجمن',
        title: 'اعضای انجمن',
        subtitle: 'با انتخاب هر عضو، رزومه و اطلاعات عمومی ثبت‌شده توسط همان عضو در پنل کاربری نمایش داده می‌شود.',
        searchPlaceholder: 'جستجو بر اساس نام، تخصص، محل کار یا شهر',
        loading: 'در حال بارگذاری اعضا...',
        empty: 'عضوی با این جستجو پیدا نشد.',
        resumeCard: 'رزومه عضو',
        overview: 'نمای کلی',
        resumeStatus: 'وضعیت رزومه',
        resumeSections: 'بخش فعال رزومه',
        profileStatus: 'وضعیت پروفایل',
        publicFields: 'فیلد عمومی تکمیل‌شده',
        noResume: 'برای این عضو هنوز بخشی از رزومه ثبت نشده است.',
        loadError: 'دریافت اطلاعات اعضا انجام نشد.',
        city: 'شهر',
        specialty: 'تخصص',
        currentPosition: 'سمت فعلی',
        workplace: 'محل کار',
        experience: 'سابقه',
        experienceYears: 'سال',
        languages: 'زبان‌ها',
        biography: 'معرفی',
        expertise: 'حوزه‌های تخصص',
        education: 'تحصیلات',
        workExperience: 'سوابق کاری',
        publications: 'انتشارات',
        awards: 'افتخارات',
        certifications: 'گواهی‌ها',
        researchInterests: 'علایق پژوهشی',
        unknownMember: 'عضو انجمن',
      }
    : {
        badge: 'Members Directory',
        title: 'Association Members',
        subtitle: 'Select any member to open the public resume built from the information they manage in their dashboard.',
        searchPlaceholder: 'Search by member, specialty, workplace, or city',
        loading: 'Loading members...',
        empty: 'No members match this search.',
        resumeCard: 'Member Resume',
        overview: 'Overview',
        resumeStatus: 'Resume Status',
        resumeSections: 'Visible resume sections',
        profileStatus: 'Profile Status',
        publicFields: 'Completed public fields',
        noResume: 'No resume section has been filled in for this member yet.',
        loadError: 'Failed to load member information.',
        city: 'City',
        specialty: 'Specialty',
        currentPosition: 'Current Position',
        workplace: 'Workplace',
        experience: 'Experience',
        experienceYears: 'years',
        languages: 'Languages',
        biography: 'Biography',
        expertise: 'Areas of Expertise',
        education: 'Education',
        workExperience: 'Work Experience',
        publications: 'Publications',
        awards: 'Awards and Honors',
        certifications: 'Certifications',
        researchInterests: 'Research Interests',
        unknownMember: 'Association Member',
      }
))

const getMemberName = (member: Member) => {
  if (locale.value === 'fa') {
    return member.persian_name || member.display_name || member.english_name || copy.value.unknownMember
  }
  return member.english_name || member.display_name || member.persian_name || copy.value.unknownMember
}

function getMemberImage(member: Member): string | null {
  if (brokenImages.value.has(member.id)) return null
  return member.profile_image?.trim() ? resolveImageUrl(member.profile_image, '') : null
}

function handleImageError(event: Event) {
  const img = event.target as HTMLImageElement
  const memberId = Number(img.dataset.memberId || '0')
  if (!memberId) return
  const next = new Set(brokenImages.value)
  next.add(memberId)
  brokenImages.value = next
}

async function fetchMembers() {
  try {
    loading.value = true
    memberError.value = null
    const response = await fetch(getApiUrl(`/api/accounts/members/?t=${Date.now()}`), {
      credentials: 'include',
      cache: 'no-store',
      headers: {
        Accept: 'application/json',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
      },
    })
    if (!response.ok) throw new Error(`Failed to load members (${response.status})`)
    const data = await response.json()
    members.value = Array.isArray(data) ? data : (data.members || [])
  } catch (error) {
    console.error('Error fetching members:', error)
    memberError.value = copy.value.loadError
  } finally {
    loading.value = false
  }
}

const filteredMembers = computed(() => {
  const query = searchQuery.value.trim().toLowerCase()
  if (!query) return members.value
  return members.value.filter((member) => {
    const fields = [
      member.display_name,
      member.persian_name,
      member.english_name,
      member.specialty,
      member.city,
      member.workplace,
      member.current_position,
      member.expertise_areas,
    ]
    return fields.some((field) => field && String(field).toLowerCase().includes(query))
  })
})

function overviewItems(member: Member) {
  return [
    { label: copy.value.city, value: member.city, icon: 'location_on' },
    { label: copy.value.specialty, value: member.specialty, icon: 'medical_services' },
    { label: copy.value.currentPosition, value: member.current_position, icon: 'badge' },
    { label: copy.value.workplace, value: member.workplace, icon: 'apartment' },
    { label: copy.value.experience, value: member.experience ? `${member.experience} ${copy.value.experienceYears}` : '', icon: 'workspace_premium' },
    { label: copy.value.languages, value: member.languages, icon: 'translate' },
  ].filter((item) => String(item.value || '').trim())
}

function memberSections(member: Member) {
  return [
    { label: copy.value.biography, value: member.bio },
    { label: copy.value.expertise, value: member.expertise_areas },
    { label: copy.value.education, value: member.education },
    { label: copy.value.workExperience, value: member.work_experience },
    { label: copy.value.publications, value: member.publications },
    { label: copy.value.awards, value: member.awards },
    { label: copy.value.certifications, value: member.certifications },
    { label: copy.value.researchInterests, value: member.research_interests },
  ].filter((section) => String(section.value || '').trim())
}

function openMemberModal(member: Member) {
  selectedMember.value = member
  showModal.value = true
  document.body.style.overflow = 'hidden'
}

function closeModal() {
  showModal.value = false
  selectedMember.value = null
  document.body.style.overflow = 'auto'
}

onMounted(fetchMembers)
</script>
