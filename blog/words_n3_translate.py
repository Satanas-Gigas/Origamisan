import csv
import time
from googletrans import Translator
from tqdm import tqdm

translator = Translator()

INPUT_FILE = 'word_n3_merged_with_kana_pos.csv'
OUTPUT_FILE = 'kanji_with_ru_n3.csv'

def clean(value):
    return "" if value.strip() in {"–", "-", "None", ""} else value.strip()

words_with_translations = []

with open(INPUT_FILE, 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    header = next(reader)
    header.append("Translation RU")  # Добавим новую колонку
    rows = list(reader)

for line_number, row in tqdm(enumerate(rows, start=2), total=len(rows), desc="🔁 Перевод"):
    if len(row) < 4:
        print(f"⚠️ Строка {line_number} неполная: {';'.join(row)}")
        continue

    # Очистка
    row = [clean(cell) for cell in row]

    # Распаковка
    try:
        kanji, kana, romaji, meaning_en, part_of_speech = row
    except ValueError:
        print(f"❌ Строка {line_number} не распаковывается корректно: {row}")
        continue

    try:
        meaning_ru = translator.translate(meaning_en, src='en', dest='ru').text
    except Exception as e:
        print(f"❌ Ошибка перевода строки {line_number}: {e}")
        meaning_ru = "Перевод недоступен"

    time.sleep(1)
    words_with_translations.append([kanji, kana, romaji, meaning_en, part_of_speech, meaning_ru])

# Сохраняем в CSV
with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(header)
    writer.writerows(words_with_translations)

print(f"\n✅ Переводы добавлены. Файл сохранён как: {OUTPUT_FILE}")