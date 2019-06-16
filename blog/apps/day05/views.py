from django.http import HttpResponse
from .models import F_test


def f_test(request):
    # F_test.objects.get_or_create(name='小明', age=18)
    
    f1 = F_test.objects.get(id=3)
    f1.name = '亮亮'
    f1.save()
    return HttpResponse('添加成功！')
