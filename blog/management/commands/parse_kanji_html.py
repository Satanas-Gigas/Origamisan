import os
import json
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Парсит parse_kanji_n2.txt в корне проекта и сохраняет в parse_kanji_n2.json'

    def handle(self, *args, **options):
        # Файл должен быть в корне проекта
        input_filename = 'parse_kanji_n2.txt'
        output_filename = 'parse_kanji_n2.json'
        input_path = os.path.join(os.getcwd(), input_filename)
        output_path = os.path.join(os.getcwd(), output_filename)

        if not os.path.exists(input_path):
            self.stdout.write(self.style.ERROR(f"Файл {input_filename} не найден в корне проекта!"))
            return

        with open(input_path, "r", encoding="utf-8") as f:
            html = f.read()

        soup = BeautifulSoup(html, "html.parser")
        result = []

        for row in soup.find_all('tr', class_='charRow'):
            kanji = row['data-char']
            tds = row.find_all('td')

            meaning_ru = tds[1].get_text(strip=True)

            # Ониёми
            onyomi_div = tds[2].find('div', class_='readingElem')
            onyomi = ''.join(onyomi_div.stripped_strings) if onyomi_div else ''

            # Куниёми (до okurigana)
            kunyomi_div = tds[3].find('div', class_='readingElem')
            kunyomi = ''
            if kunyomi_div:
                for el in kunyomi_div.contents:
                    if getattr(el, 'name', None) == 'span' and 'okurigana' in el.get('class', []):
                        break
                    if isinstance(el, str):
                        kunyomi += el
                    elif hasattr(el, 'get_text'):
                        kunyomi += el.get_text(strip=True)

            obj = {
                "kanji": kanji,
                "onyomi": onyomi,
                "kunyomi": kunyomi,
                "meaning_ru": meaning_ru,
                "meaning_en": ""
            }
            result.append(obj)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        self.stdout.write(self.style.SUCCESS(f"Успешно! Записано {len(result)} элементов в {output_filename}"))
