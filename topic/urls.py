from django.urls import path, include
from rest_framework import routers

from topic import views

router = routers.DefaultRouter()
router.register(r'themes', views.ThemeViewSet, basename='themes')
router.register(r'questions', views.QuestionViewSet, basename='questions')
router.register(r'question/rand', views.QuestionRandom, basename='question-rand')

urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.index, name='index'),
    #path('question/rand/', views.question_random, name='question_random'),
]