from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError

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


def vote(request, question_pk):
    if request.method == 'POST':
        try:
            question = Question.objects.get(pk=question_pk)
        except Question.DoesNotExist:
            return redirect('index')

        try:
            choice_pk = request.POST.get('vote')
            choice = Choice.objects.get(pk=choice_pk)
            choice.votes += 1
            choice.save()
        except MultiValueDictKeyError:
            pass
        except Choice.DoesNotExist:
            pass
        return redirect('question_detail', question_pk=question.pk)
    else:
        return HttpResponse('Permission denied', status=403)
