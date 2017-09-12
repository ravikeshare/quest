from django.test import TestCase
from .models import Question, Answer, User


class QuestionAnswerTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        user = User.objects.create(name='test')
        question = Question.objects.create(title='q1', private=False, user=user, )
        Answer.objects.create(body='a1', question=question, user=user, )

    def test_question(self):
        question = Question.objects.get(title='q1')
        self.assertIsNotNone(question)

    def test_answer(self):
        answer = Answer.objects.get(body='a1')
        self.assertIsNotNone(answer)
