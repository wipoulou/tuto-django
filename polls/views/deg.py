from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from polls.models import Question, Choice


def new_choice(request):
    id_question = request.POST['question_id']
    choice = request.POST['new_choice']

    Choice.objects.create(
        question=Question.objects.get(id=id_question),
        choice_text=choice
    )
    return redirect('polls:detail', id_question)


def add_vote(request):
    if request.method == 'POST':
        id_question = request.POST['question_id']
        id_choice = request.POST['choice_id']
        if request.POST['new_choice']:
            return new_choice(request)
        if id_choice and id_question:
            response = redirect('polls:detail', id_question)
            if request.COOKIES.get("vote_" + id_question) is None:
                choice = Choice.objects.get(id=id_choice)
                choice.votes += 1
                choice.save()
                response.set_cookie("vote_" + str(id_question), "Voted")
                messages.success(request, "Vote comptabilisé")
            else:
                messages.warning(request, "T'a déjà voté FDP (- kenji)")
            return response
    messages.error(request, "Erreur de formulaire")
    return redirect('polls:list')
