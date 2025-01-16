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
            grammar = grammar_form.save(commit=False)
            grammar.save()  # Теперь у grammar есть первичный ключ

            if example_form.is_valid():
                example = example_form.save(commit=False)
                example.grammar = grammar
                example.save()

            return redirect('grammar') 
    else:
        grammar_form = GrammarForm()
        example_form = ExampleForm()

    return render(request, 'blog/grammar_create.html', {
        'grammar_form': grammar_form,
        'example_form': example_form,
    })

def word_create(request):
    if request.method == 'POST':
        word_form = WordForm(request.POST)
        if word_form.is_valid():
            word_form.save()
            return redirect('word')
    else:
        word_form = WordForm()

    context = {'form': word_form,}
    return render(request, 'blog/word_create.html', context)

def kanji(request):
    kanjis = Kanji.objects.filter(level=5)  # Предзагрузка примеров
    return render(request, 'blog/kanji.html', {'kanjis': kanjis})

def grammar_edit(request, pk):
    grammar = get_object_or_404(Grammar, pk=pk)    
    if request.method == 'POST':
        grammar_form = GrammarForm(request.POST, instance=grammar)
        example_forms = []
        for example in grammar.examples.all():
            example_form = ExampleForm(request.POST, instance=example)
            example_forms.append(example_form)
        if grammar_form.is_valid():
            grammar = grammar_form.save(commit=False)
            grammar.save()
            for example_form in example_forms:
                if example_form.is_valid():
                    example = example_form.save(commit=False)
                    example.grammar = grammar
                    example.save()
            return redirect('grammar')
    else:
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
            return redirect('word_detail')
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

def word_test_premium(request):
    return render(request, 'blog/word_test_premium.html')

def process_request_params(request):
    rollback = request.POST.get('rollback')
    hide = request.POST.get('hide')
    test_type = request.GET.get('type', 'kanji_to_kana')  
    question_count = request.GET.get('questions')
    if not question_count:
        question_count = request.POST.get('questions_p')
    print(f"questions_count: {question_count}")

    request.session.update({
        'hide': hide,
        'test_type': test_type,
        'question_count': question_count,
        'rollback': rollback,
    })
    return hide, test_type, question_count

def handle_hide_mode(question_count):
    correct_kanjis = []
    attempts = 0
    question_count = int(question_count)
    print(f"!!!!!!!questions_count: {question_count}")
    while len(correct_kanjis) < 5:
        correct_answer = Kanji.objects.order_by('?').first()
        word = Word.objects.filter(
            kanji__contains=correct_answer.kanji,
            kanji__regex=r'[\u4E00-\u9FFF].*[\u4E00-\u9FFF]'
        ).order_by('?').first()
        if word:
            correct_kanjis.append({"kanji": word, "answer": correct_answer})
        attempts += 1
        if attempts > 20:
            # print(f"Не удалось найти подходящие слова для теста")
            raise ValueError('Не удалось найти подходящие слова для теста')

    questions = []
    for correct_kanji in correct_kanjis:
        correct_answer = correct_kanji["answer"].kanji
        kanji = correct_kanji["kanji"].kanji
        all_kanji = Kanji.objects.exclude(kanji=correct_answer).values_list('kanji', flat=True).order_by('?')[:3]
        distractors = random.sample(list(all_kanji), 3)
        options = distractors + [correct_answer]
        random.shuffle(options)
        hidden_index = kanji.find(correct_answer)
        # print(f"hidden_word: {hidden_index}")
        hidden_word = kanji[:hidden_index] + "＿" + kanji[hidden_index + 1:]
        questions.append({
            'question_word': hidden_word,
            'options': options,
            'correct': correct_answer,
        })   
    return questions

def generate_kanji_to_kana_questions(question_count):
    question_count = int(question_count)
    questions = []
    all_kana = list(Word.objects.exclude(kana__isnull=True).exclude(kana="''").values_list('kana', flat=True).order_by('?'))[:3]
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
    return questions

def generate_kana_to_kanji_questions(question_count):
    questions = []
    all_kanji = list(Word.objects.exclude(kana__isnull=True).exclude(kanji="''").values_list('kanji', flat=True).order_by('?'))[:question_count * 4]
    words = Word.objects.filter(kanji__isnull=False).exclude(kanji="''").order_by('?')[:question_count]
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
    return questions

def word_test_start(request):
    try:
        hide, test_type, question_count = process_request_params(request)
        
        if hide == 'on':
            questions = handle_hide_mode(question_count)
        elif test_type == 'kanji_to_kana':
            questions = generate_kanji_to_kana_questions(question_count)
        elif test_type == 'kana_to_kanji':
            questions = generate_kana_to_kanji_questions(question_count)
        elif test_type == 'kanji_to_trans':
            questions = generate_kanji_to_trans_questions(question_count)
        elif test_type == 'trans_to_kanji':
            questions = generate_trans_to_kanji_questions(question_count)
        else:
            return render(request, 'blog/word_test_start.html', {'error': 'Неизвестный тип теста'})

        request.session.update({
            'questions': questions,
            'current_question_index': 0,
            'user_answers': [],
        })

        context = {
            'question': questions[0],
            'total': question_count,
            'question_count': question_count,
            'test_type': test_type,
            'hide': hide,
        }
        return render(request, 'blog/word_test_start.html', context)

    except ValueError as e:
        return render(request, 'blog/word_test_start.html', {'error': str(e)})

def word_test_next(request):
    hide = request.session.get('hide')
    current_index = request.session.get('current_question_index', 0)
    questions = request.session.get('questions', [])
    user_answer = request.POST.get('user_answer')
    correct_answer = questions[current_index]['correct']
    is_correct = user_answer == correct_answer
    user_answers = request.session.get('user_answers', [])
    user_answers.append(is_correct)
    request.session['user_answers'] = user_answers
    rollback_count = request.session['rollback']
    if rollback_count != None:
        rollback_count = int(rollback_count)
    # rollback_count = int(request.session.get('rollback', 0)) - 1 if request.session.get('rollback') else 0
    request.session['hide'] = hide

    current_index += 1
    if rollback_count == None:
        print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"rollback_current_index: {current_index}")

    elif not is_correct:
        current_index = max(0, current_index - rollback_count)
        print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"rollback_current_index: {current_index}")

    if current_index < len(questions):
        request.session['current_question_index'] = current_index
        context = {
            'question': questions[current_index],
            'current_index': current_index,
            'len_qs': len(questions),
            'hide': hide,
            'rollback_count': rollback_count,
        }
        return render(request, 'blog/word_test_start.html', context)
    else:
        return redirect('word_test_complete')

def word_test_complete(request):
    user_answers = request.session.get('user_answers', [])
    if not isinstance(user_answers, list):
        user_answers = []
    correct_count = sum(1 for answer in user_answers if answer is True)
    incorrect_count = sum(1 for answer in user_answers if answer is False)
    total_count = len(user_answers)
    accuracy_percentage = (correct_count / total_count * 100) if total_count > 0 else 0
    test_type = request.session.get('test_type')
    question_count = request.session.get('question_count')
    request.session.pop('user_answers', None)
    request.session.pop('questions', None)
    request.session.pop('current_question_index', None)
    context = {
        'correct_count': correct_count,
        'incorrect_count': incorrect_count,
        'accuracy_percentage': round(accuracy_percentage, 2),  # Ограничиваем точность до двух знаков
        'total_count': total_count,
        'test_type': test_type,
        'question_count': question_count,
    }
    return render(request, 'blog/word_test_complete.html', context) 