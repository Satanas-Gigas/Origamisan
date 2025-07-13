import json
import time
from tqdm import tqdm
from googletrans import Translator
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "📥 Перевод значений поля meaning_en в файле с кандзи (parse_kanji_n5.json) на русский через Google Translate с автоповтором и автосохранением"

    def handle(self, *args, **options):
        INPUT_FILE = "parse_kanji_n5.json"
        OUTPUT_FILE = "parse_kanji_n5_translated_ru.json"
        SAVE_EVERY = 50  # сохранять прогресс каждые 50 строк
        RETRIES = 5

        translator = Translator()
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        translated_count = 0
        skipped_count = 0

        for i, kanji in enumerate(tqdm(data, desc="🌍 Перевод")):
            en = kanji.get("meaning_en", "").strip()
            if en and not kanji.get("meaning_ru"):
                success = False
                for attempt in range(RETRIES):
                    try:
                        ru = translator.translate(en, src="en", dest="ru").text
                        kanji["meaning_ru"] = ru
                        translated_count += 1
                        time.sleep(0.7)
                        success = True
                        break  # успех
                    except Exception as e:
                        print(f"⚠️ Ошибка перевода '{en}' (попытка {attempt+1}): {e}")
                        time.sleep(7 + attempt * 7)  # задержка
                if not success:
                    kanji["meaning_ru"] = ""
                    skipped_count += 1
            else:
                skipped_count += 1

            if (i+1) % SAVE_EVERY == 0:
                with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                print(f"💾 Прогресс сохранён ({i+1} из {len(data)})")

        # Финальное сохранение
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        self.stdout.write(self.style.SUCCESS(f"✅ Перевод завершён. Сохранено в {OUTPUT_FILE}"))
        self.stdout.write(self.style.SUCCESS(f"🌟 Переведено: {translated_count}"))
        self.stdout.write(self.style.WARNING(f"⏭️ Пропущено: {skipped_count}"))
