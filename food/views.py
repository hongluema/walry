# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from weixin.utils.common import wrap

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from food.utils.common import rand_str,timestamp,create_token,change_money
from food.models import Food, Group
from django.views.generic import View, TemplateView
import logging
# Create your views here.

#七牛上传图片
@csrf_exempt
def qiniu_token(request):
    status = {'status': 300, 'msg': '系统错误'}
    response = HttpResponse()
    try:
        # key = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        key = None
        policy = request.POST.get('policy', None)
        # if key:
        token = create_token('ksy-video', key, policy)
        status['status'] = 200
        status['info'] = token
        status['key'] = key
    except Exception, e:
        print str(e)
    response.content = json.dumps(status)
    response.content_type = 'application/json'
    return response

#后台添加菜系
class AddGroupView(View):
    def get(self,request):
        return render(request,'food/addGroup.html')


    def post(self,request):
        try:
            print ">>>request.POST",request.POST
            name = request.POST["group_name"]
            desc = request.POST["group_desc"]
            sequence = request.POST["group_sequence"]
            group = Group()
            group.group_id = rand_str(6)
            group.name = name
            group.desc = desc
            group.sequence = sequence
            group.create_time = datetime.datetime.now()
            group.save()
            return JsonResponse({"status": 200, "data": request.POST})
        except BaseException, e:
            return JsonResponse({"error":str(e),"status":400})

def createGroup_success(request):
    return HttpResponse(
        '恭喜您！创建菜系成功！<a href="https://zch.kuosanyun.com/activity/activeList/" class="btn btn-danger" role="button">回到首页</a>')

def createGroup_fail(request):
    return HttpResponse(
        '抱歉！创建菜系失败！<a href="https://zch.kuosanyun.com/activity/activeList/" class="btn btn-danger" role="button">回到首页</a>')


#后台添加菜品
class AddFoodView(View):
    def get(self,request):
        # group_list = [g for g in Groups.objects.filter(status__exact=1)]
        return render(request,'food/upload_food.html',{"group_list":[]})


    def post(self,request):
        try:
            print ">>>request.POST",request.POST
            food_img = request.POST["food_img"]  # 菜图片
            food_price = request.POST["food_price"]  # 菜价格
            food_name = request.POST["food_name"]  # 菜名字
            food_desc = request.POST["food_desc"]  # 活动配图
            group_id = request.POST["group_id"]  # 分组id
            food_id = rand_str(8)

            return JsonResponse({"status": 200, "data": request.POST})
        except BaseException, e:
            return JsonResponse({"error":str(e),"status":400})

def createFood_success(request):
    return HttpResponse('恭喜您！创建活动成功！<a href="https://zch.kuosanyun.com/activity/activeList/" class="btn btn-danger" role="button">回到首页</a>')

def createFood_fail(request):
    return HttpResponse('抱歉！创建活动失败！<a href="https://zch.kuosanyun.com/activity/activeList/" class="btn btn-danger" role="button">回到首页</a>')

#所有菜
#返回菜的名字，图片，月售多少份，好评率是多少
@wrap
def all_food(request, response, content):
    pass
