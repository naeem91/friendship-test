import uuid
import random
import string
import secrets

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

    def perform_create(self, serializer):
        link_generated = False

        # try to generate a unique short link first (9 alphabets only)
        # but if they haven been exausted then fallback to uuid 
        for _ in range(5):
            link = self._generate_link()
            try:
                serializer.save(link=link)
                link_generated = True
            except Exception:
                continue
            else:
                break
    
        if not link_generated:
            link = str(uuid.uuid4()) 
            serializer.save(link=link)
        
    def _generate_link(self):
        """
        Generate a short, easy to type link
        e.g, xjv-jho-lqm
        """
        link_length = settings.RANDOM_LINK_LENGTH
        char_set = string.ascii_lowercase 

        random_chars = []
        for i in range(1, link_length + 1):
            char = secrets.choice(char_set)
            if i%3 == 0 and i < link_length:
                char += '-'
            random_chars.append(char)
        
        return ''.join(random_chars)


class QuizDetailAPI(generics.RetrieveAPIView):
    queryset = Quiz.objects.filter(active=True)
    serializer_class = QuizSerializer
    lookup_field = 'link'
