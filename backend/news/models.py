from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class News(models.Model):
    """News model"""
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ')
    content = models.TextField(verbose_name='محتوا')
    short_content = models.TextField(max_length=500, blank=True, null=True, verbose_name='خلاصه خبر')
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name='تصویر')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news', verbose_name='نویسنده')
    category = models.CharField(max_length=100, blank=True, null=True, verbose_name='دسته‌بندی')
    tags = models.CharField(max_length=300, blank=True, null=True, verbose_name='برچسب‌ها (جدا شده با کاما)')
    source = models.CharField(max_length=200, blank=True, null=True, verbose_name='منبع')
    is_published = models.BooleanField(default=True, verbose_name='منتشر شده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    views = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    
    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Announcement(models.Model):
    """Announcement model"""
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ')
    content = models.TextField(verbose_name='محتوا')
    image = models.ImageField(upload_to='announcements/', blank=True, null=True, verbose_name='تصویر')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='announcements', verbose_name='نویسنده')
    is_published = models.BooleanField(default=True, verbose_name='منتشر شده')
    is_important = models.BooleanField(default=False, verbose_name='مهم')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    views = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    
    class Meta:
        verbose_name = 'اطلاعیه'
        verbose_name_plural = 'اطلاعیه‌ها'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

