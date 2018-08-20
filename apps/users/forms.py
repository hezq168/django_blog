#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 09:18
# @Author  : Hezq
# @Contact : Hezq168@gmail.com
# @File    : forms.py
# @Project : mysite
# @Software: PyCharm

from django import forms
from django.forms import widgets


# 登录form
class LoginForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'required': '邮箱不能为空'},
                             widget=widgets.EmailInput(attrs={'class': "form-control"}))
    pwd = forms.CharField(required=True, min_length=5, error_messages={'required': '密码不能为空!',
                                                                       'min_length': '密码小于5位！'},
                          widget=widgets.PasswordInput(attrs={'class': "form-control"}))
    code = forms.CharField(required=True, min_length=4, error_messages={'required': '验证码不能为空!',
                                                                        'min_length': '验证码不能小于4位！'},
                           widget=widgets.TextInput(attrs={'class': "form-control", 'placeholder': '请输入验证码'}))


# 注册form
class RegisterForm(forms.Form):
    nick_name = forms.CharField(required=True, error_messages={'required': '昵称不能为空'},
                                widget=widgets.EmailInput(attrs={'class': "form-control"}))
    email = forms.EmailField(required=True, error_messages={'required': '邮箱不能为空'},
                             widget=widgets.EmailInput(attrs={'class': "form-control"}))
    pwd = forms.CharField(required=True, min_length=5, error_messages={'required': '密码不能为空!',
                                                                       'min_length': '密码小于5位！'},
                          widget=widgets.PasswordInput(attrs={'class': "form-control"}))
    code = forms.CharField(required=True, min_length=4, error_messages={'required': '验证码不能为空!',
                                                                        'min_length': '验证码不能小于4位！'},
                           widget=widgets.TextInput(attrs={'class': "form-control", 'placeholder': '请输入验证码'}))
