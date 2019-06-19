from django.shortcuts import render, redirect, reverse

# Create your views here.


def home(request):
    username = request.session.get("username", "游客")
    return render(request, "form_test/home.html", context={"name": username})


def login_test(request):
    if request.method == "GET":
        return render(request, "form_test/login_test.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        # 使用request 设置session
        request.session["username"] = username
        return redirect(reverse("home"))


def logout_test(request):
    request.session.flush()
    return redirect(reverse("home"))

