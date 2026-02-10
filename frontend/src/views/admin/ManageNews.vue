<template>
  <div class="min-h-screen bg-gray-50 py-8 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <div class="flex justify-between items-center mb-8">
        <div>
          <h1 class="text-3xl font-bold text-gray-900">مدیریت اخبار</h1>
          <p class="text-gray-600 mt-2">افزودن، ویرایش و حذف اخبار</p>
        </div>
        <button
          @click="showAddModal = true"
          class="flex items-center gap-2 px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
        >
          <span class="material-symbols-outlined">add</span>
          افزودن خبر جدید
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

      <!-- News List -->
      <div v-else class="bg-white rounded-lg shadow overflow-hidden">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">تصویر</th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">عنوان</th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">نویسنده</th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">تاریخ</th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">وضعیت</th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">عملیات</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="news in newsList" :key="news.id">
              <td class="px-6 py-4">
                <img 
                  :src="news.image || '/img/news.png'" 
                  alt="تصویر خبر" 
                  class="w-16 h-16 object-cover rounded"
                />
              </td>
              <td class="px-6 py-4">
                <div class="text-sm font-medium text-gray-900">{{ news.title }}</div>
                <div class="text-sm text-gray-500">{{ news.slug }}</div>
              </td>
              <td class="px-6 py-4 text-sm text-gray-900">{{ news.author }}</td>
              <td class="px-6 py-4 text-sm text-gray-500">{{ formatDate(news.created_at) }}</td>
              <td class="px-6 py-4">
                <span 
                  :class="news.is_published ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'"
                  class="px-2 py-1 text-xs font-medium rounded-full"
                >
                  {{ news.is_published ? 'منتشر شده' : 'پیش‌نویس' }}
                </span>
              </td>
              <td class="px-6 py-4 text-sm font-medium">
                <button
                  @click="editNews(news)"
                  class="text-blue-600 hover:text-blue-900 ml-4"
                >
                  ویرایش
                </button>
                <button
                  @click="deleteNews(news.id)"
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
              {{ showEditModal ? 'ویرایش خبر' : 'افزودن خبر جدید' }}
            </h3>
            <button @click="closeModal" class="text-gray-400 hover:text-gray-600">
              <span class="material-symbols-outlined">close</span>
            </button>
          </div>

          <form @submit.prevent="saveNews" class="p-6 space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">عنوان خبر *</label>
                <input
                  v-model="formData.title"
                  type="text"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="عنوان خبر را وارد کنید"
                />
              </div>

              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">اسلاگ (URL) *</label>
                <input
                  v-model="formData.slug"
                  type="text"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="news-slug"
                />
              </div>

              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">محتوای خبر *</label>
                <textarea
                  v-model="formData.content"
                  rows="10"
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="محتوای کامل خبر را وارد کنید"
                ></textarea>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">دسته‌بندی</label>
                <input
                  v-model="formData.category"
                  type="text"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="مثال: مقاله علمی"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">برچسب‌ها</label>
                <input
                  v-model="formData.tags"
                  type="text"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  placeholder="آسم، کودکان، درمان"
                />
              </div>

              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-2">تصویر خبر</label>
                <input
                  ref="imageInput"
                  type="file"
                  accept="image/*"
                  @change="handleImageSelect"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg"
                />
              </div>

              <div class="md:col-span-2">
                <label class="flex items-center gap-2">
                  <input
                    v-model="formData.is_published"
                    type="checkbox"
                    class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                  />
                  <span class="text-sm font-medium text-gray-700">انتشار خبر</span>
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
                {{ saving ? 'در حال ذخیره...' : 'ذخیره خبر' }}
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

type NewsItem = {
  id: number;
  title: string;
  slug: string;
  content: string;
  category: string;
  tags: string;
  image: string | null;
  author: string;
  is_published: boolean;
  created_at: string;
};

const newsList = ref<NewsItem[]>([]);
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
  content: '',
  category: '',
  tags: '',
  is_published: true
});

const formatDate = (isoDate: string) => {
  try {
    return new Date(isoDate).toLocaleDateString('fa-IR');
  } catch (error) {
    return isoDate;
  }
};

const fetchNews = async () => {
  loading.value = true;
  error.value = null;

  try {
    const response = await fetch(getApiUrl('/api/news/?per_page=100'), {
      credentials: 'include',
    });

    if (!response.ok) throw new Error('خطا در دریافت اخبار');

    const data = await response.json();
    if (data.success) {
      newsList.value = data.news;
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

const saveNews = async () => {
  saving.value = true;

  try {
    const formDataToSend = new FormData();
    formDataToSend.append('title', formData.value.title);
    formDataToSend.append('slug', formData.value.slug);
    formDataToSend.append('content', formData.value.content);
    formDataToSend.append('category', formData.value.category);
    formDataToSend.append('tags', formData.value.tags);
    formDataToSend.append('is_published', formData.value.is_published.toString());

    if (selectedImage.value) {
      formDataToSend.append('image', selectedImage.value);
    }

    const url = showEditModal.value 
      ? getApiUrl(`/api/news/${editingId.value}/update/`)
      : getApiUrl('/api/news/create/');
    
    const method = showEditModal.value ? 'PUT' : 'POST';

    const response = await fetch(url, {
      method,
      credentials: 'include',
      body: formDataToSend
    });

    const data = await response.json();

    if (data.success) {
      alert(data.message);
      closeModal();
      fetchNews();
    } else {
      alert(data.errors || 'خطا در ذخیره خبر');
    }
  } catch (err: any) {
    alert('خطا در ارتباط با سرور');
  } finally {
    saving.value = false;
  }
};

const editNews = (news: NewsItem) => {
  editingId.value = news.id;
  formData.value = {
    title: news.title,
    slug: news.slug,
    content: news.content,
    category: news.category || '',
    tags: news.tags || '',
    is_published: news.is_published
  };
  showEditModal.value = true;
};

const deleteNews = async (id: number) => {
  if (!confirm('آیا از حذف این خبر اطمینان دارید؟')) return;

  try {
    const response = await fetch(getApiUrl(`/api/news/${id}/delete/`), {
      method: 'DELETE',
      credentials: 'include'
    });

    const data = await response.json();

    if (data.success) {
      alert(data.message);
      fetchNews();
    } else {
      alert(data.errors || 'خطا در حذف خبر');
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
    content: '',
    category: '',
    tags: '',
    is_published: true
  };
  if (imageInput.value) imageInput.value.value = '';
};

onMounted(() => {
  fetchNews();
});
</script>
