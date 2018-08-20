#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 13:57
# @Author  : Hezq
# @Contact : Hezq168@gmail.com
# @File    : urls.py
# @Project : mysite
# @Software: PyCharm


from django.urls import path
from blog import views as blog_views

urlpatterns = [
    # 博客首页
    path('', blog_views.index, name='blog_index'),
    # 博客文章页
    path('post/<int:id>', blog_views.post, name='blog_post'),
    # 博客类别
    path('category/<int:_id>', blog_views.Category.as_view(), name='blog_category'),
    # 博客标签
    path('tag/<int:_id>', blog_views.TagView.as_view(), name='blog_tag'),
    # 博客公告
    path('notice/<int:_id>', blog_views.NoticeView.as_view(), name='blog_notice'),
    #
    path('comment', blog_views.CommentView.as_view(), name='blog_comment')
]