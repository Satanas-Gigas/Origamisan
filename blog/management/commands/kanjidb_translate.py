import json
import time
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from googletrans import Translator
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "🇷🇺 Перевод кандзи сначала через kanjidb.ru, если не найден — через Google Translate"

    def handle(self, *args, **kwargs):
        INPUT_FILE = "parse_kanji_n4.json"
        OUTPUT_FILE = "parse_kanji_n4_translated_ru.json"
        SAVE_EVERY = 20
        RETRIES = 5

        translator = Translator()

        # Получаем карту kanji → kanji_id с kanjidb.ru
        url = 'https://kanjidb.ru/?p=bushu_rating'
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'html.parser')
        kanji_id_map = {}
        for a in soup.select('.kanji_small a'):
            href = a.get('href', '')
            if '?p=kanji_show' in href and 'kanji_id=' in href:
                kanji = a.text.strip()
                kanji_id = href.split('kanji_id=')[1].split('&')[0]
                kanji_id_map[kanji] = kanji_id

        # Загружаем твой json
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        translated_count = 0
        skipped_count = 0

        def get_kanji_ru_by_id(kanji_id):
            url = f'https://kanjidb.ru/?p=kanji_show&kanji_id={kanji_id}'
            try:
                resp = requests.get(url, timeout=60)
                resp.encoding = 'utf-8'
                soup = BeautifulSoup(resp.text, 'html.parser')
                font = soup.find('font', {'color': '#008080'})
                if font:
                    return font.get_text(strip=True)
            except Exception as e:
                print(f"⚠️ Ошибка запроса {url}: {e}")
            return ""

        for i, kanji_obj in enumerate(tqdm(data, desc="🇷🇺 Перевод с kanjidb.ru/Google")):
            kanji = kanji_obj["kanji"]
            if not kanji_obj.get("meaning_ru"):
                kanji_id = kanji_id_map.get(kanji)
                print(f"\n[{i+1}/{len(data)}] Кандзи: {kanji} → kanji_id: {kanji_id if kanji_id else '❌ не найден'}")
                ru = ""
                # 1. Пробуем взять с сайта
                if kanji_id:
                    ru = get_kanji_ru_by_id(kanji_id)
                    if ru:
                        print(f"  Перевод с kanjidb.ru: '{ru}'")
                        kanji_obj["meaning_ru"] = ru
                        translated_count += 1
                        print(f"  ✅ Добавлен: {ru}")
                    else:
                        print("  ⏭️ Перевод НЕ найден на странице!")
                else:
                    print("  ⏭️ kanji_id НЕ найден!")

                # 2. Если не нашли — пробуем через Google Translate
                if not ru:
                    en = kanji_obj.get("meaning_en", "").strip()
                    if en:
                        print(f"  Перевод через Google Translate: '{en}'")
                        success = False
                        for attempt in range(RETRIES):
                            try:
                                ru = translator.translate(en, src="en", dest="ru").text
                                kanji_obj["meaning_ru"] = ru
                                translated_count += 1
                                print(f"  ✅ Добавлен через Google Translate: {ru}")
                                time.sleep(0.7)
                                success = True
                                break
                            except Exception as e:
                                print(f"⚠️ Ошибка перевода '{en}' (попытка {attempt+1}): {e}")
                                time.sleep(7 + attempt * 7)
                        if not success:
                            kanji_obj["meaning_ru"] = ""
                            skipped_count += 1
                            print("  ⏭️ Перевод через Google Translate не удался!")
                    else:
                        skipped_count += 1
                        print("  ⏭️ Нет значения meaning_en для Google Translate!")
            else:
                skipped_count += 1
                print(f"[{i+1}/{len(data)}] Кандзи: {kanji} — перевод уже есть, пропущено.")

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

