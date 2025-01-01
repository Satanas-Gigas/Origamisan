from django.conf import settings
from django.shortcuts import render, redirect
from .models import Post, Grammar
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, GrammarForm, ExampleForm
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def grammar(request):
    grammars = Grammar.objects.filter(level=5)
    return render(request, 'blog/grammar.html', {'grammars': grammars})



from django.shortcuts import render, redirect
from .forms import GrammarForm, ExampleForm

from django.shortcuts import render, redirect
from .forms import GrammarForm, ExampleForm

def create_grammar(request):
    if request.method == 'POST':
        grammar_form = GrammarForm(request.POST)
        example_form = ExampleForm(request.POST)

        if grammar_form.is_valid():
            # Сохраняем объект Grammar, но не коммитим
            grammar = grammar_form.save(commit=False)
            grammar.save()  # Теперь у grammar есть первичный ключ

            if example_form.is_valid():
                # Передаем грамматику в форму примеров
                example = example_form.save(commit=False)
                example.grammar = grammar
                example.save()

            return redirect('grammar')  # Перенаправление после успешного сохранения

    else:
        grammar_form = GrammarForm()
        example_form = ExampleForm()

    return render(request, 'blog/create_grammar.html', {
        'grammar_form': grammar_form,
        'example_form': example_form,
    })