from django.core.management.base import BaseCommand
from blog.models import Word
import json
import re
from tqdm import tqdm

def html_to_ruby(html):
    """
    Преобразует сырой html (с ul/li и span) в строку с ruby-тегами, где:
    - обычный текст иероглифов идет подряд, 
    - <ruby>KANJI<rt>FURIGANA</rt></ruby> — для кусков с фуриганой
    """

    # Очищаем <ul lang="ja"> и пробелы
    html = re.sub(r'<ul[^>]*>', '', html)
    html = re.sub(r'</ul>', '', html)
    html = html.replace('\n', '')

    # Собираем все <li>...</li> и весь текст ВНЕ li-тегов
    parts = []
    last_end = 0
    for m in re.finditer(r'<li[^>]*>(.*?)</li>', html):
        # Всё что было ДО <li>... (текст между ли)
        before = html[last_end:m.start()]
        if before:
            # Могут быть случайные &nbsp; — уберём
            before = re.sub(r'&nbsp;| ', '', before)
            before = before.strip()
            if before:
                parts.append(before)
        li_html = m.group(1)
        # Есть ли фуригана
        furi = re.match(
            r'<span class="furigana">(.*?)</span><span class="unlinked">(.*?)</span>',
            li_html
        )
        if furi:
            parts.append(f'<ruby>{furi.group(2)}<rt>{furi.group(1)}</rt></ruby>')
        else:
            # Если только <span class="unlinked"> (например, частицы)
            unlinked = re.match(r'<span class="unlinked">(.*?)</span>', li_html)
            if unlinked:
                parts.append(unlinked.group(1))
            else:
                # Если вообще чистый текст внутри li
                parts.append(li_html.strip())
        last_end = m.end()

    # Если что-то осталось после последнего </li> (например, в конце предложения)
    after = html[last_end:]
    after = re.sub(r'&nbsp;| ', '', after)
    after = after.strip()
    if after:
        parts.append(after)

    # Склеиваем всё подряд — именно так, как в твоём примере
    result = ''.join(parts)
    return result.strip()

class Command(BaseCommand):
    help = "Импорт и обработка примеров с фуриганой: преобразует в ruby-формат"

    def handle(self, *args, **options):
        with open("jishyo_sentences.json", "r", encoding="utf-8") as f:
            all_examples = json.load(f)

        self.stdout.write("Очищаю все examples в базе...")
        Word.objects.update(examples="")

        kanji_to_examples = {}
        for e in all_examples:
            filtered_examples = [ex for ex in e['examples'] if not ex.get('note')]
            if filtered_examples:
                kanji_to_examples[e['kanji']] = filtered_examples

        words = Word.objects.filter(kanji__in=list(kanji_to_examples.keys()))

        for word in tqdm(words, desc="Импорт примеров"):
            ex_arr = kanji_to_examples.get(word.kanji, [])
            for ex in ex_arr:
                if "jp" in ex:
                    ex['jp'] = html_to_ruby(ex['jp'])
            word.examples = json.dumps(ex_arr, ensure_ascii=False, indent=2)
            word.save(update_fields=['examples'])

        self.stdout.write(self.style.SUCCESS(f'Импорт завершён! Добавлено примеров: {words.count()}'))
