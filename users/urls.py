# encoding: utf-8
from django.conf.urls import url
from users import views

app_name = "users"

urlpatterns = [
    url(r'^login/$',views.userlogin,name='login'), #用户登录验证
    url(r'^logout/$',views.userlogout,name='logout'), #用户退出登录
    url(r'^hello/$',views.hello,name='hello'), #hello
    url(r'^user/$',views.UserView.as_view()), #user注册
    url(r'^userList/$',views.UserListView.as_view()), #userlist
]
