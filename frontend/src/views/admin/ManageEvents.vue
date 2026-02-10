<template>
  <div class="min-h-screen bg-gray-50 py-8 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <div class="flex justify-between items-center mb-8">
        <div>
          <h1 class="text-3xl font-bold text-gray-900">مدیریت رویدادها</h1>
          <p class="text-gray-600 mt-2">افزودن، ویرایش و حذف رویدادها</p>
        </div>
        <button
          @click="showAddModal = true"
          class="flex items-center gap-2 px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
        >
          <span class="material-symbols-outlined">add</span>
          افزودن رویداد جدید
        </button>
      </div>

      <!-- Loading -->
      <div v-if="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
        <p class="mt-4 text-gray-600">در حال بارگذاری...</p>
      </div>

      <!-- Error -->
      <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4 text-red-600">
        {{ error }}
      </div>

      <!-- Events List -->
      <div v-else class="bg-white rounded-lg shadow overflow-hidden">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">تصویر</th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">عنوان</th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">نوع</th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">شماره بازآموزی</th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">تاریخ</th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">وضعیت</th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">عملیات</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="event in eventsList" :key="event.id">
              <td class="px-6 py-4">
                <img 
                  :src="event.image || '/img/events.png'" 
                  alt="تصویر رویداد" 
                  class="w-16 h-16 object-cover rounded"
                />
              </td>
              <td class="px-6 py-4">
                <div class="text-sm font-medium text-gray-900">{{ event.title }}</div>
                <div class="text-sm text-gray-500">{{ event.slug }}</div>
              </td>
              <td class="px-6 py-4 text-sm text-gray-900">{{ event.event_type }}</td>
              <td class="px-6 py-4">
                <span v-if="event.retraining_number" class="text-sm font-medium text-blue-600">
                  {{ event.retraining_number }}
                </span>
                <span v-else class="text-sm text-gray-400">-</span>
              </td>
              <td class="px-6 py-4 text-sm text-gray-500">
                {{ event.event_year }}/{{ event.event_month }}
              </td>
              <td class="px-6 py-4">
                <span 
                  :class="event.is_published ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'"
                  class="px-2 py-1 text-xs font-medium rounded-full"
                >
                  {{ event.is_published ? 'منتشر شده' : 'پیش‌نویس' }}
                </span>
              </td>
              <td class="px-6 py-4 text-sm font-medium">
                <button
                  @click="editEvent(event)"
                  class="text-blue-600 hover:text-blue-900 ml-4"
                >
                  ویرایش
                </button>
                <button
                  @click="deleteEvent(event.id)"
                  class="text-red-600 hover:text-red-900"
                >
                  حذف
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Add/Edit Modal -->
      <div
        v-if="showAddModal || showEditModal"
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4"
        @click.self="closeModal"
      >
        <div class="bg-white rounded-2xl shadow-xl max-w-4xl w-full max-h-[90vh] overflow-y-auto">
          <div class="flex items-center justify-between p-6 border-b">
            <h3 class="text-xl font-bold">
              {{ showEditModal ? 'ویرایش رویداد' : 'افزودن رویداد جدید' }}
            </h3>
            <button @click="closeModal" class="text-gray-400 hover:text-gray-600">
              <span class="material-symbols-outlined">close</span>
            </button>
          </div>

          <form @submit.prevent="saveEvent" class="p-6 space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">عنوان رویداد *</label>
                <input
                  v-model="formData.title"
                  type="text"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="عنوان رویداد را وارد کنید"
                />
              </div>

              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">اسلاگ (URL) *</label>
                <input
                  v-model="formData.slug"
                  type="text"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="event-slug"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">نوع رویداد *</label>
                <select
                  v-model="formData.event_type"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                >
                  <option value="congress">کنگره</option>
                  <option value="conference">کنفرانس</option>
                  <option value="workshop">کارگاه</option>
                  <option value="webinar">وبینار</option>
                  <option value="seminar">سمینار</option>
                  <option value="other">سایر</option>
                </select>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">شماره بازآموزی</label>
                <input
                  v-model="formData.retraining_number"
                  type="text"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="مثال: 1403-RT-001"
                />
                <p class="text-xs text-gray-500 mt-1">این شماره به جای دکمه ثبت‌نام نمایش داده می‌شود</p>
              </div>

              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">توضیحات رویداد *</label>
                <textarea
                  v-model="formData.description"
                  rows="8"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="توضیحات کامل رویداد را وارد کنید"
                ></textarea>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">مکان *</label>
                <input
                  v-model="formData.location"
                  type="text"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="تهران، مرکز همایش‌ها"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">سال رویداد *</label>
                <input
                  v-model.number="formData.event_year"
                  type="number"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="1403"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">ماه رویداد *</label>
                <select
                  v-model.number="formData.event_month"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                >
                  <option :value="1">فروردین</option>
                  <option :value="2">اردیبهشت</option>
                  <option :value="3">خرداد</option>
                  <option :value="4">تیر</option>
                  <option :value="5">مرداد</option>
                  <option :value="6">شهریور</option>
                  <option :value="7">مهر</option>
                  <option :value="8">آبان</option>
                  <option :value="9">آذر</option>
                  <option :value="10">دی</option>
                  <option :value="11">بهمن</option>
                  <option :value="12">اسفند</option>
                </select>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">مهلت ثبت‌نام</label>
                <input
                  v-model="formData.registration_deadline"
                  type="date"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">قیمت (تومان)</label>
                <input
                  v-model.number="formData.price"
                  type="number"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="2500000"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">حداکثر شرکت‌کننده</label>
                <input
                  v-model.number="formData.max_participants"
                  type="number"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="200"
                />
              </div>

              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">برگزارکننده</label>
                <input
                  v-model="formData.organizer"
                  type="text"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="انجمن علمی ریه کودکان"
                />
              </div>

              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">سخنرانان</label>
                <textarea
                  v-model="formData.speakers"
                  rows="3"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="نام سخنرانان و مشخصات آنها"
                ></textarea>
              </div>

              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">تصویر رویداد</label>
                <input
                  ref="imageInput"
                  type="file"
                  accept="image/*"
                  @change="handleImageSelect"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg"
                />
              </div>

              <div class="md:col-span-2 flex gap-4">
                <label class="flex items-center gap-2">
                  <input
                    v-model="formData.is_published"
                    type="checkbox"
                    class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                  />
                  <span class="text-sm font-medium text-gray-700">انتشار رویداد</span>
                </label>
                <label class="flex items-center gap-2">
                  <input
                    v-model="formData.is_featured"
                    type="checkbox"
                    class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                  />
                  <span class="text-sm font-medium text-gray-700">رویداد ویژه</span>
                </label>
              </div>
            </div>

            <div class="flex gap-3 justify-end">
              <button
                type="button"
                @click="closeModal"
                class="px-6 py-3 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition"
              >
                انصراف
              </button>
              <button
                type="submit"
                :disabled="saving"
                class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition disabled:opacity-50"
              >
                {{ saving ? 'در حال ذخیره...' : 'ذخیره رویداد' }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { getApiUrl } from '@/utils/api';

type EventItem = {
  id: number;
  title: string;
  slug: string;
  description: string;
  event_type: string;
  retraining_number: string | null;
  image: string | null;
  location: string;
  event_month: number;
  event_year: number;
  registration_deadline: string | null;
  max_participants: number | null;
  price: number;
  organizer: string;
  speakers: string;
  is_published: boolean;
  is_featured: boolean;
  created_at: string;
};

const eventsList = ref<EventItem[]>([]);
const loading = ref(true);
const error = ref<string | null>(null);
const showAddModal = ref(false);
const showEditModal = ref(false);
const saving = ref(false);
const editingId = ref<number | null>(null);
const imageInput = ref<HTMLInputElement | null>(null);
const selectedImage = ref<File | null>(null);

const formData = ref({
  title: '',
  slug: '',
  description: '',
  event_type: 'congress',
  retraining_number: '',
  location: '',
  event_year: 1403,
  event_month: 1,
  registration_deadline: '',
  price: 0,
  max_participants: null as number | null,
  organizer: '',
  speakers: '',
  is_published: true,
  is_featured: false
});

const fetchEvents = async () => {
  loading.value = true;
  error.value = null;

  try {
    const response = await fetch(getApiUrl('/api/events/?per_page=100'), {
      credentials: 'include',
    });

    if (!response.ok) throw new Error('خطا در دریافت رویدادها');

    const data = await response.json();
    if (data.success) {
      eventsList.value = data.events;
    }
  } catch (err: any) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
};

const handleImageSelect = (event: Event) => {
  const target = event.target as HTMLInputElement;
  selectedImage.value = target.files?.[0] || null;
};

const saveEvent = async () => {
  saving.value = true;

  try {
    const formDataToSend = new FormData();
    formDataToSend.append('title', formData.value.title);
    formDataToSend.append('slug', formData.value.slug);
    formDataToSend.append('description', formData.value.description);
    formDataToSend.append('event_type', formData.value.event_type);
    formDataToSend.append('retraining_number', formData.value.retraining_number || '');
    formDataToSend.append('location', formData.value.location);
    formDataToSend.append('event_year', formData.value.event_year.toString());
    formDataToSend.append('event_month', formData.value.event_month.toString());
    formDataToSend.append('registration_deadline', formData.value.registration_deadline || '');
    formDataToSend.append('price', formData.value.price.toString());
    formDataToSend.append('max_participants', formData.value.max_participants?.toString() || '');
    formDataToSend.append('organizer', formData.value.organizer);
    formDataToSend.append('speakers', formData.value.speakers);
    formDataToSend.append('is_published', formData.value.is_published.toString());
    formDataToSend.append('is_featured', formData.value.is_featured.toString());

    if (selectedImage.value) {
      formDataToSend.append('cover_image', selectedImage.value);
    }

    const url = showEditModal.value 
      ? getApiUrl(`/api/events/${editingId.value}/update/`)
      : getApiUrl('/api/events/create/');
    
    const method = 'POST';

    const response = await fetch(url, {
      method,
      credentials: 'include',
      body: formDataToSend
    });

    const data = await response.json();

    if (data.success) {
      alert(data.message);
      closeModal();
      fetchEvents();
    } else {
      alert(data.errors || 'خطا در ذخیره رویداد');
    }
  } catch (err: any) {
    alert('خطا در ارتباط با سرور');
  } finally {
    saving.value = false;
  }
};

const editEvent = (event: EventItem) => {
  editingId.value = event.id;
  formData.value = {
    title: event.title,
    slug: event.slug,
    description: event.description,
    event_type: event.event_type,
    retraining_number: event.retraining_number || '',
    location: event.location,
    event_year: event.event_year,
    event_month: event.event_month,
    registration_deadline: event.registration_deadline || '',
    price: event.price,
    max_participants: event.max_participants,
    organizer: event.organizer || '',
    speakers: event.speakers || '',
    is_published: event.is_published,
    is_featured: event.is_featured
  };
  showEditModal.value = true;
};

const deleteEvent = async (id: number) => {
  if (!confirm('آیا از حذف این رویداد اطمینان دارید؟')) return;

  try {
    const response = await fetch(getApiUrl(`/api/events/${id}/delete/`), {
      method: 'DELETE',
      credentials: 'include'
    });

    const data = await response.json();

    if (data.success) {
      alert(data.message);
      fetchEvents();
    } else {
      alert(data.errors || 'خطا در حذف رویداد');
    }
  } catch (err) {
    alert('خطا در ارتباط با سرور');
  }
};

const closeModal = () => {
  showAddModal.value = false;
  showEditModal.value = false;
  editingId.value = null;
  selectedImage.value = null;
  formData.value = {
    title: '',
    slug: '',
    description: '',
    event_type: 'congress',
    retraining_number: '',
    location: '',
    event_year: 1403,
    event_month: 1,
    registration_deadline: '',
    price: 0,
    max_participants: null,
    organizer: '',
    speakers: '',
    is_published: true,
    is_featured: false
  };
  if (imageInput.value) imageInput.value.value = '';
};

onMounted(() => {
  fetchEvents();
});
</script>
