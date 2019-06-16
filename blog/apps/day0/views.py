from django.http import HttpResponse


def hello(request):
    return HttpResponse('你好，django！')


def hello_mjc(request):
    return HttpResponse('你好，mjc！')


def hello_everyone(request, name):
    return HttpResponse('你好，%s' % name)


def hello_every(request, name, age):
    return HttpResponse('你好，%s, 我今年%s' % (name, age))


def hello_kwargs(request, **kwargs):
    print(kwargs)
    return HttpResponse('你好，%s' % kwargs.get('name'))

