# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from weixin.utils.common import wrap

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from food.utils.common import rand_str,timestamp,create_token,change_money
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


#后台添加菜品
class AddFoodView(View):
    def get(self,request):
        # group_list = [g for g in Groups.objects.filter(status__exact=1)]
        return render(request,'food/upload_food.html',{"group_list":[]})


    def post(self,request):
        try:
            active_url = request.POST["active_url"]  # 活动
            main_title = request.POST["main_title"]  # 主标题
            # active_sequence = request.POST["active_sequence"]  # 活动组内顺序
            secound_title = request.POST["secound_title"]  # 副标题
            active_img = request.POST["active_img"]  # 活动配图
            group_id = request.POST["group_id"]  # 分组id
            # active = Actives()
            # group = Groups.objects.get(group_id=group_id)
            # active.active_id = rand_str(10)
            # active.group = group
            # active.active_url = active_url
            # active.active_img = active_img
            # # active.active_sequence = active_sequence
            # active.create_time = datetime.datetime.now()
            # active.main_title = main_title
            # active.secound_title = secound_title
            # active.group_name = group.name
            # active.group_sequence = group.sequence
            # active.save()
            return JsonResponse({"status": 200, "data": request.POST})
        except BaseException, e:
            return JsonResponse({"error":str(e),"status":400})



#所有菜
#返回菜的名字，图片，月售多少份，好评率是多少
@wrap
def all_food(request, response, content):
    pass
