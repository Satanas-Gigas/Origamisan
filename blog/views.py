
from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Grammar, Word, Kanji, Word_kana_variant, Word_kanji_variant, Word_translate_variant
from .forms import PostForm, GrammarForm, ExampleForm, WordForm, KanjiForm,  WordKanaVariantForm, WordKanjiVariantForm, WordTranslateVariantForm
from django.forms import inlineformset_factory
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
import random


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
    grammars = Grammar.objects.prefetch_related('examples').filter(level=5)  # Предзагрузка примеров
    return render(request, 'blog/grammar.html', {'grammars': grammars})

def word(request):
    words = Word.objects.filter(level="5")  # Предзагрузка примеров
    return render(request, 'blog/word.html', {'words': words})


def mainpanel(request):
    return render(request, 'blog/mainpanel.html')

def grammar_create(request):
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

    return render(request, 'blog/grammar_create.html', {
        'grammar_form': grammar_form,
        'example_form': example_form,
    })

def word_create(request):
    """
    View to handle creation of a new Word object.
    """
    if request.method == 'POST':
        word_form = WordForm(request.POST)
        if word_form.is_valid():
            # Сохраняем слово
            word_form.save()
            # messages.success(request, 'Слово успешно сохранено!')
            return redirect('word')  # Замените на ваш URL списка слов или другую нужную страницу
        # else:
        #     messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        word_form = WordForm()

    context = {'form': word_form,}
    return render(request, 'blog/word_create.html', context)


def kanji(request):
    kanjis = Kanji.objects.filter(level=5)  # Предзагрузка примеров
    return render(request, 'blog/kanji.html', {'kanjis': kanjis})


def grammar_edit(request, pk):
    # Получаем объект Grammar
    grammar = get_object_or_404(Grammar, pk=pk)
    
    # Если форма отправлена (POST-запрос)
    if request.method == 'POST':
        # Создаем форму для Grammar
        grammar_form = GrammarForm(request.POST, instance=grammar)
        
        # Получаем формы для примеров
        example_forms = []
        for example in grammar.examples.all():
            example_form = ExampleForm(request.POST, instance=example)
            example_forms.append(example_form)

        if grammar_form.is_valid():
            # Сохраняем объект Grammar, но не коммитим сразу
            grammar = grammar_form.save(commit=False)
            grammar.save()  # Сохраняем грамматику

            # Обрабатываем формы для примеров
            for example_form in example_forms:
                if example_form.is_valid():
                    example = example_form.save(commit=False)
                    example.grammar = grammar  # Связываем пример с грамматикой
                    example.save()

            return redirect('grammar')  # Перенаправляем после успешного сохранения

    else:
        # Если запрос не POST, создаем пустые формы
        grammar_form = GrammarForm(instance=grammar)
        example_forms = [ExampleForm(instance=example) for example in grammar.examples.all()]

    return render(request, 'blog/grammar_edit.html', {
        'grammar_form': grammar_form,
        'example_forms': example_forms,
    })

def kanji_create(request):
    if request.method == 'POST':
        kanji_form = KanjiForm(request.POST)
        if kanji_form.is_valid():
            kanji_form.save()
            return redirect('kanji') 
    else:
        kanji_form = KanjiForm()

    context = {'form': kanji_form,}
    return render(request, 'blog/kanji_create.html', context)


def kanji_edit(request, pk):
    kanji = get_object_or_404(Kanji, pk=pk)
    if request.method == "POST":
        form = KanjiForm(request.POST, instance=kanji)
        if form.is_valid():
            kanji = form.save(commit=False)
            kanji.save()
            return redirect('kanji')
    else:
        form = KanjiForm(instance=kanji)
    return render(request, 'blog/kanji_edit.html', {'form': form})



def word_variant_create(request, pk):
    word = get_object_or_404(Word, pk=pk)
    if request.method == 'POST':
        kana_form = WordKanaVariantForm(request.POST)
        kanji_form = WordKanjiVariantForm(request.POST)
        translate_form = WordTranslateVariantForm(request.POST)
        if kana_form.is_valid() and kanji_form.is_valid() and translate_form.is_valid():
            kana_variant = kana_form.save(commit=False)
            kana_variant.word = word
            kana_variant.save()

            kanji_variant = kanji_form.save(commit=False)
            kanji_variant.word = word
            kanji_variant.save()

            translate_variant = translate_form.save(commit=False)
            translate_variant.word = word
            translate_variant.save()

            return redirect('word')
    else:
        kana_form = WordKanaVariantForm()
        kanji_form = WordKanjiVariantForm()
        translate_form = WordTranslateVariantForm()

    return render(request, 'blog/word_variant_create.html', {
        'word': word,
        'kana_form': kana_form,
        'kanji_form': kanji_form,
        'translate_form': translate_form,
    })


def word_detail_view(request):
    words = Word.objects.prefetch_related('fake_kana', 'fake_kanji', 'fake_translate').all()
    context = {
        'words': words,
    }
    return render(request, 'blog/word_detail.html', context)




def word_edit(request, pk):
    word = get_object_or_404(Word, pk=pk)
    if request.method == "POST":
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            word = form.save(commit=False)
            word.save()
            return redirect('word')
    else:
        form = WordForm(instance=word)
    return render(request, 'blog/word_edit.html', {'form': form})

def word_edit(request, pk):
    word = get_object_or_404(Word, pk=pk)

    # Создание формсетов для каждой дочерней модели
    KanaFormSet = inlineformset_factory(Word, Word_kana_variant, fields=['add_kana'], extra=1, can_delete=True)
    KanjiFormSet = inlineformset_factory(Word, Word_kanji_variant, fields=['add_kanji'], extra=1, can_delete=True)
    TranslateFormSet = inlineformset_factory(Word, Word_translate_variant, fields=['add_translate_ru', 'add_translate_en'], extra=1, can_delete=True)

    if request.method == "POST":
        word_form = WordForm(request.POST, instance=word)
        kana_formset = KanaFormSet(request.POST, instance=word)
        kanji_formset = KanjiFormSet(request.POST, instance=word)
        translate_formset = TranslateFormSet(request.POST, instance=word)

        if word_form.is_valid() and kana_formset.is_valid() and kanji_formset.is_valid() and translate_formset.is_valid():
            word = word_form.save()
            kana_formset.save()
            kanji_formset.save()
            translate_formset.save()
            return redirect('word_detail')  # Замените на нужный URL
    else:
        word_form = WordForm(instance=word)
        kana_formset = KanaFormSet(instance=word)
        kanji_formset = KanjiFormSet(instance=word)
        translate_formset = TranslateFormSet(instance=word)

    context = {
        'form': word_form,
        'kana_formset': kana_formset,
        'kanji_formset': kanji_formset,
        'translate_formset': translate_formset,
    }
    return render(request, 'blog/word_edit.html', context)


def word_test(request):
    return render(request, 'blog/word_test.html')

def word_test_start(request):
    question_count = int(request.GET.get('questions', 10))
    test_type = request.GET.get('type', 'kanji_to_kana')  # Тип теста: kanji -> kana или kana -> kanji
    
    questions = []
    if test_type == 'kanji_to_kana':
        # Логика текущего теста (kanji -> kana)
        all_kana = list(Word.objects.exclude(kana__isnull=True).exclude(kana="").values_list('kana', flat=True))[:question_count * 4]
        words = Word.objects.filter(kanji__isnull=False).exclude(kanji="''").order_by('?')[:question_count]
        
        for word in words:
            correct_kana = word.kana
            fake_kana = random.sample([kana for kana in all_kana if kana != correct_kana], 3)
            options = fake_kana + [correct_kana]
            random.shuffle(options)
            questions.append({
                'question_word': word.kanji,
                'options': options,
                'correct': correct_kana,
            })

    elif test_type == 'kana_to_kanji':
        # Логика нового теста (kana -> kanji)
        all_kanji = list(Word.objects.exclude(kanji__isnull=True).exclude(kanji="''").values_list('kanji', flat=True))[:question_count * 4]
        words = Word.objects.filter(kana__isnull=False).exclude(kana="''").exclude(kanji="''").order_by('?')[:question_count]
        
        for word in words:
            correct_kanji = word.kanji
            fake_kanji = random.sample([kanji for kanji in all_kanji if kanji != correct_kanji], 3)
            options = fake_kanji + [correct_kanji]
            random.shuffle(options)
            questions.append({
                'question_word': word.kana,
                'options': options,
                'correct': correct_kanji,
            })

    request.session['questions'] = questions
    request.session['current_question_index'] = 0
    request.session['user_answers'] = []

    context = {'question': questions[0], 'total': len(questions), 'question_count': question_count, 'test_type': test_type}
    return render(request, 'blog/word_test_start.html', context)



def word_test_next(request):
    # Получаем текущий индекс вопроса
    current_index = request.session.get('current_question_index')
    
    # Загружаем все вопросы из сессии
    questions = request.session.get('questions', [])
    
    # Получаем ответ пользователя
    user_answer = request.POST.get('user_answer')
    correct_answer = questions[current_index]['correct']
    
    # Сохраняем ответ пользователя (правильный/неправильный)
    is_correct = user_answer == correct_answer
    user_answers = request.session.get('user_answers', [])
    user_answers.append(is_correct)
    request.session['user_answers'] = user_answers

    # Проверяем, есть ли следующий вопрос
    if current_index < len(questions) - 1:
        # Увеличиваем индекс
        request.session['current_question_index'] = current_index + 1
        context = {
            'question': questions[current_index + 1],
            "current_index": current_index + 1,
            "len_qs": len(questions),
        }  # Передаем следующий вопрос
        return render(request, 'blog/word_test_start.html', context)
    else:
        # Если вопросы закончились, перенаправляем на страницу завершения
        return redirect('word_test_complete')


def word_test_complete(request):
    # Загружаем ответы пользователя
    user_answers = request.session.get('user_answers', [])
    
    # Подсчитываем количество правильных и неправильных ответов
    correct_count = user_answers.count(True)
    incorrect_count = user_answers.count(False)
    total_count = len(user_answers)
    
    # Дополнительная статистика
    accuracy_percentage = (correct_count / total_count * 100) if total_count > 0 else 0

    # Очищаем сессии после завершения теста
    request.session['user_answers'] = []
    request.session['questions'] = []
    request.session['current_question_index'] = 0

    context = {
        'correct_count': correct_count,
        'incorrect_count': incorrect_count,
        'accuracy_percentage': accuracy_percentage,
        'total_count': total_count,
    }
    
    return render(request, 'blog/word_test_complete.html', context)