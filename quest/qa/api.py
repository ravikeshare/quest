from rest_framework import viewsets
from .serializers import QuestionSerializer
from .models import Question, Answer


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter(private=False)
