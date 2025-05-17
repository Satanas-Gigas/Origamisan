with open("in_stroke.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Убираем пустые строки и пробелы
cleaned = [line.strip() for line in lines if line.strip()]

with open("word_n3_no_romaji.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(cleaned))