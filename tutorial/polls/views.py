from django.shortcuts import render, redirect

# Create your views here.
from polls.models import Question, Choice


def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)


def question_detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    context = {
        'question': question
    }
    return render(request, 'polls/question.html', context)

