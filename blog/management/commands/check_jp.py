import os
import json
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Проверяет примеры в jishyo_sentences.json, у которых нет поля 'jp'"

    def handle(self, *args, **options):
        # Получить абсолютный путь к файлу относительно manage.py
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        file_path = os.path.join(base_dir, 'jishyo_sentences.json')

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"Файл не найден: {file_path}"))
            return

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        errors = []
        for entry in data:
            kanji = entry.get("kanji")
            for idx, ex in enumerate(entry.get("examples", []), 1):
                if not ex.get("jp"):
                    errors.append(f"[ОШИБКА] Нет 'jp' для кандзи '{kanji}', пример #{idx}")

        if errors:
            self.stdout.write(self.style.ERROR("Найдены ошибки:"))
            for line in errors:
                self.stdout.write(line)
        else:
            self.stdout.write(self.style.SUCCESS("Все примеры содержат 'jp'!"))
