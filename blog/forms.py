from django import forms

from .models import Post, Grammar, Example

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

    
class GrammarForm(forms.ModelForm):
    class Meta:
        model = Grammar
        fields = ['level', 'title', 'explain_ru', 'explain_en']

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = ['grammar', 'example_jp', 'example_ru', 'example_en']