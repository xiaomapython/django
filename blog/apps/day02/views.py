from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template


def test_book(request):
    t = get_template('index.html')
    
    html = t.render()
    return HttpResponse(html)


def book_index(request):
    name = 'mjc'
    return render(request, 'index.html', context={'yourname': name})




