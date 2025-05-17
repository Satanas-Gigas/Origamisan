import os
from django.core.management.base import BaseCommand
from blog.models import Word
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Load words from kwords_with_romaji_n4.tx into the Word model'

    def handle(self, *args, **kwargs):
        file_path = 'words_with_romaji_n4.txt'  # Укажите путь к файлу

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"Файл {file_path} не найден."))
            return

        # Получаем пользователя-автора
        try:
            author = User.objects.get(username='adm')  # Замените 'adm' на имя существующего пользователя
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("Пользователь с username='adm' не найден."))
            return

        # Чтение строк из файла
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        created_count = 0
        skipped_count = 0

        # Обработка каждой строки
        for line in lines:
            try:
                # Не удаляем табуляции — только перевод строки
                fields = line.rstrip('\n').split('\t')

                # Заполняем недостающие поля пустыми значениями
                while len(fields) < 6:
                    fields.append('')

                # Обрезаем лишние поля (на всякий случай)
                fields = fields[:6]

                kanji, kana, part_of_speech, translate_en, translate_ru, romaji = fields

                Word.objects.create(
                    kanji=kanji or None,
                    kana=kana or None,
                    romaji=romaji or None,
                    part_of_speech=part_of_speech or None,
                    translate_en=translate_en or None,
                    translate_ru=translate_ru or None,
                    level="4",
                    author=author
                )
                created_count += 1

            except Exception as e:
                self.stdout.write(self.style.WARNING(
                    f"Ошибка при обработке строки: {line.strip()} ({e})"
                ))
                skipped_count += 1