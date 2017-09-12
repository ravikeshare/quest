from quest.qa.models import Question, Answer
from quest.tenant.models import Tenant
from quest.user.models import User


def contextprocessor(request):

    ctx = dict()
    ctx['user_count'] = User.objects.count()
    ctx['question_count'] = Question.objects.count()
    ctx['answer_count'] = Answer.objects.count()
    ctx['tenants'] = Tenant.access_count()

    return ctx
