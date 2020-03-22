from django.forms import ModelForm
from polls.models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
