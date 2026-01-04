"""
Management command to update registration deadlines for existing events
Usage: python manage.py update_events_registration
"""
from django.core.management.base import BaseCommand
from events.models import Event

# Try to import jdatetime for Persian date conversion
try:
    import jdatetime
    HAS_JDATETIME = True
except ImportError:
    HAS_JDATETIME = False


class Command(BaseCommand):
    help = 'Update registration deadlines for existing events'

    def persian_to_gregorian_date(self, year, month, day):
        """Convert Persian date to Gregorian date"""
        try:
            if HAS_JDATETIME:
                persian_date = jdatetime.date(year, month, day)
                gregorian_date = persian_date.togregorian()
                return gregorian_date
            else:
                # Fallback: approximate conversion
                from datetime import date
                approx_year = year + 621
                return date(approx_year, month, min(day, 28))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Error converting date: {e}'))
            return None

    def handle(self, *args, **options):
        # Mapping of event slugs to their registration deadlines
        # ورکشاپ POCUS: 5 بهمن 1404
        # کنفرانس علمی یک روزه: 2 دی 1404
        # چهارمین کنگره: 20 دی 1404
        
        events_to_update = {
            'workshop-pocus-1404': {
                'deadline': self.persian_to_gregorian_date(1404, 11, 5),
                'title': 'ورکشاپ عملی POCUS'
            },
            'conference-respiratory-children-1404': {
                'deadline': self.persian_to_gregorian_date(1404, 10, 2),
                'title': 'کنفرانس علمی یک روزه: بیماری شایع تنفسی کودکان'
            },
            'congress-pediatric-pulmonary-2026': {
                'deadline': self.persian_to_gregorian_date(1404, 10, 20),
                'title': 'چهارمین کنگره بین‌المللی ریه و اختلالات تنفسی خواب کودکان'
            },
        }

        updated_count = 0
        not_found_count = 0

        for slug, data in events_to_update.items():
            try:
                event = Event.objects.get(slug=slug)
                if data['deadline']:
                    event.registration_deadline = data['deadline']
                    event.save(update_fields=['registration_deadline'])
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'✓ Updated {data["title"]}: registration_deadline = {data["deadline"]}'
                        )
                    )
                    updated_count += 1
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f'⚠ Could not convert date for {data["title"]}'
                        )
                    )
            except Event.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(
                        f'⚠ Event with slug "{slug}" not found'
                    )
                )
                not_found_count += 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f'✗ Error updating {data["title"]}: {e}'
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n✓ Successfully updated {updated_count} event(s)'
            )
        )
        if not_found_count > 0:
            self.stdout.write(
                self.style.WARNING(
                    f'⚠ {not_found_count} event(s) not found'
                )
            )

