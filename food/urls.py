#encoding: utf-8
from django.conf.urls import url
from . import views

app_name = "weixin"

urlpatterns = [
    url(r'^addFood/$', views.AddFoodView.as_view()),#添加菜
    url(r'^qiniu_token/$', views.qiniu_token),#七牛上传图片
]