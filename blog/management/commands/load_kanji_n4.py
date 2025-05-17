import os
from django.core.management.base import BaseCommand
from blog.models import Kanji
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Load Kanji from kanji_n4_merged.csv into the Kanji model'

    def handle(self, *args, **kwargs):
        file_path = 'kanji_n4_merged.csv'  # Укажите путь к файлу

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"Файл {file_path} не найден."))
            return

        try:
            author = User.objects.get(username='adm')  # Замените на существующее имя пользователя
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("Пользователь с username='adm' не найден."))
            return

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        created_count = 0
        skipped_count = 0

        for line in lines[1:]:  # Пропускаем заголовок
            try:
                fields = line.strip().split(';')
                if len(fields) != 5:
                    self.stdout.write(self.style.WARNING(f"Неверное количество столбцов: {line.strip()}"))
                    skipped_count += 1
                    continue

                kanji, onyomi, kunyomi, meaning_ru, meaning_en = fields

                if Kanji.objects.filter(kanji=kanji).exists():
                    self.stdout.write(self.style.WARNING(f"Пропущен дубликат: {kanji}"))
                    skipped_count += 1
                    continue

                Kanji.objects.create(
                    kanji=kanji or None,
                    onyomi=onyomi or None,
                    kunyomi=kunyomi or None,
                    meaning_en=meaning_en or None,
                    meaning_ru=meaning_ru or None,
                    level="4",
                    author=author
                )
                created_count += 1
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Ошибка при обработке строки: {line.strip()} ({e})"))
                skipped_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"Успешно добавлено {created_count} записей. Пропущено {skipped_count} строк."))
