from django.db import models
from quest.user.models import User


class Question(models.Model):
    title = models.CharField(max_length=1000)
    private = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='questions')

    def __str__(self):
        return self.title


class Answer(models.Model):
    body = models.CharField(max_length=2000)
    question = models.ForeignKey(Question, related_name='answers')
    user = models.ForeignKey(User, related_name='answers')

    def __str__(self):
        return self.body
