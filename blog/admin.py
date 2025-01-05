from django.contrib import admin
from .models import Post, Grammar, Example, Word, Kanji,  Word_kana_variant, Word_kanji_variant, Word_translate_variant

admin.site.register(Post)
admin.site.register(Grammar)
admin.site.register(Example)
# admin.site.register(Word)
admin.site.register(Kanji)

admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('kanji', 'kana', 'romaji', 'translate_ru', 'translate_en', 'level', 'author')

# Регистрация дочерних моделей
@admin.register(Word_kana_variant)
class WordKanaVariantAdmin(admin.ModelAdmin):
    list_display = ('word', 'add_kana')

@admin.register(Word_kanji_variant)
class WordKanjiVariantAdmin(admin.ModelAdmin):
    list_display = ('word', 'add_kanji')

@admin.register(Word_translate_variant)
class WordTranslateVariantAdmin(admin.ModelAdmin):
    list_display = ('word', 'add_translate_ru', 'add_translate_en')