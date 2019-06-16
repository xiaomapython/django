from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as _UserManager


class UserManager(_UserManager):
    def create_superuser(self, username,  password, email=None, **extra_fields):
        super(UserManager, self).create_superuser(username=username,  password=password, email=email, **extra_fields)

        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        #
        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')
        #
        # return self._create_user(username, password, email=email, **extra_fields)


# 生成数据库的名字默认为：应用名+class名字
class Users(AbstractUser):
    # verbose_name会在admin后台站点显示为中文手机号，error_messages对unique字段的错误提示
    # 新加字段，但是超级用户不会使用该字段
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号', help_text='手机号', error_messages={'unique': '此手机号已注册'})

    email_active = models.BooleanField(default=False, verbose_name='邮箱验证状态')
    # 指定超级用户需要的字段，具体参考User源码
    # REQUIRED_FIELDS = ['email', 'mobile']
    REQUIRED_FIELDS = ['mobile']

    objects = UserManager()

    class Meta:
        # 数据库表明默认为：users_users
        db_table = "tb_users"
        verbose_name = "用户"
        # 复数
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username
