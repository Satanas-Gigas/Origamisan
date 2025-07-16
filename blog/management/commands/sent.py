from django.core.management.base import BaseCommand
from blog.models import Word
import sys

class Command(BaseCommand):
    help = "Экспортирует kanji из Word (без пустых/невалидных) в файл kanji_words.txt с прогресс-баром"

    def handle(self, *args, **kwargs):
        words_qs = Word.objects.exclude(kanji__isnull=True).exclude(kanji__exact="").exclude(kanji="-").exclude(kanji="''")
        total = words_qs.count()
        if total == 0:
            self.stdout.write(self.style.WARNING("Нет подходящих слов для экспорта!"))
            return

        with open('kanji_words.txt', 'w', encoding='utf-8') as f:
            for i, word in enumerate(words_qs, 1):
                f.write(word.kanji.strip() + "\n")
                # Прогресс-бар (каждые 50 элементов или на последнем)
                if i % 50 == 0 or i == total:
                    progress = int(i / total * 50)
                    bar = '[' + '#' * progress + '-' * (50 - progress) + ']'
                    sys.stdout.write(f"\r{bar} {i}/{total}")
                    sys.stdout.flush()
            sys.stdout.write('\n')

        self.stdout.write(self.style.SUCCESS(f"Выгружено {total} kanji-слов в kanji_words.txt"))
