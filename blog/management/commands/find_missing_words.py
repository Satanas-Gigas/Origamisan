import csv
from django.core.management.base import BaseCommand
from blog.models import Word
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Находит строки из CSV, которых нет в базе данных Word (level=3)'

    def handle(self, *args, **options):
        missing = []

        with open('words_with_ru_n3.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            rows = list(reader)

        self.stdout.write(f"🔍 Сравниваем {len(rows)} строк из CSV с базой данных...")

        for row in tqdm(rows, desc="🔄 Проверка записей"):
            kanji = row['Kanji'].strip()
            kana = row['Kana'].strip()
            romaji = row['Romaji'].strip()

            # Ищем по kanji и kana и уровню
            match = Word.objects.filter(
                kanji=kanji if kanji else None,
                kana=kana if kana else None,
                romaji=romaji if romaji else None,
                level="3"
            ).exists()

            if not match:
                missing.append(row)

        self.stdout.write(f"\n❌ Найдено отсутствующих слов: {len(missing)}\n")

        for row in missing:
            self.stdout.write(
                f"{row['Kanji']} | {row['Kana']} | {row['Romaji']} | {row['Translation']} | {row['Translation RU']}"
            )
