# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from weixin.utils.common import wrap

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import datetime
from food.utils.common import rand_str,timestamp,create_token,change_money
from django.views.generic import View, TemplateView
import logging
# Create your views here.


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
