from django.core.management.base import BaseCommand
from blog.models import Word, PartOfSpeech
from django.contrib.auth import get_user_model
from tqdm import tqdm
import csv

class Command(BaseCommand):
    help = 'Импортирует данные из CSV и сохраняет слова и части речи'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        try:
            author = User.objects.get(username='adm')  # ← укажи своего пользователя
        except User.DoesNotExist:
            self.stderr.write("❌ Пользователь 'adm' не найден.")
            return

        with open('words_with_ru_n3.csv', newline='', encoding='utf-8') as csvfile:
            reader = list(csv.DictReader(csvfile, delimiter=';'))

            for row in tqdm(reader, desc="📦 Импорт слов"):
                kanji = row.get('Kanji', '').strip()
                kana = row.get('Kana', '').strip()
                romaji = row.get('Romaji', '').strip()
                translation = row.get('Translation', '').strip()
                translation_ru = row.get('Translation_ru', '').strip()
                part_of_speech_raw = row.get('Part of Speech', '').strip()

                # Ищем существующее слово
                existing_words = Word.objects.filter(
                    kanji=kanji,
                    kana=kana,
                    romaji=romaji
                )

                if existing_words.exists():
                    word = existing_words.first()
                    word.translate_en = translation
                    word.translate_ru = translation_ru
                    word.author = author
                    word.save()
                    created = False
                else:
                    word = Word.objects.create(
                        kanji=kanji,
                        kana=kana,
                        romaji=romaji,
                        translate_en=translation,
                        translate_ru=translation_ru,
                        author=author
                    )
                    created = True

                # Обработка частей речи
                if part_of_speech_raw:
                    parts = [p.strip() for p in part_of_speech_raw.split(',')]
                    word.part_of_speech.clear()
                    for part in parts:
                        if part:
                            pos, _ = PartOfSpeech.objects.get_or_create(code=part)
                            word.part_of_speech.add(pos)

        self.stdout.write(self.style.SUCCESS("✅ Импорт завершён."))
