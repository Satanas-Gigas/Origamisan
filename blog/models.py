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
    title_ru = models.CharField(max_length=200, default="Des")
    title_en = models.CharField(max_length=200, default="Des")
    explain_ru = models.TextField (blank=True, null=True, default="Des")
    explain_en = models.TextField (blank=True, null=True, default="Des")
    example_jp_kanji = models.TextField (blank=True, null=True, default="Des")  # Пример на японском
    example_jp_kana = models.TextField (blank=True, null=True, default="Des") # Пример на русском
    example_ru = models.TextField (blank=True, null=True, default="Des") # Пример на английском
    example_en = models.TextField (blank=True, null=True, default="Des")  # Пример на английском


    def __str__(self):
        return self.title_ru

class Example(models.Model):
    grammar = models.ForeignKey(Grammar, related_name='examples', on_delete=models.CASCADE)
    add_example_jp_kanji = models.TextField (blank=True, null=True, default="Des") # Пример на японском
    add_example_jp_kana = models.TextField (blank=True, null=True, default="Des")  # Пример на русском
    add_example_ru = models.TextField (blank=True, null=True, default="Des") # Пример на английском
    add_example_en = models.TextField (blank=True, null=True, default="Des")  # Пример на английском

    def __str__(self):
        return f"Example for {self.grammar.title_ru}"
