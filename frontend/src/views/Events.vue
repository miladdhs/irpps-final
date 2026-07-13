<template>
  <div class="bg-background-light text-slate-900">
    <div class="mx-auto max-w-7xl px-6 py-10">
      <div class="mb-10 flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
        <div>
          <div class="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary">
            <span class="material-symbols-outlined text-base">event</span>
            Events
          </div>
          <h1 class="mt-4 text-4xl font-black tracking-tight text-slate-900 md:text-5xl">Congresses, workshops, and scientific meetings</h1>
          <p class="mt-3 max-w-3xl text-lg text-slate-600">All event cards use separate event and registration dates from the database. Past events are archived automatically.</p>
        </div>
        <div class="text-sm font-medium text-slate-500">{{ filteredEvents.length }} events shown</div>
      </div>

      <div class="mb-8 flex flex-wrap items-center gap-3">
        <button v-for="tab in tabs" :key="tab.id" class="rounded-full px-4 py-2 text-sm font-semibold transition" :class="activeTab === tab.id ? 'bg-slate-900 text-white' : 'bg-white text-slate-600 ring-1 ring-slate-200 hover:text-primary'" @click="activeTab = tab.id">
          {{ tab.label }}
        </button>
        <button v-for="filter in filters" :key="filter.id" class="rounded-full px-4 py-2 text-sm font-semibold transition" :class="selectedFilter === filter.id ? 'bg-primary text-white' : 'bg-white text-slate-600 ring-1 ring-slate-200 hover:text-primary'" @click="selectedFilter = filter.id">
          {{ filter.label }}
        </button>
      </div>

      <div v-if="eventsLoading" class="py-20 text-center">
        <div class="inline-block h-12 w-12 animate-spin rounded-full border-4 border-primary border-t-transparent"></div>
        <p class="mt-4 text-slate-500">Loading events...</p>
      </div>

      <div v-else-if="eventsError" class="rounded-2xl border border-red-200 bg-red-50 p-6 text-red-700">
        {{ eventsError }}
      </div>

      <div v-else-if="filteredEvents.length === 0" class="rounded-[28px] border border-dashed border-slate-300 bg-white px-6 py-20 text-center text-slate-500">
        No events found in this section.
      </div>

      <div v-else class="grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-3">
        <article v-for="event in filteredEvents" :key="event.id" class="group overflow-hidden rounded-[28px] border border-slate-200 bg-white shadow-sm transition-all hover:-translate-y-1 hover:border-primary/30 hover:shadow-xl">
          <div class="relative aspect-[16/10] overflow-hidden bg-slate-100">
            <img :src="event.image" :alt="event.title" class="h-full w-full object-cover transition duration-500 group-hover:scale-105" @error="handleEventImageError">
            <span class="absolute right-4 top-4 rounded-full px-3 py-1 text-xs font-bold text-white" :class="event.statusClass">{{ event.statusText }}</span>
            <span class="absolute left-4 top-4 rounded-full border border-primary/20 bg-white/90 px-3 py-1 text-xs font-bold text-primary">{{ event.type }}</span>
          </div>

          <div class="flex h-full flex-col gap-4 p-5">
            <div>
              <h2 class="line-clamp-2 text-xl font-black text-slate-900">{{ event.title }}</h2>
              <p class="mt-3 line-clamp-3 text-sm leading-7 text-slate-600">{{ event.summary }}</p>
            </div>

            <div class="space-y-2 text-sm text-slate-600">
              <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-base text-primary">calendar_month</span>
                <span><strong class="text-slate-800">Event:</strong> {{ formatDate(event.event_date) }}</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-base text-primary">edit_calendar</span>
                <span><strong class="text-slate-800">Registration:</strong> {{ formatDate(event.registration_date) }}</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-base text-primary">location_on</span>
                <span>{{ event.location }}</span>
              </div>
              <div v-if="event.retraining_number" class="flex items-center gap-2 rounded-2xl bg-primary/10 px-3 py-2 font-semibold text-primary">
                <span class="material-symbols-outlined text-base">badge</span>
                {{ event.retraining_number }}
              </div>
            </div>

            <router-link :to="`/events/${event.slug}`" class="mt-auto inline-flex items-center justify-center rounded-2xl bg-slate-900 px-4 py-3 text-sm font-semibold text-white transition hover:bg-slate-800">
              View details
            </router-link>
          </div>
        </article>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { getApiUrl } from '@/utils/api'
import { DEFAULT_EVENT_IMAGE, resolveImageUrl } from '@/utils/assets'

type EventItem = {
  id: number
  title: string
  slug: string
  description: string
  short_description?: string
  event_type: string
  event_type_code?: string
  image: string | null
  location: string
  event_date: string | null
  registration_date: string | null
  registration_deadline: string | null
  retraining_number?: string | null
  is_registration_open: boolean
  has_ended?: boolean
  status_code?: string
}

const activeTab = ref<'upcoming' | 'past'>('upcoming')
const selectedFilter = ref('all')
const eventItems = ref<EventItem[]>([])
const eventsLoading = ref(true)
const eventsError = ref<string | null>(null)

const tabs = [
  { id: 'upcoming', label: 'Upcoming' },
  { id: 'past', label: 'Past' },
]

const filters = [
  { id: 'all', label: 'All' },
  { id: 'congress', label: 'Congress' },
  { id: 'conference', label: 'Conference' },
  { id: 'workshop', label: 'Workshop' },
  { id: 'webinar', label: 'Webinar' },
  { id: 'seminar', label: 'Seminar' },
]

function formatDate(value: string | null) {
  if (!value) return 'Not set'
  return new Intl.DateTimeFormat('en-US', { dateStyle: 'medium' }).format(new Date(value))
}

const normalizedEvents = computed(() => eventItems.value.map((event) => {
  const statusMap: Record<string, { text: string; className: string }> = {
    registration_open: { text: 'Registration Open', className: 'bg-emerald-500' },
    registration_closed: { text: 'Registration Closed', className: 'bg-amber-500' },
    ended: { text: 'Ended', className: 'bg-slate-500' },
  }
  const status = statusMap[event.status_code || 'registration_closed'] || statusMap.registration_closed
  return {
    ...event,
    image: resolveImageUrl(event.image, DEFAULT_EVENT_IMAGE),
    summary: event.short_description || event.description?.replace(/<[^>]+>/g, ' ').slice(0, 160) || '',
    statusText: status.text,
    statusClass: status.className,
    type: event.event_type,
    registration_date: event.registration_date || event.registration_deadline,
  }
}))

const filteredEvents = computed(() => {
  const items = normalizedEvents.value.filter((event) => activeTab.value === 'past' ? event.has_ended : !event.has_ended)
  return selectedFilter.value === 'all' ? items : items.filter((event) => event.event_type_code === selectedFilter.value)
})

async function fetchEvents() {
  eventsLoading.value = true
  eventsError.value = null
  try {
    const response = await fetch(getApiUrl('/api/events/?page=1&per_page=50'), {
      credentials: 'include',
      cache: 'no-store',
    })
    if (!response.ok) throw new Error(`Failed to load events (${response.status})`)
    const data = await response.json()
    if (!data.success || !Array.isArray(data.events)) throw new Error('Invalid events response')
    eventItems.value = data.events
  } catch (error: any) {
    console.error('Failed to load events:', error)
    eventsError.value = error.message || 'Failed to load events'
  } finally {
    eventsLoading.value = false
  }
}

function handleEventImageError(event: Event) {
  const img = event.target as HTMLImageElement
  if (!img.src.endsWith(DEFAULT_EVENT_IMAGE)) {
    img.src = DEFAULT_EVENT_IMAGE
  }
}

onMounted(fetchEvents)
</script>
