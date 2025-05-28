from django.core.management.base import BaseCommand
from blog.models import Word
import json
from tqdm import tqdm

class Command(BaseCommand):
    help = "Экспортирует слова из Word без part_of_speech в JSON-файл"

    def handle(self, *args, **options):
        words_without_pos = Word.objects.filter(part_of_speech__isnull=True, level="5").distinct()
        result = []

        for word in tqdm(words_without_pos, desc="📤 Экспорт без part_of_speech", ncols=100):
            result.append({
                "kanji": word.kanji,
                "kana": word.kana,
                "part_of_speech": []
            })

        with open("words_n5_missing_pos.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

        self.stdout.write(self.style.SUCCESS(f"✅ Экспортировано: {len(result)} записей в words_missing_pos.json"))