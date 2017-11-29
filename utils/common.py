from datetime import datetime
import time
import string
import random
from decimal import Decimal
import re

def timestamp(date_time):#将datetime时间类型转化为时间戳
    time_stamp = int(time.mktime(date_time.timetuple()))
    return time_stamp

# a = timestamp(datetime.now())

def rand_str(n):#用于生成优惠码，店铺id等
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in xrange(n))

def change_date(time):
    cover_time = datetime.strftime(time,"%Y-%m-%d %H:%M:%S")
    return cover_time

def rand_digit(n):#用于生成验证码
    return ''.join(random.choice(string.digits) for _ in xrange(n))

def change_money(money):#转换金额为decimal
    dmoney=Decimal(money).quantize(Decimal('0.00'))
    return dmoney

def change_lag_lng(lng_lag):#转换纬经度
    dlng_lag=Decimal(lng_lag).quantize(Decimal('0.000000000000000000'))
    return dlng_lag



def change_radio(radio):#转换利率
    r_s = radio.strip("%")
    r = change_money(r_s)/100
    return r