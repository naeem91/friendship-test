from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quiz import views

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/questions', views.QuestionListAPI.as_view(), name='questions'),
    path('api/quiz', views.QuizCreateAPI.as_view(), name='quiz_create'),
    path('api/quiz/<str:link>', views.QuizDetailAPI.as_view(), name='quiz_detail'),
]
