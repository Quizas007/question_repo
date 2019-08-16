from django.shortcuts import HttpResponse,render
import logging
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from apps.repo.models import Questions

# apis为settings中Logging配置中的loggers
logger = logging.getLogger('apis')


def logtest(request):
    logger.info("欢迎访问")
    return HttpResponse('日志测试')

@login_required()
def index(request):
    return render(request,"index.html")

# 测试paginator
def test(request):
    question_list = Questions.objects.all()
    paginator = Paginator(question_list,10)
    page = request.GET.get('page')
    questions = paginator.page(page)
    return render(request,'list.html',{'questions':questions})