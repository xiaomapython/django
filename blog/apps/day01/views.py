from django.shortcuts import render, redirect, reverse

from django.http import HttpResponse


def article(request):
    # return HttpResponse('这是article老的页面')
    return redirect(reverse('new'))


def article_new(request):
    return HttpResponse('这是article新的页面')



