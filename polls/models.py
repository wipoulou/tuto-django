from django.db import models
from django.shortcuts import reverse


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.question_text}'

    def get_absolute_url(self):
        return reverse("polls:detail", kwargs={"id": self.pk})

    def get_total(self):
        count = 0
        for choice in self.choices.all():
            count += choice.votes
        return count


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices"
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.choice_text}'
