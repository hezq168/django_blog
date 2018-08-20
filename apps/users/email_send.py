#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 15:08
# @Author  : Hezq
# @Contact : Hezq168@gmail.com
# @File    : email_send.py
# @Project : mysite
# @Software: PyCharm
from random import Random

from django.core.mail import send_mail

from users.models import VerifyCode

from mysite.settings import EMAIL_FROM


# 随机生成16位数的邮件验证码
def random_str(randomlength=16):
    str = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):
    email_record = VerifyCode()
    # 生成一个16位长的随机字符串
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == 'register':
        email_title = '注册激活链接'
        email_body = '点击下面的链接激活你的帐号 :http://127.0.0.1:8000/user/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = '找回密码链接'
        email_body = '点击下面的链接修改的帐号密码 :http://127.0.0.1:8000/user/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
