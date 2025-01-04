from django.contrib import admin
from .models import Post, Grammar, Example, Word, Kanji

admin.site.register(Post)
admin.site.register(Grammar)
admin.site.register(Example)
admin.site.register(Word)
admin.site.register(Kanji)