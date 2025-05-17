from django.conf import settings
from django.db import models
from django.utils import timezone

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

class Word(models.Model):
    level = models.CharField(max_length=1, default="5")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kanji = models.CharField(max_length=100, blank=True, null=True)
    kana = models.CharField(max_length=100, blank=True, null=True)
    romaji = models.CharField(max_length=100, blank=True, null=True)
    translate_ru = models.CharField(max_length=200, blank=True, null=True)
    translate_en = models.CharField(max_length=200, blank=True, null=True)
    part_of_speech = models.CharField(
        max_length=50, 
        blank=True, 
        null=True, 
    choices=[
        ('verb', 'Verb'),
        ('noun', 'Noun'),
        ('i-adjective', 'I-Adjective'),
        ('na-adjective', 'Na-Adjective'),
        ('adverb', 'Adverb'),
        ('conjunction', 'Conjunction'),  # ← добавлен
        ('particle', 'Particle'),        # ← добавлен
        ('interjection', 'Interjection'),  # ← для あ, ええ и т.п.
        ('auxiliary-verb', 'Auxiliary Verb'),  # ← 〜たい, 〜ます
        ('question-word', 'Question Word'),
        ('counter', 'Counter'),
        ('prefix', 'Prefix'),            # ← お〜, ご〜
        ('suffix', 'Suffix'),
        ('expression', 'Expression'),    # ← устойчивые выражения
        ('other', 'Other'),              # ← для редких случаев
    ]
    )

    def __str__(self):
        return f'{self.kanji} ({self.kana}) ({self.level})'

    class Meta:
        ordering = ['level', 'kanji', 'kana']


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
    level = models.IntegerField(default=5)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kanji = models.CharField(max_length=100)
    onyomi = models.CharField(max_length=100, blank=True, null=True)
    kunyomi = models.CharField(max_length=100, blank=True, null=True)
    meaning_ru = models.CharField(max_length=200, blank=True, null=True)
    meaning_en = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
            return f'{self.kanji} ({self.level})'
    class Meta:
    # Дополнительно можно указать порядок сортировки или уникальные ограничения
        ordering = ['level', 'kanji']