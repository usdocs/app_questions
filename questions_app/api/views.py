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
    url: str = f'{settings.ENDPOINT[:-1]}{count}'
    try:
        get_and_save_questions(url)
    except Exception as error:
        message = f'Сбой в работе программы: {error}'
        return Response(
            message,
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )
    serializer = QuestionSerializer(last_question)
    return Response(serializer.data, status=status.HTTP_200_OK)
