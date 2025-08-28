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
from collections import defaultdict
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from .forms import KanjiSentenceQuestionForm, FakeFormSet, clean_fake_formset
from .models import KanjiSentenceQuestion

MAX_QUESTIONS = 50
ALLOWED_LEVELS = {1, 2, 3, 4, 5}

# --- Утилиты нормализации и рандома без order_by('?') ---

def _normalize_level(level):
    """Безопасно приводим уровень к int и разрешённому диапазону."""
    try:
        lvl = int(level)
    except Exception:
        lvl = 5
    if lvl not in ALLOWED_LEVELS:
        lvl = 5
    return lvl

def _normalize_qcount(qc, hard_cap=MAX_QUESTIONS):
    """Поддержка 'all' c жёстким верхним пределом, либо число 1..MAX_QUESTIONS."""
    if isinstance(qc, str) and qc.strip().lower() == "all":
        return hard_cap
    try:
        val = int(qc)
    except Exception:
        raise ValueError("Некорректное количество вопросов.")
    return max(1, min(val, hard_cap))

def _unique(seq):
    """Сохраняем порядок, убираем дубликаты."""
    return list(dict.fromkeys(seq))

def _shuffle_sample(seq, k):
    """Сэмпл из Python в памяти без нагрузки на БД; k может быть > len(seq)."""
    lst = list(seq)
    random.shuffle(lst)
    return lst[:k]

def _random_ids(qs, limit):
    """Берём все id, тасуем, режем до limit, затем подтягиваем объекты этим списком."""
    ids = list(qs.values_list('id', flat=True))
    if not ids:
        return []
    random.shuffle(ids)
    return ids[:limit]

# --- Вьюхи экрана выбора ---



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
    raw_level = request.POST.get('level') or request.GET.get('level') or '5'
    level = _normalize_level(raw_level)

    test_types = [
        ('kanji_to_kana',  'вопрос: Канджи, ответы: Кана',     'primary'),
        ('kana_to_kanji',  'вопрос: Кана, ответы: Канджи',     'success'),
        ('kanji_to_trans', 'вопрос: Канджи, ответы: Перевод',  'danger'),
        ('trans_to_kanji', 'вопрос: Перевод, ответы: Канджи',  'dark'),
        ('kanji_sent',     'вопрос: Текст, ответы: Канджи',    'info'),
    ]
    questions_list = [20, 30, 50]

    return render(request, 'blog/word_test.html', {
        'test_types': test_types,
        'questions_list': questions_list,
        'level': level,
    })


def word_test_premium(request):
    return render(request, 'blog/word_test_premium.html')

KANJI_PAIR_REGEX = r'[\u4E00-\u9FFF][^\u4E00-\u9FFF]*[\u4E00-\u9FFF]'  # две кандзи

def handle_hide_mode(request, question_count, level):
    level = _normalize_level(level)

    # Соберём список подходящих слов (содержат >=2 кандзи) уровня
    word_kanji_list = list(
        Word.objects.filter(
            level=level,
            kanji__regex=KANJI_PAIR_REGEX
        ).values_list('kanji', flat=True)
    )
    word_kanji_list = _unique([w for w in word_kanji_list if w])

    # Кандзи этого уровня, которые вообще встречаются в выбранных словах
    # (оптимизация без вложенного «any» в Python в большой таблице тут в порядке,
    #  но можно ещё быстрее, если хранить обратный индекс.)
    level_kanji_qs = Kanji.objects.filter(level=level)
    level_kanji = list(level_kanji_qs.values_list('kanji', flat=True))
    covered_kanji = [k for k in level_kanji if any(k in w for w in word_kanji_list)]

    kanji_list_qs = Kanji.objects.filter(kanji__in=covered_kanji, level=level)

    # Нормализуем требуемое число вопросов под фактический пул и верхний предел
    total_possible = kanji_list_qs.count()
    qcap = min(MAX_QUESTIONS, total_possible if total_possible else 0) or MAX_QUESTIONS
    question_count = _normalize_qcount(question_count, hard_cap=qcap)

    correct_kanjis = []
    attempts = 0

    # Выбираем случайные Kanji.id на каждой итерации без order_by('?')
    excluded = set()

    while len(correct_kanjis) < question_count:
        # пул допустимых id
        ids = list(kanji_list_qs.exclude(kanji__in=excluded).values_list('id', flat=True))
        if not ids:
            break

        random_id = random.choice(ids)
        correct_answer = Kanji.objects.get(id=random_id)
        excluded.add(correct_answer.kanji)

        # Небольшой лимит слов на комбинирование
        cand_words_qs = Word.objects.filter(
            kanji__contains=correct_answer.kanji,
            kanji__regex=KANJI_PAIR_REGEX
        ).only('kanji', 'kana').values('kanji', 'kana')

        cand_words = _shuffle_sample(list(cand_words_qs), 4)
        if cand_words:
            combined_words = " ".join(w['kanji'] for w in cand_words if w.get('kanji'))
            combined_kana  = " ".join(w['kana']  for w in cand_words if w.get('kana'))
            # заменим пробелы на NBSP только визуально — это безопасно, экранировать в шаблоне не «safe»
            combined_words = combined_words.replace(" ", "\u00A0\u00A0\u00A0\u00A0\u00A0")
            combined_kana  = combined_kana.replace(" ",  "\u00A0\u00A0\u00A0\u00A0\u00A0")

            correct_kanjis.append({
                "kanji": combined_words,
                "kana": combined_kana,
                "answer": correct_answer
            })
        else:
            attempts += 1

        if attempts > 28:
            raise ValueError("Не удалось подобрать достаточное количество слов для теста.")

    questions = []
    # Дистракторы без order_by('?')
    all_kanji_pool = list(Kanji.objects.values_list('kanji', flat=True))

    for item in correct_kanjis:
        correct_answer = item["answer"].kanji
        kanji = item["kanji"]
        kana = item["kana"]

        pool = [x for x in all_kanji_pool if x and x != correct_answer]
        pool = _unique(pool)
        if len(pool) < 3:
            continue

        distractors = _shuffle_sample(pool, 3)
        options = distractors + [correct_answer]
        random.shuffle(options)

        # заменим только первое вхождение, чтобы не «прятать» лишнее
        hidden_word = re.sub(re.escape(correct_answer), '___', kanji)
        questions.append({
            'question_word': hidden_word,
            'kana': kana,
            'options': options,
            'correct': correct_answer,
        })

    return questions

def generate_kanji_to_kana_questions(request, question_count, level):
    level = _normalize_level(level)

    # Сколько максимум вообще возможно для данного уровня
    total_possible = Word.objects.filter(
        kanji__isnull=False, level=level
    ).exclude(kanji="''").exclude(kanji=None).count()
    qcap = min(MAX_QUESTIONS, total_possible or 0) or MAX_QUESTIONS

    question_count = _normalize_qcount(question_count, hard_cap=qcap)

    # Берём id и тасуем их
    ids = _random_ids(
        Word.objects.filter(
            kanji__isnull=False, level=level
        ).exclude(kanji="''").exclude(kanji=None),
        limit=question_count
    )
    if not ids:
        return []

    words = list(Word.objects.filter(id__in=ids))

    questions = []

    for word in words:
        correct_kana = word.kana or ""
        if not correct_kana:
            continue

        part_of_speech_set = list(word.part_of_speech.all())

        # Суффикс каны (если kanji с фуриганой на конце)
        kana_suffix = ""
        if word.kanji and re.match(r'^[\u4e00-\u9fff]+', word.kanji):
            m = re.match(r'[\u4e00-\u9fff]+([\u3040-\u309f\u30a0-\u30ff]*)$', word.kanji)
            if m:
                kana_suffix = m.group(1) or ""

        # Пул для дистракторов
        all_kana_q = Word.objects.filter(~Q(kana=correct_kana)).exclude(kanji="''").exclude(kanji=None)
        if part_of_speech_set:
            all_kana_q = all_kana_q.filter(part_of_speech__in=part_of_speech_set)
        if kana_suffix:
            all_kana_q = all_kana_q.filter(kana__endswith=kana_suffix)

        # Без order_by('?')
        kana_pool = list(all_kana_q.values_list('kana', flat=True))
        if len(kana_pool) < 3:
            # fallback
            kana_pool = list(
                Word.objects.filter(~Q(kana=correct_kana)).values_list('kana', flat=True)
            )
        kana_pool = [k for k in kana_pool if k and k != correct_kana]
        kana_pool = _unique(kana_pool)
        if len(kana_pool) < 3:
            continue

        fake_kana = _shuffle_sample(kana_pool, 3)
        options = fake_kana + [correct_kana]
        random.shuffle(options)

        questions.append({
            'question_word': word.kanji,
            'options': options,
            'correct': correct_kana,
        })

    return questions

def generate_kana_to_kanji_questions(request, question_count, level):
    level = _normalize_level(level)

    total_possible = Word.objects.filter(
        level=level, kana__isnull=False, kanji__isnull=False
    ).exclude(kana="").exclude(kanji="''").exclude(kanji=None).count()
    qcap = min(MAX_QUESTIONS, total_possible or 0) or MAX_QUESTIONS
    question_count = _normalize_qcount(question_count, hard_cap=qcap)

    ids = _random_ids(
        Word.objects.filter(
            level=level,
            kana__isnull=False, kanji__isnull=False
        ).exclude(kana="''").exclude(kanji="''").exclude(kanji=None),
        limit=question_count
    )
    if not ids:
        return []

    words = list(Word.objects.filter(id__in=ids))

    questions = []

    for word in words:
        correct_kanji = word.kanji
        if not correct_kanji:
            continue

        part_of_speech_set = list(word.part_of_speech.all())

        kana_suffix = ""
        m = re.match(r'[\u4e00-\u9fff]+([\u3040-\u309f\u30a0-\u30ff]*)$', correct_kanji or "")
        if m:
            kana_suffix = m.group(1) or ""

        all_kanji_q = Word.objects.filter(~Q(kanji=correct_kanji)).exclude(kanji="''").exclude(kanji=None)
        if part_of_speech_set:
            all_kanji_q = all_kanji_q.filter(part_of_speech__in=part_of_speech_set)
        if kana_suffix:
            all_kanji_q = all_kanji_q.filter(kana__endswith=kana_suffix)

        cand = list(all_kanji_q.values_list('kanji', flat=True))
        if len(cand) < 3:
            cand = list(
                Word.objects.filter(~Q(kanji=correct_kanji)).values_list('kanji', flat=True)
            )
        cand = [x for x in cand if x and x != correct_kanji]
        cand = _unique(cand)
        if len(cand) < 3:
            continue

        fake_kanji = _shuffle_sample(cand, 3)
        options = fake_kanji + [correct_kanji]
        random.shuffle(options)

        questions.append({
            'question_word': word.kana,
            'options': options,
            'correct': correct_kanji,
        })

    return questions

def generate_kanji_to_trans_questions(request, question_count, level):
    level = _normalize_level(level)

    base_qs = Word.objects.annotate(pos_count=Count('part_of_speech')).filter(
        kanji__isnull=False,
        translate_ru__isnull=False,
        level=level,
        pos_count__gt=0
    ).exclude(kanji="").exclude(kanji=None)

    total_possible = base_qs.count()
    qcap = min(MAX_QUESTIONS, total_possible or 0) or MAX_QUESTIONS
    question_count = _normalize_qcount(question_count, hard_cap=qcap)

    ids = _random_ids(base_qs, limit=question_count)
    if not ids:
        return []

    words = list(Word.objects.filter(id__in=ids))

    questions = []

    for word in words:
        correct_trans = (word.translate_ru or "").strip()
        if not correct_trans:
            continue

        part_of_speech_set = list(word.part_of_speech.all())

        # другие переводы с совпадающими частями речи
        trans_q = Word.objects.filter(part_of_speech__in=part_of_speech_set).exclude(
            translate_ru__isnull=True
        ).exclude(
            translate_ru=""
        ).exclude(
            translate_ru=correct_trans
        ).values_list('translate_ru', flat=True)

        all_trans = _unique([t.strip() for t in list(trans_q) if t and t.strip()])
        if len(all_trans) < 3:
            # fallback на любые переводы
            fallback_q = Word.objects.exclude(
                translate_ru__isnull=True
            ).exclude(
                translate_ru=""
            ).exclude(
                translate_ru=correct_trans
            ).values_list('translate_ru', flat=True)

            all_trans = _unique([t.strip() for t in list(fallback_q) if t and t.strip()])

        if len(all_trans) < 3:
            continue

        fake_trans = _shuffle_sample(all_trans, 3)
        options = fake_trans + [correct_trans]
        random.shuffle(options)

        questions.append({
            'question_word': word.kanji,
            'options': options,
            'correct': correct_trans,
        })

    return questions

def generate_trans_to_kanji_questions(request, question_count, level):
    level = _normalize_level(level)

    base_qs = Word.objects.filter(
        translate_ru__isnull=False,
        kana__isnull=False,
        kanji__isnull=False,
        level=level
    ).exclude(translate_ru="''").exclude(kana="''").exclude(kanji="''").exclude(kanji=None)

    total_possible = base_qs.count()
    qcap = min(MAX_QUESTIONS, total_possible or 0) or MAX_QUESTIONS
    question_count = _normalize_qcount(question_count, hard_cap=qcap)

    ids = _random_ids(base_qs, limit=question_count)
    if not ids:
        return []

    words = list(Word.objects.filter(id__in=ids))

    questions = []

    # Пул для дистракторов (kanji_or_kana) без order_by('?')
    for word in words:
        correct_kanji = word.kanji if (word.kanji and word.kanji != "''") else (word.kana or "")
        if not correct_kanji:
            continue

        part_of_speech_set = list(word.part_of_speech.all())

        # Сформируем общий пул «kanji_or_kana»
        cand_q = (
            Word.objects.filter(part_of_speech__in=part_of_speech_set)
            .annotate(
                kanji_or_kana=Case(
                    When(kanji="''", then=F('kana')),
                    default=F('kanji')
                )
            )
            .exclude(kanji_or_kana=correct_kanji)
            .values_list('kanji_or_kana', flat=True)
        )

        pool = _unique([x for x in list(cand_q) if x and x != correct_kanji])
        if len(pool) < 3:
            continue

        fake_kanji = _shuffle_sample(pool, 3)
        options = fake_kanji + [correct_kanji]
        random.shuffle(options)

        questions.append({
            'question_word': word.translate_ru,
            'options': options,
            'correct': correct_kanji,
        })

    return questions

def hide_kanji_with_ruby(text, kanji):
    """
    Скрывает первое вхождение кандзи:
    - если кандзи внутри <ruby>...</ruby> — заменяет весь ruby-блок на ____
    - если кандзи вне ruby — заменяет только первое вхождение на ____
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
    # logger = logging.getLogger("kanji_sentence_test")
    # logger.setLevel(logging.INFO)
    # if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
    #     logger.addHandler(logging.StreamHandler())

    # --- кандзи уровня
    kanji_list = list(
        Kanji.objects.filter(level=level).values_list('kanji', flat=True)
    )
    # logger.info(f"=== Генерация kanji_sentence_test: level={level}, question_count={question_count}")
    # logger.info(f"Кандзи на уровне {level}: {kanji_list}")

    if not kanji_list:
        # logger.warning("Нет кандзи для выбранного уровня!")
        return []

    # question_count: поддержка "all"
    if isinstance(question_count, str) and question_count.strip().lower() == "all":
        need_questions = len(kanji_list)
    else:
        try:
            need_questions = int(question_count)
        except Exception as e:
        #     logger.error(f"Ошибка преобразования question_count: {question_count} — {e}")
            return []

    # --- кэш радикалов (1 SQL)
    radical_by_kanji = dict(
        Kanji.objects.filter(level=level).values_list('kanji', 'radical')
    )
    kanji_by_radical = defaultdict(list)
    for k, r in radical_by_kanji.items():
        if r:
            kanji_by_radical[r].append(k)

    # --- единый пул слов уровня с примерами (1 SQL) и индекс по кандзи
    candidate_words = list(
        Word.objects
        .filter(level=level)
        .exclude(examples__isnull=True)
        .exclude(examples='')
        .only('id', 'kanji', 'kana', 'examples')
    )

    words_by_kanji = defaultdict(list)
    # индексируем по каждому символу из поля Word.kanji
    level_kanji_set = set(kanji_list)
    for w in candidate_words:
        for ch in set((w.kanji or "")):  # set — чтобы не дублировать одинаковый символ
            if ch in level_kanji_set:
                words_by_kanji[ch].append(w)

    # равномерная попытка закрыть нужное количество вопросов
    pool = kanji_list[:]  # копия
    random.shuffle(pool)

    def pick_fake_kanji(correct_k: str, need: int = 3):
        radical = radical_by_kanji.get(correct_k)
        base = [x for x in kanji_by_radical.get(radical, []) if x != correct_k]
        if len(base) < need:
            extra = [x for x in kanji_list if x != correct_k and x not in base]
            random.shuffle(extra)
            base.extend(extra[: need - len(base)])
        return random.sample(base, need) if len(base) > need else base[:need]

    questions = []
    used_kanji = set()

    while pool and len(questions) < need_questions:
        k = pool.pop()
        if k in used_kanji:
            continue
        used_kanji.add(k)

        # logger.info(f"\n=== Проверяем кандзи: {k}")

        words_for_k = words_by_kanji.get(k, [])
        # logger.info(f"Количество Word с этим кандзи и примерами: {len(words_for_k)}")
        if not words_for_k:
        #     logger.warning(f"Нет слов с этим кандзи ({k}) на уровне {level}")
            continue

        random.shuffle(words_for_k)

        built = None  # сюда положим сформированный вопрос

        # попробуем до 5 разных слов/примеров для этого кандзи
        for w in words_for_k[:5]:
            ex_preview = (w.examples or '')[:80] + ('...' if w.examples and len(w.examples) > 80 else '')
            # logger.info(f"Слово-кандидат: {w.kanji} | kana: {w.kana} | examples: {ex_preview}")

            try:
                examples = json.loads(w.examples or '[]')
            except Exception as e:
                # logger.error(f"Ошибка JSON в examples для {w.kanji}: {e}")
                continue

            examples = [e for e in examples if isinstance(e, dict) and isinstance(e.get("jp"), str)]
            # logger.info(f"Примеров с ключом jp: {len(examples)}")
            if not examples:
                continue

            random.shuffle(examples)
            # найдём пример, где точно есть нужный кандзи
            ex = next((e for e in examples if k in e.get("jp", "")), None)
            if not ex:
                # logger.warning(f"В примерах слова {w.kanji} нет кандзи {k}")
                continue

            jp_text = ex["jp"]
            # logger.info(f"Выбранный пример: {jp_text[:80]}...")

            ruby_body, ruby_span = get_ruby_block(jp_text, k)
            options = []
            if ruby_body:
                question_word = jp_text[:ruby_span[0]] + ' ____ ' + jp_text[ruby_span[1]:]
                correct_variant = strip_ruby_tags(ruby_body)

                fakes = pick_fake_kanji(k, need=3)
                for fk in fakes:
                    fake_text = ruby_body.replace(k, fk, 1)
                    options.append(strip_ruby_tags(fake_text))
                options.append(correct_variant)
                random.shuffle(options)
            else:
                question_word = jp_text.replace(k, ' ____ ', 1)
                correct_variant = k
                fakes = pick_fake_kanji(k, need=3)
                options = fakes + [correct_variant]
                random.shuffle(options)

            # logger.info(f"Варианты ответа: {options} (правильный: {correct_variant})")

            built = {
                "question_word": question_word,
                "options": options,
                "correct": correct_variant,
                "kana": w.kana,
                "en": ex.get("en"),
                "ru": ex.get("ru"),
            }
            break  # вопрос собран

        if built:
            questions.append(built)

    # logger.info(f"\nИтого вопросов сгенерировано: {len(questions)}")
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
    # print('question_time', question_time,'  answers_time', answers_time)

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
        # print(f"test_type={test_type}, question_count={question_count}, level={level}")

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

# new pages

def _is_developer(u):
    return u.is_authenticated and (u.is_staff or u.is_superuser or u.groups.filter(name="dev").exists())

@login_required
@user_passes_test(_is_developer)
def dev_add_ksq(request):
    initial_parent = {
        "level": 5,
        "sentence_kanji": "には小さい頃から姉妹のように育った従姉妹がいる",
        "sentence_kana":  "たしにはちいさいころからしまいのようにそだったいとこがいる",
        "question_kanji": "小さい",
        "question_kana":  "ちいさい",
        "translation_en": "I have a cousin who I grew up with like a sister from a young age.",
        "translation_ru": "У меня есть двоюродная сестра, с которой я росла как с сестрой с самого детства.",
    }

    if request.method == "POST":
        form = KanjiSentenceQuestionForm(request.POST)
        formset = FakeFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            # Доп. проверка на уникальность/совпадение
            try:
                clean_fake_formset(formset, q_kanji=form.cleaned_data["question_kanji"])
            except Exception as e:
                formset._non_form_errors = formset.error_class([str(e)])  # аккуратно показать сверху
                messages.error(request, "Исправьте ошибки в фейковых вариантах.")
            else:
                parent = form.save(commit=False)
                if request.user.is_authenticated:
                    parent.created_by = request.user
                parent.save()
                formset.instance = parent
                formset.save()
                messages.success(request, "Задание добавлено.")
                return redirect("dev_add_ksq")
        else:
            messages.error(request, "Исправьте ошибки в форме.")
    else:
        form = KanjiSentenceQuestionForm(initial=initial_parent)
        formset = FakeFormSet()

    return render(request, "blog/dev_add_ksq.html", {"form": form, "formset": formset})