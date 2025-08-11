import time
from django.core.management.base import BaseCommand
from django.db.models import Q
from blog.models import Word

try:
    from googletrans import Translator
except ImportError:
    raise ImportError("Установи googletrans: pip install googletrans==4.0.0rc1")

class Command(BaseCommand):
    help = "Автоматически переводит пустые translate_ru из translate_en с пометкой [AUTO]"

    def handle(self, *args, **options):
        qs = Word.objects.filter(
            Q(translate_ru__isnull=True) | Q(translate_ru='')
        ).filter(
            translate_en__isnull=False
        ).exclude(
            translate_en=''
        )

        total = qs.count()
        if total == 0:
            self.stdout.write(self.style.WARNING('Нет слов для автоперевода.'))
            return

        self.stdout.write(self.style.NOTICE(
            f'Найдено {total} слов с пустым translate_ru и заполненным translate_en.'
        ))
        start_time = time.time()
        translator = Translator()
        updated = 0
        error_log = []

        for idx, word in enumerate(qs, 1):
            text = word.translate_en
            attempt = 0
            translated = None

            while attempt < 2 and not translated:
                try:
                    result = translator.translate(text, src='en', dest='ru')
                    translated = result.text.strip()
                except Exception as e:
                    attempt += 1
                    self.stdout.write(self.style.ERROR(f"Ошибка перевода для id={word.id}: {e} (попытка {attempt})"))
                    time.sleep(2)  # Добавляем задержку перед повтором

            if not translated:
                error_log.append(str(word.id))
                continue

            # Добавляем пометку [AUTO] для автоматических переводов
            word.translate_ru = translated + " [AUTO]"
            word.save(update_fields=['translate_ru'])
            updated += 1

            # Прогресс-бар и ETA
            elapsed = time.time() - start_time
            avg_time = elapsed / idx if idx > 0 else 0
            left = total - idx
            eta = int(avg_time * left)
            d, h = divmod(eta, 86400)
            h, m = divmod(h, 3600)
            m, s = divmod(m, 60)
            print(
                f"\r{idx}/{total} ({(idx/total)*100:.2f}%) "
                f"- ETA: {d}д {h}ч {m}м {s}с   ",
                end='', flush=True
            )

            time.sleep(1.1)  # Задержка между запросами, чтобы не душило API

        print(f"\nГотово! Всего обновлено: {updated}")

        # Лог ошибок
        if error_log:
            with open('translate_ru_errors.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(error_log))
            print(f"Ошибок перевода: {len(error_log)}. См. translate_ru_errors.txt")

