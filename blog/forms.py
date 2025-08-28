from django import forms
from .models import Grammar, Example, Word, Kanji, Word_kana_variant, Word_kanji_variant, Word_translate_variant
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
import re

from .models import KanjiSentenceQuestion, KanjiSentenceFake

    
class GrammarForm(forms.ModelForm):
    class Meta:
        model = Grammar
        fields = ['level', 'author', 'title', 'formula_ru', 'formula_en', 'explain_ru', 'explain_en', 'example_jp_kanji', 'example_jp_kana', 'example_ru', 'example_en']

    author = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Выберите автора", widget=forms.Select(attrs={'class': 'form-select'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Применяем rows="3" ко всем полям Textarea и устанавливаем пустые значения
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['rows'] = '3'
                # Устанавливаем пустое значение для textarea, если оно None
                if field.initial is None:
                    field.initial = ""


class ExampleForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = ['grammar', 'add_example_jp_kanji', 'add_example_jp_kana', 'add_example_ru', 'add_example_en']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grammar'].required = False  # Поле grammar необязательно

    def clean(self):
        cleaned_data = super().clean()
        # Проверяем, заполнены ли хотя бы какие-то данные, кроме поля grammar
        non_grammar_fields = {
            key: value
            for key, value in cleaned_data.items()
            if key != 'grammar'
        }
        if not any(non_grammar_fields.values()):
            raise forms.ValidationError("Заполните хотя бы одно поле примера или не отправляйте форму.")
        return cleaned_data


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['level', 'author', 'kanji', 'kana', 'romaji', 'translate_ru', 'translate_en']
        
        widgets = {
            'level': forms.NumberInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'kanji': forms.TextInput(attrs={'class': 'form-control'}),
            'kana': forms.TextInput(attrs={'class': 'form-control'}),
            'romaji': forms.TextInput(attrs={'class': 'form-control'}),
            'translate_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'translate_en': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Устанавливаем значение по умолчанию для уровня
        self.fields['level'].initial = 5

    def clean(self):
        cleaned_data = super().clean()
        kana = cleaned_data.get('kana')
        romaji = cleaned_data.get('romaji')

        if not kana and not romaji:
            raise forms.ValidationError('По крайней мере одно из полей Kana или Romaji должно быть заполнено.')

        return cleaned_data

class KanjiForm(forms.ModelForm):
    class Meta:
        model = Kanji
        fields = ['level', 'author', 'kanji', 'onyomi', 'kunyomi', 'meaning_ru', 'meaning_en']

    author = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Выберите автора", widget=forms.Select(attrs={'class': 'form-select'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Применяем rows="3" ко всем полям Textarea и устанавливаем пустые значения
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['rows'] = '1'
                # Устанавливаем пустое значение для textarea, если оно None
                if field.initial is None:
                    field.initial = ""


class WordKanaVariantForm(forms.ModelForm):
    class Meta:
        model = Word_kana_variant
        fields = ['add_kana']

class WordKanjiVariantForm(forms.ModelForm):
    class Meta:
        model = Word_kanji_variant
        fields = ['add_kanji']

class WordTranslateVariantForm(forms.ModelForm):
    class Meta:
        model = Word_translate_variant
        fields = ['add_translate_ru', 'add_translate_en']
        


class WordKanaVariantForm(forms.ModelForm):
    class Meta:
        model = Word_kana_variant
        fields = ['add_kana']
        widgets = {
            'add_kana': forms.TextInput(attrs={'class': 'form-control'}),
        }

class WordKanjiVariantForm(forms.ModelForm):
    class Meta:
        model = Word_kanji_variant
        fields = ['add_kanji']
        widgets = {
            'add_kanji': forms.TextInput(attrs={'class': 'form-control'}),
        }

class WordTranslateVariantForm(forms.ModelForm):
    class Meta:
        model = Word_translate_variant
        fields = ['add_translate_ru', 'add_translate_en']
        widgets = {
            'add_translate_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'add_translate_en': forms.TextInput(attrs={'class': 'form-control'}),
        }

# new forms

KANJI_RANGE = r"[\u4E00-\u9FFF]"  # базовый CJK диапазон

class KanjiSentenceQuestionForm(forms.ModelForm):
    class Meta:
        model = KanjiSentenceQuestion
        fields = (
            "level",
            "sentence_kanji",
            "sentence_kana",
            "question_kanji",
            "question_kana",
            "translation_en",
            "translation_ru",
        )
        widgets = {
            "sentence_kanji": forms.Textarea(attrs={"rows": 3}),
            "sentence_kana":  forms.Textarea(attrs={"rows": 3}),
            "translation_en": forms.Textarea(attrs={"rows": 2}),
            "translation_ru": forms.Textarea(attrs={"rows": 2}),
        }

    def clean(self):
        cleaned = super().clean()
        s_kanji = (cleaned.get("sentence_kanji") or "").strip()
        q_kanji = (cleaned.get("question_kanji") or "").strip()
        s_kana  = (cleaned.get("sentence_kana") or "").strip()
        q_kana  = (cleaned.get("question_kana") or "").strip()

        if not s_kanji or not q_kanji:
            raise ValidationError("Заполните предложение и целевое слово (кандзи).")

        if q_kanji not in s_kanji:
            raise ValidationError("`question_kanji` не найден в `sentence_kanji`.")

        if not s_kana or not q_kana:
            raise ValidationError("Заполните поля каны (предложение и целевое слово).")

        return cleaned


class KanjiSentenceFakeForm(forms.ModelForm):
    class Meta:
        model = KanjiSentenceFake
        fields = ("text", "order")
        widgets = {
            "text": forms.TextInput(attrs={"placeholder": "Фейковый вариант (кандзи)", "class": "form-control"}),
            "order": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
        }

    def clean_text(self):
        txt = (self.cleaned_data.get("text") or "").strip()
        if not txt:
            raise ValidationError("Укажите фейковый вариант.")
        if not re.search(KANJI_RANGE, txt):
            raise ValidationError("Фейковый вариант должен содержать хотя бы один кандзи.")
        return txt


FakeFormSet = inlineformset_factory(
    parent_model=KanjiSentenceQuestion,
    model=KanjiSentenceFake,
    form=KanjiSentenceFakeForm,
    extra=3,              # при загрузке отображаем 3 пустые формы
    can_delete=True,
    min_num=3,            # минимум 3 фейка
    validate_min=True,
    max_num=20,
    validate_max=True,
)

def clean_fake_formset(formset: FakeFormSet, q_kanji: str):
    """
    Дополнительная валидация formset: уникальность, не равны правильному ответу.
    """
    texts = []
    for form in formset:
        if form.cleaned_data.get("DELETE"):
            continue
        txt = (form.cleaned_data.get("text") or "").strip()
        if not txt:
            # базовая форма бросит ошибку сама
            continue
        if txt == q_kanji:
            form.add_error("text", "Фейк не должен совпадать с правильным ответом.")
        if txt in texts:
            form.add_error("text", "Дубликат фейкового варианта.")
        texts.append(txt)
    if len(texts) < 3:
        raise ValidationError("Нужно минимум 3 различных фейковых варианта.")