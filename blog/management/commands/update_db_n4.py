import json
import os
from django.core.management.base import BaseCommand
from blog.models import Grammar


class Command(BaseCommand):
    help = "Обновляет уровень записей Grammar с 5 на 4 по совпадающим заголовкам из файла"

    def handle(self, *args, **kwargs):
        file_path = 'grammar_n4.json'
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"Файл {file_path} не найден."))
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            grammar_data = json.load(f)

        titles = [item.get('title', '') for item in grammar_data]

        # Обновляем записи
        updated_count = Grammar.objects.filter(level="5", title__in=titles).update(level="4")
        self.stdout.write(self.style.SUCCESS(f"Обновлено {updated_count} записей."))

with open('grammar_n4.json', 'r', encoding='utf-8') as f:
    grammar_data = json.load(f)

titles = [item.get('title', '') for item in grammar_data]

# Обновляем только те записи, чьи заголовки совпадают с импортированными
Grammar.objects.filter(level="5", title__in=titles).update(level="4")