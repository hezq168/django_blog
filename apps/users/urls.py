#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/6 10:19
# @Author  : Hezq
# @Contact : Hezq168@gmail.com
# @File    : urls.py
# @Project : mysite
# @Software: PyCharm
from django.urls import path

from users.views import Register, UserLogin, check_code, UserLogout, ActiveUserView

urlpatterns = [
    # path('', InfoView.as_view(), name='user_info'),
    path('register', Register.as_view(), name='register'),
    path('login', UserLogin.as_view(), name='login'),
    path('logout', UserLogout, name='logout'),
    path('check_code', check_code, name='check_code'),
    path('active/<str:active_code>', ActiveUserView.as_view(), name='active'),
]
