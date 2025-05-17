import os
import csv
import requests
import time

INPUT_FILE = "word_n3_merged.csv"
OUTPUT_FILE = "word_n3_merged_with_kana_pos.csv"

def get_kana_from_jisho(kanji):
    try:
        url = f"https://jisho.org/api/v1/search/words?keyword={kanji}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            json_data = response.json()
            if json_data["data"]:
                for entry in json_data["data"]:
                    for jp in entry.get("japanese", []):
                        if "reading" in jp:
                            return jp["reading"]
    except Exception as e:
        print(f"❌ Ошибка при получении kana для {kanji}: {e}")
    return ""

def get_part_of_speech(kanji):
    try:
        url = f"https://jisho.org/api/v1/search/words?keyword={kanji}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            json_data = response.json()
            if json_data["data"]:
                senses = json_data["data"][0].get("senses", [])
                if senses and "parts_of_speech" in senses[0]:
                    return ", ".join(senses[0]["parts_of_speech"])
    except Exception as e:
        print(f"⚠️ Ошибка получения части речи для '{kanji}': {e}")
    return ""

def process_file(input_file, output_file):
    with open(input_file, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        rows = list(reader)

    header = rows[0]
    data_rows = rows[1:]

    # Добавим заголовок части речи
    updated_rows = [["Kanji", "Kana", "Romaji", "Translation", "Part of Speech"]]

    for i, row in enumerate(data_rows, 1):
        if len(row) < 3:
            continue
        kanji = row[0].strip()
        kana = row[1].strip()
        romaji = row[2].strip()
        translation = ";".join(row[3:]).strip()

        if not kana:
            print(f"[{i}/{len(data_rows)}] 🔤 Получаем kana для: {kanji}")
            kana = get_kana_from_jisho(kanji)
            time.sleep(1)

        print(f"[{i}/{len(data_rows)}] 📚 Получаем часть речи для: {kanji}")
        part_of_speech = get_part_of_speech(kanji)
        time.sleep(1)

        updated_rows.append([kanji, kana, romaji, translation, part_of_speech])

    with open(output_file, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";", quoting=csv.QUOTE_NONE, escapechar="\\")
        writer.writerows(updated_rows)

    print(f"\n✅ Готово! Сохранено в файл: {output_file}")

if __name__ == "__main__":
    process_file(INPUT_FILE, OUTPUT_FILE)

    output_path = os.path.abspath(OUTPUT_FILE)
    print(f"📁 Абсолютный путь к файлу: {output_path}")

    if os.path.exists(output_path):
        print("📦 Файл успешно создан. Можно использовать дальше.")
    else:
        print("❌ Файл не найден. Что-то пошло не так.")