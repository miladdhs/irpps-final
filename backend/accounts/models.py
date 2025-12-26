from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


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
    is_active = models.BooleanField(default=False, verbose_name='فعال')  # Changed default to False
    
    # Membership approval workflow fields
    APPROVAL_STATUS_CHOICES = [
        ('pending', 'در انتظار تایید'),
        ('approved', 'تایید شده'),
        ('rejected', 'رد شده'),
    ]
    approval_status = models.CharField(
        max_length=20,
        choices=APPROVAL_STATUS_CHOICES,
        default='pending',
        verbose_name='وضعیت تایید'
    )
    requested_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ درخواست')
    approved_at = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ تایید')
    approved_by = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='approved_members',
        verbose_name='تایید شده توسط'
    )
    rejection_reason = models.TextField(blank=True, null=True, verbose_name='دلیل رد')
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        ordering = ['-date_joined']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}" if self.first_name else self.username
    
    def approve_membership(self, approved_by_user):
        """Approve user membership"""
        self.approval_status = 'approved'
        self.is_active = True
        self.approved_at = timezone.now()
        self.approved_by = approved_by_user
        self.save()
    
    def reject_membership(self, reason='', rejected_by_user=None):
        """Reject user membership"""
        self.approval_status = 'rejected'
        self.is_active = False
        self.rejection_reason = reason
        if rejected_by_user:
            self.approved_by = rejected_by_user  # Track who rejected
        self.save()

