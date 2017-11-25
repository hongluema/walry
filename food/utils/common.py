#!/usr/bin/env python
# encoding: utf-8

import string
import random
import time
from decimal import Decimal

def rand_str(n):#用于生成活动id
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in xrange(n))

def timestamp(date_time):#将datetime时间类型转化为时间戳
    time_stamp = int(time.mktime(date_time.timetuple()))
    return time_stamp

def change_money(money):#转换金额为decimal
    dmoney=Decimal(money).quantize(Decimal('0.00'))
    return dmoney


# qiniu账号
qn_access_key = 'g6gLWr981vRItEilSfXsT-31adDnCS9Us2mYuUA9'
qn_secret_key = 'd8XvPYpaFC64ms0G_MDsCLOi-wcxRm7fKsjRiYEK'
from qiniu import Auth, urlsafe_base64_encode
def create_token(bucket_name, key, policy=None):
    access_key = qn_access_key
    secret_key = qn_secret_key
    q = Auth(access_key, secret_key)
    token = q.upload_token(bucket_name, key, 3600, policy)
    return token

