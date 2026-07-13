from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customuser_approval_status_customuser_approved_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='current_position',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='سمت فعلی'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='expertise_areas',
            field=models.TextField(blank=True, null=True, verbose_name='حوزه‌های تخصص'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='work_experience',
            field=models.TextField(blank=True, null=True, verbose_name='سوابق کاری'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='workplace',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='محل کار'),
        ),
    ]
