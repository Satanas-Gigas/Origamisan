import re
import json
import time
import requests
from tqdm import tqdm
from pykakasi import kakasi  # pip install pykakasi
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "📥 Обрабатывает wods_n2.txt и сохраняет romaji, part_of_speech и translate_en в words_n1.json"

    def handle(self, *args, **options):
        input_txt = "words_n1.txt"
        output_json = "words_n1.json"

        pattern = r'^(.+?)【(.+?)】\s+(.*)$'

        kakasi_inst = kakasi()
        kakasi_inst.setMode("H", "a")  # Hiragana to ascii
        kakasi_inst.setMode("K", "a")  # Katakana to ascii
        kakasi_inst.setMode("J", "a")  # Japanese to ascii
        kakasi_inst.setMode("r", "Hepburn")  # use Hepburn Romanization
        conv = kakasi_inst.getConverter()

        def to_romaji(kana):
            return conv.do(kana)

        def fetch_jisho(kanji, kana, retries=3):
            query = kanji if kanji else kana
            url = f"https://jisho.org/api/v1/search/words?keyword={query}"
            for attempt in range(retries):
                try:
                    response = requests.get(url, timeout=10)
                    if response.status_code == 200:
                        return response.json()
                except requests.exceptions.RequestException as e:
                    if attempt < retries - 1:
                        time.sleep(2 + attempt * 2)
                    else:
                        print(f"⚠️ Ошибка запроса для {kanji}/{kana}: {e}")
            return None

        try:
            with open(input_txt, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            self.stderr.write(f"❌ Не удалось прочитать файл {input_txt}: {e}")
            return

        results = []

        for line in tqdm(lines, desc="🔍 Обработка строк", ncols=100):
            match = re.match(pattern, line.strip())
            if not match:
                continue

            kanji = match.group(1).strip()
            kana = match.group(2).strip()
            translate_en = match.group(3).strip()
            romaji = to_romaji(kana)
            pos_list = []

            data = fetch_jisho(kanji, kana)
            if data:
                for item in data.get("data", []):
                    for j in item.get("japanese", []):
                        if j.get("reading") == kana:
                            for sense in item.get("senses", []):
                                pos_list.extend(sense.get("parts_of_speech", []))
                            break
                    if pos_list:
                        break

            results.append({
                "kanji": kanji,
                "kana": kana,
                "romaji": romaji,
                "translate_en": translate_en,
                "part_of_speech": list(set(pos_list))
            })

            time.sleep(1)

        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

        self.stdout.write(self.style.SUCCESS(f"✅ Завершено. Сохранено в {output_json}"))