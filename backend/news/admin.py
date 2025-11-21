from django.contrib import admin
from .models import News, Announcement


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'is_published', 'views', 'created_at')
    list_filter = ('is_published', 'category', 'created_at')
    search_fields = ('title', 'content', 'short_content', 'author__username', 'category', 'tags', 'source')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('views', 'created_at', 'updated_at')
    
    fieldsets = (
        ('اطلاعات اصلی خبر', {
            'fields': ('title', 'slug', 'short_content', 'content')
        }),
        ('تصویر و رسانه', {
            'fields': ('image',),
            'description': 'تصویر اصلی خبر برای نمایش در لیست و صفحه جزئیات'
        }),
        ('دسته‌بندی و برچسب‌ها', {
            'fields': ('category', 'tags', 'source')
        }),
        ('تنظیمات انتشار', {
            'fields': ('author', 'is_published')
        }),
        ('آمار و اطلاعات سیستم', {
            'fields': ('views', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'is_important', 'views', 'created_at')
    list_filter = ('is_published', 'is_important', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('views', 'created_at', 'updated_at')
    
    fieldsets = (
        ('اطلاعات اصلی اطلاعیه', {
            'fields': ('title', 'slug', 'content')
        }),
        ('تصویر', {
            'fields': ('image',),
            'description': 'تصویر اطلاعیه (اختیاری)'
        }),
        ('تنظیمات انتشار', {
            'fields': ('author', 'is_published', 'is_important')
        }),
        ('آمار و اطلاعات سیستم', {
            'fields': ('views', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

