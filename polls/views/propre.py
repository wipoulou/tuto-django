from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from polls.models import Question, Choice
from polls.forms import QuestionForm


def list(request):
    questions = Question.objects.all()

    context = {
        'questions': questions,
        'form': QuestionForm(),
    }
    return render(request, 'polls/list.html', context)


def detail(request, id):
    question = Question.objects.get(id=id)

    context = {
        'question': question,
    }
    return render(request, 'polls/details.html', context)


def new_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Question ajoutée")
        else:
            messages.error(request, "Formulaire invalide")
    else:
        messages.error(request, "Formulaire non trouvé")
    return redirect('polls:list')


def result(request, id):
    question = Question.objects.get(id=id)
    choices = question.choices.all().order_by('-votes')
    choice_list = []
    for choice in choices:
        choice_list.append({
            'value': choice.choice_text,
            'count': choice.votes,
            'width': choice.votes / question.get_total() * 100,
        })

    context = {
        'question': question,
        'choices': choice_list,
    }
    return render(request, 'polls/results.html', context)
