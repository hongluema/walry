# encoding: utf-8
from django.conf.urls import url
from users import views

app_name = "users"

urlpatterns = [
    url(r'^login/',views.userlogin,name='login'), #用户登录验证
    url(r'^hello/',views.hello,name='hello'), #hello
]
