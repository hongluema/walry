# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from weixin.utils.common import wrap

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime, timedelta
from food.utils.common import rand_str,timestamp,create_token,change_money
from food.models import Food, Group, Store, Order, FoodEvalute
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
            group.create_time = datetime.now()
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
        group_list = [g for g in Group.objects.filter(is_delete=0)]
        return render(request,'food/upload_food.html',{"group_list":group_list})


    def post(self,request):
        try:
            print ">>>request.POST",request.POST
            food_img = request.POST["food_img"]  # 菜图片
            food_price = request.POST["food_price"]  # 菜价格
            food_name = request.POST["food_name"]  # 菜名字
            food_desc = request.POST["food_desc"]  # 活动配图
            group_id = request.POST["group_id"]  # 分组id
            food_id = rand_str(8)
            food = Food()
            food.food_id = food_id
            food.name = food_name
            food.group_id = group_id
            food.food_img = food_img
            food.desc = food_desc
            food.price = food_price
            food.create_time = datetime.now()
            food.save()
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

#大家共同点菜系统
"""
原理：
    1.先判断该桌是下过单还是未下单，
    2.判断扫码的人是否已经扫过该桌，
    customers = json.loads(customers) if customers else []
    foods = json.loads(foods) if foods else []
    cart = {"wecxada":number,"asdasddf":number}
        for i in cart:
            food = Food.objects.filter(food_id = i).first()
            if food:
                food_info = {"food_img":food.food_img,"name":food.name,\
                "price":food.price,"number":cart[i]}
            foods.append(food_info)
            
            
    #展示菜单
    food_id = request.POST["food_id"] #菜id
    number = request.POST["number"] #菜数量
    table = request.POST["table"] #桌号
    openid = request.POST["openid"] #用户openid
    is_order = Order.objects.filter(table=table,status=9000,customers__contains=openid).order_by("-create_time").first()
    if is_order: #本桌已经下过单
        order = Order.objects.filter(table=table,status=9000).order_by("-create_time").first()
        customers = json.loads(order.customers) #所有未下单时扫过码的顾客
        if openid in customers: #在最近一次就餐的客人中有该用户信息，认为是加菜
            foods = json.loads(order.foods) #已经点过的菜信息
            menu_info #菜单信息
        else: #默认为是新的一桌客人
            menu_info #菜单信息
        
    else: #本桌未下单,但是菜加入购物车
        order = Order.objects.filter(table=table,status=5000).order_by("-create_time").first()
        if order: #已经有人把菜加入购物车了，但是还没下单
            customers.append(openid)
            cart = json.loads(order.cart) #购物车
            cart.update({food_id:number})
            customers = json.loads(order.customers) #顾客
            customers.append(openid)
            order.cart = cart
            order.customers = customers
            order.save()
            
            info = {"food_id":food_id,"price":str(food_id.price*number),\
            ...}
            return info
            # 小程序本地存储购物车
            # cart = {"wecxada":number,"asdasddf":number}
        else: #还没有人把菜加入购物车
            new_order = Order()
            new_order.order_id = rand_str(12)
            new_order.store_id = ""
            new_order.table = int(table)
            new_order.status = 5000
            new_order.cart = {food_id:number}
            new_order.customers = [].append(openid)
            new_order.create_time = datetime.now()
            new_order.is_delete = 0
            new_order.save()
            info = {"food_id":food_id,"price":str(food_id.price*number),\
            ...}
            return info
            
"""
#<1> 第一个人点菜，加入购物车，创建订单，openid加入customers ，条件：openid not in customers ,status=9000, table=table
#<2> 其他人点菜加入购物车,不创建订单，openid加入customers，条件：status=5000,table=table
#<3> 下单 条件：status=5000,table=table
#<4> 老用户加菜， 条件：status=9000,table=table,openid in customers
@wrap
def show_order(request, response, content):
    # 展示菜单
    food_id = request.POST["food_id"]  # 菜id
    number = int(request.POST["number"])  # 菜数量
    table = request.POST["table"]  # 桌号
    openid = request.POST["openid"]  # 用户openid
    order = Order.objects.filter(table=table, status=9000).order_by("-create_time").first() #该桌最近一次订单是否已经下过单
    if order:  # 本桌已经下过单
        # order = Order.objects.filter(table=table, status=9000).order_by("-create_time").first()
        customers = json.loads(order.customers)  # 所有未下单时扫过码的顾客
        if openid in customers:  # 在最近一次就餐的客人中有该用户信息，认为是加菜
            foods = json.loads(order.foods)  # 已经点过的菜信息
            menu_info = "menu_info"  # 菜单信息
            content["menu_info"] = menu_info
        else:  # 默认为是新的一桌客人
            new_order = Order()
            new_order.order_id = rand_str(12)
            new_order.store_id = "暂不设定"
            new_order.table = int(table)
            new_order.status = 5000
            new_order.cart = {food_id: number}
            new_order.customers = [].append(openid)
            new_order.create_time = datetime.now()
            new_order.is_delete = 0
            new_order.save()
            food = Food.objects.get(food_id=food_id)
            info = {"food_id": food_id, "price": str(food.price * number)}
            content["infp"] = info
    else:
        order = Order.objects.filter(table=table, status=5000).order_by("-create_time").first()
        if order:  # 已经有人把菜加入购物车了，但是还没下单
            customers = json.loads(order.customers)
            customers.append(openid)
            print ">>>order.cart",order.cart
            cart = json.loads(order.cart)  # 购物车
            is_tixing = request.POST.get("is_tixing",0)
            if food_id in cart:
                if not is_tixing:
                    print "您已经点过该菜，请确认是否再点一份"
                else:
                    cart[food_id] = cart[food_id] + number
            else:
                cart.update({food_id: number})
            customers = json.loads(order.customers)  # 顾客
            if openid not in customers:
                customers.append(openid)
            order.cart = json.dumps(cart)
            order.customers = json.dumps(customers)
            order.save()
            food = Food.objects.get(food_id=food_id)
            info = {"food_id": food_id, "price": str(food.price * number)}
            content["info"] = info
            # return content
            # 小程序本地存储购物车
            # cart = {"wecxada":number,"asdasddf":number}
        else:  # 还没有人把菜加入购物车
            new_order = Order()
            new_order.order_id = rand_str(12)
            new_order.store_id = "暂不设定"
            new_order.table = int(table)
            new_order.status = 5000
            new_order.cart = json.dumps({food_id: number})
            customers = []
            customers.append(openid)
            new_order.customers = json.dumps(customers)
            new_order.create_time = datetime.now()
            new_order.is_delete = 0
            new_order.save()
            food = Food.objects.get(food_id=food_id)
            info = {"food_id": food_id, "price": str(food.price * number)}
            content["infp"] = info

@wrap
def to_order(request,response,content):
    store_id = request.POST["store_id"]  #店铺id
    table = int(request.POST["table"])  #桌号，int类型
    opneid = request.POST["openid"]
    three_hours = datetime.now() - timedelta(hours=3) #三个小时之前
    not_end = Order.objects.filter(table=table,customs_contains = opneid,create_time__gte=three_hours).order_by("-create_time").first() #判断是不是同一桌，
    #如果三个小时内找到了该openid在该桌上消费过，就自动默认为是这顿饭还没吃完
    if not_end: #还没吃完呢
        foods = json.loads(not_end.foods) #已经点过的菜单
    else: #已经吃完了
        order = Order.objects.filter(table=table)
        order.table = table
        order.customers = []

@wrap #RESTFUL风格的测试用例
def cais(request,response,content):
    if request.method == "GET": #查询
        if request.GET:
            food_id = request.GET["food_id"]
            f = Food.objects.filter(food_id=food_id).first()
            info = {"name":f.name,"price":str(f.price)}
            content["info"] = info
        else:
            foods = Food.objects.filter(is_delete=0)
            info = [{"name":f.name,"price":str(f.price)} for f in foods]
            content["info"] = info
    elif request.method == "POST": #添加
        group_id = request.POST["group_id"]
        store_id = request.POST["store_id"]
        name = request.POST["name"]
        desc = request.POST["desc"]
        food_img = request.POST["food_img"]
        price = request.POST["price"]
        sequence = int(request.POST.get("sequence",1))
        is_delete = int(request.POST.get("is_delete",0))
        food = Food()
        food.food_id = rand_str(8)
        food.group_id = group_id
        food.store_id = store_id
        food.name = name
        food.desc = desc
        food.food_img = food_img
        food.price = change_money(price)
        food.sequence = sequence
        food.is_delete = is_delete
        food.save()
        content["info"] = {"msg":"成功"}
    elif request.method == "PUT": #修改
        put = QueryDict(request.body)
        food_id = put["food_id"]
        name = request.PUT["name"]
        food = Food.objects.filter(food_id=food_id,is_delete=0).first()
        food.name = name
        food.save()
        info = {"msg":"更新名字成功","name":name}
        content["info"] = info
    elif request.method == "DELETE": #删除
        delete = QueryDict(request.body)
        food_id = delete["food_id"]
        food = Food.objects.filter(food_id=food_id,is_delete=0).first()
        food.is_delete = 1
        food.save()
        info = {"msg": "菜删除成功"}
        content["info"] = info



