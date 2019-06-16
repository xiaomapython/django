#!/usr/bin/env python3
# -*- coding=utf-8 -*-
"""
---------------------------------------------------------
 @Time    : 2019/6/8 0:41
 @Author  : mjc
 @project : happy_django
 @File    : conn.py
 @Software: PyCharm
---------------------------------------------------------
"""
import pymysql as MySQLdb

# change root password to yours:
conn = MySQLdb.connect(host='127.0.0.1', user='root', password='123456', database='happy_django')




