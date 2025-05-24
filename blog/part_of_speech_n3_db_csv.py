import csv
from blog.models import Word, PartOfSpeech
from django.contrib.auth.models import User

with open('words_with_ru_n3.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    author = User.objects.get(username='your_admin_username')  # замените на реального пользователя

    for row in reader:
        word = Word.objects.create(
            level="3",
            author=author,
            kanji=row['Kanji'],
            kana=row['Kana'],
            romaji=row['Romaji'],
            translate_en=row['Translation'],
            translate_ru=row.get('Russian Translation', ''),
        )

        parts = [p.strip() for p in row['Part of Speech'].split(',')]
        for part in parts:
            pos_obj, _ = PartOfSpeech.objects.get_or_create(code=part)
            word.part_of_speech.add(pos_obj)