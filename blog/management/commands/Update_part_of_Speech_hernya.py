from django.core.management.base import BaseCommand
from blog.models import Word, PartOfSpeech
from django.db.models import Q
import json
from tqdm import tqdm

class Command(BaseCommand):
    help = "Обновляет part_of_speech в модели Word на основе файла words_level4_with_pos.json"

    def handle(self, *args, **kwargs):
        try:
            with open('words_level4_with_pos.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            self.stderr.write(f"❌ Ошибка при чтении JSON: {e}")
            return

        updated = 0
        skipped = 0

        for item in tqdm(data, desc="🔄 Обновление частей речи"):
            kanji = item.get('kanji')
            kana = item.get('kana')
            pos_list = item.get('part_of_speech', [])

            if not kana:
                skipped += 1
                continue

            # Найти Word по kana и kanji (kanji может быть None)
            words = Word.objects.filter(kana=kana)
            if kanji:
                words = words.filter(kanji=kanji)
            else:
                words = words.filter(kanji__isnull=True)

            if not words.exists():
                skipped += 1
                continue

            # Получить или создать объекты PartOfSpeech
            pos_objects = []
            for pos_code in pos_list:
                pos_obj, _ = PartOfSpeech.objects.get_or_create(code=pos_code.strip())
                pos_objects.append(pos_obj)

            # Обновить part_of_speech у найденных слов
            for word in words:
                word.part_of_speech.set(pos_objects)
                updated += 1

        self.stdout.write(f"\n✅ Обновлено слов: {updated}")
        self.stdout.write(f"⏭️ Пропущено (не найдено в БД): {skipped}")
