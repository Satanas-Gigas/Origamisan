import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from blog.models import Grammar
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Импорт данных из JSON файла в модель Grammar"

    def handle(self, *args, **kwargs):
        # Путь к JSON-файлу
        file_path = os.path.join(settings.BASE_DIR, 'grammar_n4.json')

        # Проверьте, существует ли файл
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"Файл {file_path} не найден."))
            return

        # Загрузите JSON данные
        with open(file_path, 'r', encoding='utf-8') as file:
            grammar_data = json.load(file)

        # Получаем пользователя-автора
        try:
            author = User.objects.get(username='adm')  # Замените 'adm' на имя существующего пользователя
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("Пользователь с username='adm' не найден."))
            return

        # Создаём объекты Grammar
        for item in grammar_data:
            Grammar.objects.create(
                level="4",
                author=author,
                title=item.get('title', ''),
                formula_ru=item.get('formula_ru', ''),
                formula_en=item.get('formula_en', ''),
                explain_ru=item.get('explain_ru', ''),
                explain_en=item.get('explain_en', ''),
                example_jp_kanji=item.get('example_jp_kanji', ''),
                example_jp_kana=item.get('example_jp_kana', ''),
                example_ru=item.get('example_ru', ''),
                example_en=item.get('example_en', ''),
            )
        print("Импорт данных завершён успешно.")