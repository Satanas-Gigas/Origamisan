import json
from django.core.management.base import BaseCommand
from blog.models import Word  # Замени на имя твоего приложения, если нужно

class Command(BaseCommand):
    help = "Экспортирует слова с уровнем 5 (kanji и kana) в JSON-файл"

    def handle(self, *args, **kwargs):
        words = Word.objects.filter(level='5').values('kanji', 'kana')
        word_list = list(words)

        with open('level5_words.json', 'w', encoding='utf-8') as f:
            json.dump(word_list, f, ensure_ascii=False, indent=5)

        self.stdout.write(self.style.SUCCESS(f"✅ Экспортировано {len(word_list)} слов в level5_words.json"))