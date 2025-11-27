import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.dateparse import parse_datetime
from django.utils import timezone

from accounts.models import CustomUser
from news.models import News, Announcement


class Command(BaseCommand):
    """
    Import data from a phpMyAdmin JSON export (ispp_db.json) into the current database.

    This **does not** change any database settings or schema – it only inserts/updates rows
    using the existing Django models, similar to how migrations affect data.

    Expected format is like the current ispp_db.json:
      [
        {"type": "header", ...},
        {"type": "database", "name": "..."},
        {"type": "table", "name": "accounts_customuser", "data": [ {...}, ... ]},
        {"type": "table", "name": "news_news", "data": [ {...}, ... ]},
        {"type": "table", "name": "news_announcement", "data": [ {...}, ... ]},
        ...
      ]

    Usage on server (from the directory that has manage.py):
        python manage.py import_ispp_json --path /absolute/path/to/ispp_db.json

    If --path is omitted, it looks for "ispp_db.json" next to manage.py.
    """

    help = "Import data from phpMyAdmin JSON export (ispp_db.json) into current DB (users + news + announcements)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            dest="path",
            default=None,
            help="Absolute path to ispp_db.json (default: BASE_DIR / 'ispp_db.json')",
        )

    def handle(self, *args, **options):
        json_path = options["path"] or os.path.join(settings.BASE_DIR, "ispp_db.json")

        if not os.path.isfile(json_path):
            self.stderr.write(self.style.ERROR(f"JSON file not found: {json_path}"))
            return

        self.stdout.write(self.style.WARNING(f"Loading data from: {json_path}"))

        with open(json_path, "r", encoding="utf-8") as f:
            raw = json.load(f)

        # Build a mapping: table_name -> list[rows]
        tables = {}
        for entry in raw:
            if entry.get("type") == "table":
                tables[entry["name"]] = entry.get("data", []) or []

        users_data = tables.get("accounts_customuser", [])
        news_data = tables.get("news_news", [])
        announcements_data = tables.get("news_announcement", [])

        with transaction.atomic():
            self._import_users(users_data)
            self._import_news(news_data)
            self._import_announcements(announcements_data)

        self.stdout.write(self.style.SUCCESS("Import from ispp_db.json finished successfully."))

    # ------------------------------
    # Helpers
    # ------------------------------

    def _parse_bool(self, value):
        if value is None:
            return False
        if isinstance(value, bool):
            return value
        return str(value).strip() in {"1", "true", "True", "YES", "yes"}

    def _parse_int(self, value, default=0):
        if value in (None, "", "null"):
            return default
        try:
            return int(value)
        except (TypeError, ValueError):
            return default

    def _parse_decimal_str(self, value, default="0.0"):
        if value in (None, "", "null"):
            return default
        return str(value)

    def _parse_dt(self, value):
        """
        Parse a datetime string from MySQL (e.g. '2025-11-06 07:25:33.876259').
        Returns a timezone-aware datetime or None.
        """
        if not value:
            return None
        s = str(value).strip()
        # django.utils.dateparse.parse_datetime expects ISO-like format; replace space with 'T'
        dt = parse_datetime(s.replace(" ", "T"))
        if dt is None:
            return None
        # If datetime is naive (no timezone), make it aware using the default timezone
        if timezone.is_naive(dt):
            dt = timezone.make_aware(dt, timezone.get_current_timezone())
        return dt

    def _import_users(self, rows):
        if not rows:
            self.stdout.write(self.style.WARNING("No rows found for accounts_customuser – skipping users."))
            return

        self.stdout.write(self.style.NOTICE(f"Importing {len(rows)} users into accounts.CustomUser ..."))

        for row in rows:
            user_id = self._parse_int(row.get("id"))
            if not user_id:
                continue

            # Map basic fields directly
            defaults = {
                "username": row.get("username") or "",
                "password": row.get("password") or "",
                "first_name": row.get("first_name") or "",
                "last_name": row.get("last_name") or "",
                "email": row.get("email") or "",
                "phone": row.get("phone") or "",
                "city": row.get("city") or "",
                "specialty": row.get("specialty") or "",
                "bio": row.get("bio") or "",
                "education": row.get("education") or "",
                "publications": row.get("publications") or "",
                "awards": row.get("awards") or "",
                "certifications": row.get("certifications") or "",
                "research_interests": row.get("research_interests") or "",
                "languages": row.get("languages") or "",
                "experience": self._parse_int(row.get("experience"), default=0),
                "rating": self._parse_decimal_str(row.get("rating"), default="0.0"),
                "is_superuser": self._parse_bool(row.get("is_superuser")),
                "is_staff": self._parse_bool(row.get("is_staff")),
                "is_active": self._parse_bool(row.get("is_active", True)),
            }

            # Optional: preserve joined / login dates if present
            date_joined = self._parse_dt(row.get("date_joined"))
            last_login = self._parse_dt(row.get("last_login"))
            created_at = self._parse_dt(row.get("created_at"))
            updated_at = self._parse_dt(row.get("updated_at"))
            if date_joined:
                defaults["date_joined"] = date_joined
            if last_login:
                defaults["last_login"] = last_login
            if created_at:
                defaults["created_at"] = created_at
            if updated_at:
                defaults["updated_at"] = updated_at

            # Profile image: in the dump it may be empty string or null
            profile_image = row.get("profile_image")
            if profile_image not in (None, "", "null"):
                defaults["profile_image"] = profile_image

            CustomUser.objects.update_or_create(
                id=user_id,
                defaults=defaults,
            )

        self.stdout.write(self.style.SUCCESS("Users imported/updated successfully."))

    def _import_news(self, rows):
        if not rows:
            self.stdout.write(self.style.WARNING("No rows found for news_news – skipping news."))
            return

        self.stdout.write(self.style.NOTICE(f"Importing {len(rows)} news items ..."))

        for row in rows:
            news_id = self._parse_int(row.get("id"))
            if not news_id:
                continue

            author_id = self._parse_int(row.get("author_id"))

            defaults = {
                "title": row.get("title") or "",
                "slug": row.get("slug") or "",
                "content": row.get("content") or "",
                "short_content": row.get("short_content") or "",
                "category": row.get("category") or "",
                "tags": row.get("tags") or "",
                "source": row.get("source") or "",
                "is_published": self._parse_bool(row.get("is_published", True)),
                "views": self._parse_int(row.get("views"), default=0),
            }

            created_at = self._parse_dt(row.get("created_at"))
            updated_at = self._parse_dt(row.get("updated_at"))
            if created_at:
                defaults["created_at"] = created_at
            if updated_at:
                defaults["updated_at"] = updated_at

            if author_id:
                # Set FK directly via *_id field
                defaults["author_id"] = author_id

            image = row.get("image")
            if image not in (None, "", "null"):
                defaults["image"] = image

            News.objects.update_or_create(
                id=news_id,
                defaults=defaults,
            )

        self.stdout.write(self.style.SUCCESS("News imported/updated successfully."))

    def _import_announcements(self, rows):
        if not rows:
            self.stdout.write(self.style.WARNING("No rows found for news_announcement – skipping announcements."))
            return

        self.stdout.write(self.style.NOTICE(f"Importing {len(rows)} announcements ..."))

        for row in rows:
            ann_id = self._parse_int(row.get("id"))
            if not ann_id:
                continue

            author_id = self._parse_int(row.get("author_id"))

            defaults = {
                "title": row.get("title") or "",
                "slug": row.get("slug") or "",
                "content": row.get("content") or "",
                "is_published": self._parse_bool(row.get("is_published", True)),
                "is_important": self._parse_bool(row.get("is_important", False)),
                "views": self._parse_int(row.get("views"), default=0),
            }

            created_at = self._parse_dt(row.get("created_at"))
            updated_at = self._parse_dt(row.get("updated_at"))
            if created_at:
                defaults["created_at"] = created_at
            if updated_at:
                defaults["updated_at"] = updated_at

            if author_id:
                defaults["author_id"] = author_id

            image = row.get("image")
            if image not in (None, "", "null"):
                defaults["image"] = image

            Announcement.objects.update_or_create(
                id=ann_id,
                defaults=defaults,
            )

        self.stdout.write(self.style.SUCCESS("Announcements imported/updated successfully."))


