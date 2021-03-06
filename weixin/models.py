#encoding: utf-8
from django.db import models

# Create your models here.
class CarDayInfo(models.Model):
    car = models.CharField(max_length=55,verbose_name="车号",null=True,blank=True,default='')
    desc = models.CharField(max_length=55,verbose_name="车辆从哪到哪",null=True,blank=True,default='项城到郑州')
    site_number = models.CharField(max_length=512,verbose_name="座位数列表，是json字符串",null=True,blank=True,default="[]")
    sates_info = models.TextField(verbose_name="座位信息",null=True,blank=True)
    virtual_time = models.CharField(max_length=512,verbose_name="虚拟时间，用作判断是否需要创建记录",null=True,blank=True,default="2017-11-16 6:00")
    real_time = models.DateTimeField(verbose_name="真实时间",auto_now_add=True,null=True,blank=True)


    class Meta:
        db_table = 'car_day_info'
        verbose_name = "车辆每日信息表"

class WxInfo(models.Model):
    openid = models.CharField(max_length=150, blank=True, null=True)
    nickname = models.CharField(max_length=155, blank=True, null=True,default='')
    sex = models.IntegerField(blank=True, null=True,default=1,verbose_name="1是男，2是女")
    province = models.CharField(max_length=45, blank=True, null=True,default='')
    city = models.CharField(max_length=45, blank=True, null=True,default='')
    country = models.CharField(max_length=45, blank=True, null=True,default='')
    language = models.CharField(max_length=45, blank=True, null=True,default='')
    headimgurl = models.CharField(max_length=512, blank=True, null=True,default='')
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建微信记录时间')

    class Meta:
        db_table = "wx_info"
        verbose_name = "微信信息表"



