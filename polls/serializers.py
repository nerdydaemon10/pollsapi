from rest_framework import serializers
from .models import Question, Choice

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["text", "created_at", "updated_at"]


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["text", "votes", "created_at", "updated_at"]