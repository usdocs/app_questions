from http import HTTPStatus

import requests
from django.conf import settings

from api.serializers import QuestionSaveSerializer
from questions.models import Question


def get_api_answer(url: str) -> list:
    """Делает запрос к эндпоинту API-сервиса."""
    try:
        questions_list = requests.get(url)
    except Exception as error:
        raise Exception(f'Ошибка при запросе к публичному API: {error}')
    if questions_list.status_code != HTTPStatus.OK:
        raise Exception('публичный API возвращает код, отличный от 200')
    return questions_list.json()


def check_response(response: list) -> list:
    """Проверяем ответ API на соответствие документации."""
    if not isinstance(response, list):
        raise TypeError('Ошибка в типе данных')
    for question in response:
        if not isinstance(question, dict):
            raise TypeError('Ошибка в типе данных')
        if 'id' not in question:
            raise Exception('В ответе нет данных id')
        if 'question' not in question:
            raise Exception('В ответе нет данных question')
        if 'answer' not in question:
            raise Exception('В ответе нет данных answer')
        if 'created_at' not in question:
            raise Exception('В ответе нет данных created_at')
    return response


def get_and_save_questions(url: str) -> None:
    response: list = get_api_answer(url)
    questions_list: list = check_response(response)
    for question in questions_list:
        while Question.objects.filter(id_question=question['id']).exists():
            response: list = get_api_answer(settings.ENDPOINT)
            questions_list: list = check_response(response)
            question: dict = questions_list[0]
        serializer = QuestionSaveSerializer(data=question)
        serializer.is_valid(raise_exception=True)
        serializer.save()
