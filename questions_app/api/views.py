from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.include.getquestions import get_and_save_questions
from api.serializers import QuestionNumSerializer, QuestionSerializer
from questions.models import Question


@api_view(['POST'])
def questions(request):
    last_question = Question.objects.last()
    serializer = QuestionNumSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    count: int = serializer.data['questions_num']
    url: str = f'{settings.ENDPOINT}{count}'
    get_and_save_questions(url)
    serializer = QuestionSerializer(last_question)
    return Response(serializer.data, status=status.HTTP_200_OK)
