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