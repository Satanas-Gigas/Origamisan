import json
import time
import openai
from tqdm import tqdm

openai.api_key = "your-openai-api-key"  # 🔑 Вставь сюда свой ключ

INPUT_FILE = "words_n2.json"
OUTPUT_FILE = "words_n2_translated.json"

MAX_RETRIES = 3
DELAY = 1.5  # Секунды между запросами

def translate_with_gpt(text):
    """Перевод с английского на русский через OpenAI GPT."""
    prompt = f"Переведи на русский язык следующую английскую фразу:\n{text}"
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # или gpt-4 если нужно
                messages=[
                    {"role": "system", "content": "Ты профессиональный переводчик с английского на русский."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"⚠️ Ошибка при переводе '{text}' (попытка {attempt}): {e}")
            time.sleep(DELAY * attempt)
    return ""

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    for word in tqdm(data, desc="🌐 Перевод на русский"):
        if "translate_ru" not in word or not word["translate_ru"]:
            en_text = word.get("translate_en", "").strip()
            if en_text:
                ru_text = translate_with_gpt(en_text)
                word["translate_ru"] = ru_text
                time.sleep(DELAY)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"\n✅ Перевод завершён. Сохранено в {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
