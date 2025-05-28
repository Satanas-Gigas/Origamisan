import json
from django.core.management.base import BaseCommand
from blog.models import Word, PartOfSpeech  # замени 'blog' на свою app, если она другая
from tqdm import tqdm

class Command(BaseCommand):
    help = "🔄 Обновляет part_of_speech у Word из файла words_level5_with_pos_updated_last.json"

    def handle(self, *args, **options):
        INPUT_FILE = "words_level5_with_pos_updated_last.json"

        try:
            with open(INPUT_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            self.stderr.write(f"❌ Ошибка при чтении файла: {e}")
            return

        updated = 0
        skipped = 0

        for entry in tqdm(data, desc="🔁 Обновление базы"):
            kanji = entry.get("kanji")
            kana = entry.get("kana")
            pos_list = entry.get("part_of_speech", [])

            if not kana or not pos_list:
                skipped += 1
                continue

            # Найти соответствующие записи в БД
            words = Word.objects.filter(kana=kana)
            if kanji in [None, "", "''"]:
                words = words.filter(kanji__isnull=True)
            else:
                words = words.filter(kanji=kanji)

            if not words.exists():
                skipped += 1
                continue

            # Получить или создать объекты PartOfSpeech
            pos_objs = []
            for pos in pos_list:
                obj, _ = PartOfSpeech.objects.get_or_create(code=pos.strip())
                pos_objs.append(obj)

            # Обновить каждую найденную запись
            for word in words:
                word.part_of_speech.set(pos_objs)
                updated += 1

        self.stdout.write(f"\n✅ Обновлено слов: {updated}")
        self.stdout.write(f"⏭️ Пропущено (нет совпадений или part_of_speech): {skipped}")



# import json
# import os
# from django.core.management.base import BaseCommand
# from blog.models import Grammar


# class Command(BaseCommand):
#     help = "Обновляет уровень записей Grammar с 5 на 4 по совпадающим заголовкам из файла"

#     def handle(self, *args, **kwargs):
#         file_path = 'grammar_n4.json'
#         if not os.path.exists(file_path):
#             self.stdout.write(self.style.ERROR(f"Файл {file_path} не найден."))
#             return

#         with open(file_path, 'r', encoding='utf-8') as f:
#             grammar_data = json.load(f)

#         titles = [item.get('title', '') for item in grammar_data]

#         # Обновляем записи
#         updated_count = Grammar.objects.filter(level="5", title__in=titles).update(level="4")
#         self.stdout.write(self.style.SUCCESS(f"Обновлено {updated_count} записей."))

# with open('grammar_n4.json', 'r', encoding='utf-8') as f:
#     grammar_data = json.load(f)

# titles = [item.get('title', '') for item in grammar_data]

# # Обновляем только те записи, чьи заголовки совпадают с импортированными
# Grammar.objects.filter(level="5", title__in=titles).update(level="4")