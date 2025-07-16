# blog/management/commands/jisho_sentences.py

import requests
from bs4 import BeautifulSoup
import json
import time
import os
from tqdm import tqdm
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Парсит до 3 примеров с jisho.org для каждого kanji из файла kanji_words.txt (resume поддерживается)"

    def handle(self, *args, **kwargs):
        kanji_path = 'kanji_words.txt'
        out_path = 'jishyo_sentences.json'
        sleep_time = 2.5  # Не спамим сайт!
        timeout = 60

        # Грузим все kanji-слова
        with open(kanji_path, encoding='utf-8') as f:
            kanji_words = [line.strip() for line in f if line.strip()]

        # Поддержка resume: грузим уже спарсенное
        results = []
        already_done = set()
        if os.path.exists(out_path):
            with open(out_path, encoding='utf-8') as f:
                try:
                    results = json.load(f)
                    already_done = set(x["kanji"] for x in results if "kanji" in x)
                except Exception:
                    results = []
                    already_done = set()

        # Собираем только недостающие слова
        todo_words = [k for k in kanji_words if k not in already_done]

        self.stdout.write(f"Всего слов: {len(kanji_words)} | Уже собрано: {len(already_done)} | Осталось: {len(todo_words)}")

        # tqdm для шкалы прогресса
        pbar = tqdm(total=len(todo_words), desc="Парсим Jisho.org")

        start_time = time.time()
        for idx, word in enumerate(todo_words):
            entry = {"kanji": word, "examples": []}
            url = f"https://jisho.org/search/{requests.utils.quote(word)}%20%23sentences"
            try:
                r = requests.get(url, timeout=timeout)
                soup = BeautifulSoup(r.text, "html.parser")
                # Блоки с предложениями
                contents = soup.select("div.sentence_content")
                if not contents:
                    entry["examples"].append({"note": "Нет японских примеров на Jisho"})
                else:
                    for block in contents[:3]:
                        # Берём весь ul как есть
                        ul = block.find("ul", class_="japanese_sentence")
                        jp = str(ul) if ul else ""
                        # Перевод
                        en_block = block.select_one(".english_sentence .english")
                        en = en_block.get_text(strip=True) if en_block else ""
                        # URL
                        url_block = block.select_one(".inline_copyright a")
                        ex_url = url_block['href'] if url_block else ""
                        # абсолютный url если надо
                        if ex_url and ex_url.startswith("//"):
                            ex_url = "https:" + ex_url
                        elif ex_url and ex_url.startswith("/"):
                            ex_url = "https://jisho.org" + ex_url
                        example = {
                            "jp": jp,
                            "en": en,
                            "ru": "",
                            "url": ex_url
                        }
                        entry["examples"].append(example)
            except Exception as e:
                entry["examples"].append({"note": f"Ошибка: {str(e)}"})

            results.append(entry)
            # Сохраняем каждый раз (resume)
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(results, f, ensure_ascii=False, indent=2)

            pbar.update(1)
            # Подсчёт оставшегося времени
            elapsed = time.time() - start_time
            remain = (elapsed / (idx+1)) * (len(todo_words) - (idx+1))
            pbar.set_postfix(ETA=f"{int(remain//60)}m{int(remain%60)}s")
            time.sleep(sleep_time)
        pbar.close()
        self.stdout.write(self.style.SUCCESS(f"Готово! Сохранили {len(results)} записей в {out_path}"))
