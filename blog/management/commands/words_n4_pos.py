from django.core.management.base import BaseCommand
import json
import requests
import time
from tqdm import tqdm

class Command(BaseCommand):
    help = "Fetch part_of_speech for N4 words from Jisho API"

    def handle(self, *args, **options):
        def fetch_part_of_speech(kana_query):
            url = f"https://jisho.org/api/v1/search/words?keyword={kana_query}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    for entry in data.get('data', []):
                        readings = [j.get('reading') for j in entry.get('japanese', [])]
                        if kana_query in readings:
                            pos_list = []
                            for sense in entry.get('senses', []):
                                pos_list.extend(sense.get('parts_of_speech', []))
                            return list(set(pos_list))
            except Exception as e:
                print(f"⚠️ Ошибка при запросе для '{kana_query}': {e}")
            return []

        # Загружаем слова
        with open('words_level4.json', 'r', encoding='utf-8') as f:
            words = json.load(f)

        result = []

        # Прогресс-бар
        with tqdm(total=len(words), desc="🔍 Получение частей речи", ncols=100) as pbar:
            for word in words:
                orig_kanji = word.get('kanji')
                orig_kana = word.get('kana')

                if not orig_kana:
                    pbar.update(1)
                    continue

                # Убираем ～ и ・する
                query_kana = orig_kana.lstrip('～').replace('・する', '')
                query_kanji = orig_kanji.lstrip('～') if orig_kanji else None

                # Получаем part_of_speech
                part_of_speech = fetch_part_of_speech(query_kana)

                # Выводим в прогресс-бар info
                pbar.set_postfix({
                    'kana': query_kana,
                    'pos': ', '.join(part_of_speech)[:40] + ('...' if len(', '.join(part_of_speech)) > 40 else '')
                })

                # Добавляем в список
                result.append({
                    'kanji': query_kanji if orig_kanji is not None else None,
                    'kana': query_kana,
                    'part_of_speech': part_of_speech
                })

                pbar.update(1)
                time.sleep(1)

        # Сохраняем результат
        with open('words_level4_with_pos.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

        self.stdout.write(self.style.SUCCESS("✅ Обновлённый JSON сохранён в words_level4_with_pos.json"))
