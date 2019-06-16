import json

from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import login as _login, logout

from utils.json_fun import to_json_data
from utils.res_code import Code, error_map
from .forms import RegisterForm, LoginForm
from .models import Users


def login(request):
    return render(request, "users/login.html")


def register(request):
    return render(request, "users/register.html")


class RegisterView(View):
    """
    user register
    url: /users/register/
    """
    def get(self, request):
        return render(request, "users/register.html")

    """
    user login
    """
    def post(self, request):
        # 1、获取前端传过来的数据
        json_data = request.body
        print(json_data)
        if not json_data:
            return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])
        # 将json转化为dict
        dict_data = json.loads(json_data.decode('utf8'))
        # 2、校验
        form = RegisterForm(data=dict_data)
        if form.is_valid():
            # 3、保存数据
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            mobile = form.cleaned_data.get("mobile")

            user = Users.objects.create_user(username=username, password=password, mobile=mobile)
            # user.mobile = mobile
            # user.save()
            # 登录进去，登录到哪里呢
            _login(request, user)
            # 4、返回给前端
            return to_json_data(errmsg="恭喜你,注册成功！")
        else:
            # 定义一个错误信息列表
            err_msg_list = []
            for item in form.errors.get_json_data().values():
                err_msg_list.append(item[0].get('message'))
                # print(item[0].get('message'))   # for test
            err_msg_str = '/'.join(err_msg_list)  # 拼接错误信息为一个字符串

            return to_json_data(errno=Code.PARAMERR, errmsg=err_msg_str)


class LoginView(View):

    def get(self, request):
        return render(request, "users/login.html")

    def post(self, request):
        # 获取前端json参数
        json_data = request.body
        print(json_data)
        if not json_data:
            return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])
        # 将json转化为dict
        dict_data = json.loads(json_data.decode('utf8'))

        # 校验参数
        form = LoginForm(data=dict_data, request=request)
        
        if form.is_valid():
            return to_json_data(errmsg=">恭喜你登录成功<")
        else:
            # 定义一个错误信息列表
            err_msg_list = []
            for item in form.errors.get_json_data().values():
                err_msg_list.append(item[0].get('message'))
                # print(item[0].get('message'))   # for test
            err_msg_str = '/'.join(err_msg_list)  # 拼接错误信息为一个字符串
            return to_json_data(errno=Code.PARAMERR, errmsg=err_msg_str)
        # 登录

        # 返回前端json格式的数据
        
    
class LogoutView(View):
    """
    log out view
    /users/logout
    """
    def get(self, request):
        logout(request)
        return redirect(reverse("users:users_login"))
    
        



