from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 
# from .views import CreateWordView
# from .views import GrammarUpdateView

urlpatterns = [
    path('mainpanel/', views.mainpanel, name='mainpanel'), 
    path('', views.mainpanel, name='mainpanel'), 
    path('word/', views.word, name='word'),# Другие маршруты
    path('word_edit/<int:pk>/edit/', views.word_edit, name='word_edit'),# Другие маршруты
    path('word_create/', views.word_create, name='word_create'),# Другие маршруты
    path('word_variant_create/<int:pk>/add/', views.word_variant_create, name='word_variant_create'),# Другие маршруты
    path('word_detail/', views.word_detail_view, name='word_detail'),
    path('grammar/', views.grammar, name='grammar'),  # Имя пути 'about'
    path('grammar_create/', views.grammar_create, name='grammar_create'),# Другие маршруты
    path('grammar/<int:pk>/edit/', views.grammar_edit, name='grammar_edit'),
    path('kanji/', views.kanji, name='kanji'),# Другие маршруты
    path('kanji_create/', views.kanji_create, name='kanji_create'),# Другие маршруты
    path('kanji_edit/<int:pk>/edit/', views.kanji_edit, name='kanji_edit'),# Другие маршруты
    path('word_test/', views.word_test, name='word_test'),
    path('word_test_start/', views.word_test_start, name='word_test_start'),
    path('word_test_next/', views.word_test_next, name='word_test_next'),
    path('word_test_complete/', views.word_test_complete, name='word_test_complete'),
    path('word_test_premium/', views.word_test_premium, name='word_test_premium'),
    path("dev/add-ksq/", views.dev_add_ksq, name="dev_add_ksq"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)