import json
from django.core.management.base import BaseCommand
from blog.models import Word, PartOfSpeech
from django.contrib.auth import get_user_model
from tqdm import tqdm

User = get_user_model()


class Command(BaseCommand):
    help = "📥 Импортирует N1 слова из JSON, форматирует translate_ru и записывает в базу данных."

    def handle(self, *args, **options):
        INPUT_FILE = "words_n1_translated_ru.json"

        try:
            with open(INPUT_FILE, "r", encoding="utf-8") as f:
                words = json.load(f)
        except Exception as e:
            self.stderr.write(f"❌ Ошибка при чтении файла: {e}")
            return

        try:
            author = User.objects.get(username='adm')  # Замените на существующее имя пользователя
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("Пользователь с username='adm' не найден."))
            return

        created, updated = 0, 0

        for item in tqdm(words, desc="📦 Импорт слов"):

            kanji = item.get("kanji")
            kana = item.get("kana")
            romaji = item.get("romaji")
            translate_en = item.get("translate_en")
            translate_ru = item.get("translate_ru")
            pos_list = item.get("part_of_speech", [])

            if not kana:
                continue

            # Обработка translate_ru: вставить пробел после ";" если нужно
            if translate_ru:
                parts = translate_ru.split(";")
                translate_ru = "; ".join(part.strip() for part in parts)

            word_obj, is_created = Word.objects.get_or_create(
                kanji=None if kanji in ["", "''", None] else kanji,
                kana=kana,
                defaults={
                    "romaji": romaji,
                    "translate_en": translate_en,
                    "translate_ru": translate_ru,
                    "author": author,
                    "level": "1",
                }
            )

            if not is_created:
                word_obj.romaji = romaji
                word_obj.translate_en = translate_en
                word_obj.translate_ru = translate_ru
                word_obj.author = author
                word_obj.level = "1"
                word_obj.save()
                updated += 1
            else:
                created += 1

            # Обработка PartOfSpeech
            pos_objects = []
            for pos in pos_list:
                pos_obj, _ = PartOfSpeech.objects.get_or_create(code=pos.strip())
                pos_objects.append(pos_obj)

            word_obj.part_of_speech.set(pos_objects)

        self.stdout.write(f"\n✅ Создано: {created}")
        self.stdout.write(f"🔁 Обновлено: {updated}")
        self.stdout.write(f"📚 Всего обработано: {len(words)}")
