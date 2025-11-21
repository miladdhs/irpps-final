from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Extended User model with additional fields
    
    NOTE: Name fields usage:
    - first_name: Persian name (نام فارسی)
    - last_name: English full name (نام کامل انگلیسی)
    """
    phone = models.CharField(max_length=200, blank=True, null=True, verbose_name='شماره تلفن')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='شهر')
    specialty = models.CharField(max_length=200, blank=True, null=True, verbose_name='تخصص')
    experience = models.IntegerField(default=0, verbose_name='سابقه کار (سال)')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, verbose_name='امتیاز')
    bio = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    # Profile image
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True, verbose_name='عکس پروفایل')
    # Resume fields
    education = models.TextField(blank=True, null=True, verbose_name='تحصیلات')
    publications = models.TextField(blank=True, null=True, verbose_name='مقالات و انتشارات')
    awards = models.TextField(blank=True, null=True, verbose_name='جوایز و افتخارات')
    certifications = models.TextField(blank=True, null=True, verbose_name='گواهینامه‌ها')
    research_interests = models.TextField(blank=True, null=True, verbose_name='علایق پژوهشی')
    languages = models.CharField(max_length=200, blank=True, null=True, verbose_name='زبان‌ها')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        ordering = ['-date_joined']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}" if self.first_name else self.username

