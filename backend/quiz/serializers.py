from rest_framework import serializers

from .models import Question, Choice, Quiz


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'choices']
    
    def create(self, validated_data):
        choices = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)

        for choice in choices:
            Choice.objects.create(question=question, **choice)
        
        return question


class QuizSerializer(serializers.ModelSerializer):
    quiz_link = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ['id', 'creator', 'questions', 'quiz_link']

    def get_quiz_link(self, quiz):
        return quiz.link
