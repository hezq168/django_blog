from django.contrib import admin
from blog.models import Type, Post, Tag, Comments, Notice

# Register your models here.

# 管理后台title设置
admin.site.site_header = '后台管理'
admin.site.site_title = '后台'


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'content', 'blog_user', 'created_time')
    search_fields = ['content']




# @admin.register(BlogUser)
# class BlogUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'name', 'status')
#     search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'title', 'type', 'content', 'author', 'page_view', 'love', 'created_time')
    # 字段会被链接到mode的change页面
    list_display_links = ('id', 'title')

    # search_fields 搜索功能及能实现搜索的字段
    search_fields = ['title']
    # # list_editable设置默认可编辑字段
    # list_editable = ['title']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # # ordering设置默认排序字段，负号表示降序排序
    # ordering = ('-id',)

    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    # actions_on_top = True
    # actions_on_bottom = True
    # 操作项功能显示选中项的数目
    # actions_selection_counter = False
    # 字段为空值显示的内容
    # empty_value_display = '-空白-'
    # 过滤器功能及能过滤的字段
    list_filter = ('content', 'type')


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    search_fields = ['title']
