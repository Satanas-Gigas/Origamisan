from django.contrib import admin
from .models import Grammar, Example, Word, Kanji, Word_kana_variant, Word_kanji_variant, Word_translate_variant

admin.site.register(Example)

# Регистрация модели Word
@admin.register(Kanji)
class KanjiAdmin(admin.ModelAdmin):
    list_display = ('kanji', 'onyomi', 'kunyomi', 'meaning_ru', 'meaning_en', 'level', 'author')


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('kanji', 'kana', 'part_of_speech', 'level', 'author')
    list_filter = ('part_of_speech', 'level')
    search_fields = ('kanji', 'kana', 'translate_ru', 'translate_en')    

@admin.register(Grammar)
class GrammarAdmin(admin.ModelAdmin):
    list_display = ('title', 'formula_ru')

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
