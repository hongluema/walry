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

# Create your views here.

#创建汽车运营流水记录
#"""每天每辆汽车分为上午11：00(zheng->xiang)，下午5：00(xiang->zheng)两个运营记录"""
class AddRunLoggingView(View):
    def get(self,request):
        return render(request,"bus/addRunLogging.html")

    def post(self,request):
        try:
            print ">>>request.POST", request.POST
            """
            bus_number = request.POST("bus_number")
            money = request.POST("money")
            time = request.POST("time")
            bus_peoples = request.POST("bus_peoples")
            driver = request.POST("driver")
            saler = request.POST("saler")
            today = date.today()
            ts = today.strftime("%Y-%m-%d ")
            today_11dian_string = ts+"11:00:00"
            today_11dian = datetime.strptime(today_11dian_string,"%Y-%m-%d %H:%M:%S")
            today_17dian_string = ts+"17:00:00"
            today_17dian = datetime.strptime(today_17dian_string, "%Y-%m-%d %H:%M:%S")
            """
            return JsonResponse({"status": 200})
        except Exception, e:
            return JsonResponse({"status":500,"errorMsg":str(e)})
            traceback.print_exc()