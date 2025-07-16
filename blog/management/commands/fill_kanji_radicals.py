import json
from django.core.management.base import BaseCommand
from blog.models import Kanji
from tqdm import tqdm

class Command(BaseCommand):
    help = "Заполняет поле radical у Kanji из kanji_radicals.json с прогресс-баром"

    def handle(self, *args, **options):
        with open('kanji_radicals.json', encoding='utf-8') as f:
            radical_data = json.load(f)

        updated, not_found = 0, 0

        for item in tqdm(radical_data, desc="Обновляем Kanji", unit="канжи"):
            kanji = item.get('kanji')
            radical = item.get('rd')
            if not kanji or not radical:
                continue

            obj = Kanji.objects.filter(kanji=kanji).first()
            if obj:
                obj.radical = radical
                obj.save()
                updated += 1
            else:
                not_found += 1
                self.stdout.write(self.style.WARNING(f"Не найдено в БД: {kanji}"))

        self.stdout.write(self.style.SUCCESS(
            f'Готово! Обновлено: {updated}, не найдено: {not_found}'))
