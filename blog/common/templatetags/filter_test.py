#!/usr/bin/env python3
# -*- coding=utf-8 -*-
"""
---------------------------------------------------------
 @Time    : 2019/5/21 14:07
 @Author  : mjc
 @project : blog
 @File    : filter_test.py
 @Software: PyCharm
---------------------------------------------------------
"""
from django import template

register = template.Library()  # 变量名是固定的，必须是register


# 自定义过滤器在day03中使用
@register.filter
def my_lower(value):
    return value.lower()


# register.filter(my_lower)

# 自定义过滤器在day03中使用
@register.filter
def my_cut(value, arg):
    return value.replace(arg, "")


import datetime


# 自定义标签
@register.simple_tag
def current_time1(format_string):
    return datetime.datetime.now().strftime(format_string)


# 自定义标签
@register.simple_tag(takes_context=True)
def current_time2(context):
    format_string = context.get('format_string')
    return datetime.datetime.now().strftime(format_string)


