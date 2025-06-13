from django.core.management.base import BaseCommand
import json


class Command(BaseCommand):
    help = "📄 Преобразует kanji_n3.txt в kanji_n3.json"

    def handle(self, *args, **options):
        INPUT_FILE = "kanji_n3.txt"
        OUTPUT_FILE = "kanji_n3.json"

        kanji_list = []

        try:
            with open(INPUT_FILE, "r", encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            self.stderr.write(f"❌ Файл '{INPUT_FILE}' не найден.")
            return

        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue

            if '\t' not in line:
                self.stderr.write(f"⚠️ Пропущена строка {i}: нет табуляции -> '{line}'")
                i += 1
                continue

            try:
                kanji, meaning_ru = line.split('\t', 1)
                onyomi = lines[i + 1].strip()
                kunyomi = lines[i + 2].strip()
                # Пропускаем следующие строки (проценты и прочее)
                i += 6
            except Exception as e:
                self.stderr.write(f"⚠️ Ошибка на строке {i}: {e}")
                i += 1
                continue

            kanji_entry = {
                "kanji": kanji,
                "onyomi": onyomi,
                "kunyomi": kunyomi,
                "meaning_ru": meaning_ru,
                "meaning_en": ""
            }

            kanji_list.append(kanji_entry)

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(kanji_list, f, ensure_ascii=False, indent=4)

        self.stdout.write(f"\n✅ Готово! Сохранено в {OUTPUT_FILE}")
        self.stdout.write(f"📊 Всего успешно обработано: {len(kanji_list)} записей")
