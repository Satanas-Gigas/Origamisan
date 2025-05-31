import json
import time
from tqdm import tqdm
from googletrans import Translator
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "📥 Перевод с английского на русский через Google Translate"

    def handle(self, *args, **options):
        INPUT_FILE = "words_n1.json"
        OUTPUT_FILE = "words_n1_translated_ru.json"

        translator = Translator()

        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        for word in tqdm(data, desc="🌍 Перевод"):
            en = word.get("translate_en", "").strip()
            if en and not word.get("translate_ru"):
                try:
                    ru = translator.translate(en, src="en", dest="ru").text
                    word["translate_ru"] = ru
                    time.sleep(0.5)  # чтобы не получить блокировку
                except Exception as e:
                    print(f"⚠️ Ошибка перевода '{en}': {e}")
                    word["translate_ru"] = ""

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        self.stdout.write(self.style.SUCCESS(f"✅ Перевод завершён. Сохранено в {OUTPUT_FILE}"))
