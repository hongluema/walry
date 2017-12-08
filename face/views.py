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
from django.contrib.sessions.models import Session

def cookie_get(request):
    print ">>>cookie: ",request.COOKIES
    print ">>>session: ",request.session.session_key
    users_dict_session_key = Session.objects.all().values("session_key")
    #users_dict_session_key:[{'session_key': u'e5q61qzrxzlqi619a68xpcu0z0f1ma9b'},\
    # {'session_key': u'33thht7f8029rys25iu0hpkz25f4n8nu'},\
    # {'session_key': u'tlnodb8jcw0d1i3jdw4lv6tk3pxzg6yw'},\
    # {'session_key': u'nrto541f6zoadx9umatfpekywn2x3cgk'}]

    users_list_session_key = []

    for s in users_dict_session_key:
        print ">>> user session_key:",s
        users_list_session_key.append(s["session_key"])

    sid = request.COOKIES["sessionid"]
    if sid in users_list_session_key:
        print ">>>哈哈 获取的sessionid对的上，找到了登录的人"
    return HttpResponse("你好")

def cookie_set(request):
    resp = HttpResponse("设置cookie成功")
    sessionid = request.session.session_key
    resp.set_cookie("sid",sessionid)
    return resp



