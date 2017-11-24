#encoding: utf-8
from django.conf.urls import url
from . import views

app_name = "weixin"

urlpatterns = [
    url(r'^addGroup/$', views.AddGroupView.as_view()),#添加菜系
    url(r'^addFood/$', views.AddFoodView.as_view()),#添加菜
    url(r'^qiniu_token/$', views.qiniu_token),#七牛上传图片
    url(r'^createFoodSuccess/$', views.createFood_success),#添加成功
    url(r'^createFoodFail/$', views.createFood_fail),#添加失败
]