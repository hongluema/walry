# encoding:utf-8
from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=50,verbose_name="用户名",null=True,blank=True)
    password = models.CharField(max_length=50,verbose_name="密码",null=True,blank=True)
    email = models.CharField(max_length=50,verbose_name="邮箱",null=True,blank=True)

    class Meta:
        db_table = "users" #用户表

    def __str__(self):
        return "创建用户{}".format(self.username)