from django.core.management.base import BaseCommand
from blog.models import Word

class Command(BaseCommand):
    help = 'Подсчитывает количество слов с уровнем 4'

    def handle(self, *args, **options):
        count = Word.objects.filter(level="4").count()
        self.stdout.write(self.style.SUCCESS(f"🔢 Всего слов с уровнем 4: {count}"))