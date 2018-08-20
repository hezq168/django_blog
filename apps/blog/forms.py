#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/6 11:00
# @Author  : Hezq
# @Contact : Hezq168@gmail.com
# @File    : forms.py
# @Project : mysite
# @Software: PyCharm

from django import forms
from blog.models import Comments
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

from django.forms import fields as Ffields
from django.forms import widgets as Fwidgets


# class CommentsForm(forms.Form):
#     comment = RichTextField()


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        # fields = '__all__'
        fields = ['content']
        widgets = {
            'content': Fwidgets.Textarea(attrs={'class': 'form-control', 'rows': "3", 'cols': "20"})
        }
