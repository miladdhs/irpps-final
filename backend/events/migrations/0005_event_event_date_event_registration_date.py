from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_retraining_number_alter_event_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ برگزاری'),
        ),
        migrations.AddField(
            model_name='event',
            name='registration_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ ثبت نام'),
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-event_date', '-event_year', '-event_month', '-created_at'], 'verbose_name': 'رویداد', 'verbose_name_plural': 'رویدادها'},
        ),
    ]
