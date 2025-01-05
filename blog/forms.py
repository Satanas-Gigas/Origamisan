from django import forms
from .models import Post, Grammar, Example, Word, Kanji
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
    
class GrammarForm(forms.ModelForm):
    class Meta:
        model = Grammar
        fields = ['level', 'author', 'title_ru', 'title_en', 'explain_ru', 'explain_en', 'example_jp_kanji', 'example_jp_kana', 'example_ru', 'example_en']

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