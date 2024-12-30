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

def about(request):
    return render(request, 'blog/grammar.html')  # Вернёт страницу about.html



def create_grammar(request):
    if request.method == 'POST':
        grammar_form = GrammarForm(request.POST)
        if grammar_form.is_valid():
            # Сохраняем грамматику
            grammar = grammar_form.save()

            # Создаем форму для добавления примера
            example_form = ExampleForm(request.POST)
            if example_form.is_valid():
                example_form.instance.grammar = grammar
                example_form.save()
                return redirect('grammar_list')  # Перенаправление на страницу с грамматиками

    else:
        grammar_form = GrammarForm()
        example_form = ExampleForm()

    return render(request, 'blog/create_grammar.html', {
        'grammar_form': grammar_form,
        'example_form': example_form
    })
