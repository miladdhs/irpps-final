from django.db import models


class Service(models.Model):
    """Model for association services"""
    
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    icon = models.CharField(max_length=100, verbose_name='آیکون', help_text='Material Icon name')
    link = models.CharField(max_length=200, default='#', verbose_name='لینک')
    link_text = models.CharField(max_length=100, default='اطلاعات بیشتر', verbose_name='متن لینک')
    order = models.IntegerField(default=0, verbose_name='ترتیب نمایش')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'
        ordering = ['order', 'id']

    def __str__(self):
        return self.title
