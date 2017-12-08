# encoding: utf-8

from django.shortcuts import render
import traceback
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta,date
import json
from food.utils.common import rand_str,timestamp,create_token,change_money
from django.views.generic import View, TemplateView
import logging

def cookie_get(request):
    print ">>>cookie: ",request.COOKIES
    print ">>>session: ",request.session
    sid = request.COOKIES["sid"]
    if sid == request.session["sid"]:
        print ">>>哈哈 获取的sid对的上，找到了登录的人"
    return HttpResponse("你好")

def cookie_set(request):
    resp = HttpResponse("设置cookie成功")
    sid = rand_str(12) #sessionId
    request.session["sid"] = sid
    resp.set_cookie("sid",sid)
    return resp



