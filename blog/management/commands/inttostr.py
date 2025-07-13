import json
from django.core.management.base import BaseCommand
from blog.models import Kanji

class Command(BaseCommand):
    help = "Обновляет onyomi, kunyomi и meaning_en у Kanji из JSON-файла"

    def handle(self, *args, **options):
        n = "4"  # или подставь любой уровень
        json_path = f"parse_kanji_n{n}_translated_ru.json"

        # 1. Загружаем файл
        with open(json_path, encoding='utf-8') as f:
            data = json.load(f)
        data_dict = {item['kanji']: item for item in data}

        # 2. Ищем все Kanji с нужным level
        kanji_qs = Kanji.objects.filter(level=n)
        updated = 0
        skipped = 0

        for obj in kanji_qs:
            if obj.kanji in data_dict:
                obj.onyomi = data_dict[obj.kanji].get('onyomi', '')
                obj.kunyomi = data_dict[obj.kanji].get('kunyomi', '')
                obj.meaning_en = data_dict[obj.kanji].get('meaning_en', '')  # Вот это строка!
                obj.save()
                updated += 1
                self.stdout.write(self.style.SUCCESS(f"Обновлено: {obj.kanji}"))
            else:
                skipped += 1
                self.stdout.write(self.style.WARNING(f"Пропущено (нет в файле): {obj.kanji}"))

        self.stdout.write(self.style.SUCCESS(f"✅ Готово! Обновлено {updated}, пропущено {skipped}."))
