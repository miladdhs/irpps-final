<template>
  <div class="min-h-screen bg-slate-50 px-4 py-10">
    <div class="mx-auto max-w-6xl">
      <div class="mb-8 flex flex-wrap items-center justify-between gap-4">
        <div>
          <router-link to="/dashboard" class="mb-3 inline-flex items-center gap-2 text-sm font-medium text-slate-500 transition hover:text-primary">
            <span class="material-symbols-outlined text-base">{{ locale === 'fa' ? 'arrow_forward' : 'arrow_back' }}</span>
            {{ copy.back }}
          </router-link>
          <h1 class="text-4xl font-black tracking-tight text-slate-900">{{ copy.pageTitle }}</h1>
          <p class="mt-2 max-w-2xl text-slate-600">{{ copy.pageText }}</p>
        </div>
        <button
          type="button"
          class="inline-flex items-center gap-2 rounded-2xl bg-slate-900 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-slate-900/15 transition hover:-translate-y-0.5"
          @click="showResumeModal = true"
        >
          <span class="material-symbols-outlined text-base">edit_note</span>
          {{ copy.editResume }}
        </button>
      </div>

      <div v-if="successMessage" class="mb-6 rounded-2xl border border-emerald-200 bg-emerald-50 px-5 py-4 text-emerald-700">
        {{ successMessage }}
      </div>
      <div v-if="errorMessage" class="mb-6 rounded-2xl border border-red-200 bg-red-50 px-5 py-4 text-red-700">
        {{ errorMessage }}
      </div>

      <div class="grid gap-6 xl:grid-cols-[360px,1fr]">
        <aside class="space-y-6">
          <section class="overflow-hidden rounded-[28px] bg-white shadow-sm ring-1 ring-slate-200">
            <div class="bg-[radial-gradient(circle_at_top_left,_rgba(14,165,233,0.24),_transparent_52%),linear-gradient(135deg,#0f172a,#1e293b)] px-8 py-10 text-white">
              <div class="mx-auto flex h-36 w-36 items-center justify-center overflow-hidden rounded-full border-4 border-white/40 bg-white/10">
                <img
                  v-if="currentProfileImage && !imageBroken"
                  :src="currentProfileImage"
                  :alt="copy.profilePhoto"
                  class="h-full w-full object-cover"
                  @error="handleProfileImageError"
                >
                <img v-else-if="!defaultIconBroken" src="/iconly/Svg/Light/Profile.svg" alt="" aria-hidden="true" class="h-20 w-20 opacity-70" @error="defaultIconBroken = true">
                <span v-else class="material-symbols-outlined text-7xl text-white/70">person</span>
              </div>
              <div class="mt-6 text-center">
                <h2 class="text-2xl font-black">{{ fullName }}</h2>
                <p v-if="profileForm.current_position || profileForm.specialty" class="mt-2 text-sm text-white/80">
                  {{ [profileForm.current_position, profileForm.specialty].filter(Boolean).join(' • ') }}
                </p>
                <p v-if="profileForm.workplace" class="mt-1 text-sm text-white/70">{{ profileForm.workplace }}</p>
              </div>
            </div>

            <div class="space-y-3 p-6">
              <input ref="imageInput" type="file" accept="image/*" class="hidden" @change="handleFileSelection">
              <button type="button" class="w-full rounded-2xl bg-primary px-4 py-3 font-semibold text-white transition hover:bg-primary/90 disabled:opacity-50" :disabled="isImageLoading" @click="openFilePicker">
                {{ isImageLoading ? copy.uploading : copy.upload }}
              </button>
              <button type="button" class="w-full rounded-2xl border border-slate-300 px-4 py-3 font-semibold text-slate-700 transition hover:bg-slate-50 disabled:opacity-50" :disabled="isImageLoading || !authStore.user?.profile_image" @click="handleDeleteProfileImage">
                {{ copy.removePhoto }}
              </button>
            </div>
          </section>

          <section class="rounded-[28px] bg-white p-6 shadow-sm ring-1 ring-slate-200">
            <h3 class="text-lg font-black text-slate-900">{{ copy.visibleSections }}</h3>
            <div class="mt-4 flex flex-wrap gap-2">
              <span v-for="section in visibleResumeSections" :key="section.label" class="rounded-full bg-slate-100 px-3 py-1.5 text-xs font-semibold text-slate-700">
                {{ section.label }}
              </span>
              <span v-if="visibleResumeSections.length === 0" class="text-sm text-slate-500">{{ copy.noVisibleSections }}</span>
            </div>
          </section>
        </aside>

        <section class="rounded-[28px] bg-white p-8 shadow-sm ring-1 ring-slate-200">
          <h2 class="text-2xl font-black text-slate-900">{{ copy.personalInfo }}</h2>
          <p class="mt-2 text-sm text-slate-600">{{ copy.personalInfoText }}</p>

          <form class="mt-8 grid gap-5 md:grid-cols-2" @submit.prevent="handleUpdateProfile">
            <label class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">{{ copy.persianName }}</span>
              <input v-model="profileForm.first_name" type="text" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>
            <label class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">{{ copy.englishName }}</span>
              <input v-model="profileForm.last_name" type="text" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>
            <label class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">{{ copy.email }}</span>
              <input v-model="profileForm.email" type="email" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>
            <label class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">{{ copy.phone }}</span>
              <input v-model="profileForm.phone" type="tel" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>
            <label class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">{{ copy.city }}</span>
              <input v-model="profileForm.city" type="text" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>
            <label class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">{{ copy.specialty }}</span>
              <input v-model="profileForm.specialty" type="text" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>
            <label class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">{{ copy.currentPosition }}</span>
              <input v-model="profileForm.current_position" type="text" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>
            <label class="space-y-2">
              <span class="text-sm font-semibold text-slate-700">{{ copy.workplace }}</span>
              <input v-model="profileForm.workplace" type="text" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>
            <label class="space-y-2 md:col-span-2">
              <span class="text-sm font-semibold text-slate-700">{{ copy.experience }}</span>
              <input v-model.number="profileForm.experience" min="0" type="number" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
            </label>

            <div class="md:col-span-2 flex flex-wrap items-center justify-between gap-4 rounded-2xl bg-slate-50 px-5 py-4">
              <div class="text-sm text-slate-600">
                <div><span class="font-semibold text-slate-900">{{ copy.username }}:</span> {{ authStore.user?.username }}</div>
                <div><span class="font-semibold text-slate-900">{{ copy.joined }}:</span> {{ formatDate(authStore.user?.date_joined) }}</div>
              </div>
              <button type="submit" :disabled="isLoading" class="rounded-2xl bg-slate-900 px-6 py-3 font-semibold text-white transition hover:bg-slate-800 disabled:opacity-50">
                {{ isLoading ? copy.saving : copy.saveProfile }}
              </button>
            </div>
          </form>
        </section>
      </div>
    </div>

    <div v-if="showResumeModal" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/60 p-4 backdrop-blur-sm" @click.self="showResumeModal = false">
      <div class="max-h-[92vh] w-full max-w-4xl overflow-y-auto rounded-[32px] bg-white shadow-2xl ring-1 ring-slate-200">
        <div class="sticky top-0 z-10 flex items-center justify-between border-b border-slate-200 bg-white/95 px-7 py-5 backdrop-blur">
          <div>
            <h2 class="text-2xl font-black text-slate-900">{{ copy.editResume }}</h2>
            <p class="mt-1 text-sm text-slate-500">{{ copy.emptyFieldsHint }}</p>
          </div>
          <button class="rounded-full p-2 text-slate-500 transition hover:bg-slate-100 hover:text-slate-900" @click="showResumeModal = false">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>

        <form class="grid gap-5 p-7 md:grid-cols-2" @submit.prevent="handleUpdateResume">
          <label class="space-y-2">
            <span class="text-sm font-semibold text-slate-700">{{ copy.biography }}</span>
            <textarea v-model="resumeForm.bio" rows="4" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10"></textarea>
          </label>
          <label class="space-y-2">
            <span class="text-sm font-semibold text-slate-700">{{ copy.expertiseAreas }}</span>
            <textarea v-model="resumeForm.expertise_areas" rows="4" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10" :placeholder="copy.expertisePlaceholder"></textarea>
          </label>
          <label class="space-y-2 md:col-span-2">
            <span class="text-sm font-semibold text-slate-700">{{ copy.education }}</span>
            <textarea v-model="resumeForm.education" rows="4" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10"></textarea>
          </label>
          <label class="space-y-2 md:col-span-2">
            <span class="text-sm font-semibold text-slate-700">{{ copy.workExperience }}</span>
            <textarea v-model="resumeForm.work_experience" rows="5" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10"></textarea>
          </label>
          <label class="space-y-2">
            <span class="text-sm font-semibold text-slate-700">{{ copy.languages }}</span>
            <input v-model="resumeForm.languages" type="text" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
          </label>
          <label class="space-y-2">
            <span class="text-sm font-semibold text-slate-700">{{ copy.researchInterests }}</span>
            <input v-model="resumeForm.research_interests" type="text" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10">
          </label>
          <label class="space-y-2 md:col-span-2">
            <span class="text-sm font-semibold text-slate-700">{{ copy.publications }}</span>
            <textarea v-model="resumeForm.publications" rows="4" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10"></textarea>
          </label>
          <label class="space-y-2">
            <span class="text-sm font-semibold text-slate-700">{{ copy.awards }}</span>
            <textarea v-model="resumeForm.awards" rows="4" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10"></textarea>
          </label>
          <label class="space-y-2">
            <span class="text-sm font-semibold text-slate-700">{{ copy.certifications }}</span>
            <textarea v-model="resumeForm.certifications" rows="4" class="w-full rounded-2xl border border-slate-300 px-4 py-3 outline-none transition focus:border-primary focus:ring-4 focus:ring-primary/10"></textarea>
          </label>

          <div class="md:col-span-2 flex items-center justify-end gap-3 border-t border-slate-200 pt-4">
            <button type="button" class="rounded-2xl border border-slate-300 px-5 py-3 font-semibold text-slate-700 transition hover:bg-slate-50" @click="showResumeModal = false">
              {{ copy.cancel }}
            </button>
            <button type="submit" :disabled="isLoading" class="rounded-2xl bg-primary px-6 py-3 font-semibold text-white transition hover:bg-primary/90 disabled:opacity-50">
              {{ isLoading ? copy.saving : copy.saveResume }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useAuthStore } from '@/stores/auth'
import { resolveImageUrl } from '@/utils/assets'

const authStore = useAuthStore()
const { locale } = useI18n()

const profileForm = ref({
  first_name: '',
  last_name: '',
  email: '',
  phone: '',
  city: '',
  specialty: '',
  current_position: '',
  workplace: '',
  experience: 0,
})

const resumeForm = ref({
  bio: '',
  expertise_areas: '',
  education: '',
  work_experience: '',
  languages: '',
  research_interests: '',
  publications: '',
  awards: '',
  certifications: '',
})

const isLoading = ref(false)
const isImageLoading = ref(false)
const successMessage = ref('')
const errorMessage = ref('')
const imageInput = ref<HTMLInputElement | null>(null)
const imageBroken = ref(false)
const defaultIconBroken = ref(false)
const showResumeModal = ref(false)

const copy = computed(() => (
  locale.value === 'fa'
    ? {
        back: 'بازگشت به داشبورد',
        pageTitle: 'پروفایل عضو',
        pageText: 'پروفایل عمومی، بخش‌های رزومه و اطلاعاتی که در صفحه اعضا نمایش داده می‌شود را از اینجا مدیریت کنید.',
        editResume: 'ویرایش رزومه',
        profilePhoto: 'تصویر پروفایل',
        uploading: 'در حال بارگذاری...',
        upload: 'بارگذاری تصویر پروفایل',
        removePhoto: 'حذف تصویر',
        visibleSections: 'بخش‌های قابل نمایش رزومه',
        noVisibleSections: 'هنوز هیچ بخشی از رزومه شما نمایش داده نمی‌شود.',
        personalInfo: 'اطلاعات شخصی',
        personalInfoText: 'این اطلاعات با دیتابیس همگام است و در بخش‌های مختلف سایت استفاده می‌شود.',
        persianName: 'نام فارسی',
        englishName: 'نام کامل انگلیسی',
        email: 'ایمیل',
        phone: 'تلفن',
        city: 'شهر',
        specialty: 'تخصص',
        currentPosition: 'سمت فعلی',
        workplace: 'محل کار',
        experience: 'سال‌های سابقه',
        username: 'نام کاربری',
        joined: 'تاریخ عضویت',
        saving: 'در حال ذخیره...',
        saveProfile: 'ذخیره پروفایل',
        emptyFieldsHint: 'فیلدهای خالی در صفحه اعضا و رزومه عمومی نمایش داده نمی‌شوند.',
        biography: 'معرفی',
        expertiseAreas: 'حوزه‌های تخصص',
        expertisePlaceholder: 'هر مورد در یک خط یا با ویرگول جدا شود',
        education: 'تحصیلات',
        workExperience: 'سوابق کاری',
        languages: 'زبان‌ها',
        researchInterests: 'علایق پژوهشی',
        publications: 'انتشارات',
        awards: 'افتخارات',
        certifications: 'گواهی‌ها',
        cancel: 'انصراف',
        saveResume: 'ذخیره رزومه',
        member: 'عضو انجمن',
        profileUpdated: 'پروفایل با موفقیت به‌روزرسانی شد.',
        profileUpdateFailed: 'به‌روزرسانی پروفایل انجام نشد.',
        resumeUpdated: 'رزومه با موفقیت به‌روزرسانی شد.',
        resumeUpdateFailed: 'به‌روزرسانی رزومه انجام نشد.',
        photoUpdated: 'تصویر پروفایل با موفقیت به‌روزرسانی شد.',
        photoUploadFailed: 'بارگذاری تصویر انجام نشد.',
        photoRemoved: 'تصویر پروفایل حذف شد.',
        photoRemoveFailed: 'حذف تصویر انجام نشد.',
      }
    : {
        back: 'Back to Dashboard',
        pageTitle: 'Member Profile',
        pageText: 'Manage your public profile, resume sections, and the information shown on the members page.',
        editResume: 'Edit Resume',
        profilePhoto: 'Profile Photo',
        uploading: 'Uploading...',
        upload: 'Upload Profile Photo',
        removePhoto: 'Remove Photo',
        visibleSections: 'Visible Resume Sections',
        noVisibleSections: 'No resume section is visible yet.',
        personalInfo: 'Personal Information',
        personalInfoText: 'This information is synced with the database and used across the site.',
        persianName: 'Persian Name',
        englishName: 'English Full Name',
        email: 'Email',
        phone: 'Phone',
        city: 'City',
        specialty: 'Specialty',
        currentPosition: 'Current Position',
        workplace: 'Workplace',
        experience: 'Years of Experience',
        username: 'Username',
        joined: 'Joined',
        saving: 'Saving...',
        saveProfile: 'Save Profile',
        emptyFieldsHint: 'Empty fields will not appear on the members page or the public resume.',
        biography: 'Biography',
        expertiseAreas: 'Areas of Expertise',
        expertisePlaceholder: 'One per line or comma-separated',
        education: 'Education',
        workExperience: 'Work Experience',
        languages: 'Languages',
        researchInterests: 'Research Interests',
        publications: 'Publications',
        awards: 'Awards and Honors',
        certifications: 'Certifications',
        cancel: 'Cancel',
        saveResume: 'Save Resume',
        member: 'Member',
        profileUpdated: 'Profile updated successfully.',
        profileUpdateFailed: 'Failed to update profile.',
        resumeUpdated: 'Resume updated successfully.',
        resumeUpdateFailed: 'Failed to update resume.',
        photoUpdated: 'Profile photo updated successfully.',
        photoUploadFailed: 'Failed to upload image.',
        photoRemoved: 'Profile photo removed.',
        photoRemoveFailed: 'Failed to remove image.',
      }
))

function syncForms() {
  const user = authStore.user
  if (!user) return

  profileForm.value = {
    first_name: user.first_name || '',
    last_name: user.last_name || '',
    email: user.email || '',
    phone: user.phone || '',
    city: user.city || '',
    specialty: user.specialty || '',
    current_position: user.current_position || '',
    workplace: user.workplace || '',
    experience: Number(user.experience || 0),
  }

  resumeForm.value = {
    bio: user.bio || '',
    expertise_areas: user.expertise_areas || '',
    education: user.education || '',
    work_experience: user.work_experience || '',
    languages: user.languages || '',
    research_interests: user.research_interests || '',
    publications: user.publications || '',
    awards: user.awards || '',
    certifications: user.certifications || '',
  }
}

onMounted(syncForms)

const currentProfileImage = computed(() => {
  const image = authStore.user?.profile_image
  return image ? resolveImageUrl(image, '') : ''
})

const fullName = computed(() => {
  const persian = profileForm.value.first_name?.trim()
  const english = profileForm.value.last_name?.trim()
  if (locale.value === 'fa') {
    return persian || english || authStore.user?.username || copy.value.member
  }
  return english || persian || authStore.user?.username || copy.value.member
})

const visibleResumeSections = computed(() => {
  const sections = [
    { label: copy.value.biography, value: resumeForm.value.bio },
    { label: copy.value.expertiseAreas, value: resumeForm.value.expertise_areas },
    { label: copy.value.education, value: resumeForm.value.education },
    { label: copy.value.workExperience, value: resumeForm.value.work_experience || profileForm.value.experience },
    { label: copy.value.languages, value: resumeForm.value.languages },
    { label: copy.value.researchInterests, value: resumeForm.value.research_interests },
    { label: copy.value.publications, value: resumeForm.value.publications },
    { label: copy.value.awards, value: resumeForm.value.awards },
    { label: copy.value.certifications, value: resumeForm.value.certifications },
  ]
  return sections.filter((section) => String(section.value || '').trim())
})

async function handleUpdateProfile() {
  isLoading.value = true
  successMessage.value = ''
  errorMessage.value = ''

  const result = await authStore.updateProfile(profileForm.value)
  if (result.success) {
    successMessage.value = result.message || copy.value.profileUpdated
    syncForms()
  } else {
    errorMessage.value = result.error || copy.value.profileUpdateFailed
  }

  isLoading.value = false
}

async function handleUpdateResume() {
  isLoading.value = true
  successMessage.value = ''
  errorMessage.value = ''

  const result = await authStore.updateResume({
    ...resumeForm.value,
    city: profileForm.value.city,
    specialty: profileForm.value.specialty,
    current_position: profileForm.value.current_position,
    workplace: profileForm.value.workplace,
    experience: profileForm.value.experience,
  })

  if (result.success) {
    successMessage.value = result.message || copy.value.resumeUpdated
    showResumeModal.value = false
    syncForms()
  } else {
    errorMessage.value = result.error || copy.value.resumeUpdateFailed
  }

  isLoading.value = false
}

function openFilePicker() {
  imageInput.value?.click()
}

async function handleFileSelection(event: Event) {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  if (!file) return

  isImageLoading.value = true
  imageBroken.value = false
  successMessage.value = ''
  errorMessage.value = ''

  const result = await authStore.uploadProfileImage(file)
  if (result.success) {
    successMessage.value = result.message || copy.value.photoUpdated
  } else {
    errorMessage.value = result.error || copy.value.photoUploadFailed
  }

  target.value = ''
  isImageLoading.value = false
}

async function handleDeleteProfileImage() {
  isImageLoading.value = true
  successMessage.value = ''
  errorMessage.value = ''

  const result = await authStore.deleteProfileImage()
  if (result.success) {
    imageBroken.value = false
    successMessage.value = result.message || copy.value.photoRemoved
  } else {
    errorMessage.value = result.error || copy.value.photoRemoveFailed
  }

  isImageLoading.value = false
}

function handleProfileImageError() {
  imageBroken.value = true
}

function formatDate(dateString?: string) {
  if (!dateString) return '-'
  return new Intl.DateTimeFormat(locale.value === 'fa' ? 'fa-IR' : 'en-US', { dateStyle: 'medium' }).format(new Date(dateString))
}
</script>
