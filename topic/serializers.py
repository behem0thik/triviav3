from rest_framework import serializers

from topic.models import Theme, Question, Answer


class ThemeSerializer(serializers.ModelSerializer):
    questions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Theme
        fields = ['theme_text', 'id', 'questions']


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = ['question_text', 'theme_id', 'pub_date', 'answers']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer_text']


class QuestionRandomSerializer(serializers.ModelSerializer):
    def __call__(self, *args, **kwargs):
        return self.context

    class Meta:
        model = Question
        fields = ['question_text', 'id']
