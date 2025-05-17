# -*- coding: utf-8 -*-
import csv

# Считываем английские значения
eng_meanings = {}
with open('kanji_n4_ENG.csv', 'r', encoding='utf-8') as eng_file:
    reader = csv.DictReader(eng_file, delimiter=';')
    for row in reader:
        kanji = row['kanji'].strip()
        meaning_en = row['meaning'].strip()
        eng_meanings[kanji] = meaning_en

# Объединяем с русским файлом
with open('kanji_n4_data.csv', 'r', encoding='utf-8') as ru_file, \
     open('kanji_n4_merged.csv', 'w', newline='', encoding='utf-8') as out_file:
    
    reader = csv.DictReader(ru_file, delimiter=';')
    fieldnames = ['kanji', 'onyomi', 'kunyomi', 'meaning_ru', 'meaning_en']
    writer = csv.DictWriter(out_file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

    for row in reader:
        kanji = row['kanji'].strip()
        meaning_en = eng_meanings.get(kanji, 'N/A')  # Подставляем "N/A" если нет значения
        writer.writerow({
            'kanji': kanji,
            'onyomi': row['onyomi'].strip(),
            'kunyomi': row['kunyomi'].strip(),
            'meaning_ru': row['meaning'].strip(),
            'meaning_en': meaning_en
        })

print("Файл 'kanji_n4_merged.csv' успешно создан.")