import re
import csv
from pathlib import Path

# Пути к файлам
file_1_path = Path("word_n3_no_romaji.txt")
file_2_path = Path("word_n3_work.txt")
output_csv_path = Path("word_n3_merged.csv")

# Чтение второго файла и создание словаря: Кандзи -> Кана (из 【】)
kanji_reading_dict = {}
with open(file_2_path, encoding="utf-8") as f2:
    for line in f2:
        match = re.match(r"(?P<kanji>\S+?)【(?P<reading>.+?)】", line.strip())
        if match:
            kanji = match.group("kanji")
            reading = match.group("reading")
            kanji_reading_dict[kanji] = reading

# Чтение первого файла и формирование строк для CSV
output_rows = []
with open(file_1_path, encoding="utf-8") as f1:
    for line in f1:
        line = line.strip()
        # Проверяем, начинается ли строка с кандзи (китайского символа)
        if not re.match(r'^[\u4e00-\u9fff]', line):
            continue

        match = re.match(r"(?P<kanji>.+?) \((?P<romaji>.+?)\): (?P<translation>.+)", line)
        if match:
            kanji = match.group("kanji").strip()
            romaji = match.group("romaji").strip()
            translation = match.group("translation").strip()
            kana = kanji_reading_dict.get(kanji, "")
            output_rows.append([kanji, kana, romaji, translation])

# Запись в CSV без кавычек вокруг строк, разделитель - ;
with open(output_csv_path, mode="w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";", quoting=csv.QUOTE_NONE, escapechar="\\")
    writer.writerow(["Kanji", "Kana", "Romaji", "Translation"])
    writer.writerows(output_rows)

output_csv_path.name