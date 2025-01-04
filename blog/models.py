from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Grammar(models.Model):
    level = models.IntegerField(default=5)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    explain_ru = models.TextField (blank=True, null=True)
    explain_en = models.TextField (blank=True, null=True)
    example_jp_kanji = models.TextField (blank=True, null=True)  # Пример на японском
    example_jp_kana = models.TextField (blank=True, null=True) # Пример на русском
    example_ru = models.TextField (blank=True, null=True) # Пример на английском
    example_en = models.TextField (blank=True, null=True)  # Пример на английском


    def __str__(self):
        return f'{self.example_ru} ({self.level})'
    
    class Meta:
    # Дополнительно можно указать порядок сортировки или уникальные ограничения
        ordering = ['level', 'title_ru', 'title_en']

class Example(models.Model):
    grammar = models.ForeignKey(Grammar, related_name='examples', on_delete=models.CASCADE)
    add_example_jp_kanji = models.TextField (blank=True, null=True) # Пример на японском
    add_example_jp_kana = models.TextField (blank=True, null=True)  # Пример на русском
    add_example_ru = models.TextField (blank=True, null=True) # Пример на английском
    add_example_en = models.TextField (blank=True, null=True)  # Пример на английском

    def __str__(self):
        return f"Example for {self.grammar.title_ru}"
    
class Word(models.Model):
    level = models.IntegerField(default=5)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kanji = models.CharField(max_length=100, blank=True, null=True)
    kana = models.CharField(max_length=100, blank=True, null=True)
    romaji = models.CharField(max_length=100, blank=True, null=True)
    translate_ru = models.CharField(max_length=200, blank=True, null=True)
    translate_en = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
            return f'{self.kanji} ({self.kana})'
    class Meta:
    # Дополнительно можно указать порядок сортировки или уникальные ограничения
        ordering = ['level', 'kanji', 'kana']




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