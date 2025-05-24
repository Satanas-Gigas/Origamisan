from django.contrib import admin
from .models import PartOfSpeech, Grammar, Example, Word, Kanji, Word_kana_variant, Word_kanji_variant, Word_translate_variant

admin.site.register(Example)

# Регистрация модели Word
@admin.register(Kanji)
class KanjiAdmin(admin.ModelAdmin):
    list_display = ('kanji', 'onyomi', 'kunyomi', 'meaning_ru', 'meaning_en', 'level', 'author')

@admin.register(PartOfSpeech)
class PartOfSpeechAdmin(admin.ModelAdmin):
    list_display = ('code',)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('kanji', 'kana', 'romaji', 'level', 'translate_ru', 'get_part_of_speech')
    search_fields = ('kanji', 'kana', 'romaji', "level", 'translate_en', 'translate_ru')
    filter_horizontal = ('part_of_speech',)

    @admin.display(description="Part of Speech")
    def get_part_of_speech(self, obj):
        return ", ".join(pos.code for pos in obj.part_of_speech.all())
    # def get_part_of_speech(self, obj):
    #     return ", ".join([pos.code for pos in obj.part_of_speech.all()])
    # get_part_of_speech.short_description = "Part of Speech"
    
@admin.register(Grammar)
class GrammarAdmin(admin.ModelAdmin):
    list_display = ('level', 'title', 'formula_ru', 'formula_en')

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
