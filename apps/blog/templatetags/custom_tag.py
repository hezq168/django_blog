#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 14:33
# @Author  : Hezq
# @Contact : Hezq168@gmail.com
# @File    : custom_tag.py
# @Project : mysite
# @Software: PyCharm
from django import template
from blog.models import Tag, Notice, Type

register = template.Library()


@register.simple_tag
def post_tag():
    """
    标签
    :return:
    """
    return Tag.objects.all()


@register.simple_tag
def post_notice():
    """
    公告
    :return:
    """
    return Notice.objects.all().first()


@register.simple_tag
def post_type():
    """
    分类
    :return:
    """
    return Type.objects.all()
