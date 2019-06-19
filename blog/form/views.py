from django.shortcuts import render, redirect, reverse
from django.contrib.auth.hashers import make_password, check_password

from .forms import LoginForm, RegisterForm
from .models import User


def register_test(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "form/register.html", context={"form": form})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            password_repeat = form.cleaned_data.get("password_repeat")
            email = form.cleaned_data.get("email")
            if password == password_repeat:
                password = make_password(password)  # 对密码进行加密
                User.objects.get_or_create(username=username, password=password, email=email)
                return redirect(reverse("form:login_form"))
            else:
                return render(request, "form/register.html",
                              context={"form": form, "error": "两次输入密码不一致，请重新输入"})
        else:
            # return redirect(reverse("form:reg_form"))
            return render(request, "form/register.html", context={"form": form, "error": form.errors})


def login_test(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "form/login.html", context={"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = User.objects.filter(username=username)
            if user:
                if check_password(password, user[0].password):
                    request.session["username"] = username
                    return render(request, "form/home.html", context={"name": username})
                else:
                    return render(
                        request, "form/login.html",
                        context={"form": form, "error": "请输入正确的密码"}
                    )
            else:
                return render(
                    request, "form/login.html",
                    context={"form": form, "error": "该用户不存在"}
                )
        else:
            return render(
                request, "form/login.html",
                context={"form": form, "error": "请确认账户或密码"}
            )


