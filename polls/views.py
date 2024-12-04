from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from polls.models import Question
from polls.serializers import QuestionSerializer

# Create your views here.
class PollsListApiView(APIView):
    def get(self, request, *args, **kwargs):
        questions = get_list_or_404(Question)
        serializer = QuestionSerializer(questions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'text': request.data.get('text')
        }

        serializer = QuestionSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PollsDetailApiView(APIView):        
    def get(self, request, pk, format=None):
        question = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    
    def get(self, request, pk, format=None):
        question = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    
    def was_created_recently(self, request, pk, format=None):
        question = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(question.was_created_recently())
        return Response(serializer.data)