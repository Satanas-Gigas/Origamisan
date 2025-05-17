with open('words_with_ru_n4.txt', 'r', encoding='utf-8') as f:
    word_lines = [line.rstrip('\n') for line in f if line.strip()]

# Чтение ромадзи
with open('words_romaji_n4.txt', 'r', encoding='utf-8') as f:
    romaji_lines = [line.strip() for line in f if line.strip()]

# Проверка совпадения количества строк
if len(word_lines) != len(romaji_lines):
    print(f"Количество строк не совпадает: {len(word_lines)} vs {len(romaji_lines)}")
else:
    combined_lines = []
    for word_line, romaji in zip(word_lines, romaji_lines):
        # Просто добавляем табуляцию и ромадзи в конец строки без изменения исходной табуляции
        combined_line = f"{word_line}\t{romaji}"
        combined_lines.append(combined_line)

    # Запись в новый файл
    with open('words_with_romaji_n4.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(combined_lines) + '\n')

    print("Файл успешно создан: words_with_romaji_n4.txt")