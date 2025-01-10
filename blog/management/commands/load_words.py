import os
from django.core.management.base import BaseCommand
from blog.models import Kanji
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Load Kanji from kanji_n5.txt into the Word model'

    def handle(self, *args, **kwargs):
        file_path = 'kanji_n5.txt'  # Укажите путь к файлу

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
                # Разделение строки на поля
                fields = line.strip().split('\t')

                # Дополняем недостающие поля пустыми строками
                while len(fields) < 4:
                    fields.append('')

                kanji, onyomi, kunyomi, meaning_en = fields

                Kanji.objects.create(
                    kanji=kanji or None,  # Если kanji отсутствует, сохраняем как None
                    onyomi=onyomi or None,
                    kunyomi=kunyomi or None,
                    meaning_en=meaning_en or None,
                    level="5",  # Уровень по умолчанию
                    author=author  # Указываем автора
                )
                created_count += 1
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Ошибка при обработке строки: {line.strip()} ({e})"))
                skipped_count += 1

        # Итоговый результат
        self.stdout.write(self.style.SUCCESS(f"Успешно добавлено {created_count} записей. Пропущено {skipped_count} строк."))