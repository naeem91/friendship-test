import random

from django.conf import settings
from rest_framework import generics

from .models import Question, Quiz
from .serializers import QuestionSerializer, QuizSerializer


class QuestionListAPI(generics.ListCreateAPIView):
    """
    API endpoint that allows users to create and view questions
    """
    queryset = Question.objects.filter(active=True)
    serializer_class = QuestionSerializer

    def get_queryset(self):
        qs = super().get_queryset() 
        sample_size = settings.QUIZ_SIZE

        # get random quesions by selecting random ids within the range of
        # max id. Get 5x more ids to avoid holes in ids
        question_count = qs.all().count()

        # not enough data to select N random questions
        if question_count <= sample_size:
            return qs
        elif question_count > sample_size * 5:
            sample_size = sample_size * 5

        rand_ids = random.sample(range(1, question_count + 1), sample_size)
        return qs.filter(id__in=rand_ids)[:settings.QUIZ_SIZE]
    

class QuizCreateAPI(generics.CreateAPIView):
    queryset = Quiz.objects.filter(active=True)
    serializer_class = QuizSerializer


class QuizDetailAPI(generics.RetrieveAPIView):
    queryset = Quiz.objects.filter(active=True)
    serializer_class = QuizSerializer
    lookup_field = 'link'
