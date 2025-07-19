from django.core.management.base import BaseCommand
import MeCab

def kata_to_hira(char):
    """Перевести символ катаканы в хирагану"""
    code = ord(char)
    if 0x30A0 <= code <= 0x30FF:
        return chr(code - 0x60)
    return char

def fix_yomi(original, yomi):
    orig_kata = set([c for c in original if '\u30A0' <= c <= '\u30FF'])
    result = []
    for c in yomi:
        if '\u30A0' <= c <= '\u30FF':
            if c in orig_kata:
                result.append(c)
            else:
                result.append(kata_to_hira(c))
        else:
            result.append(c)
    return ''.join(result)

def get_yomi_mecab(text):
    # Используем MeCab для разбора йоми
    tagger = MeCab.Tagger("-Oyomi")
    yomi = tagger.parse(text).strip()
    return yomi

class Command(BaseCommand):
    help = "Добавляет исправленную йоми к японским предложениям"

    def handle(self, *args, **kwargs):
        input_path = 'jpn_sentences.tsv'
        output_path = 'jpn_sentences_with_yomi.tsv'

        # Узнаём общее число строк для шкалы прогресса
        with open(input_path, encoding='utf-8') as f:
            total_lines = sum(1 for _ in f)
        processed = 0

        tagger = MeCab.Tagger("-Oyomi")

        with open(input_path, encoding='utf-8') as fin, \
             open(output_path, 'w', encoding='utf-8') as fout:
            for line in fin:
                parts = line.strip().split('\t')
                if len(parts) < 3:
                    continue
                sid, lang, sentence = parts[:3]
                yomi = tagger.parse(sentence).strip()
                yomi_fixed = fix_yomi(sentence, yomi)
                fout.write(f"{sid}\t{lang}\t{sentence}\t{yomi_fixed}\n")

                processed += 1
                if processed % 5000 == 0 or processed == total_lines:
                    percent = processed / total_lines * 100
                    self.stdout.write(f"Processed {processed}/{total_lines} ({percent:.1f}%)")

        self.stdout.write(self.style.SUCCESS(f"Done! {processed} sentences processed. Saved to {output_path}"))
