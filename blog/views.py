from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import Grammar, Word, Kanji, Word_kana_variant, Word_kanji_variant, Word_translate_variant
from .forms import GrammarForm, ExampleForm, WordForm, KanjiForm,  WordKanaVariantForm, WordKanjiVariantForm, WordTranslateVariantForm
from django.forms import inlineformset_factory
import re
from django.db.models import Q, Case, When, F, Func, Count
from django.urls import reverse
from django.shortcuts import redirect
import json, random
import logging

def grammar(request):
    if request.method == "POST":
        level = request.POST.get('level', '5')
    else:
        level = request.GET.get('level', '5')

    if level not in ['4', '5']:
        level = '5'

    # grammars = Grammar.objects.prefetch_related('examples').filter(level=level)
    grammars = Grammar.objects.filter(level=level)
    return render(request, 'blog/grammar.html', {
        'grammars': grammars,
        'level': level
    })

def word(request):
    # Сначала пробуем из POST, потом из GET, если не указано — '5'
    level = request.POST.get('level') or request.GET.get('level') or '5'
    if level not in ['1', '2', '3', '4', '5']:
        level = '5'
    words = Word.objects.filter(level=level)
    return render(request, 'blog/word.html', {'words': words, 'level': level})

def mainpanel(request):
    return render(request, 'blog/mainpanel.html', {"show_header": True})

def mama(request):
    return render(request, 'blog/mama.html', {"show_header": False})


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
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            new_word = form.save()
            level = new_word.level  # уровень из созданного слова
            return redirect(reverse('word') + f'?level={level}#word-{new_word.pk}')
    else:
        form = WordForm()

    return render(request, 'blog/word_create.html', {'form': form})

def kanji(request):
    if request.method == "POST":
        level = request.POST.get('level', '5')
    else:
        level = request.GET.get('level', '5')

    if level not in ['5', '4', '3', '2', '1']:
        level = '5'

    kanjis = Kanji.objects.filter(level=level) # Предзагрузка примеров
    return render(request, 'blog/kanji.html', {'kanjis': kanjis, 'level': level})

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
    level = request.GET.get("level", "5")

    KanaFormSet = inlineformset_factory(Word, Word_kana_variant, fields=['add_kana'], extra=1, can_delete=True)
    KanjiFormSet = inlineformset_factory(Word, Word_kanji_variant, fields=['add_kanji'], extra=1, can_delete=True)
    TranslateFormSet = inlineformset_factory(Word, Word_translate_variant, fields=['add_translate_ru', 'add_translate_en'], extra=1, can_delete=True)

    if request.method == "POST":
        word_form = WordForm(request.POST, instance=word)
        kana_formset = KanaFormSet(request.POST, instance=word)
        kanji_formset = KanjiFormSet(request.POST, instance=word)
        translate_formset = TranslateFormSet(request.POST, instance=word)

        if all([word_form.is_valid(), kana_formset.is_valid(), kanji_formset.is_valid(), translate_formset.is_valid()]):
            word_form.save()
            kana_formset.save()
            kanji_formset.save()
            translate_formset.save()

            url = reverse('word') + f'?level={level}#word-{word.pk}'
            return redirect(url)
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
        'level': level,
        'word': word,
    }
    return render(request, 'blog/word_edit.html', context)

def word_test(request):
    level = request.POST.get('level') or request.GET.get('level') or '5'

    test_types = [
        ('kanji_to_kana', 'вопрос: Канджи, ответы: Кана', 'primary'),
        ('kana_to_kanji', 'вопрос: Кана, ответы: Канджи', 'success'),
        ('kanji_to_trans', 'вопрос: Канджи, ответы: Перевод', 'danger'),
        ('trans_to_kanji', 'вопрос: Перевод, ответы: Канджи', 'dark'),
    ]
    questions_list = [20, 30, 50]

    return render(request, 'blog/word_test.html', {
        'test_types': test_types,
        'questions_list': questions_list,
        'level': level  # 🔥 добавляем level в контекст
    })


def word_test_premium(request):
    return render(request, 'blog/word_test_premium.html')

def handle_hide_mode(request, question_count, level):
    correct_kanjis = []
    attempts = 0 
    word_kanji_list = Word.objects.filter(
    level = level,
    kanji__regex=r'[\u4E00-\u9FFF].*[\u4E00-\u9FFF]'
    ).values_list('kanji', flat=True)
    word_kanji_list = list(word_kanji_list)
    kanji_list = Kanji.objects.filter(
    kanji__in=[ 
        # kanji.kanji for kanji in Kanji.objects.all()
        kanji.kanji for kanji in Kanji.objects.filter(level = level)
        if any(kanji.kanji in word for word in word_kanji_list)
    ])
    if question_count == "all":
        question_count = len(kanji_list)
    else: 
        if not str(question_count).isdigit():
            return render(request, 'blog/word_test_start.html', {'error': 'Некорректное количество вопросов.'})
        question_count = int(question_count)

    while len(correct_kanjis) < question_count:
        excluded_kanji = [entry["answer"].kanji for entry in correct_kanjis]
        ids = list(kanji_list.exclude(kanji__in=excluded_kanji).values_list('id', flat=True))

        if not ids:
            break  # или continue — если не осталось подходящих

        random_id = random.choice(ids)
        correct_answer = Kanji.objects.get(id=random_id)
            
        words = Word.objects.filter(
            kanji__contains=correct_answer.kanji,
            kanji__regex=r'[\u4E00-\u9FFF].*[\u4E00-\u9FFF]'
        )[:4]
        if words.exists():
            combined_words = " ".join(word.kanji for word in words).replace(" ", "\u00A0\u00A0\u00A0\u00A0\u00A0")
            combined_kana = " ".join(word.kana for word in words).replace(" ", "\u00A0\u00A0\u00A0\u00A0\u00A0")
            correct_kanjis.append({"kanji": combined_words, "kana": combined_kana, "answer": correct_answer})
        else:    
            attempts += 1
        if len(correct_kanjis) >= question_count:
            break        
        if attempts > 28:
            raise ValueError('Не удалось найти подходящие слова для теста')        
    questions = []
    for correct_kanji in correct_kanjis:
        correct_answer = correct_kanji["answer"].kanji
        kanji = correct_kanji["kanji"]
        kana = correct_kanji["kana"]
        all_kanji = Kanji.objects.exclude(kanji=correct_answer).values_list('kanji', flat=True).order_by('?')[:3]
        distractors = random.sample(list(all_kanji), 3)
        options = distractors + [correct_answer]
        random.shuffle(options)
        hidden_word = kanji.replace(correct_answer, '___')
        questions.append({
            'question_word': hidden_word,
            'kana': kana,
            'options': options,
            'correct': correct_answer,
        })
    
    return questions

def generate_kanji_to_kana_questions(request, question_count, level):
    # Проверка значения question_count
    try:
        if question_count == "all":
            question_count = Word.objects.filter(
            kanji__isnull=False,
            level=level
            ).exclude(kanji="''").exclude(kanji=None).count()
        else:
            if not str(question_count).isdigit():
                return render(request, 'blog/word_test_start.html', {'error': 'Некорректное количество вопросов.'})
            question_count = int(question_count)
    except ValueError:
        raise ValueError("question_count должно быть числом или 'all'")

    questions = []

    # Получаем случайные слова с каной и канзи
    words = Word.objects.filter(kanji__isnull=False, level=level).exclude(kanji="''").exclude(kanji=None).order_by('?')[:question_count]

    for word in words:
        correct_kana = word.kana
        part_of_speech_set = word.part_of_speech.all()

        # Попытка найти суффикс каны через kanji
        kana_suffix = ""
        if re.match(r'^[\u4e00-\u9fff]+$', word.kanji):
            match = re.match(r'[\u4e00-\u9fff]+([\u3040-\u309f\u30a0-\u30ff]*)$', word.kanji)
            if match:
                kana_suffix = match.group(1)  # Извлекаем суффикс каны

        # Формируем запрос для получения фейковых вариантов
        all_kana_query = Word.objects.filter(~Q(kana=correct_kana)).exclude(kanji="''").exclude(kanji=None)  # Исключаем правильный ответ
        if part_of_speech_set:
            all_kana_query = all_kana_query.filter(part_of_speech__in=part_of_speech_set)
        if kana_suffix and len(kana_suffix) > 0:
            all_kana_query = all_kana_query.filter(kana__endswith=kana_suffix)

        # Получаем список вариантов
        all_kana = list(all_kana_query.values_list('kana', flat=True).order_by('?')[:10])
        if len(all_kana) < 3:
            # print(f'not enough kana {len(all_kana)}')
            all_kana = list(Word.objects.filter(~Q(kana=correct_kana)).values_list('kana', flat=True).order_by('?')[:3])
            if len(all_kana) < 3:
                continue

        # Генерируем фейковые ответы
        fake_kana = random.sample(all_kana, 3)
        if correct_kana in fake_kana:
            fake_kana.remove(correct_kana)
        options = fake_kana + [correct_kana]
        random.shuffle(options)

        # Добавляем вопрос в список
        questions.append({
            'question_word': word.kanji,
            'options': options,
            'correct': correct_kana,
        })

    return questions

def generate_kana_to_kanji_questions(request, question_count, level):
    if question_count == "all":
        question_count = Word.objects.filter(
            level=level,
            kana__isnull=False, kanji__isnull=False
        ).exclude(kana="").exclude(kanji="''").exclude(kanji=None).count()
    else:
        if not str(question_count).isdigit():
            return render(request, 'blog/word_test_start.html', {'error': 'Некорректное количество вопросов.'})
        question_count = int(question_count)

    questions = []

    # Получаем случайные слова с каной и канзи
    words = Word.objects.filter(
        level=level,
        kana__isnull=False, kanji__isnull=False
    ).exclude(kana="''").exclude(kanji="''").exclude(kanji=None).order_by('?')[:question_count]

    for word in words:
        correct_kanji = word.kanji
        part_of_speech_set = word.part_of_speech.all()

        # Регулярное выражение для выделения каны и иероглифов
        kana_suffix = ""
        match = re.match(r'[\u4e00-\u9fff]+([\u3040-\u309f\u30a0-\u30ff]*)$', correct_kanji)
        if match:
            kana_suffix = match.group(1)  # Извлекаем суффикс каны
            # print(f'kana_suffix is - {kana_suffix}')

        # Формируем запрос для получения фейковых вариантов
        all_kanji_query = Word.objects.filter(~Q(kanji=correct_kanji)).exclude(kanji="''").exclude(kanji=None)
        if part_of_speech_set:  # Учитываем часть речи
            all_kanji_query = all_kanji_query.filter(part_of_speech__in=part_of_speech_set)
        if kana_suffix:  # Если найден суффикс, фильтруем по нему
            all_kanji_query = all_kanji_query.filter(kana__endswith=kana_suffix)

        # Получаем список фейковых вариантов
        all_kanji = list(all_kanji_query.values_list('kanji', flat=True).order_by('?')[:10])
        if len(all_kanji) < 3:
            # Если недостаточно вариантов, используем общий список
            all_kanji = list(
                Word.objects.filter(~Q(kanji=correct_kanji))
                .values_list('kanji', flat=True)
                .order_by('?')[:3]
            )
        if len(all_kanji) < 3:
            continue  # Пропускаем вопрос, если недостаточно данных

        # Создаем варианты ответа
        fake_kanji = random.sample(all_kanji, min(len(all_kanji), 3))
        options = fake_kanji + [correct_kanji]
        random.shuffle(options)

        # Добавляем вопрос
        questions.append({
            'question_word': word.kana,
            'options': options,
            'correct': correct_kanji,
        })

    return questions

def generate_kanji_to_trans_questions(request, question_count, level):
    if question_count == "all":
        question_count = Word.objects.annotate(pos_count=Count('part_of_speech')).filter(
            kanji__isnull=False,
            translate_ru__isnull=False,
            level=level,
            pos_count__gt=0
        ).exclude(kanji="").exclude(kanji=None).count()
    else:
        if not str(question_count).isdigit():
            return render(request, 'blog/word_test_start.html', {'error': 'Некорректное количество вопросов.'})
        question_count = int(question_count)

    questions = []

    words = Word.objects.annotate(pos_count=Count('part_of_speech')).filter(
        kanji__isnull=False,
        translate_ru__isnull=False,
        level=level,
        pos_count__gt=0
    ).exclude(kanji="").exclude(kanji=None).order_by('?')[:question_count]

    for word in words:
        correct_trans = word.translate_ru or ""
        part_of_speech_set = list(word.part_of_speech.all())

        # print(f"\n▶️ Слово: {word.kanji} → {correct_trans}")
        # print(f"   Части речи: {[p.code for p in part_of_speech_set]}")

        # Поиск других переводов с совпадающими частями речи
        all_trans = Word.objects.filter(
            part_of_speech__in=part_of_speech_set
        ).exclude(
            translate_ru__isnull=True
        ).exclude(
            translate_ru=""
        ).exclude(
            translate_ru=correct_trans
        ).values_list(
            'translate_ru', flat=True
        ).distinct()

        all_trans = list(set(all_trans))  # Убираем дубликаты

        # print(f"   🔍 Найдено вариантов перевода: {len(all_trans)}")

        if len(all_trans) < 3:
            # fallback на любые переводы
            all_trans = Word.objects.exclude(
                translate_ru__isnull=True
            ).exclude(
                translate_ru=""
            ).exclude(
                translate_ru=correct_trans
            ).values_list(
                'translate_ru', flat=True
            ).order_by('?')[:10]
            all_trans = list(set(all_trans))

        if len(all_trans) < 3:
            print("⛔ Недостаточно вариантов — пропущено")
            continue

        fake_trans = random.sample(all_trans, 3)
        options = fake_trans + [correct_trans]
        random.shuffle(options)

        questions.append({
            'question_word': word.kanji,
            'options': options,
            'correct': correct_trans,
        })

    return questions

def generate_trans_to_kanji_questions(request, question_count, level):
    if question_count == "all":
        # question_count = Word.objects.filter(translate_ru__isnull=False).exclude(translate_ru="''").count()
        question_count = Word.objects.filter(
            translate_ru__isnull=False,
            kana__isnull=False,
            kanji__isnull=False,
            level=level
        ).exclude(translate_ru="''").count()
    else:
        if not str(question_count).isdigit():
            return render(request, 'blog/word_test_start.html', {'error': 'Некорректное количество вопросов.'})
        question_count = int(question_count)
    questions = []

    # Получаем случайные слова с переводом на русский
    # words = Word.objects.filter(translate_ru__isnull=False).exclude(translate_ru="''").order_by('?')[:question_count]
    words = Word.objects.filter(
        kana__isnull=False,
        kanji__isnull=False,
        level=level
    ).exclude(kana="''").exclude(kanji="''").exclude(kanji=None).order_by('?')[:question_count]

    for word in words:
        # Определяем правильный вариант (kanji или kana)
        correct_kanji = word.kanji if word.kanji != "''" else word.kana
        part_of_speech_set = word.part_of_speech.all()

        # Получаем список всех kanji или заменяем их на kana, если kanji пусто
        all_kanji = list(
            Word.objects.filter(part_of_speech__in=part_of_speech_set)
            .annotate(
                kanji_or_kana=Case(
                    When(kanji="''", then=F('kana')),  # Если kanji пусто, берём kana
                    default=F('kanji')                 # Иначе берём kanji
                )
            )
            .exclude(kanji_or_kana=correct_kanji)  # Исключаем правильный ответ
            .values_list('kanji_or_kana', flat=True)
            .order_by('?')[:10]  # Больше выборка для надёжности
        )

        # Если недостаточно вариантов, пропускаем вопрос
        if len(all_kanji) < 3:
            continue

        # Генерируем фейковые варианты
        fake_kanji = random.sample(all_kanji, 3)
        options = fake_kanji + [correct_kanji]
        random.shuffle(options)

        # Добавляем вопрос
        questions.append({
            'question_word': word.translate_ru,
            'options': options,
            'correct': correct_kanji,
        })
        
    return questions

def hide_kanji_with_ruby(text, kanji):
    """
    Скрывает первое вхождение кандзи:
    - если кандзи внутри <ruby>...</ruby> — заменяет весь ruby-блок на ＊＊＊
    - если кандзи вне ruby — заменяет только первое вхождение на ＊＊＊
    """
    ruby_pattern = re.compile(r'<ruby>(.+?)<rt>.*?</rt></ruby>')
    for m in ruby_pattern.finditer(text):
        ruby_body = m.group(1)
        if kanji in ruby_body:
            start, end = m.span()
            return text[:start] + ' ____ ' + text[end:]
    return text.replace(kanji, ' ____ ', 1)

def get_ruby_block(text, kanji):
    """
    Возвращает (ruby_body, ruby_span)
    - ruby_body: что между <ruby> и <rt>
    - ruby_span: tuple индексов (start, end)
    Если нет — возвращает (None, None)
    """
    ruby_pattern = re.compile(r'<ruby>(.+?)<rt>.*?</rt></ruby>')
    for m in ruby_pattern.finditer(text):
        ruby_body = m.group(1)
        if kanji in ruby_body:
            return ruby_body, m.span()
    return None, None


def strip_ruby_tags(text):
    """
    Удаляет ruby/rt и любые другие html-теги, возвращая только видимый текст.
    """
    text = re.sub(r'<rt>.*?</rt>', '', text)
    text = re.sub(r'</?ruby>', '', text)
    text = re.sub(r'<.*?>', '', text)
    return text

def generate_kanji_sentence_test(request, question_count, level):
    logger = logging.getLogger("kanji_sentence_test")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    
    logger.info(f"=== Генерация kanji_sentence_test: level={level}, question_count={question_count}")

    try:
        question_count = int(question_count)
    except Exception as e:
        logger.error(f"Ошибка преобразования question_count: {question_count} — {e}")
        return []

    # Все кандзи этого уровня
    kanji_list = list(Kanji.objects.filter(level=level).values_list('kanji', flat=True))
    logger.info(f"Кандзи на уровне {level}: {kanji_list}")

    if not kanji_list:
        logger.warning("Нет кандзи для выбранного уровня!")
        return []

    sample_kanji = random.sample(kanji_list, min(question_count, len(kanji_list)))
    logger.info(f"Выбраны кандзи для вопросов: {sample_kanji}")

    questions = []

    for k in sample_kanji:
        logger.info(f"\n=== Проверяем кандзи: {k}")

        word_qs = Word.objects.filter(
            kanji__contains=k, level=level
        ).exclude(examples__isnull=True).exclude(examples='')

        logger.info(f"Количество Word с этим кандзи и примерами: {word_qs.count()}")

        if not word_qs.exists():
            logger.warning(f"Нет слов с этим кандзи ({k}) на уровне {level}")
            continue

        word = word_qs.order_by('?').first()
        logger.info(f"Случайное слово: {word.kanji} | kana: {word.kana} | examples: {word.examples[:80]+'...'}")

        try:
            examples = json.loads(word.examples)
        except Exception as e:
            logger.error(f"Ошибка загрузки examples для {word.kanji}: {e}")
            continue

        examples = [e for e in examples if "jp" in e]
        logger.info(f"Примеров с ключом jp: {len(examples)}")

        if not examples:
            logger.warning(f"Нет подходящих примеров для {word.kanji}")
            continue

        ex = random.choice(examples)
        logger.info(f"Выбранный пример: {ex['jp'][:80]}...")

        # Проверяем, содержится ли сам кандзи в примере
        if k not in ex["jp"]:
            logger.warning(f"В примере нет кандзи {k}! Пример: {ex['jp'][:80]}")
            continue

        # --- Ключевой момент: ищем ruby-блок
        ruby_body, ruby_span = get_ruby_block(ex["jp"], k)
        options = []
        correct_variant = None

        if ruby_body:
            # Вариант с ruby
            question_word = ex["jp"][:ruby_span[0]] + ' ____ ' + ex["jp"][ruby_span[1]:]
            correct_variant = strip_ruby_tags(ruby_body)  # Текст без тегов

            # Подбор фейковых кандзи по радикалу
            radical = Kanji.objects.filter(kanji=k).first().radical
            fake_kanji_qs = Kanji.objects.filter(radical=radical).exclude(kanji=k)
            fake_kanji_list = list(fake_kanji_qs.values_list('kanji', flat=True))

            # Если фейковых кандзи >=3, используем их, иначе добираем случайными с уровня
            if len(fake_kanji_list) >= 3:
                fake_kanji_list = random.sample(fake_kanji_list, 3)
            else:
                candidates = [x for x in kanji_list if x != k and x not in fake_kanji_list]
                while len(fake_kanji_list) < 3 and candidates:
                    extra = random.choice(candidates)
                    fake_kanji_list.append(extra)
                    candidates.remove(extra)

            # Генерируем ложные ответы: заменяем только первое вхождение k на поддельный
            for fk in fake_kanji_list:
                fake_text = ruby_body.replace(k, fk, 1)
                options.append(strip_ruby_tags(fake_text))
            options.append(correct_variant)
            random.shuffle(options)

        else:
            # Нет ruby — просто скрываем символ, ответы — отдельные кандзи
            question_word = ex["jp"].replace(k, ' ____ ', 1)
            correct_variant = k

            # Ложные варианты — по радикалу или случайные
            radical = Kanji.objects.filter(kanji=k).first().radical
            fake_kanji_qs = Kanji.objects.filter(radical=radical).exclude(kanji=k)
            fake_kanji_list = list(fake_kanji_qs.values_list('kanji', flat=True))

            if len(fake_kanji_list) >= 3:
                fake_kanji_list = random.sample(fake_kanji_list, 3)
            else:
                candidates = [x for x in kanji_list if x != k and x not in fake_kanji_list]
                while len(fake_kanji_list) < 3 and candidates:
                    extra = random.choice(candidates)
                    fake_kanji_list.append(extra)
                    candidates.remove(extra)

            options = fake_kanji_list + [correct_variant]
            random.shuffle(options)

        logger.info(f"Варианты ответа: {options} (правильный: {correct_variant})")

        questions.append({
            "question_word": question_word,
            "options": options,
            "correct": correct_variant,
            "kana": word.kana,
            "en": ex.get("en"),
            "ru": ex.get("ru"),
        })

    logger.info(f"\nИтого вопросов сгенерировано: {len(questions)}")
    return questions

def process_request_params(request):
    rollback = request.POST.get('rollback')
    test_type = request.GET.get('test_type')    
    if not test_type:
        test_type = request.POST.get('test_type')
    extra_option = request.POST.get('extra_option')
    question_count = request.GET.get('questions')
    if not question_count:
        question_count = request.POST.get('questions_p')

    # ВРЕМЯ ПОКАЗА ВОПРОСА
    question_time_raw = request.POST.get('question_time', request.GET.get('question_time', None))
    if question_time_raw in [None, "", "None"]:
        question_time = 0   # <- если "нет" - это именно 0, а не None!
    else:
        try:
            question_time = int(question_time_raw)
            if question_time < 0:
                question_time = 0
        except ValueError:
            question_time = 0

    # ВРЕМЯ ПОКАЗА ОТВЕТОВ
    answers_time_raw = request.POST.get('answers_time', request.GET.get('answers_time', None))
    if answers_time_raw in [None, "", "None"]:
        answers_time = 40  # дефолт
    else:
        try:
            answers_time = int(answers_time_raw)
            if answers_time < 1 or answers_time > 60:
                answers_time = 40
        except ValueError:
            answers_time = 40
    print('question_time', question_time,'  answers_time', answers_time)

    request.session.update({
        'question_time': question_time,
        'answers_time': answers_time,
        'test_type': test_type,
        'extra_option': extra_option,
        'question_count': question_count,
        'rollback': rollback,        
    })

    return test_type, question_count, extra_option, question_time, answers_time

def word_test_start(request):

    level = request.POST.get('level') or request.GET.get('level') or '5'
   
    
    try:
        test_type, question_count, extra_option, question_time, answers_time = process_request_params(request)
        print(f"test_type={test_type}, question_count={question_count}, level={level}")

        allowed_test_types = {'hide', 'kanji_to_kana', 'kana_to_kanji', 'kanji_to_trans', 'trans_to_kanji', 'kanji_sent'}
        if test_type not in allowed_test_types:
            return render(request, 'blog/word_test_start.html', {'error': 'Некорректный тип теста.'})

        # Генерация вопросов с учётом типа теста
        if test_type == 'hide':
            questions = handle_hide_mode(request, question_count, level)
        elif test_type == 'kanji_to_kana':
            questions = generate_kanji_to_kana_questions(request, question_count, level)
        elif test_type == 'kana_to_kanji':
            questions = generate_kana_to_kanji_questions(request, question_count, level)
        elif test_type == 'kanji_to_trans':
            questions = generate_kanji_to_trans_questions(request, question_count, level)
        elif test_type == 'trans_to_kanji':
            questions = generate_trans_to_kanji_questions(request, question_count, level)
        elif test_type == 'kanji_sent':
            # print("PROVERKA")
            questions = generate_kanji_sentence_test(request, question_count, level)
        else:
            return render(request, 'blog/word_test_start.html', {'error': 'Неизвестный тип теста.'})

        # ✅ Проверка: есть ли вопросы вообще
        if not questions:
            return render(request, 'blog/word_test_start.html', {
                'error': '❌ Не удалось сгенерировать вопросы. Возможно, в базе нет подходящих слов для этого уровня или типа теста.'
            })

        # Сохраняем данные в сессию
        request.session.update({
            'questions': questions,
            'current_question_index': 0,
            'user_answers': [],
            'question_time': question_time,
            'answers_time': answers_time,
            'extra_option': extra_option,
            'level': level
        })

        # Отображаем первый вопрос
        context = {
            'question': questions[0],
            'total': question_count if question_count != "all" else len(questions),
            'question_count': question_count,
            'test_type': test_type,
            'question_time': question_time,
            'answers_time': answers_time,
            'extra_option': extra_option,
            'level': level
        }
        
        return render(request, 'blog/word_test_start.html', context)
    except ValueError as e:
        return render(request, 'blog/word_test_start.html', {'error': str(e)})
    
def word_test_next(request):
    hide = request.session.get('hide')
    question_time = request.session.get('question_time')
    answers_time = request.session.get('answers_time')
    current_index = request.session.get('current_question_index', 0)
    questions = request.session.get('questions', [])
    user_answer = request.POST.get('user_answer')
    correct_answer = questions[current_index]['correct']
    is_correct = user_answer == correct_answer
    user_answers = request.session.get('user_answers', [])
    user_answers.append(is_correct)
    request.session['user_answers'] = user_answers
    rollback = request.session['rollback']
    extra_option = request.session['extra_option']
    level = request.session.get('level')
    
    if rollback == 'all':
        rollback = len(questions)
    elif (rollback == 'no' or rollback == 'None'):
        rollback = None
    if rollback != None:
        rollback = int(rollback)
        
    request.session['hide'] = hide

    current_index += 1

    if (not is_correct and rollback):
        current_index = max(0, current_index - rollback)

    if current_index < len(questions):
        request.session['current_question_index'] = current_index
        context = {
            'question': questions[current_index],
            'current_index': current_index,
            'len_qs': len(questions),
            'hide': hide,
            'rollback': rollback,
            'question_time': question_time,
            'answers_time': answers_time,
            'extra_option': extra_option,  # убрали пробел в ключе
            'level': level,    
            'test_type': request.session.get('test_type'),  # ⬅️ ЭТО ВАЖН

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
    rollback = request.session.get('rollback')
    question_count = request.session.get('question_count')
    extra_option = request.session.get('extra_option')
    answers_time = request.session.get('answers_time')
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
        'rollback': rollback,
        'extra_option': extra_option,
        'answers_time': answers_time,
    }
    return render(request, 'blog/word_test_complete.html', context)

