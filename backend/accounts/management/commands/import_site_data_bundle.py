from pathlib import Path

from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.management import BaseCommand, call_command
from django.db import transaction
from django.utils import timezone

from add_board_members import BOARD_MEMBERS_DATA, create_username


User = get_user_model()


class Command(BaseCommand):
    help = "Import the latest prepared site data bundle: users, board members, news, announcements, and events."

    def add_arguments(self, parser):
        parser.add_argument(
            "--users-file",
            default=None,
            help="Path to ispp_db.json. Default: BASE_DIR/ispp_db.json",
        )
        parser.add_argument(
            "--content-file",
            default=None,
            help="Path to structured_content_complete.json. Default: mounted/import path if available.",
        )
        parser.add_argument(
            "--skip-board-members",
            action="store_true",
            help="Skip importing board members.",
        )
        parser.add_argument(
            "--author-username",
            default="system_import",
            help="Fallback staff username to create when no author user exists.",
        )

    def handle(self, *args, **options):
        base_dir = Path(settings.BASE_DIR)
        users_file = Path(options["users_file"]) if options["users_file"] else base_dir / "ispp_db.json"
        content_file = (
            Path(options["content_file"])
            if options["content_file"]
            else self._resolve_content_file(base_dir)
        )

        self.stdout.write(self.style.WARNING("Starting full site data import bundle..."))

        if users_file.exists():
            self.stdout.write(self.style.WARNING(f"Importing users/news/announcements from: {users_file}"))
            call_command("import_ispp_json", path=str(users_file))
        else:
            self.stdout.write(self.style.WARNING(f"Users source not found, skipping: {users_file}"))

        author = self._ensure_author_user(options["author_username"])
        self.stdout.write(self.style.SUCCESS(f"Using author user: {author.username} (ID: {author.id})"))

        if not options["skip_board_members"]:
            created_count, updated_count = self._import_board_members()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Board members import finished: {created_count} created, {updated_count} updated"
                )
            )

        if content_file and content_file.exists():
            self.stdout.write(self.style.WARNING(f"Importing news/events bundle from: {content_file}"))
            call_command(
                "import_content_from_json",
                file=str(content_file),
                author_id=author.id,
                update=True,
            )
        else:
            self.stdout.write(self.style.WARNING(f"Content source not found, skipping: {content_file}"))

        self.stdout.write(self.style.WARNING("Final record counts:"))
        call_command("inspect_database", format="count")
        self.stdout.write(self.style.SUCCESS("Full site data import bundle finished successfully."))

    def _resolve_content_file(self, base_dir: Path):
        candidates = [
            base_dir / "import_content" / "structured_content_complete.json",
            base_dir / "structured_content_complete.json",
            base_dir / "import_content" / "Content" / "structured_content_complete.json",
            base_dir.parent / "frontend" / "public" / "Content" / "structured_content_complete.json",
            Path("/opt/irpps/src/frontend/public/Content/structured_content_complete.json"),
        ]
        for candidate in candidates:
            if candidate.exists():
                return candidate
        return candidates[0]

    def _ensure_author_user(self, fallback_username: str):
        author = User.objects.filter(is_staff=True).order_by("id").first()
        if author:
            return author

        author = User.objects.filter(is_superuser=True).order_by("id").first()
        if author:
            return author

        author = User.objects.order_by("id").first()
        if author:
            if not author.is_staff:
                author.is_staff = True
                author.is_active = True
                if hasattr(author, "approval_status"):
                    author.approval_status = "approved"
                author.save(update_fields=["is_staff", "is_active", "approval_status"] if hasattr(author, "approval_status") else ["is_staff", "is_active"])
            return author

        author = User.objects.create(
            username=fallback_username,
            first_name="System",
            last_name="Importer",
            email="system-import@irpps.local",
            is_staff=True,
            is_superuser=True,
            is_active=True,
            approval_status="approved",
            approved_at=timezone.now(),
        )
        author.set_unusable_password()
        author.save()
        return author

    def _import_board_members(self):
        created_count = 0
        updated_count = 0

        with transaction.atomic():
            for members in BOARD_MEMBERS_DATA.values():
                for member_data in members:
                    username = create_username(member_data["persian_name"])
                    defaults = {
                        "first_name": member_data["persian_name"],
                        "last_name": member_data["english_name"],
                        "specialty": member_data["specialty"],
                        "bio": f'{member_data["position"]} - دوره {member_data["period"]}',
                        "is_active": True,
                        "approval_status": "approved",
                    }
                    user, created = User.objects.update_or_create(
                        username=username,
                        defaults=defaults,
                    )
                    if created:
                        user.set_unusable_password()
                        user.save(update_fields=["password"])
                        created_count += 1
                    else:
                        updated_count += 1

        return created_count, updated_count
