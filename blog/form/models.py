from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    
    class Meta:
        db_table = "tb_user"
