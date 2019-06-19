from django.http import HttpResponse
from django.shortcuts import render

import datetime


def post_test(request):
    if request.method == "GET":
        print(request.path)
        return render(request, "get_post/post.html")
    elif request.method == "POST":
        print(request.POST)
        print(request.path)
        a = request.POST.get("a")
        b = request.POST.get("b")
        x = a + b
        return HttpResponse(x)


def get_req(request):
    print(request.GET)
    a = request.GET.get("a")
    b = request.GET.get("b")
    print(a)
    print(b)
    return render(request, "get_post/get.html")


def get_test(request):
    print(request.GET)
    a = request.GET.getlist("a")
    print(a)
    return render(request, "get_post/get_test.html")


def set_ck(request):
    response = HttpResponse("设置cookie")
    # response.set_cookie("name", "taka")  # 默认浏览器关闭过期
    # response.set_cookie("name", "taka", expires=120)  # 200秒过期
    # 设置到未来某一天过期
    # response.set_cookie("name", "taka", expires=datetime.datetime(2019, 10, 18))
    response.set_signed_cookie("name", "taka", salt="salt", expires=datetime.datetime(2019, 10, 18))
    return response


def get_ck(request):
    cookie = request.COOKIES
    print(cookie)
    response = HttpResponse(cookie.get("name"))
    return response


def delete_ck(request):
    response = HttpResponse("cookie已删除")
    response.delete_cookie("name")
    return response
























