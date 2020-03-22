from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('list', views.list, name="list"),
    path('new-question', views.new_question, name="new-question"),
    path('add-vote', views.add_vote, name="vote"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('detail/<int:id>/resultat', views.result, name="results"),
]
