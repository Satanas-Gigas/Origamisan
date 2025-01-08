import csv
import os
from django.core.management.base import BaseCommand
from blog.models import Word
from django.contrib.auth.models import User
from django.conf import settings


class Command(BaseCommand):
    help = "Обновление переводов в базе данных на основе CSV-файла"

    def handle(self, *args, **kwargs):
        # Путь к CSV-файлу
        file_path = os.path.join(settings.BASE_DIR, 'Vocab_N5.csv')

        # Проверяем наличие файла
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"Файл {file_path} не найден."))
            return

        # Открываем CSV-файл
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            next(csv_reader)  # Пропускаем первую строку с метаданными (#name и #description)

            updated_count = 0
            for row in csv_reader:
                # Проверяем, что строка содержит необходимые поля
                if len(row) < 3:
                    continue

                jp, jp_kana, ru = row

                # Пропускаем пустые строки
                if not jp and not jp_kana:
                    continue

                # Ищем запись в базе данных
                try:
                    grammar_entry = Word.objects.get(kanji=jp, kana=jp_kana)
                    grammar_entry.translate_ru = ru  # Обновляем перевод
                    grammar_entry.save()
                    updated_count += 1
                except Word.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Запись не найдена: JP={jp}, JP_KANA={jp_kana}"))

        self.stdout.write(self.style.SUCCESS(f"Обновлено {updated_count} записей в базе данных."))
