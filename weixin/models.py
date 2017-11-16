#encoding: utf-8
from django.db import models

# Create your models here.
class WxOrder(models.Model):
    user_id = models.CharField(verbose_name="用户id",max_length=50,blank=True,null=True)
    store_id = models.CharField(verbose_name="店铺id", max_length=50, blank=True, null=True)
    out_trade_no = models.CharField(max_length=255, blank=True, null=True,verbose_name="订单号")
    trade_type = models.CharField(max_length=45, blank=True, null=True,verbose_name="支付类型")
    money = models.DecimalField(max_digits=13, decimal_places=2, null=False, default=0.00,verbose_name="用户实际支付金额，不是以分为计算单位")
    mobile = models.CharField(max_length=45, blank=True, null=True,verbose_name="电话号码")
    status = models.IntegerField(null=True, blank=True,verbose_name="支付状态")  # 5000 等待付款 6000取消付款 9000付款成功
    subject = models.CharField(max_length=500, null=True, blank=True,verbose_name="微信规定的subject")
    body = models.CharField(max_length=500, null=True, blank=True,verbose_name="信息描述")
    appid = models.CharField(max_length=45, blank=True, null=True,verbose_name="公众账号ID")
    mch_id = models.CharField(max_length=45, blank=True, null=True,verbose_name="商户号")
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建微信订单时间')

    class Meta:
        managed = False
        db_table = 'wx_order'

class CarDayInfo(models.Model):
    car = models.CharField(max_length=55,verbose_name="车号",null=True,blank=True,default='')
    desc = models.CharField(max_length=55,verbose_name="车辆从哪到哪",null=True,blank=True,default='项城到郑州')
    site_number = models.CharField(max_length=512,verbose_name="座位数列表，是json字符串",null=True,blank=True,default="[]")
    virtual_time = models.CharField(max_length=512,verbose_name="虚拟时间，用作判断是否需要创建记录",null=True,blank=True,default="2017-11-16 6:00")
    real_time = models.DateTimeField(verbose_name="真实时间",auto_now_add=True,null=True,blank=True)

    class Meta:
        db_table = 'car_day_info'
        verbose_name = "车辆每日信息表"
