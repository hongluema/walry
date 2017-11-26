# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from weixin.utils.common import wrap

from django.shortcuts import render
import traceback
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta,date
import json
from food.utils.common import rand_str,timestamp,create_token,change_money
from django.views.generic import View, TemplateView
from bus.models import RunLogging
# Create your views here.

"""
错误解决办法
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-13: ordinal not in range(128)
"""
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

#创建汽车运营流水记录
#"""每天每辆汽车分为上午11：00(zheng->xiang)，下午5：00(xiang->zheng)两个运营记录"""
class AddRunLoggingView(View):
    def get(self,request):
        return render(request,"bus/addRunLogging.html")

    def post(self,request):
        try:
            print ">>>request.POST", request.POST
            bus_number = request.POST["bus_number"] #车牌号
            real_money = request.POST["real_money"] #本趟到手金额
            other_money = request.POST["other_money"] #本趟其他花销
            sum_money = request.POST["sum_money"]  # 本趟总收入
            luxian = request.POST["luxian"] #路线
            bus_peoples = request.POST["peoples"] #车上人数
            driver = request.POST["driver"] #司机
            saler = request.POST["saler"] #售票员

            today = date.today()
            ts = today.strftime("%Y-%m-%d ")
            today_11dian_string = ts+"11:00:00"
            today_11dian = datetime.strptime(today_11dian_string,"%Y-%m-%d %H:%M:%S")
            today_17dian_string = ts+"17:00:00"
            today_17dian = datetime.strptime(today_17dian_string, "%Y-%m-%d %H:%M:%S")
            if luxian == "郑州到项城":
                time = today_11dian
                is_exist = RunLogging.objects.filter(time=time,bus_number=bus_number).first()
                if is_exist:
                    return JsonResponse({"status": 400, "errorMsg": str("已经添加过，无需重复添加记录")})
                run = RunLogging()
                run.run_id = rand_str(12)
                run.bus_number = bus_number
                run.driver = driver
                run.saler = saler
                run.bus_peoples = bus_peoples
                run.time = time
                run.real_money = change_money(real_money)
                run.other_money = change_money(other_money)
                run.sum_money = change_money(sum_money)
                run_xia = RunLogging.objects.filter(bus_number=bus_number, time=today_11dian).first()  # 下午的金额
                if run_xia:
                    xia_real_money = run_xia.real_money #实际到手的金额
                else:
                    xia_real_money = change_money(0.00)
                run.day_sum_money = change_money(real_money) + xia_real_money
                run.save()
            else:
                time = today_17dian
                is_exist = RunLogging.objects.filter(time=time, bus_number=bus_number).first()
                if is_exist:
                    return JsonResponse({"status": 400, "errorMsg": str("已经添加过，无需重复添加记录")})
                run = RunLogging()
                run.run_id = rand_str(12)
                run.bus_number = bus_number
                run.driver = driver
                run.saler = saler
                run.bus_peoples = bus_peoples
                run.time = time
                run.real_money = change_money(real_money)
                run.other_money = change_money(other_money)
                run.sum_money = change_money(sum_money)
                run_shang = RunLogging.objects.filter(bus_number=bus_number,time=today_11dian).first()#上午的金额
                if run_shang:
                    shang_real_money = run_shang.real_money
                else:
                    shang_real_money = change_money(0.00)
                run.day_sum_money = change_money(real_money) + shang_real_money
                run.save()
            print ">>>time:",time


            return JsonResponse({"status": 200})
        except Exception, e:
            traceback.print_exc()
            return JsonResponse({"status":500,"errorMsg":str(e)})

