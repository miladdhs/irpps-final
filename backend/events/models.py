from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.Model):
    """Event model"""
    EVENT_TYPES = [
        ('conference', 'کنفرانس'),
        ('workshop', 'کارگاه'),
        ('seminar', 'سمینار'),
        ('congress', 'کنگره'),
        ('webinar', 'وبینار'),
        ('other', 'سایر'),
    ]
    
    MONTH_CHOICES = [
        (1, 'فروردین'), (2, 'اردیبهشت'), (3, 'خرداد'),
        (4, 'تیر'), (5, 'مرداد'), (6, 'شهریور'),
        (7, 'مهر'), (8, 'آبان'), (9, 'آذر'),
        (10, 'دی'), (11, 'بهمن'), (12, 'اسفند'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ')
    description = models.TextField(verbose_name='توضیحات')
    short_description = models.TextField(max_length=500, blank=True, null=True, verbose_name='خلاصه توضیحات')
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='other', verbose_name='نوع رویداد')
    cover_image = models.ImageField(upload_to='events/covers/', blank=True, null=True, verbose_name='تصویر کاور')
    image = models.ImageField(upload_to='events/', blank=True, null=True, verbose_name='تصویر (قدیمی)')
    location = models.CharField(max_length=200, verbose_name='مکان')
    event_month = models.IntegerField(choices=MONTH_CHOICES, blank=True, null=True, verbose_name='ماه رویداد')
    event_year = models.IntegerField(blank=True, null=True, verbose_name='سال رویداد')
    registration_deadline = models.DateField(blank=True, null=True, verbose_name='مهلت ثبت نام')
    
    # فیلد جدید: شماره بازآموزی
    retraining_number = models.CharField(max_length=100, blank=True, null=True, verbose_name='شماره بازآموزی')
    
    max_participants = models.IntegerField(blank=True, null=True, verbose_name='حداکثر شرکت‌کننده')
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name='قیمت')
    organizer = models.CharField(max_length=200, blank=True, null=True, verbose_name='برگزارکننده')
    target_audience = models.CharField(max_length=200, blank=True, null=True, verbose_name='مخاطبان')
    prerequisites = models.TextField(blank=True, null=True, verbose_name='پیش‌نیازها')
    agenda = models.TextField(blank=True, null=True, verbose_name='برنامه زمانی')
    speakers = models.TextField(blank=True, null=True, verbose_name='سخنرانان')
    contact_info = models.CharField(max_length=300, blank=True, null=True, verbose_name='اطلاعات تماس')
    is_published = models.BooleanField(default=True, verbose_name='منتشر شده')
    is_featured = models.BooleanField(default=False, verbose_name='ویژه')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events', verbose_name='ایجادکننده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    views = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    
    class Meta:
        verbose_name = 'رویداد'
        verbose_name_plural = 'رویدادها'
        ordering = ['-event_year', '-event_month']
    
    def __str__(self):
        return self.title
    
    @property
    def is_registration_open(self):
        """Check if registration is still open"""
        from django.utils import timezone
        from datetime import date
        if self.registration_deadline:
            return date.today() <= self.registration_deadline
        return True


class EventRegistration(models.Model):
    """Event registration model"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations', verbose_name='رویداد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_registrations', verbose_name='کاربر')
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت نام')
    is_confirmed = models.BooleanField(default=False, verbose_name='تأیید شده')
    notes = models.TextField(blank=True, null=True, verbose_name='یادداشت')
    
    class Meta:
        verbose_name = 'ثبت نام رویداد'
        verbose_name_plural = 'ثبت نام‌های رویداد'
        unique_together = ('event', 'user')
        ordering = ['-registered_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.event.title}"

