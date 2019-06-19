#!/usr/bin/env python3
# -*- coding=utf-8 -*-
"""
---------------------------------------------------------
 @Time    : 2019/6/19 16:04
 @Author  : mjc
 @project : blog
 @File    : mymiddleware.py
 @Software: PyCharm
---------------------------------------------------------
"""
from django.utils.deprecation import MiddlewareMixin

from django.http import HttpResponse

from form.models import UserModel


# 自定义异常
class MyException(MiddlewareMixin):
    
    def process_exception(self, request, exception):
        print("自定义异常处理")
        return HttpResponse(exception)


# 为 request增加属性
class UserMiddleWare:
    def __init__(self, get_request):
        self.get_response = get_request
    
    def __call__(self, request):
        username = request.session.get("username", "游客")
        user = UserModel.objects.filter(username=username)
        if user:
            setattr(request, "myuser", user[0].username)  # 为request定义属性
        else:
            setattr(request, "myuser", "未登录")
        
        # 上面是request到达视图之前
        response = self.get_response(request)
        
        # 下面部分，就是response到达浏览器执行的
        return response
            

