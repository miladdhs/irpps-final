<template>
  <div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100">
    <div class="relative flex min-h-screen flex-col overflow-x-hidden">
      <main class="mx-auto w-full max-w-[1280px] grow px-6 py-8 lg:px-10">
        <!-- Header Section -->
        <div class="mb-12 flex flex-col gap-4">
          <div class="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary w-fit">
            <span class="material-symbols-outlined text-[20px]">groups</span>
            {{ $t('team.badge') }}
          </div>
          <h1 class="text-4xl font-black text-slate-900 dark:text-white md:text-5xl">{{ $t('team.title') }}</h1>
          <p class="text-lg text-slate-600 dark:text-slate-400 max-w-2xl">{{ $t('team.subtitle') }}</p>
        </div>

        <!-- Search Bar -->
        <div class="mb-8 flex w-full max-w-2xl overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm dark:border-slate-800 dark:bg-slate-900">
          <div class="flex flex-1 items-center px-4">
            <span class="material-symbols-outlined text-slate-400">search</span>
            <input 
              v-model="searchQuery"
              class="w-full border-none bg-transparent py-4 text-sm focus:ring-0" 
              :placeholder="$t('team.search')" 
              type="text"
            />
          </div>
          <button 
            v-if="searchQuery"
            @click="searchQuery = ''"
            class="bg-slate-100 px-6 font-medium text-slate-600 hover:bg-slate-200 transition-colors dark:bg-slate-800 dark:text-slate-400 dark:hover:bg-slate-700"
          >
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>

        <!-- Loading State -->
        <div v-if="loading" class="flex items-center justify-center py-20">
          <div class="flex flex-col items-center gap-4">
            <div class="h-12 w-12 animate-spin rounded-full border-4 border-primary border-t-transparent"></div>
            <p class="text-slate-500">{{ $t('common.loading') }}</p>
          </div>
        </div>

        <!-- Error State -->
        <div v-else-if="memberError" class="rounded-xl border border-red-200 bg-red-50 p-6 dark:border-red-900 dark:bg-red-950">
          <div class="flex items-center gap-3">
            <span class="material-symbols-outlined text-red-600">error</span>
            <p class="text-red-600 dark:text-red-400">{{ memberError }}</p>
          </div>
        </div>

        <!-- Members Grid -->
        <div v-else-if="filteredMembers.length > 0" class="grid grid-cols-2 gap-4 md:grid-cols-4 lg:grid-cols-6">
          <div 
            v-for="member in filteredMembers" 
            :key="member.id"
            class="group cursor-pointer rounded-xl border border-slate-200 bg-white p-4 shadow-sm transition-all hover:shadow-lg hover:border-primary/30 dark:border-slate-800 dark:bg-slate-900"
            @click="openMemberModal(member)"
          >
            <div class="mb-3 aspect-square overflow-hidden rounded-lg bg-slate-100 dark:bg-slate-800">
              <img 
                v-if="getMemberImage(member)"
                :src="getMemberImage(member)" 
                :alt="getMemberName(member)" 
                class="h-full w-full object-cover transition-transform group-hover:scale-110"
                @error="handleImageError($event)"
              />
              <div 
                v-else
                class="flex h-full w-full items-center justify-center"
              >
                <span class="material-symbols-outlined text-4xl text-slate-400">person</span>
              </div>
            </div>
            <h3 class="text-center text-sm font-bold line-clamp-2">{{ getMemberName(member) }}</h3>
          </div>
        </div>

        <!-- No Results -->
        <div v-else class="flex flex-col items-center justify-center py-20">
          <span class="material-symbols-outlined text-6xl text-slate-300 mb-4">person_search</span>
          <p class="text-slate-500">{{ $t('team.noResults') }}</p>
        </div>

        <!-- Stats Section -->
        <div class="mt-16 grid grid-cols-2 gap-6 md:grid-cols-4">
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">person</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">{{ members.length }}+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">{{ $t('team.stat1') }}</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">school</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">15+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">{{ $t('team.stat2') }}</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">menu_book</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">50+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">{{ $t('team.stat3') }}</div>
          </div>
          <div class="rounded-xl border border-slate-200 bg-white p-6 text-center shadow-sm dark:border-slate-800 dark:bg-slate-900">
            <div class="mb-2 flex justify-center">
              <span class="material-symbols-outlined text-4xl text-primary">emoji_events</span>
            </div>
            <div class="text-3xl font-black text-slate-900 dark:text-white">10+</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">{{ $t('team.stat4') }}</div>
          </div>
        </div>
      </main>
    </div>

    <!-- Member Modal -->
    <div 
      v-if="showModal && selectedMember" 
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4"
      @click.self="closeModal"
    >
      <div class="max-h-[90vh] w-full max-w-2xl overflow-y-auto rounded-xl border border-slate-200 bg-white shadow-xl dark:border-slate-800 dark:bg-slate-900">
        <div class="sticky top-0 flex items-center justify-between border-b border-slate-200 bg-white p-6 dark:border-slate-800 dark:bg-slate-900">
          <h2 class="text-xl font-bold">{{ getMemberName(selectedMember) }}</h2>
          <button @click="closeModal" class="rounded-lg p-2 hover:bg-slate-100 dark:hover:bg-slate-800">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>
        <div class="p-6">
          <div class="mb-6 flex justify-center">
            <div class="h-32 w-32 overflow-hidden rounded-full bg-slate-100 dark:bg-slate-800">
              <img 
                v-if="getMemberImage(selectedMember)"
                :src="getMemberImage(selectedMember)" 
                :alt="getMemberName(selectedMember)" 
                class="h-full w-full object-cover"
                @error="handleImageError($event)"
              />
              <div v-else class="flex h-full w-full items-center justify-center">
                <span class="material-symbols-outlined text-6xl text-slate-400">person</span>
              </div>
            </div>
          </div>
          
          <div class="flex flex-col gap-4">
            <div v-if="selectedMember.city" class="flex items-start gap-3">
              <span class="material-symbols-outlined text-primary">location_on</span>
              <div>
                <div class="text-sm font-medium text-slate-500 dark:text-slate-400">{{ $t('profile.city') }}</div>
                <div class="font-medium">{{ selectedMember.city }}</div>
              </div>
            </div>
            
            <div v-if="selectedMember.specialty" class="flex items-start gap-3">
              <span class="material-symbols-outlined text-primary">medical_services</span>
              <div>
                <div class="text-sm font-medium text-slate-500 dark:text-slate-400">{{ $t('profile.specialty') }}</div>
                <div class="font-medium">{{ selectedMember.specialty }}</div>
              </div>
            </div>
            
            <div v-if="selectedMember.bio" class="flex items-start gap-3">
              <span class="material-symbols-outlined text-primary">info</span>
              <div>
                <div class="text-sm font-medium text-slate-500 dark:text-slate-400">{{ $t('profile.bio') }}</div>
                <div class="leading-relaxed text-slate-600 dark:text-slate-400">{{ selectedMember.bio }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useI18n } from 'vue-i18n';
import { getApiUrl } from '@/utils/api';

const { locale } = useI18n();

interface Member {
  id: number;
  persian_name: string;
  english_name: string;
  full_name: string;
  display_name: string;
  email: string;
  phone: string;
  city: string;
  specialty: string;
  experience: number;
  rating: number;
  bio: string;
  profile_image: string;
  education: string;
  publications: string;
  awards: string;
  certifications: string;
  research_interests: string;
  languages: string;
}

const members = ref<Member[]>([]);
const loading = ref(true);
const memberError = ref<string | null>(null);
const searchQuery = ref('');
const selectedMember = ref<Member | null>(null);
const showModal = ref(false);

const getMemberName = (member: Member): string => {
  if (locale.value === 'fa') {
    return member.persian_name || member.english_name || member.display_name || 'نامشخص';
  } else {
    return member.english_name || member.persian_name || member.display_name || 'Unknown';
  }
};

function getMemberImage(member: Member): string | null {
  if (member && member.profile_image && member.profile_image.trim() !== '' && 
      member.profile_image !== 'null' && member.profile_image !== 'undefined') {
    const imageUrl = member.profile_image.trim();
    if (imageUrl.startsWith('http://') || imageUrl.startsWith('https://')) {
      return imageUrl;
    } else if (imageUrl.startsWith('/')) {
      return imageUrl;
    } else {
      return `/${imageUrl}`;
    }
  }
  return null;
}

function handleImageError(event: Event) {
  const img = event.target as HTMLImageElement;
  img.style.display = 'none';
}

async function fetchMembers() {
  try {
    loading.value = true;
    memberError.value = null;
    
    const timestamp = Date.now();
    const apiUrl = getApiUrl(`/api/accounts/members/?t=${timestamp}`);
    const response = await fetch(apiUrl, {
      headers: {
        'Accept': 'application/json',
        'Cache-Control': 'no-cache'
      }
    });

    if (!response.ok) {
      throw new Error(`خطای سرور (${response.status})`);
    }

    const data = await response.json();
    members.value = Array.isArray(data) ? data : (data.members || []);
  } catch (error) {
    console.error('Error fetching members:', error);
    memberError.value = 'خطا در دریافت اطلاعات اعضا';
  } finally {
    loading.value = false;
  }
}

const filteredMembers = computed(() => {
  const query = searchQuery.value.trim().toLowerCase();
  if (!query) return members.value;
  
  return members.value.filter(member => {
    const searchableFields = [
      member.display_name,
      member.persian_name,
      member.english_name,
      member.specialty,
      member.city
    ];
    return searchableFields.some(field => 
      field && String(field).toLowerCase().includes(query)
    );
  });
});

function openMemberModal(member: Member) {
  selectedMember.value = member;
  showModal.value = true;
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  showModal.value = false;
  selectedMember.value = null;
  document.body.style.overflow = 'auto';
}

onMounted(() => {
  fetchMembers();
});
</script>
