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
    title = models.CharField(max_length=200)
    explain_ru = models.TextField()
    explain_en = models.TextField()

    def __str__(self):
        return self.title

class Example(models.Model):
    grammar = models.ForeignKey(Grammar, related_name='examples', on_delete=models.CASCADE)
    example_jp = models.TextField()  # Пример на японском
    example_ru = models.TextField()  # Пример на русском
    example_en = models.TextField()  # Пример на английском

    def __str__(self):
        return f"Example for {self.grammar.title}"
