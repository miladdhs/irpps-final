<template>
  <div class="bg-background-light text-slate-900">
    <div class="mx-auto max-w-6xl px-6 py-10">
      <nav class="mb-8 flex items-center gap-2 text-sm text-slate-500">
        <router-link to="/" class="transition hover:text-primary">Home</router-link>
        <span class="material-symbols-outlined text-base">chevron_right</span>
        <router-link to="/events" class="transition hover:text-primary">Events</router-link>
        <span class="material-symbols-outlined text-base">chevron_right</span>
        <span class="text-slate-900">{{ event?.title || 'Details' }}</span>
      </nav>

      <div v-if="eventLoading" class="py-20 text-center">
        <div class="inline-block h-12 w-12 animate-spin rounded-full border-4 border-primary border-t-transparent"></div>
        <p class="mt-4 text-slate-500">Loading event...</p>
      </div>

      <div v-else-if="eventError" class="rounded-2xl border border-red-200 bg-red-50 p-6 text-red-700">
        {{ eventError }}
      </div>

      <div v-else-if="event" class="grid gap-8 lg:grid-cols-[1.2fr,0.8fr]">
        <article class="overflow-hidden rounded-[32px] border border-slate-200 bg-white shadow-sm">
          <div class="aspect-[16/9] overflow-hidden bg-slate-100">
            <img :src="event.image" :alt="event.title" class="h-full w-full object-cover" @error="handleEventImageError">
          </div>
          <div class="p-8">
            <div class="mb-4 flex flex-wrap items-center gap-3">
              <span class="rounded-full px-4 py-2 text-sm font-bold text-white" :class="statusClass">{{ statusLabel }}</span>
              <span class="rounded-full border border-primary/20 bg-primary/10 px-4 py-2 text-sm font-bold text-primary">{{ event.event_type }}</span>
            </div>
            <h1 class="text-4xl font-black leading-tight text-slate-900">{{ event.title }}</h1>
            <div class="prose prose-slate mt-8 max-w-none" v-html="event.description"></div>
          </div>
        </article>

        <aside class="space-y-6">
          <section class="rounded-[32px] border border-slate-200 bg-white p-6 shadow-sm">
            <h2 class="text-xl font-black text-slate-900">Event Information</h2>
            <div class="mt-5 space-y-5">
              <div class="flex items-start gap-3">
                <span class="material-symbols-outlined text-primary">calendar_month</span>
                <div>
                  <div class="text-xs font-bold uppercase tracking-[0.2em] text-slate-400">Event Date</div>
                  <div class="mt-1 font-medium text-slate-800">{{ formatDate(event.event_date) }}</div>
                </div>
              </div>
              <div class="flex items-start gap-3">
                <span class="material-symbols-outlined text-primary">edit_calendar</span>
                <div>
                  <div class="text-xs font-bold uppercase tracking-[0.2em] text-slate-400">Registration Date</div>
                  <div class="mt-1 font-medium text-slate-800">{{ formatDate(event.registration_date || event.registration_deadline) }}</div>
                </div>
              </div>
              <div class="flex items-start gap-3">
                <span class="material-symbols-outlined text-primary">location_on</span>
                <div>
                  <div class="text-xs font-bold uppercase tracking-[0.2em] text-slate-400">Location</div>
                  <div class="mt-1 font-medium text-slate-800">{{ event.location }}</div>
                </div>
              </div>
              <div v-if="event.organizer" class="flex items-start gap-3">
                <span class="material-symbols-outlined text-primary">domain</span>
                <div>
                  <div class="text-xs font-bold uppercase tracking-[0.2em] text-slate-400">Organizer</div>
                  <div class="mt-1 font-medium text-slate-800">{{ event.organizer }}</div>
                </div>
              </div>
              <div v-if="event.max_participants" class="flex items-start gap-3">
                <span class="material-symbols-outlined text-primary">group</span>
                <div>
                  <div class="text-xs font-bold uppercase tracking-[0.2em] text-slate-400">Capacity</div>
                  <div class="mt-1 font-medium text-slate-800">{{ event.max_participants }}</div>
                </div>
              </div>
              <div v-if="event.retraining_number" class="flex items-start gap-3">
                <span class="material-symbols-outlined text-primary">badge</span>
                <div>
                  <div class="text-xs font-bold uppercase tracking-[0.2em] text-slate-400">Retraining Number</div>
                  <div class="mt-1 text-lg font-black text-primary">{{ event.retraining_number }}</div>
                </div>
              </div>
            </div>
          </section>

          <section v-if="event.speakers || event.agenda || event.contact_info" class="rounded-[32px] border border-slate-200 bg-white p-6 shadow-sm">
            <h2 class="text-xl font-black text-slate-900">Additional Details</h2>
            <div class="mt-5 space-y-5 text-sm leading-7 text-slate-600">
              <div v-if="event.speakers">
                <div class="text-xs font-bold uppercase tracking-[0.2em] text-slate-400">Speakers</div>
                <div class="mt-1 whitespace-pre-line">{{ event.speakers }}</div>
              </div>
              <div v-if="event.agenda">
                <div class="text-xs font-bold uppercase tracking-[0.2em] text-slate-400">Agenda</div>
                <div class="mt-1 whitespace-pre-line">{{ event.agenda }}</div>
              </div>
              <div v-if="event.contact_info">
                <div class="text-xs font-bold uppercase tracking-[0.2em] text-slate-400">Contact</div>
                <div class="mt-1 whitespace-pre-line">{{ event.contact_info }}</div>
              </div>
            </div>
          </section>
        </aside>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { getApiUrl } from '@/utils/api'
import { DEFAULT_EVENT_IMAGE, resolveImageUrl } from '@/utils/assets'

const route = useRoute()
const event = ref<any>(null)
const eventLoading = ref(true)
const eventError = ref<string | null>(null)

const statusMap: Record<string, { text: string; className: string }> = {
  registration_open: { text: 'Registration Open', className: 'bg-emerald-500' },
  registration_closed: { text: 'Registration Closed', className: 'bg-amber-500' },
  ended: { text: 'Event Ended', className: 'bg-slate-500' },
}

const statusCode = computed(() => event.value?.status_code || 'registration_closed')
const statusClass = computed(() => statusMap[statusCode.value]?.className || 'bg-slate-500')
const statusLabel = computed(() => statusMap[statusCode.value]?.text || 'Closed')

function formatDate(value: string | null) {
  if (!value) return 'Not set'
  return new Intl.DateTimeFormat('en-US', { dateStyle: 'full' }).format(new Date(value))
}

async function fetchEvent() {
  eventLoading.value = true
  eventError.value = null
  try {
    const slug = route.params.slug as string
    const response = await fetch(getApiUrl(`/api/events/${slug}/`), {
      credentials: 'include',
      cache: 'no-store',
    })
    if (!response.ok) throw new Error(`Failed to load event (${response.status})`)
    const data = await response.json()
    if (!data.success || !data.event) throw new Error('Invalid event response')
    event.value = {
      ...data.event,
      image: resolveImageUrl(data.event.image, DEFAULT_EVENT_IMAGE),
    }
  } catch (error: any) {
    console.error('Failed to load event:', error)
    eventError.value = error.message || 'Failed to load event'
  } finally {
    eventLoading.value = false
  }
}

function handleEventImageError(eventObj: Event) {
  const img = eventObj.target as HTMLImageElement
  if (!img.src.endsWith(DEFAULT_EVENT_IMAGE)) {
    img.src = DEFAULT_EVENT_IMAGE
  }
}

onMounted(fetchEvent)
</script>
