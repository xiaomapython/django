from django.shortcuts import render

list_temp = [12, 26, 98, 78]


def template_test(request):
    return render(request, 'music/templates_test.html', context={
        'list': list_temp,
        'html': '<h2>很爱很爱你</h2>'
    })


def to_template_test(request):
    return render(request, 'music/url_test.html')


def jichneg_test(request):
    return render(request, 'music/index.html')
