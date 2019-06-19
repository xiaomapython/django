#!/usr/bin/env python3
# -*- coding=utf-8 -*-
"""
---------------------------------------------------------
 @Time    : 2019/6/19 0:35
 @Author  : mjc
 @project : blog
 @File    : forms.py
 @Software: PyCharm
---------------------------------------------------------
"""
from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=6, max_length=10,
                               widget=forms.TextInput(attrs={"placeholder": "请输入用户名"}))
    # widget=forms.PasswordInput 表示这个文本框是密码
    password = forms.CharField(
        min_length=6, max_length=12,
        widget=forms.PasswordInput(attrs={"placeholder": "请输入密码"}),
        error_messages={
            "min_length": "密码小于6位",
            "max_length": "密码大于12位"
        }
    )
    password_repeat = forms.CharField(
        min_length=6, max_length=12, widget=forms.PasswordInput(
            attrs={"placeholder": "请再次输入密码"}
        ))
    email = forms.EmailField()
    

class LoginForm(forms.Form):
    username = forms.CharField(min_length=6, max_length=10,
                               widget=forms.TextInput(attrs={"placeholder": "请输入用户名"}))
    # widget=forms.PasswordInput 表示这个文本框是密码
    password = forms.CharField(min_length=6, max_length=12,
                               widget=forms.PasswordInput(attrs={"placeholder": "请输入密码"}))
    



