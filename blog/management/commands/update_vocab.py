from blog.models import Word
from collections import defaultdict

# Словарь: (kanji, kana, level) → список id
seen = defaultdict(list)

for word in Word.objects.filter(level="3"):
    key = (word.kanji, word.kana, word.level)
    seen[key].append(word.id)

# Удаляем всё, кроме первого
for ids in seen.values():
    if len(ids) > 1:
        Word.objects.filter(id__in=ids[1:]).delete()

print("✅ Дубликаты удалены.")
# import csv
# from django.core.management.base import BaseCommand
# from blog.models import Word
# from tqdm import tqdm

# class Command(BaseCommand):
#     help = 'Обновляет поле translate_ru в модели Word из файла words_with_ru_n3.csv (только для level=3)'

#     def handle(self, *args, **kwargs):
#         updated = 0
#         not_found = 0
#         skipped = 0

#         try:
#             with open('words_with_ru_n3.csv', newline='', encoding='utf-8') as csvfile:
#                 reader = list(csv.DictReader(csvfile, delimiter=';'))
#                 total = len(reader)

#                 for row in tqdm(reader, total=total, desc="🔄 Обновление перевода"):
#                     kanji = row['Kanji'].strip()
#                     translation_ru = row['Translation RU'].strip()

#                     if not kanji or not translation_ru:
#                         skipped += 1
#                         continue

#                     # Только level=3
#                     words = Word.objects.filter(kanji=kanji, level="3")

#                     if words.exists():
#                         for word in words:
#                             if word.translate_ru != translation_ru:
#                                 word.translate_ru = translation_ru
#                                 word.save()
#                                 updated += 1
#                     else:
#                         not_found += 1

#         except FileNotFoundError:
#             self.stderr.write("❌ Файл words_with_ru_n3.csv не найден.")
#             return

#         self.stdout.write(self.style.SUCCESS("\n✅ Обновление завершено"))
#         self.stdout.write(f"📝 Обновлено переводов: {updated}")
#         self.stdout.write(f"❌ Не найдено слов с level=3: {not_found}")
#         self.stdout.write(f"⏭ Пропущено строк (пустые данные): {skipped}")
