#!/usr/bin/env python3
# -*- coding=utf-8 -*-
"""
---------------------------------------------------------
 @Time    : 2019/6/19 18:22
 @Author  : mjc
 @project : blog
 @File    : mycontent.py
 @Software: PyCharm
---------------------------------------------------------
"""
from form.models import UserModel


def my_user(request):
    name = request.session.get("username", "游客")
    user = UserModel.objects.filter(username=name).first()
    
    if user:
        return {"username": user.username}
    else:
        return {"username": "没登录哦"}



