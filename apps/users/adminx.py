#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/6 10:23
# @Author  : Hezq
# @Contact : Hezq168@gmail.com
# @File    : adminx.py
# @Project : mysite
# @Software: PyCharm

import xadmin
from xadmin import views

from .models import VerifyCode


# xadmin全局配置
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '博客管理系统'
    site_footer = '博客管理系统'
    # 菜单收缩
    # menu_style = 'accordion'


class VerifyCodeAdmin(object):
    # 显示字段
    list_display = ['id', 'code', 'email', 'code_type', 'add_time']
    # 搜索
    search_fields = ['code', 'email']
    # 过滤器
    list_filter = ['code', 'email', 'code_type', 'add_time']


xadmin.site.register(VerifyCode, VerifyCodeAdmin)

# xadmin全局配置
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
