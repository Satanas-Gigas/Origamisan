from googletrans import Translator
import time
from tqdm import tqdm

# Инициализация переводчика
translator = Translator()

# Чтение существующего файла
words_with_translations = []

# Чтение всех строк файла в список
with open('kanji.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Прогресс-бар для обработки строк
for line_number, line in tqdm(enumerate(lines, start=1), total=len(lines), desc="Обработка строк"):
    # Убираем лишние пробелы и пропускаем пустые строки
    parts = line.strip().split('\t')
    if len(parts) < 4:
        print(f"Строка {line_number} имеет недостаточно данных: {line.strip()}")
        continue

    kanji = parts[0]
    onyomi = parts[1] if parts[1] != "–" else ""
    kunyomi = parts[2] if parts[2] != "–" else ""
    meaning_en = parts[3]

    # Перевод на русский
    try:
        meaning_ru = translator.translate(meaning_en, src='en', dest='ru').text
    except Exception as e:
        print(f"Ошибка перевода для слова '{meaning_en}': {e}")
        meaning_ru = "Перевод недоступен"

    # Задержка для избегания блокировки
    time.sleep(1)

    # Сохранение строки с новым переводом
    words_with_translations.append((kanji, onyomi, kunyomi, meaning_en, meaning_ru))

# Запись в новый файл
with open('kanji_with_ru.txt', 'w', encoding='utf-8') as file:
    for kanji, onyomi, kunyomi, meaning_en, meaning_ru in words_with_translations:
        file.write(f"{kanji}\t{onyomi}\t{kunyomi}\t{meaning_en}\t{meaning_ru}\n")

print("Файл с русскими переводами сохранён как kanji_with_ru.txt")
