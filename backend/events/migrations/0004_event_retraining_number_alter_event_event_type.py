# Generated migration

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_previous'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='retraining_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='شماره بازآموزی'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('conference', 'کنفرانس'), ('workshop', 'کارگاه'), ('seminar', 'سمینار'), ('congress', 'کنگره'), ('webinar', 'وبینار'), ('other', 'سایر')], default='other', max_length=20, verbose_name='نوع رویداد'),
        ),
    ]
