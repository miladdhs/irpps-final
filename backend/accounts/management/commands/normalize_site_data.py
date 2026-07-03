import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from accounts.member_directory import FIRST_NAME_OVERRIDES, contains_latin, contains_persian
from accounts.models import CustomUser
from events.models import Event
from news.models import Announcement, News


class Command(BaseCommand):
    help = "Normalize member names, remove bad seed content, and ensure default images."

    def handle(self, *args, **options):
        with transaction.atomic():
            member_updates = self.normalize_member_names()
            removed_news, removed_announcements = self.remove_bad_seed_content()
            news_images, announcement_images, event_images = self.ensure_default_images()

        self.stdout.write(self.style.SUCCESS("Site data normalization finished."))
        self.stdout.write(
            f"Members updated: {member_updates} | "
            f"Bad news removed: {removed_news} | "
            f"Bad announcements removed: {removed_announcements} | "
            f"News images fixed: {news_images} | "
            f"Announcement images fixed: {announcement_images} | "
            f"Event images fixed: {event_images}"
        )

    def normalize_member_names(self):
        updated = 0
        for user in CustomUser.objects.filter(is_superuser=False):
            original = (user.first_name or "").strip()
            fallback = (user.last_name or "").strip()
            normalized = FIRST_NAME_OVERRIDES.get(original)

            if not normalized and contains_latin(original) and contains_persian(fallback):
                normalized = fallback

            if normalized and normalized != user.first_name:
                user.first_name = normalized
                user.save(update_fields=["first_name"])
                updated += 1

        return updated

    def remove_bad_seed_content(self):
        news_removed = News.objects.filter(slug="2ROOD").delete()[0]
        announcement_removed = Announcement.objects.filter(title="دروددددد").delete()[0]
        return news_removed, announcement_removed

    def ensure_default_images(self):
        repo_root = Path(settings.BASE_DIR).parent
        media_root = Path(settings.MEDIA_ROOT)

        news_source = repo_root / "frontend" / "public" / "img" / "news.png"
        events_source = repo_root / "frontend" / "public" / "img" / "events.png"

        news_relative = self.copy_default_asset(news_source, media_root / "news" / "default-news.png", "news/default-news.png")
        event_relative = self.copy_default_asset(events_source, media_root / "events" / "covers" / "default-event.png", "events/covers/default-event.png")

        news_count = 0
        for item in News.objects.filter(image__isnull=True):
            item.image = news_relative
            item.save(update_fields=["image"])
            news_count += 1
        for item in News.objects.filter(image=""):
            item.image = news_relative
            item.save(update_fields=["image"])
            news_count += 1

        announcement_count = 0
        for item in Announcement.objects.filter(image__isnull=True):
            item.image = news_relative
            item.save(update_fields=["image"])
            announcement_count += 1
        for item in Announcement.objects.filter(image=""):
            item.image = news_relative
            item.save(update_fields=["image"])
            announcement_count += 1

        event_count = 0
        for item in Event.objects.filter(cover_image__isnull=True, image__isnull=True):
            item.cover_image = event_relative
            item.save(update_fields=["cover_image"])
            event_count += 1
        for item in Event.objects.filter(cover_image="", image=""):
            item.cover_image = event_relative
            item.save(update_fields=["cover_image"])
            event_count += 1

        return news_count, announcement_count, event_count

    def copy_default_asset(self, source: Path, destination: Path, relative_path: str):
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.exists() and not destination.exists():
            shutil.copy2(source, destination)
        return relative_path
