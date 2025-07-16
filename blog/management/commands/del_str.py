import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
import time
import os

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Парсит переводы кандзи с japanese-words.org/ru/kanji для списка иероглифов'

    def add_arguments(self, parser):
        parser.add_argument('--input', type=str, default='skip_kanji.txt', help='Файл со списком иероглифов')
        parser.add_argument('--output', type=str, default='kanji_skip_kanji.json', help='Файл для результата')
        parser.add_argument('--resume', action='store_true', help='Продолжить с места остановки')

    def handle(self, *args, **options):
        input_file = options['input']
        output_file = options['output']
        resume = options['resume']

        if not os.path.exists(input_file):
            self.stderr.write(self.style.ERROR(f"Файл {input_file} не найден"))
            return

        with open(input_file, encoding='utf-8') as f:
            kanji_list = [line.strip() for line in f if line.strip()]

        # Режим докачки, если уже есть результат
        results = {}
        if resume and os.path.exists(output_file):
            with open(output_file, encoding='utf-8') as f:
                results = {item['kanji']: item for item in json.load(f)}
        else:
            results = {}

        # Только те, которых нет в рез-те
        kanji_to_parse = [k for k in kanji_list if k not in results]

        url = 'https://japanese-words.org/ru/kanji'
        session = requests.Session()

        for kanji in tqdm(kanji_to_parse, desc="Парсим переводы кандзи"):
            entry = {"kanji": kanji}

            try:
                r = session.post(url, data={'text': kanji}, timeout=60)
                soup = BeautifulSoup(r.text, 'html.parser')
                row = soup.select_one('table tbody tr')

                if row:
                    tds = row.find_all('td')
                    entry['jlpt'] = tds[0].get_text(strip=True)
                    entry['kanji'] = tds[1].get_text(strip=True)
                    entry['onyomi'] = tds[2].get_text(strip=True)
                    entry['kunyomi'] = tds[3].get_text(strip=True)
                    entry['translate_ru'] = tds[4].get_text(strip=True)
                else:
                    entry['note'] = 'Кандзи не найден на сайте'

            except Exception as e:
                entry['note'] = f'Ошибка: {str(e)}'

            results[kanji] = entry

            # Автосейв каждые 5 запросов
            if len(results) % 5 == 0:
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(list(results.values()), f, ensure_ascii=False, indent=2)

            time.sleep(2.0)

        # Финальный сейв
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(list(results.values()), f, ensure_ascii=False, indent=2)

        self.stdout.write(self.style.SUCCESS(f'Завершено! Найдено: {len(results)} кандзи.'))
