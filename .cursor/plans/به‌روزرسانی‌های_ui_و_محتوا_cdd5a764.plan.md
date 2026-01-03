---
name: به‌روزرسانی‌های UI و محتوا
overview: انجام تغییرات متعدد در رابط کاربری شامل حذف فیلدهای رویداد، اصلاح مودال‌ها، تغییرات محتوا و سازماندهی فایل‌ها
todos:
  - id: remove_event_fields
    content: حذف هزینه و ظرفیت و وضعیت ثبت نام از کارت رویدادها
    status: pending
  - id: show_event_id
    content: نمایش شناسه عددی رویداد به جای 'ویژه' در کارت رویدادها
    status: pending
  - id: fix_modals_scroll
    content: اصلاح مشکل اسکرول در مودال‌های رزومه، محصولات و انتشارات
    status: pending
  - id: remove_home_texts
    content: حذف متن‌های subtitle و description از صفحه هوم
    status: pending
  - id: empty_founders
    content: خالی کردن بخش موسسین در صفحه درباره ما
    status: pending
  - id: fix_board_title
    content: حذف 'موسسین انجمن' از عنوان صفحه هیئت مدیره اول
    status: pending
  - id: update_email
    content: تغییر ایمیل تماس به info@irspp.ir
    status: pending
  - id: move_abstracts_file
    content: انتقال فایل 'خلاصه مقالات 5 همایش 403.pdf' از سایر محصولات به کتابچه کنگره‌ها
    status: pending
  - id: remove_book_folders
    content: حذف پوشه‌های 'هیپوتیروئیدی'، 'تکامل' و 'گفتار خانواده' از کتاب‌ها
    status: pending
  - id: remove_brochures
    content: حذف کامل بخش بروشورها از صفحه آموزش
    status: pending
---

# برنامه به‌روزرسانی‌های UI و محتوا

## تغییرات کارت رویدادها

1. **حذف هزینه و ظرفیت از کارت رویداد** ([frontend/src/views/Events.vue](frontend/src/views/Events.vue))

- حذف لی آیتم‌های `capacity` و `fee` از `event-card-info`

2. **حذف وضعیت ثبت نام از کارت رویداد** ([frontend/src/views/Events.vue](frontend/src/views/Events.vue))

- حذف badge نمایش "ثبت‌نام باز است" یا "ثبت‌نام بسته است"

3. **نمایش شناسه عددی به جای "ویژه"** ([frontend/src/views/Events.vue](frontend/src/views/Events.vue))

- تغییر badge از `is_featured ? 'ویژه' : event.event_type` به نمایش `event.id`

4. **حذف هزینه از صفحه جزئیات رویداد** ([frontend/src/views/EventDetail.vue](frontend/src/views/EventDetail.vue))

- حذف info-card نمایش "هزینه شرکت"

## اصلاح مشکل اسکرول مودال‌ها

5. **اصلاح مودال رزومه** ([frontend/src/views/Dashboard.vue](frontend/src/views/Dashboard.vue))

- بررسی و اصلاح استایل `max-height` و `overflow-y: auto` در modal-body

6. **اصلاح مودال محصولات/انتشارات** ([frontend/src/views/Publications.vue](frontend/src/views/Publications.vue) و [frontend/src/views/Doctors.vue](frontend/src/views/Doctors.vue))

- اطمینان از وجود `overflow-y: auto` و ارتفاع محدود در modal-body

## تغییرات محتوا

7. **حذف متن‌های صفحه هوم** ([frontend/src/i18n/locales/fa.json](frontend/src/i18n/locales/fa.json))

- خالی کردن `home.subtitle` و `home.description`

8. **خالی کردن بخش موسسین در صفحه درباره ما** ([frontend/src/views/About.vue](frontend/src/views/About.vue))

- حذف تمام founder-item ها از بخش founders

9. **حذف "موسسین انجمن" از عنوان صفحه هیئت مدیره اول** ([frontend/src/views/BoardFirst.vue](frontend/src/views/BoardFirst.vue))

- تغییر عنوان از "موسسین انجمن (هیئت مدیره اول)" به "هیئت مدیره اول"

10. **تغییر ایمیل تماس** ([frontend/src/views/Contact.vue](frontend/src/views/Contact.vue))

    - تغییر از `info@childrenlung.ir` به `info@irspp.ir`

## سازماندهی فایل‌ها

11. **انتقال فایل خلاصه مقالات** ([frontend/src/views/Publications.vue](frontend/src/views/Publications.vue))

    - حذف "خلاصه مقالات 5 همایش 403.pdf" از لیست products
    - اضافه کردن به لیست congress

12. **حذف پوشه‌های کتاب** ([frontend/src/views/Doctors.vue](frontend/src/views/Doctors.vue))