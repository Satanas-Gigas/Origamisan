import json
from tqdm import tqdm  # Не забудь pip install tqdm
from django.core.management.base import BaseCommand
from blog.models import Kanji
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Импортировать кандзи N1 из JSON, удаляя старые записи с level=1"

    def handle(self, *args, **kwargs):
        username = "adm"
        try:
            author = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stderr.write(f"❌ Пользователь '{username}' не найден!")
            return

        # 1. Удаляем старые записи
        deleted_count, _ = Kanji.objects.filter(level="1").delete()
        self.stdout.write(self.style.WARNING(f"Удалено {deleted_count} записей Kanji с level=1"))

        # 2. Загружаем новые данные
        with open("parse_kanji_n1_translated_ru.json", encoding="utf-8") as f:
            kanji_list = json.load(f)

        added = 0
        for entry in tqdm(kanji_list, desc="Импорт кандзи N1"):
            kanji_obj = Kanji(
                level="1",
                author=author,
                kanji=entry.get("kanji", ""),
                onyomi=entry.get("onyomi", ""),
                kunyomi=entry.get("kunyomi", ""),
                meaning_ru=entry.get("meaning_ru", ""),
                meaning_en=entry.get("meaning_en", "")
            )
            kanji_obj.save()
            added += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Импорт завершён! Добавлено {added} новых кандзи N1."))
