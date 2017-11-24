#encoding: utf-8
from django.conf.urls import url
from . import views

app_name = "weixin"

urlpatterns = [
    url(r'^addFood/$', views.AddFoodView.as_view()),#添加菜
]