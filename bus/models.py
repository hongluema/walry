# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class RunLogging(models.Model):
    run_id = models.CharField(verbose_name="运营id，每天每车会有上午下午两次",max_length=66,primary_key=True)
    bus_number = models.CharField(verbose_name="车牌号，每天每车会有上午下午两次",max_length=66,null=True,blank=True,default="")
    driver = models.CharField(verbose_name="司机姓名，每天每车会有上午下午两次",max_length=66,null=True,blank=True,default="")
    saler = models.CharField(verbose_name="售票员姓名，每天每车会有上午下午两次",max_length=66,null=True,blank=True,default="")
    real_money = models.DecimalField(verbose_name="每趟实际到手金额",max_digits=13,decimal_places=2,null=False,default=0.00)
    other_money = models.DecimalField(verbose_name="每趟额外花销金额",max_digits=13,decimal_places=2,null=False,default=0.00)
    sum_money = models.DecimalField(verbose_name="每趟总金额",max_digits=13,decimal_places=2,null=False,default=0.00)
    time = models.DateTimeField(verbose_name="运营时间")
    bus_peoples = models.IntegerField(verbose_name="车上人数",null=True,default=0)
    day_sum_money = models.DecimalField(verbose_name="当日总金额",max_digits=13,decimal_places=2,null=False,default=0.00)

    class Meta:
        verbose_name = "运营记录表"
        db_table = "run_logging"




