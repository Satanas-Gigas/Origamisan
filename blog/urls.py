from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
# from .views import GrammarUpdateView

urlpatterns = [
    path('', views.mainpanel, name='mainpanel'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('grammar/', views.grammar, name='grammar'),  # Имя пути 'about'
    path('mainpanel/', views.mainpanel, name='mainpanel'),  # Имя пути 'about'
    path('create_grammar/', views.create_grammar, name='create_grammar'),# Другие маршруты
    path('create_word/', views.create_word, name='create_word'),# Другие маршруты
    path('word/', views.word, name='word'),# Другие маршруты
    path('kanji/', views.kanji, name='kanji'),# Другие маршруты
    path('grammar/<int:pk>/edit/', views.grammar_edit, name='grammar_edit'),
    path('kanji_create/', views.kanji_create, name='kanji_create'),# Другие маршруты
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)