# encoding: utf-8
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View

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
            return HttpResponseRedirect(request.GET.get("next",'/')) #登录成功后跳转next的页面，没有next就跳转首页
        else:
            #用户名与密码不匹配
            return HttpResponse("用户登录失败")


#验证当前请求的视图是否登录
@login_required #只要有这个装饰器，就需要会验证是否登录了，如果登录了就登录，如果没有就会要求登录
#需要去settings.py中设置一下LOGIN_URL
def hello(request):
    return HttpResponse("Hello!")

#退出登录
def userlogout(request):
    logout(request)
    """
    从logout的源码可以看出，logout()这个函数主要做了两步：
    1. request.session.flush()  #清空了session
    2. request.user = AnonymousUser() #设置当前登录成功的用户为游客
    """
    return HttpResponse("退出登录！")


class UserView(View):

    def get(self,request):
        #get请求将执行这个函数
        return render(request,'users/create.html')

    def post(self,request):
        #post请求将执行这个函数
        pass