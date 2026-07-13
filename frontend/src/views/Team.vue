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
                Members Directory
              </div>
              <h1 class="mt-4 text-4xl font-black tracking-tight text-slate-900 md:text-5xl">Association Members</h1>
              <p class="mt-3 text-lg leading-relaxed text-slate-600">Click on any member to open the full resume card built from the information they maintain in their dashboard.</p>
            </div>

            <div class="w-full max-w-xl overflow-hidden rounded-2xl border border-slate-200 bg-slate-50">
              <div class="flex items-center px-4">
                <span class="material-symbols-outlined text-slate-400">search</span>
                <input v-model="searchQuery" class="w-full border-none bg-transparent py-4 text-sm outline-none" placeholder="Search by member, specialty, workplace, or city" type="text">
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
            <p class="text-slate-500">Loading members...</p>
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
            <p class="text-slate-500">No members match this search.</p>
          </div>
        </section>
      </main>
    </div>

    <div v-if="showModal && selectedMember" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/60 p-4" @click.self="closeModal">
      <div class="max-h-[92vh] w-full max-w-5xl overflow-y-auto rounded-[32px] bg-white shadow-2xl ring-1 ring-slate-200">
        <div class="sticky top-0 z-10 flex items-center justify-between border-b border-slate-200 bg-white/95 px-7 py-5 backdrop-blur">
          <div>
            <h2 class="text-2xl font-black text-slate-900">{{ getMemberName(selectedMember) }}</h2>
            <p class="mt-1 text-sm text-slate-500">{{ [selectedMember.current_position, selectedMember.workplace].filter(Boolean).join(' • ') }}</p>
          </div>
          <button class="rounded-full p-2 text-slate-500 transition hover:bg-slate-100 hover:text-slate-900" @click="closeModal">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>

        <div class="grid gap-8 p-7 lg:grid-cols-[300px,1fr]">
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

            <div class="rounded-[28px] border border-slate-200 bg-slate-50 p-5">
              <h3 class="text-sm font-black uppercase tracking-[0.2em] text-slate-500">Overview</h3>
              <div class="mt-4 space-y-4">
                <div v-for="item in overviewItems(selectedMember)" :key="item.label" class="flex items-start gap-3">
                  <span class="material-symbols-outlined text-primary">{{ item.icon }}</span>
                  <div>
                    <div class="text-xs font-semibold uppercase tracking-wide text-slate-400">{{ item.label }}</div>
                    <div class="mt-1 text-sm font-medium text-slate-800 whitespace-pre-line">{{ item.value }}</div>
                  </div>
                </div>
              </div>
            </div>
          </aside>

          <section class="space-y-5">
            <article v-for="section in memberSections(selectedMember)" :key="section.label" class="rounded-[28px] border border-slate-200 bg-white p-6 shadow-sm">
              <h3 class="text-lg font-black text-slate-900">{{ section.label }}</h3>
              <div class="mt-3 whitespace-pre-line text-sm leading-7 text-slate-600">{{ section.value }}</div>
            </article>
          </section>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
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

const getMemberName = (member: Member) => member.english_name || member.persian_name || member.display_name || 'Unknown member'

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
    memberError.value = 'Failed to load member information.'
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
    { label: 'City', value: member.city, icon: 'location_on' },
    { label: 'Specialty', value: member.specialty, icon: 'medical_services' },
    { label: 'Current Position', value: member.current_position, icon: 'badge' },
    { label: 'Workplace', value: member.workplace, icon: 'apartment' },
    { label: 'Experience', value: member.experience ? `${member.experience} years` : '', icon: 'workspace_premium' },
    { label: 'Languages', value: member.languages, icon: 'translate' },
  ].filter((item) => String(item.value || '').trim())
}

function memberSections(member: Member) {
  return [
    { label: 'Biography', value: member.bio },
    { label: 'Areas of Expertise', value: member.expertise_areas },
    { label: 'Education', value: member.education },
    { label: 'Work Experience', value: member.work_experience },
    { label: 'Publications', value: member.publications },
    { label: 'Awards and Honors', value: member.awards },
    { label: 'Certifications', value: member.certifications },
    { label: 'Research Interests', value: member.research_interests },
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
