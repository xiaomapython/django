from django.db import models


class F_test(models.Model):
    name = models.CharField(max_length=30, unique=True)
    age = models.IntegerField()
    note = models.TextField(null=True)
    gender = models.BooleanField(default=True)
    create_time = models.DateField(auto_now_add=True)
    # 必须使用save()方法才能实现时间的更新
    update_time = models.DateTimeField(auto_now=True)
