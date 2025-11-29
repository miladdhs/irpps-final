<template>
  <div class="dashboard-wrapper">
    <div class="dashboard-bg"></div>
    <div class="dashboard-decoration">
      <span class="dashboard-shape shape-1"></span>
      <span class="dashboard-shape shape-2"></span>
      <span class="dashboard-shape shape-3"></span>
    </div>

    <section class="dashboard-content py-5">
      <div class="container-xl position-relative">
        <div v-if="loading" class="dashboard-loading text-center py-5">
          <i class="fa fa-spinner fa-spin fa-3x col_blue"></i>
          <p class="mt-3">در حال بارگذاری...</p>
        </div>

        <div v-else-if="user">
          <div class="glass-card hero-card p-4 p-lg-5 mb-4">
            <div class="row g-4 align-items-center">
              <div class="col-lg-12 col-xl-10">
                <div class="d-flex align-items-center gap-3">
                  <div class="hero-avatar">
                    <span>{{ userInitials }}</span>
                  </div>
                  <div>
                    <span class="hero-badge">داشبورد شخصی</span>
                    <h1 class="hero-title mb-2">سلام {{ user.first_name || user.username }} 👋</h1>
                    <p class="hero-subtitle mb-3">{{ greetingText }}</p>
                    <div class="hero-tags d-flex flex-wrap gap-2">
                      <span class="hero-tag" v-if="profileCompletion.missing.length === 0">
                        <i class="fa fa-check me-1"></i>پروفایل کامل
                      </span>
                      <span 
                        class="hero-tag warning" 
                        v-else 
                        v-for="missing in profileCompletion.missing" 
                        :key="'hero-missing-' + missing"
                      >
                        <i class="fa fa-exclamation-circle me-1"></i>{{ missing }} ثبت نشده
                      </span>
                    </div>
                    <div class="hero-quote mt-3">
                      <i class="fa fa-magic"></i>
                      <span>{{ dailyAffirmation }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="row g-3 mb-4">
            <div class="col-md-4" v-for="stat in quickStats" :key="stat.id">
              <div class="stat-card glass-card" :class="'stat-card--' + stat.tone">
                <div class="stat-icon">
                  <i :class="'fa ' + stat.icon"></i>
                </div>
                <div class="stat-meta">
                  <h6 class="stat-title">{{ stat.title }}</h6>
                  <div class="stat-value">{{ stat.value }}</div>
                  <p class="stat-desc mb-0">{{ stat.description }}</p>
                </div>
              </div>
            </div>
          </div>

          <div v-if="isStaff" class="glass-card admin-stats-wrapper p-4 mb-4">
            <div class="d-flex flex-column flex-lg-row align-items-lg-center justify-content-between gap-3 mb-3">
              <div class="d-flex align-items-center gap-3">
                <div class="admin-stats-icon">
                  <i class="fa fa-chart-line"></i>
                </div>
                <div>
                  <h5 class="mb-1">آمار مدیریتی سامانه</h5>
                  <p class="mb-0 text-muted">وضعیت کلی کاربران، اخبار و رویدادها در یک نگاه</p>
                </div>
              </div>
            </div>
            <div v-if="adminStatsLoading" class="text-center py-4">
              <i class="fa fa-spinner fa-spin fa-2x col_blue"></i>
              <p class="mt-3 mb-0 text-muted">در حال دریافت آمار...</p>
            </div>
            <div v-else-if="adminStatsError" class="alert alert-warning border-0 rounded-4 mb-0">
              <i class="fa fa-exclamation-triangle me-2"></i>{{ adminStatsError }}
            </div>
            <div v-else class="row g-3 mb-0">
              <div class="col-xl-3 col-md-4 col-sm-6" v-for="stat in adminStatCards" :key="stat.key">
                <div class="admin-stat-card" :class="'admin-stat-card--' + stat.tone">
                  <div class="admin-stat-icon-circle">
                    <i :class="'fa ' + stat.icon"></i>
                  </div>
                  <div class="admin-stat-content">
                    <span class="admin-stat-label">{{ stat.title }}</span>
                    <span class="admin-stat-value">{{ stat.value }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div v-if="isStaff" class="glass-card admin-management-wrapper p-4 mb-4">
            <div class="d-flex flex-column flex-lg-row align-items-lg-center justify-content-between gap-3 mb-4">
              <div class="d-flex align-items-center gap-3">
                <div class="admin-management-icon">
                  <i class="fa fa-tools"></i>
                </div>
                <div>
                  <h5 class="mb-1">مدیریت محتوا</h5>
                  <p class="mb-0 text-muted">از اینجا می‌توانید خبر، اطلاعیه و رویداد جدید ثبت کنید.</p>
                </div>
              </div>
            </div>
            <div class="admin-management-tabs d-flex flex-wrap gap-2 mb-4">
              <button
                class="btn btn-soft-light"
                :class="{ active: adminActiveTab === 'news' }"
                @click="adminActiveTab = 'news'"
              >
                <i class="fa fa-newspaper me-2"></i>خبر جدید
              </button>
              <button
                class="btn btn-soft-light"
                :class="{ active: adminActiveTab === 'announcement' }"
                @click="adminActiveTab = 'announcement'"
              >
                <i class="fa fa-bullhorn me-2"></i>اطلاعیه جدید
              </button>
              <button
                class="btn btn-soft-light"
                :class="{ active: adminActiveTab === 'event' }"
                @click="adminActiveTab = 'event'"
              >
                <i class="fa fa-calendar-plus me-2"></i>رویداد جدید
              </button>
            </div>

            <transition name="fade-slide" mode="out-in">
              <div v-if="adminActiveTab === 'news'" key="news" class="admin-form-card">
                <h6 class="admin-form-title">
                  <i class="fa fa-newspaper me-2 col_blue"></i>ثبت خبر جدید
                </h6>
                <div
                  v-if="newsSubmitMessage"
                  :class="'alert alert-' + (newsSubmitSuccess ? 'success' : 'danger') + ' alert-dismissible fade show'"
                  role="alert"
                >
                  {{ newsSubmitMessage }}
                  <button type="button" class="btn-close" @click="newsSubmitMessage = ''"></button>
                </div>
                <form class="modern-form" @submit.prevent="submitNewsForm" enctype="multipart/form-data">
                  <div class="row">
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="newsTitle"><i class="fa fa-heading me-2 col_blue"></i>عنوان</label>
                      <input v-model="newsForm.title" type="text" id="newsTitle" class="form-control modern-input" required placeholder="عنوان خبر را وارد کنید">
                    </div>
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="newsSlug"><i class="fa fa-link me-2 col_blue"></i>اسلاگ (پیوند)</label>
                      <input v-model="newsForm.slug" type="text" id="newsSlug" class="form-control modern-input" required placeholder="مثلاً: new-research-2025">
                    </div>
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="newsCategory"><i class="fa fa-tags me-2 col_blue"></i>دسته‌بندی</label>
                      <input v-model="newsForm.category" type="text" id="newsCategory" class="form-control modern-input" placeholder="مثلاً: علمی، پزشکی، عمومی">
                    </div>
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="newsSource"><i class="fa fa-link me-2 col_blue"></i>منبع</label>
                      <input v-model="newsForm.source" type="text" id="newsSource" class="form-control modern-input" placeholder="منبع خبر (اختیاری)">
                    </div>
                    <div class="col-12 mb-3">
                      <label class="form-label" for="newsShortContent"><i class="fa fa-align-right me-2 col_blue"></i>خلاصه خبر</label>
                      <textarea v-model="newsForm.short_content" id="newsShortContent" class="form-control modern-input" rows="2" placeholder="خلاصه کوتاه خبر (حداکثر 500 کاراکتر)"></textarea>
                    </div>
                    <div class="col-12 mb-3">
                      <label class="form-label" for="newsContent"><i class="fa fa-align-right me-2 col_blue"></i>متن کامل خبر</label>
                      <textarea v-model="newsForm.content" id="newsContent" class="form-control modern-input" rows="5" required placeholder="متن کامل خبر را بنویسید"></textarea>
                    </div>
                    <div class="col-12 mb-3">
                      <label class="form-label" for="newsImage"><i class="fa fa-image me-2 col_blue"></i>تصویر خبر</label>
                      <input type="file" id="newsImage" class="form-control modern-input" accept="image/*" @change="handleNewsImageChange">
                      <small class="text-muted">فرمت‌های مجاز: JPG, PNG, GIF</small>
                      <div v-if="newsImagePreview" class="mt-2">
                        <img :src="newsImagePreview" alt="پیش‌نمایش" style="max-width: 200px; max-height: 200px; border-radius: 10px;">
                      </div>
                    </div>
                    <div class="col-12 mb-3">
                      <label class="form-label" for="newsTags"><i class="fa fa-hashtag me-2 col_blue"></i>برچسب‌ها</label>
                      <input v-model="newsForm.tags" type="text" id="newsTags" class="form-control modern-input" placeholder="برچسب‌ها را با کاما جدا کنید (مثلاً: پزشکی، تحقیق، اخبار)">
                    </div>
                  </div>
                  <div class="d-flex flex-wrap gap-2">
                    <button type="submit" class="btn btn-primary modern-btn" :disabled="newsSubmitLoading">
                      <i v-if="newsSubmitLoading" class="fa fa-spinner fa-spin me-2"></i>
                      <i v-else class="fa fa-save me-2"></i>
                      {{ newsSubmitLoading ? 'در حال ثبت...' : 'ثبت خبر' }}
                    </button>
                    <button type="button" class="btn btn-outline-secondary modern-btn" @click="resetNewsForm" :disabled="newsSubmitLoading">
                      <i class="fa fa-undo me-2"></i>پاک‌کردن فرم
                    </button>
                  </div>
                </form>
              </div>

              <div v-else-if="adminActiveTab === 'announcement'" key="announcement" class="admin-form-card">
                <h6 class="admin-form-title">
                  <i class="fa fa-bullhorn me-2 col_blue"></i>ثبت اطلاعیه جدید
                </h6>
                <div
                  v-if="announcementSubmitMessage"
                  :class="'alert alert-' + (announcementSubmitSuccess ? 'success' : 'danger') + ' alert-dismissible fade show'"
                  role="alert"
                >
                  {{ announcementSubmitMessage }}
                  <button type="button" class="btn-close" @click="announcementSubmitMessage = ''"></button>
                </div>
                <form class="modern-form" @submit.prevent="submitAnnouncementForm">
                  <div class="row">
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="announcementTitle"><i class="fa fa-heading me-2 col_blue"></i>عنوان</label>
                      <input v-model="announcementForm.title" type="text" id="announcementTitle" class="form-control modern-input" required placeholder="عنوان اطلاعیه را وارد کنید">
                    </div>
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="announcementSlug"><i class="fa fa-link me-2 col_blue"></i>اسلاگ</label>
                      <input v-model="announcementForm.slug" type="text" id="announcementSlug" class="form-control modern-input" required placeholder="مثلاً: urgent-meeting">
                    </div>
                    <div class="col-12 mb-3">
                      <label class="form-label" for="announcementContent"><i class="fa fa-align-right me-2 col_blue"></i>متن اطلاعیه</label>
                      <textarea v-model="announcementForm.content" id="announcementContent" class="form-control modern-input" rows="4" required placeholder="متن کامل اطلاعیه را بنویسید"></textarea>
                    </div>
                    <div class="col-md-6 mb-3 form-check form-switch">
                      <input v-model="announcementForm.is_important" class="form-check-input" type="checkbox" id="announcementImportant">
                      <label class="form-check-label" for="announcementImportant">برچسب مهم</label>
                    </div>
                  </div>
                  <div class="d-flex flex-wrap gap-2">
                    <button type="submit" class="btn btn-primary modern-btn" :disabled="announcementSubmitLoading">
                      <i v-if="announcementSubmitLoading" class="fa fa-spinner fa-spin me-2"></i>
                      <i v-else class="fa fa-save me-2"></i>
                      {{ announcementSubmitLoading ? 'در حال ثبت...' : 'ثبت اطلاعیه' }}
                    </button>
                    <button type="button" class="btn btn-outline-secondary modern-btn" @click="resetAnnouncementForm" :disabled="announcementSubmitLoading">
                      <i class="fa fa-undo me-2"></i>پاک‌کردن فرم
                    </button>
                  </div>
                </form>
              </div>

              <div v-else key="event" class="admin-form-card">
                <h6 class="admin-form-title">
                  <i class="fa fa-calendar-plus me-2 col_blue"></i>ثبت رویداد جدید
                </h6>
                <div
                  v-if="eventSubmitMessage"
                  :class="'alert alert-' + (eventSubmitSuccess ? 'success' : 'danger') + ' alert-dismissible fade show'"
                  role="alert"
                >
                  {{ eventSubmitMessage }}
                  <button type="button" class="btn-close" @click="eventSubmitMessage = ''"></button>
                </div>
                <form class="modern-form" @submit.prevent="submitEventForm" enctype="multipart/form-data">
                  <div class="row">
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="eventTitle"><i class="fa fa-heading me-2 col_blue"></i>عنوان</label>
                      <input v-model="eventForm.title" type="text" id="eventTitle" class="form-control modern-input" required placeholder="عنوان رویداد را وارد کنید">
                    </div>
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="eventSlug"><i class="fa fa-link me-2 col_blue"></i>اسلاگ</label>
                      <input v-model="eventForm.slug" type="text" id="eventSlug" class="form-control modern-input" required placeholder="مثلاً: pediatric-workshop">
                    </div>
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="eventType"><i class="fa fa-tasks me-2 col_blue"></i>نوع رویداد</label>
                      <select v-model="eventForm.event_type" id="eventType" class="form-select modern-input" required>
                        <option value="conference">کنفرانس</option>
                        <option value="seminar">سمینار</option>
                        <option value="workshop">کارگاه</option>
                        <option value="congress">کنگره</option>
                        <option value="other">سایر</option>
                      </select>
                    </div>
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="eventLocation"><i class="fa fa-map-marker-alt me-2 col_blue"></i>محل برگزاری</label>
                      <input v-model="eventForm.location" type="text" id="eventLocation" class="form-control modern-input" required placeholder="مثلاً: بیمارستان مرکز طبی">
                    </div>
                    <div class="col-12 mb-3">
                      <label class="form-label" for="eventShortDescription"><i class="fa fa-align-right me-2 col_blue"></i>خلاصه توضیحات</label>
                      <textarea v-model="eventForm.short_description" id="eventShortDescription" class="form-control modern-input" rows="2" placeholder="خلاصه کوتاه رویداد (حداکثر 500 کاراکتر)"></textarea>
                    </div>
                    <div class="col-12 mb-3">
                      <label class="form-label" for="eventDescription"><i class="fa fa-align-right me-2 col_blue"></i>توضیحات کامل رویداد</label>
                      <textarea v-model="eventForm.description" id="eventDescription" class="form-control modern-input" rows="4" required placeholder="توضیحات کامل رویداد را بنویسید"></textarea>
                    </div>
                    <div class="col-12 mb-3">
                      <label class="form-label" for="eventCoverImage"><i class="fa fa-image me-2 col_blue"></i>تصویر کاور رویداد</label>
                      <input type="file" id="eventCoverImage" class="form-control modern-input" accept="image/*" @change="handleEventCoverImageChange">
                      <small class="text-muted">تصویر کاور برای نمایش در لیست رویدادها - فرمت‌های مجاز: JPG, PNG, GIF</small>
                      <div v-if="eventCoverImagePreview" class="mt-2">
                        <img :src="eventCoverImagePreview" alt="پیش‌نمایش" style="max-width: 200px; max-height: 200px; border-radius: 10px;">
                      </div>
                    </div>
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="eventMonth"><i class="fa fa-calendar-alt me-2 col_blue"></i>ماه رویداد</label>
                      <select v-model="eventForm.event_month" id="eventMonth" class="form-select modern-input" required>
                        <option value="">انتخاب کنید</option>
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
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="eventYear"><i class="fa fa-calendar me-2 col_blue"></i>سال رویداد</label>
                      <input v-model="eventForm.event_year" type="number" id="eventYear" class="form-control modern-input" placeholder="1403" required>
                    </div>
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="eventDeadline"><i class="fa fa-hourglass-half me-2 col_blue"></i>مهلت ثبت‌نام</label>
                      <date-picker
                        v-model="eventForm.registration_deadline"
                        format="YYYY-MM-DD"
                        display-format="jYYYY/jMM/jDD"
                        :clearable="true"
                        placeholder="انتخاب تاریخ شمسی"
                        input-class="form-control modern-input"
                        style="width: 100%;"
                      />
                      <small class="text-muted">برای انتخاب تاریخ شمسی کلیک کنید</small>
                    </div>
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="eventCapacity"><i class="fa fa-users me-2 col_blue"></i>ظرفیت (اختیاری)</label>
                      <input v-model="eventForm.max_participants" type="number" min="0" id="eventCapacity" class="form-control modern-input" placeholder="مثلاً 120">
                    </div>
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="eventPrice"><i class="fa fa-credit-card me-2 col_blue"></i>هزینه (به تومان)</label>
                      <input v-model="eventForm.price" type="number" min="0" step="1000" id="eventPrice" class="form-control modern-input" placeholder="در صورت رایگان، صفر را وارد کنید">
                    </div>
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="eventOrganizer"><i class="fa fa-building me-2 col_blue"></i>برگزارکننده</label>
                      <input v-model="eventForm.organizer" type="text" id="eventOrganizer" class="form-control modern-input" placeholder="نام سازمان یا نهاد برگزارکننده">
                    </div>
                    <div class="col-md-6 mb-3">
                      <label class="form-label" for="eventTargetAudience"><i class="fa fa-users me-2 col_blue"></i>مخاطبان</label>
                      <input v-model="eventForm.target_audience" type="text" id="eventTargetAudience" class="form-control modern-input" placeholder="مثلاً: پزشکان، پرستاران، دانشجویان">
                    </div>
                    <div class="col-12 mb-3">
                      <label class="form-label" for="eventPrerequisites"><i class="fa fa-list-check me-2 col_blue"></i>پیش‌نیازها</label>
                      <textarea v-model="eventForm.prerequisites" id="eventPrerequisites" class="form-control modern-input" rows="2" placeholder="پیش‌نیازهای شرکت در رویداد"></textarea>
                    </div>
                    <div class="col-12 mb-3">
                      <label class="form-label" for="eventAgenda"><i class="fa fa-calendar-days me-2 col_blue"></i>برنامه زمانی</label>
                      <textarea v-model="eventForm.agenda" id="eventAgenda" class="form-control modern-input" rows="3" placeholder="برنامه زمانی رویداد را وارد کنید"></textarea>
                    </div>
                    <div class="col-12 mb-3">
                      <label class="form-label" for="eventSpeakers"><i class="fa fa-microphone me-2 col_blue"></i>سخنرانان</label>
                      <textarea v-model="eventForm.speakers" id="eventSpeakers" class="form-control modern-input" rows="2" placeholder="نام و سمت سخنرانان را وارد کنید"></textarea>
                    </div>
                    <div class="col-12 mb-3">
                      <label class="form-label" for="eventContactInfo"><i class="fa fa-phone me-2 col_blue"></i>اطلاعات تماس</label>
                      <input v-model="eventForm.contact_info" type="text" id="eventContactInfo" class="form-control modern-input" placeholder="شماره تماس، ایمیل یا سایر اطلاعات تماس">
                    </div>
                    <div class="col-md-6 mb-3 form-check form-switch">
                      <input v-model="eventForm.is_featured" class="form-check-input" type="checkbox" id="eventFeatured">
                      <label class="form-check-label" for="eventFeatured">رویداد ویژه</label>
                    </div>
                  </div>
                  <div class="d-flex flex-wrap gap-2">
                    <button type="submit" class="btn btn-primary modern-btn" :disabled="eventSubmitLoading">
                      <i v-if="eventSubmitLoading" class="fa fa-spinner fa-spin me-2"></i>
                      <i v-else class="fa fa-save me-2"></i>
                      {{ eventSubmitLoading ? 'در حال ثبت...' : 'ثبت رویداد' }}
                    </button>
                    <button type="button" class="btn btn-outline-secondary modern-btn" @click="resetEventForm" :disabled="eventSubmitLoading">
                      <i class="fa fa-undo me-2"></i>پاک‌کردن فرم
                    </button>
                  </div>
                </form>
              </div>
            </transition>
          </div>

          <div v-if="profileCompletion.missing.length > 0" class="profile-alert glass-card mb-4">
            <div class="d-flex flex-column flex-lg-row align-items-lg-center justify-content-between gap-3">
              <div class="d-flex align-items-center gap-3">
                <div class="alert-icon">
                  <i class="fa fa-exclamation-triangle"></i>
                </div>
                <div>
                  <h5 class="mb-1">پروفایل هنوز کامل نشده</h5>
                  <p class="mb-0 text-muted">برای نمایش بهتر در لیست اعضا، لطفاً موارد زیر را تکمیل کنید.</p>
                </div>
              </div>
              <div class="d-flex flex-wrap gap-2">
                <span class="missing-chip" v-for="missing in profileCompletion.missing" :key="'chip-' + missing">
                  <i class="fa fa-circle me-1"></i>{{ missing }}
                </span>
              </div>
            </div>
          </div>

          <div class="row g-4">
            <div class="col-lg-8">
              <transition name="fade-slide">
                <div v-if="showProfileForm" class="card glass-card border-0 shadow-none mb-4">
                  <div class="card-header glass-card-header border-0">
                    <h4 class="mb-0">
                      <i class="fa fa-user-edit me-2"></i>
                      تکمیل پروفایل
                    </h4>
                  </div>
                  <div class="card-body p-4">
                    <div v-if="updateMessage" :class="'alert alert-' + (updateSuccess ? 'success' : 'danger') + ' alert-dismissible fade show'" role="alert">
                      <i :class="(updateSuccess ? 'fa fa-check-circle' : 'fa fa-exclamation-circle') + ' me-2'"></i>
                      {{ updateMessage }}
                      <button type="button" class="btn-close" @click="updateMessage = ''"></button>
                    </div>
                    <form @submit.prevent="updateProfile" class="modern-form">
                      <div class="row">
                        <div class="col-md-6 mb-3">
                          <label for="first_name" class="form-label"><i class="fa fa-user me-2 col_blue"></i>نام</label>
                          <input type="text" class="form-control modern-input" id="first_name" v-model="profileForm.first_name" placeholder="نام خود را وارد کنید">
                        </div>
                        <div class="col-md-6 mb-3">
                          <label for="last_name" class="form-label"><i class="fa fa-user me-2 col_blue"></i>نام خانوادگی</label>
                          <input type="text" class="form-control modern-input" id="last_name" v-model="profileForm.last_name" placeholder="نام خانوادگی خود را وارد کنید">
                        </div>
                        <div class="col-md-6 mb-3">
                          <label for="email" class="form-label"><i class="fa fa-envelope me-2 col_blue"></i>ایمیل</label>
                          <input type="email" class="form-control modern-input" id="email" v-model="profileForm.email" placeholder="ایمیل خود را وارد کنید">
                        </div>
                        <div class="col-md-6 mb-3">
                          <label for="phone" class="form-label"><i class="fa fa-phone me-2 col_blue"></i>شماره تلفن</label>
                          <input type="text" class="form-control modern-input" id="phone" v-model="profileForm.phone" placeholder="شماره تلفن خود را وارد کنید">
                        </div>
                      </div>
                      <div class="d-flex flex-wrap gap-2">
                        <button type="submit" class="btn btn-primary modern-btn" :disabled="updateLoading">
                          <i v-if="updateLoading" class="fa fa-spinner fa-spin me-2"></i>
                          <i v-else class="fa fa-save me-2"></i>
                          {{ updateLoading ? 'در حال ذخیره...' : 'ذخیره تغییرات' }}
                        </button>
                        <button type="button" class="btn btn-outline-secondary modern-btn" @click="showProfileForm = false">
                          <i class="fa fa-times me-2"></i>انصراف
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
              </transition>

              <div class="card glass-card border-0 shadow-none h-100">
                <div class="card-header glass-card-header border-0">
                  <div class="d-flex justify-content-between align-items-center flex-wrap gap-2">
                    <h4 class="mb-0">
                      <i class="fa fa-info-circle col_blue me-2"></i>
                      اطلاعات حساب کاربری
                    </h4>
                    <button v-if="!showProfileForm" class="btn btn-sm btn-soft-primary" @click="showProfileForm = true">
                      <i class="fa fa-edit me-1"></i>ویرایش
                    </button>
                  </div>
                </div>
                <div class="card-body p-4">
                  <div class="row gy-4">
                    <div class="col-sm-6" v-for="detail in userDetails" :key="detail.label">
                      <div class="detail-item">
                        <span class="detail-icon">
                          <i :class="'fa ' + detail.icon"></i>
                        </span>
                        <div>
                          <span class="detail-label">{{ detail.label }}</span>
                          <p class="detail-value mb-0">{{ detail.value }}</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

            </div>

            <div class="col-lg-4">
              <div class="card glass-card border-0 shadow-none sticky-lg-top" style="top: 90px;">
                <div class="card-body p-4">
                  <div class="user-avatar-container mb-3 position-relative">
                    <div class="user-avatar-glow"></div>
                    <div v-if="!getProfileImageUrl()" class="user-avatar-large">
                      <i class="fa fa-user"></i>
                    </div>
                    <img 
                      v-else
                      :src="getProfileImageUrl()" 
                      alt="عکس پروفایل" 
                      class="user-profile-image"
                      @error="handleImageError"
                      :key="`profile-${user.id}-${user.profile_image || 'default'}`"
                    >
                  </div>
                  <h5 class="fw-bold mb-1 text-center">{{ user.first_name || user.username }} {{ user.last_name || '' }}</h5>
                  <p class="text-muted mb-3 text-center">{{ user.username }}</p>
                  <div class="profile-progress mb-4">
                    <div class="d-flex justify-content-between mb-1">
                      <span class="text-muted">درصد تکمیل پروفایل</span>
                      <span class="fw-semibold">{{ profileCompletion.percent }}%</span>
                    </div>
                    <div class="progress modern-progress">
                      <div class="progress-bar" role="progressbar" :style="{ width: profileCompletion.percent + '%' }"></div>
                    </div>
                  </div>
                  <div class="d-grid gap-2">
                    <button class="btn btn-soft-primary" @click="showImageUploadModal = true">
                      <i class="fa fa-image me-2"></i>{{ user.profile_image ? 'تغییر عکس' : 'افزودن عکس' }}
                    </button>
                    <button 
                      v-if="user.profile_image" 
                      class="btn btn-soft-warning" 
                      @click="deleteProfileImage"
                      :disabled="imageDeleteLoading"
                    >
                      <i v-if="imageDeleteLoading" class="fa fa-spinner fa-spin me-2"></i>
                      <i v-else class="fa fa-trash me-2"></i>
                      {{ imageDeleteLoading ? 'در حال حذف...' : 'حذف عکس' }}
                    </button>
                    <button class="btn btn-soft-info" @click="showResumeModal = true">
                      <i class="fa fa-file-text me-2"></i>رزومه و توضیحات
                    </button>
                    <button class="btn btn-soft-danger" @click="handleLogout">
                      <i class="fa fa-sign-out me-2"></i>خروج از حساب
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div v-else class="text-center py-5">
          <div class="alert alert-danger">
            <i class="fa fa-exclamation-circle me-2"></i>
            خطا در بارگذاری اطلاعات کاربر
          </div>
          <router-link to="/" class="btn btn-primary">
            <i class="fa fa-home me-2"></i>بازگشت به صفحه اصلی
          </router-link>
        </div>
      </div>
    </section>

    <!-- Image Upload Modal -->
    <div v-if="showImageUploadModal" class="modal fade show d-block" tabindex="-1" style="background-color: rgba(0,0,0,0.5);" @click.self="showImageUploadModal = false">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="border-radius: 20px;">
              <div class="modal-header border-0">
                <h5 class="modal-title"><i class="fa fa-image col_blue me-2"></i>تغییر عکس پروفایل</h5>
                <button type="button" class="btn-close" @click="showImageUploadModal = false"></button>
              </div>
              <div class="modal-body">
                <div v-if="imageUploadMessage" :class="'alert alert-' + (imageUploadSuccess ? 'success' : 'danger') + ' alert-dismissible fade show'" role="alert">
                  {{ imageUploadMessage }}
                  <button type="button" class="btn-close" @click="imageUploadMessage = ''"></button>
                </div>
                <form @submit.prevent="uploadProfileImage">
                  <div class="mb-3">
                    <label for="profileImageInput" class="form-label">انتخاب عکس</label>
                    <input type="file" class="form-control" id="profileImageInput" accept="image/*" @change="handleImagePreview" required>
                    <small class="text-muted">فرمت‌های مجاز: JPG, PNG, GIF</small>
                  </div>
                  <div v-if="imagePreviewUrl" class="mb-3 text-center">
                    <img :src="imagePreviewUrl" alt="پیش‌نمایش" style="max-width: 200px; max-height: 200px; border-radius: 10px;">
                  </div>
                  <div class="d-grid gap-2">
                    <button type="submit" class="btn btn-primary" :disabled="imageUploadLoading">
                      <i v-if="imageUploadLoading" class="fa fa-spinner fa-spin me-2"></i>
                      <i v-else class="fa fa-upload me-2"></i>
                      {{ imageUploadLoading ? 'در حال آپلود...' : 'آپلود عکس' }}
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>

    <!-- Resume Modal -->
    <div v-if="showResumeModal" class="modal fade show d-block" tabindex="-1" style="background-color: rgba(0,0,0,0.5);" @click.self="showResumeModal = false">
          <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content" style="border-radius: 20px;">
              <div class="modal-header border-0">
                <h5 class="modal-title"><i class="fa fa-file-text col_blue me-2"></i>توضیحات عمومی و رزومه</h5>
                <button type="button" class="btn-close" @click="showResumeModal = false"></button>
              </div>
              <div class="modal-body" style="max-height: 70vh; overflow-y: auto;">
                <div v-if="resumeMessage" :class="'alert alert-' + (resumeSuccess ? 'success' : 'danger') + ' alert-dismissible fade show'" role="alert">
                  {{ resumeMessage }}
                  <button type="button" class="btn-close" @click="resumeMessage = ''"></button>
                </div>
                <form @submit.prevent="updateResume">
                  <div class="mb-3">
                    <label for="bio" class="form-label"><i class="fa fa-info-circle col_blue me-2"></i>توضیحات عمومی</label>
                    <textarea class="form-control" id="bio" v-model="resumeForm.bio" rows="3" placeholder="توضیحات کوتاه درباره خودتان..."></textarea>
                  </div>
                  <div class="mb-3">
                    <label for="education" class="form-label"><i class="fa fa-graduation-cap col_blue me-2"></i>تحصیلات</label>
                    <textarea class="form-control" id="education" v-model="resumeForm.education" rows="3" placeholder="مدرک تحصیلی، دانشگاه، سال فارغ‌التحصیلی..."></textarea>
                  </div>
                  <div class="mb-3">
                    <label for="publications" class="form-label"><i class="fa fa-book col_blue me-2"></i>مقالات و انتشارات</label>
                    <textarea class="form-control" id="publications" v-model="resumeForm.publications" rows="4" placeholder="مقالات، کتاب‌ها و انتشارات علمی..."></textarea>
                  </div>
                  <div class="mb-3">
                    <label for="awards" class="form-label"><i class="fa fa-trophy col_blue me-2"></i>جوایز و افتخارات</label>
                    <textarea class="form-control" id="awards" v-model="resumeForm.awards" rows="3" placeholder="جوایز، افتخارات و دستاوردها..."></textarea>
                  </div>
                  <div class="mb-3">
                    <label for="certifications" class="form-label"><i class="fa fa-certificate col_blue me-2"></i>گواهینامه‌ها</label>
                    <textarea class="form-control" id="certifications" v-model="resumeForm.certifications" rows="3" placeholder="گواهینامه‌های تخصصی و حرفه‌ای..."></textarea>
                  </div>
                  <div class="mb-3">
                    <label for="research_interests" class="form-label"><i class="fa fa-microscope col_blue me-2"></i>علایق پژوهشی</label>
                    <textarea class="form-control" id="research_interests" v-model="resumeForm.research_interests" rows="3" placeholder="حوزه‌های تحقیقاتی و علایق پژوهشی..."></textarea>
                  </div>
                  <div class="mb-3">
                    <label for="languages" class="form-label"><i class="fa fa-language col_blue me-2"></i>زبان‌ها</label>
                    <input type="text" class="form-control" id="languages" v-model="resumeForm.languages" placeholder="مثال: فارسی، انگلیسی، آلمانی">
                  </div>
                  <div class="d-grid gap-2">
                    <button type="submit" class="btn btn-primary" :disabled="resumeLoading">
                      <i v-if="resumeLoading" class="fa fa-spinner fa-spin me-2"></i>
                      <i v-else class="fa fa-save me-2"></i>
                      {{ resumeLoading ? 'در حال ذخیره...' : 'ذخیره رزومه' }}
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, nextTick } from 'vue';
import { useRouter } from 'vue-router';
import DatePicker from 'vue3-persian-datetime-picker';
import { getApiUrl } from '@/utils/api';

const router = useRouter();
const user = ref<any>(null);
const loading = ref(true);
const showProfileForm = ref(false);
const updateLoading = ref(false);
const updateMessage = ref('');
const updateSuccess = ref(false);
const profileForm = ref({
  first_name: '',
  last_name: '',
  email: '',
  phone: ''
});

// Image upload
const showImageUploadModal = ref(false);
const imageUploadLoading = ref(false);
const imageUploadMessage = ref('');
const imageUploadSuccess = ref(false);
const imagePreviewUrl = ref('');
const selectedImageFile = ref<File | null>(null);

// Image delete
const imageDeleteLoading = ref(false);

// Resume
const showResumeModal = ref(false);
const resumeLoading = ref(false);
const resumeMessage = ref('');
const resumeSuccess = ref(false);
const resumeForm = ref({
  bio: '',
  education: '',
  publications: '',
  awards: '',
  certifications: '',
  research_interests: '',
  languages: ''
});

type AdminTab = 'news' | 'announcement' | 'event';

const adminStats = ref<Record<string, number> | null>(null);
const adminStatsLoading = ref(false);
const adminStatsError = ref<string | null>(null);

const adminActiveTab = ref<AdminTab>('news');

const newsForm = ref({
  title: '',
  slug: '',
  content: '',
  short_content: '',
  category: '',
  tags: '',
  source: '',
  is_published: true,
});
const newsImageFile = ref<File | null>(null);
const newsImagePreview = ref('');
const newsSubmitLoading = ref(false);
const newsSubmitMessage = ref('');
const newsSubmitSuccess = ref(false);

const announcementForm = ref({
  title: '',
  slug: '',
  content: '',
  is_published: true,
  is_important: false,
});
const announcementSubmitLoading = ref(false);
const announcementSubmitMessage = ref('');
const announcementSubmitSuccess = ref(false);

const eventForm = ref({
  title: '',
  slug: '',
  description: '',
  short_description: '',
  event_type: 'other',
  location: '',
  event_month: null,
  event_year: null,
  registration_deadline: '',
  max_participants: '',
  price: '',
  organizer: '',
  target_audience: '',
  prerequisites: '',
  agenda: '',
  speakers: '',
  contact_info: '',
  is_published: true,
  is_featured: false,
});
const eventCoverImageFile = ref<File | null>(null);
const eventCoverImagePreview = ref('');
const eventSubmitLoading = ref(false);
const eventSubmitMessage = ref('');
const eventSubmitSuccess = ref(false);

const dailyAffirmations: string[] = [
  'قدم‌های کوچک امروز، آینده بزرگ فردا را می‌سازند.',
  'نفس عمیق بکشید و با آرامش به مسیرتان ادامه دهید.',
  'مهربانی با خودتان، اولین قدم خدمت به دیگران است.',
  'هر تجربه‌ای در مسیر شما، فرصتی برای رشد است.',
  'امروز هم می‌توانید الهام‌بخش یک خانواده باشید.'
];

const isStaff = computed(() => !!user.value?.is_staff);

const greetingText = computed(() => {
  const hour = new Date().getHours();
  if (hour < 12) return 'صبح بخیر! امروز هم فرصتی تازه برای ساختن آینده‌ای روشن است.';
  if (hour < 18) return 'عصر دل‌انگیزی داشته باشید؛ تلاش شما امیدبخش خانواده‌هاست.';
  return 'شب آرامی داشته باشید؛ امروز به اندازه کافی تاثیرگذار بودید.';
});

const dailyAffirmation = computed(() => {
  if (!dailyAffirmations.length) return '';
  const index = new Date().getDate() % dailyAffirmations.length;
  return dailyAffirmations[index];
});

const userInitials = computed(() => {
  if (!user.value) return 'کاربر';
  const first = (user.value.first_name || '').trim();
  const last = (user.value.last_name || '').trim();
  if (first || last) {
    return `${first ? first.charAt(0) : ''}${last ? last.charAt(0) : ''}`.toUpperCase();
  }
  const username = (user.value.username || 'کاربر').trim();
  return username.slice(0, 2).toUpperCase();
});

const profileCompletion = computed(() => {
  if (!user.value) return { percent: 0, missing: [] as string[] };
  const fields = [
    { key: 'first_name', label: 'نام' },
    { key: 'last_name', label: 'نام خانوادگی' },
    { key: 'email', label: 'ایمیل' },
    { key: 'phone', label: 'شماره تلفن' }
  ] as const;

  const filled = fields.filter(field => !!user.value?.[field.key]);
  const percent = Math.round((filled.length / fields.length) * 100);
  const missing = fields
    .filter(field => !user.value?.[field.key])
    .map(field => field.label);

  return { percent, missing };
});

const resumeCompletion = computed(() => {
  if (!user.value) return 0;
  const fields: Array<keyof typeof resumeForm.value> = [
    'bio',
    'education',
    'publications',
    'awards',
    'certifications',
    'research_interests',
    'languages'
  ];
  const filledCount = fields.filter(field => !!user.value?.[field]).length;
  return Math.round((filledCount / fields.length) * 100);
});

const quickStats = computed(() => {
  if (!user.value) return [];

  const profilePercent = profileCompletion.value.percent;
  const resumePercent = resumeCompletion.value;
  const missingCount = profileCompletion.value.missing.length;

  return [
    {
      id: 'profile',
      title: 'تکمیل پروفایل',
      value: `${profilePercent}%`,
      icon: profilePercent === 100 ? 'fa-user-check' : 'fa-user-clock',
      tone: profilePercent === 100 ? 'success' : 'warning',
      description: profilePercent === 100
        ? 'پروفایل شما کامل است.'
        : `${missingCount} مورد برای تکمیل باقی مانده است.`
    },
    {
      id: 'resume',
      title: 'رزومه تخصصی',
      value: `${resumePercent}%`,
      icon: 'fa-scroll',
      tone: resumePercent >= 60 ? 'info' : 'primary',
      description: resumePercent === 0
        ? 'رزومه خود را از همین جا شروع کنید.'
        : 'رزومه شما قابل مشاهده برای مدیران است.'
    },
    {
      id: 'member',
      title: 'تاریخ عضویت',
      value: formatDate(user.value?.date_joined),
      icon: 'fa-calendar-check',
      tone: 'violet',
      description: 'ممنون که همراه ما هستید.'
    }
  ];
});

const adminStatCards = computed(() => {
  if (!adminStats.value) return [];
  return [
    {
      key: 'total_users',
      title: 'تعداد کاربران',
      value: adminStats.value.total_users ?? 0,
      icon: 'fa-users',
      tone: 'primary'
    },
    {
      key: 'total_news',
      title: 'اخبار ثبت‌شده',
      value: adminStats.value.total_news ?? 0,
      icon: 'fa-newspaper',
      tone: 'info'
    },
    {
      key: 'published_news',
      title: 'اخبار منتشر شده',
      value: adminStats.value.published_news ?? 0,
      icon: 'fa-bullhorn',
      tone: 'success'
    },
    {
      key: 'total_announcements',
      title: 'اعلانات ثبت‌شده',
      value: adminStats.value.total_announcements ?? 0,
      icon: 'fa-bell',
      tone: 'violet'
    },
    {
      key: 'published_announcements',
      title: 'اعلانات منتشر شده',
      value: adminStats.value.published_announcements ?? 0,
      icon: 'fa-broadcast-tower',
      tone: 'warning'
    },
    {
      key: 'total_events',
      title: 'رویدادهای ثبت‌شده',
      value: adminStats.value.total_events ?? 0,
      icon: 'fa-calendar-alt',
      tone: 'info'
    },
    {
      key: 'published_events',
      title: 'رویدادهای فعال',
      value: adminStats.value.published_events ?? 0,
      icon: 'fa-calendar-check',
      tone: 'success'
    },
    {
      key: 'total_registrations',
      title: 'ثبت‌نام در رویدادها',
      value: adminStats.value.total_registrations ?? 0,
      icon: 'fa-users-cog',
      tone: 'primary'
    }
  ];
});

const userDetails = computed(() => {
  if (!user.value) return [];

  const details = [
    { label: 'نام کاربری', value: user.value.username || 'ثبت نشده', icon: 'fa-at' },
    { label: 'ایمیل', value: user.value.email || 'ثبت نشده', icon: 'fa-envelope' },
    { label: 'نام', value: user.value.first_name || 'ثبت نشده', icon: 'fa-id-badge' },
    { label: 'نام خانوادگی', value: user.value.last_name || 'ثبت نشده', icon: 'fa-id-badge' },
    { label: 'شماره تلفن', value: user.value.phone || 'ثبت نشده', icon: 'fa-phone' },
    { label: 'تاریخ عضویت', value: formatDate(user.value.date_joined), icon: 'fa-calendar' }
  ];

  if (user.value.city) {
    details.push({ label: 'شهر', value: user.value.city, icon: 'fa-map-marker-alt' });
  }

  if (user.value.specialty) {
    details.push({ label: 'تخصص', value: user.value.specialty, icon: 'fa-stethoscope' });
  }

  return details;
});

const fetchAdminStats = async () => {
  if (!isStaff.value) {
    adminStats.value = null;
    return;
  }
  adminStatsLoading.value = true;
  adminStatsError.value = null;

  try {
    const response = await fetch(getApiUrl('/api/dashboard/admin/stats/'), {
      credentials: 'include'
    });

    if (!response.ok) {
      if (response.status === 403) {
        adminStatsError.value = 'دسترسی به آمار داشبورد فقط برای مدیران مجاز است.';
        adminStats.value = null;
        return;
      }
      const errorText = await response.text();
      throw new Error(errorText || 'خطا در دریافت آمار داشبورد');
    }

    const data = await response.json();

    if (data.success && data.stats) {
      adminStats.value = data.stats;
    } else {
      adminStatsError.value = data.errors || 'آمار معتبر از سرور دریافت نشد';
      adminStats.value = null;
    }
  } catch (error) {
    console.error('Error fetching admin stats:', error);
    adminStatsError.value = 'خطا در ارتباط با سرور هنگام دریافت آمار داشبورد';
    adminStats.value = null;
  } finally {
    adminStatsLoading.value = false;
  }
};

const fetchUserProfile = async () => {
  try {
    // Add cache busting to API call
    const timestamp = Date.now();
    const response = await fetch(getApiUrl(`/api/accounts/profile/?t=${timestamp}&v=${Math.random()}`), {
      headers: {
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0'
      },
      credentials: 'include'
    });
    
    const data = await response.json();
    
    if (data.success) {
      // FORCE update user data from database
      user.value = { ...data.user };
      
      // Ensure profile_image is properly set from database
      if (data.user.profile_image && data.user.profile_image.trim() !== '') {
        user.value.profile_image = String(data.user.profile_image).trim();
      } else {
        // FORCE clear if no image in database
        user.value.profile_image = '';
      }
      // Initialize form with current user data
      profileForm.value = {
        first_name: user.value.first_name || '',
        last_name: user.value.last_name || '',
        email: user.value.email || '',
        phone: user.value.phone || ''
      };
      // Initialize resume form
      resumeForm.value = {
        bio: user.value.bio || '',
        education: user.value.education || '',
        publications: user.value.publications || '',
        awards: user.value.awards || '',
        certifications: user.value.certifications || '',
        research_interests: user.value.research_interests || '',
        languages: user.value.languages || ''
      };
      if (data.user.is_staff) {
        await fetchAdminStats();
      } else {
        adminStats.value = null;
      }
    } else {
      // Redirect to home if not authenticated
      router.push('/');
    }
  } catch (error) {
    console.error('Error fetching user profile:', error);
    router.push('/');
  } finally {
    loading.value = false;
  }
};

const updateProfile = async () => {
  updateLoading.value = true;
  updateMessage.value = '';
  
  try {
    const response = await fetch(getApiUrl('/api/accounts/profile/update/'), {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      credentials: 'include',
      body: JSON.stringify(profileForm.value)
    });
    
    const data = await response.json();
    
    if (data.success) {
      updateSuccess.value = true;
      updateMessage.value = data.message || 'پروفایل با موفقیت به‌روزرسانی شد';
      user.value = data.user;
      showProfileForm.value = false;
      
      // Refresh profile after a short delay
      setTimeout(() => {
        fetchUserProfile();
      }, 1000);
    } else {
      updateSuccess.value = false;
      updateMessage.value = data.errors || 'خطا در به‌روزرسانی پروفایل';
    }
  } catch (error) {
    updateSuccess.value = false;
    updateMessage.value = 'خطا در ارتباط با سرور';
    console.error('Error updating profile:', error);
  } finally {
    updateLoading.value = false;
  }
};

const handleLogout = async () => {
  try {
    const response = await fetch(getApiUrl('/api/accounts/logout/'), {
      method: 'POST',
      credentials: 'include'
    });
    
    const data = await response.json();
    
    if (data.success) {
      // Reload the page to update the navbar
      window.location.href = '/';
    }
  } catch (error) {
    console.error('Error logging out:', error);
  }
};

const formatDate = (dateString: string) => {
  if (!dateString) return 'ثبت نشده';
  try {
    return new Date(dateString).toLocaleDateString('fa-IR');
  } catch {
    return dateString;
  }
};

// Get profile image URL - return null if no profile_image
const getProfileImageUrl = (): string | null => {
  if (!user.value) return null;
  
  // Check if user has a valid profile_image from database
  if (user.value.profile_image && 
      user.value.profile_image.trim() !== '' && 
      user.value.profile_image !== 'null' && 
      user.value.profile_image !== 'undefined') {
    
    const imageUrl = user.value.profile_image.trim();
    let finalUrl = '';
    
    // If URL is already absolute, use it directly
    if (imageUrl.startsWith('http://') || imageUrl.startsWith('https://')) {
      finalUrl = imageUrl;
    }
    // If URL starts with /, it's a relative path
    else if (imageUrl.startsWith('/')) {
      finalUrl = imageUrl;
    }
    // Otherwise, prepend / to make it relative from root
    else {
      finalUrl = `/${imageUrl}`;
    }
    
    // Add strong cache busting to force refresh
    const userId = user.value.id || '';
    const timestamp = Date.now();
    const separator = finalUrl.includes('?') ? '&' : '?';
    return `${finalUrl}${separator}id=${userId}&t=${timestamp}&v=${Math.random()}`;
  }
  
  // Return null if no valid profile_image from database
  return null;
};

const handleImageError = (event: Event) => {
  const img = event.target as HTMLImageElement;
  // Hide the broken image and show placeholder if available
  img.style.display = 'none';
  
  // Try to find or create a placeholder
  const parent = img.parentElement;
  if (parent) {
    // Check if placeholder already exists
    let placeholder = parent.querySelector('.no-image-placeholder') as HTMLElement;
    if (!placeholder) {
      // Create placeholder
      placeholder = document.createElement('div');
      placeholder.className = 'no-image-placeholder d-flex align-items-center justify-content-center';
      placeholder.style.cssText = 'width: 100%; height: 100%; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 12px; border: 2px dashed #dee2e6;';
      placeholder.innerHTML = '<i class="fa fa-user fa-2x text-muted"></i>';
      parent.appendChild(placeholder);
    }
    placeholder.style.display = 'flex';
  }
};

const handleImagePreview = (event: Event) => {
  const input = event.target as HTMLInputElement;
  if (input.files && input.files[0]) {
    selectedImageFile.value = input.files[0];
    const reader = new FileReader();
    reader.onload = (e) => {
      imagePreviewUrl.value = e.target?.result as string;
    };
    reader.readAsDataURL(input.files[0]);
  }
};

const handleNewsImageChange = (event: Event) => {
  const input = event.target as HTMLInputElement;
  if (input.files && input.files[0]) {
    newsImageFile.value = input.files[0];
    const reader = new FileReader();
    reader.onload = (e) => {
      newsImagePreview.value = e.target?.result as string;
    };
    reader.readAsDataURL(input.files[0]);
  }
};

const resetNewsForm = (keepMessage = false) => {
  newsForm.value = {
    title: '',
    slug: '',
    content: '',
    short_content: '',
    category: '',
    tags: '',
    source: '',
    is_published: true,
  };
  newsImageFile.value = null;
  newsImagePreview.value = '';
  if (!keepMessage) {
    newsSubmitMessage.value = '';
    newsSubmitSuccess.value = false;
  }
};

const submitNewsForm = async () => {
  if (!newsForm.value.title.trim() || !newsForm.value.slug.trim() || !newsForm.value.content.trim()) {
    newsSubmitSuccess.value = false;
    newsSubmitMessage.value = 'لطفاً همه فیلدهای ضروری خبر را تکمیل کنید.';
    return;
  }

  newsSubmitLoading.value = true;
  newsSubmitMessage.value = '';

  const formData = new FormData();
  formData.append('title', newsForm.value.title.trim());
  formData.append('slug', newsForm.value.slug.trim());
  formData.append('content', newsForm.value.content.trim());
  if (newsForm.value.short_content) {
    formData.append('short_content', newsForm.value.short_content.trim());
  }
  if (newsForm.value.category) {
    formData.append('category', newsForm.value.category.trim());
  }
  if (newsForm.value.tags) {
    formData.append('tags', newsForm.value.tags.trim());
  }
  if (newsForm.value.source) {
    formData.append('source', newsForm.value.source.trim());
  }
  formData.append('is_published', String(newsForm.value.is_published));
  
  if (newsImageFile.value) {
    formData.append('image', newsImageFile.value);
  }

  try {
    const response = await fetch(getApiUrl('/api/news/create/'), {
      method: 'POST',
      credentials: 'include',
      body: formData,
    });

    const data = await response.json();

    if (response.ok && data.success) {
      newsSubmitSuccess.value = true;
      newsSubmitMessage.value = data.message || 'خبر با موفقیت ثبت شد.';
      resetNewsForm(true);
      if (isStaff.value) {
        fetchAdminStats();
      }
    } else {
      newsSubmitSuccess.value = false;
      newsSubmitMessage.value = data.errors || 'خطا در ثبت خبر.';
    }
  } catch (error) {
    console.error('Error creating news:', error);
    newsSubmitSuccess.value = false;
    newsSubmitMessage.value = 'خطا در ارتباط با سرور هنگام ثبت خبر.';
  } finally {
    newsSubmitLoading.value = false;
  }
};

const resetAnnouncementForm = (keepMessage = false) => {
  announcementForm.value = {
    title: '',
    slug: '',
    content: '',
    is_published: true,
    is_important: false,
  };
  if (!keepMessage) {
    announcementSubmitMessage.value = '';
    announcementSubmitSuccess.value = false;
  }
};

const submitAnnouncementForm = async () => {
  if (
    !announcementForm.value.title.trim() ||
    !announcementForm.value.slug.trim() ||
    !announcementForm.value.content.trim()
  ) {
    announcementSubmitSuccess.value = false;
    announcementSubmitMessage.value = 'لطفاً همه فیلدهای ضروری اطلاعیه را تکمیل کنید.';
    return;
  }

  announcementSubmitLoading.value = true;
  announcementSubmitMessage.value = '';

  const payload = {
    title: announcementForm.value.title.trim(),
    slug: announcementForm.value.slug.trim(),
    content: announcementForm.value.content.trim(),
    is_published: announcementForm.value.is_published,
    is_important: announcementForm.value.is_important,
  };

  try {
    const response = await fetch(getApiUrl('/api/news/announcements/create/'), {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      credentials: 'include',
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (response.ok && data.success) {
      announcementSubmitSuccess.value = true;
      announcementSubmitMessage.value = data.message || 'اطلاعیه با موفقیت ثبت شد.';
      resetAnnouncementForm(true);
      if (isStaff.value) {
        fetchAdminStats();
      }
    } else {
      announcementSubmitSuccess.value = false;
      announcementSubmitMessage.value = data.errors || 'خطا در ثبت اطلاعیه.';
    }
  } catch (error) {
    console.error('Error creating announcement:', error);
    announcementSubmitSuccess.value = false;
    announcementSubmitMessage.value = 'خطا در ارتباط با سرور هنگام ثبت اطلاعیه.';
  } finally {
    announcementSubmitLoading.value = false;
  }
};

const handleEventCoverImageChange = (event: Event) => {
  const input = event.target as HTMLInputElement;
  if (input.files && input.files[0]) {
    eventCoverImageFile.value = input.files[0];
    const reader = new FileReader();
    reader.onload = (e) => {
      eventCoverImagePreview.value = e.target?.result as string;
    };
    reader.readAsDataURL(input.files[0]);
  }
};


const resetEventForm = (keepMessage = false) => {
  eventForm.value = {
    title: '',
    slug: '',
    description: '',
    short_description: '',
    event_type: 'other',
    location: '',
    event_month: null,
    event_year: null,
    registration_deadline: '',
    max_participants: '',
    price: '',
    organizer: '',
    target_audience: '',
    prerequisites: '',
    agenda: '',
    speakers: '',
    contact_info: '',
    is_published: true,
    is_featured: false,
  };
  eventCoverImageFile.value = null;
  eventCoverImagePreview.value = '';
  if (!keepMessage) {
    eventSubmitMessage.value = '';
    eventSubmitSuccess.value = false;
  }
};

const submitEventForm = async () => {
  if (
    !eventForm.value.title.trim() ||
    !eventForm.value.slug.trim() ||
    !eventForm.value.description.trim() ||
    !eventForm.value.location.trim() ||
    !eventForm.value.event_month ||
    !eventForm.value.event_year
  ) {
    eventSubmitSuccess.value = false;
    eventSubmitMessage.value = 'لطفاً فیلدهای ضروری رویداد را تکمیل کنید.';
    return;
  }

  // Ensure we always work with string values to safely call trim()
  const maxParticipantsRaw = (eventForm.value.max_participants ?? '').toString().trim();
  let maxParticipants: number | null = null;
  if (maxParticipantsRaw) {
    maxParticipants = Number(maxParticipantsRaw);
    if (Number.isNaN(maxParticipants) || maxParticipants < 0) {
      eventSubmitSuccess.value = false;
      eventSubmitMessage.value = 'ظرفیت رویداد باید یک عدد معتبر باشد.';
      return;
    }
  }

  const priceRaw = (eventForm.value.price ?? '').toString().trim();
  let price: number | null = null;
  if (priceRaw) {
    price = Number(priceRaw);
    if (Number.isNaN(price) || price < 0) {
      eventSubmitSuccess.value = false;
      eventSubmitMessage.value = 'هزینه رویداد باید یک عدد معتبر باشد.';
      return;
    }
  }

  eventSubmitLoading.value = true;
  eventSubmitMessage.value = '';

  const formData = new FormData();
  formData.append('title', eventForm.value.title.trim());
  formData.append('slug', eventForm.value.slug.trim());
  formData.append('description', eventForm.value.description.trim());
  if (eventForm.value.short_description) {
    formData.append('short_description', eventForm.value.short_description.trim());
  }
  formData.append('event_type', eventForm.value.event_type);
  formData.append('location', eventForm.value.location.trim());
  if (eventForm.value.registration_deadline) {
    formData.append('registration_deadline', eventForm.value.registration_deadline);
  }
  if (maxParticipants !== null) {
    formData.append('max_participants', String(maxParticipants));
  }
  formData.append('price', String(price ?? 0));
  if (eventForm.value.event_month) {
    formData.append('event_month', String(eventForm.value.event_month));
  }
  if (eventForm.value.event_year) {
    formData.append('event_year', String(eventForm.value.event_year));
  }
  if (eventForm.value.organizer) {
    formData.append('organizer', eventForm.value.organizer.trim());
  }
  if (eventForm.value.target_audience) {
    formData.append('target_audience', eventForm.value.target_audience.trim());
  }
  if (eventForm.value.prerequisites) {
    formData.append('prerequisites', eventForm.value.prerequisites.trim());
  }
  if (eventForm.value.agenda) {
    formData.append('agenda', eventForm.value.agenda.trim());
  }
  if (eventForm.value.speakers) {
    formData.append('speakers', eventForm.value.speakers.trim());
  }
  if (eventForm.value.contact_info) {
    formData.append('contact_info', eventForm.value.contact_info.trim());
  }
  formData.append('is_published', String(eventForm.value.is_published));
  formData.append('is_featured', String(eventForm.value.is_featured));
  
  if (eventCoverImageFile.value) {
    formData.append('cover_image', eventCoverImageFile.value);
  }

  try {
    const response = await fetch(getApiUrl('/api/events/create/'), {
      method: 'POST',
      credentials: 'include',
      body: formData,
    });

    const data = await response.json();

    if (response.ok && data.success) {
      eventSubmitSuccess.value = true;
      eventSubmitMessage.value = data.message || 'رویداد با موفقیت ثبت شد.';
      resetEventForm(true);
      if (isStaff.value) {
        fetchAdminStats();
      }
    } else {
      eventSubmitSuccess.value = false;
      eventSubmitMessage.value = data.errors || 'خطا در ثبت رویداد.';
    }
  } catch (error) {
    console.error('Error creating event:', error);
    eventSubmitSuccess.value = false;
    eventSubmitMessage.value = 'خطا در ارتباط با سرور هنگام ثبت رویداد.';
  } finally {
    eventSubmitLoading.value = false;
  }
};

const uploadProfileImage = async () => {
  if (!selectedImageFile.value) {
    imageUploadMessage.value = 'لطفاً یک فایل انتخاب کنید';
    imageUploadSuccess.value = false;
    return;
  }

  imageUploadLoading.value = true;
  imageUploadMessage.value = '';

  const formData = new FormData();
  formData.append('profile_image', selectedImageFile.value);

  try {
    const response = await fetch(getApiUrl('/api/accounts/profile/image/upload/'), {
      method: 'POST',
      body: formData,
      credentials: 'include'
    });

    const data = await response.json();

    if (data.success) {
      imageUploadSuccess.value = true;
      imageUploadMessage.value = data.message || 'عکس پروفایل با موفقیت به‌روزرسانی شد';
      
      // Immediately update user profile_image with the URL from server
      if (data.profile_image_url) {
        user.value.profile_image = data.profile_image_url;
      }
      
      // Refresh user profile immediately to get latest data from database
      await fetchUserProfile();
      
      // Force component re-render
      await nextTick();
      
      // Close modal after short delay
      setTimeout(() => {
        showImageUploadModal.value = false;
        imagePreviewUrl.value = '';
        selectedImageFile.value = null;
        const input = document.getElementById('profileImageInput') as HTMLInputElement;
        if (input) input.value = '';
        
        // Force page reload to show new image
        window.location.reload();
      }, 1000);
    } else {
      imageUploadSuccess.value = false;
      imageUploadMessage.value = data.errors || 'خطا در آپلود عکس';
    }
  } catch (error) {
    imageUploadSuccess.value = false;
    imageUploadMessage.value = 'خطا در ارتباط با سرور';
    console.error('Error uploading image:', error);
  } finally {
    imageUploadLoading.value = false;
  }
};

const deleteProfileImage = async () => {
  if (!confirm('آیا مطمئن هستید که می‌خواهید عکس پروفایل را حذف کنید؟')) {
    return;
  }

  imageDeleteLoading.value = true;

  try {
    const response = await fetch(getApiUrl('/api/accounts/profile/image/delete/'), {
      method: 'DELETE',
      credentials: 'include'
    });

    const data = await response.json();

    if (data.success) {
      // FORCE clear profile image immediately
      user.value.profile_image = '';
      user.value = { ...user.value, profile_image: '' };
      
      // Force refresh profile to get latest data from database
      await fetchUserProfile();
      
      // Force component re-render and clear cache
      await nextTick();
      
      // Force page reload to clear all cache
      setTimeout(() => {
        window.location.reload();
      }, 500);
    } else {
      alert(data.errors || 'خطا در حذف عکس');
    }
  } catch (error) {
    console.error('Error deleting image:', error);
    alert('خطا در ارتباط با سرور');
  } finally {
    imageDeleteLoading.value = false;
  }
};

const updateResume = async () => {
  resumeLoading.value = true;
  resumeMessage.value = '';

  try {
    const response = await fetch(getApiUrl('/api/accounts/profile/resume/update/'), {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      credentials: 'include',
      body: JSON.stringify(resumeForm.value)
    });

    const data = await response.json();

    if (data.success) {
      resumeSuccess.value = true;
      resumeMessage.value = data.message || 'رزومه با موفقیت به‌روزرسانی شد';
      
      // Update user data
      if (data.resume) {
        user.value = { ...user.value, ...data.resume };
      }
      
      setTimeout(() => {
        showResumeModal.value = false;
        fetchUserProfile();
      }, 1500);
    } else {
      resumeSuccess.value = false;
      resumeMessage.value = data.errors || 'خطا در ذخیره رزومه';
    }
  } catch (error) {
    resumeSuccess.value = false;
    resumeMessage.value = 'خطا در ارتباط با سرور';
    console.error('Error updating resume:', error);
  } finally {
    resumeLoading.value = false;
  }
};

onMounted(() => {
  fetchUserProfile();
});
</script>

<style scoped>
.dashboard-wrapper {
  position: relative;
  min-height: 100vh;
  background: #f3f4f8;
  overflow-x: hidden;
}

.dashboard-bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(13, 110, 253, 0.12) 0%, rgba(9, 181, 211, 0.08) 45%, rgba(120, 81, 255, 0.12) 100%);
  filter: blur(80px);
  transform: scale(1.1);
  z-index: 0;
}

.dashboard-decoration {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 0;
}

.dashboard-shape {
  position: absolute;
  border-radius: 999px;
  opacity: 0.45;
}

.dashboard-shape.shape-1 {
  width: 320px;
  height: 320px;
  background: radial-gradient(circle, rgba(13, 110, 253, 0.35), transparent 65%);
  top: -140px;
  right: -60px;
}

.dashboard-shape.shape-2 {
  width: 220px;
  height: 220px;
  background: radial-gradient(circle, rgba(32, 201, 151, 0.28), transparent 70%);
  bottom: 120px;
  left: -80px;
}

.dashboard-shape.shape-3 {
  width: 180px;
  height: 180px;
  background: radial-gradient(circle, rgba(132, 94, 247, 0.3), transparent 70%);
  top: 220px;
  left: 35%;
}

.dashboard-content {
  position: relative;
  z-index: 1;
}

.dashboard-loading p {
  color: #4b5d77;
}

.glass-card {
  background: rgba(255, 255, 255, 0.92);
  box-shadow: 0 25px 60px rgba(15, 23, 42, 0.08);
  border-radius: 24px;
  border: 1px solid rgba(255, 255, 255, 0.4);
  backdrop-filter: blur(16px);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.glass-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 28px 65px rgba(15, 23, 42, 0.14);
}

.hero-card {
  position: relative;
  overflow: hidden;
}

.hero-card::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at top right, rgba(13, 110, 253, 0.18), transparent 55%);
  z-index: 0;
}

.hero-card > * {
  position: relative;
  z-index: 1;
}

.hero-avatar {
  width: 72px;
  height: 72px;
  border-radius: 24px;
  background: linear-gradient(135deg, #0d6efd 0%, #845ef7 100%);
  color: #fff;
  font-weight: 700;
  font-size: 1.6rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 12px 30px rgba(13, 110, 253, 0.35);
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.85rem;
  padding: 0.35rem 0.8rem;
  border-radius: 999px;
  background: rgba(13, 110, 253, 0.1);
  color: #0d6efd;
  font-weight: 600;
}

.hero-title {
  font-size: clamp(1.8rem, 3vw, 2.4rem);
  font-weight: 800;
  color: #14233c;
}

.hero-subtitle {
  color: #4b5d77;
  font-size: 1rem;
}

.hero-quote {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  padding: 0.45rem 1rem;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.72);
  box-shadow: 0 12px 28px rgba(15, 23, 42, 0.12);
  font-size: 0.95rem;
  color: #3c4d6b;
}

.hero-quote i {
  color: #845ef7;
}

.hero-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.35rem 0.9rem;
  border-radius: 999px;
  background: rgba(25, 135, 84, 0.1);
  color: #198754;
  font-size: 0.85rem;
  font-weight: 600;
}

.hero-tag.warning {
  background: rgba(255, 193, 7, 0.15);
  color: #d08700;
}

.hero-actions .btn {
  border-radius: 18px;
  padding: 0.75rem 1.4rem;
  font-weight: 600;
}

.hero-actions .btn-outline-light {
  border: 1px solid rgba(255, 255, 255, 0.6);
  color: #fff;
}

.hero-actions .btn-outline-light:hover {
  background: rgba(255, 255, 255, 0.15);
}

.stat-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.4rem 1.6rem;
  border-radius: 20px;
}

.stat-card--primary {
  background: linear-gradient(135deg, rgba(13, 110, 253, 0.12), rgba(13, 202, 240, 0.1));
}

.stat-card--success {
  background: linear-gradient(135deg, rgba(25, 135, 84, 0.12), rgba(56, 193, 114, 0.1));
}

.stat-card--warning {
  background: linear-gradient(135deg, rgba(255, 193, 7, 0.12), rgba(255, 159, 67, 0.1));
}

.stat-card--info {
  background: linear-gradient(135deg, rgba(13, 202, 240, 0.12), rgba(32, 201, 151, 0.1));
}

.stat-card--violet {
  background: linear-gradient(135deg, rgba(120, 81, 255, 0.14), rgba(64, 93, 230, 0.12));
}

.stat-icon {
  width: 52px;
  height: 52px;
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.85);
  color: #0d6efd;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  box-shadow: inset 0 0 0 1px rgba(13, 110, 253, 0.08);
}

.stat-meta {
  color: #20324d;
}

.stat-title {
  font-size: 0.85rem;
  letter-spacing: 0.02em;
  text-transform: uppercase;
  margin-bottom: 0.35rem;
}

.stat-value {
  font-size: 1.8rem;
  font-weight: 700;
}

.stat-desc {
  font-size: 0.9rem;
  color: #5f6f8d;
}

.profile-alert {
  padding: 1.6rem 1.8rem;
  border-radius: 20px;
  border: 1px solid rgba(255, 193, 7, 0.25);
  background: linear-gradient(120deg, rgba(255, 249, 196, 0.65), rgba(255, 243, 205, 0.4));
}

.admin-stats-wrapper {
  border-radius: 24px;
}

.admin-stats-icon {
  width: 48px;
  height: 48px;
  border-radius: 16px;
  background: rgba(13, 110, 253, 0.15);
  color: #0d6efd;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
}

.admin-stat-card {
  display: flex;
  align-items: center;
  gap: 0.9rem;
  padding: 1.1rem 1.2rem;
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(13, 110, 253, 0.08);
  box-shadow: 0 18px 38px rgba(15, 23, 42, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.admin-stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 24px 48px rgba(15, 23, 42, 0.14);
}

.admin-management-wrapper {
  border-radius: 24px;
}

.admin-management-icon {
  width: 48px;
  height: 48px;
  border-radius: 16px;
  background: rgba(13, 110, 253, 0.15);
  color: #0d6efd;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
}

.admin-management-tabs .btn {
  border-radius: 18px;
  padding: 0.6rem 1.2rem;
  font-weight: 600;
  transition: all 0.2s ease;
}

.btn-soft-light {
  background: rgba(20, 35, 60, 0.08);
  color: #20324d;
  border: none;
}

.btn-soft-light:hover,
.btn-soft-light.active {
  background: linear-gradient(135deg, rgba(13, 110, 253, 0.18), rgba(120, 81, 255, 0.18));
  color: #0d6efd;
  box-shadow: 0 12px 24px rgba(15, 23, 42, 0.12);
  transform: translateY(-2px);
}

.admin-form-card {
  background: rgba(255, 255, 255, 0.92);
  border-radius: 20px;
  padding: 1.5rem;
  box-shadow: inset 0 0 0 1px rgba(13, 110, 253, 0.05);
}

.admin-form-title {
  font-weight: 700;
  color: #14233c;
  margin-bottom: 1.25rem;
}

.admin-stat-card--primary {
  background: linear-gradient(135deg, rgba(13, 110, 253, 0.14), rgba(13, 202, 240, 0.1));
}

.admin-stat-card--info {
  background: linear-gradient(135deg, rgba(13, 202, 240, 0.14), rgba(32, 201, 151, 0.1));
}

.admin-stat-card--success {
  background: linear-gradient(135deg, rgba(25, 135, 84, 0.14), rgba(56, 193, 114, 0.1));
}

.admin-stat-card--warning {
  background: linear-gradient(135deg, rgba(255, 193, 7, 0.16), rgba(255, 159, 67, 0.12));
}

.admin-stat-card--violet {
  background: linear-gradient(135deg, rgba(120, 81, 255, 0.16), rgba(64, 93, 230, 0.12));
}

.admin-stat-icon-circle {
  width: 46px;
  height: 46px;
  border-radius: 15px;
  background: rgba(255, 255, 255, 0.85);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  color: #0d6efd;
  box-shadow: inset 0 0 0 1px rgba(13, 110, 253, 0.08);
}

.admin-stat-content {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.admin-stat-label {
  font-size: 0.85rem;
  color: #4b5d77;
}

.admin-stat-value {
  font-size: 1.6rem;
  font-weight: 700;
  color: #14233c;
}

.alert-icon {
  width: 48px;
  height: 48px;
  border-radius: 16px;
  background: rgba(255, 193, 7, 0.18);
  color: #d08700;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
}

.missing-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.35rem 0.9rem;
  border-radius: 999px;
  border: 1px solid rgba(255, 193, 7, 0.35);
  background: rgba(255, 255, 255, 0.85);
  color: #b67300;
  font-size: 0.85rem;
}

.modern-form .form-label {
  font-weight: 600;
  color: #2c3e5b;
}

.modern-input {
  border-radius: 14px;
  border: 1px solid rgba(20, 35, 60, 0.1);
  padding: 0.8rem 1rem;
  background: rgba(255, 255, 255, 0.85);
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.modern-input:focus {
  border-color: rgba(13, 110, 253, 0.5);
  box-shadow: 0 0 0 4px rgba(13, 110, 253, 0.12);
}

.modern-btn {
  border-radius: 14px;
  padding: 0.8rem 1.4rem;
  font-weight: 600;
}

.btn-soft-primary,
.btn-soft-info,
.btn-soft-danger {
  border-radius: 14px;
  padding: 0.75rem 1.1rem;
  font-weight: 600;
  border: none;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.btn-soft-primary {
  background: rgba(13, 110, 253, 0.12);
  color: #0d6efd;
}

.btn-soft-primary:hover {
  background: rgba(13, 110, 253, 0.18);
  color: #0b5ed7;
}

.btn-soft-info {
  background: rgba(32, 201, 151, 0.12);
  color: #20c997;
}

.btn-soft-info:hover {
  background: rgba(32, 201, 151, 0.18);
  color: #1ba97e;
}

.btn-soft-danger {
  background: rgba(220, 53, 69, 0.12);
  color: #dc3545;
}

.btn-soft-danger:hover {
  background: rgba(220, 53, 69, 0.18);
  color: #bb2d3b;
}

.btn-soft-warning {
  background: rgba(255, 193, 7, 0.12);
  color: #ffc107;
  border-radius: 14px;
  padding: 0.75rem 1.1rem;
  font-weight: 600;
  border: none;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.btn-soft-warning:hover {
  background: rgba(255, 193, 7, 0.18);
  color: #ffb300;
  transform: translateY(-2px);
  box-shadow: 0 12px 24px rgba(15, 23, 42, 0.12);
}

.btn-soft-primary:hover,
.btn-soft-info:hover,
.btn-soft-danger:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 24px rgba(15, 23, 42, 0.12);
}

.glass-card-header {
  background: linear-gradient(135deg, rgba(248, 250, 255, 0.85), rgba(255, 255, 255, 0.72));
  border-radius: 20px 20px 0 0;
  padding: 1.2rem 1.5rem;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.9rem 1rem;
  border-radius: 16px;
  background: rgba(248, 250, 255, 0.85);
}

.detail-icon {
  width: 40px;
  height: 40px;
  border-radius: 14px;
  background: rgba(13, 110, 253, 0.12);
  color: #0d6efd;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
}

.detail-label {
  font-size: 0.85rem;
  color: #5f6f8d;
}

.detail-value {
  font-weight: 600;
  color: #1c2d4b;
  font-size: 1.05rem;
}

.user-avatar-glow {
  position: absolute;
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(13, 110, 253, 0.25), transparent 65%);
  filter: blur(0.5px);
  transform: translateY(-8px);
}

.user-avatar-large {
  width: 110px;
  height: 110px;
  border-radius: 32px;
  background: linear-gradient(135deg, #0d6efd 0%, #845ef7 100%);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 2.2rem;
  color: white;
  box-shadow: 0 15px 40px rgba(13, 110, 253, 0.35);
}

.user-profile-image {
  width: 110px;
  height: 110px;
  border-radius: 32px;
  object-fit: cover;
  box-shadow: 0 15px 40px rgba(13, 110, 253, 0.25);
}

.user-avatar-container {
  position: relative;
  display: flex;
  justify-content: center;
}

.profile-progress .progress {
  height: 10px;
}

.modern-progress {
  background: rgba(13, 110, 253, 0.12);
  border-radius: 999px;
  overflow: hidden;
}

.modern-progress .progress-bar {
  background: linear-gradient(90deg, #0d6efd, #845ef7);
}

.card {
  border-radius: 24px;
  border: none;
  background: transparent;
}

.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: opacity 0.25s ease, transform 0.25s ease;
}

.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}

@media (max-width: 991.98px) {
  .hero-actions {
    flex-direction: row !important;
  }
}

@media (max-width: 575.98px) {
  .glass-card {
    border-radius: 20px;
  }

  .hero-avatar {
    width: 64px;
    height: 64px;
    font-size: 1.4rem;
  }

  .stat-card {
    padding: 1.1rem 1.2rem;
  }
}
</style>

