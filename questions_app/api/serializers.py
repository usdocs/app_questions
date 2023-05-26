from rest_framework import serializers

from questions.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question',)


class QuestionNumSerializer(serializers.Serializer):
    questions_num = serializers.IntegerField()


class QuestionSaveSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_question')

    class Meta:
        model = Question
        fields = ('id', 'question', 'answer', 'created_at')
