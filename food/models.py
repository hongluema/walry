# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Group(models.Model):
    group_id = models.CharField(max_length=64,verbose_name="菜系id",primary_key=True)
    name = models.CharField(max_length=255, verbose_name="菜系的名字", default="")
    desc = models.TextField(verbose_name="描述", null=True,blank=True)
    create_time = models.DateTimeField(verbose_name="添加时间", auto_now_add=True)
    sequence = models.IntegerField(verbose_name="默认排序", default=1)
    is_delete = models.BooleanField(verbose_name="是否逻辑删除了", default=False)

    class Meta:
        verbose_name = "菜系表"
        db_table = "group"

class Food(models.Model):
    food_id = models.CharField(max_length=64,verbose_name="菜的id",primary_key=True)
    group_id = models.CharField(max_length=64,verbose_name="菜系id",null=False,blank=False)
    food_img = models.CharField(max_length=255,verbose_name="菜图片",default="")
    name = models.CharField(max_length=255,verbose_name="菜的名字",default="")
    desc = models.TextField(verbose_name="描述",null=True,blank=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, null=False, default=0.00,verbose_name="用户实际支付金额，不是以分为计算单位")
    create_time = models.DateTimeField(verbose_name="添加时间",auto_now_add=True)
    sequence = models.IntegerField(verbose_name="默认菜系内排序",default=1)
    is_delete = models.BooleanField(verbose_name="是否逻辑删除了",default=False)

    class Meta:
        verbose_name = "菜单表"
        db_table = "food"

