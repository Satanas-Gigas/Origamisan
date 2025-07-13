import os
import json
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Парсит parse_kanji_n5.txt в корне проекта и сохраняет в parse_kanji_n5.json'

    def handle(self, *args, **options):
        input_filename = 'parse_kanji_n5.txt'
        output_filename = 'parse_kanji_n5.json'
        input_path = os.path.join(os.getcwd(), input_filename)
        output_path = os.path.join(os.getcwd(), output_filename)

        if not os.path.exists(input_path):
            self.stdout.write(self.style.ERROR(f"Файл {input_filename} не найден в корне проекта!"))
            return

        with open(input_path, "r", encoding="utf-8") as f:
            html = f.read()

        soup = BeautifulSoup(html, "html.parser")
        result = []

        for row in soup.find_all('tr', class_='jl-row'):
            tds = row.find_all('td')
            if len(tds) < 5:
                continue  # safety

            # kanji: <td class="jl-td-k ..."> → <a>текст
            kanji_td = tds[1]
            kanji_a = kanji_td.find('a')
            kanji = kanji_a.get_text(strip=True) if kanji_a else ''

            # onyomi: <td class="jl-td-on ..."> → <p>японский
            onyomi_td = tds[2]
            onyomi_p = onyomi_td.find('p')
            onyomi = onyomi_p.get_text(strip=True) if onyomi_p else ''

            # kunyomi: <td class="jl-td-kun ..."> → <p>японский
            kunyomi_td = tds[3]
            kunyomi_p = kunyomi_td.find('p')
            kunyomi = kunyomi_p.get_text(strip=True) if kunyomi_p else ''

            # meaning_en: <td class="jl-td-m ..."> → просто текст
            meaning_en = tds[4].get_text(strip=True)

            obj = {
                "kanji": kanji,
                "onyomi": onyomi,
                "kunyomi": kunyomi,
                "meaning_ru": "",
                "meaning_en": meaning_en
            }
            result.append(obj)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        self.stdout.write(self.style.SUCCESS(f"Успешно! Записано {len(result)} элементов в {output_filename}"))