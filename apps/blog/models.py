from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import UserProfile
import django.utils.timezone as timezone


# 博客分类
class Type(models.Model):
    name = models.CharField(max_length=16, verbose_name='分类')
    keywords = models.CharField(max_length=32, verbose_name='关键字', null=True)
    description = models.CharField(max_length=64, verbose_name='描述', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = "博客分类"


# 博客标签
class Tag(models.Model):
    name = models.CharField('标签', max_length=32)
    keywords = models.CharField(max_length=32, verbose_name='关键字', null=True)
    description = models.CharField(max_length=64, verbose_name='描述', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客标签'
        verbose_name_plural = "博客标签"


# 博客文章
class Post(models.Model):
    title = models.CharField(max_length=32, verbose_name='标题')
    # 博客分类 一对多
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, verbose_name='分类')
    content = RichTextUploadingField(verbose_name='内容')
    author = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, verbose_name='作者')
    page_view = models.IntegerField(verbose_name='阅读数', default=0)
    cover = models.ImageField('封面', default='cover/default.jpg', upload_to='cover/%Y/%m/%d')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # 博客标签 多对多关系
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    keywords = models.CharField(max_length=32, verbose_name='关键字', null=True)
    description = models.CharField(max_length=64, verbose_name='描述', null=True)

    def __str__(self):
        return '<Blog: %s>' % self.title

    class Meta:
        verbose_name = "博客文章"
        verbose_name_plural = "博客文章"
        ordering = ['-id']


# 博客评论
class Comments(models.Model):
    content = RichTextUploadingField(verbose_name='评论内容', config_name='default')
    # 多对一
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, verbose_name='博客文章')
    created_time = models.DateTimeField(default=timezone.now, verbose_name='评论时间')
    blog_user = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, verbose_name='评论用户', default=1)
    is_reply = models.IntegerField(verbose_name='回复', default=0)
    is_show = models.BooleanField(verbose_name='显示', default=False)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '博客评论'
        verbose_name_plural = "博客评论"
        ordering = ['-id']


# 网站公告
class Notice(models.Model):
    title = models.CharField(max_length=64)
    content = RichTextUploadingField(verbose_name='内容')
    keywords = models.CharField(max_length=32, verbose_name='关键字', null=True)
    description = models.CharField(max_length=64, verbose_name='描述', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '网站公告'
        verbose_name_plural = "网站公告"
        ordering = ['-id']


# 关注
class Stars(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, verbose_name='关注文章')
    user = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, verbose_name='作者')
