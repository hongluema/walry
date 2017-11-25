# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Store(models.Model):
    store_id = models.CharField(max_length=64,verbose_name="店铺id",primary_key=True)
    name = models.CharField(max_length=255,verbose_name="店铺名字",default="")
    desc = models.TextField(verbose_name="店铺简介",null=True,blank=True)
    create_time = models.DateTimeField(verbose_name="创建店铺时间",auto_now_add=True)
    storekeeper_id = models.CharField(max_length=64,verbose_name="店主id",default="")
    storekeeper_name = models.CharField(max_length=64,verbose_name="店主名字",default="")
    storekeeper_mobile = models.CharField(max_length=64,verbose_name="店主手机号",default="")
    is_delete = models.BooleanField(verbose_name="店是否删除",default=False)

    class Meta:
        verbose_name = "店铺表"
        db_table = "store"

class Group(models.Model):
    group_id = models.CharField(max_length=64,verbose_name="菜系id",primary_key=True)
    store_id = models.CharField(max_length=64,verbose_name="店铺id",null=False)
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
    store_id = models.CharField(max_length=64, verbose_name="店铺id", null=False)
    food_img = models.CharField(max_length=255,verbose_name="菜图片",default="")
    name = models.CharField(max_length=255,verbose_name="菜的名字",default="")
    desc = models.TextField(verbose_name="描述",null=True,blank=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, null=False, default=0.00,verbose_name="菜的金额，不是以分为计算单位")
    create_time = models.DateTimeField(verbose_name="添加时间",auto_now_add=True)
    sequence = models.IntegerField(verbose_name="默认菜系内排序",default=1)
    is_delete = models.BooleanField(verbose_name="是否逻辑删除了",default=False)

    class Meta:
        verbose_name = "菜单表"
        db_table = "food"

class FoodEvalute(models.Model):
    evalute = models.CharField(max_length=64,verbose_name="评价id",null=False,blank=False)
    food_id = models.CharField(max_length=64, verbose_name="菜的id", null=False,blank=False)
    group_id = models.CharField(max_length=64, verbose_name="菜系id", null=False, blank=False)
    store_id = models.CharField(max_length=64, verbose_name="店铺id", null=False)
    food_img = models.CharField(max_length=255, verbose_name="菜图片", default="")
    name = models.CharField(max_length=255, verbose_name="菜的名字", default="")
    content = models.TextField(verbose_name="评价内容", null=True, blank=True)
    create_time = models.DateTimeField(verbose_name="添加时间", auto_now_add=True)
    zan = models.IntegerField(verbose_name="赞的星数，默认是1",default=1)
    is_delete = models.BooleanField(verbose_name="是否逻辑删除了", default=False)

    class Meta:
        verbose_name = "评价表"
        db_table = "food_evalute"

class Order(models.Model):
    order_id = models.CharField(max_length=88,verbose_name="订单id",unique=True)
    store_id = models.CharField(max_length=64, verbose_name="店铺id", null=False)
    table = models.IntegerField(verbose_name="桌号",default=1)
    foods = models.TextField(verbose_name="已经点的菜列表",default="[]")
    customers = models.TextField(verbose_name="顾客列表",default="[]")
    create_time = models.DateTimeField(verbose_name="下单时间",auto_now_add=True)
    status = models.IntegerField(verbose_name="订单状态，5000是未下单，9000是已下单",default=5000)
    price = models.DecimalField(verbose_name="饭菜总金额",max_digits=13, decimal_places=2, null=False, default=0.00)
    is_delete = models.BooleanField(verbose_name="是否删除了订单",default=False)
    #订单表，状态  未下单  下单  相当于购物车

    class Meta:
        verbose_name = "订单表"
        db_table = "order"

# class Consume(models.Model):
    #消费流水表，可以获取月销售多少，openid，规格，
    # pass

#登录，收藏，

