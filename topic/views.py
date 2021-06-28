from random import randint, random

import requests
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets


from topic.models import Theme, Question, Answer
from topic.serializers import ThemeSerializer, QuestionSerializer, AnswerSerializer, QuestionRandomSerializer

""" random.randint(int - минимальное, int - максимальное) """

"""def question_random(request):
    a = Question.objects.count()
    random_index = randint(0, a-1)
    random_question = Question.objects.all().values('question_text')[random_index]
    #return JsonResponse(random_question, safe=False)
    return Response(random_question, content_type='application/json')"""
"""def question_random(model, max_id=None):
    random_idx = randint(0, Question.objects.count() - 1)
    random_obj = Question.objects.all()[random_idx]
    qs_json = serializers.serialize('json', random_obj)
    return JsonResponse(qs_json, )
    return HttpResponse(qs_json, content_type='application/json')"""


class QuestionRandom(viewsets.ModelViewSet):
    queryset = Question.objects.order_by('?')
    serializer_class = QuestionRandomSerializer(queryset, many=False)


def index(request):
    return HttpResponse()


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.order_by('theme_id')
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.order_by('question_id')
    serializer_class = AnswerSerializer

