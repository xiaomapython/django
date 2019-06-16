#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re

from django import forms
from django.core.validators import RegexValidator
from django_redis import get_redis_connection
from django.db.models import Q
from django.contrib.auth import login

from verification.constants import SMS_CODE_NUMS
from .models import Users

# 创建手机号的正则校验器
# mobile_validator = RegexValidator(r"^1[3-9]\d{9}$", "手机号码格式不正确")


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20, min_length=5,
                               error_messages={"min_length": "用户名长度要大于5", "max_length": "用户名长度要小于20",
                                               "required": "用户名不能为空"}
                               )
    password = forms.CharField(label='密码', max_length=20, min_length=6,
                               error_messages={"min_length": "密码长度要大于6", "max_length": "密码长度要小于20",
                                               "required": "密码不能为空"}
                               )
    password_repeat = forms.CharField(label='确认密码', max_length=20, min_length=6,
                                      error_messages={"min_length": "密码长度要大于6", "max_length": "密码长度要小于20",
                                                      "required": "密码不能为空"}
                                      )
    mobile = forms.CharField(label='手机号', max_length=11, min_length=11,
                             error_messages={"min_length": "手机号长度有误", "max_length": "手机号长度有误",
                                             "required": "手机号不能为空"})

    sms_code = forms.CharField(label='短信验证码', max_length=SMS_CODE_NUMS, min_length=SMS_CODE_NUMS,
                               error_messages={"min_length": "短信验证码长度有误", "max_length": "短信验证码长度有误",
                                               "required": "短信验证码不能为空"})

    def clean_mobile(self):
        """
        """
        tel = self.cleaned_data.get('mobile')
        if not re.match(r"^1[3-9]\d{9}$", tel):
            raise forms.ValidationError("手机号码格式不正确")

        if Users.objects.filter(mobile=tel).exists():
            raise forms.ValidationError("手机号已注册，请重新输入！")

        return tel

    def clean(self):
        """
        """
        #
        cleaned_data = super().clean()
        passwd = cleaned_data.get('password')
        passwd_repeat = cleaned_data.get('password_repeat')

        if passwd != passwd_repeat:
            #
            raise forms.ValidationError("两次密码不一致")

        #
        tel = cleaned_data.get('mobile')
        sms_text = cleaned_data.get('sms_code')

        # 建立redis连接
        redis_conn = get_redis_connection(alias='verify_codes')
        #
        sms_fmt = "sms_{}".format(tel).encode('utf-8')
        #
        real_sms = redis_conn.get(sms_fmt)

        #
        if (not real_sms) or (sms_text != real_sms.decode('utf-8')):
            raise forms.ValidationError("短信验证码错误")


class LoginForm(forms.Form):
    user_account = forms.CharField()
    password = forms.CharField(label='密码', max_length=20, min_length=6,
                               error_messages={"min_length": "密码要大于6", "max_length": "密码要小于20"})
    
    remember_me = forms.BooleanField(required=False)
    
    def __init__(self, *args, **kwargs):
        self.request= kwargs.pop("request", None)
        super(LoginForm, self).__init__(*args, **kwargs)
        
    def clean_user_account(self):
        
        user_info = self.cleaned_data.get("user_account")
        
        if not user_info:
            raise forms.ValidationError("用户账号不能为空")

        if (not re.match(r"^1[3-9]\d{9}$", user_info)) \
                and (len(user_info) < 5) or (len(user_info) > 20):
            raise forms.ValidationError("用户账号格式不正确，请重新输入")
        
        return user_info
    
    def clean(self):
        # 联合校验，校验用户对应的密码是否正确
        clean_date= super().clean()
        user_info = clean_date.get("user_account")
        password = clean_date.get("password")
        hold_login = clean_date.get("remember_me")
        
        user_queryset = Users.objects.filter(Q(mobile=user_info) | Q(username=user_info))
        if user_queryset:
            user = user_queryset.first()
            # 继承AbstractUser自带check_password方法
            if user.check_password(password):
                if hold_login:
                    # expiry_time = 5 * 60   # 5分钟过期
                    self.request.session.set_expiry(None)
                else:
                    self.request.session.set_expiry(0)
                login(self.request, user)
            else:
                raise forms.ValidationError("密码不正确，请重新输入")
        else:
            raise forms.ValidationError("用户账号不存在，请重新输入")
        
        
        
        
        
        
