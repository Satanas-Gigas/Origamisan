from django.core.management.base import BaseCommand
from blog.models import Word, PartOfSpeech

class Command(BaseCommand):
    help = "Удаляет 'Wikipedia definition' из всех записей Word.part_of_speech"

    def handle(self, *args, **options):
        try:
            wiki_pos = PartOfSpeech.objects.get(code="Wikipedia definition")
        except PartOfSpeech.DoesNotExist:
            self.stdout.write(self.style.WARNING("❌ 'Wikipedia definition' не найдено в базе."))
            return

        # Найти все слова, у которых установлена эта часть речи
        words = Word.objects.filter(part_of_speech=wiki_pos)

        count = words.count()
        for word in words:
            word.part_of_speech.remove(wiki_pos)

        self.stdout.write(self.style.SUCCESS(f"✅ Удалено 'Wikipedia definition' из {count} слов."))

# import json
# from django.core.management.base import BaseCommand
# from blog.models import Word, PartOfSpeech
# from django.db.models import Q
# from tqdm import tqdm

# class Command(BaseCommand):
#     help = "🔄 Обновляет part_of_speech у Word из файла words_level5_with_pos_updated_last.json"

#     def handle(self, *args, **options):
#         INPUT_FILE = "words_level5_with_pos_updated_last.json"

#         try:
#             with open(INPUT_FILE, "r", encoding="utf-8") as f:
#                 data = json.load(f)
#         except Exception as e:
#             self.stderr.write(f"❌ Ошибка при чтении файла: {e}")
#             return

#         updated = 0
#         skipped = 0
#         not_found = []

#         for entry in tqdm(data, desc="🔁 Обновление базы"):
#             raw_kanji = entry.get("kanji")
#             kana = entry.get("kana")
#             pos_list = entry.get("part_of_speech", [])

#             if not kana or not pos_list:
#                 skipped += 1
#                 continue

#             # Обработка kanji
#             kanji = raw_kanji
#             if not kanji or kanji.strip() in ["''", ""]:
#                 kanji = None

#             # Поиск записи
#             filters = Q(kana=kana)
#             if kanji is None:
#                 filters &= (Q(kanji__isnull=True) | Q(kanji="") | Q(kanji="''"))
#             else:
#                 filters &= Q(kanji=kanji)

#             words = Word.objects.filter(filters, level="5")

#             if not words.exists():
#                 not_found.append(f"kana={kana}, kanji={raw_kanji}")
#                 skipped += 1
#                 continue

#             # Обработка part_of_speech
#             pos_objs = []
#             for pos in pos_list:
#                 obj, _ = PartOfSpeech.objects.get_or_create(code=pos.strip())
#                 pos_objs.append(obj)

#             # Обновление записей
#             for word in words:
#                 word.part_of_speech.set(pos_objs)
#                 updated += 1

#         self.stdout.write(f"\n✅ Обновлено слов: {updated}")
#         self.stdout.write(f"⏭️ Пропущено (не найдено или пустой POS): {skipped}")

#         if not_found:
#             self.stdout.write("\n📋 Не найденные слова:")
#             for item in not_found:
#                 self.stdout.write(f"⏭️ Не найдено: {item}")


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