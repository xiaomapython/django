from django.shortcuts import render


import datetime

str_tmp = 'I Love Python!'
list_tmp = ['abc', 12, 89, 'mjc']
float_tmp = 3.141526926


def index(request):
    return render(request, 'book/index.html', context={
        'str': str_tmp,
        'list': list_tmp,
        'html': '<h1>hello django!</h1>',
        'float': float_tmp,
        # 在模板中调用 {{ now() }}
        'now': datetime.datetime.now,
        'num1': 12,
        'num2': 13,
        'num3': 60,
        'num4': None,
        'format_string': '%Y-%m-%d %H:%M:%S',
    })


def static_test(request):
    return render(request, 'book/static_test.html')

