from googletrans import Translator
import time
from tqdm import tqdm

# Инициализация переводчика
translator = Translator()

# Чтение существующего файла
words_with_translations = []

# Чтение всех строк файла в список для использования с tqdm
with open('words.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Инициализация прогресс-бара
for line_number, line in tqdm(enumerate(lines, start=1), total=len(lines), desc="Обработка строк"):
    # Убираем лишние пробелы и пропускаем пустые строки
    parts = line.strip().split('\t')

    # Если строка содержит 3 элемента (без kanji)
    if len(parts) == 3:
        kana = parts[0]
        romaji = parts[1]
        translate_en = parts[2]
        kanji = ''  # Устанавливаем kanji как пустое значение, так как оно отсутствует

    # Если строка содержит 4 элемента (с kanji)
    elif len(parts) == 4:
        kanji = parts[0]
        kana = parts[1]
        romaji = parts[2]
        translate_en = parts[3]

    # Если строка не содержит 3 или 4 элемента, пропускаем её
    else:
        print(f"Строка {line_number} имеет недостаточно данных: {line.strip()}")
        continue

    # Слово для перевода: либо kanji, либо kana (если kanji пустое)
    word_to_translate = kanji if kanji else kana
    
    # Перевод на русский
    try:
        translate_ru = translator.translate(word_to_translate, src='ja', dest='ru').text
    except Exception as e:
        print(f"Ошибка перевода для слова {word_to_translate}: {e}")
        translate_ru = "Перевод недоступен"
    
    # Добавляем задержку, чтобы избежать тайм-аутов
    time.sleep(1)

    # Сохранение строки с новым переводом
    words_with_translations.append((kanji, kana, romaji, translate_en, translate_ru))

# Запись в новый файл
with open('words_with_ru.txt', 'w', encoding='utf-8') as file:
    for kanji, kana, romaji, translate_en, translate_ru in words_with_translations:
        # Если kanji пустое, записываем пустые кавычки
        if kanji != kana:
            file.write(f"{kanji}\t{kana}\t{romaji}\t{translate_en}\t{translate_ru}\n")
        else:
            file.write(f"''\t{kana}\t{romaji}\t{translate_en}\t{translate_ru}\n")

print("Файл с русскими переводами сохранён как words_with_ru.txt")