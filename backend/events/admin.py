from django.contrib import admin
from .models import Event, EventRegistration


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'event_month', 'event_year', 'location', 'is_published', 'is_featured', 'views', 'created_at')
    list_filter = ('event_type', 'is_published', 'is_featured', 'event_month', 'event_year')
    search_fields = ('title', 'description', 'short_description', 'location', 'organizer')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('views', 'created_at', 'updated_at')
    
    fieldsets = (
        ('اطلاعات اصلی رویداد', {
            'fields': ('title', 'slug', 'event_type', 'short_description', 'description')
        }),
        ('تصاویر', {
            'fields': ('cover_image', 'image'),
            'description': 'تصویر کاور برای نمایش در لیست رویدادها و تصویر قدیمی (اختیاری)'
        }),
        ('تاریخ و مکان', {
            'fields': ('event_month', 'event_year', 'location')
        }),
        ('جزئیات رویداد', {
            'fields': ('organizer', 'target_audience', 'prerequisites', 'agenda', 'speakers', 'contact_info'),
            'classes': ('collapse',)
        }),
        ('ثبت نام و هزینه', {
            'fields': ('registration_deadline', 'max_participants', 'price')
        }),
        ('تنظیمات انتشار', {
            'fields': ('created_by', 'is_published', 'is_featured')
        }),
        ('آمار و اطلاعات سیستم', {
            'fields': ('views', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'is_confirmed', 'registered_at')
    list_filter = ('is_confirmed', 'registered_at')
    search_fields = ('user__username', 'event__title')
    readonly_fields = ('registered_at',)

