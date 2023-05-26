from django.db import models


class Question(models.Model):
    id_question = models.IntegerField(
        'ID вопроса',
        unique=True,
    )
    question = models.TextField(
        'Текст вопроса',
    )
    answer = models.TextField(
        'Текст ответа',
    )
    created_at = models.DateTimeField(
        'Дата создания вопроса',
    )

    def __str__(self):
        return self.question
