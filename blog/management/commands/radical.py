from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import json
import os

class Command(BaseCommand):
    help = "Парсит файл radical.txt и сохраняет пары кандзи-радикал в kanji_radicals.json"

    def handle(self, *args, **options):
        input_file = "radicals.txt"
        output_file = "kanji_radicals.json"

        if not os.path.exists(input_file):
            self.stdout.write(self.style.ERROR(f"Файл {input_file} не найден"))
            return

        with open(input_file, encoding="utf-8") as f:
            html = f.read()

        soup = BeautifulSoup(html, "html.parser")
        result = []

        for tr in soup.find_all("tr"):
            tds = tr.find_all("td")
            kanji = None
            rd = None
            note = ""
            # kanji — 2-й td (индекс 1), внутри <a>
            try:
                kanji_a = tds[1].find("a")
                kanji = kanji_a.text.strip() if kanji_a else None
                if not kanji:
                    note += "kanji not found; "
            except Exception:
                note += "kanji td missing; "
            # rd — 4-й td (индекс 3), внутри <a>
            try:
                rd_a = tds[3].find("a")
                rd = rd_a.text.strip() if rd_a else None
                if not rd:
                    note += "radical not found; "
            except Exception:
                note += "radical td missing; "
            entry = {"kanji": kanji or "", "rd": rd or ""}
            if note:
                entry["note"] = note.strip()
            result.append(entry)

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        self.stdout.write(self.style.SUCCESS(f"Готово! Спарсили {len(result)} записей, результат — {output_file}"))
