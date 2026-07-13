<template>
  <div class="min-h-screen bg-slate-50 px-4 py-8">
    <div class="mx-auto max-w-7xl">
      <div class="mb-8 flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 class="text-3xl font-black text-slate-900">Event Management</h1>
          <p class="mt-2 text-slate-600">Create, update, and publish events with separate Shamsi registration and event dates.</p>
        </div>
        <button @click="showAddModal = true" class="inline-flex items-center gap-2 rounded-2xl bg-slate-900 px-6 py-3 font-semibold text-white transition hover:bg-slate-800">
          <span class="material-symbols-outlined">add</span>
          Add Event
        </button>
      </div>

      <div v-if="loading" class="py-20 text-center">
        <div class="inline-block h-12 w-12 animate-spin rounded-full border-4 border-primary border-t-transparent"></div>
        <p class="mt-4 text-slate-500">Loading events...</p>
      </div>

      <div v-else-if="error" class="rounded-2xl border border-red-200 bg-red-50 p-4 text-red-700">
        {{ error }}
      </div>

      <div v-else class="overflow-hidden rounded-[28px] border border-slate-200 bg-white shadow-sm">
        <table class="min-w-full divide-y divide-slate-200">
          <thead class="bg-slate-50">
            <tr class="text-left text-xs font-bold uppercase tracking-[0.2em] text-slate-500">
              <th class="px-6 py-4">Image</th>
              <th class="px-6 py-4">Title</th>
              <th class="px-6 py-4">Type</th>
              <th class="px-6 py-4">Event Date</th>
              <th class="px-6 py-4">Registration Date</th>
              <th class="px-6 py-4">Status</th>
              <th class="px-6 py-4">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200 bg-white">
            <tr v-for="event in eventsList" :key="event.id" class="align-top">
              <td class="px-6 py-4">
                <img :src="eventImageUrl(event.image)" alt="Event cover" class="h-16 w-16 rounded-2xl object-cover" @error="handleEventImageError">
              </td>
              <td class="px-6 py-4">
                <div class="font-semibold text-slate-900">{{ event.title }}</div>
                <div class="mt-1 text-sm text-slate-500">{{ event.slug }}</div>
              </td>
              <td class="px-6 py-4 text-sm text-slate-700">{{ event.event_type }}</td>
              <td class="px-6 py-4 text-sm text-slate-700">{{ formatDate(event.event_date) }}</td>
              <td class="px-6 py-4 text-sm text-slate-700">{{ formatDate(event.registration_date || event.registration_deadline) }}</td>
              <td class="px-6 py-4">
                <span class="rounded-full px-3 py-1 text-xs font-semibold" :class="event.is_published ? 'bg-emerald-100 text-emerald-700' : 'bg-slate-100 text-slate-600'">
                  {{ event.is_published ? 'Published' : 'Draft' }}
                </span>
              </td>
              <td class="px-6 py-4 text-sm font-semibold">
                <button class="mr-4 text-primary transition hover:text-primary/70" @click="editEvent(event)">Edit</button>
                <button class="text-red-600 transition hover:text-red-500" @click="deleteEvent(event.id)">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-if="showAddModal || showEditModal" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/60 p-4" @click.self="closeModal">
        <div class="max-h-[92vh] w-full max-w-5xl overflow-y-auto rounded-[32px] bg-white shadow-2xl ring-1 ring-slate-200">
          <div class="sticky top-0 z-10 flex items-center justify-between border-b border-slate-200 bg-white/95 px-6 py-5 backdrop-blur">
            <div>
              <h2 class="text-2xl font-black text-slate-900">{{ showEditModal ? 'Edit Event' : 'Create Event' }}</h2>
              <p class="mt-1 text-sm text-slate-500">Date inputs use the Shamsi date picker and are stored in the database in Gregorian format.</p>
            </div>
            <button class="rounded-full p-2 text-slate-500 transition hover:bg-slate-100 hover:text-slate-900" @click="closeModal">
              <span class="material-symbols-outlined">close</span>
            </button>
          </div>

          <form class="grid gap-5 p-6 md:grid-cols-2" @submit.prevent="saveEvent">
            <label class="space-y-2 md:col-span-2">
              <span class="text-sm font-semibold text-slate-700">Event title</span>
              <input v-model="formData.title" type="text" required class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>

            <label class="space-y-2 md:col-span-2">
              <span class="text-sm font-semibold text-slate-700">Slug</span>
              <input v-model="formData.slug" type="text" required class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>

            <label class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">Event type</span>
              <select v-model="formData.event_type" required class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
                <option value="congress">Congress</option>
                <option value="conference">Conference</option>
                <option value="workshop">Workshop</option>
                <option value="webinar">Webinar</option>
                <option value="seminar">Seminar</option>
                <option value="other">Other</option>
              </select>
            </label>

            <label class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">Retraining number</span>
              <input v-model="formData.retraining_number" type="text" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>

            <label class="space-y-2 md:col-span-2">
              <span class="text-sm font-semibold text-slate-700">Description</span>
              <textarea v-model="formData.description" rows="7" required class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10"></textarea>
            </label>

            <label class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">Location</span>
              <input v-model="formData.location" type="text" required class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>

            <label class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">Organizer</span>
              <input v-model="formData.organizer" type="text" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>

            <div class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">Event date</span>
              <date-picker
                v-model="formData.event_date"
                format="YYYY-MM-DD"
                display-format="jYYYY/jMM/jDD"
                input-class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10"
                placeholder="Select event date"
                :editable="false"
                color="#0f766e"
              />
            </div>

            <div class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">Registration date</span>
              <date-picker
                v-model="formData.registration_date"
                format="YYYY-MM-DD"
                display-format="jYYYY/jMM/jDD"
                input-class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10"
                placeholder="Select registration date"
                :editable="false"
                color="#0f766e"
              />
            </div>

            <label class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">Price</span>
              <input v-model.number="formData.price" type="number" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>

            <label class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">Max participants</span>
              <input v-model.number="formData.max_participants" type="number" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>

            <label class="space-y-2 md:col-span-2">
              <span class="text-sm font-semibold text-slate-700">Speakers</span>
              <textarea v-model="formData.speakers" rows="3" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10"></textarea>
            </label>

            <label class="space-y-2 md:col-span-2">
              <span class="text-sm font-semibold text-slate-700">Event image</span>
              <input ref="imageInput" type="file" accept="image/*" class="w-full rounded-2xl border border-slate-300 px-4 py-3" @change="handleImageSelect">
            </label>

            <div class="md:col-span-2 flex flex-wrap gap-5 rounded-2xl bg-slate-50 px-5 py-4">
              <label class="inline-flex items-center gap-3 text-sm font-semibold text-slate-700">
                <input v-model="formData.is_published" type="checkbox" class="h-4 w-4 rounded border-slate-300 text-primary focus:ring-primary">
                Publish event
              </label>
              <label class="inline-flex items-center gap-3 text-sm font-semibold text-slate-700">
                <input v-model="formData.is_featured" type="checkbox" class="h-4 w-4 rounded border-slate-300 text-primary focus:ring-primary">
                Featured event
              </label>
            </div>

            <div class="md:col-span-2 flex items-center justify-end gap-3 border-t border-slate-200 pt-4">
              <button type="button" class="rounded-2xl border border-slate-300 px-5 py-3 font-semibold text-slate-700 transition hover:bg-slate-50" @click="closeModal">Cancel</button>
              <button type="submit" :disabled="saving" class="rounded-2xl bg-slate-900 px-6 py-3 font-semibold text-white transition hover:bg-slate-800 disabled:opacity-50">
                {{ saving ? 'Saving...' : 'Save Event' }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import DatePicker from 'vue3-persian-datetime-picker'
import { getApiUrl } from '@/utils/api'
import { DEFAULT_EVENT_IMAGE, resolveImageUrl } from '@/utils/assets'

type EventItem = {
  id: number
  title: string
  slug: string
  description: string
  event_type: string
  event_type_code?: string
  retraining_number: string | null
  image: string | null
  location: string
  event_date: string | null
  registration_date: string | null
  registration_deadline: string | null
  max_participants: number | null
  price: number
  organizer: string
  speakers: string
  is_published: boolean
  is_featured: boolean
}

const eventsList = ref<EventItem[]>([])
const loading = ref(true)
const error = ref<string | null>(null)
const showAddModal = ref(false)
const showEditModal = ref(false)
const saving = ref(false)
const editingId = ref<number | null>(null)
const imageInput = ref<HTMLInputElement | null>(null)
const selectedImage = ref<File | null>(null)

const initialFormState = () => ({
  title: '',
  slug: '',
  description: '',
  event_type: 'congress',
  retraining_number: '',
  location: '',
  event_date: '',
  registration_date: '',
  price: 0,
  max_participants: null as number | null,
  organizer: '',
  speakers: '',
  is_published: true,
  is_featured: false,
})

const formData = ref(initialFormState())

const eventImageUrl = (image: string | null) => resolveImageUrl(image, DEFAULT_EVENT_IMAGE)

function handleEventImageError(event: Event) {
  const img = event.target as HTMLImageElement
  if (!img.src.endsWith(DEFAULT_EVENT_IMAGE)) {
    img.src = DEFAULT_EVENT_IMAGE
  }
}

function formatDate(value: string | null) {
  if (!value) return '-'
  return new Intl.DateTimeFormat('en-US', { dateStyle: 'medium' }).format(new Date(value))
}

const fetchEvents = async () => {
  loading.value = true
  error.value = null
  try {
    const response = await fetch(getApiUrl('/api/events/?per_page=100'), {
      credentials: 'include',
      cache: 'no-store',
    })
    if (!response.ok) throw new Error('Failed to fetch events')
    const data = await response.json()
    if (data.success) {
      eventsList.value = data.events
    }
  } catch (err: any) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

function handleImageSelect(event: Event) {
  const target = event.target as HTMLInputElement
  selectedImage.value = target.files?.[0] || null
}

async function saveEvent() {
  saving.value = true
  try {
    const payload = new FormData()
    payload.append('title', formData.value.title)
    payload.append('slug', formData.value.slug)
    payload.append('description', formData.value.description)
    payload.append('event_type', formData.value.event_type)
    payload.append('retraining_number', formData.value.retraining_number || '')
    payload.append('location', formData.value.location)
    payload.append('event_date', formData.value.event_date || '')
    payload.append('registration_date', formData.value.registration_date || '')
    payload.append('price', String(formData.value.price ?? 0))
    payload.append('max_participants', formData.value.max_participants?.toString() || '')
    payload.append('organizer', formData.value.organizer || '')
    payload.append('speakers', formData.value.speakers || '')
    payload.append('is_published', String(formData.value.is_published))
    payload.append('is_featured', String(formData.value.is_featured))
    if (selectedImage.value) payload.append('cover_image', selectedImage.value)

    const url = showEditModal.value ? getApiUrl(`/api/events/${editingId.value}/update/`) : getApiUrl('/api/events/create/')
    const response = await fetch(url, { method: 'POST', credentials: 'include', body: payload })
    const data = await response.json()
    if (!data.success) throw new Error(data.errors || 'Failed to save event')

    closeModal()
    await fetchEvents()
  } catch (err: any) {
    alert(err.message || 'Server communication failed')
  } finally {
    saving.value = false
  }
}

function editEvent(event: EventItem) {
  editingId.value = event.id
  formData.value = {
    title: event.title,
    slug: event.slug,
    description: event.description,
    event_type: event.event_type_code || 'other',
    retraining_number: event.retraining_number || '',
    location: event.location,
    event_date: event.event_date || '',
    registration_date: event.registration_date || event.registration_deadline || '',
    price: event.price,
    max_participants: event.max_participants,
    organizer: event.organizer || '',
    speakers: event.speakers || '',
    is_published: event.is_published,
    is_featured: event.is_featured,
  }
  showEditModal.value = true
}

async function deleteEvent(id: number) {
  if (!confirm('Delete this event?')) return
  try {
    const response = await fetch(getApiUrl(`/api/events/${id}/delete/`), {
      method: 'DELETE',
      credentials: 'include',
    })
    const data = await response.json()
    if (!data.success) throw new Error(data.errors || 'Failed to delete event')
    await fetchEvents()
  } catch (err: any) {
    alert(err.message || 'Server communication failed')
  }
}

function closeModal() {
  showAddModal.value = false
  showEditModal.value = false
  editingId.value = null
  selectedImage.value = null
  formData.value = initialFormState()
  if (imageInput.value) imageInput.value.value = ''
}

onMounted(fetchEvents)
</script>
