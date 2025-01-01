from django import forms

from .models import Post, Grammar, Example

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

    
class GrammarForm(forms.ModelForm):
    class Meta:
        model = Grammar
        fields = ['level', 'author', 'title_ru', 'title_en', 'explain_ru', 'explain_en', 'example_jp_kanji', 'example_jp_kana', 'example_ru', 'example_en']

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
