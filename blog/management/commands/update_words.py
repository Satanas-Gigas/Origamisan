from django.core.management.base import BaseCommand
from blog.models import Word, PartOfSpeech

class Command(BaseCommand):
    help = 'Обновляет слова с пустыми частями речи и показывает их'

    def handle(self, *args, **options):
        empty_pos = PartOfSpeech.objects.filter(code='')
        words_with_empty_pos = Word.objects.filter(part_of_speech__in=empty_pos).distinct()

        for word in words_with_empty_pos:
            print(f"{word.kanji or word.kana} — уровень: {word.level}")


# from django.core.management.base import BaseCommand
# from django.conf import settings
# from blog.models import Word
# import os


# class Command(BaseCommand):
#     help = "Обновление переводов в базе данных"

#     def handle(self, *args, **kwargs):
#         # Указываем путь к файлу
#         file_path = os.path.join(settings.BASE_DIR, 'Noun.txt')
#         if not os.path.exists(file_path):
#             self.stdout.write(self.style.ERROR(f"Файл {file_path} не найден."))
#             return

#         # Открываем файл Noun.txt и обрабатываем его построчно
#         with open(file_path, 'r', encoding='utf-8') as file:
#             lines = file.readlines()

#         updated_count = 0
#         skipped_count = 0

#         for line in lines:
#             # Разделяем строку на слова по табуляции
#             words = line.strip().split('\t')

#             # # Проверяем, что строка имеет достаточно элементов
#             # if len(words) < 2:
#             #     self.stdout.write(f"Пропущена строка: {line.strip()} (недостаточно элементов)")
#             #     skipped_count += 1
#             #     continue

#             # Берём второй элемент как целевое слово
#             target_word = words[1]

#             # Ищем запись в базе данных
#             word_entry = Word.objects.filter(kana=target_word).first()

#             if word_entry:
#                 word_entry.part_of_speech = 'verb'
#                 word_entry.save()
#                 updated_count += 1
#                 self.stdout.write(self.style.SUCCESS(f"Обновлено: {line.strip()}"))
#             else:
#                 skipped_count += 1
#                 self.stdout.write(f"Пропущено: {line.strip()}")

#         # Выводим итоговую статистику
#         self.stdout.write(self.style.SUCCESS(f"Обновлено записей: {updated_count}"))
#         self.stdout.write(self.style.WARNING(f"Пропущено строк: {skipped_count}"))
