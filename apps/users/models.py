from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户信息表
    """
    nick_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='姓名', default='')
    birthday = models.DateField(verbose_name='出生年月', null=True, blank=True)
    gender = models.CharField(choices=(('male', '男'), ('female', "女")), default="male", verbose_name='性别', max_length=6)
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    email = models.EmailField(max_length=100, verbose_name='用户邮箱')
    photo = models.ImageField('头像', default='photo/default.jpg', upload_to='photo/%Y/%m/%d')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}{1}'.format(self.username, self.email)


class VerifyCode(models.Model):
    """
    邮箱验证码
    """
    code = models.CharField(max_length=16, verbose_name='验证码')
    email = models.EmailField(max_length=100, verbose_name='用户邮箱')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='日期')
    code_type = models.CharField(choices=(('reg', '注册'), ('reset', '找回密码')), max_length=10, default='reg',
                                 verbose_name='验证码类型')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}{1}'.format(self.code, self.email)
