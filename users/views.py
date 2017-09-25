# encoding: utf-8
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def userlogin(request):
    if request.method == "GET":
        return render(request,"users/login.html")
    elif request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        user = authenticate(username=username,password=password) #这里只是验证用户名和密码是否正确,但是并没有登录
        if user is not None:
            #用户名与密码匹配
            login(request,user) #登录
            """
            从login的源码可以看出，login()这个函数主要做了两步：
            1. request.session[SESSION_KEY] = user._meta.pk.value_to_string(user) #用户的信息存放在request.session里面
            2. request.user = user #将当前登录的对象放到request.user中
            """
            return HttpResponse("用户登录成功")
        else:
            #用户名与密码不匹配
            return HttpResponse("用户登录失败")


#验证当前请求的视图是否登录
@login_required #只要有这个装饰器，就需要会验证是否登录了，如果登录了就登录，如果没有就会要求登录
#需要去settings.py中设置一下LOGIN_URL
def hello(request):
    return HttpResponse("Hello!")