import json
import requests
import time
from tqdm import tqdm
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "🔄 Обновляет part_of_speech из файла words_n5_missing_pos.json с помощью Jisho API"

    def handle(self, *args, **options):
        INPUT_FILE = "words_n5_missing_pos.json"
        OUTPUT_FILE = "words_level5_with_pos_updated_last.json"

        def fetch_part_of_speech(query, reading):
            url = f"https://jisho.org/api/v1/search/words?keyword={query}"
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    for entry in data.get('data', []):
                        japanese = entry.get('japanese', [])
                        if any(j.get('reading') == reading for j in japanese):
                            pos = []
                            for sense in entry.get('senses', []):
                                pos.extend(sense.get('parts_of_speech', []))
                            return list(set(pos))
            except Exception as e:
                self.stderr.write(f"⚠️ Ошибка при запросе '{query}': {e}")
            return []

        def clean_text(value):
            if not value or not isinstance(value, str):
                return ""
            return value.strip().lstrip("〜").replace("・する", "")

        try:
            with open(INPUT_FILE, "r", encoding="utf-8") as f:
                words = json.load(f)
        except Exception as e:
            self.stderr.write(f"❌ Ошибка при чтении файла: {e}")
            return

        updated = 0
        for word in tqdm(words, desc="🔍 Обновление пропущенных частей речи", ncols=100):
            current_pos = word.get("part_of_speech", "")
            if current_pos and len(current_pos) > 0:
                continue

            kanji = word.get("kanji")
            kana = word.get("kana")

            if not kana:
                continue

            query = clean_text(kanji) if kanji and kanji != "''" else clean_text(kana)
            reading = clean_text(kana)

            pos = fetch_part_of_speech(query, reading)
            word["part_of_speech"] = pos
            updated += 1

            tqdm.write(f"✔️ {query}: {', '.join(pos) if pos else '—'}")
            time.sleep(1)

        try:
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                json.dump(words, f, ensure_ascii=False, indent=4)
        except Exception as e:
            self.stderr.write(f"❌ Ошибка при сохранении файла: {e}")
            return

        self.stdout.write(self.style.SUCCESS(f"\n✅ Обновлено записей: {updated}"))
        self.stdout.write(self.style.SUCCESS(f"💾 Сохранено в файл: {OUTPUT_FILE}"))