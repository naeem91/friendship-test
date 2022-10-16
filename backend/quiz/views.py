import random

from django.conf import settings
from rest_framework import generics, views, status
from rest_framework.response import Response

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
        qs_ans_map = self.request.data.get('questions')
        qids = [int(qid) for qid in qs_ans_map.keys()]
        qs = Question.objects.filter(active=True).filter(id__in=qids)
        qs_serializer = QuestionSerializer(qs, many=True)

        return serializer.save(
            questions=qs_serializer.data,
            answers=qs_ans_map
        )


class QuizDetailAPI(generics.RetrieveAPIView):
    queryset = Quiz.objects.filter(active=True)
    serializer_class = QuizSerializer
    lookup_field = 'link'


class QuizCheckAPI(views.APIView):
    def post(self, request, **kwargs):
        qs_ans_map = request.data.get('answers')
        link = kwargs.get('link')
        try:
            quiz = Quiz.objects.get(link=link)
        except Quiz.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        answers = quiz.answers
        correct = len([True for q,ans in qs_ans_map.items() if answers.get(q) == ans]) 

        if len(answers) <= 0:
            percentage = 0
        else:
            percentage = (100 / len(answers)) * correct

        res = {
            'total': len(answers),
            'correct': correct,
            'percentage': round(percentage, 2),
        }

        return Response(res, status=status.HTTP_200_OK)
