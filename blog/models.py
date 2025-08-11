from django.conf import settings
from django.db import models
from django.utils import timezone
import json

class Grammar(models.Model):
    level = models.CharField(max_length=1,default="5")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    formula_ru = models.CharField(max_length=200, blank=True, null=True)
    formula_en = models.CharField(max_length=200, blank=True, null=True)
    explain_ru = models.TextField (blank=True, null=True)
    explain_en = models.TextField (blank=True, null=True)
    example_jp_kanji = models.TextField (blank=True, null=True)  # Пример на японском
    example_jp_kana = models.TextField (blank=True, null=True) # Пример на русском
    example_ru = models.TextField (blank=True, null=True) # Пример на английском
    example_en = models.TextField (blank=True, null=True)  # Пример на английском


    def __str__(self):
            return f'{self.title} ({self.level})'
    
    class Meta:
    # Дополнительно можно указать порядок сортировки или уникальные ограничения
        ordering = ['level', 'title']

class PartOfSpeech(models.Model):
    code = models.CharField(max_length=100, unique=True)  # например, "Noun" или "Transitive verb"
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.code



class Word(models.Model):
    level = models.CharField(max_length=1, default="5")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    kanji = models.CharField(max_length=100, blank=True, null=True)
    kana = models.CharField(max_length=100, blank=True, null=True)
    romaji = models.CharField(max_length=100, blank=True, null=True)
    
    translate_en = models.CharField(max_length=200, blank=True, null=True)
    translate_ru = models.CharField(max_length=200, blank=True, null=True)
    
    part_of_speech = models.ManyToManyField('PartOfSpeech', blank=True)
    auto_translated_ru = models.BooleanField(default=False)

    # Заменяем JSONField на TextField
    examples = models.TextField(blank=True, null=True, help_text="Примеры предложений (сохранять как JSON-строку)")

    def __str__(self):
        return f'{self.kanji or self.kana} ({self.level})'
    
    class Meta:
        ordering = ['level', 'kanji', 'kana']

    # Вспомогательные методы для работы с примерами
    def get_examples(self):
        if self.examples:
            try:
                return json.loads(self.examples)
            except json.JSONDecodeError:
                return []
        return []
    
    def set_examples(self, examples_list):
        self.examples = json.dumps(examples_list, ensure_ascii=False)

    def get_random_example(self):
        import random
        examples = self.get_examples()
        if examples:
            return random.choice(examples)
        return None



class Example(models.Model):
    grammar = models.ForeignKey(Grammar, related_name='examples', on_delete=models.CASCADE)
    add_example_jp_kanji = models.TextField (blank=True, null=True) # Пример на японском
    add_example_jp_kana = models.TextField (blank=True, null=True)  # Пример на русском
    add_example_ru = models.TextField (blank=True, null=True) # Пример на английском
    add_example_en = models.TextField (blank=True, null=True)  # Пример на английском

    def __str__(self):
        return f"Example for {self.grammar.title} ({self.grammar.level})"
    

class Word_kana_variant(models.Model):
    word = models.ForeignKey(Word, related_name='fake_kana', on_delete=models.CASCADE)
    add_kana = models.TextField (blank=True, null=True)

    def __str__(self):
        return f"Example for {self.word.kana} ({self.word.level})"    

class Word_kanji_variant(models.Model):
    word = models.ForeignKey(Word, related_name='fake_kanji', on_delete=models.CASCADE)
    add_kanji = models.TextField (blank=True, null=True)
    
    def __str__(self):
        return f"Example for {self.word.kanji} ({self.word.level})"
    

class Word_translate_variant(models.Model):
    word = models.ForeignKey(Word, related_name='fake_translate', on_delete=models.CASCADE)
    add_translate_ru = models.TextField (blank=True, null=True)
    add_translate_en = models.TextField (blank=True, null=True)
    
    def __str__(self):
        return f"Example for {self.word.translate_ru} ({self.word.level})"
   

class Kanji(models.Model):
    level = models.CharField(max_length=1, default="5")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kanji = models.CharField(max_length=1)  # обновлённый размер
    onyomi = models.CharField(max_length=100, blank=True, null=True)
    kunyomi = models.CharField(max_length=100, blank=True, null=True)
    meaning_ru = models.CharField(max_length=200, blank=True, null=True)
    meaning_en = models.CharField(max_length=200, blank=True, null=True)
    radical = models.CharField(max_length=1, blank=True, null=True)  # новое поле

    def __str__(self):
        return f'{self.kanji} ({self.level})'
    class Meta:
        ordering = ['level', 'kanji']