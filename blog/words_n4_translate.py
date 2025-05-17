from googletrans import Translator
import time
from tqdm import tqdm

translator = Translator()

def clean(value):
    """Очищает значение от лишнего и заменяет '–', '-', 'None' и пустое на '' """
    return "" if value.strip() in {"–", "-", "None", ""} else value.strip()

words_with_translations = []

with open('word_n3_merged_with_kana_pos.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

for line_number, line in tqdm(enumerate(lines, start=1), total=len(lines), desc="Обработка строк"):
    parts = line.strip().split(';')

    if len(parts) < 3:
        print(f"Строка {line_number} имеет недостаточно данных: {line.strip()}")
        continue

    # Очистка всех элементов
    parts = [clean(part) for part in parts]

    # Распаковка с безопасной длиной
    kanji, kana, romaji, meaning_en, part_of_speech = "", "", "", ""
    if len(parts) == 5:
        kanji, kana, romaji, meaning_en, part_of_speech = parts
    elif len(parts) == 4:
        kana, romaji, meaning_en, part_of_speech = parts  # когда нет кандзи

    # Если поле kanji пустое, а kana содержит кандзи — меняем местами
    if not kanji and any('\u4e00' <= ch <= '\u9faf' for ch in kana):
        kanji, kana = kana, ""

    # Перевод
    try:
        meaning_ru = translator.translate(meaning_en, src='en', dest='ru').text
    except Exception as e:
        print(f"Ошибка перевода на строке {line_number}: {e}")
        meaning_ru = "Перевод недоступен"

    time.sleep(1)

    words_with_translations.append((kanji, kana, romaji, meaning_en, part_of_speech , meaning_ru))

# Сохраняем в файл
with open('kanji_with_ru_n3.csv', 'w', encoding='utf-8') as file:
    for kanji, kana, romaji, meaning_en, part_of_speech , meaning_ru in words_with_translations:
        file.write(f"{kanji}\t{kana}\t{romaji}\t{part_of_speech}\t{meaning_en}\t{meaning_ru}\n")

print("✅ Файл с русскими переводами сохранён как kanji_with_ru_n3.csv")