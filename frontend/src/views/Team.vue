<template>
  <div class="page-shell team-view position-relative">
    <span class="team-bubble bubble-1 blurred-bubble"></span>
    <span class="team-bubble bubble-2 blurred-bubble"></span>
    <span class="team-bubble bubble-3 blurred-bubble"></span>
    <section id="team-hero" class="team-hero-section page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center min-vh-80">
          <div class="col-md-6">
            <div class="team-hero-content animate__animated animate__fadeInRight">
              <span class="soft-badge mb-3"><i class="fa fa-users"></i> {{ $t('team.badge') }}</span>
              <h1 class="display-4 fw-bold mb-4">{{ $t('team.title') }}</h1>
              <p class="lead mb-4">{{ $t('team.subtitle') }}</p>
              <p class="mb-4 text-muted">{{ $t('team.description') }}</p>
              <div class="team-hero-buttons d-flex flex-wrap gap-2">
                <a class="soft-button primary animate__animated animate__pulse" href="#team-members">
                  <i class="fa fa-arrow-right"></i>
                  {{ $t('team.teamMembers') }}
                </a>
                <a class="soft-button outline" href="#expertise">
                  <i class="fa fa-lightbulb-o"></i>
                  {{ $t('team.expertise') }}
                </a>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="team-hero-image animate__animated animate__fadeInLeft">
              <div class="team-hero-image-wrapper image-frame image-frame--wide">
                <img :src="getAssetUrl('img/hero-team.svg')" class="img-fluid" alt="تیم متخصص">
                <div class="floating-elements">
                  <div class="floating-icon floating-icon-1">
                    <i class="fa fa-user-md"></i>
                  </div>
                  <div class="floating-icon floating-icon-2">
                    <i class="fa fa-stethoscope"></i>
                  </div>
                  <div class="floating-icon floating-icon-3">
                    <i class="fa fa-graduation-cap"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="team-members" class="p_3 glass-section">
      <div class="container-xl">
        <div class="row">
          <div class="col-md-12 text-center mb-5 section-heading">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">{{ $t('team.title') }}</h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('team.subtitle') }}</p>
            <p class="text-muted mt-3 animate__animated animate__fadeInUp animate__delay-2s" style="max-width: 800px; margin: 0 auto;">
              {{ $t('team.membersDescription') }}
            </p>
          </div>
        </div>
        <div class="row justify-content-center mb-4">
          <div class="col-lg-6 col-md-8">
            <div class="member-search-card animate__animated animate__fadeInUp animate__delay-2s">
              <div class="member-search-icon">
                <i class="fa fa-search"></i>
              </div>
              <input
                type="text"
                class="member-search-input"
                :placeholder="$t('team.search')"
                v-model="searchQuery"
                :aria-label="$t('team.search')"
              >
              <button
                v-if="searchQuery"
                type="button"
                class="member-search-clear"
                @click="clearSearch"
                aria-label="پاک کردن جستجو"
              >
                <i class="fa fa-times"></i>
              </button>
            </div>
          </div>
        </div>
        <div v-if="loading" class="row">
          <div class="col-12 text-center">
            <div class="spinner-border text-primary" role="status">
              <span class="visually-hidden">در حال بارگذاری...</span>
            </div>
          </div>
        </div>
        <div v-else>
          <div v-if="memberError" class="row">
            <div class="col-12">
              <div class="alert alert-danger border-0 rounded-4 shadow-sm d-flex align-items-center gap-2">
                <i class="fa fa-exclamation-circle"></i>
                <span>{{ memberError }}</span>
              </div>
            </div>
          </div>
          <div v-else-if="filteredMembers.length > 0" class="row g-3">
            <div v-for="(member, index) in filteredMembers" :key="member.id" class="col-md-2 col-sm-4 col-lg-2 col-6">
              <div 
                class="team-card glass-card text-center animate__animated animate__fadeInUp cursor-pointer" 
                :style="{ animationDelay: (index * 0.1) + 's' }"
                @click="openMemberModal(member)"
                style="cursor: pointer; transition: transform 0.2s;"
                @mouseenter="(e) => { const el = e.currentTarget as HTMLElement; if (el) el.style.transform = 'scale(1.05)'; }"
                @mouseleave="(e) => { const el = e.currentTarget as HTMLElement; if (el) el.style.transform = 'scale(1)'; }"
              >
                <div class="team-image mb-2">
                  <img 
                    v-if="getMemberImage(member)"
                    :src="getMemberImage(member)" 
                    :alt="member.full_name" 
                    class="img-fluid rounded"
                    style="width: 100%; height: 150px; object-fit: cover; border-radius: 8px !important;"
                    @error="handleImageError($event)"
                    :key="`member-${member.id}-${member.profile_image || 'default'}`"
                  >
                  <div 
                    v-else
                    class="no-image-placeholder d-flex align-items-center justify-content-center"
                    style="width: 100%; height: 150px; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 8px; border: 2px dashed #dee2e6;"
                  >
                    <i class="fa fa-user fa-3x text-muted"></i>
                  </div>
                </div>
                <h6 class="fw-bold mb-0" style="font-size: 0.9rem;">{{ member.displayName || getMemberName(member) }}</h6>
              </div>
            </div>
          </div>
          <div v-else class="row">
            <div class="col-12 text-center">
              <p class="text-muted">{{ $t('team.noResults') }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Member Detail Modal -->
    <div v-if="selectedMember" class="modal fade show" :class="{ 'd-block': showModal }" tabindex="-1" style="background-color: rgba(0,0,0,0.5);" @click.self="closeModal">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content" style="border-radius: 15px;">
          <div class="modal-header border-0 pb-0">
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <div class="modal-body pt-0">
            <div class="text-center mb-4">
              <img 
                v-if="getMemberImage(selectedMember)"
                :src="getMemberImage(selectedMember)" 
                :alt="selectedMember.full_name" 
                class="img-fluid rounded mb-3"
                style="width: 150px; height: 150px; object-fit: cover; border-radius: 12px !important;"
                @error="handleImageError($event)"
                :key="`modal-${selectedMember.id}-${selectedMember.profile_image || 'default'}`"
              >
              <div 
                v-else
                class="no-image-placeholder d-flex align-items-center justify-content-center mb-3 mx-auto"
                style="width: 150px; height: 150px; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 12px; border: 2px dashed #dee2e6;"
              >
                <i class="fa fa-user fa-4x text-muted"></i>
              </div>
              <h4 class="fw-bold mb-2">{{ selectedMember ? getMemberName(selectedMember) : '' }}</h4>
            </div>
            <div class="member-details" style="max-height: 70vh; overflow-y: auto;">
              <div v-if="selectedMember.city" class="mb-3">
                <i class="fa fa-map-marker col_blue me-2"></i>
                <strong>{{ $t('profile.city') }}:</strong> {{ selectedMember.city }}
              </div>
              <div v-if="selectedMember.specialty" class="mb-3">
                <i class="fa fa-stethoscope col_blue me-2"></i>
                <strong>{{ $t('profile.specialty') }}:</strong> {{ selectedMember.specialty }}
              </div>
              <div v-if="selectedMember.experience" class="mb-3">
                <i class="fa fa-briefcase col_blue me-2"></i>
                <strong>{{ $t('profile.experience') }}:</strong> {{ selectedMember.experience }} {{ $t('common.year') }}
              </div>
              <div v-if="selectedMember.rating" class="mb-3">
                <i class="fa fa-star col_blue me-2"></i>
                <strong>{{ $t('profile.rating') }}:</strong> 
                <span class="text-warning">
                  {{ selectedMember.rating.toFixed(1) }}
                  <i class="fa fa-star text-warning"></i>
                </span>
              </div>
              <div v-if="selectedMember.languages" class="mb-3">
                <i class="fa fa-language col_blue me-2"></i>
                <strong>{{ $t('profile.languages') }}:</strong> {{ selectedMember.languages }}
              </div>
              
              <div v-if="selectedMember.bio" class="mt-3 pt-3 border-top">
                <p class="text-muted" style="text-align: justify; line-height: 1.8; white-space: pre-line;">
                  {{ selectedMember.bio }}
                </p>
              </div>
              
              <div v-if="selectedMember.education" class="mt-3 pt-3 border-top">
                <h6 class="fw-bold mb-2"><i class="fa fa-graduation-cap col_blue me-2"></i>{{ $t('profile.education') }}</h6>
                <p class="text-muted" style="text-align: justify; line-height: 1.8; white-space: pre-line;">
                  {{ selectedMember.education }}
                </p>
              </div>
              
              <div v-if="selectedMember.publications" class="mt-3 pt-3 border-top">
                <h6 class="fw-bold mb-2"><i class="fa fa-book col_blue me-2"></i>{{ $t('profile.publications') }}</h6>
                <p class="text-muted" style="text-align: justify; line-height: 1.8; white-space: pre-line;">
                  {{ selectedMember.publications }}
                </p>
              </div>
              
              <div v-if="selectedMember.awards" class="mt-3 pt-3 border-top">
                <h6 class="fw-bold mb-2"><i class="fa fa-trophy col_blue me-2"></i>{{ $t('profile.awards') }}</h6>
                <p class="text-muted" style="text-align: justify; line-height: 1.8; white-space: pre-line;">
                  {{ selectedMember.awards }}
                </p>
              </div>
              
              <div v-if="selectedMember.certifications" class="mt-3 pt-3 border-top">
                <h6 class="fw-bold mb-2"><i class="fa fa-certificate col_blue me-2"></i>{{ $t('profile.certifications') }}</h6>
                <p class="text-muted" style="text-align: justify; line-height: 1.8; white-space: pre-line;">
                  {{ selectedMember.certifications }}
                </p>
              </div>
              
              <div v-if="selectedMember.research_interests" class="mt-3 pt-3 border-top">
                <h6 class="fw-bold mb-2"><i class="fa fa-microscope col_blue me-2"></i>{{ $t('profile.researchInterests') }}</h6>
                <p class="text-muted" style="text-align: justify; line-height: 1.8; white-space: pre-line;">
                  {{ selectedMember.research_interests }}
                </p>
              </div>
              
              <div v-if="!selectedMember.bio && !selectedMember.education && !selectedMember.publications && !selectedMember.awards && !selectedMember.certifications && !selectedMember.research_interests" class="mt-4 pt-3 border-top">
                <p class="text-muted" style="text-align: justify; line-height: 1.8;">
                  {{ selectedMember.full_name }} یکی از اعضای فعال انجمن علمی ریه کودکان است که با تعهد و تخصص خود در زمینه بهبود سلامت تنفسی کودکان تلاش می‌کند.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <section id="expertise" class="p_3 glass-section">
      <div class="container-xl">
        <div class="row">
          <div class="col-md-12 text-center mb-5 section-heading">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">{{ $t('team.expertise') }}</h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('team.expertiseSubtitle') }}</p>
          </div>
        </div>
        <div class="row g-4">
          <div class="col-md-6 col-lg-4" v-for="(expertiseItem, index) in expertiseCards" :key="expertiseItem.title">
            <div class="expertise-card glass-card text-center p-4 animate__animated animate__fadeInUp" :class="'animate__delay-' + (index + 2) + 's'">
              <div class="expertise-icon mb-4">
                <i :class="'fa fa-3x col_blue ' + expertiseItem.icon"></i>
              </div>
              <h5 class="fw-bold mb-3">{{ expertiseItem.title }}</h5>
              <p class="text-muted">{{ expertiseItem.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="team-stats" class="p_3 home-stats-section">
      <div class="container-xl">
        <div class="row text-center">
          <div class="col-md-3 col-sm-6 mb-4" v-for="(stat, index) in teamStats" :key="stat.title">
            <div class="stat-item glass-card animate__animated animate__fadeInUp" :class="'animate__delay-' + (index + 1) + 's'">
              <div class="stat-icon mb-3">
                <i :class="'fa fa-2x ' + stat.icon"></i>
              </div>
              <h2 class="fw-bold counter" :data-target="stat.target">0</h2>
              <p class="mb-0">{{ stat.title }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue';
import { useRoute } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { getAssetUrl } from '@/utils/assets';
import { getApiUrl } from '@/utils/api';

const { t } = useI18n();

interface Member {
  id: number;
  persian_name: string;
  english_name: string;
  full_name: string; // برای سازگاری با کد موجود
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

const { locale } = useI18n();

const members = ref<Member[]>([]);
const loading = ref(true);
const selectedMember = ref<Member | null>(null);
const showModal = ref(false);
const searchQuery = ref('');
const memberError = ref<string | null>(null);

const getMemberName = (member: Member): string => {
  if (locale.value === 'fa') {
    return member.english_name || member.persian_name || member.display_name || 'Unknown';
  } else {
    return member.persian_name || member.english_name || member.display_name || 'نامشخص';
  }
};

const expertiseCards = computed(() => [
  { icon: 'fa-heartbeat', title: t('team.expertise1'), description: t('team.expertise1Desc') },
  { icon: 'fa-lungs', title: t('team.expertise2'), description: t('team.expertise2Desc') },
  { icon: 'fa-allergies', title: t('team.expertise3'), description: t('team.expertise3Desc') },
  { icon: 'fa-microscope', title: t('team.expertise4'), description: t('team.expertise4Desc') },
  { icon: 'fa-graduation-cap', title: t('team.expertise5'), description: t('team.expertise5Desc') },
  { icon: 'fa-users', title: t('team.expertise6'), description: t('team.expertise6Desc') }
]);

const teamStats = computed(() => [
  { icon: 'fa-user-md', title: t('team.stat1'), target: '25' },
  { icon: 'fa-graduation-cap', title: t('team.stat2'), target: '15' },
  { icon: 'fa-book', title: t('team.stat3'), target: '50' },
  { icon: 'fa-trophy', title: t('team.stat4'), target: '10' }
]);

function getMemberImage(member: Member | number): string | null {
  let memberObj: Member | undefined;
  
  if (typeof member === 'number') {
    memberObj = members.value.find(m => m.id === member);
  } else {
    memberObj = member;
  }
  
  if (memberObj && 
      memberObj.profile_image && 
      memberObj.profile_image.trim() !== '' && 
      memberObj.profile_image !== 'null' && 
      memberObj.profile_image !== 'undefined') {
    
    const imageUrl = memberObj.profile_image.trim();
    let finalUrl = '';
    
    // If URL is already absolute, use it directly
    if (imageUrl.startsWith('http://') || imageUrl.startsWith('https://')) {
      finalUrl = imageUrl;
    }
    // If URL starts with /, it's a relative path (like /media/profile_images/...)
    // Use it directly - nginx will proxy /media/ to backend
    else if (imageUrl.startsWith('/')) {
      finalUrl = imageUrl;
    }
    // Otherwise, prepend / to make it relative from root
    else {
      finalUrl = `/${imageUrl}`;
    }
    
    // Add cache busting to force refresh
    const timestamp = Date.now();
    const separator = finalUrl.includes('?') ? '&' : '?';
    return `${finalUrl}${separator}t=${timestamp}`;
  }
  
  return null;
}

function handleImageError(event: Event) {
  const img = event.target as HTMLImageElement;
  if (img.parentElement) {
    const placeholder = img.parentElement.querySelector('.no-image-placeholder');
    if (placeholder) {
      img.style.display = 'none';
      (placeholder as HTMLElement).style.display = 'flex';
    }
  }
}

async function fetchMembers() {
  try {
    loading.value = true;
    memberError.value = null;
    
    const timestamp = Date.now();
    const apiUrl = getApiUrl(`/api/accounts/members/?t=${timestamp}&v=${Math.random()}`);

    const response = await fetch(apiUrl, {
      headers: {
        'Accept': 'application/json',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0'
      }
      // credentials: 'include' // ممکن است برای درخواست Cross-Origin نیاز نباشد یا باعث خطا شود. در صورت بروز مشکل آن را حذف یا اضافه کنید
    });

    if (!response.ok) {
      // تلاش برای خواندن متن خطا از سرور
      let errorText = `خطای سرور (${response.status})`;
      try {
        const errorData = await response.json();
        errorText = errorData.detail || errorData.message || JSON.stringify(errorData);
      } catch (e) {
         errorText = await response.text();
      }
      throw new Error(errorText || `خطای سرور (${response.status})`);
    }

    const data = await response.json();

    if (Array.isArray(data)) { // اگر API مستقیما آرایه برمی‌گرداند
      members.value = data;
    } else if (data && Array.isArray(data.members)) { // اگر API یک آبجکت شامل آرایه برمی‌گرداند
      members.value = data.members;
    } else {
      throw new Error('فرمت پاسخ دریافت شده از سرور نامعتبر است.');
    }
  } catch (error) {
    console.error('Error fetching members:', error);
    memberError.value = error instanceof Error ? error.message : 'خطایی هنگام دریافت اعضا رخ داد. لطفاً اتصال خود را بررسی کرده و دوباره تلاش کنید.';
    if (error instanceof TypeError && error.message.includes('Failed to fetch')) {
        memberError.value = 'اتصال به سرور برقرار نشد. ممکن است به دلیل مشکل در شبکه یا خطای CORS باشد. (F12 را زده و کنسول را بررسی کنید)';
    }
  } finally {
    loading.value = false;
  }
}


const filteredMembers = computed(() => {
  const query = searchQuery.value.trim().toLowerCase();
  let filtered = members.value;
  
  if (query) {
    filtered = members.value.filter(member => {
      const searchableFields = [
        member.display_name,
        member.persian_name,
        member.english_name,
        member.specialty,
        member.city
      ];

      return searchableFields.some(field => {
        if (!field) return false;
        return String(field).toLowerCase().includes(query);
      });
    });
  }
  
  return filtered.map(member => ({
    ...member,
    displayName: getMemberName(member)
  }));
});

function clearSearch() {
  searchQuery.value = '';
}

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

function animateCounter(element: HTMLElement) {
  const target = parseInt(element.getAttribute('data-target') || '0');
  const duration = 1200;
  const increment = target / (duration / 16);
  let current = 0;
  
  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      current = target;
      clearInterval(timer);
    }
    element.textContent = Math.floor(current).toString();
  }, 16);
}

const route = useRoute();

watch(() => route.path, (newPath) => {
  if (newPath.includes('/team')) { // برای سازگاری با روت‌های مختلف
    fetchMembers();
  }
}, { immediate: true });

onMounted(() => {
  // fetchMembers(); // به دلیل وجود watch immediate، دیگر نیازی به این خط نیست

  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate__animated');
        if (entry.target.classList.contains('counter')) {
          animateCounter(entry.target as HTMLElement);
          obs.unobserve(entry.target);
        }
      }
    });
  }, observerOptions);

  // برای اینکه انیمیشن‌ها هر بار اجرا شوند، باید observer را روی المان‌های جدید اعمال کنیم
  // این کار را می‌توان با یک watch روی filteredMembers انجام داد یا از یک directive سفارشی استفاده کرد
  // در اینجا برای سادگی، observer فقط یک بار در onMounted اجرا می‌شود
  setTimeout(() => {
    document.querySelectorAll('.animate__fadeInUp, .animate__fadeInLeft, .animate__fadeInRight, .counter').forEach(el => {
      observer.observe(el);
    });
  }, 500); // تاخیر برای اطمینان از رندر شدن المان‌ها

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const targetId = (this as HTMLAnchorElement).getAttribute('href');
      if (targetId) {
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          targetElement.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      }
    });
  });
});
</script>

<style scoped>
.member-search-card {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.9rem 1.1rem;
  border-radius: 20px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(235, 245, 255, 0.95) 100%);
  box-shadow: 0 18px 45px rgba(13, 110, 253, 0.08);
  border: 1px solid rgba(13, 110, 253, 0.08);
  transition: all 0.3s ease;
  direction: rtl;
}

.member-search-card:focus-within {
  box-shadow: 0 22px 55px rgba(13, 110, 253, 0.16);
  border-color: rgba(13, 110, 253, 0.35);
  transform: translateY(-2px);
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(222, 238, 255, 0.98) 100%);
}

.member-search-icon {
  color: #0d6efd;
  font-size: 1.1rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.member-search-input {
  flex: 1;
  border: 0;
  background: transparent;
  font-size: 1rem;
  color: #1a2a3a;
  padding: 0.1rem 0.3rem;
}

.member-search-input:focus {
  outline: none;
}

.member-search-input::placeholder {
  color: rgba(26, 42, 58, 0.55);
  font-weight: 300;
}

.member-search-clear {
  border: 0;
  background: rgba(13, 110, 253, 0.12);
  color: #0d6efd;
  padding: 0.45rem 0.8rem;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.member-search-clear:hover {
  background: #0d6efd;
  color: #ffffff;
}

.member-search-clear i {
  font-size: 0.9rem;
}

@media (max-width: 575px) {
  .member-search-card {
    border-radius: 16px;
    padding: 0.8rem 1rem;
  }

  .member-search-input {
    font-size: 0.95rem;
  }
}
</style>
