#encoding: utf-8
from django.shortcuts import render
import MySQLdb
from MySQLdb.cursors import DictCursor
from django.http import JsonResponse
import traceback
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from weixin.utils.common import wrap, code_token_
from weixin.models import CarDayInfo, WxInfo
from datetime import datetime
import requests
# Create your views here.


def find_task(request):
    if request.method == "POST":
        user_id = request.POST["uid"]
        conn = MySQLdb.connect(host="570ddef683032.sh.cdb.myqcloud.com", user='root', passwd='N205U89KSY8X', port=5394)
        cursor = conn.cursor(DictCursor)
        cursor.execute("use community")
        sql = "select * from message where user_id=%s"
        cursor.execute(sql, (user_id,))
        tasks = cursor.fetchall()
        cursor.close()
        conn.close()
        # for t in tasks:
        #     print "start..."
        #     print ">>>id:", t["id"], "uid:", t["user_id"], "时间：", t["pub_time"], "剩余金额：", t["r_amount"], "总金额:", t[
        #         "t_amount"]
        return render(request,'weixin/findTask.html',{"tasks":tasks})
    else:
        return render(request, 'weixin/findTask.html')

def delete_task(request):
    id = request.GET["id"]
    print "id:",id
    conn = MySQLdb.connect(host="570ddef683032.sh.cdb.myqcloud.com", user='root', passwd='N205U89KSY8X', port=5394)
    cursor = conn.cursor(DictCursor)
    cursor.execute("use community")
    sql = "update from message set status = 2 where id=%s"
    cursor.execute(sql, (id,))
    task = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return JsonResponse({"status":200,"task":task})

def recover_task(request):
    id = request.GET["id"]
    conn = MySQLdb.connect(host="570ddef683032.sh.cdb.myqcloud.com", user='root', passwd='N205U89KSY8X', port=5394)
    cursor = conn.cursor(DictCursor)
    cursor.execute("use community")
    sql = "update from message set status = 1 where id=%s"
    cursor.execute(sql, (id,))
    task = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return JsonResponse({"status":200,"task":task})

#展示座位的页面
@csrf_exempt
def show_zuowei(request):
    print ">>>request.POST",request.POST
    status = {'status': 300, "data": "", "msg": ""}
    response = HttpResponse(content_type='application/json')
    try:
        car_number = request.POST.get("carNumber","") #车牌号
        zuowei = request.POST.get("zuowei","") #车牌号
        cdis = CarDayInfo.objects.filter(car=car_number)
        if cdis:
            cdi = cdis[0]
            sates = json.loads(cdi.sates_info)
            for i in sates:
                if i == zuowei:
                    sates[i] = "../../images/sate_true.png"
            cdi.sates_info = json.dumps(sates)
            cdi.save()
        else:
            cdi = CarDayInfo()
            cdi.car = car_number
            cdi.virtual_time = datetime.strptime("2017-11-23 00:00:00","%Y-%m-%d %H:%M:%S")
            cdi.real_time = datetime.now()
            sates = {}
            for i in range(1,63):
                k = "zuowei"+str(i)
                v = "../../images/sate.png"
                sates.update({k:v})
            cdi.sates_info = json.dumps(sates)
            cdi.save()
        status["status"] = 200
        status["msg"] = "测试"
        status["data"] = sates
    except BaseException, e:
        traceback.print_exc()
        status["msg"] = "服务器错误"
    response.content = json.dumps(status)
    response["Access-Control-Allow-Origin"] = "*"
    return response

#创建车辆每日运营记录
@wrap
def create_log(requst,response,content):

    content["msg"] = "你好"


#根据地理位置进行智能搜索
@wrap
def find_location(request,response,content):
    pass

#通过微信code来获取openid
@wrap
def get_code(request,response,content):
    code = request.POST.get("code","")
    if code:
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=wx39fac537e9c5bad9&secret=5ea1112304709f9eb056702cbabb9ab3&js_code={code}&grant_type=authorization_codetest.com/onLogin'.format(code=code)
        r = requests.post(url)
        res = r.text.encode('unicode-escape').decode('string_escape')
        res = json.loads(res)
        content["status"] = 200
        content["openid"] = res["openid"]
    else:
        content["status"] = 401
        content["msg"] = "未获取到code"

#获取微信用户信息
@wrap
def get_wx_info(request,response,content):
    userInfo = request.POST.get("userInfo","")
    openid = request.POST.get("openid","")
    userInfo = json.loads(userInfo)
    wx_info = WxInfo.objects.filter(openid=openid).first()
    """
    ﻿注意 first() 是一个方便的方法，下面的代码示例等同于上面的例子:
    try:
        wx_info = WxInfo.objects.filter(openid=openid)[0]
    except IndexError:
        wx_info = None
    """
    if not wx_info:
        wx_info = WxInfo()
    wx_info.openid = openid
    wx_info.nickname = userInfo['nickName']
    wx_info.headimgurl = userInfo['avatarUrl'].replace('\/', '/')
    wx_info.province = userInfo["province"]
    wx_info.language = userInfo["language"]
    wx_info.city = userInfo["city"]
    wx_info.country = userInfo["country"]
    wx_info.sex = userInfo["gender"]
    wx_info.create_time = datetime.now()
    wx_info.save()
    content["status"] = 200
    content["msg"] = "微信用户信息存入或更新成功"