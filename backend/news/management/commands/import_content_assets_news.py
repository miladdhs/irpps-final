from pathlib import Path
from urllib.parse import quote
from xml.etree import ElementTree as ET
from zipfile import ZipFile
import shutil

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils.text import slugify

from news.models import News

User = get_user_model()


class Command(BaseCommand):
    help = "Import prepared content assets from frontend/public/Content as news items."

    def add_arguments(self, parser):
        parser.add_argument(
            "--content-dir",
            default=None,
            help="Path to the frontend/public/Content directory.",
        )
        parser.add_argument(
            "--author-id",
            type=int,
            default=None,
            help="Specific author id to assign to imported news.",
        )
        parser.add_argument(
            "--update",
            action="store_true",
            help="Update existing records matched by slug.",
        )

    def handle(self, *args, **options):
        content_dir = self._resolve_content_dir(options["content_dir"])
        author = self._resolve_author(options["author_id"])

        imported = 0
        updated = 0

        for item in self._build_news_items(content_dir):
            slug = item["slug"]
            news = News.objects.filter(slug=slug).first()

            if news and not options["update"]:
                self.stdout.write(self.style.WARNING(f"Skipping existing asset-based news: {slug}"))
                continue

            image_relative = self._copy_news_image(content_dir / item["image_file"]) if item.get("image_file") else None
            defaults = {
                "title": item["title"],
                "content": item["content"],
                "short_content": item["short_content"],
                "category": item["category"],
                "tags": item["tags"],
                "source": item["source"],
                "author": author,
                "is_published": True,
            }
            if image_relative:
                defaults["image"] = image_relative

            if news:
                for key, value in defaults.items():
                    setattr(news, key, value)
                news.save()
                updated += 1
                self.stdout.write(self.style.SUCCESS(f"Updated asset-based news: {news.title}"))
            else:
                News.objects.create(slug=slug, **defaults)
                imported += 1
                self.stdout.write(self.style.SUCCESS(f"Created asset-based news: {item['title']}"))

        self.stdout.write(self.style.SUCCESS(f"Asset-based news import finished: {imported} created, {updated} updated"))

    def _resolve_content_dir(self, custom_dir):
        if custom_dir:
            return Path(custom_dir)

        base_dir = Path(settings.BASE_DIR)
        candidates = [
            base_dir.parent / "frontend" / "public" / "Content",
            base_dir / "Content",
            Path("/opt/irpps/src/frontend/public/Content"),
        ]
        for candidate in candidates:
            if candidate.exists():
                return candidate
        return candidates[0]

    def _resolve_author(self, author_id):
        if author_id:
            author = User.objects.filter(id=author_id).first()
            if author:
                return author

        author = User.objects.filter(is_staff=True).order_by("id").first()
        if author:
            return author

        author = User.objects.filter(is_superuser=True).order_by("id").first()
        if author:
            return author

        author = User.objects.order_by("id").first()
        if author:
            return author

        raise RuntimeError("No user found to assign as author for asset-based news import.")

    def _copy_news_image(self, source: Path):
        if not source.exists():
            self.stdout.write(self.style.WARNING(f"News image not found: {source}"))
            return None

        target_dir = Path(settings.MEDIA_ROOT) / "news" / "imported"
        target_dir.mkdir(parents=True, exist_ok=True)
        target = target_dir / source.name
        shutil.copy2(source, target)
        return f"news/imported/{source.name}"

    def _extract_docx_text(self, file_path: Path):
        if not file_path.exists():
            return ""

        namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        with ZipFile(file_path) as docx_file:
            xml = docx_file.read("word/document.xml")

        root = ET.fromstring(xml)
        paragraphs = []
        for paragraph in root.findall(".//w:p", namespace):
            texts = [node.text or "" for node in paragraph.findall(".//w:t", namespace)]
            text = "".join(texts).strip()
            if text:
                paragraphs.append(text)

        return "\n".join(paragraphs)

    def _paragraphs_to_html(self, raw_text: str):
        parts = [part.strip() for part in raw_text.split("\n") if part.strip()]
        return "".join(f"<p>{part}</p>" for part in parts)

    def _build_news_items(self, content_dir: Path):
        evaluation_docx = content_dir / "New Microsoft Word Document.docx"
        evaluation_text = self._extract_docx_text(evaluation_docx)

        attachment_pdf = "ارزیابی .pdf"
        extra_image = "IMG_5400.jpeg"
        cover_image = "IMG_5403.jpeg"
        attachment_pdf_url = f"/Content/{quote(attachment_pdf)}"
        extra_image_url = f"/Content/{quote(extra_image)}"
        cover_image_url = f"/Content/{quote(cover_image)}"

        evaluation_html = self._paragraphs_to_html(evaluation_text)
        evaluation_html += (
            "<hr />"
            "<p><strong>فایل‌های مرتبط:</strong></p>"
            f'<p><a href="{attachment_pdf_url}" target="_blank" rel="noopener">مشاهده فایل ارزیابی (PDF)</a></p>'
            f'<p><a href="{cover_image_url}" target="_blank" rel="noopener">مشاهده تصویر ۱</a></p>'
            f'<p><a href="{extra_image_url}" target="_blank" rel="noopener">مشاهده تصویر ۲</a></p>'
        )

        return [
            {
                "title": "جلسه ارزیابی عملکرد و اعتباربخشی انجمن علمی ریه کودکان ایران",
                "slug": slugify("جلسه ارزیابی عملکرد و اعتباربخشی انجمن علمی ریه کودکان ایران", allow_unicode=True),
                "short_content": "گزارش نشست ارزیابی عملکرد و اعتباربخشی سال‌های ۱۴۰۲ و ۱۴۰۳ انجمن علمی ریه کودکان ایران به همراه فایل‌ها و تصاویر مرتبط.",
                "content": evaluation_html,
                "category": "اخبار انجمن",
                "tags": "ارزیابی, اعتباربخشی, انجمن, ریه کودکان",
                "source": attachment_pdf_url,
                "image_file": cover_image,
            },
        ]
